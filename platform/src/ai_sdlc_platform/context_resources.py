"""Deterministic, metadata-first context selection for the two pilot stacks."""
from fnmatch import fnmatchcase
import os
from pathlib import Path
import re

from .context_workspace import relative_path
from .manifest_schema import strict_yaml_mapping


# Skill compatibility uses the technology baselines in SKILL.md metadata.
STACK_TASKS = {"code-generation", "testing", "code-review"}
STACK_BASELINES = {"nestjs": {"nestjs"}, "umi-max": {"umi-max", "react", "antd"}, "react": {"react"}}
TASK_SKILLS = {"documentation", "requirement-analysis", "system-design", "testing", "code-review"}
FOCUS = {
    "dto": ("nestjs", "dto-validation"), "query": ("nestjs", "controller-service-repository"),
    "di": ("nestjs", "dependency-injection"), "transport": ("nestjs", "microservice-transports"),
    "auth": ("nestjs", "authentication"), "authorization": ("nestjs", "authentication"),
    "table": ("umi-max", "forms-tables"), "request": ("umi-max", "data-fetching"),
    "route": ("umi-max", "routing-access"),
}
FOCUS_TAGS = frozenset(FOCUS) | {"component", "contract", "migration", "security", "ci"}


def safe_file(root: Path, rel: str) -> Path:
    path = root / relative_path(rel)
    try:
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Resource escapes its root: {rel}")
        if not path.is_file():
            raise ValueError(f"Missing resource: {rel}")
    except RuntimeError as exc:
        raise ValueError(f"Cannot resolve resource: {rel}") from exc
    return path


def metadata(path: Path) -> dict:
    with path.open("rb") as stream:
        if stream.readline(6).rstrip(b"\r\n") != b"---":
            return {}
        header = bytearray()
        while line := stream.readline(16385 - len(header)):
            if line.rstrip(b"\r\n") == b"---":
                return strict_yaml_mapping(header.decode("utf-8")) if header.strip() else {}
            header.extend(line)
            if len(header) > 16384:
                break
    raise ValueError("Unterminated or oversized resource frontmatter")


def _resource_paths(root, *patterns, exclude=(), skill_catalog=False):
    if not root.is_dir():
        return
    paths = []
    def on_error(error):
        raise error

    for directory, dirs, files in os.walk(root, onerror=on_error):
        base = Path(directory)
        if base == root:
            dirs[:] = [name for name in dirs if name not in exclude]
        if skill_catalog and "SKILL.md" in files:
            paths.append((base / "SKILL.md").relative_to(root).as_posix())
            dirs.clear()  # references/examples are not part of catalog discovery
            continue
        for name in (*dirs, *files):
            path = base / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() and not path.resolve().is_relative_to(root.resolve()):
                raise ValueError(f"Resource escapes its root: {rel}")
            if name in files and any(fnmatchcase(name, pattern) for pattern in patterns):
                paths.append(rel)
    for rel in sorted(paths):
        yield rel, safe_file(root, rel)


def _strings(value, field):
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise ValueError(f"{field} must be a list of nonempty strings")
    return value


def _rule_matches(meta, request):
    scope = meta.get("scope", {})
    if not isinstance(scope, dict) or set(scope) - {"repos", "paths", "tasks", "stages"}:
        raise ValueError("Rule scope allows only repos, paths, tasks and stages")
    scope = {field: _strings(values, field) for field, values in scope.items()}
    patterns = [relative_path(pattern) for pattern in scope.get("paths", [])]
    matches = all(field not in scope or actual in scope[field]
                  for field, actual in (("repos", request.repo), ("tasks", request.task), ("stages", request.stage)))
    return matches and ("paths" not in scope or any(fnmatchcase(path, pattern) for pattern in patterns
                                                     for path in request.paths))


