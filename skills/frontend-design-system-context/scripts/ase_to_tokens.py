#!/usr/bin/env python3
"""Convert Adobe Swatch Exchange (ASE) or extracted ASE JSON into brand tokens.

The tool intentionally preserves non-RGB source models instead of guessing color-managed
CMYK/LAB -> sRGB conversions. RGB colors are exported losslessly enough for web tokens.
"""
from __future__ import annotations

import argparse
import json
import re
import struct
import unicodedata
from pathlib import Path
from typing import BinaryIO, Any


class PaletteError(ValueError):
    """Raised for invalid or unsupported palette input."""


def _read_exact(stream: BinaryIO, size: int) -> bytes:
    data = stream.read(size)
    if len(data) != size:
        raise PaletteError("Unexpected end of ASE file.")
    return data


def _u16(stream: BinaryIO) -> int:
    return struct.unpack(">H", _read_exact(stream, 2))[0]


def _u32(stream: BinaryIO) -> int:
    return struct.unpack(">I", _read_exact(stream, 4))[0]


def _f32(stream: BinaryIO) -> float:
    return struct.unpack(">f", _read_exact(stream, 4))[0]


def _ase_name(stream: BinaryIO) -> str:
    length = _u16(stream)
    raw = _read_exact(stream, length * 2)
    return raw.decode("utf-16-be").rstrip("\x00")


def _rgb_hex(values: list[float]) -> str:
    if len(values) != 3:
        raise PaletteError("RGB color requires exactly three channel values.")
    channels = [max(0, min(255, round(value * 255))) for value in values]
    return "#" + "".join(f"{channel:02X}" for channel in channels)


def parse_ase(path: Path) -> dict[str, Any]:
    groups: list[dict[str, str | None]] = []
    colors: list[dict[str, Any]] = []
    stack: list[str] = []

    with path.open("rb") as stream:
        if _read_exact(stream, 4) != b"ASEF":
            raise PaletteError(f"{path} is not a valid ASE file.")

        major = _u16(stream)
        minor = _u16(stream)
        block_count = _u32(stream)

        for _ in range(block_count):
            block_type = _u16(stream)
            block_length = _u32(stream)
            block_start = stream.tell()
            block_end = block_start + block_length

            if block_type == 0xC001:
                name = _ase_name(stream)
                groups.append({"name": name, "parent": stack[-1] if stack else None})
                stack.append(name)
            elif block_type == 0xC002:
                if stack:
                    stack.pop()
            elif block_type == 0x0001:
                name = _ase_name(stream)
                model = _read_exact(stream, 4).decode("ascii").strip()
                channel_counts = {"RGB": 3, "CMYK": 4, "LAB": 3, "Gray": 1}
                if model not in channel_counts:
                    raise PaletteError(f"Unsupported ASE color model {model!r} in {name!r}.")
                values = [_f32(stream) for _ in range(channel_counts[model])]
                color_type_raw = _u16(stream)
                color = {
                    "name": name,
                    "group": list(stack),
                    "model": model,
                    "values": values,
                    "type": {0: "global", 1: "spot", 2: "normal"}.get(
                        color_type_raw, f"unknown-{color_type_raw}"
                    ),
                }
                if model == "RGB":
                    color["hex"] = _rgb_hex(values)
                    color["rgb_255"] = [
                        max(0, min(255, round(value * 255))) for value in values
                    ]
                colors.append(color)

            if stream.tell() > block_end:
                raise PaletteError("ASE block length is inconsistent with its payload.")
            stream.seek(block_end)

    return {
        "source": path.name,
        "ase_version": f"{major}.{minor}",
        "groups": groups,
        "colors": colors,
    }


