from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import Mock, patch

import yaml

from ai_sdlc_platform.constants import STAGES
from ai_sdlc_platform.context_resolver import ContextRequest
from ai_sdlc_platform.managed_model import ManagedModelRunner, Observation, ToolReply
from ai_sdlc_platform.model_router import ModelRouter
from ai_sdlc_platform.tool_adapters import ToolAdapterRegistry
from ai_sdlc_platform.tool_binding import BindingError, ToolBinder


ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "shared-ai"


class ManagedModelTests(TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.project = self.root / "project"
        self.manifest = self.project / ".ai-sdlc/project.yaml"
        self.manifest.parent.mkdir(parents=True)
        self.ai = {"tools": ["claude", "second"], "default_tool": "claude", "budget_policy": "story-budget",
                   "tool_bindings": {"second": {"implementation": {"model": "other-model"}}}}
        self.save_manifest()
        self.registry = ToolAdapterRegistry(self.root / "adapters")
        self.adapter("claude", "default-model", ["routine"], ["text"], {"low": "native-small", "high": "native-large"})
        self.adapter("second", "other-model", ["implementation"], ["text", "code"], {"low": "compact", "high": "deep"})
        self.request = ContextRequest("US-0001", "be", "a" * 40, "ba", STAGES[0], "documentation", "low", ("docs/story.md",))
        resolver = patch("ai_sdlc_platform.managed_model.resolve_context", return_value={"blockers": []})
        self.resolve = resolver.start()
        self.addCleanup(resolver.stop)
        self.scope = Mock(return_value=True)
        self.data = Mock(return_value=True)
        self.budget = Mock(return_value=True)
        self.first = Mock(return_value=ToolReply("ok", "answer", Observation("default-model", "native-small")))
        self.second = Mock(return_value=ToolReply("ok", "other answer", Observation("other-model", "compact")))
        self.audit = Mock()
        self.wait = Mock()
        self.attempt_budget = Mock()
        self.attempt_budget.reserve.return_value = "fixture-reservation"
        self.attempt_budget.settle.return_value = "settled"

    def save_manifest(self):
        self.manifest.write_text(yaml.safe_dump({"schema_version": 1, "project": {"id": "demo", "name": "Demo"},
                                                 "ai": self.ai}), encoding="utf-8")

    def adapter(self, name, model, profiles, caps, effort, *, data_policy="private", allow_default=False, enabled=True):
        target = self.registry.root / name / "adapter.yaml"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump({"name": name, "enabled": enabled, "routing": {"default_model": model,
                          "models": {model: {"capabilities": caps, "profiles": profiles, "effort": effort,
                                             "data_policy": data_policy, "capability_evidence": "evidence:v1",
                                             "allow_uncontrolled_routine_effort": allow_default}}}}), encoding="utf-8")

    def runner(self, *, with_ledger=True):
        return ManagedModelRunner(self.project, ROOT / "framework", SHARED, {}, self.root / "state",
                                  adapters=self.registry, transports={"claude": self.first, "second": self.second},
                                  authorize_scope=self.scope, allow_data=self.data, allow_budget=self.budget,
                                  audit=self.audit, wait=self.wait, budget=self.attempt_budget if with_ledger else None)

    def test_declared_ledger_policy_cannot_fall_back_to_boolean_preflight(self):
        result = self.runner(with_ledger=False).run(self.request, b"synthetic")
        self.assertEqual((result.status, result.reason), ("blocked", "BUDGET_LEDGER_NOT_CONFIGURED"))
        self.first.assert_not_called()

    def run_task(self, request=None, payload=b"fixture private input"):
        return self.runner().run(request or self.request, payload)

    def test_preflight_maps_native_effort_and_records_only_route_metadata(self):
        result = self.run_task()
        self.assertEqual((result.status, result.content), ("completed", "answer"))
        self.assertEqual(result.attempts[0]["effective_effort"], "low")
        self.assertEqual(result.attempts[0]["requested_native_effort"], "native-small")
        self.assertEqual(result.attempts[0]["effective_model"], "default-model")
        attempt, payload = self.data.call_args.args
        self.assertEqual(attempt.budget_policy, "story-budget")
        self.assertEqual(payload, b"fixture private input")
        self.budget.assert_called_once_with(attempt)
        self.assertEqual([call.args[0]["status"] for call in self.audit.call_args_list], ["preflight_passed", "ok"])
        self.assertNotIn("fixture private input", repr(self.audit.call_args_list))
        self.assertNotIn(str(self.project), repr(self.audit.call_args_list))
        self.assertNotIn("answer", repr(self.audit.call_args_list))

    def test_denials_and_missing_context_do_not_dispatch(self):
        for check, code in ((self.scope, "SCOPE_DENIED"), (self.data, "DATA_DENIED"),
                            (self.budget, "BUDGET_NOT_APPROVED")):
            with self.subTest(code=code):
                check.return_value = None
                self.assertEqual(self.run_task().reason, code)
                check.return_value = True
        self.budget.side_effect = RuntimeError("internal data")
        self.assertEqual(self.run_task().reason, "BUDGET_NOT_APPROVED")
        self.assertEqual(self.run_task(payload=b"").reason, "MISSING_PAYLOAD")
        self.assertEqual(self.run_task(replace(self.request, task="code-generation")).reason, "MANAGED_ACTION_MISMATCH")
        self.assertEqual(self.run_task(replace(self.request, action="merge")).reason, "MANAGED_ACTION_MISMATCH")
        self.resolve.return_value = {"blockers": [{"code": "GATE_UNVERIFIED"}]}
        self.assertEqual(self.run_task(replace(self.request, action="coding", task="code-generation",
                                                stage=STAGES[3])).reason, "GATE_UNVERIFIED")
        self.first.assert_not_called()
        self.second.assert_not_called()

    def test_retry_and_one_non_chained_fallback_repeat_all_preflight_checks(self):
        self.first.return_value = ToolReply("rate_limited", safe_to_repeat=True, retry_after_seconds=2)
        self.second.return_value = ToolReply("temporarily_unavailable", safe_to_repeat=True)
        result = self.run_task()
        self.assertEqual(result.reason, "ATTEMPT_POLICY_EXHAUSTED")
        self.assertEqual([a["cause"] for a in result.attempts], ["initial", "retry", "fallback"])
        self.assertEqual([a["requested_native_effort"] for a in result.attempts], ["native-small", "native-small", "compact"])
        self.assertEqual([a["previous_status"] for a in result.attempts], [None, "rate_limited", "rate_limited"])
        for callback in (self.resolve, self.scope, self.data, self.budget):
            self.assertEqual(callback.call_count, 3)
        self.assertEqual([call.args for call in self.wait.call_args_list], [(2,), (2,)])
        self.assertEqual(self.second.call_count, 1)

    def test_no_retry_or_fallback_on_refusal_budget_errors_or_uncertain_outcome(self):
        for error_code in ("refusal", "permission_denied", "invalid_request", "budget_exceeded", "unknown_error"):
            with self.subTest(error_code=error_code):
                self.first.reset_mock()
                self.first.return_value = ToolReply(error_code, "do not return this", safe_to_repeat=True)
                result = self.run_task()
                self.assertEqual(result.reason, error_code.upper())
                self.assertIsNone(result.content)
                self.first.assert_called_once()
        for reply, expected in ((ToolReply("temporarily_unavailable"), "TEMPORARILY_UNAVAILABLE"),
                                (ToolReply("rate_limited", safe_to_repeat=True, retry_after_seconds=121),
                                 "RETRY_DELAY_OUT_OF_RANGE")):
            self.first.return_value = reply
            self.assertEqual(self.run_task().reason, expected)
        self.wait.assert_not_called()
        self.second.assert_not_called()

    def test_gate_and_budget_are_rechecked_after_wait(self):
        self.first.return_value = ToolReply("rate_limited", safe_to_repeat=True, retry_after_seconds=1)
        self.wait.side_effect = lambda _: setattr(self.resolve, "return_value", {"blockers": [{"code": "GATE_UNVERIFIED"}]})
        self.assertEqual(self.run_task().reason, "GATE_UNVERIFIED")
        self.first.assert_called_once()
        self.resolve.return_value = {"blockers": []}
        self.wait.side_effect = None
        self.budget.side_effect = [True, True, False]
        result = self.run_task()
        self.assertEqual(result.reason, "BUDGET_NOT_APPROVED")
        self.assertEqual(len(result.attempts), 2)
        self.second.assert_not_called()

    def test_fallback_needs_own_capability_same_data_policy_and_explicit_binding(self):
        self.first.return_value = ToolReply("temporarily_unavailable", safe_to_repeat=True)
        for policy, caps, effort in (("public", ["text", "code"], {"low": "compact"}),
                                     ("private", ["text"], {"low": "compact"}),
                                     ("private", ["text", "code"], {"medium": "balanced"})):
            self.adapter("second", "other-model", ["implementation"], caps, effort, data_policy=policy)
            self.assertEqual(self.run_task().reason, "NO_APPROVED_FALLBACK")
        self.adapter("second", "other-model", ["implementation"], ["text", "code"], {"low": "compact"})
        self.ai.pop("tool_bindings")
        self.save_manifest()
        self.assertEqual(self.run_task().reason, "NO_APPROVED_FALLBACK")
        self.second.assert_not_called()

    def test_unverified_effort_only_when_operator_approves_routine_default(self):
        self.adapter("claude", "default-model", ["routine"], ["text"], {}, allow_default=True)
        self.first.return_value = ToolReply("ok", "answer", Observation("default-model"))
        result = self.run_task()
        self.assertEqual(result.status, "completed")
        self.assertEqual(result.attempts[0]["observation"], "unverified")
        self.assertIsNone(result.attempts[0]["effective_effort"])
        elevated = replace(self.request, focus=frozenset({"auth"}))
        self.assertEqual(self.run_task(elevated).reason, "EFFORT_UNSUPPORTED")
        self.first.assert_called_once()

    def test_effective_route_is_never_inferred_and_mismatch_stops(self):
        for observation, reason in ((Observation(), "EFFECTIVE_ROUTE_UNVERIFIED"),
                                    (Observation("unexpected", "native-small"), "OBSERVED_ROUTE_MISMATCH"),
                                    (Observation("default-model", "other"), "OBSERVED_ROUTE_MISMATCH")):
            self.first.return_value = ToolReply("ok", "answer", observation)
            result = self.run_task()
            self.assertEqual(result.reason, reason)
            self.assertIsNone(result.content)
            self.assertEqual(result.attempts[0]["effective_model"], observation.model)
            if observation.native_effort != "native-small":
                self.assertIsNone(result.attempts[0]["effective_effort"])
        self.second.assert_not_called()

    def test_unapproved_tool_model_and_effort_mapping(self):
        router = ModelRouter(SHARED)
        binder = ToolBinder(self.registry, router)
        route = router.route("documentation", risk="low")
        self.ai["tool_bindings"]["claude"] = {"routine": {"model": "default-model", "effort": {"low": "low"}}}
        with self.assertRaisesRegex(BindingError, "NATIVE_EFFORT_NOT_APPROVED"):
            binder.primary(self.ai, route)
        self.ai["tool_bindings"]["claude"]["routine"]["model"] = "unapproved"
        with self.assertRaisesRegex(BindingError, "MODEL_NOT_APPROVED"):
            binder.primary(self.ai, route)
        self.adapter("claude", "default-model", ["routine"], ["text"], {}, enabled=False)
        with self.assertRaisesRegex(BindingError, "TOOL_NOT_APPROVED"):
            binder.primary(self.ai, route)

    def test_audit_failure_is_fail_closed(self):
        self.audit.side_effect = RuntimeError("no sink")
        self.assertEqual(self.run_task().reason, "AUDIT_UNAVAILABLE")
        self.first.assert_not_called()
        self.audit.side_effect = [None, RuntimeError("no sink")]
        result = self.run_task()
        self.assertEqual(result.reason, "AUDIT_UNAVAILABLE_AFTER_DISPATCH")
        self.first.assert_called_once()
        # The reply was already paid for: keep it, but never present it as completed output.
        self.assertEqual((result.status, result.content, result.unresolved_content), ("manual", "answer", True))

    def test_unverified_route_never_keeps_content(self):
        self.audit.side_effect = [None, RuntimeError("no sink")]
        self.first.return_value = ToolReply("ok", "answer", Observation("unexpected", "native-small"))
        result = self.run_task()
        self.assertEqual(result.status, "manual")
        self.assertIsNone(result.content)
        self.assertFalse(result.unresolved_content)
