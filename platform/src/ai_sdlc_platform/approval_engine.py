"""Record verified human decisions against an active artifact review."""
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import os
from pathlib import Path
from types import MappingProxyType
from typing import Callable, Mapping

from .audit import EventStore
from .governance import GATES, artifact_digest, latest_review, references, require_current_schema, required_text


@dataclass(frozen=True)
class VerifiedApprover:
    subject: str
    roles: frozenset[str]
    is_human: bool


@dataclass(frozen=True)
class ApprovalScope:
    project: Path
    execution_id: str
    gate: str
    target: Mapping[str, str]


class ApprovalEngine:
    def __init__(
        self,
        project: Path,
        *,
        state_dir: Path,
        verify_identity: Callable[[str], VerifiedApprover | None] | None = None,
        can_approve: Callable[[VerifiedApprover, str, ApprovalScope], bool] | None = None,
        can_authorize_exception: Callable[[VerifiedApprover, ApprovalScope], bool] | None = None,
    ):
        self.project = project.resolve()
        state_dir = state_dir.resolve()
        if state_dir.is_relative_to(self.project):
            raise ValueError("Governance state must be outside the project workspace")
        project_key = sha256(os.fsencode(self.project)).hexdigest()
        self.store = EventStore(state_dir / project_key, project=self.project)
        self.verify_identity = verify_identity
        self.can_approve = can_approve
        self.can_authorize_exception = can_authorize_exception

    def _human(self, credential):
        identity = self.verify_identity(credential) if self.verify_identity else None
        if (not isinstance(identity, VerifiedApprover) or identity.is_human is not True
                or not isinstance(identity.roles, frozenset)
                or not all(isinstance(role, str) and role.strip() for role in identity.roles)):
            raise PermissionError("A verified human identity with trusted role claims is required")
        required_text(identity.subject, "verified subject")
        return identity

    def _scope(self, review):
        target = dict(review.get("target", {}))
        if review["gate"] == "G5":
            target["repository"] = review["build_provenance"]["repository"]
        return ApprovalScope(self.project, review["execution_id"], review["gate"], MappingProxyType(target))

    def approve(self, execution_id, gate, credential, decision, *, role, review_id, artifact_sha256,
                comment="", evidence_refs=()):
        if decision not in {"approved", "rejected", "blocked", "changes_requested"}:
            raise ValueError("Decision must be approved, rejected, blocked, or changes_requested")
        if decision != "approved":
            required_text(comment, "decision reason")
        sha256 = artifact_digest(artifact_sha256)
        evidence = references(evidence_refs, "evidence_refs", required=decision == "approved")
        identity = self._human(credential)
        with self.store.transaction() as conn:
            review = self._open_review(self.store.read(conn, execution_id), gate, sha256)
            if review["event_id"] != review_id:
                raise ValueError("The submitted review ID is no longer active")
            if role not in review["allowed_roles"] or role not in identity.roles:
                raise PermissionError(f"Verified identity does not hold an allowed {gate} role")
            if not self.can_approve or self.can_approve(identity, role, self._scope(review)) is not True:
                raise PermissionError(f"Verified identity is not authorized for this {gate} review scope")
            if identity.subject in review["author_ids"]:
                raise PermissionError("Artifact authors may not approve their own work")
            return self.store.append(
                conn, execution_id, "approval_recorded", gate=gate, review_id=review["event_id"],
                artifact_sha256=sha256, approver=identity.subject, approver_role=role,
                decision=decision, reason=comment, evidence_refs=evidence,
            )

    def authorize_exception(self, execution_id, gate, credential, *, review_id, artifact_sha256,
                            reason, risk, mitigation, owner, expires_at, evidence_refs):
        if gate not in GATES:
            raise ValueError(f"Unknown gate: {gate}")
        if GATES[gate].require_all_roles:
            raise PermissionError(f"The dual sign-off for {gate} is not waivable")
        identity = self._human(credential)
        details = {name: required_text(value, name) for name, value in {
            "reason": reason, "risk": risk, "mitigation": mitigation, "owner": owner,
        }.items()}
        if not isinstance(expires_at, datetime) or expires_at.utcoffset() is None:
            raise ValueError("Exception expiry must be a timezone-aware datetime")
        sha256 = artifact_digest(artifact_sha256)
        evidence = references(evidence_refs, "evidence_refs", required=True)
        with self.store.transaction() as conn:
            if expires_at <= datetime.now(timezone.utc):
                raise ValueError("Exception must expire in the future")
            events = self.store.read(conn, execution_id)
            review = self._open_review(events, gate, sha256)
            if review["event_id"] != review_id:
                raise ValueError("The submitted review ID is no longer active")
            if not self.can_authorize_exception or self.can_authorize_exception(identity, self._scope(review)) is not True:
                raise PermissionError(f"No authorized exception for this {gate} review scope")
            if identity.subject in review["author_ids"]:
                raise PermissionError("Artifact authors may not grant their own exception")
            if any(event.get("review_id") == review_id and event["event_type"] == "exception_authorized"
                   for event in events):
                raise ValueError("An exception is already recorded for this review")
            return self.store.append(
                conn, execution_id, "exception_authorized", gate=gate,
                review_id=review["event_id"], artifact_sha256=sha256, approver=identity.subject,
                scope=GATES[gate].action or f"complete:{GATES[gate].stage}",
                approver_roles=sorted(identity.roles), expires_at=expires_at.isoformat(),
                evidence_refs=evidence, **details,
            )

    @staticmethod
    def _open_review(events, gate, sha256):
        if gate not in GATES:
            raise ValueError(f"Unknown gate: {gate}")
        require_current_schema(events)
        review = latest_review(events, gate)
        if not review or review["artifact_sha256"] != sha256:
            raise ValueError(f"No active {gate} review for this artifact revision")
        if any(event.get("review_id") == review["event_id"] and event["event_type"] in {
            "action_authorized", "stage_completed",
        } for event in events):
            raise ValueError(f"The {gate} review is closed")
        return review

    @staticmethod
    def _decision(events, review):
        gate_id = review["gate"]
        allowed = set(review["allowed_roles"])
        latest = {}
        exception = None
        for event in events:
            if event.get("review_id") != review["event_id"]:
                continue
            if event["event_type"] == "approval_recorded":
                latest[event["approver"]] = event
            elif event["event_type"] == "exception_authorized":
                exception = event
        valid = [event for event in latest.values() if event["approver_role"] in allowed]
        vetoes = [event for event in valid if event["decision"] != "approved"]
        if vetoes:
            return "blocked", [event["event_id"] for event in vetoes], None
        roles = {event["approver_role"] for event in valid}
        if (allowed <= roles if GATES[gate_id].require_all_roles else bool(roles)):
            return "approved", [event["event_id"] for event in valid], None
        if exception and datetime.fromisoformat(exception["expires_at"]) > datetime.now(timezone.utc):
            return "exception_authorized", [exception["event_id"]], exception["expires_at"]
        return "awaiting_approval", [], None
