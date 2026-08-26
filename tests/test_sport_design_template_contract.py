import json
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


def test_sport_profile_binds_branding_to_existing_impeccable_layout():
    profile = load(PROFILE)
    policy = profile["policy"]

    assert profile["id"] == "sport-performance"
    assert profile["version"] == "1.3.0"
    assert policy["binding_app_templates"] is True
    assert policy["branding_preserves_accepted_impeccable_layout"] is True
    assert policy["layout_redesign_requires_explicit_scope"] is True
    assert set(policy["branding_only_scope"]) == {
        "color-tokens",
        "semantic-color-roles",
        "logo",
        "wordmark",
        "favicon",
        "app-icon",
        "pwa-theme-metadata",
    }


def test_confirmed_template_spectrum_is_exact():
    profile = load(PROFILE)
    assert profile["confirmed_template_spectrum"] == CONFIRMED_SPECTRUM
    assert profile["palette"]["body"] == CONFIRMED_SPECTRUM["text_primary"]
    assert profile["palette"]["muted"] == CONFIRMED_SPECTRUM["text_secondary"]
    assert profile["palette"]["surface_subtle"] == CONFIRMED_SPECTRUM["surface_1"]
    assert profile["palette"]["surface"] == CONFIRMED_SPECTRUM["surface_2"]
    assert profile["palette"]["border"] == CONFIRMED_SPECTRUM["border"]


def test_sport_profile_exposes_both_reference_products():
    profile = load(PROFILE)
    products = profile["design_templates"]["products"]

    assert "sport-athlete-management" in products
    assert "masters-diagnostics" in products
    assert profile["design_templates"]["reference"].endswith("sport-performance-apps.md")


def test_template_contract_contains_literal_logo_and_color_guardrail():
    text = TEMPLATE.read_text(encoding="utf-8")

    assert "only logos and colors" in text
    assert "MUST NOT alter" in text
    assert "Impeccable UI template" in text
    assert "Sport Performance branding overlay" in text


def test_plugin_distribution_contains_same_binding_profile_and_template():
    assert load(PLUGIN_PROFILE) == load(PROFILE)
    plugin_text = PLUGIN_TEMPLATE.read_text(encoding="utf-8")
    assert "frozen by default" in plugin_text
    assert "only logos and colors" in plugin_text
