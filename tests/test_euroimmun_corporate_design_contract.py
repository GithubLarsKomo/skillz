from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "docs" / "corporate" / "euroimmun" / "DESIGN.md"
CONTRACT_PATH = "docs/corporate/euroimmun/DESIGN.md"

BOUND_SKILLS = (
    ROOT / "skills" / "euroimmun-presentation-workflow" / "SKILL.md",
    ROOT / "skills" / "euroimmun-docx-report-renderer" / "SKILL.md",
    ROOT / "skills" / "euroimmun-pdf-report-renderer" / "SKILL.md",
)


class TestEuroimmunCorporateDesignContract(unittest.TestCase):
    def test_design_contract_exists_and_contains_hard_gate(self):
        self.assertTrue(DESIGN.is_file(), "Canonical EUROIMMUN DESIGN.md is missing")
        text = DESIGN.read_text(encoding="utf-8")
        required_markers = (
            "# EUROIMMUN Corporate Content Design System",
            "## 3. Source-of-truth hierarchy",
            "## 4. Brand identity and asset integrity",
            "## 5. Typography",
            "## 6. Content and language design",
            "## 7. Presentation composition contract",
            "## 8. DOCX composition contract",
            "## 9. PDF contract",
            "## 12. Accessibility and robustness",
            "## 13. Corporate Design Gate",
            "Corporate Design Gate: PASS | FAIL",
            "unresolved Critical findings = 0",
            "unresolved Major findings = 0",
        )
        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_all_euroimmun_output_skills_bind_canonical_contract(self):
        for skill in BOUND_SKILLS:
            with self.subTest(skill=skill.name, path=str(skill)):
                self.assertTrue(skill.is_file())
                text = skill.read_text(encoding="utf-8")
                self.assertIn("## Verbindlicher Corporate Design Contract", text)
                self.assertIn(CONTRACT_PATH, text)
                self.assertIn("Corporate Design Gate", text)
                self.assertIn("PASS", text)

    def test_presentation_reference_cannot_override_corporate_palette(self):
        spec = (
            ROOT
            / "skills"
            / "euroimmun-presentation-workflow"
            / "references"
            / "euroimmun-template-spec.md"
        ).read_text(encoding="utf-8")
        self.assertIn(CONTRACT_PATH, spec)
        self.assertIn("euroimmun-corporate", spec)
        self.assertIn("non-normative observations", spec)

    def test_pdf_requires_docx_design_pass_and_full_render(self):
        text = (ROOT / "skills" / "euroimmun-pdf-report-renderer" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("DOCX mit `Corporate Design Gate: PASS`", text)
        self.assertIn("PDF vollständig rendern", text)
        self.assertIn("jede Seite", text)


if __name__ == "__main__":
    unittest.main()
