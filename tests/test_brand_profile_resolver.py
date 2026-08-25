from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "frontend-design-system-context"
SCRIPT_DIR = SKILL_ROOT / "scripts"
PROFILE_DIR = SKILL_ROOT / "references" / "brand-profiles"
sys.path.insert(0, str(SCRIPT_DIR))

from brand_profile_resolver import resolve_profile_id  # noqa: E402


def _luminance(hex_value: str) -> float:
    value = hex_value.lstrip("#")
    rgb = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def _contrast(a: str, b: str) -> float:
    la, lb = _luminance(a), _luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


class BrandProfileResolverTests(unittest.TestCase):
    def setUp(self):
        self.euroimmun = json.loads((PROFILE_DIR / "euroimmun.json").read_text(encoding="utf-8"))
        self.sport = json.loads((PROFILE_DIR / "sport-performance.json").read_text(encoding="utf-8"))

    def test_euroimmun_profile_preserves_authoritative_13_color_palette(self):
        expected = {
            "black": "#000000", "white": "#FFFFFF", "forest": "#218529", "clover": "#73C054",
            "orchid": "#7F03B0", "purple": "#B985D9", "sea": "#148087", "turquoise": "#3DD4CC",
            "flame": "#C94D00", "orange": "#FA7E33", "fuchsia": "#9E306E", "pink": "#FF8ECF",
            "yellow": "#FFEB0F",
        }
        self.assertEqual(self.euroimmun["palette"], expected)
        self.assertTrue(self.euroimmun["policy"]["automatic_default"])
        self.assertTrue(self.euroimmun["policy"]["skip_color_palette_grilling"])
        self.assertTrue(self.euroimmun["policy"]["corporate_tokens_immutable"])

    def test_resolution_precedence_euroimmun_over_sport_context(self):
        self.assertEqual(
            resolve_profile_id(context="EUROIMMUN sport performance dashboard", skill_slug="sport-performance-diagnostics"),
            "euroimmun-corporate",
        )

    def test_explicit_different_brand_suppresses_built_in_defaults(self):
        self.assertIsNone(
            resolve_profile_id(context="EUROIMMUN sport dashboard", skill_slug="sport-performance-diagnostics", explicit_brand="Partner Brand")
        )

    def test_ambiguous_ei_text_does_not_trigger_euroimmun(self):
        self.assertIsNone(resolve_profile_id(context="EI dashboard"))

    def test_sport_skill_and_renderer_resolve_sport_profile(self):
        self.assertEqual(resolve_profile_id(skill_slug="sport-performance-diagnostics"), "sport-performance")
        self.assertEqual(resolve_profile_id(skill_slug="dr-komorowski-sport-docx-report-renderer"), "sport-performance")

    def test_sport_profile_keeps_existing_report_theme_anchors(self):
        theme_path = ROOT / "skills" / "dr-komorowski-sport-docx-report-renderer" / "assets" / "report-theme.json"
        theme = json.loads(theme_path.read_text(encoding="utf-8"))["colors"]
        mapping = {
            "navy": "navy", "dark": "dark", "body": "body", "teal": "teal_bright",
            "teal_text": "teal", "muted": "muted", "border": "border", "table_fill": "surface",
            "callout_fill": "surface_subtle", "warning_fill": "warning_surface", "warning_border": "warning",
            "white": "white",
        }
        for theme_token, profile_token in mapping.items():
            self.assertEqual(theme[theme_token], self.sport["palette"][profile_token])

    def test_approved_sport_foreground_pairs_meet_wcag_aa_normal_text(self):
        for token, foreground in self.sport["foreground_defaults"].items():
            background = self.sport["palette"][token]
            self.assertGreaterEqual(_contrast(background, foreground), 4.5, token)


if __name__ == "__main__":
    unittest.main()
