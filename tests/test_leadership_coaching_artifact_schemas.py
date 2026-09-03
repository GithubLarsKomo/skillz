from __future__ import annotations

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


class LeadershipCoachingArtifactSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract_schema = load_schema("leadership-coaching-contract-v1.schema.json")
        cls.model_schema = load_schema("leadership-development-model-v1.schema.json")
        cls.reflection_schema = load_schema("leadership-reflection-v1.schema.json")
        cls.experiment_schema = load_schema("leadership-behavior-experiment-v1.schema.json")
        cls.review_schema = load_schema("leadership-coaching-review-v1.schema.json")
        cls.safety_schema = load_schema("coaching-safety-routing-v1.schema.json")
        cls.state_schema = load_schema("leadership-coaching-state-v1.schema.json")

    def test_representative_core_artifacts_match_schemas(self):
        artifacts = [
            ({
                "schemaVersion": 1,
                "coachingContractId": "LCC-001",
                "version": 1,
                "status": "active",
                "coachingMode": "self-coaching",
                "coachingPurpose": "Improve decision dialogue in management meetings.",
                "desiredOutcomes": ["Explore perspectives before deciding."],
                "successEvidence": ["Three clarification questions before own solution."],
                "scope": {"included": ["management meetings"], "excluded": []},
                "confidentiality": {"default": "private"},
                "persistence": {"rawReflections": False},
            }, self.contract_schema),
            ({
                "schemaVersion": 1,
                "developmentModelId": "LDM-001",
                "coachingCaseId": "LC-001",
                "developmentGoals": [{
                    "id": "DG-001",
                    "challenge": "Solutions are offered before exploration.",
                    "targetBehavior": "Ask clarifying questions first.",
                    "observableSignals": ["Three questions before solution."],
                    "status": "active",
                }],
            }, self.model_schema),
            ({
                "schemaVersion": 1,
                "reflectionId": "LR-001",
                "coachingCaseId": "LC-001",
                "situation": {"context": "steering meeting"},
                "observations": ["Two objections were raised."],
                "interpretations": ["The group may have disengaged."],
                "learningHypotheses": ["More exploration may increase contribution."],
            }, self.reflection_schema),
            ({
                "schemaVersion": 1,
                "experimentId": "LBE-001",
                "developmentGoalId": "DG-001",
                "hypothesis": "Exploration before solution increases contribution.",
                "targetSituation": "project meeting",
                "cue": "A problem is raised.",
                "behavior": "Ask three clarification questions before proposing a solution.",
                "dose": {"occurrences": 3},
                "measures": [{"type": "behavior", "description": "question count"}],
                "status": "planned",
            }, self.experiment_schema),
            ({
                "schemaVersion": 1,
                "reviewId": "LCR-001",
                "experimentRef": "LBE-001",
                "adherence": {"plannedOccurrences": 3, "observedOccurrences": 3},
                "behaviorChange": {"assessment": "improved"},
                "outcome": {"assessment": "uncertain"},
                "decision": "modify",
                "developmentGoalStatus": "active",
            }, self.review_schema),
            ({
                "schemaVersion": 1,
                "routingLevel": "coaching-support",
                "concernSummary": "Normal leadership development topic.",
                "observedSignals": [],
                "uncertainties": [],
                "routes": ["leadership-coaching"],
                "coachingBoundary": "Normal coaching is appropriate.",
                "privacyMinimization": {"thirdPartyData": "minimum"},
            }, self.safety_schema),
            ({
                "schemaVersion": 1,
                "coachingCaseId": "LC-001",
                "version": 1,
                "status": "active",
                "mode": "self-coaching",
                "safetyState": "coaching-support",
                "routing": {"currentSkill": "leadership-development-model"},
                "persistencePolicy": {"rawConversation": "session-only"},
                "updatedAt": "2026-09-03T19:00:00+02:00",
            }, self.state_schema),
        ]
        for data, schema in artifacts:
            self.assertEqual([], validator.validate(data, schema))

    def test_contract_rejects_unknown_status(self):
        data = {
            "schemaVersion": 1,
            "coachingContractId": "LCC-001",
            "version": 1,
            "status": "banana",
            "coachingMode": "self-coaching",
            "coachingPurpose": "Test",
            "desiredOutcomes": [],
            "successEvidence": [],
            "scope": {},
            "confidentiality": {},
            "persistence": {},
        }
        errors = validator.validate(data, self.contract_schema)
        self.assertTrue(any("status" in item for item in errors))

    def test_experiment_rejects_unknown_status(self):
        data = {
            "schemaVersion": 1,
            "experimentId": "LBE-001",
            "developmentGoalId": "DG-001",
            "hypothesis": "Test",
            "targetSituation": "meeting",
            "cue": "problem",
            "behavior": "ask",
            "dose": {},
            "measures": [],
            "status": "banana",
        }
        errors = validator.validate(data, self.experiment_schema)
        self.assertTrue(any("status" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
