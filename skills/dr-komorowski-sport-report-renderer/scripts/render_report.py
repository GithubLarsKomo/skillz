#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.platypus import Flowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
except ImportError as exc:
    raise SystemExit("ERROR: reportlab is required (pip install reportlab)") from exc

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
DEFAULT_THEME = SKILL_ROOT / "assets" / "report-theme.json"


def hexcolor(value: str) -> colors.Color:
    return colors.HexColor(value)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"top-level JSON must be an object: {path}")
    return data


def _fc_match(family: str) -> str | None:
    try:
        proc = subprocess.run(
            ["fc-match", "-f", "%{file}\n", family],
            capture_output=True,
            text=True,
            timeout=3,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    candidate = proc.stdout.strip().splitlines()[0] if proc.stdout.strip() else ""
    return candidate if candidate and Path(candidate).is_file() else None


def register_fonts() -> tuple[str, str]:
    regular_candidates = [
        _fc_match("DejaVu Sans"),
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/DejaVuSans.ttf",
    ]
    bold_candidates = [
        _fc_match("DejaVu Sans:style=Bold"),
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/DejaVuSans-Bold.ttf",
    ]
    regular = next((p for p in regular_candidates if p and Path(p).is_file()), None)
    bold = next((p for p in bold_candidates if p and Path(p).is_file()), None)
    if regular and bold:
        pdfmetrics.registerFont(TTFont("DrKRegular", regular))
        pdfmetrics.registerFont(TTFont("DrKBold", bold))
        return "DrKRegular", "DrKBold"
    return "Helvetica", "Helvetica-Bold"


class LogoFlowable(Flowable):
    """Vector rendition of the established DK mark and wordmark."""

    def __init__(self, width: float = 68 * mm, height: float = 15 * mm, theme: dict[str, Any] | None = None):
        super().__init__()
        self.width = width
        self.height = height
        self.theme = theme or {}

    def draw(self) -> None:
        c = self.canv
        navy = hexcolor(self.theme["colors"]["navy"])
        teal = hexcolor(self.theme["colors"]["teal"])
        teal_text = hexcolor(self.theme["colors"]["teal_text"])
        _, bold = self.theme["_fonts"]
        box = 12 * mm
        y0 = 1 * mm
        c.setStrokeColor(navy)
        c.setLineWidth(1.4)
        c.roundRect(0, y0, box, box, 2 * mm, stroke=1, fill=0)
        c.setFillColor(navy)
        c.setFont(bold, 18)
        c.drawString(2.1 * mm, y0 + 3.2 * mm, "DK")
        x = box + 1.2 * mm
        c.setStrokeColor(teal)
        c.setLineWidth(2.0)
        for y_mm, length_mm in ((10.0, 7.0), (7.5, 9.5), (5.0, 5.7)):
            c.line(x, y0 + y_mm * mm, x + length_mm * mm, y0 + y_mm * mm)
        text_x = x + 11 * mm
        c.setFillColor(navy)
        c.setFont(bold, 8.8)
        c.drawString(text_x, y0 + 8.2 * mm, "DR. KOMOROWSKI")
        c.setFillColor(teal_text)
        c.setFont(bold, 6.4)
        c.drawString(text_x, y0 + 4.0 * mm, "DIAGNOSE & TRAINING")


def validate_spec(spec: dict[str, Any]) -> None:
    if not isinstance(spec.get("metadata"), dict):
        raise ValueError("metadata object is required")
    metadata = spec["metadata"]
    for key in ("title", "date", "header_right", "footer_left"):
        if not isinstance(metadata.get(key), str) or not metadata[key].strip():
            raise ValueError(f"metadata.{key} is required and must be a non-empty string")
    if "cover" in spec and not isinstance(spec["cover"], dict):
        raise ValueError("cover must be an object")
    sections = spec.get("sections", [])
    if not isinstance(sections, list):
        raise ValueError("sections must be an array")
    allowed = {"heading", "subheading", "paragraph", "bullets", "table", "callout", "spacer", "pagebreak"}
    for sidx, section in enumerate(sections):
        if not isinstance(section, dict):
            raise ValueError(f"sections[{sidx}] must be an object")
        blocks = section.get("blocks", [])
        if not isinstance(blocks, list):
            raise ValueError(f"sections[{sidx}].blocks must be an array")
        for bidx, block in enumerate(blocks):
            if not isinstance(block, dict):
                raise ValueError(f"sections[{sidx}].blocks[{bidx}] must be an object")
            btype = block.get("type")
            if btype not in allowed:
                raise ValueError(f"unsupported block type at sections[{sidx}].blocks[{bidx}]: {btype!r}")
            if btype == "table" and (
                not isinstance(block.get("columns"), list) or not isinstance(block.get("rows"), list)
            ):
                raise ValueError(f"table at sections[{sidx}].blocks[{bidx}] requires columns and rows arrays")


def build_styles(theme: dict[str, Any], regular: str, bold: str) -> dict[str, ParagraphStyle]:
    c = theme["colors"]
    styles = getSampleStyleSheet()
    return {
        "body": ParagraphStyle("Body", parent=styles["BodyText"], fontName=regular, fontSize=9.2, leading=12.6,
                               textColor=hexcolor(c["body"]), spaceAfter=3 * mm),
        "h1": ParagraphStyle("H1", parent=styles["Heading1"], fontName=bold, fontSize=19, leading=23,
                             textColor=hexcolor(c["navy"]), spaceBefore=4 * mm, spaceAfter=3 * mm),
        "h2": ParagraphStyle("H2", parent=styles["Heading2"], fontName=bold, fontSize=13.5, leading=16.5,
                             textColor=hexcolor(c["teal_text"]), spaceBefore=2.5 * mm, spaceAfter=2 * mm),
        "cover_brand": ParagraphStyle("CoverBrand", parent=styles["Heading1"], fontName=bold, fontSize=27, leading=31,
                                      textColor=hexcolor(c["navy"]), spaceAfter=6 * mm),
        "cover_title": ParagraphStyle("CoverTitle", parent=styles["Heading1"], fontName=bold, fontSize=22, leading=26,
                                      textColor=hexcolor(c["dark"]), spaceAfter=2 * mm),
        "cover_subtitle": ParagraphStyle("CoverSubtitle", parent=styles["BodyText"], fontName=regular, fontSize=13.5,
                                         leading=17, textColor=hexcolor(c["teal_text"]), spaceAfter=7 * mm),
        "eyebrow": ParagraphStyle("Eyebrow", parent=styles["BodyText"], fontName=bold, fontSize=10.5, leading=13,
                                  textColor=hexcolor(c["teal"]), spaceAfter=2 * mm),
        "table": ParagraphStyle("Table", parent=styles["BodyText"], fontName=regular, fontSize=7.8, leading=10.1,
                                textColor=hexcolor(c["body"])),
        "table_bold": ParagraphStyle("TableBold", parent=styles["BodyText"], fontName=bold, fontSize=7.8, leading=10.1,
                                     textColor=hexcolor(c["body"])),
        "callout_title": ParagraphStyle("CalloutTitle", parent=styles["BodyText"], fontName=bold, fontSize=10.2,
                                        leading=12.8, textColor=hexcolor(c["teal_text"]), spaceAfter=1.5 * mm),
        "callout_body": ParagraphStyle("CalloutBody", parent=styles["BodyText"], fontName=regular, fontSize=9.2,
                                       leading=12.6, textColor=hexcolor(c["body"])),
        "bullet": ParagraphStyle("Bullet", parent=styles["BodyText"], fontName=regular, fontSize=9.1, leading=12.4,
                                 textColor=hexcolor(c["body"]), leftIndent=5 * mm, firstLineIndent=-3 * mm,
                                 bulletIndent=1.5 * mm, spaceAfter=1.2 * mm),
    }


def escape_text(value: Any) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ptext(value: Any, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape_text(value), style)


def make_table(block: dict[str, Any], width: float, st: dict[str, ParagraphStyle], theme: dict[str, Any]) -> Table:
    columns = block["columns"]
    rows = block["rows"]
    ncols = len(columns)
    if ncols < 1:
        raise ValueError("table must have at least one column")
    for ridx, row in enumerate(rows):
        if not isinstance(row, list) or len(row) != ncols:
            raise ValueError(f"table row {ridx} must have {ncols} cells")
    widths = block.get("widths")
    if widths is not None:
        if not isinstance(widths, list) or len(widths) != ncols:
            raise ValueError("table widths must match column count")
        total = sum(float(x) for x in widths)
        if total <= 0:
            raise ValueError("table widths must sum to a positive value")
        col_widths = [width * float(x) / total for x in widths]
    else:
        col_widths = [width / ncols] * ncols
    data = [[ptext(cell, st["table_bold"]) for cell in columns]]
    data.extend([[ptext(cell, st["table"]) for cell in row] for row in rows])
    c = theme["colors"]
    table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), hexcolor(c["table_fill"])),
        ("GRID", (0, 0), (-1, -1), 0.35, hexcolor(c["border"])),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, hexcolor(c["teal"])),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5.5),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]))
    return table


