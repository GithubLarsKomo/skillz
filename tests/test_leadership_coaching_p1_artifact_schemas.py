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


class LeadershipCoachingP1ArtifactSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.feedback_schema = load_schema("leadership-feedback-plan-v1.schema.json")
        cls.delegation_schema = load_schema("leadership-delegation-plan-v1.schema.json")
        cls.oneonone_schema = load_schema("leadership-1on1-plan-v1.schema.json")
        cls.conversation_schema = load_schema("difficult-conversation-plan-v1.schema.json")
        cls.performance_schema = load_schema("performance-management-plan-v1.schema.json")

    def test_representative_p1_artifacts_match_schemas(self):
        artifacts = [
            ({
                "schemaVersion": 1,
                "feedbackPlanId": "LFP-001",
                "purpose": "Clarify missed escalation expectations.",
                "observations": ["Two milestone risks were reported after the due date."],
                "impact": ["Decision time was reduced."],
                "questions": ["What prevented earlier escalation?"],
                "expectation": "Escalate forecast risk when threshold is crossed.",
                "status": "ready",
            }, self.feedback_schema),
            ({
                "schemaVersion": 1,
                "delegationId": "LD-001",
                "outcome": "Prepare an evidence-based operating review recommendation.",
                "delegateeRef": "role:team-lead",
                "authority": {"level": "decide-within-boundaries", "reservedDecisions": ["budget changes"]},
                "checkpoints": ["48 hours before review"],
                "escalationConditions": ["material data conflict"],
                "status": "planned",
            }, self.delegation_schema),
            ({
                "schemaVersion": 1,
                "oneOnOnePlanId": "O3-001",
                "meetingRef": "meeting:2026-09-10",
                "participantRef": "role:team-lead",
                "objectives": ["Review commitments and development topic."],
                "questions": ["What obstacle needs my decision?"],
                "decisionsToConfirm": [],
                "followUpCandidates": [],
                "status": "ready",
            }, self.oneonone_schema),
            ({
                "schemaVersion": 1,
                "conversationPlanId": "DCP-001",
                "purpose": "Address repeated late escalation of delivery risk.",
                "facts": ["Two risks were escalated after committed dates."],
                "interpretations": ["The manager may be avoiding escalation."],
                "messages": ["Early escalation is an explicit role expectation."],
                "questions": ["What contributed to the timing?"],
                "boundaries": ["No conclusion about motive before hearing perspective."],
                "professionalGate": {"triggered": False, "domains": [], "reasons": []},
                "desiredOutcome": "Shared expectation and next-step agreement.",
                "status": "ready",
            }, self.conversation_schema),
            ({
                "schemaVersion": 1,
                "performancePlanId": "PMP-001",
                "expectedOutcomes": ["Milestone forecasts remain within agreed tolerance."],
                "observedEvidence": ["Two milestones slipped by more than two weeks."],
                "performanceGaps": ["Forecast reliability below agreed threshold."],
                "causeHypotheses": [{"hypothesis": "Resource constraint", "status": "unverified"}],
                "employeePerspective": {"status": "not-yet-obtained", "summary": None},
                "supportActions": ["Review resource and priority conflicts."],
                "expectations": ["Escalate forecast risks earlier."],
                "reviewCriteria": ["Next two milestones and escalation timing."],
                "professionalGate": {"triggered": False, "domains": [], "reasons": []},
                "status": "active",
            }, self.performance_schema),
        ]
        for data, schema in artifacts:
            self.assertEqual([], validator.validate(data, schema))

    def test_delegation_rejects_unknown_authority_level(self):
        data = {
            "schemaVersion": 1,
            "delegationId": "LD-001",
            "outcome": "Test",
            "delegateeRef": "role:test",
            "authority": {"level": "do-whatever"},
            "checkpoints": [],
            "escalationConditions": [],
            "status": "planned",
        }
        errors = validator.validate(data, self.delegation_schema)
        self.assertTrue(any("authority" in item or "level" in item for item in errors))

    def test_performance_rejects_unknown_employee_perspective_status(self):
        data = {
            "schemaVersion": 1,
            "performancePlanId": "PMP-001",
            "expectedOutcomes": [],
            "observedEvidence": [],
            "performanceGaps": [],
            "causeHypotheses": [],
            "employeePerspective": {"status": "assumed"},
            "supportActions": [],
            "expectations": [],
            "reviewCriteria": [],
            "professionalGate": {"triggered": False, "domains": [], "reasons": []},
            "status": "draft",
        }
        errors = validator.validate(data, self.performance_schema)
        self.assertTrue(any("employeePerspective" in item or "status" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
