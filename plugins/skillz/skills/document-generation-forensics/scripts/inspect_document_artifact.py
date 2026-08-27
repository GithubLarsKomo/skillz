#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

SUPPORTED_TEXT = {".txt", ".md", ".csv", ".tsv"}
SUPPORTED_OOXML = {".docx", ".xlsx", ".pptx"}
AI_MARKERS = (
    "openai", "chatgpt", "gpt-4", "gpt-5", "copilot",
    "claude", "anthropic", "gemini", "perplexity", "large language model", "llm",
)
PROGRAMMATIC_MARKERS = (
    "python-docx", "openpyxl", "python-pptx", "pandoc", "libreoffice",
    "reportlab", "wkhtmltopdf", "weasyprint", "apache poi", "docx4j",
)
CORE_NAMES = {
    "creator": "creator",
    "lastModifiedBy": "lastModifiedBy",
    "created": "created",
    "modified": "modified",
    "revision": "revision",
    "title": "title",
    "subject": "subject",
    "keywords": "keywords",
    "description": "description",
}
APP_NAMES = {
    "Application": "application",
    "AppVersion": "appVersion",
    "Company": "company",
    "Manager": "manager",
    "Template": "template",
    "TotalTime": "totalTime",
}


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _safe_xml(data: bytes):
    return ET.fromstring(data)


def _extract_simple_xml(data: bytes, wanted: dict[str, str]) -> dict[str, str]:
    out: dict[str, str] = {}
    root = _safe_xml(data)
    for elem in root.iter():
        local = _local(elem.tag)
        if local in wanted and elem.text is not None:
            value = elem.text.strip()
            if value:
                out[wanted[local]] = value
    return out


def _extract_custom_props(data: bytes) -> dict[str, str]:
    out: dict[str, str] = {}
    root = _safe_xml(data)
    for prop in root:
        name = prop.attrib.get("name")
        if not name:
            continue
        value = ""
        for child in prop:
            if child.text:
                value = child.text.strip()
                break
        out[name] = value
    return out


def _metadata_hints(metadata: dict[str, object]) -> list[dict[str, object]]:
    signals: list[dict[str, object]] = []
    for key, raw in metadata.items():
        if not isinstance(raw, str):
            continue
        lower = raw.lower()
        ai_hits = sorted({marker for marker in AI_MARKERS if marker in lower})
        tooling_hits = sorted({marker for marker in PROGRAMMATIC_MARKERS if marker in lower})
        if ai_hits:
            signals.append({
                "class": "explicit-provenance",
                "strength": "supporting",
                "llmSpecific": True,
                "source": f"metadata:{key}",
                "observed": raw,
                "interpretation": "Metadata names a GenAI/LLM-related tool or model; treat as provenance evidence that may be rewritten or forged.",
                "forgeability": "medium",
                "markers": ai_hits,
            })
        if tooling_hits:
            signals.append({
                "class": "generator-tooling",
                "strength": "context",
                "llmSpecific": False,
                "source": f"metadata:{key}",
                "observed": raw,
                "interpretation": "Metadata identifies programmatic document tooling; this does not establish LLM use.",
                "forgeability": "medium",
                "markers": tooling_hits,
            })
    return signals


def _number_signals(signals: list[dict[str, object]]) -> list[dict[str, object]]:
    return [{"id": f"S{i}", **signal} for i, signal in enumerate(signals, 1)]


def _analyze_text(path: Path) -> tuple[dict, dict, list, list]:
    limitations: list[str] = []
    raw = path.read_bytes()
    encoding = None
    text = None
    for candidate in ("utf-8-sig", "utf-8", "utf-16", "latin-1"):
        try:
            text = raw.decode(candidate)
            encoding = candidate
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        limitations.append("Text encoding could not be decoded with supported fallback encodings.")
        inventory = {"lineCount": None, "characterCount": None}
    else:
        inventory = {
            "lineCount": len(text.splitlines()),
            "characterCount": len(text),
            "nonEmptyLineCount": sum(1 for line in text.splitlines() if line.strip()),
        }
    return {"encoding": encoding}, inventory, [], limitations


