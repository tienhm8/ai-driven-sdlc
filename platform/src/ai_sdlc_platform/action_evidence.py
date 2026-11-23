"""Trusted adapter contracts for action receipts and build provenance."""
from collections.abc import Mapping
from dataclasses import dataclass

from .governance import artifact_digest, required_text


_TARGET_FIELDS = {
    "G4": ("repository", "pull_request", "base_ref"),
    "G6": ("environment",),
    "G7": ("incident_ref",),
}


def action_target(gate: str, target) -> dict[str, str]:
    fields = _TARGET_FIELDS[gate]
    if not isinstance(target, Mapping) or set(target) != set(fields):
        raise ValueError(f"{gate} target must contain exactly: {', '.join(fields)}")
    return {field: required_text(target[field], f"target.{field}") for field in fields}


@dataclass(frozen=True)
class VerifiedActionResult:
    """Observed provider result for one specific governance authorization."""

    authorization_id: str
    artifact_sha256: str
    target: Mapping[str, str]
    succeeded: bool
    merge_commit: str | None = None
    failure_outcome: str | None = None
    start_event_id: str | None = None

    def evidence(self, authorization: dict, result_ref: str, start_event: dict | None) -> dict:
        if (self.authorization_id != authorization["event_id"]
                or artifact_digest(self.artifact_sha256) != authorization["artifact_sha256"]
                or action_target(authorization["gate"], self.target) != authorization["target"]):
            raise ValueError("Verified action result does not match the authorization")
        if self.start_event_id != (start_event["event_id"] if start_event else None):
            raise ValueError("Verified action result does not match the execution claim")
        evidence = {"authorization_id": self.authorization_id, "result_ref": result_ref,
                    "start_event_id": self.start_event_id, "target": dict(authorization["target"])}
        if self.succeeded is True and self.failure_outcome is None:
            if start_event is None:
                raise ValueError("Claim the authorization before executing the action")
            if authorization["gate"] == "G4":
                evidence["merge_commit"] = required_text(self.merge_commit, "merge_commit")
        elif (self.succeeded is False and self.merge_commit is None
              and (self.failure_outcome == "failed_no_changes"
                   or (start_event is not None and authorization["gate"] == "G6"
                       and self.failure_outcome == "rolled_back"))):
            evidence["failure_outcome"] = self.failure_outcome
        else:
            raise ValueError("The authorized action did not succeed and has no verified safe terminal failure")
        return evidence


@dataclass(frozen=True)
class VerifiedBuildProvenance:
    """Observed build origin for an immutable release candidate."""

    repository: str
    source_commit: str
    artifact_sha256: str

    def evidence(self, merge: dict, sha256: str, provenance_ref: str) -> dict:
        if (artifact_digest(self.artifact_sha256) != sha256
                or self.repository != merge["target"]["repository"]
                or self.source_commit != merge["merge_commit"]):
            raise ValueError("Verified build provenance does not match the recorded G4 merge and candidate digest")
        return {"provenance_ref": provenance_ref, "repository": self.repository,
                "source_commit": self.source_commit, "merge_authorization_id": merge["authorization_id"]}
