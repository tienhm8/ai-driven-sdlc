#!/usr/bin/env python3
"""Initialize an AI-Driven SDLC project instance."""

from pathlib import Path
import argparse
from os.path import relpath
import re
import shutil
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ai_sdlc_platform.config import PROJECT_ID_PATTERN, PROJECT_MANIFEST
from ai_sdlc_platform.manifest_schema import AI_POLICY_DEFAULTS, MANIFEST_SCHEMA_VERSION
from ai_sdlc_platform.constants import STAGES

SYSTEM_DESIGN_OUTPUT_FOLDERS = [
    "architecture",
    "adr",
    "api",
    "database",
    "data-model",
    "flows",
    "security",
    "approvals",
]

# Project-level working documents created for every new project instance.
# The source templates remain owned by framework/03-task-planning.
TASK_PLANNING_PROJECT_FILES = {
    "product-backlog.md": "templates/product-backlog.md",
    "task-breakdown.md": "templates/task-breakdown.md",
    "effort-estimation.md": "templates/effort-estimation.md",
    "dependency-matrix.md": "templates/dependency-matrix.md",
    "definition-of-ready.md": "templates/definition-of-ready.md",
    "definition-of-done.md": "templates/definition-of-done.md",
    "sprint-plan.md": "templates/sprint-plan.md",
    "planning-change-log.md": "templates/planning-change-log.md",
}

PROJECT_MANAGEMENT_FOLDERS = [
    "project-charter",
    "project-status",
    "meeting-notes",
    "decisions",
    "risks",
    "issues",
    "changes",
    "approvals",
    "project-closeout",
]

PROJECT_MANAGEMENT_REGISTERS = {
    "change-log.md": "Change Log",
    "risk-register.md": "Risk Register",
    "issue-log.md": "Issue Log",
    "decision-log.md": "Decision Log",
    "approval-register.md": "Approval Register",
    "meeting-notes.md": "Meeting Notes",
}

AI_TOOLS = {
    "claude": ".claude",
    "cursor": ".cursor",
    "copilot": ".github",
    "codex": ".agents",
}


def write_if_missing(path: Path, content: str):
    """Create a text file only when it does not already exist."""
    if path.exists():
        print(f"[SKIP] {path}")
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"[CREATE] {path}")


def create_directory(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    print(f"[DIR] {path}")


def copy_file_if_missing(source: Path, destination: Path):
    """Copy one framework file without overwriting project changes."""
    if not source.is_file():
        print(f"[WARN] Framework source not found: {source}")
        return

    if destination.exists():
        print(f"[SKIP] File exists: {destination}")
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"[COPY] {source} -> {destination}")


def copy_templates(source: Path, destination: Path):
    """Copy a directory's contents, preserving existing project files."""
    if not source.exists() or not source.is_dir():
        return

    create_directory(destination)

    for item in source.iterdir():
        target = destination / item.name

        if target.exists():
            print(f"[SKIP] Template exists: {target}")
            continue

        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)

        print(f"[COPY] {item} -> {target}")


def validate_slug(slug: str):
    if not re.fullmatch(PROJECT_ID_PATTERN, slug):
        raise ValueError(
            "Invalid project slug. "
            "Use only letters, numbers, hyphens and underscores."
        )


def generate_config(
    project_name: str,
    slug: str,
    tools: list,
    include_project_management: bool,
):
    default_tool = tools[0]
    tool_dir = AI_TOOLS[default_tool]
    return yaml.safe_dump({
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "project": {"id": slug, "name": project_name, "version": "1.0.0"},
        "framework": {"name": "AI-Driven-SDLC", "version": "1.0.0"},
        "technology_stack": {"repositories": {}},
        "ai": {
            "tools": tools,
            "default_tool": default_tool,
            **AI_POLICY_DEFAULTS,
            "shared_resources": {
                "rules": ["core", "sdlc", "engineering"],
                "skills": ["architecture", "backend", "frontend", "database", "devops", "security"],
            },
            "local_resources": {"rules_path": f"{tool_dir}/rules", "skills_path": f"{tool_dir}/skills"},
        },
        "autonomy": {
            "default_level": "L2",
            "stages": {
                "requirement_analysis": "L2",
                "system_design": "L3",
                "task_planning": "L2",
                "development": "L2",
                "code_review": "L3",
                "testing_qa": "L2",
                "deployment": "L3",
                "monitoring_maintenance": "L2",
            },
        },
        "project_management": {"enabled": include_project_management, "path": "docs/project-management"},
        "governance": {
            "require_human_approval": True,
            "enforce_review_gates": True,
            "allow_project_override_mandatory_rules": False,
        },
    }, sort_keys=False, allow_unicode=True)


