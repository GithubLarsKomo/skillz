from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "euroimmun" / "corporate-design-24h-neuro.json"
GOLDEN_REFERENCE = ROOT / "docs" / "corporate" / "euroimmun" / "GOLDEN_REFERENCE.md"
DESIGN = ROOT / "docs" / "corporate" / "euroimmun" / "DESIGN.md"
BRAND_PROFILE = (
    ROOT
    / "skills"
    / "frontend-design-system-context"
    / "references"
    / "brand-profiles"
    / "euroimmun.json"
)


class TestEuroimmunCorporateDesignGoldenReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_reference_files_exist(self):
        for path in (FIXTURE, GOLDEN_REFERENCE, DESIGN, BRAND_PROFILE):
            with self.subTest(path=str(path)):
                self.assertTrue(path.is_file())

    def test_fixture_is_bound_to_canonical_design_contract(self):
        self.assertEqual(
            self.fixture["designContract"], "docs/corporate/euroimmun/DESIGN.md"
        )
        self.assertEqual(self.fixture["brandProfile"]["id"], "euroimmun-corporate")
        self.assertEqual(self.fixture["brandProfile"]["version"], "1.0.0")

    def test_reference_uses_real_last_24h_content(self):
        self.assertEqual(
            self.fixture["contentWindow"],
            {"start": "2026-08-27", "end": "2026-08-28"},
        )
        themes = "\n".join(self.fixture["contentThemes"])
        for marker in (
            "Fujirebio",
            "pTau217",
            "NfL",
            "P216-pT217-P218-P219-T220-R221",
            "GFAP",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, themes)

    def test_expected_gate_is_strict_pass(self):
        gate = self.fixture["expectedGate"]
        self.assertEqual(gate["status"], "PASS")
        self.assertEqual(gate["critical"], 0)
        self.assertEqual(gate["major"], 0)
        self.assertEqual(
            gate["warningIds"],
            [
                "PPT-FONT-001",
                "PPT-TEMPLATE-001",
                "DOCX-TEMPLATE-001",
                "SCOPE-001",
            ],
        )

    def test_full_render_and_pdf_parity_are_recorded(self):
        presentation = self.fixture["presentation"]
        self.assertEqual(presentation["slides"], 7)
        self.assertEqual(presentation["renderCoverage"], "7/7")
        self.assertEqual(presentation["pdfParity"], "PASS")
        self.assertEqual(presentation["templateStatus"], "confirmed-reference")
        self.assertEqual(presentation["derivation"], "template-compatible")

        report = self.fixture["report"]
        self.assertEqual(report["pages"], 3)
        self.assertEqual(report["renderCoverage"], "3/3")
        self.assertEqual(report["pdfParity"], "PASS")
        self.assertEqual(report["templateStatus"], "public-reference-fallback")

    def test_external_evidence_keeps_regulatory_precision(self):
        evidence = self.fixture["externalEvidence"]
        fda_clearance = next(item for item in evidence if item.get("id") == "K242706")
        self.assertEqual(fda_clearance["source"], "FDA")
        self.assertEqual(fda_clearance["date"], "2025-05-16")

        events = "\n".join(item.get("event", "") for item in evidence)
        self.assertIn("NfL Blood IVDR CE", events)
        self.assertIn("pTau217 Plasma IVDR CE", events)
        self.assertIn("Class II recall/product correction", events)

    def test_documentation_carries_non_approved_template_warnings(self):
        text = GOLDEN_REFERENCE.read_text(encoding="utf-8")
        for marker in (
            "template-compatible`, not `template-derived`",
            "MUST NOT be represented as an approved internal controlled DOCX template",
            "PPT-FONT-001",
            "PPT-TEMPLATE-001",
            "DOCX-TEMPLATE-001",
            "SCOPE-001",
            "Corporate Design Gate: PASS",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
