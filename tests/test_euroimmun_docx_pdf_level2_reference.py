from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "docs" / "corporate" / "euroimmun" / "ACTIVE_REPORT_REFERENCE.md"
DE_NOVO = ROOT / "docs" / "corporate" / "euroimmun" / "DE_NOVO_REPORT_MASTER.md"
POLICY = ROOT / "docs" / "corporate" / "euroimmun" / "GOLDEN_REFERENCE.md"
FIXTURE = ROOT / "tests" / "fixtures" / "euroimmun" / "corporate-design-controlled-report-level2.json"
DOCX_SKILL = ROOT / "skills" / "euroimmun-docx-report-renderer" / "SKILL.md"
PDF_SKILL = ROOT / "skills" / "euroimmun-pdf-report-renderer" / "SKILL.md"


class TestEuroimmunDocxPdfLevel2Reference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.active = ACTIVE.read_text(encoding="utf-8")
        cls.de_novo = DE_NOVO.read_text(encoding="utf-8")
        cls.policy = POLICY.read_text(encoding="utf-8")
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.docx = DOCX_SKILL.read_text(encoding="utf-8")
        cls.pdf = PDF_SKILL.read_text(encoding="utf-8")

    def test_files_exist(self):
        for path in (ACTIVE, DE_NOVO, POLICY, FIXTURE, DOCX_SKILL, PDF_SKILL):
            self.assertTrue(path.is_file(), str(path))

    def test_no_false_controlled_reference_is_registered(self):
        self.assertIn("NONE_REGISTERED", self.active)
        self.assertIn("current Level-2 certification record: `NONE`", self.active)
        self.assertIn("public-reference-fallback", self.active)
        self.assertEqual(self.fixture["status"], "NOT_RUN")
        self.assertIsNone(self.fixture["currentReference"]["preferredCurrentReferenceName"])
        self.assertFalse(self.fixture["activation"]["publicReferenceMaySatisfyLevel2"])
        self.assertTrue(self.fixture["activation"]["mustNotPassWithoutBinaryTemplate"])

    def test_de_novo_visual_baseline_is_approved_without_level2_promotion(self):
        for marker in (
            "approved visual design baseline: `EUROIMMUN Corporate Report Master v0.2`",
            "DESIGN_APPROVED / CONTROLLED_MASTER_PENDING",
            "DOCX Level 2: `NOT_RUN`",
            "PDF Level 2: `NOT_RUN`",
            "REPORT_BODY_START",
            "EI_REPORT_BODY",
            "320e1a291aaf8639f05844bb7cff24cfc42e1f8c59618bb90059d6a9861afacb",
            "e5efc95c12a05efa10483f3f15cf45b823dc88a21de643780fd265d723221276",
        ):
            self.assertIn(marker, self.active)
        self.assertIn("Status: **DESIGN_APPROVED / CONTROLLED_MASTER_PENDING**", self.de_novo)
        self.assertIn("blank master DOCX: `2/2 PASS`", self.de_novo)
        self.assertIn("specimen DOCX: `4/4 PASS`", self.de_novo)
        self.assertIn("derived specimen PDF: `4/4 PASS`", self.de_novo)
        self.assertIn("visible-layout parity: `PASS`", self.de_novo)
        self.assertIn("does **not** mean:", self.de_novo)
        self.assertIn("`LEVEL_2_PASS`", self.de_novo)

    def test_docx_skill_requires_real_binary_sha_and_adapter(self):
        for marker in (
            "ACTIVE_REPORT_REFERENCE.md",
            "Report-Level-2",
            "SHA-256",
            "template-derived",
            "Template-Profil/Adapter",
            "Public-Reference-Fallback",
            "approved-controlled",
            "NOT_RUN",
        ):
            self.assertIn(marker, self.docx)
        self.assertIn("nicht verpflichtend", self.docx)
        self.assertIn("kontrolliertes Template", self.docx)

    def test_pdf_level_cannot_exceed_docx_level(self):
        for marker in (
            "ACTIVE_REPORT_REFERENCE.md",
            "kein höheres Golden-Reference-Level",
            "DOCX-Level-2 = `NOT_RUN`",
            "PDF-Level-2 = `NOT_RUN`",
            "Source DOCX hat Report-Level-2 = `LEVEL_2_PASS`",
            "DOCX/PDF source parity = `PASS`",
        ):
            self.assertIn(marker, self.pdf)

    def test_fixture_requires_full_docx_and_pdf_evidence(self):
        self.assertTrue(all(self.fixture["requiredSourceEvidence"].values()))
        self.assertTrue(all(self.fixture["docxRequiredChecks"].values()))
        self.assertTrue(all(self.fixture["pdfRequiredChecks"].values()))
        self.assertEqual(self.fixture["docxAcceptance"]["requiredDerivation"], "template-derived")
        self.assertEqual(self.fixture["docxAcceptance"]["critical"], 0)
        self.assertEqual(self.fixture["docxAcceptance"]["major"], 0)
        self.assertEqual(self.fixture["pdfAcceptance"]["sourceDocxRequiredStatus"], "LEVEL_2_PASS")
        self.assertEqual(self.fixture["pdfAcceptance"]["sourceParity"], "PASS")

    def test_policy_explicitly_defines_report_level2(self):
        for marker in (
            "DOCX/PDF Report Level 2",
            "Report Level 2 is currently `NOT_RUN`",
            "A real internal Word template MUST NOT be modified merely to add Skillz-specific",
            "DOCX `LEVEL_2_PASS` requires",
            "PDF `LEVEL_2_PASS` additionally requires",
            "If DOCX Level 2 is `NOT_RUN`, PDF Level 2 MUST also be `NOT_RUN`",
        ):
            self.assertIn(marker, self.policy)


if __name__ == "__main__":
    unittest.main()