def initialize_requirement_analysis_outputs(
    framework_dir: Path,
    project_docs_dir: Path,
):
    """Create the project-level Requirement Analysis deliverable set.

    Copies the framework's standard output structure into
    docs/01-requirement-analysis/outputs. The RTM starter is copied from
    the canonical Stage 01 template, not the framework output snapshot.
    Existing project files are never overwritten.
    """
    framework_stage = framework_dir / "01-requirement-analysis"
    framework_outputs = framework_stage / "outputs"
    project_outputs = project_docs_dir / "01-requirement-analysis" / "outputs"
    rtm_output = Path("11-requirement-traceability/requirement-traceability-matrix.md")

    create_directory(project_outputs)

    if not framework_outputs.is_dir():
        print(f"[WARN] Framework source not found: {framework_outputs}")
        return

    for source in sorted(framework_outputs.rglob("*")):
        relative = source.relative_to(framework_outputs)
        if source.is_dir():
            create_directory(project_outputs / relative)
        elif source.is_file() and relative != rtm_output:
            copy_file_if_missing(source, project_outputs / relative)

    copy_file_if_missing(
        framework_stage / "templates" / "requirement-traceability.md",
        project_outputs / rtm_output,
    )


def initialize_system_design_outputs(
    framework_dir: Path,
    project_docs_dir: Path,
):
    """Create project-level System Design deliverable folders."""
    framework_outputs = framework_dir / "02-system-design" / "outputs"
    project_outputs = project_docs_dir / "02-system-design" / "outputs"

    create_directory(project_outputs)

    for folder in SYSTEM_DESIGN_OUTPUT_FOLDERS:
        create_directory(project_outputs / folder)

    # Copy guidance and the starter artifact register without overwriting
    # files that project members may already have edited.
    for filename in ("README.md", "design-package-index.md"):
        copy_file_if_missing(
            framework_outputs / filename,
            project_outputs / filename,
        )


