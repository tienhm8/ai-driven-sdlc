"""Read-only Context step. An explanation never conveys execution authority."""
from contextlib import closing
from dataclasses import dataclass
from datetime import datetime, timezone
import re
from pathlib import Path
import sqlite3
import subprocess

from yaml import YAMLError

from .action_evidence import action_target
from .audit import EventStore
from .config import allow_mandatory_rule_overrides, load_project_manifest, resolve_local_resources
from .constants import STAGES
from .context_resources import FOCUS_TAGS, safe_file, select_rules, select_skills
from .context_workspace import COMMIT_ID, PACKAGES, Checkout, relative_path, within_scope
from .governance import artifact_digest, latest_review
from .manifest_schema import ID_PATTERN, ai_policy_ids
from .model_router import ModelRouter, RoutingError
from .progress import store_path
from .tool_adapters import ToolAdapterRegistry
from .tool_binding import BindingError, ToolBinder
from .workflow_engine import WorkflowEngine


@dataclass(frozen=True)
class ContextRequest:
    work_item_id: str
    repo: str
    revision: str
    role: str
    stage: str
    task: str
    risk: str
    paths: tuple[str, ...]
    focus: frozenset[str] = frozenset()
    action: str = "prepare"

    def validate(self):
        for field in ("work_item_id", "repo", "role", "task", "risk"):
            if not isinstance(value := getattr(self, field), str) or not re.fullmatch(ID_PATTERN, value):
                raise ValueError(f"Invalid {field}")
        if not isinstance(self.revision, str) or not COMMIT_ID.fullmatch(self.revision):
            raise ValueError("Revision must be a full lowercase Git commit ID")
        if self.stage not in STAGES:
            raise ValueError("Unknown stage")
        if self.action not in {"prepare", "coding", "merge"}:
            raise ValueError("Unknown action")
        if not self.paths:
            raise ValueError("At least one file or module path is required")
        for path in self.paths:
            relative_path(path)
        if self.focus - FOCUS_TAGS:
            raise ValueError("Unknown focus tag")


