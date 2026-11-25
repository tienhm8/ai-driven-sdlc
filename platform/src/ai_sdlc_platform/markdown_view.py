"""Render repository Markdown as a standalone, script-free HTML page."""
from html import escape, unescape
import re
from unicodedata import category

import markdown
from markdown.extensions import Extension
from markdown.extensions.toc import HTML_PLACEHOLDER_RE, stashedHTML2text
from markdown.treeprocessors import Treeprocessor

SAFE_SCHEMES = {"http", "https", "mailto"}
SCHEME = re.compile(r"^([A-Za-z][A-Za-z0-9+.-]*):")

PAGE = """<!doctype html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root{{--bg:#f7f8fa;--fg:#1c2330;--muted:#5d6878;--card:#fff;--line:#d9dee6;--accent:#1f6feb;--chip:#eef1f6}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0f141b;--fg:#e6eaf0;--muted:#99a3b3;--card:#171e28;--line:#2b3442;--accent:#6aa6ff;--chip:#222c3a}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:16px}}
article{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px 20px 16px;overflow-wrap:anywhere}}
a{{color:var(--accent)}}
nav{{margin:4px 0 12px;font-size:14px}}
h1,h2,h3{{line-height:1.3}}
/* Keep whole words in the minimum column width; scroll wide tables locally. */
table{{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;overflow-wrap:break-word}}
th,td{{border:1px solid var(--line);padding:5px 9px;vertical-align:top;text-align:left}}
th{{background:var(--chip)}}
code{{background:var(--chip);padding:1px 5px;border-radius:4px;font-size:13px}}
pre{{background:var(--chip);padding:10px 12px;border-radius:6px;overflow-x:auto}}
pre code{{background:none;padding:0}}
blockquote{{margin:8px 0;padding:2px 12px;border-left:3px solid var(--line);color:var(--muted)}}
img{{max-width:100%;height:auto}}
hr{{border:0;border-top:1px solid var(--line)}}
</style></head><body><main>
<nav><a href="{guide}">&larr; Quay lại guide</a> &middot; <span>{path}</span></nav>
<article>
{body}
</article></main></body></html>
"""


class _NoRawHtml(Extension):
    """Treat raw HTML in source as text so it is escaped, not rendered."""

    def extendMarkdown(self, md):
        md.preprocessors.deregister("html_block")
        md.inlinePatterns.deregister("html")


class _SafeLinks(Treeprocessor):
    def run(self, root):
        for element in root.iter():
            for attribute in ("href", "src"):
                value = element.get(attribute)
                match = SCHEME.match(value.strip()) if value else None
                if match and match.group(1).lower() not in SAFE_SCHEMES:
                    element.set(attribute, "#")


class _SafeLinksExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(_SafeLinks(md), "safe_links", 5)


def _heading_slug(text: str) -> str:
    # Preserve literal hyphens and one hyphen per space, even when punctuation
    # between two spaces is removed (e.g. "A — B" becomes "a--b").
    return "".join(
        "-" if char == " " else char
        for char in text.lower()
        if char in " -_" or category(char)[0] in "LMN"
    )

def _heading_text(element, md) -> str:
    def decode_stashed(text):
        return HTML_PLACEHOLDER_RE.sub(
            lambda match: unescape(stashedHTML2text(match.group(), md, strip_entities=False)),
            text,
        )

    if element.tag == "code":
        # Markdown escapes code text before serialization; undo only that layer.
        return unescape(element.text or "")
    return (decode_stashed(element.text or "") + "".join(
        _heading_text(child, md) + decode_stashed(child.tail or "") for child in element
    ))

class _HeadingIds(Treeprocessor):
    def run(self, root):
        used = set()
        suffixes = {}
        for heading in root.iter():
            if heading.tag not in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                continue
            base = _heading_slug(_heading_text(heading, self.md).strip())
            if not base:
                continue
            slug = base
            suffix = suffixes.get(base, 0)
            while slug in used:
                suffix += 1
                slug = f"{base}-{suffix}"
            suffixes[base] = suffix
            used.add(slug)
            heading.set("id", slug)

class _HeadingIdsExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(_HeadingIds(md), "heading_ids", -1)

def render_markdown_page(text: str, *, title: str, path: str, guide_url: str) -> bytes:
    body = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", _HeadingIdsExtension(),
                          _NoRawHtml(), _SafeLinksExtension()])
    return PAGE.format(title=escape(title), path=escape(path), guide=escape(guide_url, quote=True),
                       body=body).encode("utf-8")
