"""Check repository template links and pipe-delimited tables, without network access."""
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

from ai_sdlc_platform.markdown_view import render_markdown_page


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework"
# These two documents are entry points for, or contain, a canonical template.
RELATED_DOCS = (
    FRAMEWORK / "04-development/workflow.md",
    FRAMEWORK / "06-testing-qa/test-strategy/test-coverage.md",
)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
DIVIDER_CELL = re.compile(r":?-{1,}:?")
# Don't count pipes in code spans or pipes escaped outside a code span.
CELL_TOKEN = re.compile(r"\\.|(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)|\|")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.anchors.add(attributes["id"])
        attribute = {"a": "href", "img": "src"}.get(tag)
        if attribute and attributes.get(attribute):
            self.links.add(attributes[attribute])


@lru_cache(maxsize=None)
def parse_page(path):
    page = Page()
    # The guide link in the wrapper is not part of the source document.
    rendered = render_markdown_page(path.read_text(encoding="utf-8"), title="", path="", guide_url="")
    page.feed(rendered.decode("utf-8"))
    return page


def table_cells(line):
    line = line.strip()
    pipes = [match.start() for match in CELL_TOKEN.finditer(line) if match[0] == "|"]
    if len(pipes) < 2 or pipes[0] != 0 or pipes[-1] != len(line) - 1:
        return None
    return [line[left + 1:right].strip() for left, right in zip(pipes, pipes[1:])]


def table_errors(text):
    """Check the fully pipe-delimited table style used by framework templates."""
    fence = None
    previous = None
    width = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1].startswith(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
        cells = table_cells(line) if not marker else None
        if cells is None:
            previous = width = None
            continue
        if width is None:
            if previous and all(DIVIDER_CELL.fullmatch(cell) for cell in cells):
                width = len(previous)
        if width is not None and len(cells) != width:
            yield f"{number}: expected {width} table cells, found {len(cells)}"
        previous = cells


class TemplateDocsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = sorted(p for p in FRAMEWORK.rglob("*.md") if "templates" in p.relative_to(FRAMEWORK).parts[:-1])
        cls.paths.extend(RELATED_DOCS)

    def test_local_links_and_markdown_anchors_exist(self):
        for source in self.paths:
            for link in sorted(parse_page(source).links):
                url = urlsplit(link)
                if url.scheme or url.netloc:
                    continue
                target = (source.parent / unquote(url.path)).resolve() if url.path else source
                with self.subTest(source=source.relative_to(ROOT), link=link):
                    self.assertTrue(target.exists(), f"Missing target: {target}")
                    if url.fragment and target.suffix == ".md":
                        self.assertIn(unquote(url.fragment), parse_page(target).anchors)

    def test_pipe_tables_have_consistent_width(self):
        for path in self.paths:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(list(table_errors(path.read_text(encoding="utf-8"))), [])

    def test_table_check_handles_escaped_pipes_code_and_mismatched_rows(self):
        text = "\n".join([
            "```md", "| A | B |", "|---|", "```", "",
            "| `A|B` | C |", "|---|", r"| A\|B | C |", "| Too short |",
        ])
        self.assertEqual(list(table_errors(text)), [
            "7: expected 2 table cells, found 1",
            "9: expected 2 table cells, found 1",
        ])