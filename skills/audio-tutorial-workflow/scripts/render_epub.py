#!/usr/bin/env python3
"""Render a chaptered EPUB3 from a simple Markdown tutorial.

The renderer is deliberately content-neutral: it does not rewrite text.
Level-1 headings after the book title become EPUB chapters.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import uuid
import zipfile
from pathlib import Path


def parse_markdown(text: str) -> tuple[str, str | None, list[tuple[str, str]]]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    title = None
    subtitle = None
    chapters: list[tuple[str, list[str]]] = []
    current_title = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
            continue
        if line.startswith("## ") and title is not None and subtitle is None and not chapters and current_title is None:
            subtitle = line[3:].strip()
            continue
        if line.startswith("# "):
            if current_title is not None:
                chapters.append((current_title, current_lines))
            current_title = line[2:].strip()
            current_lines = []
            continue
        if current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        chapters.append((current_title, current_lines))

    if not title:
        raise ValueError("Markdown must start with a level-1 book title.")
    if not chapters:
        raise ValueError("Markdown must contain at least one level-1 chapter heading after the title.")

    normalized = []
    for chapter_title, body_lines in chapters:
        body = "\n".join(body_lines).strip()
        if not chapter_title or not body:
            raise ValueError(f"Empty chapter detected: {chapter_title!r}")
        normalized.append((chapter_title, body))
    return title, subtitle, normalized


def markdown_body_to_xhtml(text: str) -> str:
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    out: list[str] = []
    for block in blocks:
        if block.startswith("## "):
            out.append(f"<h2>{html.escape(block[3:].strip())}</h2>")
            continue
        if block.startswith("### "):
            out.append(f"<h3>{html.escape(block[4:].strip())}</h3>")
            continue
        if all(line.lstrip().startswith("- ") for line in block.splitlines()):
            items = "".join(
                f"<li>{html.escape(line.lstrip()[2:].strip())}</li>"
                for line in block.splitlines()
            )
            out.append(f"<ul>{items}</ul>")
            continue
        paragraph = " ".join(line.strip() for line in block.splitlines())
        paragraph = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html.escape(paragraph))
        out.append(f"<p>{paragraph}</p>")
    return "\n".join(out)


def render_epub(source: Path, output: Path, author: str, language: str) -> None:
    raw = source.read_text(encoding="utf-8")
    title, subtitle, chapters = parse_markdown(raw)
    uid = f"urn:uuid:{uuid.uuid4()}"
    modified = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    css = """
body { font-family: serif; line-height: 1.55; margin: 5%; }
h1 { font-size: 1.65em; margin-top: 0; }
h2 { font-size: 1.2em; margin-top: 1.5em; }
h3 { font-size: 1.05em; margin-top: 1.3em; }
p { margin: 0 0 0.9em 0; }
li { margin-bottom: 0.45em; }
.titlepage { text-align: center; margin-top: 20%; }
.subtitle { font-size: 1.15em; }
"""

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr(
            "META-INF/container.xml",
            """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""",
        )
        zf.writestr("OEBPS/style.css", css)

        subtitle_html = f'<p class="subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
        title_page = f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{html.escape(language)}">
<head><title>{html.escape(title)}</title><link rel="stylesheet" href="style.css" type="text/css"/></head>
<body><section class="titlepage"><h1>{html.escape(title)}</h1>{subtitle_html}<p>{html.escape(author)}</p></section></body>
</html>"""
        zf.writestr("OEBPS/title.xhtml", title_page)

        manifest = [
            '<item id="css" href="style.css" media-type="text/css"/>',
            '<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>',
            '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        ]
        spine = ['<itemref idref="title"/>']
        nav_items = []
        ncx_items = []

        for index, (chapter_title, body) in enumerate(chapters, start=1):
            cid = f"ch{index:02d}"
            filename = f"chapter_{index:02d}.xhtml"
            xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{html.escape(language)}">
<head><title>{html.escape(chapter_title)}</title><link rel="stylesheet" href="style.css" type="text/css"/></head>
<body><section epub:type="chapter" id="{cid}"><h1>{html.escape(chapter_title)}</h1>
{markdown_body_to_xhtml(body)}
</section></body></html>"""
            zf.writestr(f"OEBPS/{filename}", xhtml)
            manifest.append(f'<item id="{cid}" href="{filename}" media-type="application/xhtml+xml"/>')
            spine.append(f'<itemref idref="{cid}"/>')
            nav_items.append(f'<li><a href="{filename}">{html.escape(chapter_title)}</a></li>')
            ncx_items.append(
                f'<navPoint id="navPoint-{index}" playOrder="{index}">'
                f'<navLabel><text>{html.escape(chapter_title)}</text></navLabel>'
                f'<content src="{filename}"/></navPoint>'
            )

        zf.writestr(
            "OEBPS/nav.xhtml",
            f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{html.escape(language)}">
<head><title>Inhaltsverzeichnis</title><link rel="stylesheet" href="style.css" type="text/css"/></head>
<body><nav epub:type="toc" id="toc"><h1>Inhaltsverzeichnis</h1><ol>{''.join(nav_items)}</ol></nav></body></html>""",
        )
        zf.writestr(
            "OEBPS/toc.ncx",
            f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{uid}"/></head>
<docTitle><text>{html.escape(title)}</text></docTitle>
<navMap>{''.join(ncx_items)}</navMap>
</ncx>""",
        )

        opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{html.escape(language)}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{uid}</dc:identifier>
<dc:title>{html.escape(title)}</dc:title>
<dc:language>{html.escape(language)}</dc:language>
<dc:creator>{html.escape(author)}</dc:creator>
<meta property="dcterms:modified">{modified}</meta>
</metadata>
<manifest>{''.join(manifest)}</manifest>
<spine toc="ncx">{''.join(spine)}</spine>
</package>"""
        zf.writestr("OEBPS/content.opf", opf)

    validate_epub(output)


def validate_epub(path: Path) -> None:
    with zipfile.ZipFile(path, "r") as zf:
        names = zf.namelist()
        if not names or names[0] != "mimetype":
            raise ValueError("EPUB mimetype must be the first ZIP entry.")
        if zf.read("mimetype") != b"application/epub+zip":
            raise ValueError("Invalid EPUB mimetype.")
        required = {"META-INF/container.xml", "OEBPS/content.opf", "OEBPS/nav.xhtml", "OEBPS/toc.ncx"}
        missing = required.difference(names)
        if missing:
            raise ValueError(f"Missing EPUB files: {sorted(missing)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a chaptered EPUB3 from Markdown.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--author", default="ChatGPT Tutorial")
    parser.add_argument("--language", default="de")
    args = parser.parse_args()
    render_epub(args.input, args.output, args.author, args.language)


if __name__ == "__main__":
    main()
