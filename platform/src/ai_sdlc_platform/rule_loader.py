from pathlib import Path

from .config import (
    allow_mandatory_rule_overrides, load_project_manifest, resource_files, resource_roots,
)


def rule_files(root: Path, *, project: bool):
    for pattern in (("*.md", "*.mdc") if project else ("*.md",)):
        yield from resource_files(root, pattern)


def is_reserved_rule(relative: Path) -> bool:
    return relative.parts[0] in {"core", "sdlc"}


def load_rules(shared_root: Path | None, project_root: Path):
    manifest = load_project_manifest(project_root)
    allow_override = allow_mandatory_rule_overrides(manifest)
    rules = {}
    for scope, root in resource_roots(shared_root, project_root, "rules", manifest=manifest):
        for path in rule_files(root, project=scope == "project"):
            relative = path.relative_to(root)
            if scope == "project" and not allow_override and is_reserved_rule(relative):
                continue
            key = relative.as_posix()
            rules[key] = {"id": key, "scope": scope, "path": str(path),
                          "content": path.read_text(encoding="utf-8")}
    return list(rules.values())
