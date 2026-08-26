import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "skills/frontend-design-system-context/references/brand-profiles/sport-performance.json"
TEMPLATE = ROOT / "skills/frontend-design-system-context/references/design-templates/sport-performance-apps.md"
PLUGIN_PROFILE = ROOT / "plugins/skillz/skills/frontend-design-system-context/references/brand-profiles/sport-performance.json"
PLUGIN_TEMPLATE = ROOT / "plugins/skillz/skills/frontend-design-system-context/references/design-templates/sport-performance-apps.md"


CONFIRMED_SPECTRUM = {
    "navy": "#173652",
    "teal": "#246F6C",
    "teal_bright": "#2B8884",
    "energy": "#B54708",
    "critical": "#B42318",
    "recovery": "#6D5BD0",
    "success": "#2E7D32",
    "surface_0": "#FFFFFF",
    "surface_1": "#F5F7FA",
    "surface_2": "#EEF2F7",
    "text_primary": "#0F172A",
    "text_secondary": "#475569",
    "border": "#E2E8F0",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class SportDesignTemplateContractTests(unittest.TestCase):
    def test_sport_profile_binds_branding_to_existing_impeccable_layout(self):
        profile = load(PROFILE)
        policy = profile["policy"]

        self.assertEqual(profile["id"], "sport-performance")
        self.assertEqual(profile["version"], "1.3.0")
        self.assertTrue(policy["binding_app_templates"])
        self.assertTrue(policy["branding_preserves_accepted_impeccable_layout"])
        self.assertTrue(policy["layout_redesign_requires_explicit_scope"])
        self.assertEqual(set(policy["branding_only_scope"]), {
            "color-tokens",
            "semantic-color-roles",
            "logo",
            "wordmark",
            "favicon",
            "app-icon",
            "pwa-theme-metadata",
        })

    def test_confirmed_template_spectrum_is_exact(self):
        profile = load(PROFILE)
        self.assertEqual(profile["confirmed_template_spectrum"], CONFIRMED_SPECTRUM)
        self.assertEqual(profile["palette"]["body"], CONFIRMED_SPECTRUM["text_primary"])
        self.assertEqual(profile["palette"]["muted"], CONFIRMED_SPECTRUM["text_secondary"])
        self.assertEqual(profile["palette"]["surface_subtle"], CONFIRMED_SPECTRUM["surface_1"])
        self.assertEqual(profile["palette"]["surface"], CONFIRMED_SPECTRUM["surface_2"])
        self.assertEqual(profile["palette"]["border"], CONFIRMED_SPECTRUM["border"])

    def test_sport_profile_exposes_both_reference_products(self):
        profile = load(PROFILE)
        products = profile["design_templates"]["products"]

        self.assertIn("sport-athlete-management", products)
        self.assertIn("masters-diagnostics", products)
        self.assertTrue(profile["design_templates"]["reference"].endswith("sport-performance-apps.md"))

    def test_template_contract_contains_literal_logo_and_color_guardrail(self):
        text = TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("only logos and colors", text)
        self.assertIn("MUST NOT alter", text)
        self.assertIn("Impeccable UI template", text)
        self.assertIn("Sport Performance branding overlay", text)

    def test_plugin_distribution_contains_same_binding_profile_and_template(self):
        self.assertEqual(load(PLUGIN_PROFILE), load(PROFILE))
        plugin_text = PLUGIN_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("frozen by default", plugin_text)
        self.assertIn("only logos and colors", plugin_text)


if __name__ == "__main__":
    unittest.main()
