from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_sport_contracts.py"
SPEC = importlib.util.spec_from_file_location("validate_sport_contracts", SCRIPT)
module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(module)


def envelope() -> dict:
    return {
        "schema_version": 1,
        "athlete_id": "athlete-1",
        "generated_at": "2026-08-22T10:00:00Z",
        "source_refs": [],
        "uncertainties": [],
        "safety_flags": [],
    }


class SportAthleteManagementContractTests(unittest.TestCase):
    def test_schema_has_all_p0_definitions(self) -> None:
        data = json.loads((ROOT / "schemas" / "sport-athlete-management-v1.schema.json").read_text(encoding="utf-8"))
        expected = {"athleteProfile", "performanceModel", "seasonPlan", "mesocycle", "plannedSession", "microcycle", "dailyCheckin", "completedSession", "adaptationDecision", "athleteManagementState"}
        self.assertTrue(expected.issubset(data["$defs"]))

    def test_daily_checkin_accepts_sparse_optional_data(self) -> None:
        payload = envelope() | {
            "local_date": "2026-08-22",
            "sleep_quality_1_5": 3,
            "fatigue_1_5": 2,
            "soreness_1_5": 2,
            "stress_1_5": 4,
            "motivation_1_5": 4,
        }
        self.assertEqual([], module.validate("daily-checkin", payload))

    def test_session_load_is_deterministic(self) -> None:
        payload = envelope() | {
            "completed_session_id": "done-1",
            "started_at": "2026-08-22T08:00:00Z",
            "completed_at": "2026-08-22T09:20:00Z",
            "duration_min": 80,
            "session_rpe": 6,
            "session_load": 480,
            "completion_status": "completed",
        }
        self.assertEqual([], module.validate("completed-session", payload))
        payload["session_load"] = 470
        self.assertIn("session_load must equal duration_min * session_rpe", module.validate("completed-session", payload))

    def test_red_decision_cannot_progress_training(self) -> None:
        payload = envelope() | {
            "adaptation_decision_id": "decision-1",
            "decision_level": "acute",
            "action": "progress",
            "safety_state": "RED",
            "trigger": "syncope",
            "input_snapshot": {"red_flag": "syncope"},
            "rationale": "Medical review required",
            "confidence": 0.9,
            "human_override": False,
        }
        self.assertIn("RED decisions cannot continue normal training progression", module.validate("adaptation-decision", payload))

    def test_age_is_not_required_for_adaptation_decision(self) -> None:
        payload = envelope() | {
            "adaptation_decision_id": "decision-2",
            "decision_level": "acute",
            "action": "proceed",
            "safety_state": "GREEN",
            "trigger": "routine checkpoint",
            "input_snapshot": {},
            "rationale": "No adverse signal",
            "confidence": 0.6,
            "human_override": False,
        }
        self.assertEqual([], module.validate("adaptation-decision", payload))


if __name__ == "__main__":
    unittest.main()