def initialize_task_planning_project_docs(
    framework_dir: Path,
    project_docs_dir: Path,
):
    """Create the proposed project-level Stage 03 document set.

    The project docs are working copies of framework templates. The
    framework's templates remain unchanged, and existing project files
    are never overwritten.
    """
    stage_framework_dir = framework_dir / "03-task-planning"
    stage_project_dir = project_docs_dir / "03-task-planning"

    create_directory(stage_project_dir)

    # Stage overview: prefer the framework README.
    copy_file_if_missing(
        stage_framework_dir / "README.md",
        stage_project_dir / "README.md",
    )
    write_if_missing(
        stage_project_dir / "README.md",
        (
            "# 03 — Task Planning\n\n"
            "Project-level planning artifacts for this project instance.\n\n"
            "Use the approved Requirement Baseline (G1) and Design "
            "Baseline (G2) as planning inputs. Keep project-specific "
            "planning decisions and approvals in this directory.\n"
        ),
    )

    # Create editable project working documents from shared templates.
    for destination_name, source_relative_path in TASK_PLANNING_PROJECT_FILES.items():
        copy_file_if_missing(
            stage_framework_dir / source_relative_path,
            stage_project_dir / destination_name,
        )

    # Input register is project-specific: it records the exact approved
    # upstream artifacts and their versions rather than duplicating them.
    write_if_missing(
        stage_project_dir / "input-register.md",
        """# Input Register — Task Planning

Record the authoritative inputs used to prepare this planning baseline.
Prefer references, repository paths, document IDs, versions and approval
evidence over copying upstream documents into this folder.

| Input | Required | Reference / Path | Version | Approval / Status | Owner | Notes |
|---|---|---|---|---|---|---|
| Requirement Baseline (G1) | Yes | | | Approved | | |
| User Stories & Acceptance Criteria | Yes | | | Approved / linked to G1 | | |
| Design Baseline (G2) | Yes | | | Pending | | |
| Architecture Decision Records | When applicable | | | | | |
| Technical constraints / technology stack | Yes | | | | | |
| Risks, assumptions and dependencies | Yes | | | | | |
| Team capacity / availability | Yes, for sprint planning | | | | | |

For Design Baseline, record the exact finalized design package version and
G2 approval evidence for that version. Set input verification to Verified
only when G2 is Approved and the package is the baseline handed off to Stage 03;
otherwise keep it Pending. This input status is distinct from the gate status.

## Readiness decision

- Planning input status: `Not assessed`
- Assessed by:
- Assessment date:
- Open issues:
- Decision: `Pending`

Do not proceed to G3 approval while mandatory baselines are missing,
unapproved or inconsistent.
""",
    )

    write_if_missing(
        stage_project_dir / "planning-review.md",
        """# Planning Review

> Record the review of the proposed backlog, task breakdown, estimates,
> dependencies, Definition of Done and sprint plan.

## Review information

- Project:
- Planning baseline / version:
- Review date:
- Reviewers:
- Review facilitator:

## Review checklist

- [ ] Planning inputs reference approved G1 and G2 baselines.
- [ ] Backlog items trace to requirements, user stories or approved design.
- [ ] Tasks have clear scope, owner/role and acceptance or completion criteria.
- [ ] Estimates include assumptions and uncertainty.
- [ ] Dependencies, external blockers and critical path are identified.
- [ ] Definition of Done is measurable and applicable.
- [ ] Sprint scope reflects team capacity and priority.
- [ ] Risks, assumptions and unresolved questions have owners.
- [ ] No planning item silently changes an approved requirement or design.

## Findings and actions

| ID | Finding / Action | Severity | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Review outcome

- Decision: `Pending` / `Changes requested` / `Ready for G3`
- Rationale:
- Reviewed by:
- Date:
""",
    )

    approval_template = framework_dir / "templates" / "review" / "approval-record.md"
    if approval_template.is_file():
        approval_record = approval_template.read_text(encoding="utf-8")
        for field, value in (("Gate / subject", "G3"), ("Vai trò approver bắt buộc", "Tech Lead")):
            approval_record, count = re.subn(
                rf"^- {re.escape(field)}:[^\n]*$",
                f"- {field}: {value}",
                approval_record,
                flags=re.MULTILINE,
            )
            if count != 1:
                raise ValueError(f"Expected one {field} field in {approval_template}")
        write_if_missing(stage_project_dir / "g3-approval.md", approval_record)
    else:
        print(f"[WARN] Framework source not found: {approval_template}")


def initialize_development_project_docs(
    framework_dir: Path,
    project_docs_dir: Path,
):
    """Create project-level Development outputs and their templates.

    Actual project artifacts live in docs/04-development/outputs.
    Reusable output templates are copied to
    docs/04-development/_templates/outputs.
    Existing project files are never overwritten.
    """
    stage_framework_dir = framework_dir / "04-development"
    stage_project_dir = project_docs_dir / "04-development"

    framework_outputs = stage_framework_dir / "outputs"
    project_outputs = stage_project_dir / "outputs"
    project_output_templates = (
        stage_project_dir / "_templates" / "outputs"
    )

    # Actual Development deliverables for this project.
    create_directory(project_outputs)

    # Copy output guidance, if provided by the framework.
    copy_file_if_missing(
        framework_outputs / "README.md",
        project_outputs / "README.md",
    )

    # Fallback guidance when the framework README is not present.
    write_if_missing(
        project_outputs / "README.md",
        (
            "# Development Outputs\n\n"
            "Project-specific Development artifacts and handover evidence.\n\n"
            "Store implementation summaries, test evidence and the "
            "Development handover package here. Source code and tests "
            "remain in the Git repository.\n\n"
            "These artifacts do not constitute approval to merge, accept "
            "or deploy. Code Review and subsequent human review gates "
            "remain mandatory.\n"
        ),
    )

    # Keep reusable output templates separate from actual project artifacts.
    create_directory(project_output_templates)

    if framework_outputs.is_dir():
        for source in framework_outputs.glob("*.md"):
            if source.name == "README.md":
                continue

            copy_file_if_missing(
                source,
                project_output_templates / source.name,
            )


