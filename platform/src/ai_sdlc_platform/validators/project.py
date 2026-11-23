from pathlib import Path

from yaml import YAMLError

from ..config import PROJECT_MANIFEST, load_project_manifest, resolve_local_resources
from ..constants import STAGES
from ..governance import load_approver_roles


def validate_project(project: Path, framework: Path | None = None):
    issues = []

    def report(severity, code, message):
        issues.append({"severity": severity, "code": code, "message": message})

    if not project.is_dir():
        report("error", "PROJECT_NOT_FOUND", str(project))
        return issues

    try:
        data = load_project_manifest(project)
    except FileNotFoundError:
        message = f"Missing {PROJECT_MANIFEST.as_posix()}"
        if (project / "config.yml").is_file():
            message += "; migrate config.yml and rename project.slug to project.id"
        report("error", "MISSING_MANIFEST", message)
    except (YAMLError, UnicodeError) as error:
        report("error", "INVALID_YAML", str(error))
    except ValueError as error:
        report("error", "INVALID_METADATA", str(error))
    except OSError as error:
        report("error", "UNREADABLE_MANIFEST", str(error))
    else:
        if not data.get("technology_stack"):
            report("warning", "STACK_UNDEFINED", "technology_stack is not defined")
        try:
            paths = resolve_local_resources(project, data)
        except (ValueError, OSError, RuntimeError) as error:
            report("error", "INVALID_LOCAL_RESOURCES", str(error))
        else:
            for path in paths.values():
                if not path.is_dir():
                    report("warning", "OPTIONAL_DIR_MISSING", f"{path.relative_to(project.resolve())} is absent")

    try:
        load_approver_roles(project)
    except (ValueError, YAMLError, OSError) as error:
        report("error", "INVALID_APPROVAL_POLICY", str(error))

    for stage in STAGES:
        if not (project / "docs" / stage).is_dir():
            report("warning", "STAGE_DOCS_MISSING", f"docs/{stage}/ is absent")
    if framework is not None and not framework.is_dir():
        report("error", "FRAMEWORK_NOT_FOUND", str(framework))
    if not any(issue["severity"] == "error" for issue in issues):
        report("info", "VALIDATION_PASSED", "No blocking configuration errors")
    return issues
