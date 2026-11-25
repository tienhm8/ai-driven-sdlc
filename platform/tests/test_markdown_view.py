from unittest import TestCase

from ai_sdlc_platform.markdown_view import render_markdown_page


def render(text):
    return render_markdown_page(text, title="t.md", path="framework/t.md", guide_url="/framework/guide/index.html").decode()


class MarkdownViewTests(TestCase):
    def test_renders_tables_code_lists_and_links(self):
        html = render("# Tiêu đề\\n\\n| A | B |\\n|---|---|\\n| 1 | 2 |\\n\\n```text\\nx\\n```\\n\\n- [ ] việc\\n\\n[liên kết](other.md)\\n".replace("\\n", "\n"))
        for fragment in ("<h1>Tiêu đề</h1>", "<table>", "<td>1</td>", "<pre><code", "<li>", 'href="other.md"'):
            self.assertIn(fragment, html)
        self.assertIn("Quay lại guide", html)

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
