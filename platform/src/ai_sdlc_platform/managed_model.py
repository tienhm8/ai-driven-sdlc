"""Guard a single inference operation with trusted transport and preflight ports.

No transport is bundled or discovered from the project. A transport must send at
most one request per invocation: no tools, implicit retries, or provider fallback.
"""
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from hashlib import sha256
import math
from pathlib import Path
import re
from time import sleep
from uuid import uuid4

from yaml import YAMLError

from .config import load_project_manifest
from .context_resolver import ContextRequest, effective_risk, resolve_context
from .manifest_schema import ai_policy_ids
from .model_router import ModelRouter
from .tool_adapters import ToolAdapterRegistry
from .tool_binding import BindingError, BoundRoute, ToolBinder


@dataclass(frozen=True)
class Attempt:
    run_id: str
    number: int
    cause: str
    project: Path
    request: ContextRequest
    risk: str
    route: BoundRoute
    payload_sha256: str
    budget_policy: str | None


@dataclass(frozen=True)
class Observation:
    """Transport observations, not values copied from the request or model text."""
    model: str | None = None
    native_effort: str | None = None


@dataclass(frozen=True)
class ToolReply:
    status: str
    content: str | None = None
    observed: Observation = Observation()
    safe_to_repeat: bool = False
    retry_after_seconds: float | None = None


@dataclass(frozen=True)
class ManagedResult:
    status: str
    reason: str
    attempts: tuple[dict, ...]
    content: str | None = None


_STATUSES = {"ok", "rate_limited", "temporarily_unavailable", "refusal", "permission_denied",
             "invalid_request", "budget_exceeded", "unknown_error"}
_OBSERVED_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/@+-]{0,127}")


def _observed_id(value):
    return value if isinstance(value, str) and _OBSERVED_ID.fullmatch(value) else None


