from pathlib import Path

from yaml import YAMLError

from ..config import (
    PROJECT_MANIFEST, allow_mandatory_rule_overrides, load_project_manifest, resolve_local_resources,
)
from ..constants import STAGES
from ..governance import load_approver_roles
from ..rule_loader import is_reserved_rule, rule_files


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
        allow_override = None
        try:
            allow_override = allow_mandatory_rule_overrides(data)
        except ValueError as error:
            report("error", "INVALID_RULE_OVERRIDE_POLICY", str(error))
        if not data.get("technology_stack"):
            report("warning", "STACK_UNDEFINED", "technology_stack is not defined")
        try:
            paths = resolve_local_resources(project, data)
        except (ValueError, OSError, RuntimeError) as error:
            report("error", "INVALID_LOCAL_RESOURCES", str(error))
        else:
            project_root = project.resolve()
            for path in paths.values():
                if not path.is_dir():
                    report("warning", "OPTIONAL_DIR_MISSING", f"{path.relative_to(project_root)} is absent")
            if allow_override is False:
                rules_root = paths["rules"]
                try:
                    for path in rule_files(rules_root, project=True):
                        if is_reserved_rule(path.relative_to(rules_root)):
                            report("warning", "RESERVED_RULE_IGNORED",
                                   f"{path.relative_to(project_root).as_posix()} is ignored; "
                                   "move project-specific rules outside core/ and sdlc/")
                except (OSError, RuntimeError) as error:
                    report("error", "INVALID_LOCAL_RESOURCES", str(error))

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