def _zip_read(zf: zipfile.ZipFile, name: str) -> bytes | None:
    try:
        return zf.read(name)
    except KeyError:
        return None


def _count_tags(xml_bytes: bytes | None, local_name: str) -> int:
    if not xml_bytes:
        return 0
    try:
        root = _safe_xml(xml_bytes)
    except ET.ParseError:
        return 0
    return sum(1 for elem in root.iter() if _local(elem.tag) == local_name)


def _ooxml_metadata(zf: zipfile.ZipFile) -> tuple[dict, list[str]]:
    metadata: dict[str, object] = {}
    limitations: list[str] = []
    core = _zip_read(zf, "docProps/core.xml")
    app = _zip_read(zf, "docProps/app.xml")
    custom = _zip_read(zf, "docProps/custom.xml")
    try:
        if core:
            metadata.update(_extract_simple_xml(core, CORE_NAMES))
        if app:
            metadata.update(_extract_simple_xml(app, APP_NAMES))
        if custom:
            metadata["customProperties"] = _extract_custom_props(custom)
    except ET.ParseError as exc:
        limitations.append(f"OOXML metadata XML parsing failed: {exc}")
    return metadata, limitations


def _analyze_docx(zf: zipfile.ZipFile) -> tuple[dict, list[str]]:
    names = set(zf.namelist())
    document = _zip_read(zf, "word/document.xml")
    inventory = {
        "packageMemberCount": len(names),
        "paragraphCount": _count_tags(document, "p"),
        "tableCount": _count_tags(document, "tbl"),
        "insertedRevisionCount": _count_tags(document, "ins"),
        "deletedRevisionCount": _count_tags(document, "del"),
        "fieldCount": _count_tags(document, "fldSimple") + _count_tags(document, "instrText"),
        "commentFileCount": sum(1 for n in names if n.startswith("word/comments") and n.endswith(".xml")),
        "footnotesPresent": "word/footnotes.xml" in names,
        "endnotesPresent": "word/endnotes.xml" in names,
        "embeddedObjectCount": sum(1 for n in names if n.startswith("word/embeddings/") and not n.endswith("/")),
        "mediaCount": sum(1 for n in names if n.startswith("word/media/") and not n.endswith("/")),
    }
    limitations = []
    if document is None:
        limitations.append("word/document.xml is missing; DOCX body inventory is incomplete.")
    return inventory, limitations