def make_meta_table(rows: list[list[Any]], width: float, st: dict[str, ParagraphStyle], theme: dict[str, Any]) -> Table:
    data = []
    for idx, row in enumerate(rows):
        if not isinstance(row, list) or len(row) != 2:
            raise ValueError(f"cover.meta_rows[{idx}] must contain exactly two cells")
        data.append([ptext(row[0], st["table_bold"]), ptext(row[1], st["table"])])
    c = theme["colors"]
    table = Table(data, colWidths=[width * 0.27, width * 0.73], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), hexcolor(c["table_fill"])),
        ("GRID", (0, 0), (-1, -1), 0.35, hexcolor(c["border"])),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def make_callout(item: dict[str, Any], width: float, st: dict[str, ParagraphStyle], theme: dict[str, Any]) -> Table:
    c = theme["colors"]
    kind = item.get("kind", "info")
    fill, border = (
        (c["warning_fill"], c["warning_border"])
        if kind == "warning"
        else (c["callout_fill"], c["teal"])
    )
    content: list[Flowable] = []
    if item.get("title"):
        content.append(ptext(item["title"], st["callout_title"]))
    content.append(ptext(item.get("text", ""), st["callout_body"]))
    table = Table([[content]], colWidths=[width], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), hexcolor(fill)),
        ("BOX", (0, 0), (-1, -1), 0.8, hexcolor(border)),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return table


