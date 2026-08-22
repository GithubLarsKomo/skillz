from __future__ import annotations

import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import sport_specialist_runtime as runtime


class SportSpecialistRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.provider = {
            "schemaVersion": 1,
            "providerId": "openai-compatible:test",
            "endpoint": "http://provider.internal/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }

    def request(self, artifact_type: str, *, skill: str | None = None, contract: dict | None = None, snapshot: dict | None = None) -> dict:
        descriptor = runtime.REGISTRY[artifact_type]
        return {
            "athlete_id": "athlete-1",
            "trigger": "fixture-trigger",
            "artifact_type": artifact_type,
            "skill": descriptor["skill"] if skill is None else skill,
            "contract": contract or {"layer": descriptor["layer"], "version": 1, "definition": descriptor["definition"]},
            "snapshot": {} if snapshot is None else snapshot,
        }

    @staticmethod
    def response(artifact: dict) -> bytes:
        return json.dumps({"choices": [{"message": {"content": json.dumps(artifact)}}]}).encode("utf-8")

    @staticmethod
    def music_artifact() -> dict:
        return {
            "schema_version": 99,
            "athlete_id": "forged-athlete",
            "generated_at": "2000-01-01T00:00:00Z",
            "source_refs": ["fixture"],
            "uncertainties": [],
            "safety_flags": [],
            "profile_version": 1,
            "preferences": {},
            "exclusions": [],
            "session_goals": [],
            "activation_target": {},
            "timing": [],
            "selection_rules": [],
            "bpm_context": {"descriptive_only": True},
            "safety_constraints": [],
            "feedback_fields": [],
        }

    def test_registry_covers_all_p1_and_p2_product_artifacts(self):
        self.assertEqual(len(runtime.REGISTRY), 13)
        self.assertEqual(runtime.REGISTRY["recovery_state"]["skill"], "sport-recovery-sleep")
        self.assertEqual(runtime.REGISTRY["mental_health_routing"]["definition"], "mentalHealthRouting")
        self.assertEqual(runtime.REGISTRY["environment_adjustment"]["layer"], "p2")

    def test_request_rejects_skill_and_contract_injection(self):
        with self.assertRaisesRegex(ValueError, "skill does not match"):
            runtime.validate_runtime_request(self.request("training_music_profile", skill="../../arbitrary-skill"))
        with self.assertRaisesRegex(ValueError, "contract does not match"):
            runtime.validate_runtime_request(self.request("training_music_profile", contract={"layer": "p1", "version": 1, "definition": "recoveryState"}))

    def test_prompt_contains_registered_skill_and_canonical_contract_only(self):
        request = self.request("training_music_profile", snapshot={"profile": {"sport": "rowing"}})
        body = runtime.build_provider_body(request, self.provider)
        self.assertEqual(body["temperature"], 0)
        self.assertEqual(body["model"], "fixture-model")
        self.assertIn("sport-training-music", body["messages"][0]["content"])
        user = json.loads(body["messages"][1]["content"])
        self.assertEqual(user["contract"]["definition"], "trainingMusicProfile")
        self.assertIn("commonEnvelope", user["contract_schema"])
        self.assertIn("trainingMusicProfile", user["contract_schema"])
        self.assertEqual(user["snapshot"]["profile"]["sport"], "rowing")

    def test_valid_provider_artifact_is_identity_bound_validated_and_provenanced(self):
        request = self.request("training_music_profile")
        captured = {}

        def transport(endpoint, body, headers, timeout):
            captured.update(endpoint=endpoint, body=json.loads(body), headers=headers, timeout=timeout)
            return self.response(self.music_artifact())

        result = runtime.invoke(
            request,
            self.provider,
            transport=transport,
            environ={},
            revision="skillz-fixture-sha",
            now=datetime(2026, 8, 22, 18, 30, tzinfo=timezone.utc),
        )
        artifact = result["artifact"]
        self.assertEqual(artifact["schema_version"], 1)
        self.assertEqual(artifact["athlete_id"], "athlete-1")
        self.assertEqual(artifact["generated_at"], "2026-08-22T18:30:00Z")
        self.assertEqual(result["provenance"]["skillz_revision"], "skillz-fixture-sha")
        self.assertEqual(result["provenance"]["runtime"], runtime.RUNTIME_ID)
        self.assertEqual(result["provenance"]["model"], "fixture-model")
        self.assertEqual(result["provenance"]["provider"], "openai-compatible:test")
        self.assertEqual(captured["endpoint"], self.provider["endpoint"])
        self.assertEqual(captured["timeout"], 5)

    def test_recovery_opaque_readiness_score_is_rejected(self):
        artifact = {
            "source_refs": [], "uncertainties": [], "safety_flags": [],
            "window_start": "2026-08-20", "window_end": "2026-08-22",
            "baseline": {}, "current_signals": {}, "trend": {}, "interventions": [],
            "next_re_evaluation": "2026-08-23T06:00:00Z", "readiness_score": 87,
        }
        with self.assertRaisesRegex(ValueError, "readiness_score"):
            runtime.invoke(self.request("recovery_state"), self.provider, transport=lambda *_: self.response(artifact), environ={})

    def test_p2_direct_plan_patch_is_rejected(self):
        artifact = self.music_artifact()
        artifact["revised_plan"] = {"entity_type": "planned_session"}
        with self.assertRaisesRegex(ValueError, "directly mutate training plans"):
            runtime.invoke(self.request("training_music_profile"), self.provider, transport=lambda *_: self.response(artifact), environ={})

    def test_incomplete_urgent_mental_health_routing_is_rejected(self):
        artifact = {
            "source_refs": [], "uncertainties": [], "safety_flags": ["urgent"],
            "routing_version": 1,
            "concern_summary": "acute concern",
            "observed_signals": [],
            "functioning_course": {},
            "routing_level": "urgent",
            "training_boundaries": {"performance_optimization_paused": False},
            "support_path": {"immediate": False},
            "privacy_minimization": {},
            "confidence": 0.8,
        }
        with self.assertRaisesRegex(ValueError, "urgent routing"):
            runtime.invoke(self.request("mental_health_routing"), self.provider, transport=lambda *_: self.response(artifact), environ={})

    def test_provider_message_must_be_strict_json_not_markdown(self):
        raw = json.dumps({"choices": [{"message": {"content": "```json\n{}\n```"}}]})
        with self.assertRaisesRegex(ValueError, "not valid JSON"):
            runtime.parse_provider_artifact(raw)


if __name__ == "__main__":
    unittest.main()
