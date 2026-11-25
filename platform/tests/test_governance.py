from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, skipUnless
from unittest.mock import patch

from ai_sdlc_platform.action_evidence import VerifiedActionResult, VerifiedBuildProvenance
from ai_sdlc_platform.approval_engine import VerifiedApprover
from ai_sdlc_platform.constants import STAGES
from ai_sdlc_platform import governance
from ai_sdlc_platform.governance import GATES, load_approver_roles
from ai_sdlc_platform.workflow_engine import WorkflowEngine


class GovernanceTests(TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.project = root / "project"
        self.project.mkdir()
        self.state = root / "protected-state"
        self.credentials = {
            "po": VerifiedApprover("po-id", frozenset({"product_owner"}), True),
            "architect": VerifiedApprover("architect-id", frozenset({"solution_architect"}), True),
            "lead": VerifiedApprover("lead-id", frozenset({"tech_lead"}), True),
            "reviewer": VerifiedApprover("reviewer-id", frozenset({"reviewer"}), True),
            "qa": VerifiedApprover("qa-id", frozenset({"qa_lead"}), True),
            "both": VerifiedApprover("both-id", frozenset({"qa_lead", "product_owner"}), True),
            "release": VerifiedApprover("release-id", frozenset({"release_manager"}), True),
            "commander": VerifiedApprover("ic-id", frozenset({"incident_commander"}), True),
            "bot": VerifiedApprover("bot-id", frozenset({"product_owner"}), False),
            "officer": VerifiedApprover("compliance-id", frozenset({"compliance"}), True),
        }
        self.reviews = {}
        self.authorizations = {}
        self.claims = {}
        self.results = {}
        self.provenance = {}
        self.merge_commit = "merged-commit"
        self.rev_a = sha256(b"artifact A").hexdigest()
        self.rev_b = sha256(b"artifact B").hexdigest()
        self.context_a = sha256(b"review bundle A").hexdigest()
        self.context_b = sha256(b"review bundle B").hexdigest()
        self.targets = {
            "G4": {"repository": "repo/example", "pull_request": "42", "base_ref": "refs/heads/main"},
            "G6": {"environment": "production-eu"},
            "G7": {"incident_ref": "INC-001"},
        }
        self.provenance.update({digest: VerifiedBuildProvenance("repo/example", self.merge_commit, digest)
                                for digest in (self.rev_a, self.rev_b)})
        self.engine = self.new_engine()
        self.run = self.engine.start()["execution_id"]

    def new_engine(self, **kwargs):
        options = {"verify_action_result": lambda gate, ref: self.results.get((gate, ref)),
                   "verify_build_provenance": self.provenance.get,
                   "can_approve": lambda identity, role, scope: scope.project == self.project, **kwargs}
        return WorkflowEngine(self.project, state_dir=self.state, verify_identity=self.credentials.get, **options)

    def review(self, gate, digest=None, authors=("author-id",), run=None, *, context=None,
               target=None, artifact_refs=("artifact:ref",), provenance_ref=None):
        key = (run or self.run, gate)
        digest = digest or self.rev_a
        review = self.engine.request_review(*key, artifact_sha256=digest,
                                            review_context_sha256=context or self.context_a,
                                            author_ids=authors, actor="pipeline", artifact_refs=artifact_refs,
                                            target=target if target is not None else self.targets.get(gate),
                                            provenance_ref=provenance_ref or (digest if gate == "G5" else None))
        self.reviews[key] = review
        return review

    def approve(self, gate, token, role, digest=None, run=None, decision="approved", review_id=None):
        key = (run or self.run, gate)
        return self.engine.approvals.approve(*key, token, decision, role=role,
                                             review_id=review_id or self.reviews[key]["event_id"],
                                             artifact_sha256=digest or self.rev_a,
                                             comment="Decision reason", evidence_refs=["report:ref"])

    def complete(self, stage_index, digest=None, *, result_ref=None, **overrides):
        gate = {0: "G1", 1: "G2", 2: "G3", 5: "G5"}.get(stage_index)
        review = self.reviews.get((self.run, gate), {})
        args = {"review_id": review.get("event_id"), "review_context_sha256": review.get("review_context_sha256"),
                **overrides}
        return self.engine.complete_stage(self.run, STAGES[stage_index], artifact_sha256=digest,
                                          action_result_ref=result_ref, **args)

    def claim(self, gate, authorization=None):
        action = authorization or self.authorizations[gate]
        claim = self.engine.check_action_start(action["execution_id"], gate, authorization_id=action["event_id"],
                                               artifact_sha256=action["artifact_sha256"],
                                               review_context_sha256=action["review_context_sha256"],
                                               target=action["target"])
        self.claims[action["event_id"]] = claim["event_id"]
        return claim

    def record_result(self, gate, **changes):
        authorization = self.authorizations[gate]
        result = VerifiedActionResult(authorization["event_id"], authorization["artifact_sha256"],
                                      authorization["target"], True, self.merge_commit if gate == "G4" else None,
                                      start_event_id=self.claims.get(authorization["event_id"]))
        ref = f"receipt:{gate}"
        self.results[gate, ref] = replace(result, **changes)
        return ref

    def advance_to_code_review(self):
        for index, (gate, token, role) in enumerate([
            ("G1", "po", "product_owner"), ("G2", "architect", "solution_architect"),
            ("G3", "lead", "tech_lead"),
        ]):
            self.review(gate)
            self.approve(gate, token, role)
            self.assertEqual(self.complete(index, self.rev_a)["next_stage"], STAGES[index + 1])
        self.assertEqual(self.complete(3)["next_stage"], STAGES[4])

    def advance_to_qa(self):
        self.advance_to_code_review()
        self.review("G4")
        self.approve("G4", "reviewer", "reviewer")
        self.authorize("G4")
        self.claim("G4")
        self.complete(4, self.rev_a, result_ref=self.record_result("G4"))

    def authorize(self, gate, digest=None, run=None, *, engine=None, **overrides):
        key = (run or self.run, gate)
        review = self.reviews[key]
        args = {"artifact_sha256": digest or review["artifact_sha256"], "review_id": review["event_id"],
                "review_context_sha256": review["review_context_sha256"], "target": review["target"],
                **overrides}
        result = (engine or self.engine).authorize_action(*key, **args)
        if result["status"] == "authorized":
            self.authorizations[gate] = result
        return result

    def test_blocks_non_initial_unknown_skipped_and_duplicate_stages_after_restart(self):
        with self.assertRaisesRegex(ValueError, "must start"):
            self.engine.start(STAGES[3])
        with self.assertRaisesRegex(ValueError, "Unknown SDLC execution"):
            self.engine.complete_stage("missing", STAGES[0])
        with self.assertRaisesRegex(ValueError, "active stage"):
            self.complete(7)
        with self.assertRaisesRegex(ValueError, "not available"):
            self.review("G4")
        self.review("G1")
        self.assertEqual(self.complete(0, self.rev_a)["status"], "awaiting_approval")
        self.approve("G1", "po", "product_owner")
        self.engine = self.new_engine()
        self.assertEqual(self.complete(0, self.rev_a)["next_stage"], STAGES[1])
        with self.assertRaisesRegex(ValueError, "active stage"):
            self.complete(0, self.rev_a)
        with self.assertRaisesRegex(ValueError, "review is closed"):
            self.approve("G1", "po", "product_owner")

    def test_rejects_unverified_nonhuman_wrong_role_and_self_approval(self):
        self.review("G1", authors=("po-id",))
        for token in ("unknown", "bot", "reviewer", "po"):
            with self.subTest(token=token), self.assertRaises(PermissionError):
                self.approve("G1", token, "product_owner")
        self.engine = WorkflowEngine(self.project, state_dir=self.state)
        with self.assertRaisesRegex(PermissionError, "verified human"):
            self.approve("G1", "po", "product_owner")
        self.assertEqual(self.complete(0, self.rev_a)["status"], "awaiting_approval")

    def test_revision_change_invalidates_prior_decisions_even_if_reverted(self):
        first_review = self.review("G1")
        self.assertEqual(self.review("G1")["event_id"], first_review["event_id"])
        with self.assertRaisesRegex(ValueError, "metadata"):
            self.review("G1", authors=("different-author",))
        self.approve("G1", "po", "product_owner")
        self.review("G1", self.rev_b)
        with self.assertRaisesRegex(ValueError, "No active"):
            self.approve("G1", "po", "product_owner", self.rev_a)
        self.assertEqual(self.complete(0, self.rev_b)["status"], "awaiting_approval")
        self.assertNotEqual(self.review("G1", self.rev_a)["event_id"], first_review["event_id"])
        with self.assertRaisesRegex(ValueError, "review ID is no longer active"):
            self.approve("G1", "po", "product_owner", review_id=first_review["event_id"])
        self.assertEqual(self.complete(0, self.rev_a)["status"], "awaiting_approval")

    def test_full_sdlc_requires_g4_before_merge_g5_from_two_people_and_g6_before_deploy(self):
        self.advance_to_code_review()
        self.review("G4")
        self.assertEqual(self.authorize("G4")["status"], "awaiting_approval")
        self.approve("G4", "reviewer", "reviewer")
        with self.assertRaisesRegex(ValueError, "Authorize merge"):
            self.complete(4, self.rev_a)
        self.assertEqual(self.authorize("G4")["action"], "merge")
        with self.assertRaisesRegex(ValueError, "already authorized"):
            self.authorize("G4")
        self.claim("G4")
        self.complete(4, self.rev_a, result_ref=self.record_result("G4"))
        self.review("G5")
        self.approve("G5", "both", "qa_lead")
        self.approve("G5", "both", "product_owner")
        self.assertEqual(self.complete(5, self.rev_a)["status"], "awaiting_approval")
        self.approve("G5", "qa", "qa_lead")
        self.assertEqual(self.complete(5, self.rev_a)["next_stage"], STAGES[6])
        with self.assertRaisesRegex(ValueError, "cleared by G5"):
            self.review("G6", self.rev_b)
        self.review("G6")
        with self.assertRaises(PermissionError):
            self.approve("G6", "commander", "incident_commander")
        self.approve("G6", "release", "release_manager")
        with self.assertRaisesRegex(ValueError, "Authorize deploy_production"):
            self.complete(6, self.rev_a)
        self.assertEqual(self.authorize("G6")["action"], "deploy_production")
        with self.assertRaisesRegex(ValueError, "for this revision"):
            self.complete(6, self.rev_b)
        self.claim("G6")
        result_ref = self.record_result("G6")
        self.assertEqual(self.complete(6, self.rev_a, result_ref=result_ref)["next_stage"], STAGES[7])
        self.assertIsNone(self.complete(7)["next_stage"])
        with self.assertRaisesRegex(ValueError, "active stage"):
            self.complete(7)

    def test_g7_only_on_critical_incident_and_requires_incident_commander(self):
        with self.assertRaisesRegex(ValueError, "critical incident execution"):
            self.review("G7")
        incident = self.engine.start_critical_incident(incident_ref="INC-001")["execution_id"]
        with self.assertRaisesRegex(ValueError, "match the incident execution"):
            self.review("G7", run=incident, target={"incident_ref": "INC-002"})
        self.review("G7", run=incident)
        self.assertEqual(self.authorize("G7", run=incident)["status"], "awaiting_approval")
        with self.assertRaises(PermissionError):
            self.approve("G7", "release", "release_manager", run=incident)
        self.approve("G7", "commander", "incident_commander", run=incident)
        action = self.authorize("G7", run=incident)
        self.assertEqual(action["action"], "respond_to_critical_incident")
        self.assertEqual(action["target"], {"incident_ref": "INC-001"})
        with self.assertRaisesRegex(ValueError, "Unknown SDLC execution"):
            self.engine.complete_stage(incident, STAGES[7])

    def test_project_policy_rejects_waivers_invalid_roles_and_missing_g5_role(self):
        path = self.project / ".ai-sdlc" / "approval-policy.yaml"
        path.parent.mkdir()
        invalid = ["G1: {required: false}", "G1: {required: null}", "G1: {required: 1}",
                   "G1: {approver_roles: [developer]}", "G5: {approver_roles: [qa_lead]}",
                   "G7: {approver_roles: incident_commander}", "G8: {required: true}"]
        for override in invalid:
            with self.subTest(override=override), self.assertRaises(ValueError):
                path.write_text(f"gates:\n  {override}\n", encoding="utf-8")
                load_approver_roles(self.project)
        path.write_text("gates:\n  G4: {approver_roles: [tech_lead]}\n", encoding="utf-8")
        self.advance_to_code_review()
        self.review("G4")
        with self.assertRaises(PermissionError):
            self.approve("G4", "reviewer", "reviewer")
        self.approve("G4", "lead", "tech_lead")
        self.assertEqual(self.authorize("G4")["status"], "authorized")

    def test_symlinked_approval_policy_blocks_new_reviews(self):
        policy = self.project / ".ai-sdlc" / "approval-policy.yaml"
        policy.parent.mkdir()
        target = self.project.parent / "external-policy.yaml"
        try:
            policy.symlink_to(target)
        except (NotImplementedError, OSError) as error:
            self.skipTest(f"Cannot create policy symlink: {error}")
        with self.assertRaisesRegex(ValueError, "Approval policy must be a regular file"):
            self.review("G1")
        target.write_text("gates: {}\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Approval policy must be a regular file"):
            self.review("G1")

        # A missing policy entry, unlike a symlink, permits defaults.
        policy.unlink()
        self.assertEqual(self.review("G1")["allowed_roles"], ["product_owner"])

    def test_symlinked_approval_policy_directory_blocks_new_reviews(self):
        config_dir = self.project / ".ai-sdlc"
        target = self.project.parent / "external-config"
        try:
            config_dir.symlink_to(target, target_is_directory=True)
        except (NotImplementedError, OSError) as error:
            self.skipTest(f"Cannot create directory symlink: {error}")

        with self.assertRaisesRegex(ValueError, "Approval policy directory must be a real directory"):
            self.review("G1")
        target.mkdir()
        with self.assertRaisesRegex(ValueError, "Approval policy directory must be a real directory"):
            self.review("G1")

        config_dir.unlink()
        self.assertEqual(self.review("G1")["allowed_roles"], ["product_owner"])

    def test_path_based_policy_reader_matches_descriptor_reader(self):
        policy = self.project / ".ai-sdlc" / "approval-policy.yaml"
        policy.parent.mkdir()
        policy.write_text("gates:\n  G4: {approver_roles: [tech_lead]}\n", encoding="utf-8")
        expected = load_approver_roles(self.project)
        self.assertEqual(expected["G4"], frozenset({"tech_lead"}))

        with patch.object(governance.os, "supports_dir_fd", set()):
            self.assertEqual(load_approver_roles(self.project), expected)
            policy.unlink()
            self.assertEqual(load_approver_roles(self.project)["G4"], GATES["G4"].roles)
            policy.symlink_to(self.project.parent / "external-policy.yaml")
            with self.assertRaisesRegex(ValueError, "Approval policy must be a regular file"):
                load_approver_roles(self.project)

    @skipUnless(hasattr(os, "O_PATH") and hasattr(os, "geteuid") and os.geteuid() != 0,
                "Requires O_PATH and a non-root user to exercise search-only directory access")
    def test_search_only_config_directory_is_readable_on_both_paths(self):
        policy = self.project / ".ai-sdlc" / "approval-policy.yaml"
        policy.parent.mkdir()
        policy.write_text("gates:\n  G4: {approver_roles: [tech_lead]}\n", encoding="utf-8")
        policy.parent.chmod(0o311)
        self.addCleanup(policy.parent.chmod, 0o755)
        expected = {**{gate_id: gate.roles for gate_id, gate in GATES.items()}, "G4": frozenset({"tech_lead"})}
        self.assertEqual(load_approver_roles(self.project), expected)
        with patch.object(governance.os, "supports_dir_fd", set()):
            self.assertEqual(load_approver_roles(self.project), expected)

    def test_policy_edit_cannot_remove_an_active_review_veto(self):
        self.advance_to_code_review()
        self.review("G4")
        self.approve("G4", "reviewer", "reviewer", decision="rejected")
        path = self.project / ".ai-sdlc" / "approval-policy.yaml"
        path.parent.mkdir()
        path.write_text("gates:\n  G4: {approver_roles: [tech_lead]}\n", encoding="utf-8")
        self.approve("G4", "lead", "tech_lead")
        self.assertEqual(self.authorize("G4")["status"], "blocked")
        self.review("G4", self.rev_b)
        with self.assertRaises(PermissionError):
            self.approve("G4", "reviewer", "reviewer", digest=self.rev_b)

    def test_g5_dual_signoff_cannot_be_waived(self):
        self.advance_to_qa()
        self.review("G5")
        self.engine = self.new_engine(can_authorize_exception=lambda identity, scope: True)
        with self.assertRaisesRegex(PermissionError, "not waivable"):
            self.engine.approvals.authorize_exception(
                self.run, "G5", "officer", review_id=self.reviews[self.run, "G5"]["event_id"],
                artifact_sha256=self.rev_a, reason="Exception", risk="Known risk",
                mitigation="Follow-up", owner="PM", evidence_refs=["ticket:ref"],
                expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
            )

    def test_sample_policy_matches_runtime(self):
        path = self.project / ".ai-sdlc" / "approval-policy.yaml"
        path.parent.mkdir()
        path.write_bytes((Path(__file__).resolve().parents[1] / "config-examples/gate-policy.yaml").read_bytes())
        self.assertEqual(load_approver_roles(self.project), {gate_id: gate.roles for gate_id, gate in GATES.items()})

    def exception(self, digest=None, token="officer"):
        return self.engine.approvals.authorize_exception(
            self.run, "G1", token, review_id=self.reviews[self.run, "G1"]["event_id"], artifact_sha256=digest or self.rev_a,
            reason="Documented exception", risk="Known risk",
            mitigation="Manual follow-up", owner="PM", evidence_refs=["ticket:ref"],
            expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
        )

    def test_exception_is_opt_in_revision_bound_expiring_and_audited(self):
        self.review("G1")
        with self.assertRaises(PermissionError):
            self.exception()
        self.engine = self.new_engine(can_authorize_exception=lambda identity, scope: (
            identity.subject == "compliance-id" and scope.gate == "G1"))
        with self.assertRaises(PermissionError):
            self.exception(token="po")
        self.exception()
        self.review("G1", self.rev_b)
        self.assertEqual(self.complete(0, self.rev_b)["status"], "awaiting_approval")
        exception = self.exception(self.rev_b)
        self.assertEqual(exception["scope"], f"complete:{STAGES[0]}")
        with self.assertRaisesRegex(ValueError, "already recorded"):
            self.exception(self.rev_b)
        with patch("ai_sdlc_platform.approval_engine.datetime", wraps=datetime) as clock:
            clock.now.return_value = datetime.now(timezone.utc) + timedelta(hours=2)
            self.assertEqual(self.complete(0, self.rev_b)["status"], "awaiting_approval")
        self.assertEqual(self.complete(0, self.rev_b)["status"], "completed")
        with self.engine.store.transaction() as conn:
            completion = self.engine.store.read(conn, self.run)[-1]
        self.assertEqual(completion["basis"], "exception_authorized")
        self.assertEqual(completion["decision_event_ids"], [exception["event_id"]])
        self.assertIn("timestamp", exception)

    def test_rejection_blocks_gate_even_with_exception_until_reviewer_revises_decision(self):
        self.engine = self.new_engine(can_authorize_exception=lambda identity, scope: True)
        self.review("G1")
        self.exception()
        self.approve("G1", "po", "product_owner", decision="rejected")
        self.assertEqual(self.complete(0, self.rev_a)["status"], "blocked")
        self.approve("G1", "po", "product_owner")
        self.assertEqual(self.complete(0, self.rev_a)["status"], "completed")

    def test_concurrent_action_authorization_only_succeeds_once(self):
        self.advance_to_code_review()
        self.review("G4")
        self.approve("G4", "reviewer", "reviewer")

        def attempt():
            try:
                return self.authorize("G4", engine=self.new_engine())["status"]
            except ValueError as error:
                return str(error)

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: attempt(), range(2)))
        self.assertCountEqual(results, ["authorized", "The G4 action is already authorized"])

    def advance_to_deployment(self, digest=None):
        self.advance_to_qa()
        self.sign_off_qa(digest or self.rev_a)

    def sign_off_qa(self, digest):
        self.review("G5", digest)
        self.approve("G5", "qa", "qa_lead", digest)
        self.approve("G5", "po", "product_owner", digest)
        self.assertEqual(self.complete(5, digest)["next_stage"], STAGES[6])

    def test_action_target_must_match_review_at_merge_and_production(self):
        self.advance_to_code_review()
        self.review("G4")
        self.approve("G4", "reviewer", "reviewer")
        for field, wrong in (("repository", "repo/other"), ("pull_request", "43"),
                             ("base_ref", "refs/heads/other")):
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "reviewed target"):
                self.authorize("G4", target={**self.targets["G4"], field: wrong})
        self.authorize("G4")
        self.claim("G4")
        self.complete(4, self.rev_a, result_ref=self.record_result("G4"))
        self.sign_off_qa(self.rev_a)
        self.review("G6")
        self.approve("G6", "release", "release_manager")
        with self.assertRaisesRegex(ValueError, "reviewed target"):
            self.authorize("G6", target={"environment": "production-us"})
        self.assertEqual(self.authorize("G6")["target"], self.targets["G6"])

    def test_completion_requires_verified_success_for_the_exact_authorization(self):
        self.advance_to_deployment()
        self.review("G6")
        self.approve("G6", "release", "release_manager")
        self.authorize("G6")
        with self.assertRaisesRegex(ValueError, "verified action result"):
            self.complete(6, self.rev_a)
        self.record_result("G6")
        with self.assertRaisesRegex(ValueError, "Claim the authorization"):
            self.complete(6, self.rev_a, result_ref="receipt:G6")
        self.claim("G6")
        with self.assertRaisesRegex(ValueError, "does not match the execution claim"):
            self.complete(6, self.rev_a, result_ref="receipt:G6")
        self.record_result("G6")
        previous = self.engine
        self.engine = self.new_engine(verify_action_result=None)
        with self.assertRaisesRegex(PermissionError, "verified action result"):
            self.complete(6, self.rev_a, result_ref="receipt:G6")
        self.engine = previous
        for change, message in (({"authorization_id": "other"}, "does not match"),
                                ({"artifact_sha256": self.rev_b}, "does not match"),
                                ({"target": {"environment": "other"}}, "does not match"),
                                ({"succeeded": False}, "did not succeed")):
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, message):
                self.complete(6, self.rev_a, result_ref=self.record_result("G6", **change))
        self.assertEqual(self.complete(6, self.rev_a, result_ref=self.record_result("G6"))["next_stage"], STAGES[7])

    def test_qa_requires_build_from_verified_merge_not_only_the_same_repository(self):
        self.advance_to_qa()
        with self.assertRaisesRegex(PermissionError, "verified build provenance"):
            self.review("G5", provenance_ref="unknown")
        for change in ({"source_commit": "other"}, {"repository": "repo/other"}, {"artifact_sha256": self.rev_b}):
            with self.subTest(change=change):
                self.provenance["wrong"] = replace(self.provenance[self.rev_a], **change)
                with self.assertRaisesRegex(ValueError, "recorded G4 merge and candidate"):
                    self.review("G5", provenance_ref="wrong")
        review = self.review("G5")
        self.assertEqual(review["build_provenance"]["merge_authorization_id"], self.authorizations["G4"]["event_id"])

    def test_revised_deployment_plan_requires_new_review_with_same_binary(self):
        self.advance_to_deployment()
        prior = self.review("G6", artifact_refs=["rollback-v1"])
        self.approve("G6", "release", "release_manager")
        with self.assertRaisesRegex(ValueError, "new review context digest"):
            self.review("G6", artifact_refs=["rollback-v2"])
        current = self.review("G6", context=self.context_b, artifact_refs=["rollback-v2"])
        self.assertNotEqual(current["event_id"], prior["event_id"])
        with self.assertRaisesRegex(ValueError, "active review and context"):
            self.authorize("G6", review_id=prior["event_id"], review_context_sha256=self.context_a)
        self.assertEqual(self.authorize("G6")["status"], "awaiting_approval")
        self.approve("G6", "release", "release_manager")
        self.assertEqual(self.authorize("G6")["review_context_sha256"], self.context_b)

    def test_return_to_qa_supersedes_release_approvals_and_is_audited(self):
        self.advance_to_deployment()
        g5 = self.reviews[self.run, "G5"]
        g6 = self.review("G6")
        self.approve("G6", "release", "release_manager")
        transition = self.engine.return_to_qa(self.run, reason="Rebuild required", actor="pipeline")
        self.assertEqual(transition["reason"], "Rebuild required")
        self.assertCountEqual(transition["superseded_review_ids"], [g5["event_id"], g6["event_id"]])
        self.engine = self.new_engine()
        with self.assertRaisesRegex(ValueError, "No active G6 review"):
            self.approve("G6", "release", "release_manager")
        with self.assertRaisesRegex(ValueError, "No active G5 review"):
            self.complete(5, self.rev_a)
        with self.assertRaisesRegex(ValueError, "not available at the current stage"):
            self.authorize("G6")
        self.sign_off_qa(self.rev_b)
        with self.assertRaisesRegex(ValueError, "cleared by G5"):
            self.review("G6", self.rev_a)
        self.review("G6", self.rev_b)
        self.assertEqual(self.authorize("G6")["status"], "awaiting_approval")
        self.approve("G6", "release", "release_manager", self.rev_b)
        self.authorize("G6")
        with self.assertRaisesRegex(ValueError, "production authorization has no terminal result"):
            self.engine.return_to_qa(self.run, reason="Rebuild required", actor="pipeline")

    def test_changes_requested_is_recorded_and_blocks_the_gate(self):
        self.review("G1")
        decision = self.approve("G1", "po", "product_owner", decision="changes_requested")
        self.assertEqual(decision["decision"], "changes_requested")
        self.assertEqual(self.complete(0, self.rev_a)["status"], "blocked")
        self.approve("G1", "po", "product_owner")
        self.assertEqual(self.complete(0, self.rev_a)["status"], "completed")

    def test_relative_project_keeps_its_policy_after_working_directory_changes(self):
        root = self.project.parent
        path = self.project / ".ai-sdlc" / "approval-policy.yaml"
        path.parent.mkdir()
        path.write_text("gates:\n  G4: {approver_roles: [tech_lead]}\n", encoding="utf-8")
        another = root / "other" / "project"
        another.mkdir(parents=True)
        previous = Path.cwd()
        try:
            os.chdir(root)
            self.engine = WorkflowEngine(Path("project"), state_dir=self.state, verify_identity=self.credentials.get,
                                         can_approve=lambda identity, role, scope: scope.project == self.project)
            os.chdir(another.parent)
            self.advance_to_code_review()
            self.review("G4")
            with self.assertRaises(PermissionError):
                self.approve("G4", "reviewer", "reviewer")
            self.approve("G4", "lead", "tech_lead")
        finally:
            os.chdir(previous)

    def test_legacy_execution_cannot_be_used_without_review_and_evidence_metadata(self):
        with self.engine.store.transaction() as conn:
            self.engine.store.append(conn, "legacy", "workflow_started", kind="sdlc", stage=STAGES[0])
        with self.assertRaisesRegex(ValueError, "Legacy governance execution must be restarted"):
            self.review("G1", run="legacy")

    def test_approval_and_exception_callbacks_receive_the_actual_review_scope(self):
        self.advance_to_deployment()
        self.engine = self.new_engine(
            can_approve=lambda identity, role, scope: (
                scope.project == self.project and scope.gate == "G6"
                and scope.target == {"environment": "production-eu"}),
            can_authorize_exception=lambda identity, scope: (
                scope.project == self.project and scope.gate == "G6"
                and scope.target == {"environment": "production-eu"}),
        )
        self.review("G6", target={"environment": "production-us"})
        with self.assertRaisesRegex(PermissionError, "not authorized.*scope"):
            self.approve("G6", "release", "release_manager")
        with self.assertRaisesRegex(PermissionError, "No authorized exception"):
            self.grant_action_exception("G6")
        self.review("G6", context=self.context_b)
        self.approve("G6", "release", "release_manager")
        self.assertEqual(self.authorize("G6")["status"], "authorized")

    def test_role_claims_without_a_scope_verifier_do_not_authorize_approval(self):
        self.review("G1")
        self.engine = self.new_engine(can_approve=None)
        with self.assertRaisesRegex(PermissionError, "not authorized.*scope"):
            self.approve("G1", "po", "product_owner")

    def test_non_action_completion_requires_active_review_id_and_current_context(self):
        self.advance_to_qa()
        first = self.review("G5")
        self.approve("G5", "qa", "qa_lead")
        self.approve("G5", "po", "product_owner")
        with self.assertRaisesRegex(ValueError, "review_context_sha256"):
            self.engine.complete_stage(self.run, STAGES[5], artifact_sha256=self.rev_a)
        with self.assertRaisesRegex(ValueError, "active review and context"):
            self.complete(5, self.rev_a, review_context_sha256=self.context_b)
        current = self.review("G5", context=self.context_b)
        with self.assertRaisesRegex(ValueError, "active review and context"):
            self.complete(5, self.rev_a, review_id=first["event_id"])
        self.assertEqual(self.complete(5, self.rev_a, review_id=current["event_id"])["status"], "awaiting_approval")

    def test_development_handoff_accepts_null_output_refs(self):
        for index, (gate, token, role) in enumerate([
            ("G1", "po", "product_owner"), ("G2", "architect", "solution_architect"),
            ("G3", "lead", "tech_lead"),
        ]):
            self.review(gate)
            self.approve(gate, token, role)
            self.complete(index, self.rev_a)
        self.assertEqual(self.complete(3, output_refs=None)["next_stage"], STAGES[4])

    def test_failed_merge_closes_attempt_and_requires_new_review(self):
        self.advance_to_code_review()
        old_review = self.review("G4")
        self.approve("G4", "reviewer", "reviewer")
        old_action = self.authorize("G4")
        self.claim("G4")
        with self.assertRaisesRegex(PermissionError, "already claimed"):
            self.claim("G4")
        failed = self.record_result("G4", succeeded=False, merge_commit=None, failure_outcome="failed_no_changes")
        self.assertEqual(self.complete(4, self.rev_a, result_ref=failed)["status"], "action_failed")
        self.engine = self.new_engine()
        self.assertNotEqual(self.review("G4")["event_id"], old_review["event_id"])
        self.assertEqual(self.authorize("G4")["status"], "awaiting_approval")
        self.approve("G4", "reviewer", "reviewer")
        self.assertNotEqual(self.authorize("G4")["event_id"], old_action["event_id"])
        with self.assertRaisesRegex(PermissionError, "No matching active"):
            self.claim("G4", old_action)
        self.claim("G4")
        with self.assertRaisesRegex(ValueError, "does not match"):
            self.complete(4, self.rev_a, result_ref=failed)
        self.assertEqual(self.complete(4, self.rev_a, result_ref=self.record_result("G4"))["next_stage"], STAGES[5])

    def test_verified_rollback_allows_fresh_deployment_review_or_qa_rewind(self):
        self.advance_to_deployment()
        old_review = self.review("G6")
        self.approve("G6", "release", "release_manager")
        self.authorize("G6")
        self.claim("G6")
        rolled_back = self.record_result("G6", succeeded=False, failure_outcome="rolled_back")
        failure = self.complete(6, self.rev_a, result_ref=rolled_back)
        self.assertEqual(failure["status"], "action_failed")
        self.assertEqual(failure["action_result"]["failure_outcome"], "rolled_back")
        self.assertNotEqual(self.review("G6")["event_id"], old_review["event_id"])
        self.assertEqual(self.authorize("G6")["status"], "awaiting_approval")
        self.assertEqual(self.engine.return_to_qa(self.run, reason="Rebuild", actor="pipeline")["next_stage"], STAGES[5])

    def test_source_fix_supersedes_merge_and_all_downstream_gate_state(self):
        self.advance_to_deployment()
        old_g4 = self.reviews[self.run, "G4"]
        old_g5 = self.reviews[self.run, "G5"]
        old_g6 = self.review("G6")
        transition = self.engine.return_to_development(self.run, reason="Source fix", actor="pipeline")
        self.assertEqual(transition["next_stage"], STAGES[3])
        self.assertCountEqual(transition["superseded_review_ids"],
                              [review["event_id"] for review in (old_g4, old_g5, old_g6)])
        self.engine = self.new_engine()
        with self.assertRaisesRegex(ValueError, "No active G4 review"):
            self.approve("G4", "reviewer", "reviewer")
        self.complete(3)
        self.review("G4", self.rev_b)
        self.approve("G4", "reviewer", "reviewer", self.rev_b)
        self.authorize("G4")
        self.claim("G4")
        self.merge_commit = "fixed-commit"
        self.complete(4, self.rev_b, result_ref=self.record_result("G4"))
        with self.assertRaisesRegex(ValueError, "recorded G4 merge"):
            self.review("G5", self.rev_a)
        self.provenance[self.rev_b] = VerifiedBuildProvenance("repo/example", self.merge_commit, self.rev_b)
        self.sign_off_qa(self.rev_b)
        self.review("G6", self.rev_b)
        self.assertEqual(self.authorize("G6")["status"], "awaiting_approval")

    def grant_action_exception(self, gate, *, run=None):
        run = run or self.run
        expiry = datetime.now(timezone.utc) + timedelta(hours=1)
        return self.engine.approvals.authorize_exception(
            run, gate, "officer", review_id=self.reviews[run, gate]["event_id"],
            artifact_sha256=self.rev_a, reason="Approved waiver", risk="Known risk", mitigation="Follow-up",
            owner="Owner", expires_at=expiry, evidence_refs=["ticket:ref"],
        )

    def test_exception_deadline_is_checked_when_the_adapter_claims_the_action(self):
        self.advance_to_code_review()
        self.review("G4")
        self.engine = self.new_engine(can_authorize_exception=lambda identity, scope: scope.gate == "G4")
        exception = self.grant_action_exception("G4")
        authorization = self.authorize("G4")
        self.assertEqual(authorization["expires_at"], exception["expires_at"])
        with patch("ai_sdlc_platform.workflow_engine.datetime", wraps=datetime) as clock:
            clock.now.return_value = datetime.fromisoformat(exception["expires_at"])
            with self.assertRaisesRegex(PermissionError, "expired"):
                self.claim("G4")
        receipt = self.record_result("G4", succeeded=False, merge_commit=None, failure_outcome="failed_no_changes")
        self.assertEqual(self.complete(4, self.rev_a, result_ref=receipt)["status"], "action_failed")
        self.review("G4")
        self.assertEqual(self.authorize("G4")["status"], "awaiting_approval")

    def test_g7_expired_unclaimed_exception_can_be_reopened_in_same_incident(self):
        self.engine = self.new_engine(can_authorize_exception=lambda identity, scope: scope.gate == "G7")
        run = self.engine.start_critical_incident(incident_ref="INC-001")["execution_id"]
        original = self.review("G7", run=run)
        exception = self.grant_action_exception("G7", run=run)
        authorization = self.authorize("G7", run=run)
        with self.assertRaisesRegex(ValueError, "already authorized"):
            self.review("G7", run=run)
        with patch("ai_sdlc_platform.workflow_engine.datetime", wraps=datetime) as clock:
            clock.now.return_value = datetime.fromisoformat(exception["expires_at"])
            with self.assertRaisesRegex(PermissionError, "expired"):
                self.claim("G7")
            # The expired authorization must not hide metadata under unchanged digests.
            with self.assertRaisesRegex(ValueError, "without a new review context digest"):
                self.review("G7", run=run, authors=("different-author",), artifact_refs=("different-evidence",))
            with self.engine.store.transaction() as connection:
                events = self.engine.store.read(connection, run)
            self.assertFalse(any(event["event_type"] == "action_expired" for event in events))
            replacement = self.review("G7", run=run)
        self.assertNotEqual(replacement["event_id"], original["event_id"])
        self.engine = self.new_engine()
        with self.assertRaisesRegex(PermissionError, "No matching active"):
            self.claim("G7", authorization)
        self.assertEqual(self.authorize("G7", run=run)["status"], "awaiting_approval")
        self.approve("G7", "commander", "incident_commander", run=run)
        self.assertEqual(self.authorize("G7", run=run)["status"], "authorized")
        self.claim("G7")
        with self.engine.store.transaction() as connection:
            events = self.engine.store.read(connection, run)
        expired, = [event for event in events if event["event_type"] == "action_expired"]
        self.assertEqual(expired["authorization_id"], authorization["event_id"])
        self.assertEqual(expired["review_id"], original["event_id"])
        self.assertEqual(expired["expires_at"], exception["expires_at"])
        self.assertEqual(expired["reset_gates"], ["G7"])  # Existing v3 readers honor this reset marker.

    def test_g7_claimed_exception_cannot_be_reopened_on_expiry(self):
        self.engine = self.new_engine(can_authorize_exception=lambda identity, scope: scope.gate == "G7")
        run = self.engine.start_critical_incident(incident_ref="INC-001")["execution_id"]
        self.review("G7", run=run)
        exception = self.grant_action_exception("G7", run=run)
        self.authorize("G7", run=run)
        self.claim("G7")
        with patch("ai_sdlc_platform.workflow_engine.datetime", wraps=datetime) as clock:
            clock.now.return_value = datetime.fromisoformat(exception["expires_at"])
            with self.assertRaisesRegex(ValueError, "already authorized"):
                self.review("G7", run=run, context=self.context_b)

    def test_state_path_rejects_symlinked_project_bucket_and_database(self):
        path = self.engine.store.path
        workspace_bucket = self.project / "redirected"
        workspace_bucket.mkdir()
        for link, destination in ((path.parent, workspace_bucket), (path, workspace_bucket / path.name)):
            with self.subTest(link=link):
                # Use a different, unused state directory so the protected path can be set up safely.
                alt_state = self.state.parent / link.name
                unused = WorkflowEngine(self.project, state_dir=alt_state)
                database = unused.store.path
                if link == path.parent:
                    database.parent.parent.mkdir(parents=True)
                    database.parent.symlink_to(destination, target_is_directory=True)
                else:
                    database.parent.mkdir(parents=True)
                    database.symlink_to(destination)
                with self.assertRaisesRegex(ValueError, "must be outside.*not use symlinks"):
                    WorkflowEngine(self.project, state_dir=alt_state)
        self.assertFalse((workspace_bucket / path.name).exists())

    def test_state_is_outside_workspace_and_isolated_between_projects(self):
        with self.assertRaisesRegex(ValueError, "outside the project"):
            WorkflowEngine(self.project, state_dir=self.project / "audit")
        other_project = self.project.parent / "other-project"
        other_project.mkdir()
        other_engine = WorkflowEngine(other_project, state_dir=self.state)
        with self.assertRaisesRegex(ValueError, "Unknown SDLC execution"):
            other_engine.complete_stage(self.run, STAGES[0])
