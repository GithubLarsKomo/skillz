import unittest

from scripts.validate_sport_p2_contracts import validate


def envelope():
    return {
        "schema_version": 1,
        "athlete_id": "athlete-1",
        "generated_at": "2026-08-22T18:00:00Z",
        "source_refs": [],
        "uncertainties": [],
        "safety_flags": [],
    }


class SportP2ContractTests(unittest.TestCase):
    def test_valid_performance_psychology_contract(self):
        value = envelope() | {
            "plan_version": 1,
            "performance_question": "Startfokus stabilisieren",
            "target_behavior": "zwei Prozess-Cues vor dem Start",
            "skills": [],
            "practice_blocks": [],
            "cues": [],
            "transfer_situations": [],
            "monitoring": {},
            "re_evaluation": {},
            "confidence": 0.6,
        }
        self.assertEqual(validate("performance-psychology-plan", value), [])

    def test_performance_psychology_rejects_clinical_treatment(self):
        value = envelope() | {
            "plan_version": 1, "performance_question": "focus", "target_behavior": "cue",
            "skills": [], "practice_blocks": [], "cues": [], "transfer_situations": [],
            "monitoring": {}, "re_evaluation": {}, "psychotherapy_plan": {},
        }
        self.assertIn("performance psychology must not contain psychotherapy_plan", validate("performance-psychology-plan", value))

    def test_urgent_mental_health_routing_pauses_performance_and_routes_immediately(self):
        value = envelope() | {
            "routing_version": 1,
            "concern_summary": "acute safety concern",
            "observed_signals": [],
            "functioning_course": {},
            "routing_level": "urgent",
            "training_boundaries": {"performance_optimization_paused": False},
            "support_path": {"immediate": False},
            "privacy_minimization": {},
            "confidence": 0.8,
        }
        errors = validate("mental-health-routing", value)
        self.assertIn("urgent routing requires training_boundaries.performance_optimization_paused=true", errors)
        self.assertIn("urgent routing requires support_path.immediate=true", errors)

    def test_music_requires_descriptive_bpm_context(self):
        value = envelope() | {
            "profile_version": 1,
            "preferences": {},
            "exclusions": [],
            "session_goals": [],
            "activation_target": {},
            "timing": [],
            "selection_rules": [],
            "bpm_context": {"descriptive_only": False, "range": [150, 170]},
            "safety_constraints": [],
            "feedback_fields": [],
        }
        self.assertIn("bpm_context must be descriptive_only=true", validate("training-music-profile", value))

    def test_jet_lag_requires_circadian_strategy(self):
        value = envelope() | {
            "adjustment_version": 1,
            "exposures": ["jet_lag"],
            "environment_travel_data": {},
            "target_event": {},
            "acclimation_strategy": {},
            "circadian_strategy": {},
            "microcycle_adjustments": [],
            "hydration_cooling_context": {},
            "monitoring": {},
            "next_re_evaluation": "2026-08-23T08:00:00Z",
        }
        self.assertIn("jet_lag exposure requires circadian_strategy", validate("environment-adjustment", value))

    def test_p2_artifacts_cannot_directly_patch_training_plan(self):
        value = envelope() | {
            "profile_version": 1,
            "preferences": {},
            "exclusions": [],
            "session_goals": [],
            "activation_target": {},
            "timing": [],
            "selection_rules": [],
            "safety_constraints": [],
            "feedback_fields": [],
            "revised_plan": {"entity_type": "planned_session"},
        }
        self.assertTrue(any("must not directly mutate training plans" in error for error in validate("training-music-profile", value)))


if __name__ == "__main__":
    unittest.main()
