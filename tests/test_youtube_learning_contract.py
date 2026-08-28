from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "youtube-video-ingestion",
    "multimodal-learning-analysis",
    "learning-summary-synthesis",
    "procedure-sop-extractor",
    "learning-visual-planner",
    "learning-content-design-system",
    "learning-svg-generator",
    "learning-image-generator",
    "learning-landingpage-renderer",
    "learning-document-delivery",
    "learning-artifact-qa",
    "youtube-learning-workflow",
}


class TestYoutubeLearningContract(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_all_learning_skills_exist(self) -> None:
        for slug in sorted(SKILLS):
            path = ROOT / "skills" / slug / "SKILL.md"
            self.assertTrue(path.exists(), slug)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"name: {slug}", text)
            self.assertIn("version: 0.1.0", text)
            self.assertIn("lastEvaluated: 2026-08-28", text)

    def test_orchestrator_routes_existing_presentation_stack(self) -> None:
        text = self.read("skills/youtube-learning-workflow/SKILL.md")
        for dependency in (
            "youtube-video-ingestion",
            "multimodal-learning-analysis",
            "learning-summary-synthesis",
            "procedure-sop-extractor",
            "learning-visual-planner",
            "learning-content-design-system",
            "learning-svg-generator",
            "learning-image-generator",
            "learning-landingpage-renderer",
            "learning-document-delivery",
            "learning-artifact-qa",
            "template-presentation-workflow",
        ):
            self.assertIn(f"  - {dependency}", text)
        self.assertIn("learning-content-model.json", text)
        self.assertIn("Der Orchestrator erklärt Subskill-Artefakte nicht zusätzlich als eigene Outputs", text)

    def test_sop_keeps_evidence_classes_and_control_boundary(self) -> None:
        text = self.read("skills/procedure-sop-extractor/SKILL.md")
        for marker in ("observed", "derived", "recommended", "incomplete-for-controlled-use"):
            self.assertIn(marker, text)
        self.assertIn("controlled-quality-documentation", text)
        self.assertIn("nicht erfinden", text)

    def test_multimodal_analysis_does_not_infer_visual_actions_from_transcript(self) -> None:
        text = self.read("skills/multimodal-learning-analysis/SKILL.md")
        self.assertIn("Transcript allein", text)
        self.assertIn("speech+frame", text)
        self.assertIn("unknown", text)

    def test_design_authority_preserves_corporate_contract(self) -> None:
        design = self.read("docs/learning-content/DESIGN.md")
        resolver = self.read("skills/learning-content-design-system/SKILL.md")
        orchestrator = self.read("skills/youtube-learning-workflow/SKILL.md")
        for text in (design, resolver, orchestrator):
            self.assertIn("docs/corporate/euroimmun/DESIGN.md", text)
        self.assertIn("Corporate Design Gate", design)
        self.assertIn("Corporate Design Gate", resolver)
        self.assertIn("Corporate Design Gate", orchestrator)

    def test_learning_design_covers_all_requested_media_and_visuals(self) -> None:
        text = self.read("docs/learning-content/DESIGN.md")
        for marker in ("Landingpage", "Presentation", "DOCX / PDF", "Diagram and SVG", "Images and illustrations"):
            self.assertIn(marker, text)
        self.assertIn("Generated images are `illustrative-only`", text)

    def test_source_ingestion_forbids_access_control_bypass(self) -> None:
        text = self.read("skills/youtube-video-ingestion/SKILL.md")
        self.assertIn("Nicht erlaubt", text)
        self.assertIn("DRM", text)
        self.assertIn("partielles Quellenpaket", text)

    def test_final_qa_is_cross_format_and_render_based(self) -> None:
        text = self.read("skills/learning-artifact-qa/SKILL.md")
        for marker in ("HTML", "PPTX", "DOCX/PDF", "Cross-Format Fidelity"):
            self.assertIn(marker, text)
        self.assertIn("0 offenen Critical/Major Findings", text)

    def test_spec_declares_single_video_v1_and_extension_path(self) -> None:
        text = self.read("docs/specs/youtube-learner/SPEC.md")
        self.assertIn("playlist/multi-video synthesis", text)
        self.assertIn("local-video-learning-workflow", text)
        self.assertIn("provider-neutral", text)


if __name__ == "__main__":
    unittest.main()
