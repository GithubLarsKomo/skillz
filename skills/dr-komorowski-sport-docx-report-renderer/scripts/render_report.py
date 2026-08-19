#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any, Iterable

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
CORE_PATH = HERE / "_render_report_core.py"

_spec = importlib.util.spec_from_file_location("dk_sport_render_core", CORE_PATH)
if _spec is None or _spec.loader is None:
    raise SystemExit(f"ERROR: cannot load renderer core: {CORE_PATH}")
core = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(core)

METADATA_TOKENS = {"{{DOCUMENT_TYPE}}", "{{DOCUMENT_ID}}", "{{DATE}}", "{{CONFIDENTIALITY}}"}
REPORT_BODY_TOKEN = "{{REPORT_BODY}}"
TOKENS = METADATA_TOKENS | {REPORT_BODY_TOKEN}


def document_parts(doc) -> Iterable:
    yield doc
    for section in doc.sections:
        yield section.header
        yield section.footer


def _replace_in_paragraph(paragraph, token: str, value: str) -> None:
    if token not in paragraph.text:
        return
    text = paragraph.text.replace(token, value)
    if paragraph.runs:
        paragraph.runs[0].text = text
        for run in paragraph.runs[1:]:
            run.text = ""
    else:
        paragraph.add_run(text)


def replace_tokens(doc, meta: dict[str, Any]) -> None:
    counts = {token: 0 for token in METADATA_TOKENS}
    for part in document_parts(doc):
        for paragraph in core.paragraphs(part):
            for token in METADATA_TOKENS:
                if token in paragraph.text:
                    counts[token] += 1
    missing = [token for token, count in counts.items() if not count]
    if missing:
        raise ValueError("template missing required token(s): " + ", ".join(sorted(missing)))

    values = {
        "{{DOCUMENT_TYPE}}": str(meta.get("document_type", "")),
        "{{DOCUMENT_ID}}": str(meta.get("document_id", "")),
        "{{DATE}}": str(meta.get("date", "")),
        "{{CONFIDENTIALITY}}": str(meta.get("confidentiality", "Vertraulich")),
    }
    for part in document_parts(doc):
        for paragraph in core.paragraphs(part):
            for token, value in values.items():
                _replace_in_paragraph(paragraph, token, value)

    unresolved = sorted(
        token
        for token in METADATA_TOKENS
        if any(token in paragraph.text for part in document_parts(doc) for paragraph in core.paragraphs(part))
    )
    if unresolved:
        raise ValueError("template left unresolved token(s): " + ", ".join(unresolved))


def marker(doc):
    top_level = [paragraph for paragraph in doc.paragraphs if REPORT_BODY_TOKEN in paragraph.text]
    total = sum(
        1
        for part in document_parts(doc)
        for paragraph in core.paragraphs(part)
        if REPORT_BODY_TOKEN in paragraph.text
    )
    if len(top_level) != 1 or total != 1:
        raise ValueError(
            "template requires exactly one top-level {{REPORT_BODY}} paragraph and no nested copies"
        )
    return top_level[0]


core.replace_tokens = replace_tokens
core.marker = marker

render = core.render
load_json = core.load_json
validate = core.validate
load_template = core.load_template


def main() -> int:
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
