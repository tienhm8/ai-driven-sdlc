"""Canonical gate definitions and project policy validation."""
from dataclasses import dataclass
from pathlib import Path
import re

import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode, ScalarNode, SequenceNode


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
    """Yield events newest first, stopping at a gate reset or terminal failed action."""
    for event in reversed(events):
        if (gate in event.get("reset_gates", ())
                or (event["event_type"] == "action_failed" and event["gate"] == gate)):
            break
        yield event


def latest_review(events, gate):
    return next((event for event in gate_attempt_events(events, gate)
                 if event["event_type"] == "review_requested" and event["gate"] == gate), None)


class _ApprovalPolicyLoader(yaml.SafeLoader):
    """Reject ambiguous mappings, including overlaps introduced by YAML merges."""

    MAX_DEPTH = 32
    MAX_MAPPING_ENTRIES = 256
    NODE_TYPES = {"tag:yaml.org,2002:map": MappingNode, "tag:yaml.org,2002:seq": SequenceNode}

    def __init__(self, stream):
        super().__init__(stream)
        self._compose_depth = 0
        self._active_merges = set()
        self._merge_heights = {}

    def compose_node(self, parent, index):
        if self._compose_depth >= self.MAX_DEPTH:
            raise ConstructorError(None, None, "YAML nesting exceeds approval policy limit", self.peek_event().start_mark)
        self._compose_depth += 1
        try:
            return super().compose_node(parent, index)
        finally:
            self._compose_depth -= 1

    def construct_object(self, node, deep=False):
        expected = self.NODE_TYPES.get(node.tag, ScalarNode)
        if not isinstance(node, expected):
            raise ConstructorError(
                None, None, f"expected a {expected.id} node, but found {node.id} for YAML tag {node.tag}",
                node.start_mark,
            )
        try:
            return super().construct_object(node, deep=deep)
        except (KeyError, IndexError, ValueError, TypeError, OverflowError, AttributeError) as error:
            raise ConstructorError(
                None, None, f"invalid value for YAML tag {node.tag}: {error}", node.start_mark,
            ) from error

    def flatten_mapping(self, node):
        if not isinstance(node, MappingNode) or node.tag != "tag:yaml.org,2002:map":
            raise ConstructorError(None, None, "expected a mapping node for YAML merge", node.start_mark)
        if node in self._active_merges:
            raise ConstructorError(None, None, "recursive YAML merge", node.start_mark)
        if len(self._active_merges) >= self.MAX_DEPTH:
            raise ConstructorError(None, None, "YAML merge depth exceeds approval policy limit", node.start_mark)
        if node in self._merge_heights:
            if len(self._active_merges) + self._merge_heights[node] > self.MAX_DEPTH:
                raise ConstructorError(None, None, "YAML merge depth exceeds approval policy limit", node.start_mark)
            return
        self._active_merges.add(node)
        try:
            merge_seen = False
            height = 1
            merged, entries = [], []
            for key_node, value_node in node.value:
                if key_node.tag != "tag:yaml.org,2002:merge":
                    entries.append((key_node, value_node))
                    continue
                if merge_seen:
                    raise ConstructorError(None, None, "duplicate key '<<'", key_node.start_mark)
                merge_seen = True
                if isinstance(value_node, SequenceNode) and value_node.tag == "tag:yaml.org,2002:seq":
                    sources = value_node.value
                else:
                    sources = (value_node,)
                for source in sources:
                    self.flatten_mapping(source)
                    height = max(height, 1 + self._merge_heights[source])
                    if len(merged) + len(source.value) > self.MAX_MAPPING_ENTRIES:
                        raise ConstructorError(None, None, "too many approval policy mapping entries", node.start_mark)
                    merged.extend(source.value)
            if len(merged) + len(entries) > self.MAX_MAPPING_ENTRIES:
                raise ConstructorError(None, None, "too many approval policy mapping entries", node.start_mark)
            node.value = merged + entries
            self._merge_heights[node] = height
        finally:
            self._active_merges.remove(node)

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
                seen.add(key)
            except TypeError as error:
                raise ConstructorError(
                    "while constructing an approval policy mapping", node.start_mark,
                    "found an unhashable key", key_node.start_mark,
                ) from error
            if duplicate:
                raise ConstructorError(
                    "while constructing an approval policy mapping", node.start_mark,
                    f"duplicate key {key!r}", key_node.start_mark,
                )
        return super().construct_mapping(node, deep=deep)


def load_approver_roles(project: Path) -> dict[str, frozenset[str]]:
    approved = {gate_id: gate.roles for gate_id, gate in GATES.items()}
    path = project / ".ai-sdlc" / "approval-policy.yaml"
    if not path.exists():
        return approved
    policy = yaml.load(path.read_text(encoding="utf-8"), Loader=_ApprovalPolicyLoader)
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