def render(input_path: Path, output_path: Path, theme_path: Path) -> None:
    spec = load_json(input_path)
    validate_spec(spec)
    theme = load_json(theme_path)
    regular, bold = register_fonts()
    theme["_fonts"] = (regular, bold)
    st = build_styles(theme, regular, bold)
    meta = spec["metadata"]
    page = theme["page"]
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=float(page["left_margin_mm"]) * mm,
        rightMargin=float(page["right_margin_mm"]) * mm,
        topMargin=float(page["top_margin_mm"]) * mm,
        bottomMargin=float(page["bottom_margin_mm"]) * mm,
        title=meta["title"],
        author=meta.get("author", "Dr. Komorowski Diagnose- und Trainingszentrum"),
        subject=meta.get("subject", "Sportdiagnostik und Trainingsplanung"),
        creator="Dr. Komorowski Sport Report Renderer",
    )
    frame_width = A4[0] - doc.leftMargin - doc.rightMargin
    ctheme = theme["colors"]

    def header_footer(canvas: Canvas, _doc: SimpleDocTemplate) -> None:
        canvas.saveState()
        top_y = A4[1] - 10.5 * mm
        canvas.setFillColor(hexcolor(ctheme["navy"]))
        canvas.setFont(bold, 7.6)
        canvas.drawRightString(A4[0] - doc.rightMargin, top_y, meta["header_right"])
        canvas.setStrokeColor(hexcolor(ctheme["border"]))
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, top_y - 3.5 * mm, A4[0] - doc.rightMargin, top_y - 3.5 * mm)
        bottom_y = 8.5 * mm
        canvas.line(doc.leftMargin, bottom_y + 4.5 * mm, A4[0] - doc.rightMargin, bottom_y + 4.5 * mm)
        canvas.setFillColor(hexcolor(ctheme["muted"]))
        canvas.setFont(regular, 7.2)
        canvas.drawString(doc.leftMargin, bottom_y, meta["footer_left"])
        canvas.drawRightString(A4[0] - doc.rightMargin, bottom_y, f"Seite {canvas.getPageNumber()}")
        canvas.restoreState()

    story: list[Flowable] = []
    cover = spec.get("cover") or {}
    if cover:
        story.extend([Spacer(1, 5 * mm), LogoFlowable(theme=theme), Spacer(1, 8 * mm)])
        if cover.get("eyebrow"):
            story.append(ptext(cover["eyebrow"], st["eyebrow"]))
        if cover.get("brand_heading"):
            story.append(ptext(cover["brand_heading"], st["cover_brand"]))
        if cover.get("title"):
            story.append(ptext(cover["title"], st["cover_title"]))
        if cover.get("subtitle"):
            story.append(ptext(cover["subtitle"], st["cover_subtitle"]))
        if cover.get("meta_rows"):
            story.extend([make_meta_table(cover["meta_rows"], frame_width, st, theme), Spacer(1, 6 * mm)])
        for callout in cover.get("callouts", []):
            if not isinstance(callout, dict):
                raise ValueError("cover.callouts entries must be objects")
            story.extend([make_callout(callout, frame_width, st, theme), Spacer(1, 3.5 * mm)])
        if spec.get("sections"):
            story.append(PageBreak())

    for sidx, section in enumerate(spec.get("sections", [])):
        if section.get("title"):
            story.append(ptext(section["title"], st["h1"]))
        for bidx, block in enumerate(section.get("blocks", [])):
            btype = block["type"]
            try:
                if btype == "heading":
                    story.append(ptext(block.get("text", ""), st["h1"]))
                elif btype == "subheading":
                    story.append(ptext(block.get("text", ""), st["h2"]))
                elif btype == "paragraph":
                    story.append(ptext(block.get("text", ""), st["body"]))
                elif btype == "bullets":
                    items = block.get("items", [])
                    if not isinstance(items, list):
                        raise ValueError("bullets.items must be an array")
                    for item in items:
                        story.append(Paragraph("• " + escape_text(item), st["bullet"]))
                elif btype == "table":
                    story.extend([make_table(block, frame_width, st, theme), Spacer(1, 4 * mm)])
                elif btype == "callout":
                    story.extend([make_callout(block, frame_width, st, theme), Spacer(1, 3.5 * mm)])
                elif btype == "spacer":
                    story.append(Spacer(1, float(block.get("mm", 3)) * mm))
                elif btype == "pagebreak":
                    story.append(PageBreak())
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(f"invalid block sections[{sidx}].blocks[{bidx}]: {exc}") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a structured Dr. Komorowski sport report to PDF.")
    parser.add_argument("input", type=Path, help="report specification JSON")
    parser.add_argument("output", type=Path, help="output PDF")
    parser.add_argument("--theme", type=Path, default=DEFAULT_THEME, help="theme JSON (default: bundled theme)")
    args = parser.parse_args()
    try:
        render(args.input.resolve(), args.output.resolve(), args.theme.resolve())
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