def initialize_late_stage_outputs(framework_dir: Path, project_docs_dir: Path):
    """Seed output guidance and examples, never test or operations evidence."""
    for stage in ("06-testing-qa", "07-deployment", "08-monitoring-maintenance"):
        source = framework_dir / stage / "outputs"
        destination = project_docs_dir / stage / "outputs"
        create_directory(destination)
        copy_file_if_missing(source / "README.md", destination / "README.md")
        for example in sorted(source.glob("*-example.md")):
            if example.is_file():
                copy_file_if_missing(example, destination / example.name)


def initialize_project_management(framework_dir: Path, project_docs_dir: Path):
    source = framework_dir / "project-management"
    pm_dir = project_docs_dir / "project-management"
    templates = pm_dir / "_templates"

    for folder in PROJECT_MANAGEMENT_FOLDERS:
        create_directory(pm_dir / folder)

    # Copy the real Gate template rather than the framework's relative pointer.
    copy_file_if_missing(
        framework_dir / "templates" / "review" / "approval-record.md",
        templates / "approval-record-template.md",
    )
    copy_templates(source / "templates", templates)
    copy_file_if_missing(source / "templates" / "project-charter-template.md", pm_dir / "project-charter.md")
    copy_file_if_missing(source / "workflow.md", pm_dir / "workflow.md")
    for filename in PROJECT_MANAGEMENT_REGISTERS:
        copy_file_if_missing(source / filename, pm_dir / filename)

    framework_ref = Path(relpath(framework_dir, pm_dir)).as_posix()
    manifest_ref = Path(relpath(project_docs_dir.parent / PROJECT_MANIFEST, pm_dir)).as_posix()
    register_links = "".join(f"- [{title}]({filename})\n" for filename, title in PROJECT_MANAGEMENT_REGISTERS.items())
    write_if_missing(
        pm_dir / "README.md",
        "# Project Management\n\n"
        "Bắt đầu với [charter nháp](project-charter.md), theo [workflow](workflow.md) "
        "và dùng [danh mục mẫu](_templates/README.md) khi tạo hồ sơ.\n\n"
        "## Trạng thái dự án\n\n"
        "- Trạng thái hiện tại: `proposed`\n"
        "- Căn cứ phê duyệt (ID/link): Chưa có.\n\n"
        "PM chỉ cập nhật tại đây sau khi Sponsor và Product Owner cùng phê duyệt: "
        "`active` sau duyệt charter, `on_hold` khi tạm dừng, trở lại `active` khi tiếp tục, "
        "hoặc `completed` / `cancelled` sau duyệt closeout. Dẫn tới phê duyệt tương ứng; "
        "không sửa baseline để cập nhật trạng thái.\n\n"
        "## Nguồn chuẩn\n\n"
        f"- [Project manifest]({manifest_ref}): ID, tên và cấu hình platform.\n"
        "- [Charter](project-charter.md): phạm vi, KPI, baseline và thẩm quyền khi được duyệt.\n"
        f"- [Gate Policy]({framework_ref}/governance/human-review-gates/gate-policy.md): "
        "vai trò và tiêu chí Gate; Approval Register chỉ dẫn tới hồ sơ gốc.\n"
        f"- [ID Conventions]({framework_ref}/standards/metadata/id-conventions.md): chuẩn cấp ID.\n"
        f"- [Mẫu ADR]({framework_ref}/02-system-design/templates/architecture-decision-record.md) và "
        "[Dependency Matrix](../03-task-planning/dependency-matrix.md): hồ sơ chuyên môn, "
        "không lập sổ song song trong PM.\n\n"
        "## Mẫu hồ sơ\n\n"
        "Dùng [mẫu trong `_templates/`](_templates/README.md). Lưu báo cáo định kỳ trong "
        "`project-status/` và báo cáo đóng dự án trong `project-closeout/`.\n\n"
        "## Sổ theo dõi\n\n"
        "Thay dòng `No entries` khi ghi mục đầu tiên. Dẫn đến hồ sơ chi tiết theo ID/link.\n\n"
        f"{register_links}",
    )


