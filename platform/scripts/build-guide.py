#!/usr/bin/env python3
"""Embed framework/guide/guide-data.yml into framework/guide/index.html.

Run after editing guide-data.yml so the page also works when opened via file://.
"""

from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ai_sdlc_platform.guide import render_guide_html


def main():
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Build the framework guide page")
    parser.add_argument("--check", action="store_true", help="Fail if index.html is out of date")
    args = parser.parse_args()

    guide_dir = root / "framework" / "guide"
    page = guide_dir / "index.html"
    current = page.read_text(encoding="utf-8")
    updated = render_guide_html(current, guide_dir / "guide-data.yml")

    if args.check:
        if current != updated:
            print("[ERROR] framework/guide/index.html is out of date; run build-guide.py", file=sys.stderr)
            sys.exit(1)
        print("[OK] guide is up to date")
        return
    if current != updated:
        page.write_text(updated, encoding="utf-8")
        print(f"[UPDATE] {page}")
    else:
        print("[OK] guide is up to date")


if __name__ == "__main__":
    main()
