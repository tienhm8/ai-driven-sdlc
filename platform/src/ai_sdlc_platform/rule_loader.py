from pathlib import Path

from .config import resource_files, resource_roots


def load_rules(shared_root: Path | None, project_root: Path):
    rules = {}
    for scope, root in resource_roots(shared_root, project_root, "rules"):
        patterns = ("*.md", "*.mdc") if scope == "project" else ("*.md",)
        for pattern in patterns:
            for path in resource_files(root, pattern):
                key = path.relative_to(root).as_posix()
                rules[key] = {"id": key, "scope": scope, "path": str(path),
                              "content": path.read_text(encoding="utf-8")}
    return list(rules.values())
