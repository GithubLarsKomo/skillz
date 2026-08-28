from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
LEVEL1_FIXTURE = (
    ROOT / "tests" / "fixtures" / "euroimmun" / "corporate-design-24h-neuro.json"
)
LEVEL2_FIXTURE = (
    ROOT
    / "tests"
    / "fixtures"
    / "euroimmun"
    / "corporate-design-controlled-master-level2.json"
)
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
        cls.level1 = json.loads(LEVEL1_FIXTURE.read_text(encoding="utf-8"))
        cls.level2 = json.loads(LEVEL2_FIXTURE.read_text(encoding="utf-8"))
        cls.documentation = GOLDEN_REFERENCE.read_text(encoding="utf-8")

    def test_reference_files_exist(self):
        for path in (
            LEVEL1_FIXTURE,
            LEVEL2_FIXTURE,
            GOLDEN_REFERENCE,
            DESIGN,
            BRAND_PROFILE,
        ):
            with self.subTest(path=str(path)):
                self.assertTrue(path.is_file())

    def test_both_levels_are_bound_to_canonical_design_contract(self):
        for fixture in (self.level1, self.level2):
            with self.subTest(fixture=fixture["id"]):
                self.assertEqual(
                    fixture["designContract"], "docs/corporate/euroimmun/DESIGN.md"
                )

        self.assertEqual(self.level1["brandProfile"]["id"], "euroimmun-corporate")
        self.assertEqual(self.level1["brandProfile"]["version"], "1.0.0")

    def test_level1_uses_real_last_24h_content(self):
        self.assertEqual(
            self.level1["contentWindow"],
            {"start": "2026-08-27", "end": "2026-08-28"},
        )
        themes = "\n".join(self.level1["contentThemes"])
        for marker in (
            "Fujirebio",
            "pTau217",
            "NfL",
            "P216-pT217-P218-P219-T220-R221",
            "GFAP",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, themes)

    def test_level1_expected_gate_is_strict_pass(self):
        gate = self.level1["expectedGate"]
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

    def test_level1_full_render_and_pdf_parity_are_recorded(self):
        presentation = self.level1["presentation"]
        self.assertEqual(presentation["slides"], 7)
        self.assertEqual(presentation["renderCoverage"], "7/7")
        self.assertEqual(presentation["pdfParity"], "PASS")
        self.assertEqual(presentation["templateStatus"], "confirmed-reference")
        self.assertEqual(presentation["derivation"], "template-compatible")

        report = self.level1["report"]
        self.assertEqual(report["pages"], 3)
        self.assertEqual(report["renderCoverage"], "3/3")
        self.assertEqual(report["pdfParity"], "PASS")
        self.assertEqual(report["templateStatus"], "public-reference-fallback")

    def test_external_evidence_keeps_regulatory_precision(self):
        evidence = self.level1["externalEvidence"]
        fda_clearance = next(item for item in evidence if item.get("id") == "K242706")
        self.assertEqual(fda_clearance["source"], "FDA")
        self.assertEqual(fda_clearance["date"], "2025-05-16")

        events = "\n".join(item.get("event", "") for item in evidence)
        self.assertIn("NfL Blood IVDR CE", events)
        self.assertIn("pTau217 Plasma IVDR CE", events)
        self.assertIn("Class II recall/product correction", events)

    def test_level2_is_mandatory_for_controlled_template_claims(self):
        self.assertEqual(self.level2["level"], 2)
        self.assertEqual(self.level2["status"], "NOT_RUN")
        activation = self.level2["activation"]
        self.assertTrue(activation["mustNotPassWithoutBinaryMaster"])
        self.assertFalse(activation["repositoryStorageOfProprietaryMaster"])

        required_when = "\n".join(activation["requiredWhen"])
        for marker in (
            "binary master is available",
            "template-derived",
            "controlled master",
            "pixel/template parity",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, required_when)

    def test_level2_requires_binary_identity_and_master_fingerprints(self):
        evidence = self.level2["masterEvidence"]
        for key in (
            "runtimeBinaryRequired",
            "sha256Required",
            "approvedMasterIdentityMustBeRecordedAtRunTime",
            "masterLayoutInventoryRequired",
            "themeInventoryRequired",
            "logoFooterFingerprintRequired",
            "fontInventoryRequired",
        ):
            with self.subTest(key=key):
                self.assertTrue(evidence[key])

        self.assertEqual(
            evidence["confirmedReferenceSha256"],
            "a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2",
        )
        self.assertIsNone(evidence["approvedMasterSha256"])

    def test_level2_exercises_representative_master_archetypes(self):
        archetypes = "\n".join(self.level2["requiredArchetypes"])
        for marker in (
            "corporate cover",
            "section header",
            "analytical content",
            "two-column",
            "figure plus bullets plus conclusion",
            "table or portfolio",
            "custom diagram",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, archetypes)

    def test_level2_requires_full_parity_and_render_evidence(self):
        checks = self.level2["requiredChecks"]
        for key in (
            "sourceSha256",
            "slideSizeParity",
            "masterAndLayoutIdentity",
            "themeColorParity",
            "logoGeometryAndAspectRatio",
            "footerAndConfidentialityGeometry",
            "slideNumberBehavior",
            "fontFamilyAndFallbackDisposition",
            "placeholderGeometry",
            "safeAreaAndOverflow",
            "allSlidesRendered",
            "presentationPdfRendered",
            "sourcePdfParity",
            "visualDifferenceAssessment",
            "languageAndContentGate",
        ):
            with self.subTest(key=key):
                self.assertTrue(checks[key])

    def test_level2_acceptance_is_stricter_than_level1(self):
        acceptance = self.level2["acceptance"]
        self.assertEqual(acceptance["requiredDerivation"], "template-derived")
        self.assertEqual(acceptance["critical"], 0)
        self.assertEqual(acceptance["major"], 0)
        self.assertEqual(acceptance["renderCoverage"], "all/all")
        self.assertEqual(acceptance["pdfParity"], "PASS")
        self.assertEqual(acceptance["corporateDesignGate"], "PASS")
        self.assertEqual(acceptance["goldenReferenceLevel"], "LEVEL_2_PASS")

    def test_level2_supersession_and_rerun_policy_is_explicit(self):
        supersession = self.level2["supersession"]
        self.assertTrue(supersession["level1RemainsFallbackRegression"])
        self.assertTrue(supersession["level2SupersedesLevel1ForControlledPresentationClaims"])
        rerun = "\n".join(supersession["rerunRequiredWhen"])
        self.assertIn("SHA-256 changes", rerun)
        self.assertIn("master/layout/theme/logo/footer", rerun)
        self.assertIn("design contract changes materially", rerun)
        self.assertIn("rendering stack changes materially", rerun)

    def test_documentation_reserves_template_derived_claims_for_level2(self):
        for marker in (
            "Mandatory two-level model",
            "Level 1 — Shared Design / Fallback Golden Reference",
            "Level 2 — Controlled Master Golden Reference",
            "MUST NOT report `PASS` without the actual binary master",
            "Level 2 status is `NOT_RUN`",
            "template-derived",
            "SHA-256 of the actual PPTX binary",
            "logo geometry and aspect ratio",
            "source/PDF parity = `PASS`",
            "Corporate Design Gate = `PASS`",
            "LEVEL_2_PASS",
            "Level 1 remains the permanent fallback regression",
            "PPT-FONT-001",
            "PPT-TEMPLATE-001",
            "DOCX-TEMPLATE-001",
            "SCOPE-001",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.documentation)


if __name__ == "__main__":
    unittest.main()
