#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
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


def _require_finite_number(value: Any, path: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{path} must be numeric")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{path} must be finite")
    return number


def validate_chart_block(block: dict[str, Any], path: str) -> None:
    chart_type = block.get("chart_type", "lactate_hr_power")
    if chart_type != "lactate_hr_power":
        raise ValueError(f"{path}.chart_type unsupported: {chart_type!r}")
    data = block.get("data")
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError(f"{path}.data must contain at least two rows")
    previous_power: float | None = None
    for ridx, row in enumerate(data):
        if not isinstance(row, dict):
            raise ValueError(f"{path}.data[{ridx}] must be an object")
        power = _require_finite_number(row.get("power_w"), f"{path}.data[{ridx}].power_w")
        _require_finite_number(row.get("lactate_mmol_l"), f"{path}.data[{ridx}].lactate_mmol_l")
        _require_finite_number(row.get("hr_bpm"), f"{path}.data[{ridx}].hr_bpm")
        if previous_power is not None and power <= previous_power:
            raise ValueError(f"{path}.data power_w values must be strictly increasing")
        previous_power = power
    bands = block.get("threshold_bands", [])
    if not isinstance(bands, list):
        raise ValueError(f"{path}.threshold_bands must be an array")
    for tidx, band in enumerate(bands):
        bpath = f"{path}.threshold_bands[{tidx}]"
        if not isinstance(band, dict):
            raise ValueError(f"{bpath} must be an object")
        if not isinstance(band.get("label"), str) or not band["label"].strip():
            raise ValueError(f"{bpath}.label must be a non-empty string")
        start = _require_finite_number(band.get("from_w"), f"{bpath}.from_w")
        end = _require_finite_number(band.get("to_w"), f"{bpath}.to_w")
        if end <= start:
            raise ValueError(f"{bpath}.to_w must be greater than from_w")
        if "working_w" in band:
            working = _require_finite_number(band.get("working_w"), f"{bpath}.working_w")
            if not start <= working <= end:
                raise ValueError(f"{bpath}.working_w must lie within the band")
    if "height_mm" in block:
        height = _require_finite_number(block["height_mm"], f"{path}.height_mm")
        if not 60 <= height <= 130:
            raise ValueError(f"{path}.height_mm must be between 60 and 130")


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
    allowed = {"heading", "subheading", "paragraph", "bullets", "table", "callout", "chart", "spacer", "pagebreak"}
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
            path = f"sections[{sidx}].blocks[{bidx}]"
            if btype not in allowed:
                raise ValueError(f"unsupported block type at {path}: {btype!r}")
            if btype == "table" and (
                not isinstance(block.get("columns"), list) or not isinstance(block.get("rows"), list)
            ):
                raise ValueError(f"table at {path} requires columns and rows arrays")
            if btype == "chart":
                validate_chart_block(block, path)


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
        "caption": ParagraphStyle("Caption", parent=styles["BodyText"], fontName=regular, fontSize=7.6, leading=10,
                                  textColor=hexcolor(c["muted"]), spaceBefore=1.5 * mm, spaceAfter=3 * mm),
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


def _nice_step(span: float, target_ticks: int = 5) -> float:
    if span <= 0:
        return 1.0
    raw = span / max(target_ticks, 1)
    magnitude = 10 ** math.floor(math.log10(raw))
    residual = raw / magnitude
    if residual <= 1:
        nice = 1
    elif residual <= 2:
        nice = 2
    elif residual <= 5:
        nice = 5
    else:
        nice = 10
    return nice * magnitude


def _axis_bounds(values: list[float], *, floor_zero: bool = False, target_ticks: int = 5) -> tuple[float, float, float]:
    low = min(values)
    high = max(values)
    if floor_zero:
        low = min(0.0, low)
    if math.isclose(low, high):
        high = low + 1.0
    span = high - low
    padding = span * 0.08
    low -= padding
    high += padding
    step = _nice_step(high - low, target_ticks)
    low = math.floor(low / step) * step
    high = math.ceil(high / step) * step
    if floor_zero:
        low = 0.0
    if high <= low:
        high = low + step
    return low, high, step