def _analyze_xlsx(zf: zipfile.ZipFile) -> tuple[dict, list[str]]:
    names = set(zf.namelist())
    workbook = _zip_read(zf, "xl/workbook.xml")
    formula_count = 0
    for name in names:
        if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"):
            formula_count += _count_tags(_zip_read(zf, name), "f")
    hidden = 0
    defined_names = 0
    if workbook:
        try:
            root = _safe_xml(workbook)
            for elem in root.iter():
                if _local(elem.tag) == "sheet" and elem.attrib.get("state") in {"hidden", "veryHidden"}:
                    hidden += 1
                if _local(elem.tag) == "definedName":
                    defined_names += 1
        except ET.ParseError:
            pass
    inventory = {
        "packageMemberCount": len(names),
        "worksheetCount": sum(1 for n in names if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")),
        "hiddenWorksheetCount": hidden,
        "formulaCount": formula_count,
        "definedNameCount": defined_names,
        "commentFileCount": sum(1 for n in names if n.startswith("xl/comments") and n.endswith(".xml")),
        "threadedCommentFileCount": sum(1 for n in names if "threadedComments" in n and n.endswith(".xml")),
        "externalLinkCount": sum(1 for n in names if n.startswith("xl/externalLinks/externalLink") and n.endswith(".xml")),
        "calcChainPresent": "xl/calcChain.xml" in names,
        "macroProjectPresent": any(n.endswith("vbaProject.bin") for n in names),
        "sharedStringsPresent": "xl/sharedStrings.xml" in names,
    }
    return inventory, []


def _analyze_pptx(zf: zipfile.ZipFile) -> tuple[dict, list[str]]:
    names = set(zf.namelist())
    table_count = 0
    for name in names:
        if name.startswith("ppt/slides/slide") and name.endswith(".xml"):
            table_count += _count_tags(_zip_read(zf, name), "tbl")
    inventory = {
        "packageMemberCount": len(names),
        "slideCount": sum(1 for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
        "notesSlideCount": sum(1 for n in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)),
        "commentFileCount": sum(1 for n in names if n.startswith("ppt/comments/") and n.endswith(".xml")),
        "slideMasterCount": sum(1 for n in names if re.fullmatch(r"ppt/slideMasters/slideMaster\d+\.xml", n)),
        "slideLayoutCount": sum(1 for n in names if re.fullmatch(r"ppt/slideLayouts/slideLayout\d+\.xml", n)),
        "mediaCount": sum(1 for n in names if n.startswith("ppt/media/") and not n.endswith("/")),
        "chartCount": sum(1 for n in names if n.startswith("ppt/charts/chart") and n.endswith(".xml")),
        "tableCount": table_count,
        "embeddedObjectCount": sum(1 for n in names if n.startswith("ppt/embeddings/") and not n.endswith("/")),
    }
    return inventory, []


def _analyze_ooxml(path: Path, fmt: str) -> tuple[dict, dict, list, list]:
    limitations: list[str] = []
    signals: list[dict[str, object]] = []
    try:
        with zipfile.ZipFile(path) as zf:
            metadata, meta_limits = _ooxml_metadata(zf)
            limitations.extend(meta_limits)
            if fmt == "docx":
                inventory, limits = _analyze_docx(zf)
            elif fmt == "xlsx":
                inventory, limits = _analyze_xlsx(zf)
            else:
                inventory, limits = _analyze_pptx(zf)
            limitations.extend(limits)
    except (zipfile.BadZipFile, OSError) as exc:
        return {}, {}, [], [f"OOXML package could not be parsed: {exc}"]

    signals.extend(_metadata_hints({k: v for k, v in metadata.items() if isinstance(v, str)}))
    application = metadata.get("application")
    if isinstance(application, str) and application.strip():
        signals.append({
            "class": "generator-tooling",
            "strength": "context",
            "llmSpecific": False,
            "source": "docProps/app.xml:Application",
            "observed": application,
            "interpretation": "Identifies the application recorded by the OOXML package; not evidence of LLM authorship.",
            "forgeability": "medium",
        })
    if inventory.get("insertedRevisionCount", 0) or inventory.get("deletedRevisionCount", 0):
        signals.append({
            "class": "revision-workflow",
            "strength": "context",
            "llmSpecific": False,
            "source": "word/document.xml",
            "observed": {
                "inserted": inventory.get("insertedRevisionCount", 0),
                "deleted": inventory.get("deletedRevisionCount", 0),
            },
            "interpretation": "Track Changes records editing activity but does not identify whether edits were human- or LLM-produced.",
            "forgeability": "medium",
        })
    return metadata, inventory, signals, limitations


def _decode_pdf_literal(value: bytes) -> str:
    text = value.decode("latin-1", errors="replace")
    text = text.replace(r"\(", "(").replace(r"\)", ")").replace(r"\\", "\\")
    return text.strip()


def _pdf_literal(raw: bytes, key: str) -> str | None:
    match = re.search(rb"/" + re.escape(key.encode()) + rb"\s*\((.*?)\)", raw, flags=re.S)
    return _decode_pdf_literal(match.group(1)) if match else None


def _pdf_xmp_value(text: str, tag: str) -> str | None:
    match = re.search(rf"<{re.escape(tag)}[^>]*>(.*?)</{re.escape(tag)}>", text, flags=re.I | re.S)
    if not match:
        return None
    value = re.sub(r"<[^>]+>", " ", match.group(1))
    value = re.sub(r"\s+", " ", value).strip()
    return value or None


def _analyze_pdf(path: Path) -> tuple[dict, dict, list, list]:
    raw = path.read_bytes()
    text = raw.decode("latin-1", errors="ignore")
    metadata: dict[str, object] = {}
    for key, out_key in (
        ("Author", "author"), ("Creator", "creator"), ("Producer", "producer"),
        ("CreationDate", "creationDate"), ("ModDate", "modDate"),
    ):
        value = _pdf_literal(raw, key)
        if value:
            metadata[out_key] = value
    for tag, out_key in (
        ("xmp:CreatorTool", "xmpCreatorTool"),
        ("pdf:Producer", "xmpProducer"),
        ("xmp:CreateDate", "xmpCreateDate"),
        ("xmp:ModifyDate", "xmpModifyDate"),
    ):
        value = _pdf_xmp_value(text, tag)
        if value and out_key not in metadata:
            metadata[out_key] = value

    inventory = {
        "pageIndicatorCount": len(re.findall(rb"/Type\s*/Page\b", raw)),
        "encrypted": b"/Encrypt" in raw,
        "embeddedFileIndicatorCount": len(re.findall(rb"/Type\s*/EmbeddedFile\b", raw)),
        "xmpPresent": "<x:xmpmeta" in text.lower() or "<rdf:rdf" in text.lower(),
    }
    limitations = [
        "PDF parsing is best-effort and does not replace a full PDF parser; object streams or incremental updates can hide metadata from this scan."
    ]
    signals = _metadata_hints({k: v for k, v in metadata.items() if isinstance(v, str)})
    for key in ("creator", "producer", "xmpCreatorTool", "xmpProducer"):
        value = metadata.get(key)
        if isinstance(value, str) and value.strip():
            signals.append({
                "class": "generator-tooling",
                "strength": "context",
                "llmSpecific": False,
                "source": f"pdf:{key}",
                "observed": value,
                "interpretation": "Identifies PDF creation tooling when accurate; it does not by itself identify the content author or prove LLM use.",
                "forgeability": "medium",
            })
    if inventory["encrypted"]:
        limitations.append("PDF is marked as encrypted; content/provenance inspection may be incomplete.")
    return metadata, inventory, signals, limitations


def inspect_path(path: Path) -> dict:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(path)
    suffix = path.suffix.lower()
    if suffix in SUPPORTED_TEXT:
        fmt = suffix.lstrip(".")
        metadata, inventory, signals, limitations = _analyze_text(path)
    elif suffix in SUPPORTED_OOXML:
        fmt = suffix.lstrip(".")
        metadata, inventory, signals, limitations = _analyze_ooxml(path, fmt)
    elif suffix == ".pdf":
        fmt = "pdf"
        metadata, inventory, signals, limitations = _analyze_pdf(path)
    else:
        raise ValueError(f"unsupported format: {suffix or '<none>'}")
    return {
        "schemaVersion": 1,
        "artifact": {
            "path": str(path),
            "format": fmt,
            "sha256": _sha256(path),
            "sizeBytes": path.stat().st_size,
        },
        "metadata": metadata,
        "inventory": inventory,
        "signals": _number_signals(signals),
        "limitations": limitations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect TXT/MD/CSV/TSV, DOCX, XLSX, PPTX and PDF artifacts for reproducible provenance and structure facts."
    )
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    try:
        result = inspect_path(args.artifact)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.artifact}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"ERROR: could not inspect artifact: {exc}", file=sys.stderr)
        return 3
    if args.pretty:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False))
    else:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
