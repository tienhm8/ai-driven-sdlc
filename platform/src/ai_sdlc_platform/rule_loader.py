from pathlib import Path

def load_rules(shared_root: Path | None, project_root: Path):
    roots = []
    if shared_root and shared_root.exists(): roots.append(("shared", shared_root))
    local = project_root / ".ai-sdlc" / "local-rules"
    if local.exists(): roots.append(("project", local))
    rules = {}
    for scope, root in roots:
        for path in sorted(root.rglob("*.md")):
            key = path.relative_to(root).as_posix()
            rules[key] = {"id":key,"scope":scope,"path":str(path),"content":path.read_text(encoding="utf-8")}
    return list(rules.values())
