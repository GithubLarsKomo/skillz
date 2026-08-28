from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARBITRATION = ROOT / "skills" / "learning-source-arbitration" / "SKILL.md"
SYNTHESIS = ROOT / "skills" / "multi-source-learning-synthesis" / "SKILL.md"
WORKFLOW = ROOT / "skills" / "youtube-playlist-learning-workflow" / "SKILL.md"
DESIGN = ROOT / "docs" / "learning-content" / "multi-source" / "DESIGN.md"
SPEC = ROOT / "docs" / "specs" / "youtube-learner" / "MULTI_VIDEO.md"
FIXTURE = ROOT / "tests" / "fixtures" / "youtube-learning" / "pcr-multivideo-golden.json"


class TestYouTubeMultiVideoLearningContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arbitration = ARBITRATION.read_text(encoding="utf-8")
        cls.synthesis = SYNTHESIS.read_text(encoding="utf-8")
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.design = DESIGN.read_text(encoding="utf-8")
        cls.spec = SPEC.read_text(encoding="utf-8")
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_required_components_exist(self):
        for path in (ARBITRATION, SYNTHESIS, WORKFLOW, DESIGN, SPEC, FIXTURE):
            self.assertTrue(path.is_file(), path)

    def test_source_count_is_not_truth(self):
        self.assertIn("Popularität, Likes, Views oder Kanalgröße sind kein Wahrheitsbeweis", self.arbitration)
        self.assertIn("Kein Mehrheitsvotum als Wahrheitsersatz", self.workflow)
        self.assertFalse(self.fixture["sourceArbitration"]["countViewsAsEvidence"])
        self.assertFalse(self.fixture["sourceArbitration"]["countLikesAsEvidence"])

    def test_independence_is_explicit(self):
        self.assertIn("Independence", self.arbitration)
        self.assertIn("dependency groups", self.arbitration)
        self.assertFalse(self.fixture["sourceArbitration"]["dependentSourcesInflateIndependentCount"])
        consensus = self.fixture["claimClusters"][0]
        self.assertEqual(consensus["independentSourceCount"], 2)

    def test_conflicts_cannot_be_smoothed_away(self):
        self.assertIn("Widerspruch darf nicht durch sprachliches Glätten verschwinden", self.arbitration)
        self.assertIn("Ein ungelöster materieller Konflikt darf nicht als eindeutige Take-Home-Message erscheinen", self.synthesis)
        self.assertTrue(self.fixture["sourceArbitration"]["unresolvedConflictsMustRemainVisible"])
        self.assertIn("A conflict is a first-class learning object", self.design)

    def test_protocol_hybridization_is_forbidden(self):
        policy = self.fixture["procedurePolicy"]
        self.assertFalse(policy["averageNumericalParameters"])
        self.assertFalse(policy["hybridProtocolAllowed"])
        self.assertFalse(policy["approved"])
        self.assertEqual(policy["controlledUseStatus"], "incomplete-for-controlled-use")
        self.assertIn("hypothetischen Hybrid-Protokoll", self.synthesis)
        self.assertIn("do not average temperatures, times, concentrations, thresholds or settings", self.design)

    def test_single_source_extension_is_not_consensus(self):
        qpcr = next(item for item in self.fixture["claimClusters"] if item["id"] == "C3")
        self.assertEqual(qpcr["convergenceStatus"], "single-source")
        self.assertEqual(qpcr["independentSourceCount"], 1)
        coverage = next(item for item in self.fixture["coverageMap"] if "qPCR" in item["objective"])
        self.assertEqual(coverage["state"], "single-source")

    def test_teaching_numbers_remain_qualified(self):
        q1 = next(item for item in self.fixture["qualifiedClaims"] if item["id"] == "Q1")
        q2 = next(item for item in self.fixture["qualifiedClaims"] if item["id"] == "Q2")
        self.assertTrue(q1["forbidUniversalValue"])
        self.assertTrue(q2["forbidGuaranteedYield"])

    def test_multi_source_design_states_are_required(self):
        for state in ("Consensus", "Qualified", "Single source", "Conflict", "Open"):
            self.assertIn(state, self.design)
        self.assertIn("do not use green = agreement / red = conflict as the only distinction", self.design)

    def test_one_canonical_model_drives_all_outputs(self):
        self.assertIn("einzigen Source of Truth", self.workflow)
        render = self.fixture["renderRequirements"]
        self.assertTrue(render["sameMultiSourceFingerprint"])
        self.assertTrue(render["stableSourceIdsAcrossFormats"])
        self.assertTrue(render["fullRenderCoverageRequired"])
        self.assertEqual(render["formats"], ["html", "pptx", "docx", "pdf"])

    def test_playlist_scaling_does_not_fake_completeness(self):
        self.assertIn("kein `complete-playlist`-Status", self.workflow)
        self.assertIn("Unavailable videos are never represented as analyzed", self.spec)


if __name__ == "__main__":
    unittest.main()
