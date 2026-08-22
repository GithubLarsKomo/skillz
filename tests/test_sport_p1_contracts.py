import unittest

from scripts.validate_sport_p1_contracts import validate


def envelope():
    return {
        "schema_version": 1,
        "athlete_id": "athlete-1",
        "generated_at": "2026-08-22T12:00:00Z",
        "source_refs": [],
        "uncertainties": [],
        "safety_flags": [],
    }


class SportP1ContractTests(unittest.TestCase):
    def test_recovery_rejects_opaque_readiness_score(self):
        value = envelope() | {
            "window_start": "2026-08-15", "window_end": "2026-08-22", "baseline": {},
            "current_signals": {}, "trend": {}, "interventions": [],
            "next_re_evaluation": "2026-08-23T08:00:00Z", "readiness_score": 72,
        }
        self.assertIn("recovery-state must not expose an opaque readiness_score", validate("recovery-state", value))

    def test_illness_red_flags_require_medical_routing(self):
        value = envelope() | {
            "symptom_state": {}, "current_stage": 0, "stages": [], "progression_criteria": [],
            "regression_criteria": [], "red_flags": ["chest_pain"], "medical_routing": {"required": False},
        }
        self.assertIn("red flags require medical_routing.required=true", validate("return-after-illness-plan", value))

    def test_energy_availability_review_requires_routing(self):
        value = envelope() | {"risk_state": "review", "signals": [], "confidence": 0.7, "routing": {}}
        self.assertIn("review states require routing", validate("energy-availability-risk", value))

    def test_adaptation_analysis_rejects_acwr_injury_probability(self):
        value = envelope() | {
            "analysis_window": {}, "data_coverage": {}, "baseline_method": {}, "trends": [],
            "interpretations": [], "alternative_explanations": [], "confidence": 0.6,
            "next_measurements": [], "acwr_injury_probability": 0.8,
        }
        self.assertIn("adaptation-analysis must not encode ACWR as injury probability", validate("adaptation-analysis", value))

    def test_valid_strength_power_contract(self):
        value = envelope() | {
            "plan_version": 1, "objective": "power", "mesocycle_ref": {"id": "m1"},
            "exercises": [], "progression": {}, "stop_rules": ["quality_loss"],
        }
        self.assertEqual(validate("strength-power-plan", value), [])


if __name__ == "__main__":
    unittest.main()
