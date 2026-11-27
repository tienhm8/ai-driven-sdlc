from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Barrier
from unittest import TestCase
from unittest.mock import Mock, patch

import yaml

from ai_sdlc_platform.ai_budget import BudgetError, BudgetLedger
from ai_sdlc_platform.budget_runner import LedgerAttemptBudget
from ai_sdlc_platform.constants import STAGES
from ai_sdlc_platform.context_resolver import ContextRequest
from ai_sdlc_platform.managed_model import ManagedModelRunner, Observation, ToolReply
from ai_sdlc_platform.tool_adapters import ToolAdapterRegistry


ROOT = Path(__file__).resolve().parents[2]


def usage(event="evt-1", item="US-0001", **overrides):
    data = {"work_item_id": item, "repo": "be", "stage": STAGES[0], "task": "documentation",
            "run_id": "local-run-1", "provider": "fixture", "account": "fixture-account", "session_id": "session-1",
            "event_id": event, "observed_at": "2026-11-27T00:00:00Z", "unit": "request", "basis": "reported",
            "status": "ok", "amount": "1.25"}
    data.update(overrides)
    if data["basis"] not in {"billed", "reported"}:
        data.pop("amount")
    return data


class BudgetLedgerTests(TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.project = self.root / "instance"
        self.project.mkdir()
        self.ledger = BudgetLedger(self.project, self.root / "state")
        self.ledger.register_item("FEAT-0001")
        self.ledger.register_item("US-0001", parent="FEAT-0001")
        self.ledger.register_item("US-0002", parent="FEAT-0001")

    def approve(self, item, amount):
        return self.ledger.approve_limit(item, amount, approver="budget-owner", reason="Synthetic approval")

    def reserve(self, amount, *, item="US-0001", run="attempt-run", attempt=1):
        return self.ledger.reserve(item, amount, run_id=run, attempt=attempt, repo="be", stage=STAGES[0],
                                   task="documentation", tool="claude")

    def review(self, amount, item="US-0001"):
        return self.ledger.review(item, reviewer="operator", completed="Planning complete", remaining="Validation",
                                  reason="80 percent threshold", projected_usd=amount)

    def test_story_rollup_sums_both_repos_sibling_and_direct_feature_usage_once(self):
        entries = [usage("be"), usage("fe", repo="fe", status="rate_limited", amount="0.25"),
                   usage("sibling", "US-0002", session_id="session-2", amount="2.5"),
                   usage("planning", "FEAT-0001", session_id="plan", amount="4", basis="billed")]
        self.assertEqual(self.ledger.import_usage(entries), 4)
        self.assertEqual(self.ledger.import_usage(entries), 0)
        story = self.ledger.report("US-0001")
        feature = self.ledger.report("FEAT-0001")
        self.assertEqual(story["spent"]["reported"], "1.500000")
        self.assertEqual(feature["spent"]["reported"], "4.000000")
        self.assertEqual(feature["spent"]["billed"], "4.000000")
        self.assertEqual({row["repo"] for row in self.ledger.usage("US-0001")}, {"be", "fe"})
        self.assertEqual(len(self.ledger.usage("FEAT-0001")), 4)
        self.assertIsNone(story["approved"])
        self.assertEqual(story["coverage"]["outside_managed_runner"], "not-enforced")

    def test_price_cache_fee_fx_and_seat_estimate_do_not_inflate_metered_spend(self):
        fields = {"basis": "estimated", "price_source": "prices:v1", "price_effective_on": "2026-11-01",
                  "usage": {"input": 1000, "output": 2000, "cache_read": 3000, "cache_write": 4000},
                  "pricing": {"input": "2", "output": "3", "cache_read": "0.1", "cache_write": "4", "fee": "0.1"}}
        estimate = usage("estimate", **fields)
        seat = usage("seat", session_id="seat", charge="seat", **fields)
        foreign = usage("billed", basis="billed", amount="2", currency="EUR", fx_to_usd="1.125", fx_source="fx:nov")
        self.ledger.import_usage([estimate, seat, foreign])
        report = self.ledger.report("US-0001")
        self.assertEqual(report["spent"]["estimated"], "0.124300")
        self.assertEqual(report["spent"]["billed"], "2.250000")
        self.assertEqual(report["seat_estimates"], "0.124300")
        self.assertEqual(report["coverage"]["seat_records"]["estimated"], 1)
        reconciled = usage("estimate", basis="billed", amount="0.2")
        self.assertEqual(self.ledger.import_usage([reconciled, estimate]), 1)
        report = self.ledger.report("US-0001")
        self.assertEqual(report["spent"]["estimated"], "0.000000")
        self.assertEqual(report["spent"]["billed"], "2.450000")

    def test_cumulative_session_snapshots_replace_not_add_and_block_mixed_units(self):
        first = usage("snapshot-1", unit="session", sequence=1, amount="1")
        second = usage("snapshot-2", unit="session", sequence=2, amount="3")
        self.ledger.import_usage([first, second])
        self.assertEqual(self.ledger.report("US-0001")["spent"]["reported"], "3.000000")
        self.assertEqual(self.ledger.import_usage([first]), 0)
        for record in (usage("mixed"), usage("decrease", unit="session", sequence=3, amount="2"),
                       usage("moved", "US-0002", unit="session", sequence=3, amount="4")):
            with self.subTest(record=record["event_id"]), self.assertRaises(BudgetError):
                self.ledger.import_usage([record])
        self.ledger.import_usage([usage("invoice", unit="session", sequence=3, basis="billed", amount="2.75")])
        self.assertEqual(self.ledger.report("US-0001")["spent"]["billed"], "2.750000")
        self.assertEqual(len(self.ledger.usage("US-0001")), 1)

    def test_conflicting_identity_rolls_back_import_and_disallows_raw_payload(self):
        self.ledger.import_usage([usage(request_id="provider-request")])
        with self.assertRaisesRegex(BudgetError, "request is already attributed"):
            self.ledger.import_usage([usage("isolated"), usage("other-id", request_id="provider-request")])
        self.assertEqual(len(self.ledger.usage("US-0001")), 1)
        for invalid in (usage(prompt="private"), usage(amount=1.2), usage(usage={"input": -1}),
                        usage(basis="estimated", usage={"input": 1}), usage("evt-1", item="US-0002", basis="billed")):
            with self.assertRaises(BudgetError):
                self.ledger.import_usage([invalid])

    def test_unmeasured_is_not_zero_and_blocks_until_reconciled(self):
        self.approve("US-0001", "10")
        self.ledger.import_usage([usage(basis="unmeasured", usage={"input": 15})])
        report = self.ledger.report("US-0001")
        self.assertIsNone(report["spent"]["unmeasured"])
        self.assertIsNone(report["remaining"])
        self.assertEqual(report["coverage"]["metered_records"]["unmeasured"], 1)
        with self.assertRaisesRegex(BudgetError, "incomplete-coverage"):
            self.reserve("1")
        self.ledger.import_usage([usage(basis="reported", amount="1")])
        self.assertEqual(self.ledger.report("US-0001")["remaining"], "9.000000")
        self.reserve("1")

    def test_eighty_percent_holds_then_review_allows_only_reviewed_projection(self):
        self.approve("US-0001", "10")
        self.ledger.import_usage([usage(amount="7.999999")])
        self.assertEqual(self.ledger.report("US-0001")["status"], "ready")
        self.ledger.import_usage([usage("threshold", amount="0.000001")])
        with self.assertRaisesRegex(BudgetError, "review-required"):
            self.reserve("1")
        review = self.review("1")
        self.assertEqual((review["status"], review["remaining"]), ("ready", "2.000000"))
        with self.assertRaisesRegex(BudgetError, "reviewed projection"):
            self.reserve("1.000001")
        self.reserve("1")

    def test_projected_shortfall_waits_for_explicit_increase_and_keeps_history(self):
        self.approve("FEAT-0001", "10")
        self.ledger.import_usage([usage(amount="8")])
        review = self.review("3", "FEAT-0001")
        self.assertEqual((review["status"], review["increase_needed"], review["approved"]),
                         ("awaiting-approval", "1.000000", "10.000000"))
        self.approve("FEAT-0001", "10.5")
        with self.assertRaisesRegex(BudgetError, "awaiting-approval"):
            self.reserve("0.1")
        self.approve("FEAT-0001", "11")
        self.reserve("3")
        event = [e for e in self.ledger.history("FEAT-0001") if e["event"] == "limit-approved"][-1]
        self.assertEqual((event["old_usd"], event["new_usd"], event["approver"]),
                         ("10.500000", "11.000000", "budget-owner"))
        self.assertTrue(event["at"])

    def test_atomic_parent_and_child_reservations_and_quote_limit(self):
        self.approve("FEAT-0001", "10")
        self.approve("US-0001", "7")
        self.approve("US-0002", "7")
        with self.assertRaisesRegex(BudgetError, "US-0001.*exceeds"):
            self.reserve("7.01")
        barrier = Barrier(2)

        def reserve(index):
            barrier.wait(timeout=5)
            try:
                self.reserve("6", item=f"US-000{index}", run=f"run-{index}")
                return "ok"
            except BudgetError as exc:
                return exc.code

        with ThreadPoolExecutor(max_workers=2) as threads:
            result = list(threads.map(reserve, (1, 2)))
        self.assertCountEqual(result, ["ok", "BUDGET_LIMIT_EXCEEDED"])
        self.assertEqual(self.ledger.report("FEAT-0001")["reserved"], "6.000000")

    def test_settlement_keeps_pending_then_releases_rest_and_deduplicates(self):
        self.approve("US-0001", "10")
        reservation = self.reserve("5")
        self.assertEqual(self.ledger.settle(reservation), "pending")
        self.assertIsNone(self.ledger.report("US-0001")["remaining"])
        with self.assertRaisesRegex(BudgetError, "incomplete-coverage"):
            self.reserve("1", attempt=2)
        itemless = usage("charge", run_id="attempt-run", amount="2")
        self.assertEqual(self.ledger.settle(reservation, usage=itemless), "settled")
        self.assertEqual(self.ledger.settle(reservation, usage=itemless), "settled")
        report = self.ledger.report("US-0001")
        self.assertEqual((report["reserved"], report["remaining"]), ("0.000000", "8.000000"))
        self.assertEqual(self.ledger.pending("US-0001"), [])
        next_reservation = self.reserve("1", attempt=2)
        self.assertEqual(self.ledger.settle(next_reservation, not_dispatched=True), "released")

    def test_reconciled_cost_above_quote_pauses_even_below_eighty_percent(self):
        self.approve("US-0001", "10")
        reservation = self.reserve("2")
        record = usage("charge", run_id="attempt-run", attempt=1, tool="claude", amount="1")
        self.assertEqual(self.ledger.settle(reservation, usage=record), "settled")
        self.ledger.import_usage([{**record, "basis": "billed", "amount": "3"}])
        report = self.ledger.report("US-0001")
        self.assertEqual(report["status"], "review-required")
        self.assertEqual(report["known_metered_total"], "3.000000")
        self.assertEqual(report["reserved"], "0.000000")

    def test_budget_cutoff_forces_review_without_waiting_for_eighty_percent(self):
        self.approve("FEAT-0001", "10")
        self.approve("US-0001", "10")
        reservation = self.reserve("5")
        record = usage("cutoff", run_id="attempt-run", amount="2", status="budget_exceeded")
        self.ledger.settle(reservation, usage=record, budget_cutoff=True)
        self.assertEqual(self.ledger.report("US-0001")["status"], "review-required")
        self.assertEqual(self.ledger.report("FEAT-0001")["status"], "review-required")
        with self.assertRaisesRegex(BudgetError, "review-required"):
            self.reserve("1", item="US-0002", attempt=2)

    def test_requires_private_external_state(self):
        with self.assertRaises(BudgetError):
            BudgetLedger(self.project, self.project / "state")
        self.ledger.path.chmod(0o644)
        with self.assertRaisesRegex(BudgetError, "private"):
            self.ledger.report("FEAT-0001")

    def test_runner_reserves_on_retry_and_stops_on_missing_usage(self):
        self.approve("US-0001", "10")
        manifest = self.project / ".ai-sdlc/project.yaml"
        manifest.parent.mkdir()
        manifest.write_text("schema_version: 1\nproject: {id: fixture, name: Fixture}\nai: {budget_policy: story}\n")
        registry = self.root / "registry"
        adapter = registry / "claude/adapter.yaml"
        adapter.parent.mkdir(parents=True)
        adapter.write_text(yaml.safe_dump({"name": "claude", "enabled": True, "routing": {"default_model": "model",
                           "models": {"model": {"profiles": ["routine"], "capabilities": ["text"],
                                               "data_policy": "private", "capability_evidence": "local:v1",
                                               "effort": {"low": "native-low"}}}}}))
        budget = LedgerAttemptBudget(self.ledger, policies={"story": lambda attempt: "3"})
        request = ContextRequest("US-0001", "be", "a" * 40, "ba", STAGES[0], "documentation", "low", ("docs/story.md",))
        calls = []

        def transport(bound, payload):
            report = self.ledger.report("US-0001")
            calls.append(report["reserved"])
            if len(calls) == 1:
                record = {k: v for k, v in usage("retry", amount="1", status="rate_limited").items()
                          if k not in {"work_item_id", "repo", "stage", "task", "run_id"}}
                return ToolReply("rate_limited", safe_to_repeat=True, usage=record)
            return ToolReply("ok", "synthetic", Observation("model", "native-low"))

        runner = ManagedModelRunner(self.project, ROOT / "framework", ROOT / "shared-ai", {}, self.root / "state",
                                    adapters=ToolAdapterRegistry(registry), transports={"claude": transport},
                                    authorize_scope=lambda _: True, allow_data=lambda *_: True,
                                    allow_budget=lambda _: True, audit=Mock(), budget=budget)
        with patch("ai_sdlc_platform.managed_model.resolve_context", return_value={"blockers": []}):
            result = runner.run(request, b"synthetic")
            denied = runner.run(request, b"synthetic")
        self.assertEqual(calls, ["3.000000", "3.000000"])
        self.assertEqual(result.reason, "BUDGET_USAGE_PENDING")
        self.assertEqual(denied.reason, "BUDGET_INCOMPLETE_COVERAGE")
        self.assertEqual([a["budget_status"] for a in result.attempts], ["settled", "pending"])
        self.assertEqual(self.ledger.report("US-0001")["spent"]["reported"], "1.000000")
