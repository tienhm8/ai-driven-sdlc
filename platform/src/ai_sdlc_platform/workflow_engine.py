"""Enforce stage order and authorize guarded actions in the local workflow."""
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .action_evidence import VerifiedActionResult, VerifiedBuildProvenance, action_target
from .approval_engine import ApprovalEngine
from .audit import new_execution_id
from .constants import STAGES
from .governance import (
    DEVELOPMENT_REVIEW_GATES, GATES, QA_REVIEW_GATES, STAGE_GATES, WORKFLOW_SCHEMA_VERSION,
    artifact_digest, gate_attempt_events, latest_review, load_approver_roles, references,
    require_current_schema, required_text,
)


class WorkflowEngine:
    def __init__(
        self, project: Path, *, state_dir: Path, verify_identity=None, can_approve=None, can_authorize_exception=None,
        verify_action_result: Callable[[str, str], VerifiedActionResult | None] | None = None,
        verify_build_provenance: Callable[[str], VerifiedBuildProvenance | None] | None = None,
    ):
        self.approvals = ApprovalEngine(project, state_dir=state_dir, verify_identity=verify_identity,
                                        can_approve=can_approve, can_authorize_exception=can_authorize_exception)
        self.store = self.approvals.store
        self.verify_action_result = verify_action_result
        self.verify_build_provenance = verify_build_provenance

    def start(self, stage=STAGES[0], actor="system"):
        if stage != STAGES[0]:
            raise ValueError(f"A new SDLC execution must start at {STAGES[0]}")
        return self._start("sdlc", stage, actor)

    def start_critical_incident(self, *, incident_ref, actor="system"):
        return self._start("critical_incident", None, actor,
                           incident_ref=required_text(incident_ref, "incident_ref"))

    def _start(self, kind, stage, actor, **data):
        run_id = new_execution_id()
        with self.store.transaction() as conn:
            self.store.append(conn, run_id, "workflow_started", kind=kind, stage=stage,
                              schema_version=WORKFLOW_SCHEMA_VERSION,
                              actor=required_text(actor, "actor"), status="in_progress", **data)
        return {"execution_id": run_id, "stage": stage, "status": "in_progress", "kind": kind}

    def request_review(self, execution_id, gate, *, artifact_sha256, review_context_sha256,
                       author_ids, actor, artifact_refs, target=None, provenance_ref=None):
        if gate not in GATES:
            raise ValueError(f"Unknown gate: {gate}")
        sha256 = artifact_digest(artifact_sha256)
        context = artifact_digest(review_context_sha256, field="review_context_sha256")
        authors = sorted(set(references(author_ids, "author_ids", required=True)))
        artifacts = references(artifact_refs, "artifact_refs", required=True)
        requester = required_text(actor, "actor")
        if GATES[gate].action:
            target = action_target(gate, target)
        elif target is not None:
            raise ValueError(f"{gate} is not an action gate and does not accept a target")
        provenance = None
        if gate == "G5":
            provenance_ref = required_text(provenance_ref, "provenance_ref")
            provenance = self.verify_build_provenance(provenance_ref) if self.verify_build_provenance else None
            if not isinstance(provenance, VerifiedBuildProvenance):
                raise PermissionError("G5 requires verified build provenance")
        elif provenance_ref is not None:
            raise ValueError("Build provenance is only accepted for G5")

        with self.store.transaction() as conn:
            events = self.store.read(conn, execution_id)
            self._require_gate_context(events, gate)
            if gate == "G7" and target["incident_ref"] != events[0]["incident_ref"]:
                raise ValueError("G7 target must match the incident execution")
            authorization = self._authorized_action(events, gate)
            if authorization:
                expiry = authorization["expires_at"]
                if (gate != "G7" or not expiry or datetime.fromisoformat(expiry) > datetime.now(timezone.utc)
                        or self._action_started(events, authorization["event_id"])):
                    raise ValueError(f"The {gate} action is already authorized")
            scope = {}
            if gate == "G5":
                merge = self._completed_gate(events, "G4")
                if not merge or not merge.get("action_result"):
                    raise ValueError("G5 requires a verified G4 merge result")
                scope["build_provenance"] = provenance.evidence(merge["action_result"], sha256, provenance_ref)
            elif gate == "G6":
                qa = self._completed_gate(events, "G5")
                if not qa or sha256 != qa["artifact_sha256"]:
                    raise ValueError("Production review must use the release candidate cleared by G5")
                scope["qa_completion_id"] = qa["event_id"]
            if GATES[gate].action:
                scope["target"] = target
            revision = {"artifact_sha256": sha256, "review_context_sha256": context}
            metadata = {"author_ids": authors, "artifact_refs": artifacts, **scope}
            prior = latest_review(events, gate)
            if prior and all(prior[key] == value for key, value in revision.items()):
                if any(prior[key] != value for key, value in metadata.items()):
                    raise ValueError("Review metadata cannot change without a new review context digest")
                if not authorization:
                    return prior
            allowed_roles = load_approver_roles(self.approvals.project)[gate]
            if authorization:
                self.store.append(
                    conn, execution_id, "action_expired", gate=gate, actor=requester,
                    authorization_id=authorization["event_id"], review_id=authorization["review_id"],
                    expires_at=authorization["expires_at"], target=authorization["target"],
                    reset_gates=[gate],  # Recognized by existing schema-v3 readers.
                )
            return self.store.append(conn, execution_id, "review_requested", gate=gate,
                                     requester=requester, allowed_roles=sorted(allowed_roles),
                                     **revision, **metadata)

    def authorize_action(self, execution_id, gate, *, artifact_sha256, review_id,
                         review_context_sha256, target, actor="system"):
        if gate not in GATES or GATES[gate].action is None:
            raise ValueError(f"{gate} is not an action gate")
        sha256 = artifact_digest(artifact_sha256)
        context = artifact_digest(review_context_sha256, field="review_context_sha256")
        target = action_target(gate, target)
        actor = required_text(actor, "actor")
        with self.store.transaction() as conn:
            events = self.store.read(conn, execution_id)
            self._require_gate_context(events, gate)
            if gate == "G7" and target["incident_ref"] != events[0]["incident_ref"]:
                raise ValueError("G7 target must match the incident execution")
            if self._authorized_action(events, gate):
                raise ValueError(f"The {gate} action is already authorized")
            review = self.approvals._open_review(events, gate, sha256)
            if review["event_id"] != review_id or review["review_context_sha256"] != context:
                raise ValueError("The authorization request does not match the active review and context")
            if review["target"] != target:
                raise ValueError("The authorization target does not match the reviewed target")
            status, decision_ids, expiry = self.approvals._decision(events, review)
            if status in {"blocked", "awaiting_approval"}:
                return self._blocked(conn, execution_id, review, status, actor, decision_ids)
            return self.store.append(
                conn, execution_id, "action_authorized", action=GATES[gate].action,
                gate=gate, review_id=review_id, artifact_sha256=sha256,
                review_context_sha256=context, target=target,
                actor=actor, status="authorized", basis=status, decision_event_ids=decision_ids,
                expires_at=expiry,
            )

    def check_action_start(self, execution_id, gate, *, authorization_id, artifact_sha256,
                           review_context_sha256, target):
        """Claim a matching authorization once, immediately before the trusted adapter acts."""
        if gate not in GATES or not GATES[gate].action:
            raise ValueError(f"{gate} is not an action gate")
        sha256 = artifact_digest(artifact_sha256)
        context = artifact_digest(review_context_sha256, field="review_context_sha256")
        target = action_target(gate, target)
        with self.store.transaction() as conn:
            events = self.store.read(conn, execution_id)
            self._require_gate_context(events, gate)
            authorization = self._authorized_action(events, gate)
            if (not authorization or authorization["event_id"] != authorization_id
                    or authorization["artifact_sha256"] != sha256
                    or authorization["review_context_sha256"] != context or authorization["target"] != target):
                raise PermissionError("No matching active action authorization")
            if self._action_started(events, authorization_id):
                raise PermissionError("This action authorization was already claimed")
            expiry = authorization["expires_at"]
            started_at = datetime.now(timezone.utc)
            if expiry and datetime.fromisoformat(expiry) <= started_at:
                raise PermissionError("Action authorization has expired")
            return self.store.append(conn, execution_id, "action_started", gate=gate,
                                     authorization_id=authorization_id, started_at=started_at.isoformat(),
                                     expires_at=expiry)

    def complete_stage(self, execution_id, stage, actor="system", output_refs=(), *, artifact_sha256=None,
                       review_id=None, review_context_sha256=None, action_result_ref=None):
        actor = required_text(actor, "actor")
        outputs = references(() if output_refs is None else output_refs, "output_refs")
        gate = STAGE_GATES.get(stage)
        result = None
        if action_result_ref is not None:
            if not gate or not GATES[gate].action:
                raise ValueError("Only an action-gated stage accepts an action result")
            action_result_ref = required_text(action_result_ref, "action_result_ref")
            result = self.verify_action_result(gate, action_result_ref) if self.verify_action_result else None
            if not isinstance(result, VerifiedActionResult):
                raise PermissionError("A verified action result is required to complete this stage")

        with self.store.transaction() as conn:
            events = self.store.read(conn, execution_id)
            current = self._active_stage(events)
            if current is None or stage != current:
                raise ValueError(f"Cannot complete {stage!r}; active stage is {current!r}")
            sha256 = artifact_digest(artifact_sha256) if gate or artifact_sha256 is not None else None
            completed_review_id = None
            context = None
            decision_ids = []
            basis = None
            evidence = {}
            if gate and GATES[gate].action:
                authorization = self._authorized_action(events, gate)
                if authorization is None or authorization["artifact_sha256"] != sha256:
                    raise ValueError(f"Authorize {GATES[gate].action} for this revision before completing the stage")
                if result is None:
                    raise ValueError("A verified action result is required to complete this stage")
                start_event = self._action_started(events, authorization["event_id"])
                result_evidence = result.evidence(authorization, action_result_ref, start_event)
                if "failure_outcome" in result_evidence:
                    return self.store.append(conn, execution_id, "action_failed", gate=gate, stage=stage,
                                             status="action_failed", actor=actor,
                                             review_id=authorization["review_id"], artifact_sha256=sha256,
                                             action_result=result_evidence)
                evidence["action_result"] = result_evidence
                completed_review_id = authorization["review_id"]
                context = authorization["review_context_sha256"]
                decision_ids = [authorization["event_id"]]
                basis = authorization["basis"]
            elif gate:
                review = self.approvals._open_review(events, gate, sha256)
                context = artifact_digest(review_context_sha256, field="review_context_sha256")
                if review["event_id"] != review_id or review["review_context_sha256"] != context:
                    raise ValueError("Stage completion does not match the active review and context")
                completed_review_id = review_id
                basis, decision_ids, _ = self.approvals._decision(events, review)
                if basis in {"blocked", "awaiting_approval"}:
                    return self._blocked(conn, execution_id, review, basis, actor, decision_ids)
            position = STAGES.index(stage) + 1
            next_stage = STAGES[position] if position < len(STAGES) else None
            self.store.append(conn, execution_id, "stage_completed", stage=stage, next_stage=next_stage,
                              actor=actor, output_refs=outputs, gate=gate, review_id=completed_review_id,
                              review_context_sha256=context, artifact_sha256=sha256, basis=basis,
                              decision_event_ids=decision_ids, **evidence)
            return {"execution_id": execution_id, "stage": stage, "status": "completed",
                    "next_stage": next_stage}

    def return_to_qa(self, execution_id, *, reason, actor):
        """Return from Deployment when no production action is pending."""
        return self._rewind(execution_id, {GATES["G6"].stage}, GATES["G5"].stage,
                            QA_REVIEW_GATES, "qa_reopened", "QA", actor, reason)

    def return_to_development(self, execution_id, *, reason, actor):
        """Return for a source fix and require a new G4 merge and downstream approvals."""
        return self._rewind(execution_id, {GATES["G5"].stage, GATES["G6"].stage}, STAGES[3],
                            DEVELOPMENT_REVIEW_GATES, "development_reopened", "Development", actor, reason)

    def _rewind(self, execution_id, allowed_stages, next_stage, reset_gates, event_type, name, actor, reason):
        actor = required_text(actor, "actor")
        reason = required_text(reason, "reason")
        with self.store.transaction() as conn:
            events = self.store.read(conn, execution_id)
            current = self._active_stage(events)
            if current not in allowed_stages:
                raise ValueError(f"Returning to {name} is not available at the current stage")
            if self._authorized_action(events, "G6"):
                raise ValueError(f"Cannot return to {name} while a production authorization has no terminal result")
            gates = sorted(reset_gates)
            return self.store.append(
                conn, execution_id, event_type, stage=current, next_stage=next_stage, actor=actor, reason=reason,
                reset_gates=gates,
                superseded_review_ids=[review["event_id"] for gate in gates
                                       if (review := latest_review(events, gate)) is not None],
                superseded_completion_ids=[completed["event_id"] for gate in gates
                                           if (completed := self._completed_gate(events, gate)) is not None],
            )

    def _blocked(self, conn, execution_id, review, status, actor, decision_ids):
        gate = review["gate"]
        event = self.store.append(conn, execution_id, "gate_blocked", gate=gate, stage=GATES[gate].stage,
                                  review_id=review["event_id"], status=status,
                                  artifact_sha256=review["artifact_sha256"], actor=actor,
                                  decision_event_ids=decision_ids)
        return {**event, "required_gate": gate}

    @staticmethod
    def _completed_gate(events, gate):
        return next((event for event in gate_attempt_events(events, gate)
                     if event["event_type"] == "stage_completed" and event["gate"] == gate), None)

    @staticmethod
    def _authorized_action(events, gate):
        return next((event for event in gate_attempt_events(events, gate)
                     if event["event_type"] == "action_authorized" and event["gate"] == gate), None)

    @staticmethod
    def _action_started(events, authorization_id):
        return next((event for event in events if event["event_type"] == "action_started"
                     and event["authorization_id"] == authorization_id), None)

    @staticmethod
    def _active_stage(events):
        if not events or events[0].get("kind") != "sdlc":
            raise ValueError("Unknown SDLC execution")
        require_current_schema(events)
        return next((event["next_stage"] for event in reversed(events)
                     if "next_stage" in event), events[0]["stage"])

    def _require_gate_context(self, events, gate):
        if gate == "G7":
            if not events or events[0].get("kind") != "critical_incident":
                raise ValueError("G7 requires a critical incident execution")
            require_current_schema(events)
        elif self._active_stage(events) != GATES[gate].stage:
            raise ValueError(f"{gate} is not available at the current stage")
