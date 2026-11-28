"""Static validation for the versioned (schema_version: 1) project manifest.

Manifests without ``schema_version`` keep their legacy behavior untouched.
"""
import re

import yaml

MANIFEST_SCHEMA_VERSION = 1
ID_PATTERN = r"[A-Za-z0-9][A-Za-z0-9_-]*"
VERSION_PATTERN = r"[0-9]+(?:\.[0-9]+)*(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?(?:\+[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?"
DEFAULT_POLICY_ID = "default"
EFFORT_LEVELS = ("low", "medium", "high")
AI_POLICY_DEFAULTS = {"routing_policy": DEFAULT_POLICY_ID, "context_policy": DEFAULT_POLICY_ID}
DELIVERY_STANDARD = "standard"
DELIVERY_PROTOTYPE_FIRST = "prototype_first"
DELIVERY_MODES = (DELIVERY_STANDARD, DELIVERY_PROTOTYPE_FIRST)
# Only the pre-coding gates may run in parallel with development; G4-G7 always block.
DEFERRABLE_GATES = ("G1", "G2", "G3")
UX_IMPROVEMENT_MODES = ("apply_and_record", "propose_only")
MERGE_POLICIES = ("after_g4", "after_deferred_gates")


class _StrictLoader(yaml.SafeLoader):
    pass


class _AmbiguousMappingError(ValueError):
    pass


def _no_duplicates(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise _AmbiguousMappingError("YAML merge keys are not supported in versioned configuration")
        key = loader.construct_object(key_node, deep=True)
        if isinstance(key, (list, dict, set)):
            continue
        if key in seen:
            raise _AmbiguousMappingError(f"Duplicate YAML key {key!r} (line {key_node.start_mark.line + 1})")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep)


_StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def strict_yaml_mapping(text: str) -> dict:
    data = yaml.load(text, Loader=_StrictLoader)
    if not isinstance(data, dict):
        raise ValueError("Expected a YAML mapping")
    return data


def parse_manifest_text(text: str):
    """Parse versioned YAML strictly and preserve the legacy loader otherwise."""
    try:
        return strict_yaml_mapping(text)
    except _AmbiguousMappingError:
        data = yaml.safe_load(text)
        if isinstance(data, dict) and "schema_version" in data:
            raise
        return data


def is_versioned(data: dict) -> bool:
    return "schema_version" in data


def _id(value, label):
    if not isinstance(value, str) or not re.fullmatch(ID_PATTERN, value):
        raise ValueError(f"{label} must be an ID of letters, digits, hyphens or underscores")


def _mapping(value, label):
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a mapping")
    return value


def validate_manifest_schema(data: dict) -> None:
    """Raise ValueError for an invalid versioned manifest; no-op for legacy ones."""
    if not is_versioned(data):
        return
    version = data["schema_version"]
    if type(version) is not int or version != MANIFEST_SCHEMA_VERSION:
        raise ValueError(f"schema_version must be {MANIFEST_SCHEMA_VERSION}")
    stack = _mapping(data.get("technology_stack", {}), "technology_stack")
    repositories = _mapping(stack.get("repositories", {}), "technology_stack.repositories")
    for alias, technologies in repositories.items():
        label = f"technology_stack.repositories.{alias}"
        _id(alias, "technology_stack.repositories alias")
        for tech, exact in _mapping(technologies, label).items():
            _id(tech, f"{label} technology")
            if not isinstance(exact, str) or not re.fullmatch(VERSION_PATTERN, exact):
                raise ValueError(f"{label}.{tech} must be an exact version string")
    ai = _mapping(data.get("ai", {}), "ai")
    tools = ai.get("tools")
    if "tools" in ai:
        if not isinstance(tools, list) or not tools:
            raise ValueError("ai.tools must be a nonempty list of tool IDs")
        for tool in tools:
            _id(tool, "ai.tools entry")
        if len(set(tools)) != len(tools):
            raise ValueError("ai.tools contains duplicate IDs")
    if "default_tool" in ai:
        _id(ai["default_tool"], "ai.default_tool")
        if tools and ai["default_tool"] not in tools:
            raise ValueError("ai.default_tool must be listed in ai.tools")
    for key in ("routing_policy", "context_policy", "default_profile", "budget_policy"):
        if key in ai:
            _id(ai[key], f"ai.{key}")
    bindings = _mapping(ai.get("tool_bindings", {}), "ai.tool_bindings")
    for tool, profiles in bindings.items():
        _id(tool, "ai.tool_bindings tool")
        if tools and tool not in tools:
            raise ValueError(f"ai.tool_bindings.{tool} is not listed in ai.tools")
        for profile, binding in _mapping(profiles, f"ai.tool_bindings.{tool}").items():
            label = f"ai.tool_bindings.{tool}.{profile}"
            _id(profile, "ai.tool_bindings profile")
            _mapping(binding, label)
            if set(binding) - {"model", "effort"}:
                raise ValueError(f"{label} allows only model and effort")
            model = binding.get("model")
            if not isinstance(model, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/@+-]*", model):
                raise ValueError(f"{label}.model must be a model identifier")
            effort = _mapping(binding.get("effort", {}), f"{label}.effort")
            for level, native in effort.items():
                if level not in EFFORT_LEVELS:
                    raise ValueError(f"{label}.effort keys must be one of {', '.join(EFFORT_LEVELS)}")
                if not isinstance(native, str) or not re.fullmatch(ID_PATTERN, native):
                    raise ValueError(f"{label}.effort.{level} must be a native effort identifier")


    validate_delivery(data.get("delivery", {}), repositories)

