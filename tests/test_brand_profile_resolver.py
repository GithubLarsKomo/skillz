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

    def test_unrelated_explicit_brand_does_not_suppress_binding_domain_profiles(self):
        self.assertEqual(
            resolve_profile_id(context="sport dashboard", skill_slug="sport-performance-diagnostics", explicit_brand="Partner Brand"),
            "sport-performance",
        )
        self.assertEqual(
            resolve_profile_id(context="EUROIMMUN sport dashboard", skill_slug="sport-performance-diagnostics", explicit_brand="Partner Brand"),
            "euroimmun-corporate",
        )

    def test_unrelated_explicit_brand_outside_builtin_domains_still_suppresses_defaults(self):
        self.assertIsNone(resolve_profile_id(context="generic dashboard", explicit_brand="Partner Brand"))

    def test_ambiguous_ei_text_does_not_trigger_euroimmun(self):
        self.assertIsNone(resolve_profile_id(context="EI dashboard"))

    def test_sport_skill_and_renderer_resolve_sport_profile(self):
        self.assertEqual(resolve_profile_id(skill_slug="sport-performance-diagnostics"), "sport-performance")
        self.assertEqual(resolve_profile_id(skill_slug="dr-komorowski-sport-docx-report-renderer"), "sport-performance")

    def test_sport_profile_uses_confirmed_app_template_spectrum(self):
        self.assertTrue(self.sport["policy"]["binding_for_sport_applications"])
        self.assertFalse(self.sport["policy"]["explicit_project_brand_override_allowed"])
        self.assertTrue(self.sport["policy"]["branding_preserves_accepted_impeccable_layout"])
        self.assertEqual(self.sport["version"], "1.3.0")

        expected = {
            "navy": "#173652",
            "dark": "#0F172A",
            "body": "#0F172A",
            "teal_bright": "#2B8884",
            "teal": "#246F6C",
            "muted": "#475569",
            "border": "#E2E8F0",
            "surface": "#EEF2F7",
            "surface_subtle": "#F5F7FA",
            "warning_surface": "#F5F7FA",
            "warning": "#B54708",
            "white": "#FFFFFF",
        }
        for token, value in expected.items():
            self.assertEqual(self.sport["palette"][token], value)

        spectrum = self.sport["confirmed_template_spectrum"]
        self.assertEqual(spectrum["text_primary"], "#0F172A")
        self.assertEqual(spectrum["text_secondary"], "#475569")
        self.assertEqual(spectrum["surface_0"], "#FFFFFF")
        self.assertEqual(spectrum["surface_1"], "#F5F7FA")
        self.assertEqual(spectrum["surface_2"], "#EEF2F7")
        self.assertEqual(spectrum["border"], "#E2E8F0")

    def test_approved_sport_foreground_pairs_meet_wcag_aa_normal_text(self):
        for token, foreground in self.sport["foreground_defaults"].items():
            background = self.sport["palette"][token]
            self.assertGreaterEqual(_contrast(background, foreground), 4.5, token)


if __name__ == "__main__":
    unittest.main()