def init_project(
    root: Path,
    project_name: str,
    slug: str,
    tools: list,
    include_project_management: bool,
):
    validate_slug(slug)
    if not project_name.strip():
        raise ValueError("Project name must not be blank")

    project_dir = root / "projects" / slug
    framework_dir = root / "framework"

    if project_dir.exists():
        raise FileExistsError(f"Project already exists: {project_dir}")

    project_dir.mkdir(parents=True)
    print(f"\n[PROJECT] {project_dir}")

    try:
        # 1. Shared project configuration.
        config_content = generate_config(
            project_name,
            slug,
            tools,
            include_project_management,
        )
        write_if_missing(project_dir / PROJECT_MANIFEST, config_content)

        # 2. AI Tool-specific directories.
        for tool in tools:
            tool_dir = project_dir / AI_TOOLS[tool]
            create_directory(tool_dir / "rules")
            create_directory(tool_dir / "skills")

            readme = (
                f"# {tool.title()} Integration\n\n"
                f"Project-specific rules and skills for {tool}.\n\n"
                f"Shared project configuration is defined in [{PROJECT_MANIFEST.as_posix()}]"
                f"(../{PROJECT_MANIFEST.as_posix()}).\n"
            )
            write_if_missing(tool_dir / "README.md", readme)

        # 3. Documentation stages and stage templates.
        docs_dir = project_dir / "docs"

        for stage in STAGES:
            stage_dir = docs_dir / stage
            create_directory(stage_dir)

            source = framework_dir / stage / "templates"
            destination = stage_dir / "_templates"
            copy_templates(source, destination)

        # 3b. Requirement Analysis project outputs.
        initialize_requirement_analysis_outputs(
            framework_dir=framework_dir,
            project_docs_dir=docs_dir,
        )

        # 4. System Design project outputs.
        initialize_system_design_outputs(
            framework_dir=framework_dir,
            project_docs_dir=docs_dir,
        )

        # 5. Task Planning project-level working documents.
        initialize_task_planning_project_docs(
            framework_dir=framework_dir,
            project_docs_dir=docs_dir,
        )

        # 6. Development project-level outputs and output templates.
        initialize_development_project_docs(
            framework_dir=framework_dir,
            project_docs_dir=docs_dir,
        )

        # 7. QA, Deployment and Monitoring output guidance and examples.
        initialize_late_stage_outputs(framework_dir, docs_dir)

        # 8. Project management.
        if include_project_management:
            initialize_project_management(framework_dir, docs_dir)

        # 9. Project README.
        write_if_missing(
            project_dir / "README.md",
            f"# {project_name}\n\n"
            "AI-Driven SDLC Project Instance.\n\n"
            f"See [{PROJECT_MANIFEST.as_posix()}]({PROJECT_MANIFEST.as_posix()}) for project configuration.\n"
            "See `docs/` for SDLC documentation and deliverables.\n",
        )

        print("\n[SUCCESS] Project initialized.")
        print(f"Location: {project_dir}")

    except Exception:
        # Remove the incomplete project created by this run.
        shutil.rmtree(project_dir, ignore_errors=True)
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Initialize an AI-Driven SDLC Project Instance"
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Project display name",
    )
    parser.add_argument(
        "--slug",
        required=True,
        help="Project folder name",
    )
    parser.add_argument(
        "--tools",
        default="claude",
        help="Comma-separated AI tools: claude,cursor,copilot,codex",
    )
    parser.add_argument(
        "--project-management",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Create docs/project-management (default: enabled)",
    )

    args = parser.parse_args()

    tools = [
        item.strip().lower()
        for item in args.tools.split(",")
        if item.strip()
    ]

    if not tools:
        parser.error("At least one AI Tool is required.")

    unknown = set(tools) - set(AI_TOOLS)
    if unknown:
        parser.error(
            f"Unsupported AI tools: {', '.join(sorted(unknown))}"
        )

    # Remove duplicates while preserving order.
    tools = list(dict.fromkeys(tools))

    # Script is located at platform/scripts/init-project.py.
    root = Path(__file__).resolve().parents[2]

    try:
        init_project(
            root=root,
            project_name=args.name,
            slug=args.slug,
            tools=tools,
            include_project_management=args.project_management,
        )
    except Exception as error:
        print(f"\n[ERROR] {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
