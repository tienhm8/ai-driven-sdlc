from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
from unittest import TestCase

import yaml

from ai_sdlc_platform.model_router import ModelRouter, RoutingError

SHARED_AI = Path(__file__).resolve().parents[2] / "shared-ai"


class ModelRouterTests(TestCase):
    def test_every_bundled_task_uses_its_profile_and_default_effort(self):
        tasks = yaml.safe_load((SHARED_AI / "model-routing/task-model-mapping.yaml").read_text(encoding="utf-8"))["tasks"]
        router = ModelRouter(SHARED_AI)
        self.assertTrue(tasks)
        for task, config in tasks.items():
            with self.subTest(task=task):
                result = router.route(task)
                self.assertEqual(result["profile_id"], config["profile"])
                self.assertEqual(result["effort"], config["effort"])
                self.assertIn("text", result["required_capabilities"])
        self.assertEqual(router.route("documentation")["fallback"], ["implementation"])
        self.assertEqual(router.route("code-review")["fallback"], [])

    def test_effort_can_increase_but_not_drop_below_task_or_risk_floor(self):
        router = ModelRouter(SHARED_AI)
        self.assertEqual(router.route("documentation", effort="medium")["effort"], "medium")
        self.assertEqual(router.route("documentation", risk="high")["effort"], "high")
        self.assertEqual(router.route("code-review", effort="low", risk="low")["effort"], "high")

    def test_unknown_inputs_require_manual_selection(self):
        router = ModelRouter(SHARED_AI)
        for task, kwargs in [("default", {}), ("documentation", {"effort": "max"}),
                             ("documentation", {"risk": "unclassified"})]:
            with self.subTest(task=task, kwargs=kwargs), self.assertRaises(RoutingError):
                router.route(task, **kwargs)

    def test_policy_read_and_yaml_errors_are_routing_errors_with_the_cause(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(SHARED_AI / "model-routing", root / "model-routing")
            policy = root / "model-routing/fallback-policy.yaml"
            for content in (None, "broken: [", "- not a mapping"):
                with self.subTest(content=content):
                    if content is None:
                        policy.unlink()
                    else:
                        policy.write_text(content, encoding="utf-8")
                    with self.assertRaisesRegex(RoutingError, "Could not load fallback-policy.yaml") as error:
                        ModelRouter(root)
                    self.assertIsNotNone(error.exception.__cause__)

    def test_v1_validation_and_fallback_capability_filter(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(SHARED_AI / "model-routing", root / "model-routing")
            fallback = root / "model-routing/fallback-policy.yaml"
            fallback.write_text("schema_version: 1\nmax_fallbacks: 1\nfallbacks:\n"
                                "  implementation: [routine, implementation, critical-review]\n", encoding="utf-8")
            self.assertEqual(ModelRouter(root).route("code-generation")["fallback"], ["critical-review"])
            mapping = root / "model-routing/task-model-mapping.yaml"
            mapping.write_text("schema_version: 1\ntasks: {demo: {profile: missing, effort: low}}\n", encoding="utf-8")
            with self.assertRaisesRegex(RoutingError, "Undefined model profile"):
                ModelRouter(root).route("demo")
            mapping.write_text("schema_version: 2\ntasks: {}\n", encoding="utf-8")
            with self.assertRaisesRegex(RoutingError, "schema_version 1"):
                ModelRouter(root)
