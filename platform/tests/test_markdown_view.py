from html.parser import HTMLParser
from pathlib import Path
import re
from unittest import TestCase
from urllib.parse import unquote, urlsplit

from ai_sdlc_platform.markdown_view import render_markdown_page


def render(text):
    return render_markdown_page(text, title="t.md", path="framework/t.md", guide_url="/framework/guide/index.html").decode()


class PageLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if attrs.get("id"):
            self.ids.add(attrs["id"])

class MarkdownViewTests(TestCase):
    def test_renders_tables_code_lists_and_links(self):
        html = render("# Tiêu đề\\n\\n| A | B |\\n|---|---|\\n| 1 | 2 |\\n\\n```text\\nx\\n```\\n\\n- [ ] việc\\n\\n[liên kết](other.md)\\n".replace("\\n", "\n"))
        for fragment in ('<h1 id="tiêu-đề">Tiêu đề</h1>', "<table>", "<td>1</td>", "<pre><code", "<li>", 'href="other.md"'):
            self.assertIn(fragment, html)
        self.assertIn("Quay lại guide", html)

    def test_vietnamese_section_links_match_heading_ids(self):
        html = render("[Mẫu](#mẫu-hồ-sơ)\n\n## Mẫu hồ sơ\n\n## Nguồn chuẩn")
        self.assertIn('href="#mẫu-hồ-sơ"', html)
        self.assertIn('<h2 id="mẫu-hồ-sơ">', html)
        self.assertIn('<h2 id="nguồn-chuẩn">', html)

    def test_heading_ids_keep_consecutive_hyphens_and_resolve_collisions(self):
        html = render("## Sử dụng `CLI` &amp; *mẫu*\n\n## A  B\n\n## Đợt\n\n## Đợt-1\n\n## Đợt\n\n## Đợt\n\n## Nháp\n\n## Nháp")
        self.assertEqual(re.findall(r'<h2 id="([^"]+)">', html), [
            "sử-dụng-cli--mẫu", "a--b", "đợt", "đợt-1", "đợt-2", "đợt-3", "nháp", "nháp-1",
        ])

    def test_headings_without_a_slug_keep_their_text_without_an_id(self):
        html = render("#   \n\n## 🚀\n\n## !?\n\n## Nháp\n\n## Nháp")
        self.assertIn("<h1></h1>", html)
        self.assertIn("<h2>🚀</h2>", html)
        self.assertIn("<h2>!?</h2>", html)
        self.assertEqual(re.findall(r'<h2 id="([^"]*)">', html), ["nháp", "nháp-1"])

    def test_heading_ids_decode_entities_without_decoding_literal_code(self):
        page = PageLinks(render("## Entity `&copy;`\n\n## Entity &copy;\n\n## Entity &amp;copy;"))
        self.assertEqual(page.ids, {"entity-copy", "entity-", "entity-copy-1"})

    def test_link_scan_ignores_code_examples_and_includes_reference_links(self):
        page = PageLinks(render("[Real][ref]\n\n[ref]: other.md#section\n\n"
                                "`[Inline](inline-example.md#section)`\n\n"
                                "```md\n[Fenced](fenced-example.md#section)\n```"))
        self.assertIn("other.md#section", page.links)
        self.assertNotIn("inline-example.md#section", page.links)
        self.assertNotIn("fenced-example.md#section", page.links)

    def test_repository_markdown_fragments_match_rendered_targets(self):
        repo = Path(__file__).resolve().parents[2]
        sources = [repo / "README.md"]
        for directory in ("framework", "shared-ai", "platform"):
            sources.extend((repo / directory).rglob("*.md"))
        pages = {}

        def page(path):
            if path not in pages:
                pages[path] = PageLinks(render(path.read_text(encoding="utf-8")))
            return pages[path]

        for source in sources:
            for link in page(source).links:
                url = urlsplit(link)
                relative = unquote(url.path)
                if url.scheme or url.netloc or not url.fragment or relative.startswith("/"):
                    continue
                if relative and Path(relative).suffix.lower() != ".md":
                    continue
                target = (source.parent / relative).resolve() if relative else source
                if not target.is_relative_to(repo):
                    continue
                with self.subTest(source=source.relative_to(repo), link=link):
                    self.assertTrue(target.is_file())
                    self.assertIn(unquote(url.fragment), page(target).ids)

    def test_raw_html_and_script_are_escaped(self):
        html = render("<script>alert(1)</script>\n\n<img src=x onerror=alert(1)>\n\ntext")
        self.assertNotIn("<script>", html)
        self.assertNotIn("<img src=x", html)
        self.assertIn("&lt;script&gt;", html)

    def test_dangerous_link_schemes_are_neutralised(self):
        html = render("[a](javascript:alert(1)) [b](data:text/html,x) ![c](vbscript:x) [ok](https://example.com) [rel](../x.md)")
        for bad in ("javascript:", "data:text", "vbscript:"):
            self.assertNotIn(bad, html)
        self.assertIn('href="https://example.com"', html)
        self.assertIn('href="../x.md"', html)

    def test_title_and_path_are_escaped(self):
        page = render_markdown_page("x", title="<b>", path='a"><script>', guide_url="/g").decode()
        self.assertNotIn("<script>", page)
        self.assertNotIn("<b>", page)
