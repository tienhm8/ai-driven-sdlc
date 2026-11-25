from pathlib import Path
import json
import re
from unittest import TestCase

from ai_sdlc_platform.guide import MARKER, load_guide_data, render_guide_html, validate_guide_data

ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework"
DATA = FRAMEWORK / "guide" / "guide-data.yml"
PAGE = FRAMEWORK / "guide" / "index.html"


class GuideDataTests(TestCase):
    def test_data_matches_platform_and_links_exist(self):
        self.assertEqual(validate_guide_data(load_guide_data(DATA), FRAMEWORK), [])

    def test_page_embeds_current_data(self):
        text = PAGE.read_text(encoding="utf-8")
        self.assertEqual(render_guide_html(text, DATA), text, "run platform/scripts/build-guide.py")
        embedded = json.loads(MARKER.search(text).group(2).replace("<\\/", "</"))
        self.assertEqual(embedded, load_guide_data(DATA))

    def test_every_role_has_a_task_or_gate(self):
        data = load_guide_data(DATA)
        used = {t["role"] for s in data["stages"] for t in s["tasks"]}
        for stage in data["stages"]:
            if stage["gate"]:
                used |= set(stage["gate"]["approvers"])
        self.assertEqual({r["id"] for r in data["roles"]} - used, set())

    def test_drift_is_detected(self):
        data = load_guide_data(DATA)
        data["stages"][0]["gate"]["id"] = "G2"
        data["stages"][1]["tasks"][0]["link"] = "does/not/exist.md"
        problems = validate_guide_data(data, FRAMEWORK)
        self.assertTrue(any("does not match" in p for p in problems))
        self.assertTrue(any("missing file" in p for p in problems))
