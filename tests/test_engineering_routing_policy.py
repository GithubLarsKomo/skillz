import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "docs" / "engineering-routing-policy.json"


class EngineeringRoutingPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads(POLICY.read_text(encoding="utf-8"))
        cls.transitions = {item["id"]: item for item in cls.policy["transitions"]}
        cls.scenarios = {item["id"]: item for item in cls.policy["scenarios"]}
        cls.skills = cls.policy["skills"]

    def test_policy_has_four_distinct_owners(self):
        self.assertEqual(
            set(self.skills),
            {"grilling", "wayfinder", "spec", "issues"},
        )
        owners = [spec["owns"] for spec in self.skills.values()]
        self.assertEqual(len(owners), len(set(owners)))

    def test_only_conversation_to_spec_may_produce_spec(self):
        producers = [
            key for key, value in self.skills.items() if "SPEC.md" in value.get("produces", [])
        ]
        self.assertEqual(producers, ["spec"])
        self.assertIn("SPEC.md", self.skills["grilling"]["mustNotProduce"])
        self.assertIn("SPEC.md", self.skills["wayfinder"]["mustNotProduce"])
        self.assertIn("SPEC.md", self.skills["issues"]["mustNotProduce"])

    def test_only_spec_to_vertical_issues_may_produce_vertical_issue_backlog(self):
        producers = [
            key
            for key, value in self.skills.items()
            if "vertical-issues.json" in value.get("produces", [])
        ]
        self.assertEqual(producers, ["issues"])

    def test_no_direct_grilling_to_issues_transition(self):
        direct = [
            item
            for item in self.policy["transitions"]
            if item["from"] == "grilling" and item["to"] == "issues"
        ]
        self.assertEqual(direct, [])
        self.assertTrue(
            any(
                item["from"] == "grilling" and item["to"] == "issues"
                for item in self.policy["forbiddenTransitions"]
            )
        )

    def test_spec_to_issues_requires_explicit_approval(self):
        transition = self.transitions["T7-spec-to-issues"]
        self.assertIn("specApproved", transition["requires"])
        self.assertEqual(
            transition["handoff"],
            ["SPEC.md", "decision register", "consistency report"],
        )

    def test_pre_spec_wayfinder_routes_through_spec_before_issues(self):
        scenario = self.scenarios["S1-pre-spec-technical"]
        self.assertEqual(scenario["class"], "pre-spec")
        self.assertEqual(scenario["expectedPath"], ["wayfinder", "spec", "issues"])
        transition = self.transitions["T3-wayfinder-pre-spec-to-spec"]
        self.assertEqual(transition["mode"], "pre-spec")
        self.assertIn("technicalEvidenceSufficient", transition["requires"])

    def test_pre_spec_mixed_uncertainty_can_round_trip_through_grilling(self):
        scenario = self.scenarios["S2-pre-spec-domain-then-technical"]
        self.assertEqual(
            scenario["expectedPath"],
            ["grilling", "wayfinder", "grilling", "spec", "issues"],
        )
        self.assertEqual(self.transitions["T4-wayfinder-to-grilling"]["to"], "grilling")

    def test_post_spec_slice_only_returns_to_issue_slicing(self):
        scenario = self.scenarios["S3-post-spec-slice-only"]
        self.assertEqual(scenario["expectedPath"], ["issues", "wayfinder", "issues"])
        transition = self.transitions["T9-wayfinder-post-spec-to-issues"]
        self.assertEqual(transition["mode"], "post-spec")
        self.assertIn("normativeSpecUnchanged", transition["requires"])

    def test_post_spec_normative_change_returns_through_spec(self):
        scenario = self.scenarios["S4-post-spec-normative-change"]
        self.assertEqual(
            scenario["expectedPath"], ["issues", "wayfinder", "spec", "issues"]
        )
        transition = self.transitions["T10-wayfinder-post-spec-to-spec"]
        self.assertIn("normativeSpecAssumptionChanged", transition["requires"])

    def test_wayfinder_domain_discovery_returns_to_grilling(self):
        scenario = self.scenarios["S5-return-to-domain-decision"]
        self.assertEqual(scenario["class"], "return")
        self.assertEqual(scenario["expectedPath"], ["wayfinder", "grilling", "spec"])

    def test_issue_slicing_domain_discovery_returns_to_grilling_and_respec(self):
        scenario = self.scenarios["S6-issue-slicing-discovers-domain-decision"]
        self.assertEqual(
            scenario["expectedPath"], ["issues", "grilling", "spec", "issues"]
        )
        self.assertEqual(self.transitions["T11-issues-to-grilling"]["to"], "grilling")

    def test_policy_matches_canonical_skill_anchors(self):
        expectations = {
            "round-based-requirements-grilling": [
                "requirements-handoff.json",
                "large-work-wayfinder",
                "conversation-to-spec",
                "spec-to-vertical-issues",
            ],
            "large-work-wayfinder": [
                "Pre-Spec Wayfinding",
                "Post-Spec Wayfinding",
                "round-based-requirements-grilling",
                "conversation-to-spec",
                "spec-to-vertical-issues",
            ],
            "conversation-to-spec": [
                "normative `SPEC.md`",
                "round-based-requirements-grilling",
                "large-work-wayfinder",
                "spec-to-vertical-issues",
            ],
            "spec-to-vertical-issues": [
                "ausdrücklich freigegebene `SPEC.md`",
                "round-based-requirements-grilling",
                "large-work-wayfinder",
                "conversation-to-spec",
            ],
        }
        for slug, anchors in expectations.items():
            text = (ROOT / "skills" / slug / "SKILL.md").read_text(encoding="utf-8")
            for anchor in anchors:
                with self.subTest(skill=slug, anchor=anchor):
                    self.assertIn(anchor, text)

    def test_required_regression_scenario_classes_exist(self):
        classes = {item["class"] for item in self.policy["scenarios"]}
        self.assertTrue({"pre-spec", "post-spec", "return"}.issubset(classes))


if __name__ == "__main__":
    unittest.main()