def load_palette(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".ase":
        return parse_ase(path)
    if suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise PaletteError(f"Invalid JSON: {exc}") from exc
        if not isinstance(data, dict) or not isinstance(data.get("colors"), list):
            raise PaletteError("Palette JSON must contain a top-level 'colors' array.")
        return data
    raise PaletteError("Input must be an .ase or .json file.")


def token_slug(name: str) -> str:
    base = re.sub(r"\s*\((?:RGB|CMYK|LAB|Gray)\)\s*$", "", name, flags=re.IGNORECASE)
    ascii_text = (
        unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode("ascii")
    )
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
    return slug or "unnamed"


def _hex_rgb(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"#([0-9A-Fa-f]{6})", value)
    if not match:
        raise PaletteError(f"Expected six-digit HEX color, got {value!r}.")
    raw = match.group(1)
    return tuple(int(raw[index:index + 2], 16) for index in (0, 2, 4))


def _linear(channel: int) -> float:
    value = channel / 255.0
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    r, g, b = _hex_rgb(hex_color)
    return 0.2126 * _linear(r) + 0.7152 * _linear(g) + 0.0722 * _linear(b)


def contrast_ratio(first: str, second: str) -> float:
    l1 = relative_luminance(first)
    l2 = relative_luminance(second)
    light, dark = max(l1, l2), min(l1, l2)
    return (light + 0.05) / (dark + 0.05)


def analyze_color(hex_color: str) -> dict[str, Any]:
    on_black = contrast_ratio(hex_color, "#000000")
    on_white = contrast_ratio(hex_color, "#FFFFFF")
    foreground = "#000000" if on_black >= on_white else "#FFFFFF"
    best = max(on_black, on_white)
    return {
        "contrast_on_black": round(on_black, 2),
        "contrast_on_white": round(on_white, 2),
        "recommended_foreground": foreground,
        "recommended_contrast": round(best, 2),
        "wcag_aa_normal": best >= 4.5,
        "wcag_aaa_normal": best >= 7.0,
        "wcag_aa_large": best >= 3.0,
    }


def normalize_palette(data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    normalized_colors: list[dict[str, Any]] = []
    warnings: list[str] = []
    used_tokens: set[str] = set()

    for index, raw in enumerate(data.get("colors", []), start=1):
        if not isinstance(raw, dict):
            raise PaletteError(f"Color entry {index} is not an object.")
        name = str(raw.get("name") or f"Color {index}")
        model = str(raw.get("model") or "").strip()
        token = token_slug(name)
        if token in used_tokens:
            candidate_index = 2
            candidate = f"{token}-{candidate_index}"
            while candidate in used_tokens:
                candidate_index += 1
                candidate = f"{token}-{candidate_index}"
            warnings.append(
                f"Duplicate token slug {token!r}; renamed {name!r} to {candidate!r}."
            )
            token = candidate
        used_tokens.add(token)

        item: dict[str, Any] = {
            "name": name,
            "token": token,
            "group": list(raw.get("group") or []),
            "model": model,
            "values": raw.get("values"),
            "type": raw.get("type"),
        }

        if model == "RGB":
            hex_color = raw.get("hex")
            if not isinstance(hex_color, str):
                values = raw.get("values")
                if not isinstance(values, list):
                    raise PaletteError(f"RGB color {name!r} has neither HEX nor values.")
                hex_color = _rgb_hex([float(value) for value in values])
            hex_color = hex_color.upper()
            _hex_rgb(hex_color)
            item["hex"] = hex_color
            item["accessibility"] = analyze_color(hex_color)
        else:
            warnings.append(
                f"{name}: {model or 'unknown'} source preserved without web HEX conversion; "
                "use an ICC/color-managed conversion before creating sRGB tokens."
            )

        normalized_colors.append(item)

    if not normalized_colors:
        raise PaletteError("Palette contains no colors.")

    return (
        {
            "schema_version": 1,
            "source": data.get("source"),
            "ase_version": data.get("ase_version"),
            "groups": data.get("groups") or [],
            "policy": {
                "corporate_tokens_immutable": True,
                "semantic_tokens_project_specific": True,
                "derived_ui_colors_require_traceability": True,
                "non_rgb_requires_color_managed_conversion": True,
            },
            "colors": normalized_colors,
        },
        warnings,
    )


def render_brand_css(normalized: dict[str, Any]) -> str:
    lines = [
        "/* Generated corporate brand tokens. Source values are immutable.",
        " * Do not edit these values to create hover, surface, or semantic variants.",
        " * Define derived and semantic tokens in separate layers and document provenance.",
        " */",
        ":root {",
    ]
    for color in normalized["colors"]:
        if "hex" in color:
            lines.append(f"  --brand-{color['token']}: {color['hex']};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def render_contrast_report(normalized: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    entries = []
    for color in normalized["colors"]:
        if "hex" in color:
            entries.append(
                {
                    "name": color["name"],
                    "token": color["token"],
                    "hex": color["hex"],
                    **color["accessibility"],
                }
            )
    return {
        "schema_version": 1,
        "source": normalized.get("source"),
        "wcag_method": "WCAG 2 relative luminance and contrast ratio",
        "colors": entries,
        "warnings": warnings,
    }


def write_outputs(input_path: Path, output_dir: Path) -> tuple[Path, Path, Path]:
    data = load_palette(input_path)
    normalized, warnings = normalize_palette(data)
    output_dir.mkdir(parents=True, exist_ok=True)

    palette_path = output_dir / "brand-palette.json"
    css_path = output_dir / "brand.css"
    contrast_path = output_dir / "brand-contrast-report.json"

    palette_path.write_text(
        json.dumps(normalized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    css_path.write_text(render_brand_css(normalized), encoding="utf-8")
    contrast_path.write_text(
        json.dumps(render_contrast_report(normalized, warnings), indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    return palette_path, css_path, contrast_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert ASE or extracted ASE JSON into immutable brand tokens."
    )
    parser.add_argument("input", type=Path, help="Input .ase or extracted .json palette")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("design/tokens"),
        help="Output directory (default: design/tokens)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        outputs = write_outputs(args.input, args.out_dir)
    except (OSError, PaletteError) as exc:
        print(f"error: {exc}")
        return 2
    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
