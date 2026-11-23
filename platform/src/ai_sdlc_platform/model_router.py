"""Resolve static routing policy without binding to or calling a provider."""
from pathlib import Path

from yaml import YAMLError

from .config import load_yaml


class RoutingError(ValueError):
    """Routing cannot be resolved automatically from the v1 policy."""


def _policy(root: Path, filename: str) -> dict:
    try:
        data = load_yaml(root / filename, required=True)
    except (OSError, YAMLError, ValueError) as error:
        raise RoutingError(f"Could not load {filename}: {error}") from error
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise RoutingError(f"{filename}: expected schema_version 1")
    return data


def _mapping(data: dict, key: str) -> dict:
    mapping = data.get(key)
    if not isinstance(mapping, dict):
        raise RoutingError(f"{key} must be a mapping")
    return mapping


def _names(value) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)


class ModelRouter:
    def __init__(self, shared_ai: Path):
        root = shared_ai / "model-routing"
        self.tasks = _mapping(_policy(root, "task-model-mapping.yaml"), "tasks")
        self.profiles = _mapping(_policy(root, "model-profiles.yaml"), "profiles")
        effort = _policy(root, "effort-policy.yaml")
        levels = effort.get("levels")
        if not _names(levels) or not levels or len(levels) != len(set(levels)):
            raise RoutingError("levels must be a nonempty, ordered list of unique effort names")
        self.levels = levels
        self.risk_floors = _mapping(effort, "risk_floors")
        fallback = _policy(root, "fallback-policy.yaml")
        self.fallbacks = _mapping(fallback, "fallbacks")
        self.max_fallbacks = fallback.get("max_fallbacks")
        if type(self.max_fallbacks) is not int or self.max_fallbacks < 0:
            raise RoutingError("max_fallbacks must be a nonnegative integer")

    def route(self, task_type: str, effort: str | None = None, *, risk: str | None = None) -> dict:
        if not isinstance(task_type, str) or task_type not in self.tasks:
            raise RoutingError(f"Unknown task {task_type!r}; select an approved route manually")
        task = self.tasks[task_type]
        if not isinstance(task, dict):
            raise RoutingError(f"Task {task_type!r} must define profile and effort")
        profile_id = task.get("profile")
        if not isinstance(profile_id, str) or profile_id not in self.profiles:
            raise RoutingError(f"Undefined model profile {profile_id!r} for task {task_type!r}")
        profile = self.profiles[profile_id]
        required = self._capabilities(profile_id)
        default_effort = task.get("effort")
        if default_effort not in self.levels:
            raise RoutingError(f"Invalid default effort {default_effort!r} for task {task_type!r}")
        effective = default_effort
        if effort is not None:
            effective = self._higher_effort(effective, effort)
        if risk is not None:
            if not isinstance(risk, str) or risk not in self.risk_floors:
                raise RoutingError(f"Unknown risk {risk!r}; classify it before routing")
            effective = self._higher_effort(effective, self.risk_floors[risk])

        configured = self.fallbacks.get(profile_id, [])
        if not _names(configured):
            raise RoutingError(f"Fallbacks for {profile_id!r} must be a list of profile names")
        # These are candidates only: an adapter must still enforce its binding and retry policy.
        candidates = [candidate for candidate in dict.fromkeys(configured)
                      if candidate != profile_id and required <= self._capabilities(candidate)]
        return {**profile, "required_capabilities": list(profile["required_capabilities"]),
                "task_type": task_type, "profile_id": profile_id, "effort": effective,
                "fallback": candidates[:self.max_fallbacks]}

    def _higher_effort(self, minimum: str, requested: str) -> str:
        if requested not in self.levels:
            raise RoutingError(f"Unsupported effort {requested!r}; expected one of {self.levels}")
        return max((minimum, requested), key=self.levels.index)

    def _capabilities(self, profile_id: str) -> set[str]:
        profile = self.profiles.get(profile_id)
        if not isinstance(profile, dict) or not _names(profile.get("required_capabilities")):
            raise RoutingError(f"Profile {profile_id!r} must define required_capabilities")
        return set(profile["required_capabilities"])
