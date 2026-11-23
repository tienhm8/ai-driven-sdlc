from pathlib import Path
from ..config import load_yaml
from ..constants import STAGES

def validate_project(project: Path, framework: Path | None = None):
    issues = []
    if not project.is_dir():
        return [{"severity":"error","code":"PROJECT_NOT_FOUND","message":str(project)}]
    manifest = project / ".ai-sdlc" / "project.yaml"
    if not manifest.is_file():
        issues.append({"severity":"error","code":"MISSING_MANIFEST","message":"Missing .ai-sdlc/project.yaml"})
    else:
        try:
            data = load_yaml(manifest, required=True)
            meta = data.get("project", {})
            if not meta.get("id") or not meta.get("name"):
                issues.append({"severity":"error","code":"INVALID_METADATA","message":"project.id and project.name are required"})
            if not data.get("technology_stack"):
                issues.append({"severity":"warning","code":"STACK_UNDEFINED","message":"technology_stack is not defined"})
        except Exception as e:
            issues.append({"severity":"error","code":"INVALID_YAML","message":str(e)})
    for name in ("local-rules", "local-skills"):
        if not (project / ".ai-sdlc" / name).exists():
            issues.append({"severity":"warning","code":"OPTIONAL_DIR_MISSING","message":f".ai-sdlc/{name} is absent"})
    docs = project / "docs"
    for stage in STAGES:
        if not (docs / stage).is_dir():
            issues.append({"severity":"warning","code":"STAGE_DOCS_MISSING","message":f"docs/{stage}/ is absent"})
    if framework and not framework.is_dir():
        issues.append({"severity":"error","code":"FRAMEWORK_NOT_FOUND","message":str(framework)})
    if not any(x["severity"] == "error" for x in issues):
        issues.append({"severity":"info","code":"VALIDATION_PASSED","message":"No blocking configuration errors"})
    return issues
