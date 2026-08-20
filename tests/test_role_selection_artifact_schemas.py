from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_metadata_schemas", ROOT / "scripts" / "validate_metadata_schemas.py"
)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def load_schema(name: str) -> dict:
    return json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))


class RoleSelectionArtifactSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.handoff_schema = load_schema("role-requirements-handoff-v1.schema.json")
        cls.architecture_schema = load_schema("role-architecture-v1.schema.json")
        cls.scorecard_schema = load_schema("role-scorecard-v1.schema.json")
        cls.fit_schema = load_schema("candidate-role-fit-v1.schema.json")

        cls.handoff = {
            "schemaVersion": 1,
            "handoffId": "RH-001",
            "version": "1.0",
            "status": "approved",
            "rolePurpose": "Lead a measurable transformation.",
            "businessContext": "Turnaround with cross-functional dependencies.",
            "outcomes": ["Restore delivery predictability within 12 months."],
            "decisionRights": ["Own operating model decisions within approved scope."],
            "scope": "Operations, systems and transformation portfolio.",
            "interfaces": ["CEO", "CFO", "R&D"],
            "constraints": ["No additional headcount in first six months."],
            "mustHaveCapabilities": ["Turnaround execution"],
            "trainableCapabilities": ["Company-specific ERP knowledge"],
            "nonRequirements": ["Exact prior COO title"],
            "successEvidence": ["Demonstrated recovery of a complex operating system."],
            "openDecisions": [],
            "sources": ["Hiring manager workshop 2026-08-20"],
            "approvedAt": "2026-08-20",
            "approvalAuthority": "Hiring committee",
        }
        cls.architecture = {
            "schemaVersion": 1,
            "roleArchitectureId": "RA-001",
            "version": "1.0",
            "status": "approved",
            "sourceHandoffId": "RH-001",
            "sourceHandoffVersion": "1.0",
            "purpose": "Lead a measurable transformation.",
            "outcomes": ["Restore delivery predictability within 12 months."],
            "accountabilities": ["Own transformation outcomes."],
            "decisionRights": ["Own operating model decisions within approved scope."],
            "scope": "Operations, systems and transformation portfolio.",
            "interfaces": ["CEO", "CFO", "R&D"],
            "context": "Turnaround",
            "capabilities": ["Turnaround execution", "Technical-operational integration"],
            "experienceEvidence": ["Comparable transformation with measurable outcomes."],
            "successMeasures": ["Delivery predictability restored."],
            "nonGoals": ["Own commercial pricing."],
            "risksAndTensions": ["Speed versus organizational absorption capacity."],
            "approvedAt": "2026-08-20",
            "approvalAuthority": "Hiring committee",
        }
        cls.scorecard = {
            "schemaVersion": 1,
            "roleArchitectureId": "RA-001",
            "roleArchitectureVersion": "1.0",
            "scoringModelVersion": "1.0",
            "status": "approved",
            "approvedBeforeCandidateReview": True,
            "dimensions": [
                {
                    "id": "CAP-001",
                    "definition": "Can execute a complex turnaround.",
                    "weight": 0.6,
                    "evidence": ["Measured turnaround result"],
                    "minimumLevel": "strong",
                    "knockout": False,
                    "knockoutRationale": None,
                    "tracesTo": ["Turnaround execution"],
                },
                {
                    "id": "CAP-002",
                    "definition": "Can integrate technical and operating decisions.",
                    "weight": 0.4,
                    "evidence": ["Cross-functional technical operating leadership"],
                    "minimumLevel": None,
                    "knockout": False,
                    "knockoutRationale": None,
                    "tracesTo": ["Technical-operational integration"],
                },
            ],
            "approvedAt": "2026-08-20",
            "approvalAuthority": "Hiring committee",
        }
        cls.fit = {
            "schemaVersion": 1,
            "roleArchitectureId": "RA-001",
            "roleArchitectureVersion": "1.0",
            "scoringModelVersion": "1.0",
            "assessmentStatus": "current",
            "candidateEvidenceScope": "CV and primary public sources available as of assessment date.",
            "dimensionAssessments": [
                {
                    "dimensionId": "CAP-001",
                    "evidenceClass": "unknown",
                    "confidence": "low",
                    "evidence": [],
                    "assessment": "No sufficient evidence available yet.",
                    "verificationQuestion": "Describe a turnaround you personally led and quantify the result.",
                },
                {
                    "dimensionId": "CAP-002",
                    "evidenceClass": "verified",
                    "confidence": "high",
                    "evidence": ["Primary evidence of technical-operational integration."],
                    "assessment": "Directly supported by available evidence.",
                    "verificationQuestion": None,
                },
            ],
            "verifiedStrengths": ["Technical-operational integration"],
            "evidenceGaps": ["Turnaround outcome evidence"],
            "contradictions": [],
            "knockoutStatus": "unknown",
            "overallConfidence": "medium",
            "recommendedVerification": ["Structured interview"],
            "limitations": ["Public evidence is incomplete."],
        }

    def test_valid_role_stack_artifacts_match_schemas(self):
        for data, schema in (
            (self.handoff, self.handoff_schema),
            (self.architecture, self.architecture_schema),
            (self.scorecard, self.scorecard_schema),
            (self.fit, self.fit_schema),
        ):
            self.assertEqual([], validator.validate(data, schema))

    def test_invalid_status_is_rejected(self):
        data = copy.deepcopy(self.architecture)
        data["status"] = "banana"
        errors = validator.validate(data, self.architecture_schema)
        self.assertTrue(any("$.status" in item and "unsupported value" in item for item in errors))

    def test_scorecard_weight_range_is_enforced(self):
        data = copy.deepcopy(self.scorecard)
        data["dimensions"][0]["weight"] = 1.2
        errors = validator.validate(data, self.scorecard_schema)
        self.assertTrue(any("weight" in item and "greater than maximum" in item for item in errors))

    def test_scorecard_weights_sum_to_one(self):
        total = sum(item["weight"] for item in self.scorecard["dimensions"])
        self.assertAlmostEqual(total, 1.0)
        data = copy.deepcopy(self.scorecard)
        data["dimensions"][1]["weight"] = 0.3
        self.assertNotAlmostEqual(sum(item["weight"] for item in data["dimensions"]), 1.0)

    def test_scorecard_dimension_ids_are_unique(self):
        ids = [item["id"] for item in self.scorecard["dimensions"]]
        self.assertEqual(len(ids), len(set(ids)))
        data = copy.deepcopy(self.scorecard)
        data["dimensions"][1]["id"] = "CAP-001"
        ids = [item["id"] for item in data["dimensions"]]
        self.assertNotEqual(len(ids), len(set(ids)))

    def test_knockout_requires_documented_rationale(self):
        valid = copy.deepcopy(self.scorecard)
        valid["dimensions"][0]["knockout"] = True
        valid["dimensions"][0]["knockoutRationale"] = "Mandatory legal qualification for the role."
        self.assertTrue(
            all(not item["knockout"] or bool(item["knockoutRationale"]) for item in valid["dimensions"])
        )
        invalid = copy.deepcopy(valid)
        invalid["dimensions"][0]["knockoutRationale"] = None
        self.assertFalse(
            all(not item["knockout"] or bool(item["knockoutRationale"]) for item in invalid["dimensions"])
        )

    def test_architecture_and_scorecard_versions_must_match(self):
        self.assertEqual(self.architecture["roleArchitectureId"], self.scorecard["roleArchitectureId"])
        self.assertEqual(self.architecture["version"], self.scorecard["roleArchitectureVersion"])
        data = copy.deepcopy(self.scorecard)
        data["roleArchitectureVersion"] = "2.0"
        self.assertNotEqual(self.architecture["version"], data["roleArchitectureVersion"])

    def test_candidate_fit_must_use_same_normative_versions(self):
        self.assertEqual(self.fit["roleArchitectureId"], self.architecture["roleArchitectureId"])
        self.assertEqual(self.fit["roleArchitectureVersion"], self.architecture["version"])
        self.assertEqual(self.fit["scoringModelVersion"], self.scorecard["scoringModelVersion"])

    def test_candidate_fit_covers_every_scorecard_dimension_once(self):
        scorecard_ids = {item["id"] for item in self.scorecard["dimensions"]}
        assessment_ids = [item["dimensionId"] for item in self.fit["dimensionAssessments"]]
        self.assertEqual(set(assessment_ids), scorecard_ids)
        self.assertEqual(len(assessment_ids), len(set(assessment_ids)))

    def test_candidate_review_requires_prefrozen_scoring(self):
        self.assertTrue(self.scorecard["approvedBeforeCandidateReview"])
        data = copy.deepcopy(self.scorecard)
        data["approvedBeforeCandidateReview"] = False
        self.assertFalse(data["approvedBeforeCandidateReview"])

    def test_unknown_evidence_class_is_valid_without_negative_score(self):
        assessment = self.fit["dimensionAssessments"][0]
        self.assertEqual(assessment["evidenceClass"], "unknown")
        self.assertNotIn("score", assessment)


if __name__ == "__main__":
    unittest.main()
