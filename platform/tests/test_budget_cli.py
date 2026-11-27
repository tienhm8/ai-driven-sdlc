import csv
import importlib.util
import io
import json
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

PLATFORM = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), PLATFORM / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def usage_record(**overrides):
    record = {
        "work_item_id": "WI-1", "repo": "proj", "stage": "build", "task": "t1", "run_id": "r1",
        "provider": "p", "account": "a", "session_id": "s1", "event_id": "e1", "unit": "request",
        "observed_at": "2026-01-01T00:00:00Z", "status": "ok", "basis": "billed",
        "charge": "metered", "amount": "1.50",
    }
    record.update(overrides)
    return record


class BudgetCliTests(TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.cli = load_script("ai-budget")
        (self.root / "proj").mkdir()
        self.base = ["--project", str(self.root / "proj"), "--state-dir", str(self.root / "state")]

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = self.cli.main([*self.base, *argv])
        return code, out.getvalue(), err.getvalue()

    def write(self, name, value):
        path = self.root / name
        path.write_text(value if isinstance(value, str) else json.dumps(value), encoding="utf-8")
        return str(path)

    def test_register_approve_report_json_and_csv(self):
        self.assertEqual(self.run_cli("register", "WI-1")[0], 0)
        code, _, err = self.run_cli("approve", "WI-1", "--usd", "25.00", "--approver", "alice", "--reason", "plan")
        self.assertEqual(code, 0, err)
        code, out, _ = self.run_cli("report", "WI-1")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["work_item_id"], "WI-1")
        code, out, _ = self.run_cli("report", "WI-1", "--format", "csv")
        rows = list(csv.reader(io.StringIO(out)))
        self.assertEqual(len(rows), 2)
        self.assertIn("work_item_id", rows[0])
        self.assertEqual(len(rows[0]), len(rows[1]))

    def test_import_usage_and_history(self):
        self.run_cli("register", "WI-1")
        self.run_cli("approve", "WI-1", "--usd", "25.00", "--approver", "alice", "--reason", "plan")
        code, out, err = self.run_cli("import-usage", self.write("u.json", [usage_record()]))
        self.assertEqual(code, 0, err)
        self.assertIn("imported 1", out)
        code, out, _ = self.run_cli("history", "WI-1")
        self.assertEqual(code, 0)
        self.assertIsInstance(json.loads(out), list)

    def test_import_usage_rejects_bad_input_cleanly(self):
        for path in (self.write("bad.json", "{not json"), self.write("obj.json", {}),
                     self.write("items.json", [1]), str(self.root / "missing.json")):
            code, out, err = self.run_cli("import-usage", path)
            self.assertEqual((code, out), (1, ""))
            self.assertTrue(err.startswith("[ERROR]"))
            self.assertNotIn("Traceback", err)

    def test_settle_rejects_non_object_usage(self):
        code, _, err = self.run_cli("settle", "res-1", "--usage", self.write("u.json", []))
        self.assertEqual(code, 1)
        self.assertIn("JSON object", err)

    def test_ledger_errors_are_clean(self):
        code, _, err = self.run_cli("report", "NOPE")
        self.assertEqual(code, 1)
        self.assertIn("[ERROR]", err)
        self.assertNotIn("Traceback", err)

    def test_approver_required(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.cli.main([*self.base, "approve", "WI-1", "--usd", "1", "--reason", "x"])

    def test_flatten(self):
        self.assertEqual(self.cli.flatten({"a": {"b": 1}, "c": [2, None]}), {"a.b": 1, "c.0": 2, "c.1": ""})