def _relative_path(value, label):
    if not isinstance(value, str) or not value.strip() or "\0" in value or "\\" in value:
        raise ValueError(f"{label} must be a nonempty relative path")
    parts = value.split("/")
    if value.startswith("/") or ".." in parts:
        raise ValueError(f"{label} must point inside the project")

def validate_delivery(delivery, repositories: dict) -> None:
    """Validate the optional delivery mode; see framework/governance/delivery-modes/."""
    delivery = _mapping(delivery, "delivery")
    if set(delivery) - {"mode", "decision_ref", "prototype_first"}:
        raise ValueError("delivery allows only mode, decision_ref and prototype_first")
    mode = delivery.get("mode", DELIVERY_STANDARD)
    if mode not in DELIVERY_MODES:
        raise ValueError(f"delivery.mode must be one of {', '.join(DELIVERY_MODES)}")
    if mode == DELIVERY_STANDARD:
        return
    _id(delivery.get("decision_ref"), "delivery.decision_ref")
    options = _mapping(delivery.get("prototype_first", {}), "delivery.prototype_first")
    if set(options) - {"deferred_gates", "sources", "ux_improvements", "merge_policy"}:
        raise ValueError("delivery.prototype_first allows only deferred_gates, sources, ux_improvements "
                         "and merge_policy")
    gates = options.get("deferred_gates", list(DEFERRABLE_GATES))
    if (not isinstance(gates, list) or not gates or len(set(gates)) != len(gates)
            or any(gate not in DEFERRABLE_GATES for gate in gates)):
        raise ValueError(f"delivery.prototype_first.deferred_gates must be a nonempty subset of "
                         f"{', '.join(DEFERRABLE_GATES)}")
    if options.get("ux_improvements", UX_IMPROVEMENT_MODES[0]) not in UX_IMPROVEMENT_MODES:
        raise ValueError(f"delivery.prototype_first.ux_improvements must be one of {', '.join(UX_IMPROVEMENT_MODES)}")
    if options.get("merge_policy", MERGE_POLICIES[0]) not in MERGE_POLICIES:
        raise ValueError(f"delivery.prototype_first.merge_policy must be one of {', '.join(MERGE_POLICIES)}")
    sources = _mapping(options.get("sources"), "delivery.prototype_first.sources")
    if set(sources) - {"prototype", "srs", "ui_base"}:
        raise ValueError("delivery.prototype_first.sources allows only prototype, srs and ui_base")
    if not any(key in sources for key in ("prototype", "srs")):
        raise ValueError("delivery.prototype_first.sources needs a prototype or an srs")
    for key in ("prototype", "srs"):
        if key in sources:
            _relative_path(sources[key], f"delivery.prototype_first.sources.{key}")
    if "ui_base" in sources:
        _id(sources["ui_base"], "delivery.prototype_first.sources.ui_base")
        if sources["ui_base"] not in repositories:
            raise ValueError("delivery.prototype_first.sources.ui_base must be a technology_stack.repositories alias")

def delivery_mode(data: dict) -> str:
    """Return the delivery mode, defaulting to the standard gated flow."""
    delivery = data.get("delivery") or {}
    return delivery.get("mode", DELIVERY_STANDARD) if isinstance(delivery, dict) else DELIVERY_STANDARD

def ai_policy_ids(data: dict) -> dict:
    """Return routing/context policy IDs with defaults applied."""
    ai = data.get("ai") or {}
    return {key: ai.get(key, default) for key, default in AI_POLICY_DEFAULTS.items()}
