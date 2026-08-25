from __future__ import annotations

import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "skills" / "frontend-design-system-context" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from ase_to_tokens import (  # noqa: E402
    analyze_color,
    load_palette,
    normalize_palette,
    parse_ase,
    render_brand_css,
    write_outputs,
)

FIXTURE = ROOT / "tests" / "fixtures" / "impeccable_brand_palette_rgb.json"


def _ase_name(value: str) -> bytes:
    encoded = (value + "\x00").encode("utf-16-be")
    return struct.pack(">H", len(value) + 1) + encoded


def _block(kind: int, payload: bytes) -> bytes:
    return struct.pack(">HI", kind, len(payload)) + payload


def _small_ase() -> bytes:
    group = _block(0xC001, _ase_name("RGB"))
    color_payload = (
        _ase_name("Forest (RGB)")
        + b"RGB "
        + struct.pack(">fffH", 0.13, 0.52, 0.16, 0)
    )
    color = _block(0x0001, color_payload)
    group_end = _block(0xC002, b"")
    return b"ASEF" + struct.pack(">HHI", 1, 0, 3) + group + color + group_end


class AseToTokensTests(unittest.TestCase):
    def test_uploaded_palette_fixture_preserves_all_13_rgb_swatches(self):
        normalized, warnings = normalize_palette(load_palette(FIXTURE))
        self.assertEqual(len(normalized["colors"]), 13)
        self.assertEqual(warnings, [])
        by_token = {color["token"]: color for color in normalized["colors"]}
        self.assertEqual(by_token["forest"]["hex"], "#218529")
        self.assertEqual(by_token["yellow"]["hex"], "#FFEB0F")
        self.assertTrue(normalized["policy"]["corporate_tokens_immutable"])

    def test_contrast_recommends_white_for_forest_and_black_for_yellow(self):
        self.assertEqual(analyze_color("#218529")["recommended_foreground"], "#FFFFFF")
        self.assertTrue(analyze_color("#218529")["wcag_aa_normal"])
        self.assertEqual(analyze_color("#FFEB0F")["recommended_foreground"], "#000000")
        self.assertTrue(analyze_color("#FFEB0F")["wcag_aaa_normal"])

    def test_css_contains_only_immutable_brand_tokens(self):
        normalized, _ = normalize_palette(load_palette(FIXTURE))
        css = render_brand_css(normalized)
        self.assertIn("--brand-orchid: #7F03B0;", css)
        self.assertIn("--brand-sea: #148087;", css)
        self.assertNotIn("--color-primary", css)
        self.assertIn("Source values are immutable", css)

    def test_write_outputs_creates_palette_css_and_contrast_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_outputs(FIXTURE, Path(tmp))
            self.assertEqual([path.name for path in paths], [
                "brand-palette.json", "brand.css", "brand-contrast-report.json"
            ])
            report = json.loads((Path(tmp) / "brand-contrast-report.json").read_text())
            self.assertEqual(len(report["colors"]), 13)

    def test_binary_ase_parser_preserves_group_and_rgb_value(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "palette.ase"
            path.write_bytes(_small_ase())
            parsed = parse_ase(path)
            self.assertEqual(parsed["ase_version"], "1.0")
            self.assertEqual(parsed["groups"], [{"name": "RGB", "parent": None}])
            self.assertEqual(parsed["colors"][0]["group"], ["RGB"])
            self.assertEqual(parsed["colors"][0]["hex"], "#218529")

    def test_non_rgb_source_is_preserved_without_naive_hex_conversion(self):
        data = {
            "source": "print.ase",
            "colors": [{
                "name": "Corporate Spot",
                "group": [],
                "model": "CMYK",
                "values": [1.0, 0.0, 0.0, 0.0],
                "type": "spot",
            }],
        }
        normalized, warnings = normalize_palette(data)
        self.assertNotIn("hex", normalized["colors"][0])
        self.assertIn("ICC/color-managed conversion", warnings[0])


if __name__ == "__main__":
    unittest.main()
