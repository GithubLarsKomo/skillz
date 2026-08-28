from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "youtube-learning" / "pcr-golden.json"
GOLDEN = ROOT / "docs" / "learning-content" / "GOLDEN_REFERENCE.md"
DESIGN = ROOT / "docs" / "learning-content" / "DESIGN.md"
WORKFLOW = ROOT / "skills" / "youtube-learning-workflow" / "SKILL.md"


class TestYouTubeLearningGoldenReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.golden = GOLDEN.read_text(encoding="utf-8")
        cls.design = DESIGN.read_text(encoding="utf-8")
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_reference_files_exist(self):
        self.assertTrue(FIXTURE.is_file())
        self.assertTrue(GOLDEN.is_file())
        self.assertTrue(DESIGN.is_file())
        self.assertTrue(WORKFLOW.is_file())

    def test_source_and_mode_are_locked(self):
        self.assertEqual(self.fixture["source"]["youtubeVideoId"], "Q2847XA-Rfk")
        self.assertEqual(self.fixture["mode"], "full")
        self.assertEqual(self.fixture["language"], "de")
        self.assertIn("docs/learning-content/DESIGN.md", self.fixture["designAuthority"])

    def test_canonical_learning_anchors_are_preserved(self):
        anchors = self.fixture["learningAnchors"]
        self.assertEqual(anchors["denaturationC"], 95)
        self.assertEqual(anchors["annealingC"], 50)
        self.assertEqual(anchors["extensionC"], 72)
        self.assertEqual(anchors["cycles"], 35)
        self.assertEqual(anchors["amplificationStatement"], "2^35 > 34 billion")
        self.assertEqual(anchors["annealingQualification"], "source-simplified-not-universal")

    def test_sop_boundary_is_non_approval(self):
        anchors = self.fixture["learningAnchors"]
        self.assertEqual(anchors["sopClassification"], "derived-instructional-sop")
        self.assertFalse(anchors["sopApproved"])
        self.assertFalse(anchors["sopLabReady"])
        missing = set(self.fixture["requiredMissingParameters"])
        self.assertIn("reaction volumes", missing)
        self.assertIn("reagent concentrations", missing)
        self.assertIn("annealing-temperature optimization", missing)
        self.assertIn("product control", missing)
        self.assertIn("Keine regulierte SOP ohne externe fachliche/Quality-Freigabe", self.workflow)

    def test_visuals_are_generated_and_accessible(self):
        visuals = self.fixture["generatedVisuals"]
        self.assertEqual(len(visuals), 3)
        for visual in visuals:
            self.assertEqual(visual["format"], "svg")
            self.assertFalse(visual["sourceFrame"])
            self.assertTrue(visual["requiresTitle"])
            self.assertTrue(visual["requiresDesc"])
        self.assertIn("Generated imagery is illustrative, never evidence", self.design)

    def test_full_render_coverage_is_recorded(self):
        coverage = self.fixture["renderCoverage"]
        self.assertEqual(coverage["htmlWide"], "1/1 full-page")
        self.assertEqual(coverage["htmlNarrow"], "1/1 full-page")
        self.assertEqual(coverage["htmlPrint"], "7/7 pages")
        self.assertEqual(coverage["pptx"], "9/9 slides + presentation PDF")
        self.assertEqual(coverage["docx"], "4/4 pages")
        self.assertEqual(coverage["pdf"], "4/4 pages")
        self.assertEqual(coverage["svg"], "3/3 assets")

    def test_warning_state_is_explicit(self):
        warnings = {item["id"] for item in self.fixture["warnings"]}
        self.assertEqual(warnings, {"TS-001", "VIS-001", "SOP-001"})
        self.assertIn("No frame-specific claim is allowed", self.golden)
        self.assertIn("Removing a warning without improving", self.golden)

    def test_final_acceptance_is_strict(self):
        acceptance = self.fixture["acceptance"]
        self.assertEqual(acceptance["qaStatus"], "Learning Artifact QA: PASS")
        self.assertEqual(acceptance["crossFormatFidelity"], "PASS")
        self.assertEqual(acceptance["sourcePdfParity"], "PASS")
        self.assertEqual(acceptance["unresolvedCritical"], 0)
        self.assertEqual(acceptance["unresolvedMajor"], 0)
        self.assertEqual(acceptance["warningCount"], 3)
        self.assertIn("unresolved Critical findings = `0`", self.golden)
        self.assertIn("unresolved Major findings = `0`", self.golden)
        self.assertIn("Learning Artifact QA: PASS", self.golden)


if __name__ == "__main__":
    unittest.main()