def select_rules(shared: Path, local: Path, framework: Path, request) -> list[dict]:
    shared = shared / "rules"
    selected, ids = [], set()
    for layer in ("core", "sdlc"):
        safe_file(shared, f"{layer}/README.md")
        for member, _ in _resource_paths(shared / layer, "*.md"):
            rel = f"{layer}/{member}"
            safe_file(shared, rel)
            ids.add(rel.removesuffix(".md"))
            selected.append({"id": rel.removesuffix(".md"), "source": "shared", "path": rel,
                             "selected": True, "reason": "mandatory"})
    for name in ("workflow.md", "human-review.md", "ai-instructions.md"):
        path = f"{request.stage}/{name}"
        safe_file(framework, path)
        selected.append({"id": path.removesuffix(".md"), "source": "framework", "path": path,
                         "selected": True, "reason": "stage-guidance"})
    active = {entry["id"] for entry in selected}
    conflicts = []
    for source, root in (("shared", shared), ("project", local)):
        patterns = ("*.md",) if source == "shared" else ("*.md", "*.mdc")
        skip = {"core", "sdlc"} if source == "shared" else ()
        for rel, path in _resource_paths(root, *patterns, exclude=skip):
            default_id = Path(rel).with_suffix("").as_posix()
            if source == "project" and rel.partition("/")[0] in {"core", "sdlc"}:
                selected.append({"id": default_id, "source": source, "path": rel,
                                 "selected": False, "reason": "reserved-mandatory-namespace"})
                continue
            meta = metadata(path)
            rule_id = meta.get("id", default_id)
            if (not isinstance(rule_id, str) or not re.fullmatch(r"[A-Za-z0-9_/-]+", rule_id)
                    or relative_path(rule_id) != rule_id):
                raise ValueError("Invalid rule ID")
            if rule_id in ids or rule_id in active or rule_id.split("/")[0] in {"core", "sdlc"}:
                raise ValueError(f"Rule ID collision or reserved ID: {rule_id}")
            ids.add(rule_id)
            matches = _rule_matches(meta, request)
            if source == "project" and rel.endswith(".mdc") and {"globs", "alwaysApply"} & meta.keys() and "scope" not in meta:
                raise ValueError(f"Local rule requires explicit resolver scope: {rel}")
            if source == "shared" and rel == "engineering/validation-evidence.md":
                matches = matches and request.task in {"code-generation", "testing", "code-review"}
            selected.append({"id": rule_id, "source": source, "path": rel, "selected": matches,
                             "reason": "scope-matched" if matches else "scope-not-matched"})
            if matches:
                active.add(rule_id)
                conflicts.extend((rule_id, other) for other in _strings(meta.get("conflicts", []), "conflicts"))
    for rule_id, other in conflicts:
        if other not in ids and other not in active:
            raise ValueError(f"Unknown conflict target for rule {rule_id}: {other}")
        if other in active:
            raise ValueError(f"Unresolved rule conflict: {rule_id} and {other}")
    return selected


def select_skills(shared: Path, local: Path, request, stack: dict, observed: dict) -> list[dict]:
    desired = {}
    if request.task in TASK_SKILLS:
        desired[request.task] = "task-matched"
    for skill in STACK_BASELINES:
        if request.task in STACK_TASKS and skill in stack and (skill != "react" or "component" in request.focus):
            desired[skill] = "stack-and-task-matched"
    for tag, skill in (("auth", "authentication"), ("authorization", "authorization"), ("security", "owasp"),
                       ("migration", "database-migration"), ("contract", "microservices"), ("ci", "gitlab-ci")):
        if tag in request.focus:
            desired[skill] = "focus-matched"
    result, ids = [], set()
    for source, root in (("shared", shared / "skills"), ("project", local)):
        for rel, path in _resource_paths(root, "SKILL.md", skill_catalog=True):
            meta = metadata(path)
            skill = meta.get("name")
            if (not isinstance(skill, str) or skill != path.parent.name
                    or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill)
                    or not isinstance(meta.get("description"), str) or not meta["description"].strip()):
                raise ValueError(f"Invalid skill metadata: {rel}")
            if skill in ids:
                raise ValueError(f"Duplicate skill ID: {skill}")
            ids.add(skill)
            details = meta.get("metadata", {})
            if not isinstance(details, dict):
                raise ValueError(f"Invalid skill metadata: {rel}")
            baselines = {tech: details[f"{tech}-version"] for tech in ("nestjs", "umi-max", "react", "antd")
                         if f"{tech}-version" in details}
            if not STACK_BASELINES.get(skill, set()) <= baselines.keys():
                raise ValueError(f"Missing skill technology baseline: {rel}")
            if any(not isinstance(version, str) for version in baselines.values()):
                raise ValueError(f"Skill technology versions must be strings: {rel}")
            reason = desired.get(skill, "not-triggered")
            apply = skill in desired or (source == "project" and "scope" in meta and _rule_matches(meta, request))
            if apply and skill not in desired:
                reason = "scope-matched"
            if apply and any(observed.get(tech) != expected or stack.get(tech) != expected
                             for tech, expected in baselines.items()):
                apply, reason = False, "stack-version-unverified-or-incompatible"
            references = []
            if apply:
                for owner, filename in (FOCUS[tag] for tag in sorted(request.focus & FOCUS.keys())):
                    if owner == skill:
                        references.append(f"references/{filename}.md")
                references = list(dict.fromkeys(references))
                for ref in references:
                    safe_file(path.parent, ref)
            version = details.get("version")
            if version is not None and not isinstance(version, str):
                raise ValueError(f"Skill content version must be a string: {rel}")
            result.append({"id": skill, "source": source, "path": rel, "baselines": baselines, "version": version,
                           "selected": apply, "reason": reason, "references": references})
    missing = desired.keys() - ids
    if missing:
        raise ValueError("Missing required skill metadata: " + ", ".join(sorted(missing)))
    active = {row["id"] for row in result if row["selected"]}
    for row in result:
        if not row["selected"] or row["id"] not in {"testing", "code-review"}:
            continue
        root = shared / "skills" if row["source"] == "shared" else local
        for skill, test_ref, review_ref in (("nestjs", "backend-nestjs", "review-backend"),
                                            ("umi-max", "frontend-umi-max", "review-frontend")):
            if skill in active:
                ref = f"references/{test_ref if row['id'] == 'testing' else review_ref}.md"
                safe_file((root / row["path"]).parent, ref)
                row["references"].append(ref)
    order = {skill: index for index, skill in enumerate(desired)}
    return sorted(result, key=lambda item: (not item["selected"], order.get(item["id"], len(order)), item["id"]))
