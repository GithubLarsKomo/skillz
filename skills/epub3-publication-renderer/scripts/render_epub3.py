#!/usr/bin/env python3
"""Render conservative, reflowable EPUB3 from a chaptered Markdown manuscript.

This renderer is content-neutral. It preserves wording and only projects
Markdown structure into EPUB XHTML/navigation.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import uuid
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def parse_markdown(text: str):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    title = None
    subtitle = None
    chapters = []
    current_title = None
    current_lines = []

    for line in lines:
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
            continue
        if (
            line.startswith("## ")
            and title is not None
            and subtitle is None
            and current_title is None
            and not chapters
        ):
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
        raise ValueError("Markdown must start with '# <book title>'.")
    if not chapters:
        raise ValueError("Markdown must contain at least one chapter as a subsequent level-1 heading.")

    normalized = []
    for chapter_title, body_lines in chapters:
        body = "\n".join(body_lines).strip()
        if not chapter_title or not body:
            raise ValueError(f"Empty chapter detected: {chapter_title!r}")
        normalized.append((chapter_title, body))
    return title, subtitle, normalized


def inline_markup(text: str) -> str:
    value = html.escape(text, quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", value)
    return value


def markdown_body_to_xhtml(text: str) -> str:
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    out = []
    for block in blocks:
        if block in {"---", "* * *", "***"}:
            out.append('<hr class="scene-break"/>')
            continue
        if block.startswith("### "):
            out.append(f"<h3>{inline_markup(block[4:].strip())}</h3>")
            continue
        if block.startswith("## "):
            out.append(f"<h2>{inline_markup(block[3:].strip())}</h2>")
            continue

        lines = block.splitlines()
        if lines and all(line.lstrip().startswith("- ") for line in lines):
            items = "".join(
                f"<li>{inline_markup(line.lstrip()[2:].strip())}</li>" for line in lines
            )
            out.append(f"<ul>{items}</ul>")
            continue

        if lines and all(line.lstrip().startswith(">") for line in lines):
            quote = " ".join(line.lstrip()[1:].strip() for line in lines)
            out.append(f"<blockquote><p>{inline_markup(quote)}</p></blockquote>")
            continue

        paragraph = " ".join(line.strip() for line in lines)
        out.append(f"<p>{inline_markup(paragraph)}</p>")
    return "\n".join(out)


def build_uid(title: str, author: str, language: str, raw: str) -> str:
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    return f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, title + '|' + author + '|' + language + '|' + digest)}"


def validate_epub(path: Path, chapter_count: int) -> dict:
    result = {
        "schemaVersion": 1,
        "mimetypeFirst": False,
        "mimetypeStored": False,
        "requiredFilesPresent": False,
        "xmlParsePass": False,
        "navigationPresent": False,
        "ncxPresent": False,
        "chapterCount": chapter_count,
        "javascriptFree": True,
        "structuralStatus": "fail",
        "elevenReaderCompatibility": "not-assessed",
        "limitations": [
            "Structural EPUB validation only; no live ElevenReader import or rendered voice assessment was performed."
        ],
    }
    with zipfile.ZipFile(path, "r") as zf:
        infos = zf.infolist()
        names = [i.filename for i in infos]
        result["mimetypeFirst"] = bool(names) and names[0] == "mimetype"
        if infos:
            result["mimetypeStored"] = (
                infos[0].filename == "mimetype" and infos[0].compress_type == zipfile.ZIP_STORED
            )
        if "mimetype" not in names or zf.read("mimetype") != b"application/epub+zip":
            return result

        required = {
            "META-INF/container.xml",
            "OEBPS/content.opf",
            "OEBPS/nav.xhtml",
            "OEBPS/toc.ncx",
        }
        result["requiredFilesPresent"] = required.issubset(names)
        result["navigationPresent"] = "OEBPS/nav.xhtml" in names
        result["ncxPresent"] = "OEBPS/toc.ncx" in names

        xml_names = [
            n for n in names
            if n.endswith((".xml", ".opf", ".xhtml", ".ncx"))
        ]
        try:
            for name in xml_names:
                ET.fromstring(zf.read(name))
            result["xmlParsePass"] = True
        except ET.ParseError:
            result["xmlParsePass"] = False

        for name in names:
            if name.endswith(".xhtml") and b"<script" in zf.read(name).lower():
                result["javascriptFree"] = False

    checks = [
        result["mimetypeFirst"],
        result["mimetypeStored"],
        result["requiredFilesPresent"],
        result["xmlParsePass"],
        result["navigationPresent"],
        result["ncxPresent"],
        result["javascriptFree"],
        chapter_count > 0,
    ]
    if all(checks):
        result["structuralStatus"] = "pass"
        result["elevenReaderCompatibility"] = "structural-pass"
    return result


def render_epub(source: Path, output: Path, validation_output: Path, author: str, language: str) -> None:
    raw = source.read_text(encoding="utf-8")
    title, subtitle, chapters = parse_markdown(raw)
    uid = build_uid(title, author, language, raw)
    modified = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    css = """
body { font-family: serif; line-height: 1.55; margin: 5%; }
h1 { font-size: 1.65em; margin-top: 0; }
h2 { font-size: 1.2em; margin-top: 1.5em; }
h3 { font-size: 1.05em; margin-top: 1.3em; }
p { margin: 0 0 0.9em 0; }
blockquote { margin: 1em 1.5em; }
li { margin-bottom: 0.35em; }
.titlepage { text-align: center; margin-top: 20%; }
.subtitle { font-size: 1.15em; }
.scene-break { border: 0; text-align: center; margin: 1.4em 0; }
.scene-break:after { content: "* * *"; }
"""

    output.parent.mkdir(parents=True, exist_ok=True)
    validation_output.parent.mkdir(parents=True, exist_ok=True)

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

        subtitle_html = f'<p class="subtitle">{inline_markup(subtitle)}</p>' if subtitle else ""
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
            cid = f"ch{index:03d}"
            filename = f"chapter_{index:03d}.xhtml"
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
<head><title>Contents</title><link rel="stylesheet" href="style.css" type="text/css"/></head>
<body><nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{''.join(nav_items)}</ol></nav></body></html>""",
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

    validation = validate_epub(output, len(chapters))
    validation_output.write_text(json.dumps(validation, indent=2), encoding="utf-8")
    if validation["structuralStatus"] != "pass":
        raise ValueError(f"EPUB structural validation failed: {validation}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a chaptered EPUB3 publication from Markdown.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    parser.add_argument("--author", default="Unknown Author")
    parser.add_argument("--language", default="en")
    args = parser.parse_args()
    render_epub(args.input, args.output, args.validation_output, args.author, args.language)


if __name__ == "__main__":
    main()
