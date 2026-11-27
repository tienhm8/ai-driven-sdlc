from pathlib import Path
import re

import yaml

from .manifest_schema import parse_manifest_text, validate_manifest_schema


PROJECT_MANIFEST = Path(".ai-sdlc/project.yaml")
PROJECT_ID_PATTERN = r"[A-Za-z0-9][A-Za-z0-9_-]*"
DEFAULT_LOCAL_RESOURCES = {
    "rules": ".ai-sdlc/rules",
    "skills": ".ai-sdlc/skills",
}


def load_project_manifest(project_root: Path) -> dict:
    """Load the canonical project manifest and validate its core fields."""
    manifest = project_root / PROJECT_MANIFEST
    data = parse_manifest_text(manifest.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Project manifest must be a YAML mapping")
    project = data.get("project")
    if not isinstance(project, dict):
        raise ValueError("project must be a mapping with id and name")
    project_id = project.get("id")
    if not isinstance(project_id, str) or not re.fullmatch(PROJECT_ID_PATTERN, project_id):
        raise ValueError("project.id must start with a letter or digit and contain only letters, digits, hyphens or underscores")
    name = project.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("project.name must be a nonempty string")
    if not isinstance(data.get("technology_stack", {}), dict):
        raise ValueError("technology_stack must be a mapping")
    validate_manifest_schema(data)
    return data


def resolve_local_resources(project_root: Path, manifest: dict, *, kinds=tuple(DEFAULT_LOCAL_RESOURCES)) -> dict[str, Path]:
    """Resolve configured resource directories relative to the project root."""
    ai = manifest.get("ai", {})
    if not isinstance(ai, dict):
        raise ValueError("ai must be a mapping")
    local = ai.get("local_resources", {})
    if not isinstance(local, dict):
        raise ValueError("ai.local_resources must be a mapping")
    root = project_root.resolve()
    paths = {}
    for kind in kinds:
        key = f"{kind}_path"
        value = local.get(key, DEFAULT_LOCAL_RESOURCES[kind])
        if not isinstance(value, str) or not value.strip() or "\0" in value:
            raise ValueError(f"ai.local_resources.{key} must be a nonempty relative path")
        relative = Path(value)
        if relative.is_absolute() or ".." in relative.parts or not relative.parts:
            raise ValueError(f"ai.local_resources.{key} must point to a directory inside the project")
        path = (root / relative).resolve()
        if path == root or not path.is_relative_to(root):
            raise ValueError(f"ai.local_resources.{key} must point to a directory inside the project")
        if path.exists() and not path.is_dir():
            raise ValueError(f"ai.local_resources.{key} is not a directory: {value}")
        paths[kind] = path
    return paths


def allow_mandatory_rule_overrides(manifest: dict) -> bool:
    governance = manifest.get("governance", {})
    if not isinstance(governance, dict):
        raise ValueError("governance must be a mapping")
    key = "allow_project_override_mandatory_rules"
    value = governance.get(key, False)
    if not isinstance(value, bool):
        raise ValueError(f"governance.{key} must be a boolean")
    return value


def resource_roots(shared_root: Path | None, project_root: Path, kind: str, *, manifest: dict | None = None):
    if manifest is None:
        manifest = load_project_manifest(project_root)
    local_root = resolve_local_resources(project_root, manifest, kinds=(kind,))[kind]
    if shared_root is not None:
        yield "shared", shared_root.resolve()
    yield "project", local_root

def resource_files(root: Path, pattern: str):
    for path in sorted(root.rglob(pattern)):
        if path.is_file() and path.resolve().is_relative_to(root):
            yield path


def load_yaml(path: Path, required=False):
    if not path.exists():
        if required: raise FileNotFoundError(path)
        return {}
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict): raise ValueError(f"YAML root must be a mapping: {path}")
    return value

def deep_merge(base, override):
    out = dict(base)
    for key, value in override.items():
        out[key] = deep_merge(out[key], value) if isinstance(value, dict) and isinstance(out.get(key), dict) else value
    return out
