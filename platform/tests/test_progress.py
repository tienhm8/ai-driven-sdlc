from hashlib import sha256
import json
from pathlib import Path
import shutil
import sqlite3
import sys
from tempfile import TemporaryDirectory
from threading import Thread
from unittest import TestCase
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import importlib.util

from ai_sdlc_platform.approval_engine import VerifiedApprover
from ai_sdlc_platform.progress import collect_progress, store_path
from ai_sdlc_platform.workflow_engine import WorkflowEngine

PLATFORM = Path(__file__).resolve().parents[1]
FRAMEWORK = PLATFORM.parent / "framework"


def load_script(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), PLATFORM / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(text):
    return sha256(text.encode()).hexdigest()


class ProgressTests(TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.state = self.root / "state"
        shutil.copytree(FRAMEWORK, self.root / "framework")
        (self.root / "projects").mkdir()
        init = load_script("init-project")
        with open("/dev/null", "w") as null:
            from contextlib import redirect_stdout
            with redirect_stdout(null):
                init.init_project(self.root, "Demo", "demo", ["claude"], True)
        self.project = self.root / "projects" / "demo"
        self.framework = self.root / "framework"
        self.po = VerifiedApprover("po-id", frozenset({"product_owner"}), True)
        self.engine = WorkflowEngine(self.project, state_dir=self.state, verify_identity={"po": self.po}.get,
                                     can_approve=lambda identity, role, scope: True)

    def progress(self):
        return collect_progress(self.project, self.framework, self.state)

    def stage(self, result, stage_id):
        return next(s for s in result["stages"] if s["id"] == stage_id)

    def test_no_store_means_workflow_not_started(self):
        result = self.progress()
        self.assertEqual(result["workflow"], {"state": "not_started", "current_stage": None})
        self.assertEqual(result["next_actions"][0]["role"], "ba")
        self.assertTrue(all(s["status"] == "not_started" for s in result["stages"]))

    def test_seeded_templates_do_not_count_as_outputs(self):
        outputs = self.stage(self.progress(), "01-requirement-analysis")["outputs"]
        self.assertEqual(outputs["present"], [])
        self.assertIn("outputs/01-business-requirements/BRD.md", outputs["missing"])

    def test_edited_output_counts_as_present(self):
        brd = self.project / "docs/01-requirement-analysis/outputs/01-business-requirements/BRD.md"
        brd.write_text(brd.read_text(encoding="utf-8") + "\nNội dung thật của dự án\n", encoding="utf-8")
        outputs = self.stage(self.progress(), "01-requirement-analysis")["outputs"]
        self.assertIn("outputs/01-business-requirements/BRD.md", outputs["present"])

    def test_started_workflow_points_at_stage_01(self):
        self.engine.start()
        result = self.progress()
        self.assertEqual(result["workflow"], {"state": "in_progress", "current_stage": "01-requirement-analysis"})
        self.assertTrue(any("Hoàn thiện đầu ra" in a["text"] for a in result["next_actions"]))

    def test_review_then_approval_then_completion(self):
        run = self.engine.start()["execution_id"]
        review = self.engine.request_review(run, "G1", artifact_sha256=digest("a"), review_context_sha256=digest("c"),
                                            author_ids=["ba-id"], actor="ba", artifact_refs=["ref"])
        result = self.progress()
        self.assertEqual(self.stage(result, "01-requirement-analysis")["status"], "awaiting_gate")
        self.assertEqual(result["workflow"]["state"], "awaiting_gate")
        self.assertEqual([a["role"] for a in result["next_actions"]], ["product_owner"])

        self.engine.approvals.approve(run, "G1", "po", "approved", role="product_owner", review_id=review["event_id"],
                                      artifact_sha256=digest("a"), evidence_refs=["rec"])
        self.engine.complete_stage(run, "01-requirement-analysis", artifact_sha256=digest("a"),
                                   review_id=review["event_id"], review_context_sha256=digest("c"))
        result = self.progress()
        first = self.stage(result, "01-requirement-analysis")
        self.assertEqual((first["status"], first["gate"]["state"]), ("completed", "approved"))
        self.assertEqual(result["workflow"]["current_stage"], "02-system-design")
        self.assertEqual(self.stage(result, "02-system-design")["status"], "in_progress")

    def test_rejection_shows_blocked(self):
        run = self.engine.start()["execution_id"]
        review = self.engine.request_review(run, "G1", artifact_sha256=digest("a"), review_context_sha256=digest("c"),
                                            author_ids=["ba-id"], actor="ba", artifact_refs=["ref"])
        self.engine.approvals.approve(run, "G1", "po", "rejected", role="product_owner", review_id=review["event_id"],
                                      artifact_sha256=digest("a"), comment="Thiếu AC")
        stage = self.stage(self.progress(), "01-requirement-analysis")
        self.assertEqual((stage["status"], stage["gate"]["state"]), ("blocked", "blocked"))

    def test_store_path_with_uri_special_characters(self):
        state = self.root / "state?#odd"
        engine = WorkflowEngine(self.project, state_dir=state)
        engine.start()
        result = collect_progress(self.project, self.framework, state)
        self.assertEqual(result["workflow"]["current_stage"], "01-requirement-analysis")

    def test_approved_gate_not_yet_completed_asks_to_complete(self):
        run = self.engine.start()["execution_id"]
        review = self.engine.request_review(run, "G1", artifact_sha256=digest("a"), review_context_sha256=digest("c"),
                                            author_ids=["ba-id"], actor="ba", artifact_refs=["ref"])
        self.engine.approvals.approve(run, "G1", "po", "approved", role="product_owner", review_id=review["event_id"],
                                      artifact_sha256=digest("a"), evidence_refs=["rec"])
        result = self.progress()
        first = self.stage(result, "01-requirement-analysis")
        self.assertEqual((first["status"], first["gate"]["state"]), ("in_progress", "approved"))
        self.assertEqual(len(result["next_actions"]), 1)
        self.assertIn("hoàn tất giai đoạn", result["next_actions"][0]["text"])
        self.assertNotIn("trình duyệt", result["next_actions"][0]["text"])

    def test_reading_never_writes_the_store(self):
        self.engine.start()
        db = store_path(self.state, self.project)
        before = db.read_bytes()
        self.progress()
        self.assertEqual(db.read_bytes(), before)
        with self.assertRaises(sqlite3.OperationalError):
            connection = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
            try:
                connection.execute("INSERT INTO events (execution_id, event) VALUES ('x', '{}')")
            finally:
                connection.close()


class ServerTests(TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        shutil.copytree(FRAMEWORK, self.root / "framework")
        (self.root / "projects").mkdir()
        self.module = load_script("guide-server")
        self.server = self.module.ThreadingHTTPServer(
            ("127.0.0.1", 0), self.module.make_handler(self.root, self.root / "state"))
        Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def get(self, path):
        try:
            with urlopen(self.base + path) as response:
                return response.status, response.read()
        except HTTPError as error:
            return error.code, error.read()

    def init_project(self, slug="demo"):
        init = load_script("init-project")
        from contextlib import redirect_stdout
        with open("/dev/null", "w") as null, redirect_stdout(null):
            init.init_project(self.root, "Demo", slug, ["claude"], True)

    def test_empty_projects_directory(self):
        status, body = self.get("/api/projects")
        self.assertEqual((status, json.loads(body)), (200, {"projects": []}))

    def test_lists_and_reports_initialized_project(self):
        self.init_project()
        (self.root / "projects" / "not-a-project").mkdir()
        status, body = self.get("/api/projects")
        self.assertEqual(json.loads(body)["projects"], [{"id": "demo", "name": "Demo"}])
        status, body = self.get("/api/projects/demo/status")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["workflow"]["state"], "not_started")

    def test_rejects_unknown_traversal_and_writes(self):
        self.init_project()
        for path in ("/api/projects/nope/status", "/api/projects/..%2Fframework/status",
                     "/api/projects/%2e%2e/status", "/../etc/passwd", "/api/other", "/README.md"):
            self.assertEqual(self.get(path)[0], 404, path)
        request = Request(self.base + "/api/projects", data=b"{}", method="POST")
        with self.assertRaises(HTTPError) as caught:
            urlopen(request)
        self.assertEqual(caught.exception.code, 405)

    def test_serves_guide_page_and_linked_docs(self):
        status, body = self.get("/")  # urlopen follows the redirect to the page path
        self.assertEqual(status, 200)
        self.assertIn("AI-Driven SDLC Guide", body.decode())
        (self.root / "shared-ai/rules/core").mkdir(parents=True)
        (self.root / "shared-ai/rules/core/ai-usage-flow.md").write_text("rule", encoding="utf-8")
        for path in ("/framework/01-requirement-analysis/README.md", "/shared-ai/rules/core/ai-usage-flow.md"):
            self.assertEqual(self.get(path)[0], 200, path)

    def test_markdown_is_rendered_with_security_headers(self):
        with urlopen(self.base + "/framework/01-requirement-analysis/README.md") as response:
            body = response.read().decode()
            self.assertTrue(response.headers["Content-Type"].startswith("text/html"))
            self.assertIn("default-src 'none'", response.headers["Content-Security-Policy"])
        self.assertIn('<h1 id="01--requirement-analysis">', body)
        self.assertIn("<table>", body)
        self.assertNotIn("# 01", body)

    def test_folder_link_opens_readme_and_keeps_relative_links_working(self):
        status, body = self.get("/framework/01-requirement-analysis")  # redirected to trailing slash
        self.assertEqual(status, 200)
        self.assertIn("Requirement Analysis", body.decode())
        status, _ = self.get("/framework/01-requirement-analysis/workflow.md")
        self.assertEqual(status, 200)

    def test_does_not_serve_projects_hidden_or_outside_files(self):
        self.init_project()
        for path in ("/projects/demo/.ai-sdlc/project.yaml", "/framework/../platform/README.md",
                     "/framework/%2e%2e/README.md", "/platform/scripts/guide-server.py", "/framework/.hidden.md"):
            self.assertEqual(self.get(path)[0], 404, path)

    def test_rejects_foreign_host_header(self):
        request = Request(self.base + "/api/projects", headers={"Host": "evil.example"})
        with self.assertRaises(HTTPError) as caught:
            urlopen(request)
        self.assertEqual(caught.exception.code, 403)

    def test_binds_to_loopback_only(self):
        self.assertEqual(self.server.server_address[0], "127.0.0.1")
