from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
LEVEL1_FIXTURE = ROOT / "tests" / "fixtures" / "euroimmun" / "corporate-design-24h-neuro.json"
LEVEL2_FIXTURE = ROOT / "tests" / "fixtures" / "euroimmun" / "corporate-design-controlled-master-level2.json"
GOLDEN_REFERENCE = ROOT / "docs" / "corporate" / "euroimmun" / "GOLDEN_REFERENCE.md"
LEVEL2_RECORD = ROOT / "docs" / "corporate" / "euroimmun" / "GOLDEN_REFERENCE_LEVEL2_20260828.md"
DESIGN = ROOT / "docs" / "corporate" / "euroimmun" / "DESIGN.md"
BRAND_PROFILE = ROOT / "skills" / "frontend-design-system-context" / "references" / "brand-profiles" / "euroimmun.json"


class TestEuroimmunCorporateDesignGoldenReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.level1 = json.loads(LEVEL1_FIXTURE.read_text(encoding="utf-8"))
        cls.level2 = json.loads(LEVEL2_FIXTURE.read_text(encoding="utf-8"))
        cls.documentation = GOLDEN_REFERENCE.read_text(encoding="utf-8")
        cls.level2_record = LEVEL2_RECORD.read_text(encoding="utf-8")

    def test_reference_files_exist(self):
        for path in (LEVEL1_FIXTURE, LEVEL2_FIXTURE, GOLDEN_REFERENCE, LEVEL2_RECORD, DESIGN, BRAND_PROFILE):
            with self.subTest(path=str(path)):
                self.assertTrue(path.is_file())

    def test_both_levels_use_canonical_contract(self):
        for fixture in (self.level1, self.level2):
            self.assertEqual(fixture["designContract"], "docs/corporate/euroimmun/DESIGN.md")
        self.assertEqual(self.level1["brandProfile"]["id"], "euroimmun-corporate")
        self.assertEqual(self.level1["brandProfile"]["version"], "1.0.0")

    def test_level1_remains_real_24h_fallback_pass(self):
        self.assertEqual(self.level1["contentWindow"], {"start": "2026-08-27", "end": "2026-08-28"})
        themes = "\n".join(self.level1["contentThemes"])
        for marker in ("Fujirebio", "pTau217", "NfL", "P216-pT217-P218-P219-T220-R221", "GFAP"):
            self.assertIn(marker, themes)
        gate = self.level1["expectedGate"]
        self.assertEqual(gate["status"], "PASS")
        self.assertEqual(gate["critical"], 0)
        self.assertEqual(gate["major"], 0)
        self.assertEqual(self.level1["presentation"]["derivation"], "template-compatible")
        self.assertEqual(self.level1["presentation"]["renderCoverage"], "7/7")
        self.assertEqual(self.level1["report"]["renderCoverage"], "3/3")

    def test_level2_policy_still_requires_real_binary(self):
        self.assertEqual(self.level2["level"], 2)
        activation = self.level2["activation"]
        self.assertTrue(activation["mustNotPassWithoutBinaryMaster"])
        self.assertFalse(activation["repositoryStorageOfProprietaryMaster"])
        required_when = "\n".join(activation["requiredWhen"])
        for marker in ("binary master is available", "template-derived", "controlled master", "pixel/template parity"):
            self.assertIn(marker, required_when)

    def test_level2_is_now_certified_pass(self):
        self.assertEqual(self.level2["status"], "LEVEL_2_PASS")
        run = self.level2["certifiedRun"]
        self.assertEqual(run["runDate"], "2026-08-28")
        self.assertEqual(run["goldenReferenceLevel"], "LEVEL_2_PASS")
        self.assertEqual(run["corporateDesignGate"], "PASS")
        self.assertEqual(run["findings"]["critical"], 0)
        self.assertEqual(run["findings"]["major"], 0)

    def test_level2_records_exact_runtime_binary_identity(self):
        source = self.level2["certifiedRun"]["sourceBinary"]
        self.assertEqual(source["filename"], "260828 NDD Review.pptx")
        self.assertEqual(source["sha256"], "349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e")
        self.assertEqual(source["templateStatus"], "confirmed-reference-binary")
        self.assertEqual(source["slides"], 12)
        self.assertEqual(source["masters"], 3)
        self.assertEqual(source["visibleLayouts"], 51)
        self.assertEqual(source["themes"], 4)
        self.assertEqual(source["primaryTheme"]["majorFont"], "Hanken Grotesk Light")
        self.assertEqual(source["primaryTheme"]["minorFont"], "Hanken Grotesk")
        self.assertEqual(source["primaryTheme"]["colors"]["accent1"], "#208528")

    def test_level2_derived_artifact_is_template_derived_not_reconstructed(self):
        derived = self.level2["certifiedRun"]["derivedArtifact"]
        self.assertFalse(derived["repositoryStored"])
        self.assertEqual(derived["derivation"], "template-derived")
        self.assertEqual(derived["slides"], 7)
        self.assertEqual(derived["outOfBoundsObjects"], 0)
        for layout in (
            "Title Slide 05",
            "Section Header 03",
            "Title + 2 Column Content",
            "Titel und Inhalt",
            "Charts: Title and Content 02",
            "Content 02 Euroimmun",
            "Title Only",
        ):
            self.assertIn(layout, derived["layoutsUsed"])

    def test_level2_full_render_pdf_and_master_pixel_parity_pass(self):
        render = self.level2["certifiedRun"]["renderEvidence"]
        self.assertEqual(render["slideCoverage"], "7/7")
        self.assertEqual(render["presentationPdfCoverage"], "7/7")
        self.assertEqual(render["pdfParity"], "PASS")
        pixel = render["masterOwnedPixelParity"]
        for region in (
            "coverTopLogo",
            "coverBottomBrand",
            "coverRightArtwork",
            "contentFooterLeft",
            "contentFooterCenter",
            "contentFooterRule",
        ):
            self.assertEqual(pixel[region], "100% exact")

    def test_level2_warnings_preserve_font_status_and_theme_precedence(self):
        warnings = self.level2["certifiedRun"]["findings"]["warningIds"]
        self.assertEqual(warnings, ["FONT-RUNTIME-001", "TEMPLATE-STATUS-001", "THEME-PALETTE-001"])
        self.assertIn("Hanken Grotesk", self.level2_record)
        self.assertIn("confirmed-reference-binary", self.level2_record)
        self.assertIn("accent1 #208528", self.level2_record)
        self.assertIn("forest #218529", self.level2_record)

    def test_level2_required_checks_and_acceptance_remain_strict(self):
        for key, value in self.level2["requiredChecks"].items():
            with self.subTest(key=key):
                self.assertTrue(value)
        acceptance = self.level2["acceptance"]
        self.assertEqual(acceptance["requiredDerivation"], "template-derived")
        self.assertEqual(acceptance["critical"], 0)
        self.assertEqual(acceptance["major"], 0)
        self.assertEqual(acceptance["pdfParity"], "PASS")
        self.assertEqual(acceptance["corporateDesignGate"], "PASS")
        self.assertEqual(acceptance["goldenReferenceLevel"], "LEVEL_2_PASS")

    def test_level2_record_documents_master_owned_pixel_evidence(self):
        for marker in (
            "LEVEL_2_PASS",
            "349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e",
            "100% pixel-identical",
            "7/7",
            "Corporate Design Gate: `PASS`",
            "Level 1 remains the permanent fallback regression",
        ):
            self.assertIn(marker, self.level2_record)

    def test_supersession_and_rerun_policy_is_explicit(self):
        supersession = self.level2["supersession"]
        self.assertTrue(supersession["level1RemainsFallbackRegression"])
        self.assertTrue(supersession["level2SupersedesLevel1ForControlledPresentationClaims"])
        rerun = "\n".join(supersession["rerunRequiredWhen"])
        self.assertIn("SHA-256 changes", rerun)
        self.assertIn("master/layout/theme/logo/footer", rerun)
        self.assertIn("design contract changes materially", rerun)
        self.assertIn("rendering stack changes materially", rerun)

    def test_policy_document_still_reserves_template_derived_for_level2(self):
        for marker in (
            "Mandatory two-level model",
            "Level 1 — Shared Design / Fallback Golden Reference",
            "Level 2 — Controlled Master Golden Reference",
            "MUST NOT report `PASS` without the actual binary master",
            "template-derived",
            "SHA-256 of the actual PPTX binary",
            "logo geometry and aspect ratio",
            "LEVEL_2_PASS",
        ):
            self.assertIn(marker, self.documentation)


if __name__ == "__main__":
    unittest.main()
