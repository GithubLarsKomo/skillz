import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "docs" / "role-selection-routing-policy.json"


class RoleSelectionRoutingPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads(POLICY.read_text(encoding="utf-8"))
        cls.transitions = {item["id"]: item for item in cls.policy["transitions"]}
        cls.scenarios = {item["id"]: item for item in cls.policy["scenarios"]}

    def test_stage_ownership_is_distinct(self):
        owners = [item["owns"] for item in self.policy["stages"].values()]
        self.assertEqual(len(owners), len(set(owners)))

    def test_role_architecture_is_normative_hub(self):
        self.assertEqual(self.transitions["T3-architecture-to-authoring"]["from"], "architecture")
        self.assertEqual(self.transitions["T4-architecture-to-assessment"]["from"], "architecture")
        self.assertIn("architectureApproved", self.transitions["T3-architecture-to-authoring"]["requires"])
        self.assertIn("architectureApproved", self.transitions["T4-architecture-to-assessment"]["requires"])

    def test_grilling_is_preferred_but_not_hard_required_for_architecture(self):
        role_arch = (ROOT / "skills" / "role-architecture" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("requires: []", role_arch)
        self.assertIn("äquivalente bestätigte Evidenz", role_arch)
        self.assertEqual(self.transitions["T2-evidence-direct-to-architecture"]["to"], "architecture")

    def test_no_direct_requirements_to_authoring_or_assessment(self):
        forbidden = {(item["from"], item["to"]) for item in self.policy["forbiddenTransitions"]}
        self.assertIn(("requirements", "authoring"), forbidden)
        self.assertIn(("requirements", "assessment"), forbidden)

    def test_public_posting_is_not_assessment_input(self):
        forbidden = {(item["from"], item["to"]) for item in self.policy["forbiddenTransitions"]}
        self.assertIn(("public-job-posting.md", "assessment"), forbidden)
        scenario = self.scenarios["S4-assessment-from-public-posting"]
        self.assertEqual(scenario["expected"], "blocked")

    def test_draft_architecture_blocks_downstream_use(self):
        scenario = self.scenarios["S5-draft-architecture"]
        self.assertEqual(set(scenario["blockedTargets"]), {"authoring", "assessment"})

    def test_scorecard_version_mismatch_blocks_downstream_use(self):
        scenario = self.scenarios["S6-scorecard-version-mismatch"]
        self.assertEqual(set(scenario["blockedTargets"]), {"authoring", "assessment"})
        invariants = self.policy["scorecardInvariants"]
        self.assertIn("role architecture and scorecard ids and versions match exactly", invariants)

    def test_scorecard_weights_are_frozen_before_candidate_review(self):
        transition = self.transitions["T4-architecture-to-assessment"]
        self.assertIn("scoringFrozenBeforeCandidate", transition["requires"])
        self.assertEqual(self.scenarios["S11-scorecard-after-candidate"]["expected"], "blocked")

    def test_authoring_role_change_returns_to_architecture(self):
        scenario = self.scenarios["S7-authoring-discovers-role-change"]
        self.assertEqual(scenario["expectedPath"], ["authoring", "architecture", "authoring"])

    def test_assessment_role_model_defect_returns_to_architecture(self):
        scenario = self.scenarios["S8-assessment-discovers-role-model-defect"]
        self.assertEqual(scenario["expectedPath"], ["assessment", "architecture", "assessment"])

    def test_assessment_stakeholder_gap_can_return_to_grilling(self):
        scenario = self.scenarios["S9-assessment-discovers-stakeholder-decision"]
        self.assertEqual(
            scenario["expectedPath"],
            ["assessment", "architecture", "requirements", "architecture", "assessment"],
        )

    def test_new_architecture_version_invalidates_downstream_artifacts(self):
        scenario = self.scenarios["S10-architecture-version-change"]
        self.assertIn("candidate-role-fit.json", scenario["expectedStale"])
        self.assertIn("public-job-posting.md", scenario["expectedStale"])
        self.assertIn("stale", self.policy["versioning"]["staleRule"])

    def test_unknown_candidate_evidence_does_not_mean_failure(self):
        scenario = self.scenarios["S12-unknown-evidence"]
        self.assertEqual(scenario["expectedClassification"], "unknown")
        self.assertEqual(scenario["mustNotEqual"], "failed")

    def test_cross_version_candidate_ranking_is_forbidden(self):
        scenario = self.scenarios["S13-cross-version-ranking"]
        self.assertEqual(scenario["expected"], "no-common-ranking-until-reassessment")
        self.assertIn("same normative role and scoring versions", self.policy["versioning"]["comparisonRule"])

    def test_scorecard_invariants_cover_reproducibility(self):
        invariants = set(self.policy["scorecardInvariants"])
        self.assertIn("active weights sum to 1.0", invariants)
        self.assertIn("dimension ids are unique", invariants)
        self.assertIn("each knockout has a documented mandatory rationale", invariants)
        self.assertIn("weights thresholds and knockouts are approved before candidate review", invariants)

    def test_policy_matches_skill_lifecycle_anchors(self):
        expectations = {
            "role-requirements-grilling": [
                "handoffId",
                "status: draft | review | approved | superseded",
                "sourceHandoffId",
                "Keine Job Description direkt",
            ],
            "role-architecture": [
                "requires: []",
                "roleArchitectureId",
                "Summe der aktiven Gewichte",
                "vor Sichtung eines konkreten Kandidaten",
                "gelten ab diesem Zeitpunkt als `stale`",
            ],
            "job-description-authoring": [
                "status=approved",
                "roleArchitectureId",
                "Verbotene Übergänge",
                "werden alle aus der alten Version abgeleiteten Fassungen `stale`",
            ],
            "candidate-role-fit-assessment": [
                "scoringFrozenBeforeCandidate" if False else "vor Sichtung dieses Kandidaten",
                "assessmentStatus: current | stale",
                "Verbotene Übergänge",
                "muss gegen die neue normative Version erneut bewertet werden",
            ],
        }
        for slug, anchors in expectations.items():
            text = (ROOT / "skills" / slug / "SKILL.md").read_text(encoding="utf-8")
            for anchor in anchors:
                with self.subTest(skill=slug, anchor=anchor):
                    self.assertIn(anchor, text)


if __name__ == "__main__":
    unittest.main()
