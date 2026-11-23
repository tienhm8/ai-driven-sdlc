from pathlib import Path

def load_skills(shared_root: Path | None, project_root: Path, requested=None):
    roots = []
    if shared_root and shared_root.exists(): roots.append(("shared", shared_root))
    local = project_root / ".ai-sdlc" / "local-skills"
    if local.exists(): roots.append(("project", local))
    found = {}
    for scope, root in roots:
        for path in sorted(root.rglob("SKILL.md")):
            key = path.parent.name
            if requested and key not in requested: continue
            found[key] = {"name":key,"scope":scope,"path":str(path),"content":path.read_text(encoding="utf-8")}
    missing = set(requested or []) - set(found)
    if missing: raise FileNotFoundError("Skills not found: " + ", ".join(sorted(missing)))
    return list(found.values())