class LactateHRChart(Flowable):
    """Vector dual-axis chart for lactate and heart rate over power with LT working bands."""

    def __init__(self, block: dict[str, Any], width: float, theme: dict[str, Any]):
        super().__init__()
        self.block = block
        self.width = width
        self.height = float(block.get("height_mm", 92)) * mm
        self.theme = theme

    def draw(self) -> None:
        c = self.canv
        colorset = self.theme["colors"]
        regular, bold = self.theme["_fonts"]
        data = self.block["data"]
        bands = self.block.get("threshold_bands", [])

        powers = [float(row["power_w"]) for row in data]
        lactate = [float(row["lactate_mmol_l"]) for row in data]
        hr = [float(row["hr_bpm"]) for row in data]

        x_values = list(powers)
        for band in bands:
            x_values.extend([float(band["from_w"]), float(band["to_w"])])
            if "working_w" in band:
                x_values.append(float(band["working_w"]))
        x_min_raw, x_max_raw = min(x_values), max(x_values)
        x_span = max(x_max_raw - x_min_raw, 1.0)
        x_pad = max(5.0, x_span * 0.045)
        x_min = x_min_raw - x_pad
        x_max = x_max_raw + x_pad

        lact_min, lact_max, lact_step = _axis_bounds(lactate, floor_zero=True, target_ticks=5)
        hr_min, hr_max, hr_step = _axis_bounds(hr, floor_zero=False, target_ticks=5)
        hr_min = math.floor(hr_min / 10.0) * 10.0
        hr_max = math.ceil(hr_max / 10.0) * 10.0
        hr_step = max(10.0, _nice_step(hr_max - hr_min, 5))

        left = 16 * mm
        right = self.width - 16 * mm
        bottom = 18 * mm
        top = self.height - 18 * mm
        plot_w = right - left
        plot_h = top - bottom

        def sx(value: float) -> float:
            return left + (value - x_min) / (x_max - x_min) * plot_w

        def sy_lact(value: float) -> float:
            return bottom + (value - lact_min) / (lact_max - lact_min) * plot_h

        def sy_hr(value: float) -> float:
            return bottom + (value - hr_min) / (hr_max - hr_min) * plot_h

        c.setFillColor(hexcolor(colorset["navy"]))
        c.setFont(bold, 10.5)
        c.drawString(left, self.height - 7 * mm, self.block.get("title", "Laktat und Herzfrequenz über Leistung"))

        legend_y = self.height - 12 * mm
        c.setStrokeColor(hexcolor(colorset["navy"]))
        c.setLineWidth(1.8)
        c.line(left, legend_y, left + 7 * mm, legend_y)
        c.circle(left + 3.5 * mm, legend_y, 1.1 * mm, stroke=1, fill=0)
        c.setFillColor(hexcolor(colorset["body"]))
        c.setFont(regular, 7.2)
        c.drawString(left + 9 * mm, legend_y - 2.2, "Laktat (mmol/l)")
        lx = left + 43 * mm
        c.setStrokeColor(hexcolor(colorset["teal"]))
        c.setDash(3, 2)
        c.line(lx, legend_y, lx + 7 * mm, legend_y)
        c.setDash()
        c.setFillColor(hexcolor(colorset["teal"]))
        c.circle(lx + 3.5 * mm, legend_y, 1.0 * mm, stroke=0, fill=1)
        c.setFillColor(hexcolor(colorset["body"]))
        c.drawString(lx + 9 * mm, legend_y - 2.2, "Herzfrequenz (/min)")

        for band in bands:
            start = sx(float(band["from_w"]))
            end = sx(float(band["to_w"]))
            kind = str(band.get("kind", band.get("label", ""))).lower()
            is_lt2 = "2" in kind
            fill = colorset["warning_fill"] if is_lt2 else colorset["table_fill"]
            border = colorset["warning_border"] if is_lt2 else colorset["teal"]
            c.setFillColor(hexcolor(fill))
            c.setStrokeColor(hexcolor(border))
            c.setLineWidth(0.55)
            c.rect(start, bottom, max(end - start, 0.5), plot_h, stroke=1, fill=1)
            c.setFillColor(hexcolor(border))
            c.setFont(bold, 6.8)
            label = str(band["label"])
            label_w = c.stringWidth(label, bold, 6.8)
            c.drawString((start + end - label_w) / 2, top - 3.2 * mm, label)
            if "working_w" in band:
                wx = sx(float(band["working_w"]))
                c.setStrokeColor(hexcolor(border))
                c.setLineWidth(0.8)
                c.setDash(2, 2)
                c.line(wx, bottom, wx, top)
                c.setDash()

        c.setFont(regular, 6.8)
        tick = lact_min
        max_guard = 0
        while tick <= lact_max + lact_step * 0.25 and max_guard < 20:
            y = sy_lact(tick)
            c.setStrokeColor(hexcolor(colorset["border"]))
            c.setLineWidth(0.35)
            c.line(left, y, right, y)
            c.setFillColor(hexcolor(colorset["muted"]))
            label = f"{tick:.1f}".replace(".0", "")
            c.drawRightString(left - 2 * mm, y - 2.2, label)
            tick += lact_step
            max_guard += 1

        tick = hr_min
        max_guard = 0
        while tick <= hr_max + hr_step * 0.25 and max_guard < 20:
            y = sy_hr(tick)
            c.setFillColor(hexcolor(colorset["muted"]))
            c.drawString(right + 2 * mm, y - 2.2, f"{tick:.0f}")
            tick += hr_step
            max_guard += 1

        c.setStrokeColor(hexcolor(colorset["muted"]))
        c.setLineWidth(0.6)
        c.line(left, bottom, right, bottom)
        c.line(left, bottom, left, top)
        c.line(right, bottom, right, top)

        for power in powers:
            x = sx(power)
            c.setStrokeColor(hexcolor(colorset["muted"]))
            c.setLineWidth(0.45)
            c.line(x, bottom, x, bottom - 1.5 * mm)
            c.setFillColor(hexcolor(colorset["muted"]))
            c.setFont(regular, 6.6)
            label = f"{power:g}"
            w = c.stringWidth(label, regular, 6.6)
            c.drawString(x - w / 2, bottom - 5.2 * mm, label)

        c.setFillColor(hexcolor(colorset["body"]))
        c.setFont(bold, 7.0)
        x_label = self.block.get("x_label", "Leistung (W)")
        w = c.stringWidth(x_label, bold, 7.0)
        c.drawString((left + right - w) / 2, 6 * mm, x_label)
        c.saveState()
        c.translate(4.2 * mm, (bottom + top) / 2)
        c.rotate(90)
        y_label = self.block.get("left_y_label", "Laktat (mmol/l)")
        yw = c.stringWidth(y_label, bold, 7.0)
        c.drawString(-yw / 2, 0, y_label)
        c.restoreState()
        c.saveState()
        c.translate(self.width - 4.2 * mm, (bottom + top) / 2)
        c.rotate(90)
        r_label = self.block.get("right_y_label", "Herzfrequenz (/min)")
        rw = c.stringWidth(r_label, bold, 7.0)
        c.drawString(-rw / 2, 0, r_label)
        c.restoreState()

        c.setStrokeColor(hexcolor(colorset["navy"]))
        c.setFillColor(colors.white)
        c.setLineWidth(1.8)
        lact_points = [(sx(p), sy_lact(v)) for p, v in zip(powers, lactate)]
        for (x1, y1), (x2, y2) in zip(lact_points, lact_points[1:]):
            c.line(x1, y1, x2, y2)
        for x, y in lact_points:
            c.setStrokeColor(hexcolor(colorset["navy"]))
            c.setFillColor(colors.white)
            c.circle(x, y, 1.25 * mm, stroke=1, fill=1)

        c.setStrokeColor(hexcolor(colorset["teal"]))
        c.setFillColor(hexcolor(colorset["teal"]))
        c.setLineWidth(1.5)
        c.setDash(4, 2)
        hr_points = [(sx(p), sy_hr(v)) for p, v in zip(powers, hr)]
        for (x1, y1), (x2, y2) in zip(hr_points, hr_points[1:]):
            c.line(x1, y1, x2, y2)
        c.setDash()
        for x, y in hr_points:
            c.setFillColor(hexcolor(colorset["teal"]))
            c.circle(x, y, 1.1 * mm, stroke=0, fill=1)


def make_chart(block: dict[str, Any], width: float, st: dict[str, ParagraphStyle], theme: dict[str, Any]) -> list[Flowable]:
    chart = LactateHRChart(block, width, theme)
    items: list[Flowable] = [chart]
    if block.get("caption"):
        items.append(ptext(block["caption"], st["caption"]))
    else:
        items.append(Spacer(1, 3 * mm))
    return items


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
                elif btype == "chart":
                    story.extend(make_chart(block, frame_width, st, theme))
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
