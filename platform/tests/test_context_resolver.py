from dataclasses import replace
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from unittest import TestCase, skipUnless
from unittest.mock import Mock

import yaml

from ai_sdlc_platform.approval_engine import VerifiedApprover
from ai_sdlc_platform.constants import STAGES
from ai_sdlc_platform.context_resolver import ContextRequest, load_selected_context, resolve_context
from ai_sdlc_platform.managed_model import ManagedModelRunner, Observation, ToolReply
from ai_sdlc_platform.tool_adapters import ToolAdapterRegistry
from ai_sdlc_platform.workflow_engine import WorkflowEngine


ROOT = Path(__file__).resolve().parents[2]


@skipUnless(shutil.which("git"), "Git is required for checkout fixtures")
class ContextResolverTests(TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.project = self.root / "instance"
        self.state = self.root / "state"
        self.manifest = self.project / ".ai-sdlc/project.yaml"
        self.manifest.parent.mkdir(parents=True)
        self.shared = self.root / "shared-ai"
        shutil.copytree(ROOT / "shared-ai", self.shared)
        self.config = {"schema_version": 1, "project": {"id": "demo", "name": "Demo"}, "technology_stack": {
            "repositories": {"be": {"nestjs": "11.2.7"},
                             "fe": {"umi-max": "4.4.6", "react": "19.2.3", "antd": "5.24.2"}}}}
        self.save_manifest()
        deps = {"@nestjs/core": "^11.2.7"}
        be = self.make_checkout("be", {
            "package.json": json.dumps({"dependencies": deps}),
            "package-lock.json": json.dumps({"packages": {"": {"dependencies": deps},
                                                         "node_modules/@nestjs/core": {"version": "11.2.7"}}}),
        })
        fe = self.make_checkout("fe", {
            "package.json": json.dumps({"dependencies": {"@umijs/max": "^4.4.6", "react": "19.2.3", "antd": "^5.24.2"}}),
            "yarn.lock": '# yarn lockfile v1\n"@umijs/max@^4.4.6":\n  version "4.4.6"\n'
                         'react@18.3.1:\n  version "18.3.1"\nreact@19.2.3, react@^19.0.0:\n  version "19.2.3"\n'
                         'antd@^5.24.2:\n  version "5.24.2"\n',
        })
        self.workspace = {"repositories": {alias: {"checkout": str(self.root / alias), "repository": f"demo/{alias}"}
                                            for alias in ("be", "fe")}, "work_items": {"US-001": {
            "version": "v1", "backlog_ref": "backlog.md#US-001", "ac_ref": "story.md#acceptance",
            "dod_ref": "dod.md#v1", "repositories": {alias: {"paths": ["src/catalog"]} for alias in ("be", "fe")}}}}
        self.request = ContextRequest("US-001", "be", be, "developer", STAGES[3], "code-generation", "medium",
                                      ("src/catalog/filter.ts",), frozenset({"dto", "query"}))
        self.fe = replace(self.request, repo="fe", revision=fe, focus=frozenset({"table", "request"}))

    def save_manifest(self):
        self.manifest.write_text(yaml.safe_dump(self.config), encoding="utf-8")

    def git(self, alias, *args):
        result = subprocess.run(["git", "-C", str(self.root / alias), *args], check=True, capture_output=True, text=True)
        return result.stdout.strip()

    def make_checkout(self, alias, files):
        checkout = self.root / alias
        checkout.mkdir()
        self.git(alias, "init", "-q")
        self.git(alias, "config", "user.email", "fixture@example.invalid")
        self.git(alias, "config", "user.name", "Fixture")
        for name, text in {**files, "src/catalog/filter.ts": "fixture\n"}.items():
            path = checkout / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return self.commit(alias)

    def commit(self, alias):
        self.git(alias, "add", ".")
        self.git(alias, "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
        return self.git(alias, "rev-parse", "HEAD")

    def resolve(self, request=None):
        return resolve_context(self.project, ROOT / "framework", self.shared, self.workspace, self.state,
                               request or self.request)

    def selected(self, result, kind):
        return {row["id"]: row for row in result[kind] if row["selected"]}

    def local(self, rel, text):
        path = self.manifest.parent / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_story_filters_stack_by_checkout_and_reference_by_focus(self):
        for request, skill, refs in ((self.request, "nestjs", ["dto-validation", "controller-service-repository"]),
                                     (self.fe, "umi-max", ["data-fetching", "forms-tables"])):
            with self.subTest(skill=skill):
                result = self.resolve(request)
                self.assertEqual(result["status"], "resolved", result["blockers"])
                self.assertEqual(result, self.resolve(request))
                self.assertEqual(result["authority"], "none")
                selected = self.selected(result, "skills")
                self.assertEqual(set(selected), {skill})
                self.assertEqual(selected[skill]["references"], [f"references/{ref}.md" for ref in refs])
                self.assertIn("core/ai-usage-flow", self.selected(result, "rules"))
                self.assertIn("04-development/workflow", self.selected(result, "rules"))
                self.assertEqual(result["route"]["effort"], "medium")
                self.assertNotIn(str(self.root), json.dumps(result))
        self.assertFalse(self.state.exists())
        result = self.resolve(replace(self.fe, focus=frozenset({"component"})))
        self.assertIn("react", self.selected(result, "skills"))

    def test_catalog_story_validation_and_review_use_only_the_current_stack(self):
        for request, stack_skill, testing_ref, review_ref in (
            (self.request, "nestjs", "backend-nestjs", "review-backend"),
            (self.fe, "umi-max", "frontend-umi-max", "review-frontend"),
        ):
            for task, stage, profile, effort, reference in (
                ("testing", STAGES[5], "implementation", "medium", testing_ref),
                ("code-review", STAGES[4], "critical-review", "high", review_ref),
            ):
                with self.subTest(repo=request.repo, task=task):
                    result = self.resolve(replace(request, task=task, stage=stage))
                    self.assertEqual(result["status"], "resolved", result["blockers"])
                    self.assertEqual(result["work_item_id"], self.request.work_item_id)
                    self.assertEqual(result["authority"], "none")
                    self.assertEqual((result["route"]["profile"], result["route"]["effort"]), (profile, effort))
                    skills = self.selected(result, "skills")
                    self.assertEqual(set(skills), {task, stack_skill})
                    self.assertEqual(skills[task]["references"], [f"references/{reference}.md"])
        self.assertFalse(self.state.exists())

    def test_catalog_story_ci_and_component_are_opt_in(self):
        for tag, skill in (("ci", "gitlab-ci"), ("component", "react")):
            with self.subTest(focus=tag):
                result = self.resolve(replace(self.fe, focus=self.fe.focus | {tag}))
                self.assertEqual(result["status"], "resolved", result["blockers"])
                self.assertEqual(set(self.selected(result, "skills")), {"umi-max", skill})

    def test_auth_and_migration_preserve_high_effort_at_the_binding_boundary(self):
        adapter = self.root / "adapters/claude/adapter.yaml"
        adapter.parent.mkdir(parents=True)
        adapter_data = {"name": "claude", "enabled": True, "routing": {"default_model": "fixture-model", "models": {
            "fixture-model": {"profiles": ["implementation"], "capabilities": ["text", "code"],
                              "data_policy": "fixture-policy", "capability_evidence": "fixture:v1",
                              "effort": {"medium": "native-balanced"}},
        }}}
        adapter.write_text(yaml.safe_dump(adapter_data), encoding="utf-8")
        adapters = ToolAdapterRegistry(adapter.parent.parent)

        def bind(request):
            return resolve_context(self.project, ROOT / "framework", self.shared, self.workspace,
                                   self.state, request, adapters=adapters)

        self.assertEqual(bind(self.request)["route"]["status"], "bound-preview")
        for tag, skill in (("auth", "authentication"), ("migration", "database-migration")):
            with self.subTest(focus=tag):
                request = replace(self.request, risk="low", focus=frozenset({tag}))
                result = bind(request)
                self.assertEqual(result["route"]["risk"], "high")
                self.assertEqual(result["route"]["effort"], "high")
                self.assertEqual(result["route"]["status"], "manual-selection-required")
                self.assertEqual(result["blockers"][0]["code"], "EFFORT_UNSUPPORTED")
                self.assertEqual(set(self.selected(result, "skills")), {"nestjs", skill})
        adapter_data["routing"]["models"]["fixture-model"]["effort"]["high"] = "native-deep"
        adapter.write_text(yaml.safe_dump(adapter_data), encoding="utf-8")
        result = bind(replace(self.request, risk="low", focus=frozenset({"migration"})))
        self.assertEqual(result["status"], "resolved", result["blockers"])
        self.assertEqual(result["route"]["native_effort"], "native-deep")
        self.assertEqual(result["authority"], "none")

    def test_missing_alias_revision_work_item_and_path_are_not_inferred(self):
        for request, code in ((replace(self.request, repo="other"), "UNKNOWN_REPO_ALIAS"),
                              (replace(self.request, revision=self.fe.revision), "UNVERIFIED_CHECKOUT"),
                              (replace(self.request, work_item_id="US-404"), "WORK_ITEM_EVIDENCE_MISSING"),
                              (replace(self.request, paths=("src/catalogue/index.ts",)), "WORK_ITEM_SCOPE_UNVERIFIED"),
                              (replace(self.request, risk="unknown"), "ROUTE_UNRESOLVED")):
            with self.subTest(code=code):
                self.assertIn(code, {issue["code"] for issue in self.resolve(request)["blockers"]})
        self.workspace["repositories"].pop("be")
        self.assertEqual(self.resolve()["blockers"][0]["code"], "UNVERIFIED_CHECKOUT")
        with self.assertRaisesRegex(ValueError, "commit ID"):
            self.resolve(replace(self.request, revision="HEAD"))
        with self.assertRaisesRegex(ValueError, "relative path"):
            self.resolve(replace(self.request, paths=("src/../outside",)))

    def test_lockfile_is_read_at_the_requested_revision_and_mismatch_excludes_skill(self):
        lock = self.root / "be" / "package-lock.json"
        lock.write_text(lock.read_text().replace('"version": "11.2.7"', '"version": "11.2.8"'))
        newer = self.commit("be")
        self.assertIn("nestjs", self.selected(self.resolve(), "skills"))
        result = self.resolve(replace(self.request, revision=newer))
        self.assertEqual(result["stack"]["nestjs"], {"declared": "11.2.7", "observed": "11.2.8"})
        self.assertNotIn("nestjs", self.selected(result, "skills"))
        self.assertEqual(result["warnings"][0]["code"], "STACK_VERSION_MISMATCH")

    def test_scope_cannot_cross_a_committed_symlink(self):
        (self.root / "be/src/catalog/linked").symlink_to(self.root / "fe", target_is_directory=True)
        commit = self.commit("be")
        result = self.resolve(replace(self.request, revision=commit, paths=("src/catalog/linked/filter.ts",)))
        self.assertEqual(result["blockers"][0]["code"], "UNSAFE_SCOPE")

    def test_scoped_rules_mandatory_names_and_collisions(self):
        self.local("local-rules/core/ai-usage-flow.mdc", "ignored\n")
        self.local("local-rules/catalog.mdc", "---\nscope: {repos: [be], paths: ['src/catalog/**'], "
                   "tasks: [code-generation]}\n---\nbody\n")
        be = self.resolve()
        self.assertIn("catalog", self.selected(be, "rules"))
        self.assertNotIn("catalog", self.selected(self.resolve(self.fe), "rules"))
        self.assertEqual(self.selected(be, "rules")["core/ai-usage-flow"]["source"], "shared")
        self.assertNotIn("project", {rule["source"] for rule in be["rules"] if rule["reason"] == "mandatory"})
        duplicate = self.local("local-rules/catalog.md", "Duplicate extension\n")
        self.assertIn("collision", self.resolve()["blockers"][0]["message"])
        duplicate.unlink()
        self.local("local-rules/renamed.md", "---\nid: core/ai-usage-flow\n---\nbody\n")
        self.assertIn("collision", self.resolve()["blockers"][0]["message"])

    def test_explicit_conflict_and_resource_escape_block_explanation(self):
        rule = self.local("local-rules/strict.md", "---\nconflicts: [core/ai-usage-flow]\n---\nbody\n")
        self.assertIn("Unresolved rule conflict", self.resolve()["blockers"][0]["message"])
        rule.unlink()
        (rule.parent / "escape").symlink_to(self.root / "be", target_is_directory=True)
        self.assertIn("escapes its root", self.resolve()["blockers"][0]["message"])

    def test_skills_only_read_frontmatter_and_detect_duplicate_ids(self):
        for rel in ("backend/nestjs/SKILL.md", "frontend/umi-max/SKILL.md"):
            path = self.shared / "skills" / rel
            path.write_bytes(path.read_bytes().split(b"---\n", 2)[0] + b"---\n"
                             + path.read_bytes().split(b"---\n", 2)[1] + b"---\n\xff")
        ref = self.shared / "skills/backend/nestjs/references/dto-validation.md"
        ref.write_bytes(b"\xff")
        self.assertEqual(self.resolve()["status"], "resolved")
        self.local("local-skills/nestjs/SKILL.md", "---\nname: nestjs\ndescription: Duplicate\n---\nbody\n")
        self.assertIn("Duplicate skill ID", self.resolve()["blockers"][0]["message"])

    def test_materialization_reads_only_selected_body_and_references(self):
        for rel in ("frontend/umi-max/SKILL.md", "backend/nestjs/references/jobs-and-notifications.md"):
            path = self.shared / "skills" / rel
            path.write_bytes(b"---\n" + path.read_bytes().split(b"---\n", 2)[1] + b"---\n\xff"
                             if path.name == "SKILL.md" else b"\xff")
        args = (self.project, ROOT / "framework", self.shared, self.workspace, self.state)
        content = load_selected_context(*args, self.request)
        self.assertEqual([row["kind"] for row in content][-3:], ["skills", "reference", "reference"])
        self.assertTrue(content[-3]["path"].endswith("nestjs/SKILL.md"))
        self.assertTrue(content[-1]["path"].endswith("controller-service-repository.md"))
        with self.assertRaisesRegex(ValueError, "GATE_UNVERIFIED"):
            load_selected_context(*args, replace(self.request, action="coding"))

    def test_risk_floor_and_binding_are_preview_only(self):
        self.config["ai"] = {"tool_bindings": {"claude": {"implementation": {"model": "fixture-model",
                                                                             "effort": {"high": "native-high"}}}}}
        self.save_manifest()
        request = replace(self.request, risk="low", focus=frozenset({"auth"}))
        result = self.resolve(request)
        self.assertEqual(result["route"]["effort"], "high")
        self.assertEqual(result["route"]["model"], "fixture-model")
        self.assertEqual(result["route"]["native_effort"], "native-high")
        self.assertEqual(result["route"]["status"], "preview-only-unverified")
        self.assertEqual(set(self.selected(result, "skills")), {"nestjs", "authentication"})
        self.config["governance"] = {"allow_project_override_mandatory_rules": True}
        self.save_manifest()
        self.assertEqual(self.resolve()["blockers"][0]["code"], "LEGACY_MANDATORY_OVERRIDE")

    def test_gate_requires_current_record_and_never_claims_it(self):
        request = replace(self.request, action="coding")
        adapter = self.root / "adapters/claude/adapter.yaml"
        adapter.parent.mkdir(parents=True)
        adapter.write_text("name: claude\nenabled: true\nrouting:\n  default_model: fixture-model\n  models:\n"
                           "    fixture-model:\n      profiles: [implementation]\n      capabilities: [text, code]\n"
                           "      data_policy: fixture-policy\n      capability_evidence: fixture:v1\n"
                           "      effort: {medium: native-balanced}\n", encoding="utf-8")
        transport = Mock(return_value=ToolReply("ok", "answer", Observation("fixture-model", "native-balanced")))
        runner = ManagedModelRunner(self.project, ROOT / "framework", self.shared, self.workspace, self.state,
                                    adapters=ToolAdapterRegistry(adapter.parent.parent), transports={"claude": transport},
                                    authorize_scope=Mock(return_value=True), allow_data=Mock(return_value=True),
                                    allow_budget=Mock(return_value=True), audit=Mock())
        self.assertEqual(runner.run(request, b"synthetic task").reason, "GATE_UNVERIFIED")
        transport.assert_not_called()
        result = self.resolve(request)
        self.assertEqual(result["gate"]["status"], "unverified")
        self.assertFalse(self.state.exists())
        engine = WorkflowEngine(self.project, state_dir=self.state,
                                verify_identity=lambda role: VerifiedApprover(f"{role}-id", frozenset({role}), True),
                                can_approve=lambda *_: True)
        run = engine.start()["execution_id"]
        work = self.workspace["work_items"]["US-001"]["repositories"]["be"]
        artifact, context = "a" * 64, "b" * 64
        for index, role in enumerate(("product_owner", "solution_architect", "tech_lead")):
            gate = f"G{index + 1}"
            review = engine.request_review(run, gate, artifact_sha256=artifact, review_context_sha256=context,
                                           author_ids=["dev"], actor="test", artifact_refs=["fixture.md"])
            engine.approvals.approve(run, gate, role, "approved", role=role, review_id=review["event_id"],
                                     artifact_sha256=artifact, comment="Fixture decision", evidence_refs=["check.md"])
            engine.complete_stage(run, STAGES[index], artifact_sha256=artifact, review_context_sha256=context,
                                  review_id=review["event_id"])
        work["G3"] = {"revision": request.revision, "execution_id": run, "review_id": review["event_id"],
                      "artifact_sha256": artifact, "review_context_sha256": context}
        self.assertEqual(self.resolve(request)["gate"]["status"], "observed")
        self.assertEqual(runner.run(request, b"synthetic task").status, "completed")
        transport.assert_called_once()
        engine.complete_stage(run, STAGES[3])
        target = {"repository": "demo/be", "pull_request": "42", "base_ref": "refs/heads/main"}
        review = engine.request_review(run, "G4", artifact_sha256=artifact, review_context_sha256=context,
                                       author_ids=["dev"], actor="test", artifact_refs=["fixture.md"], target=target)
        engine.approvals.approve(run, "G4", "reviewer", "approved", role="reviewer", review_id=review["event_id"],
                                 artifact_sha256=artifact, comment="Fixture decision", evidence_refs=["check.md"])
        details = {"artifact_sha256": artifact, "review_context_sha256": context, "review_id": review["event_id"],
                   "target": target}
        work["G4"] = {**details, "revision": request.revision, "execution_id": run}
        merge = replace(self.request, action="merge", stage=STAGES[4], task="code-review", role="reviewer")
        self.assertEqual(self.resolve(merge)["gate"]["status"], "unverified")
        authorization = engine.authorize_action(run, "G4", **details)
        before = engine.store.path.read_bytes()
        self.assertEqual(self.resolve(merge)["gate"]["status"], "observed")
        self.assertEqual(engine.store.path.read_bytes(), before)
        work["G4"]["revision"] = self.fe.revision
        self.assertEqual(self.resolve(merge)["gate"]["reason"], "missing-or-stale-review-link")
        work["G4"]["revision"] = merge.revision
        work["G4"]["target"] = {**target, "pull_request": "43"}
        self.assertEqual(self.resolve(merge)["gate"]["reason"], "reviewed-target-mismatch")
        work["G4"]["target"] = target
        engine.check_action_start(run, "G4", authorization_id=authorization["event_id"], artifact_sha256=artifact,
                                  review_context_sha256=context, target=target)
        self.assertEqual(self.resolve(merge)["gate"]["status"], "unverified")

    def test_cli_json_exit_codes(self):
        config = self.root / "workspace.yaml"
        config.write_text(yaml.safe_dump(self.workspace))
        command = [sys.executable, "-B", str(ROOT / "platform/scripts/resolve-context.py"), "--project", str(self.project),
                   "--workspace-config", str(config), "--state-dir", str(self.state), "--work-item-id", "US-001", "--repo", "fe",
                   "--revision", self.fe.revision, "--role", "developer", "--stage", STAGES[3], "--task", "code-generation",
                   "--risk", "medium", "--path", "src/catalog/filter.ts", "--focus", "table", "--format", "json"]
        success = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr or success.stdout)
        self.assertEqual(json.loads(success.stdout)["authority"], "none")
        blocked = subprocess.run(command + ["--action", "coding"], capture_output=True, text=True)
        self.assertEqual(blocked.returncode, 1, blocked.stderr)
        self.assertEqual(json.loads(blocked.stdout)["blockers"][0]["code"], "GATE_UNVERIFIED")
        text = subprocess.run(command + ["--format", "text"], capture_output=True, text=True)
        self.assertEqual(text.returncode, 0, text.stderr)
        self.assertIn("Stack umi-max: declared=4.4.6, observed=4.4.6", text.stdout)
        self.assertIn("implementation/medium via claude → tool-default (preview-only-unverified)", text.stdout)

        adapter = self.root / "adapters/claude/adapter.yaml"
        adapter.parent.mkdir(parents=True)
        adapter.write_text("name: claude\nenabled: true\nrouting:\n  default_model: fixture-model\n  models:\n"
                           "    fixture-model:\n      profiles: [implementation]\n      capabilities: [text, code]\n"
                           "      data_policy: fixture-policy\n      capability_evidence: fixture:v1\n"
                           "      effort: {medium: native-balanced}\n", encoding="utf-8")
        bound_command = command + ["--adapters-dir", str(adapter.parent.parent)]
        bound = subprocess.run(bound_command, capture_output=True, text=True)
        self.assertEqual(bound.returncode, 0, bound.stderr or bound.stdout)
        route = json.loads(bound.stdout)["route"]
        self.assertEqual((route["status"], route["model"], route["native_effort"]),
                         ("bound-preview", "fixture-model", "native-balanced"))
        high = subprocess.run(bound_command + ["--risk", "high"], capture_output=True, text=True)
        self.assertEqual(high.returncode, 1, high.stderr or high.stdout)
        self.assertEqual(json.loads(high.stdout)["blockers"][0]["code"], "EFFORT_UNSUPPORTED")