def _record_ref(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_./:#@+-]*", value))


def _gate_evidence(project, state_dir, request, checkout, repo_id, scope):
    gate = "G3" if request.action == "coding" else "G4"
    evidence = scope.get(gate)
    if not isinstance(evidence, dict) or evidence.get("revision") != checkout.revision:
        return {"id": gate, "status": "unverified", "reason": "missing-or-stale-review-link"}
    try:
        execution = evidence.get("execution_id")
        if not _record_ref(execution):
            raise ValueError("Missing execution link")
        artifact = artifact_digest(evidence.get("artifact_sha256"))
        context = artifact_digest(evidence.get("review_context_sha256"), field="review_context_sha256")
        db = store_path(state_dir.resolve(), project)
        EventStore(db.parent, project=project)  # Validate location without opening or creating state.
        if not db.is_file():
            return {"id": gate, "status": "unverified", "reason": "governance-store-missing"}
        with closing(sqlite3.connect(f"{db.as_uri()}?mode=ro", uri=True)) as connection:
            events = EventStore.read(connection, execution)
        active_stage = WorkflowEngine._active_stage(events)
        if active_stage != request.stage:
            return {"id": gate, "status": "unverified", "reason": "stage-does-not-match-execution"}
        review = latest_review(events, gate)
        if (not review or review["event_id"] != evidence.get("review_id")
                or review["artifact_sha256"] != artifact or review["review_context_sha256"] != context):
            return {"id": gate, "status": "unverified", "reason": "review-does-not-match-current-evidence"}
        if gate == "G3":
            record = WorkflowEngine._completed_gate(events, gate)
            if (not record or record["review_id"] != review["event_id"]
                    or record["artifact_sha256"] != artifact or record["review_context_sha256"] != context):
                return {"id": gate, "status": "unverified", "reason": "task-planning-not-completed"}
        else:
            target = action_target(gate, evidence.get("target"))
            if target["repository"] != repo_id or target != review["target"]:
                return {"id": gate, "status": "unverified", "reason": "reviewed-target-mismatch"}
            record = WorkflowEngine._authorized_action(events, gate)
            if record and record.get("expires_at") and datetime.fromisoformat(record["expires_at"]) <= datetime.now(timezone.utc):
                return {"id": gate, "status": "unverified", "reason": "authorization-expired"}
            if (not record or record["review_id"] != review["event_id"] or record["target"] != target
                    or record["artifact_sha256"] != artifact or record["review_context_sha256"] != context
                    or WorkflowEngine._action_started(events, record["event_id"])):
                return {"id": gate, "status": "unverified", "reason": "no-matching-unclaimed-authorization"}
        return {"id": gate, "status": "observed", "reason": "matching-governance-record"}
    except (OSError, ValueError, KeyError, RuntimeError, sqlite3.Error):
        return {"id": gate, "status": "unverified", "reason": "governance-evidence-unavailable"}


def effective_risk(request: ContextRequest) -> str:
    if request.risk in {"low", "medium", "high"} and request.focus & {"migration", "auth", "authorization"}:
        return "high"
    return request.risk


def resolve_context(project: Path, framework: Path, shared: Path, workspace: dict,
                    state_dir: Path, request: ContextRequest, *, adapters: ToolAdapterRegistry | None = None) -> dict:
    """Workspace records must come from a trusted integration, not the task/prompt or project manifest."""
    request.validate()
    project = project.resolve()
    result = {"work_item_id": request.work_item_id, "repo": request.repo, "revision": request.revision,
              "role": request.role, "stage": request.stage, "task": request.task, "risk": request.risk,
              "scope": sorted(set(request.paths)), "focus": sorted(request.focus), "action": request.action,
              "authority": "none", "rules": [], "skills": [], "route": None, "gate": None,
              "evidence": {}, "blockers": [], "warnings": []}

    def block(code, message):
        result["blockers"].append({"code": code, "message": message})

    def finish():
        result["status"] = "blocked" if result["blockers"] else "resolved"
        return result

    try:
        manifest = load_project_manifest(project)
        if "schema_version" not in manifest:
            block("LEGACY_MANIFEST", "Opt into the versioned context manifest; legacy loaders are unchanged.")
            return finish()
        paths = resolve_local_resources(project, manifest)
        legacy_override = allow_mandatory_rule_overrides(manifest)
        if legacy_override:
            block("LEGACY_MANDATORY_OVERRIDE", "Remove the legacy mandatory override before adopting this resolver.")
    except (OSError, ValueError, RuntimeError, YAMLError):
        block("INVALID_MANIFEST", "Validate the project manifest and local resource paths.")
        return finish()

    policies = ai_policy_ids(manifest)
    result["policies"] = {key: {"id": value, "version": 1 if value == "default" else None}
                          for key, value in policies.items()}
    ai = manifest.get("ai", {})
    if policies["routing_policy"] != "default":
        block("UNKNOWN_ROUTING_POLICY", "Only the default routing policy is implemented.")
    else:
        risk = effective_risk(request)
        try:
            router = ModelRouter(shared)
            route = router.route(request.task, risk=risk)
        except RoutingError:
            block("ROUTE_UNRESOLVED", "Check task and risk against the shared routing policy, or select a route manually.")
        else:
            tool = ai.get("default_tool", (ai.get("tools") or ["claude"])[0])
            profile = route["profile_id"]
            binding = ai.get("tool_bindings", {}).get(tool, {}).get(profile, {}) if isinstance(tool, str) else {}
            result["route"] = {"profile": profile, "effort": route["effort"], "risk": risk,
                               "tool": tool if isinstance(tool, str) and re.fullmatch(ID_PATTERN, tool) else None,
                               "model": binding.get("model", "tool-default"),
                               "native_effort": binding.get("effort", {}).get(route["effort"]),
                               "source": "shared-task-mapping", "required_capabilities": route["required_capabilities"],
                               "status": "preview-only-unverified"}
            if adapters is not None:
                try:
                    binder = ToolBinder(adapters, router)
                    bound = binder.primary(ai, route)
                except BindingError as exc:
                    result["route"]["status"] = "manual-selection-required"
                    block(exc.code, "Select a tool/model with an approved binding that meets this route.")
                else:
                    result["route"].update(bound.preview())
                    if bound.planned_effort is None:
                        result["warnings"].append({"code": "UNCONTROLLED_ROUTINE_EFFORT",
                                                   "message": "The approved routine route uses the tool's default effort."})

    repos = manifest.get("technology_stack", {}).get("repositories", {})
    if request.repo not in repos:
        block("UNKNOWN_REPO_ALIAS", "The repo alias is not declared in the project manifest.")
        return finish()
    stack = repos[request.repo]
    registry = workspace.get("repositories", {})
    record = registry.get(request.repo) if isinstance(registry, dict) else None
    if not isinstance(record, dict) or not _record_ref(repo_id := record.get("repository")):
        block("UNVERIFIED_CHECKOUT", "The repo alias is not registered in the trusted workspace.")
        return finish()
    try:
        root = Path(record.get("checkout", ""))
        if not root.is_absolute():
            raise ValueError("Expected an absolute checkout path in trusted workspace configuration")
        checkout = Checkout(root, request.revision)
        if not checkout.safe_scope(request.paths):
            block("UNSAFE_SCOPE", "The scope crosses a symlink or submodule, or could not be checked at the revision.")
            return finish()
        observed = checkout.observed_versions(stack)
    except (OSError, ValueError, RuntimeError, TypeError, subprocess.SubprocessError):
        block("UNVERIFIED_CHECKOUT", "The registered checkout or exact Git revision could not be verified.")
        return finish()
    result["stack"] = {tech: {"declared": version, "observed": observed.get(tech)}
                       for tech, version in sorted(stack.items())}
    for tech, expected in sorted(stack.items()):
        if tech in PACKAGES and observed.get(tech) != expected:
            result["warnings"].append({"code": "STACK_VERSION_MISMATCH" if tech in observed else "STACK_VERSION_UNVERIFIED",
                                       "technology": tech})

    items = workspace.get("work_items", {})
    item = items.get(request.work_item_id) if isinstance(items, dict) else None
    item = item if isinstance(item, dict) else {}
    if any(not _record_ref(item.get(key)) for key in ("backlog_ref", "version", "ac_ref", "dod_ref")):
        block("WORK_ITEM_EVIDENCE_MISSING", "Register the versioned backlog item, acceptance criteria and Definition of Done.")
    else:
        result["evidence"] = {key: item[key] for key in ("backlog_ref", "version", "ac_ref", "dod_ref")}
    scopes = item.get("repositories", {})
    scope = scopes.get(request.repo) if isinstance(scopes, dict) else None
    scope = scope if isinstance(scope, dict) else {}
    try:
        allowed = scope.get("paths", [])
        if not isinstance(allowed, list):
            raise ValueError("Expected a path list")
        prefixes = tuple(relative_path(path) for path in allowed)
    except ValueError:
        prefixes = ()
    if not all(within_scope(path, prefixes) for path in request.paths):
        block("WORK_ITEM_SCOPE_UNVERIFIED", "Requested paths must belong to the registered work-item scope for the repo.")

    if request.action != "prepare":
        expected_stage = STAGES[3] if request.action == "coding" else STAGES[4]
        if request.stage != expected_stage or (request.action == "coding" and request.task != "code-generation"):
            block("ACTION_STAGE_MISMATCH", "The selected action does not match the stage or task.")
        else:
            result["gate"] = _gate_evidence(project, state_dir, request, checkout, repo_id, scope)
            if result["gate"]["status"] != "observed":
                block("GATE_UNVERIFIED", f"{result['gate']['id']}: {result['gate']['reason']}")

    if policies["context_policy"] != "default":
        block("UNKNOWN_CONTEXT_POLICY", "Only the default context policy is implemented.")
    elif not legacy_override:
        try:
            result["rules"] = select_rules(shared, paths["rules"], framework, request)
            result["skills"] = select_skills(shared, paths["skills"], request, stack, observed)
        except ValueError as exc:
            block("CONTEXT_RESOURCE_INVALID", str(exc))
        except (OSError, RuntimeError, TypeError, YAMLError):
            block("CONTEXT_RESOURCE_INVALID", "A resource could not be discovered or parsed safely.")
    return finish()


def load_selected_context(project: Path, framework: Path, shared: Path, workspace: dict,
                          state_dir: Path, request: ContextRequest) -> list[dict]:
    """Materialize only selected content for a local consumer; grants no authority to execute."""
    plan = resolve_context(project, framework, shared, workspace, state_dir, request)
    if plan["blockers"]:
        codes = ", ".join(issue["code"] for issue in plan["blockers"])
        raise ValueError(f"Cannot materialize a blocked context: {codes}")
    local = resolve_local_resources(project, load_project_manifest(project))
    bodies, references = [], []
    for kind in ("rules", "skills"):
        for entry in plan[kind]:
            if not entry["selected"]:
                continue
            source = entry["source"]
            root = {"shared": shared / kind, "project": local[kind], "framework": framework}[source]
            path = safe_file(root, entry["path"])
            bodies.append((source, kind, root, path))
            references.extend((source, "reference", root, safe_file(path.parent, ref))
                              for ref in entry.get("references", ()))
    return [{"source": source, "kind": kind, "path": path.relative_to(root).as_posix(),
             "content": path.read_text(encoding="utf-8")}
            for source, kind, root, path in bodies + references]
