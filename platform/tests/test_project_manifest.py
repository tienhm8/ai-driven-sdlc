from pathlib import Path
import shutil
from subprocess import run
import sys
from tempfile import TemporaryDirectory
from unittest import TestCase

import yaml

from ai_sdlc_platform.config import PROJECT_MANIFEST, load_project_manifest, resolve_local_resources
from ai_sdlc_platform.rule_loader import load_rules
from ai_sdlc_platform.skill_loader import load_skills
from ai_sdlc_platform.validators.project import validate_project

PLATFORM = Path(__file__).resolve().parents[1]


class ProjectManifestTests(TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.project = self.root / "projects" / "demo"

    def test_project_management_seeds_canonical_approval(self):
        shutil.copytree(PLATFORM / "scripts", self.root / "platform/scripts")
        shutil.copytree(PLATFORM / "src", self.root / "platform/src", ignore=shutil.ignore_patterns("__pycache__"))
        framework = self.root / "framework"
        shutil.copytree(PLATFORM.parent / "framework", framework)
        command = [sys.executable, "-B", str(self.root / "platform/scripts/init-project.py"),
                   "--name", "Demo", "--slug", "demo", "--tools", "claude"]
        result = run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        target = self.project / "docs/project-management/_templates/approval-record-template.md"
        source = framework / "templates/review/approval-record.md"
        self.assertEqual(target.read_bytes(), source.read_bytes())
        self.assertIn("## Quyết định", target.read_text(encoding="utf-8"))

    def test_init_validate_and_load_project_overrides(self):
        shutil.copytree(PLATFORM / "scripts", self.root / "platform/scripts")
        shutil.copytree(PLATFORM / "src", self.root / "platform/src", ignore=shutil.ignore_patterns("__pycache__"))
        framework = self.root / "framework"
        shutil.copytree(PLATFORM.parent / "framework", framework)
        ra_stage = framework / "01-requirement-analysis"
        ra_source = ra_stage / "outputs"
        rtm_relative = Path("11-requirement-traceability/requirement-traceability-matrix.md")
        rtm_template = ra_stage / "templates/requirement-traceability.md"
        self.assertEqual((ra_source / rtm_relative).read_bytes(), rtm_template.read_bytes())
        # A stale snapshot must never become the starter in a new project.
        (ra_source / rtm_relative).write_text("stale starter\n", encoding="utf-8")
        stage_examples = {
            "06-testing-qa": {"qa-signoff-example.md", "test-execution-summary-example.md"},
            "07-deployment": {"deployment-report-example.md", "release-note-example.md"},
            "08-monitoring-maintenance": {"monitoring-report-example.md", "incident-report-example.md",
                                          "postmortem-example.md"},
        }
        for stage in stage_examples:
            outputs = framework / stage / "outputs"
            (outputs / "actual-report.md").touch()
            (outputs / "historical-run").mkdir()
            (outputs / "historical-run" / "report-example.md").touch()
        display_name = 'Dự án "West" \\ demo\nDòng tiếp theo'
        init = run([sys.executable, "-B", str(self.root / "platform/scripts/init-project.py"),
                    "--name", display_name, "--slug", "demo", "--tools", "cursor,claude",
                    "--no-project-management"], capture_output=True, text=True)
        self.assertEqual(init.returncode, 0, init.stderr)
        register = (self.project / "docs/03-task-planning/input-register.md").read_text(encoding="utf-8")
        row = next(line for line in register.splitlines() if line.startswith("| Design Baseline (G2) |"))
        self.assertEqual([cell.strip() for cell in row.strip("|").split("|")][4], "Pending")
        self.assertIn("G2 approval evidence for that version", register)
        self.assertIn("G2 is Approved", register)
        planning = self.project / "docs/03-task-planning"
        approval = (planning / "g3-approval.md").read_text(encoding="utf-8")
        self.assertIn("- Gate / subject: G3", approval.splitlines())
        canonical = (framework / "templates/review/approval-record.md").read_text(encoding="utf-8")
        self.assertNotIn("Nếu dùng cho G3", canonical)
        for field in ("Phạm vi được duyệt / phần ngoài phạm vi", "| Approver |",
                      "`Approved / Rejected / Changes Requested / Blocked`"):
            self.assertIn(field, approval)
        expected = canonical.replace("- Gate / subject: G1 / G2 / G3 / G4 / G5 / G6 / G7 / Other\n",
                                     "- Gate / subject: G3\n")
        expected = expected.replace("- Vai trò approver bắt buộc:\n", "- Vai trò approver bắt buộc: Tech Lead\n")
        self.assertIn("- Vai trò approver bắt buộc: Tech Lead", approval.splitlines())
        self.assertEqual(approval, expected)
        self.assertEqual((planning / "planning-change-log.md").read_bytes(),
                         (framework / "03-task-planning/templates/planning-change-log.md").read_bytes())
        self.assertFalse((planning / "corrections").exists())
        self.assertEqual((planning / "definition-of-ready.md").read_bytes(),
                         (framework / "03-task-planning/templates/definition-of-ready.md").read_bytes())
        for stage, examples in stage_examples.items():
            with self.subTest(stage=stage):
                outputs = self.project / "docs" / stage / "outputs"
                self.assertEqual({path.name for path in outputs.iterdir()}, examples | {"README.md"})
                for name in examples | {"README.md"}:
                    self.assertEqual((outputs / name).read_bytes(), (framework / stage / "outputs" / name).read_bytes())
        ra_target = self.project / "docs" / "01-requirement-analysis" / "outputs"
        ra_files = sorted(p.relative_to(ra_source) for p in ra_source.rglob("*") if p.is_file())
        self.assertIn(Path("01-business-requirements/BRD.md"), ra_files)
        self.assertIn(Path("12-requirement-review/G1-approval.md"), ra_files)
        for relative in ra_files:
            expected = rtm_template if relative == rtm_relative else ra_source / relative
            self.assertEqual((ra_target / relative).read_bytes(), expected.read_bytes())
        self.assertFalse((self.project / "config.yml").exists())
        manifest = load_project_manifest(self.project)
        self.assertEqual(manifest["project"], {"id": "demo", "name": display_name, "version": "1.0.0"})
        self.assertEqual(manifest["ai"]["default_tool"], "cursor")
        self.assertFalse(manifest["project_management"]["enabled"])
        validation = run([sys.executable, "-B", str(self.root / "platform/scripts/validate-project.py"),
                          "--project", str(self.project), "--framework", str(framework)],
                         capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stdout + validation.stderr)
        self.assertIn("VALIDATION_PASSED", validation.stdout)
        self.assertNotIn("OPTIONAL_DIR_MISSING", validation.stdout)

        paths = resolve_local_resources(self.project, manifest)
        self.assertEqual(paths["rules"], self.project / ".cursor/rules")
        self.assertEqual(paths["skills"], self.project / ".cursor/skills")
        shared = self.root / "shared"
        for path, text in {
            shared / "skills/nestjs/SKILL.md": "shared skill",
            shared / "skills/react/SKILL.md": "shared only skill",
            shared / "rules/style.md": "shared rule",
            paths["skills"] / "nestjs/SKILL.md": "local skill",
            paths["rules"] / "style.md": "local rule",
            paths["rules"] / "cursor.mdc": "cursor rule",
            self.project / ".claude/rules/unused.md": "not default tool",
        }.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        skills = {item["name"]: item for item in load_skills(shared / "skills", self.project, ["nestjs", "react"])}
        self.assertEqual(skills["nestjs"]["scope"], "project")
        self.assertEqual(skills["nestjs"]["content"], "local skill")
        self.assertEqual(skills["react"]["scope"], "shared")
        rules = {item["id"]: item for item in load_rules(shared / "rules", self.project)}
        self.assertEqual({key: item["content"] for key, item in rules.items()},
                         {"style.md": "local rule", "cursor.mdc": "cursor rule"})

    def write_manifest(self, **data):
        path = self.project / PROJECT_MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump({"project": {"id": "demo", "name": "Demo"}, **data}), encoding="utf-8")

    def test_custom_paths_and_defaults(self):
        self.write_manifest(ai={"local_resources": {"rules_path": "custom/rules"}})
        paths = resolve_local_resources(self.project, load_project_manifest(self.project))
        self.assertEqual(paths["rules"], self.project / "custom/rules")
        self.assertEqual(paths["skills"], self.project / ".ai-sdlc/local-skills")
        skill = paths["skills"] / "local/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("local", encoding="utf-8")
        self.assertEqual(load_skills(None, self.project)[0]["name"], "local")
        with self.assertRaisesRegex(FileNotFoundError, "Skills not found: absent"):
            load_skills(None, self.project, ["absent"])

    def test_invalid_local_paths_fail_validation_and_loading(self):
        outside = self.root / "outside"
        outside.mkdir()
        self.project.mkdir(parents=True)
        (self.project / "linked").symlink_to(outside, target_is_directory=True)
        for value in ("../outside", str(outside), "linked", ".", None):
            with self.subTest(value=value):
                self.write_manifest(ai={"local_resources": {"rules_path": value}})
                issues = validate_project(self.project)
                self.assertTrue(any(issue["code"] == "INVALID_LOCAL_RESOURCES" for issue in issues))
                with self.assertRaises(ValueError):
                    load_rules(None, self.project)

    def test_resource_loaders_validate_only_their_own_path(self):
        rules = self.project / "custom/rules"
        skills = self.project / "custom/skills/local"
        rules.mkdir(parents=True)
        skills.mkdir(parents=True)
        (rules / "style.md").write_text("good rule", encoding="utf-8")
        (skills / "SKILL.md").write_text("good skill", encoding="utf-8")
        for paths, loader, expected in (
            ({"rules_path": "custom/rules", "skills_path": "custom/rules/style.md"}, load_rules, "good rule"),
            ({"skills_path": "custom/skills", "rules_path": "../outside"}, load_skills, "good skill"),
        ):
            with self.subTest(paths=paths):
                self.write_manifest(ai={"local_resources": paths})
                self.assertEqual(loader(None, self.project)[0]["content"], expected)
                self.assertIn("INVALID_LOCAL_RESOURCES", {issue["code"] for issue in validate_project(self.project)})

    def test_validator_rejects_legacy_and_malformed_approval_policies(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        for contents in ("gates: {G6: {approver_roles: [qa_engineer]}}", "gates: [", "gates: {G6: {required: false}}"):
            with self.subTest(contents=contents):
                policy.write_text(contents, encoding="utf-8")
                issues = validate_project(self.project)
                self.assertIn("INVALID_APPROVAL_POLICY", {issue["code"] for issue in issues})
                self.assertNotIn("VALIDATION_PASSED", {issue["code"] for issue in issues})
        policy.write_text("gates: {G6: {approver_roles: [release_manager]}}", encoding="utf-8")
        self.assertIn("VALIDATION_PASSED", {issue["code"] for issue in validate_project(self.project)})

    def test_validator_reports_malformed_tagged_approval_policy_values(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        for contents, message in (
            ("gates: !!map [G4]", "expected a mapping node"),
            ("gates: {G4: {required: !!bool maybe}}", "invalid value for YAML tag"),
            ("gates: {G4: {required: !!int ''}}", "invalid value for YAML tag"),
            ("gates: {G4: {required: !!float '+'}}", "invalid value for YAML tag"),
            ("gates: {G4: {approver_roles: [!!str {=: reviewer, repeated: 1, repeated: 2}]}}",
             "expected a scalar node"),
            ("gates: {G4: &gate {<<: *gate}}", "recursive YAML merge"),
        ):
            with self.subTest(contents=contents):
                policy.write_text(contents, encoding="utf-8")
                issues = validate_project(self.project)
                invalid = next(issue for issue in issues if issue["code"] == "INVALID_APPROVAL_POLICY")
                self.assertIn(message, invalid["message"])
                self.assertIn("line 1, column", invalid["message"])
                self.assertNotIn("VALIDATION_PASSED", {issue["code"] for issue in issues})

    def test_validator_bounds_policy_nesting_and_merge_expansion(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        anchors = ["&a0 {required: true}"]
        for index in range(1, 65):
            anchors.append(f"&a{index} {{<<: *a{index - 1}}}")
        # The root merge runs before the values holding the earlier anchor definitions are constructed.
        chain = f"fixtures: [{', '.join(anchors)}]\n<<: *a64\n"
        for contents, diagnostic in (
            ("gates: " + "[" * 65 + "0" + "]" * 65, "YAML nesting exceeds"),
            (chain, "YAML merge depth exceeds"),
            ("gates: {G4: {<<: [&a {required: true}, " + ", ".join(["*a"] * 256) + "]}}",
             "too many approval policy mapping entries"),
        ):
            with self.subTest(diagnostic=diagnostic):
                policy.write_text(contents, encoding="utf-8")
                issue = next(issue for issue in validate_project(self.project)
                             if issue["code"] == "INVALID_APPROVAL_POLICY")
                self.assertIn(diagnostic, issue["message"])

    def test_validator_accepts_a_policy_with_disjoint_yaml_merge_entries(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        policy.write_text("gates: {G4: {<<: [{required: true}, {approver_roles: [reviewer]}]}}", encoding="utf-8")
        self.assertIn("VALIDATION_PASSED", {issue["code"] for issue in validate_project(self.project)})

    def test_validator_rejects_duplicate_approval_policy_keys(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        for contents, key in (
            ("gates: {}\ngates: {}\n", "gates"),
            ("gates:\n  G4: {approver_roles: [tech_lead]}\n  G4: {approver_roles: [reviewer]}\n", "G4"),
            ("gates: {G4: {approver_roles: [tech_lead], approver_roles: [reviewer]}}", "approver_roles"),
            ("gates: {G4: {<<: {approver_roles: [tech_lead]}, approver_roles: [reviewer]}}", "approver_roles"),
            ("gates: {G4: {<<: {required: true}, <<: {approver_roles: [reviewer]}}}", "<<"),
        ):
            with self.subTest(contents=contents):
                policy.write_text(contents, encoding="utf-8")
                issues = validate_project(self.project)
                invalid = next(issue for issue in issues if issue["code"] == "INVALID_APPROVAL_POLICY")
                self.assertIn(f"duplicate key {key!r}", invalid["message"])
                self.assertNotIn("VALIDATION_PASSED", {issue["code"] for issue in issues})

    def test_legacy_project_gets_migration_hint(self):
        self.project.mkdir(parents=True)
        (self.project / "config.yml").write_text("project: {slug: demo, name: Demo}", encoding="utf-8")
        issue = next(issue for issue in validate_project(self.project) if issue["code"] == "MISSING_MANIFEST")
        self.assertIn("project.slug to project.id", issue["message"])
