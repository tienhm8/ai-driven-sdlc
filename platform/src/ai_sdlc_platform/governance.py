"""Canonical gate definitions and project policy validation."""
from dataclasses import dataclass
from pathlib import Path
import re

import yaml


@dataclass(frozen=True)
class Gate:
    stage: str | None
    roles: frozenset[str]
    action: str | None = None
    require_all_roles: bool = False


GATES = {
    "G1": Gate("01-requirement-analysis", frozenset({"product_owner"})),
    "G2": Gate("02-system-design", frozenset({"solution_architect"})),
    "G3": Gate("03-task-planning", frozenset({"tech_lead"})),
    "G4": Gate("05-code-review", frozenset({"reviewer", "senior_developer", "tech_lead"}), "merge"),
    "G5": Gate("06-testing-qa", frozenset({"qa_lead", "product_owner"}), require_all_roles=True),
    "G6": Gate("07-deployment", frozenset({"release_manager"}), "deploy_production"),
    "G7": Gate(None, frozenset({"incident_commander"}), "respond_to_critical_incident"),
}
STAGE_GATES = {gate.stage: gate_id for gate_id, gate in GATES.items() if gate.stage is not None}
QA_REVIEW_GATES = frozenset({"G5", "G6"})
DEVELOPMENT_REVIEW_GATES = frozenset({"G4", "G5", "G6"})
WORKFLOW_SCHEMA_VERSION = 3


def require_current_schema(events):
    if events and events[0].get("schema_version") != WORKFLOW_SCHEMA_VERSION:
        raise ValueError("Legacy governance execution must be restarted with the current review and evidence schema")


def gate_attempt_events(events, gate):
    """Yield events newest first, stopping at a rewind or a terminal failed action."""
    for event in reversed(events):
        if (gate in event.get("reset_gates", ())
                or (event["event_type"] == "action_failed" and event["gate"] == gate)):
            break
        yield event


def latest_review(events, gate):
    return next((event for event in gate_attempt_events(events, gate)
                 if event["event_type"] == "review_requested" and event["gate"] == gate), None)


def load_approver_roles(project: Path) -> dict[str, frozenset[str]]:
    approved = {gate_id: gate.roles for gate_id, gate in GATES.items()}
    path = project / ".ai-sdlc" / "approval-policy.yaml"
    if not path.exists():
        return approved
    policy = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(policy, dict) or set(policy) != {"gates"} or not isinstance(policy["gates"], dict):
        raise ValueError("Approval policy must contain a gates mapping")
    for gate_id, override in policy["gates"].items():
        if (gate_id not in GATES or not isinstance(override, dict)
                or override.keys() - {"required", "approver_roles"}):
            raise ValueError(f"Invalid policy for gate {gate_id!r}")
        if override.get("required", True) is not True:
            raise ValueError(f"Mandatory gate {gate_id} cannot be disabled by project policy")
        if "approver_roles" not in override:
            continue
        roles = override["approver_roles"]
        if not isinstance(roles, list) or not roles or not all(isinstance(role, str) for role in roles):
            raise ValueError(f"{gate_id} approver_roles must be a nonempty list of roles")
        roles = frozenset(roles)
        gate = GATES[gate_id]
        if not roles <= gate.roles or (gate.require_all_roles and roles != gate.roles):
            raise ValueError(f"Project policy cannot broaden or remove mandatory {gate_id} roles")
        approved[gate_id] = roles
    return approved


def artifact_digest(value: str, *, field: str = "artifact_sha256") -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", value):
        raise ValueError(f"{field} must be a 64-character hexadecimal SHA-256 digest")
    return value.lower()


def required_text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} is required")
    return value


def references(values, name: str, *, required: bool = False) -> list[str]:
    if not isinstance(values, (list, tuple)) or (required and not values):
        raise ValueError(f"{name} must be a {'nonempty ' if required else ''}list or tuple of references")
    return [required_text(value, name) for value in values]