class ManagedModelRunner:
    def __init__(self, project: Path, framework: Path, shared: Path, workspace: dict, state_dir: Path, *,
                 adapters: ToolAdapterRegistry, transports: Mapping[str, Callable[[BoundRoute, bytes], ToolReply]],
                 authorize_scope: Callable[[Attempt], bool], allow_data: Callable[[Attempt, bytes], bool],
                 allow_budget: Callable[[Attempt], bool], audit: Callable[[dict], None],
                 wait: Callable[[float], None] = sleep):
        self.project = project.resolve()
        self.framework = framework
        self.shared = shared
        self.workspace = workspace
        self.state_dir = state_dir
        self.adapters = adapters
        self.transports = dict(transports)
        self.authorize_scope = authorize_scope
        self.allow_data = allow_data
        self.allow_budget = allow_budget
        self.audit = audit
        self.wait = wait
        self._check_registry_location()

    def _check_registry_location(self):
        workspaces = [self.project, *(Path(entry["checkout"]).resolve()
                                     for entry in self.workspace.get("repositories", {}).values())]
        self.adapters.require_outside(workspaces)
        if any(self.state_dir.resolve().is_relative_to(path) for path in workspaces):
            raise ValueError("Governance state must be outside the managed workspaces")

    def run(self, request: ContextRequest, payload: bytes) -> ManagedResult:
        request.validate()
        attempts = []

        def stop(status, reason, content=None):
            return ManagedResult(status, reason, tuple(attempts), content)

        if not isinstance(payload, bytes) or not payload.strip():
            return stop("blocked", "MISSING_PAYLOAD")
        # A read-only model call cannot stand in for the merge action, and code
        # generation must not be relabelled as preparation to skip G3.
        if request.action == "merge" or (request.task == "code-generation" and request.action != "coding"):
            return stop("blocked", "MANAGED_ACTION_MISMATCH")
        run_id = uuid4().hex
        digest = sha256(payload).hexdigest()
        risk = effective_risk(request)

        def route_for(cause, original=None):
            self._check_registry_location()
            plan = resolve_context(self.project, self.framework, self.shared, self.workspace, self.state_dir, request)
            if plan["blockers"]:
                raise BindingError(plan["blockers"][0]["code"])
            ai = load_project_manifest(self.project).get("ai", {})
            if ai_policy_ids({"ai": ai})["routing_policy"] != "default":
                raise BindingError("UNKNOWN_ROUTING_POLICY")
            router = ModelRouter(self.shared)
            static = router.route(request.task, risk=risk)
            limits = router.attempt_limits()
            binder = ToolBinder(self.adapters, router)
            primary = binder.primary(ai, static)
            if original is not None and primary != original:
                raise BindingError("ROUTE_CHANGED")
            bound = primary
            if cause == "fallback":
                available = {name for name, transport in self.transports.items() if callable(transport)}
                bound = binder.fallback(ai, static, primary, available_tools=available) if limits[1] else None
                if bound is None:
                    raise BindingError("NO_APPROVED_FALLBACK")
            return bound, limits, ai.get("budget_policy")

        cause = "initial"
        primary = None
        pending_delay = 0
        previous_status = None
        while True:
            if pending_delay:
                try:
                    self.wait(pending_delay)
                except Exception:
                    return stop("manual", "RETRY_DELAY_UNAVAILABLE")
            try:
                bound, (max_retries, max_fallbacks, retryable), budget_policy = route_for(cause, primary)
            except BindingError as exc:
                return stop("manual" if exc.code == "NO_APPROVED_FALLBACK" else "blocked", exc.code)
            except (OSError, ValueError, RuntimeError, YAMLError):
                return stop("blocked", "ROUTING_POLICY_UNAVAILABLE")
            if cause == "retry" and (not max_retries or previous_status not in retryable):
                return stop("manual", "RETRY_NO_LONGER_ALLOWED")
            if cause == "fallback" and previous_status not in retryable:
                return stop("manual", "FALLBACK_NO_LONGER_ALLOWED")
            if primary is None:
                primary = bound
            transport = self.transports.get(bound.tool)
            if not callable(transport):
                return stop("blocked", "TRANSPORT_NOT_REGISTERED")
            attempt = Attempt(run_id, len(attempts) + 1, cause, self.project, request, risk, bound, digest, budget_policy)
            event = {"run_id": run_id, "attempt": attempt.number, "cause": cause, "work_item_id": request.work_item_id,
                     "repo": request.repo, "revision": request.revision, "stage": request.stage, "task": request.task, "risk": risk,
                     "tool": bound.tool, "profile": bound.profile, "requested_model": bound.model,
                     "requested_effort": bound.effort, "requested_native_effort": bound.native_effort,
                     "effective_model": None, "effective_effort": None, "effective_native_effort": None,
                     "observation": "unverified", "previous_status": previous_status}
            for check, reason in ((lambda: self.authorize_scope(attempt), "SCOPE_DENIED"),
                                  (lambda: self.allow_data(attempt, payload), "DATA_DENIED"),
                                  (lambda: self.allow_budget(attempt), "BUDGET_NOT_APPROVED")):
                try:
                    allowed = check() is True
                except Exception:
                    allowed = False
                if not allowed:
                    return stop("blocked", reason)
            try:
                self.audit({**event, "status": "preflight_passed"})
            except Exception:
                return stop("blocked", "AUDIT_UNAVAILABLE")
            try:
                reply = transport(bound, payload)
            except Exception:
                # Unknown outcomes can already have incurred cost. Do not retry them.
                reply = ToolReply("unknown_error")
            if (not isinstance(reply, ToolReply) or not isinstance(reply.status, str)
                    or reply.status not in _STATUSES or not isinstance(reply.observed, Observation)
                    or (reply.status == "ok" and not isinstance(reply.content, str))):
                reply = ToolReply("unknown_error")
            observed_model = _observed_id(reply.observed.model)
            observed_effort = _observed_id(reply.observed.native_effort)
            level = bound.planned_effort if observed_effort is not None and observed_effort == bound.native_effort else None
            mismatch = ((observed_model is not None and observed_model != bound.model)
                        or (bound.native_effort is not None and observed_effort is not None
                            and observed_effort != bound.native_effort))
            verified = observed_model == bound.model and level is not None
            incomplete = reply.status == "ok" and (observed_model is None or (not verified and bound.planned_effort is not None))
            status = "route_mismatch" if mismatch else "route_unverified" if incomplete else reply.status
            event.update(effective_model=observed_model, effective_effort=level, effective_native_effort=observed_effort,
                         observation="mismatch" if mismatch else "verified" if verified else "unverified",
                         status=status)
            attempts.append(event)
            try:
                self.audit(dict(event))
            except Exception:
                return stop("manual", "AUDIT_UNAVAILABLE_AFTER_DISPATCH")
            if mismatch:
                return stop("manual", "OBSERVED_ROUTE_MISMATCH")
            if incomplete:
                return stop("manual", "EFFECTIVE_ROUTE_UNVERIFIED")
            if reply.status == "ok":
                return stop("completed", "OK", reply.content)
            if (reply.status not in retryable or reply.safe_to_repeat is not True or reply.content is not None
                    or bound.planned_effort is None):
                # An uncontrolled default has no comparable actual effort to preserve.
                return stop("manual", reply.status.upper())
            delay = reply.retry_after_seconds
            if delay is not None and (type(delay) not in {int, float} or not 0 <= delay <= 120 or not math.isfinite(delay)):
                return stop("manual", "RETRY_DELAY_OUT_OF_RANGE")
            if cause == "initial" and max_retries:
                cause = "retry"
            elif cause != "fallback" and max_fallbacks:
                cause = "fallback"
            else:
                return stop("manual", "ATTEMPT_POLICY_EXHAUSTED")
            previous_status = reply.status
            pending_delay = delay or 0
