from pathlib import Path
import re
import shutil
from subprocess import run
import sys
from tempfile import TemporaryDirectory
from unittest import TestCase

import yaml

from ai_sdlc_platform.config import PROJECT_MANIFEST, load_project_manifest, resolve_local_resources
from ai_sdlc_platform.manifest_schema import ai_policy_ids
from ai_sdlc_platform.markdown_view import render_markdown_page
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

    def test_project_management_seeds_working_docs_and_canonical_templates(self):
        shutil.copytree(PLATFORM / "scripts", self.root / "platform/scripts")
        shutil.copytree(PLATFORM / "src", self.root / "platform/src", ignore=shutil.ignore_patterns("__pycache__"))
        framework = self.root / "framework"
        shutil.copytree(PLATFORM.parent / "framework", framework)
        command = [sys.executable, "-B", str(self.root / "platform/scripts/init-project.py"),
                   "--name", "Demo", "--slug", "demo"]
        result = run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        pm = self.project / "docs/project-management"
        pm_source = framework / "project-management"
        templates = pm / "_templates"
        self.assertNotIn("project_management", load_project_manifest(self.project))
        self.assertFalse((pm / "structure.yml").exists())
        charter = (pm / "project-charter.md").read_text(encoding="utf-8")
        self.assertIn("0.1 / Draft", charter)
        self.assertNotIn("Project lifecycle status", charter)
        self.assertEqual(charter, (templates / "project-charter-template.md").read_text(encoding="utf-8"))
        workflow = (pm / "workflow.md").read_text(encoding="utf-8")
        self.assertEqual(workflow, (pm_source / "workflow.md").read_text(encoding="utf-8"))
        closeout = (templates / "closeout-report-template.md").read_text(encoding="utf-8")
        for doc in (workflow, closeout):
            self.assertIn("`cancelled`: có thể đề xuất từ `active` hoặc `on_hold`", doc)

        target = templates / "approval-record-template.md"
        source = framework / "templates/review/approval-record.md"
        self.assertEqual(target.read_bytes(), source.read_bytes())
        gate_template = target.read_text(encoding="utf-8")
        self.assertIn("changes_requested", gate_template)
        self.assertIn("G7 / Other", gate_template)
        management = (templates / "management-approval-template.md").read_text(encoding="utf-8")
        self.assertIn("Không dùng để thông qua Human Review Gate", management)

        readme = (pm / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Trạng thái dự án\n\n- Trạng thái hiện tại: `proposed`", readme)
        self.assertIn("Căn cứ phê duyệt (ID/link): Chưa có", readme)
        self.assertIn("`on_hold` khi tạm dừng, trở lại `active` khi tiếp tục", readme)
        self.assertIn("Tạm dừng (`active` → `on_hold`)", charter)
        status_template = (templates / "status-report-template.md").read_text(encoding="utf-8")
        self.assertIn("Sức khỏe tổng thể: Green / Amber / Red", status_template)
        self.assertNotIn("On Hold", status_template)
        for name in ("change-log.md", "risk-register.md", "issue-log.md", "decision-log.md",
                     "approval-register.md", "meeting-notes.md"):
            with self.subTest(register=name):
                self.assertIn(f"]({name})", readme)
                lines = (pm / name).read_text(encoding="utf-8").splitlines()
                self.assertIn("No entries", lines)
                self.assertEqual(len([line for line in lines if line.startswith("|")]), 2)
        for name in ("project-status", "project-closeout"):
            with self.subTest(directory=name):
                self.assertEqual(list((pm / name).iterdir()), [])
        for path in pm.rglob("*.md"):
            for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text(encoding="utf-8")):
                with self.subTest(file=path.name, link=link):
                    self.assertTrue((path.parent / link).is_file())
        for root in (pm, pm_source):
            html = render_markdown_page((root / "README.md").read_text(encoding="utf-8"),
                                        title="README.md", path="README.md", guide_url="/").decode()
            for path in root.glob("*.md"):
                for fragment in re.findall(r"\]\(README\.md#([^)]+)\)", path.read_text(encoding="utf-8")):
                    with self.subTest(file=path, fragment=fragment):
                        self.assertIn(f'id="{fragment}"', html)

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
                      "`approved`, `rejected`, `changes_requested` hoặc `blocked`"):
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
        self.assertEqual(manifest["project"], {"id": "demo", "name": display_name})
        self.assertEqual(manifest["ai"]["default_tool"], "cursor")
        self.assertIs(manifest["governance"]["allow_project_override_mandatory_rules"], False)
        self.assertFalse((self.project / "docs/project-management").exists())
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

    def test_mandatory_rule_namespaces_are_protected_by_default(self):
        shared = self.root / "shared-rules"
        local = self.project / ".ai-sdlc/rules"
        for root, files in (
            (shared, {"core/README.md": "shared core", "sdlc/README.md": "shared sdlc",
                      "engineering/style.md": "shared style"}),
            (local, {"core/README.md": "local core", "core/README.mdc": "local variant",
                     "core/local.md": "reserved", "sdlc/README.md": "local sdlc",
                     "sdlc/README.mdc": "local sdlc variant", "sdlc/local.md": "reserved",
                     "engineering/style.md": "local style"}),
        ):
            for name, text in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")

        def loaded(root=shared):
            return {item["id"]: (item["scope"], item["content"]) for item in load_rules(root, self.project)}

        key = "allow_project_override_mandatory_rules"
        for governance in ({}, {key: False}):
            with self.subTest(governance=governance):
                self.write_manifest(**({"governance": governance} if governance else {}))
                self.assertEqual(loaded(), {"core/README.md": ("shared", "shared core"),
                                            "sdlc/README.md": ("shared", "shared sdlc"),
                                            "engineering/style.md": ("project", "local style")})
                self.assertEqual(loaded(None), {"engineering/style.md": ("project", "local style")})

        self.write_manifest(governance={key: True})
        self.assertEqual(loaded(), {"core/README.md": ("project", "local core"),
                                    "core/README.mdc": ("project", "local variant"),
                                    "core/local.md": ("project", "reserved"),
                                    "sdlc/README.md": ("project", "local sdlc"),
                                    "sdlc/README.mdc": ("project", "local sdlc variant"),
                                    "sdlc/local.md": ("project", "reserved"),
                                    "engineering/style.md": ("project", "local style")})

    def test_validator_warns_only_about_ignored_rules_in_configured_root(self):
        root = self.project / "custom/rules"
        names = ("core/README.md", "sdlc/nested/local.mdc", "sdlc/notes.txt", "engineering/style.md")
        for name in names:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        key = "allow_project_override_mandatory_rules"
        for governance in ({}, {key: False}, {key: True}):
            with self.subTest(governance=governance):
                self.write_manifest(ai={"local_resources": {"rules_path": "custom/rules"}},
                                    governance=governance)
                issues = validate_project(self.project)
                warnings = [item for item in issues if item["code"] == "RESERVED_RULE_IGNORED"]
                expected = [] if governance.get(key) else [f"custom/rules/{name}" for name in names[:2]]
                self.assertCountEqual([item["message"].split(" is ignored;")[0] for item in warnings],
                                      expected)
                self.assertTrue(all(item["severity"] == "warning" for item in warnings))
                self.assertIn("VALIDATION_PASSED", {item["code"] for item in issues})

    def test_invalid_mandatory_rule_policy_blocks_validation_and_loading(self):
        key = "allow_project_override_mandatory_rules"
        for governance in (None, [], {key: "false"}, {key: None}, {key: 1}):
            with self.subTest(governance=governance):
                self.write_manifest(governance=governance)
                with self.assertRaisesRegex(ValueError, "governance"):
                    load_rules(None, self.project)
                codes = {issue["code"] for issue in validate_project(self.project)}
                self.assertIn("INVALID_RULE_OVERRIDE_POLICY", codes)
                self.assertNotIn("VALIDATION_PASSED", codes)

    def test_custom_paths_and_defaults(self):
        self.write_manifest(ai={"local_resources": {"rules_path": "custom/rules"}})
        paths = resolve_local_resources(self.project, load_project_manifest(self.project))
        self.assertEqual(paths["rules"], self.project / "custom/rules")
        self.assertEqual(paths["skills"], self.project / ".ai-sdlc/skills")
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

    def test_validator_rejects_a_dangling_approval_policy(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        try:
            policy.symlink_to("missing-policy.yaml")
        except (NotImplementedError, OSError) as error:
            self.skipTest(f"Cannot create policy symlink: {error}")
        codes = {issue["code"] for issue in validate_project(self.project)}
        self.assertIn("INVALID_APPROVAL_POLICY", codes)
        self.assertNotIn("VALIDATION_PASSED", codes)

    def test_validator_rejects_a_directory_in_place_of_approval_policy(self):
        self.write_manifest()
        policy = self.project / ".ai-sdlc/approval-policy.yaml"
        policy.mkdir()
        issues = validate_project(self.project)
        issue = next(issue for issue in issues if issue["code"] == "INVALID_APPROVAL_POLICY")
        self.assertEqual(issue["message"], f"Approval policy must be a regular file: {policy}")

    def test_validator_rejects_symlinked_approval_policy_directory(self):
        self.write_manifest()
        config_dir = self.project / ".ai-sdlc"
        target = self.root / "external-config"
        config_dir.rename(target)
        try:
            config_dir.symlink_to(target, target_is_directory=True)
        except (NotImplementedError, OSError) as error:
            self.skipTest(f"Cannot create directory symlink: {error}")
        issues = validate_project(self.project)
        issue = next(issue for issue in issues if issue["code"] == "INVALID_APPROVAL_POLICY")
        self.assertIn("Approval policy directory must be a real directory", issue["message"])
        self.assertNotIn("VALIDATION_PASSED", {issue["code"] for issue in issues})

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
            ("gates: {G4: {? !!merge [unexpected] : {required: true}}}", "expected YAML merge key"),
            ("gates: {G4: {? !!merge unexpected : {required: true}}}", "expected YAML merge key"),
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

    def versioned(self, **data):
        self.write_manifest(schema_version=1, **data)
        return load_project_manifest(self.project)

    def test_versioned_manifest_accepts_full_schema(self):
        data = self.versioned(
            technology_stack={"repositories": {"api": {"dotnet": "8.0.100"}}},
            ai={"routing_policy": "default", "context_policy": "default", "default_profile": "balanced",
                "budget_policy": "std", "tool_bindings": {"claude": {"balanced": {
                    "model": "m", "effort": {"low": "low", "high": "max"}}}}})
        self.assertEqual(ai_policy_ids(data), {"routing_policy": "default", "context_policy": "default"})
        self.assertEqual(ai_policy_ids({}), {"routing_policy": "default", "context_policy": "default"})

    def test_versioned_manifest_rejects_invalid_schema(self):
        bad = [
            {"schema_version": 2},
            {"schema_version": True},
            {"schema_version": 1.0},
            {"technology_stack": {"repositories": []}},
            {"technology_stack": {"repositories": {"api": {"dotnet": 8}}}},
            {"technology_stack": {"repositories": {"api": {"dotnet": "latest"}}}},
            {"technology_stack": {"repositories": {"bad alias": {"dotnet": "8"}}}},
            {"ai": {"routing_policy": ""}},
            {"ai": {"budget_policy": {"amount": 5}}},
            {"ai": {"tool_bindings": {"claude": {"p": {"model": ""}}}}},
            {"ai": {"tool_bindings": {"claude": {"p": {"model": "m", "effort": {"extreme": "x"}}}}}},
            {"ai": {"tool_bindings": {"claude": {"p": {"model": "m", "extra": 1}}}}},
        ]
        for extra in bad:
            with self.subTest(extra=extra):
                data = {"schema_version": 1, **extra}
                self.write_manifest(**data)
                with self.assertRaises(ValueError):
                    load_project_manifest(self.project)
                codes = {i["code"] for i in validate_project(self.project)}
                self.assertIn("INVALID_METADATA", codes)

    def test_versioned_manifest_rejects_duplicate_keys_but_legacy_allows(self):
        path = self.project / PROJECT_MANIFEST
        path.parent.mkdir(parents=True)
        body = "project: {id: demo, name: Demo}\nai: {tools: [a]}\nai: {tools: [b]}\n"
        path.write_text(body, encoding="utf-8")
        self.assertEqual(load_project_manifest(self.project)["ai"], {"tools": ["b"]})
        path.write_text("schema_version: 1\n" + body, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate YAML key"):
            load_project_manifest(self.project)

    def test_legacy_manifest_ignores_new_fields_and_empty_versioned_stack_warns(self):
        self.write_manifest(ai={"routing_policy": 7}, technology_stack={"repositories": 3})
        load_project_manifest(self.project)
        self.write_manifest(schema_version=1, technology_stack={"repositories": {}})
        codes = {i["code"] for i in validate_project(self.project)}
        self.assertIn("STACK_UNDEFINED", codes)

    def test_init_scaffolds_versioned_manifest_that_validates(self):
        shutil.copytree(PLATFORM / "scripts", self.root / "platform/scripts")
        shutil.copytree(PLATFORM / "src", self.root / "platform/src", ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copytree(PLATFORM.parent / "framework", self.root / "framework")
        result = run([sys.executable, "-B", str(self.root / "platform/scripts/init-project.py"),
                      "--name", "Demo", "--slug", "demo"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load_project_manifest(self.project)
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["technology_stack"], {"repositories": {}})
        self.assertEqual(ai_policy_ids(data), {"routing_policy": "default", "context_policy": "default"})
        self.assertNotIn("project_management", data)
        self.assertEqual(data["ai"]["default_tool"], "claude")
        manifest = self.project / PROJECT_MANIFEST
        contents = manifest.read_bytes() + b"\n# local customization\n"
        manifest.write_bytes(contents)
        rerun = run(result.args, capture_output=True, text=True)
        self.assertEqual(rerun.returncode, 1, rerun.stderr)
        self.assertIn("Project already exists", rerun.stdout + rerun.stderr)
        self.assertEqual(manifest.read_bytes(), contents)

    def test_example_manifest_is_valid(self):
        self.project.joinpath(".ai-sdlc").mkdir(parents=True)
        shutil.copy(PLATFORM / "config-examples/project.yaml", self.project / PROJECT_MANIFEST)
        self.assertEqual(load_project_manifest(self.project)["schema_version"], 1)

    def test_legacy_project_gets_migration_hint(self):
        self.project.mkdir(parents=True)
        (self.project / "config.yml").write_text("project: {slug: demo, name: Demo}", encoding="utf-8")
        issue = next(issue for issue in validate_project(self.project) if issue["code"] == "MISSING_MANIFEST")
        self.assertIn("project.slug to project.id", issue["message"])
