from pathlib import Path

from .config import resource_files, resource_roots


def load_skills(shared_root: Path | None, project_root: Path, requested=None):
    requested_names = set(requested) if requested is not None else None
    found = {}
    for scope, root in resource_roots(shared_root, project_root, "skills"):
        for path in resource_files(root, "SKILL.md"):
            name = path.parent.name
            if requested_names is not None and name not in requested_names:
                continue
            found[name] = {"name": name, "scope": scope, "path": str(path),
                           "content": path.read_text(encoding="utf-8")}
    missing = (requested_names or set()) - found.keys()
    if missing:
        raise FileNotFoundError("Skills not found: " + ", ".join(sorted(missing)))
    return list(found.values())
