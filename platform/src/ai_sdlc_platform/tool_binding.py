"""Bind portable routing profiles to operator-approved tool settings, without I/O to providers."""
from dataclasses import dataclass
import re

from yaml import YAMLError

from .manifest_schema import ID_PATTERN
from .model_router import ModelRouter, RoutingError
from .tool_adapters import ToolAdapterRegistry


class BindingError(RoutingError):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


@dataclass(frozen=True)
class BoundRoute:
    tool: str
    model: str
    profile: str
    effort: str
    planned_effort: str | None
    native_effort: str | None
    capabilities: frozenset[str]
    data_policy: str
    source: str
    capability_evidence: str

    @property
    def identity(self):
        return self.tool, self.model

    def preview(self) -> dict:
        return {"tool": self.tool, "model": self.model, "profile": self.profile, "effort": self.effort,
                "planned_effort": self.planned_effort, "native_effort": self.native_effort,
                "binding_source": self.source, "data_policy": self.data_policy,
                "capability_evidence": self.capability_evidence, "status": "bound-preview"}


def _identifier(value, pattern=ID_PATTERN):
    return isinstance(value, str) and re.fullmatch(pattern, value) is not None


def _names(value):
    return isinstance(value, list) and all(_identifier(name) for name in value)


class ToolBinder:
    def __init__(self, registry: ToolAdapterRegistry, router: ModelRouter):
        self.registry = registry
        self.router = router
        self.levels = tuple(router.levels)

    def primary(self, ai: dict, route: dict) -> BoundRoute:
        tool = ai.get("default_tool", (ai.get("tools") or ["claude"])[0])
        return self._bind(ai, route, tool, route["profile_id"])

    def fallback(self, ai: dict, route: dict, primary: BoundRoute, *, available_tools) -> BoundRoute | None:
        tools = list(dict.fromkeys([primary.tool, *(ai.get("tools") or [])]))
        for profile in route["fallback"]:
            for tool in tools:
                if tool not in available_tools:
                    continue
                try:
                    candidate = self._bind(ai, route, tool, profile, fallback=True)
                except BindingError:
                    continue
                if (candidate.identity != primary.identity and candidate.data_policy == primary.data_policy
                        and candidate.capabilities >= primary.capabilities and self._preserves_effort(candidate, primary)):
                    return candidate
        return None

    def _preserves_effort(self, candidate: BoundRoute, primary: BoundRoute) -> bool:
        return (candidate.planned_effort in self.levels and
                (primary.planned_effort is None or self.levels.index(candidate.planned_effort)
                 >= self.levels.index(primary.planned_effort)))

    def _bind(self, ai, route, tool, profile, *, fallback=False):
        try:
            adapter = self.registry.managed(tool)
        except (OSError, ValueError, RuntimeError, YAMLError):
            raise BindingError("TOOL_NOT_APPROVED") from None
        routing = adapter.get("routing")
        if not isinstance(routing, dict):
            raise BindingError("TOOL_ROUTE_UNVERIFIED")
        binding = ai.get("tool_bindings", {}).get(tool, {}).get(profile)
        if fallback and binding is None:
            raise BindingError("FALLBACK_NOT_EXPLICIT")
        model = binding["model"] if binding else routing.get("default_model")
        models = routing.get("models")
        record = models.get(model) if isinstance(models, dict) and isinstance(model, str) else None
        if not isinstance(record, dict) or not _identifier(model, r"[A-Za-z0-9][A-Za-z0-9._:/@+-]{0,127}"):
            raise BindingError("MODEL_NOT_APPROVED")
        caps, profiles = record.get("capabilities"), record.get("profiles")
        data_policy, evidence = record.get("data_policy"), record.get("capability_evidence")
        if (not _names(caps) or not _names(profiles) or not _identifier(data_policy)
                or not _identifier(evidence, r"[A-Za-z0-9][A-Za-z0-9._:/#@+-]*")):
            raise BindingError("TOOL_ROUTE_UNVERIFIED")
        required = self.router.profile_capabilities(profile) | set(route["required_capabilities"])
        if profile not in profiles or not required <= set(caps):
            raise BindingError("CAPABILITY_UNSUPPORTED")
        mapping = record.get("effort", {})
        if (not isinstance(mapping, dict) or any(key not in self.levels or not _identifier(value)
                                                for key, value in mapping.items())
                or len(set(mapping.values())) != len(mapping)):
            raise BindingError("TOOL_ROUTE_UNVERIFIED")
        effort = route["effort"]
        native = mapping.get(effort)
        declared = binding.get("effort", {}) if binding else {}
        if any(mapping.get(key) != value for key, value in declared.items()):
            raise BindingError("NATIVE_EFFORT_NOT_APPROVED")
        planned = effort
        source = "project-binding" if binding else "approved-tool-default"
        if native is None:
            if (profile != "routine" or effort != "low" or fallback
                    or record.get("allow_uncontrolled_routine_effort") is not True):
                raise BindingError("EFFORT_UNSUPPORTED")
            planned = None
            source += ":uncontrolled-routine-effort"
        return BoundRoute(tool, model, profile, effort, planned, native, frozenset(caps), data_policy, source, evidence)
