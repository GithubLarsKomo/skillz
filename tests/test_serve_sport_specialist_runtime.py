from __future__ import annotations

import json
import sys
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import serve_sport_specialist_runtime as server_module
import sport_specialist_runtime as runtime


class SportSpecialistHttpTests(unittest.TestCase):
    def setUp(self):
        self.provider = {
            "schemaVersion": 1,
            "providerId": "openai-compatible:test",
            "endpoint": "http://provider.internal/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }
        self.token = "0123456789abcdef0123456789abcdef"
        self.provider_calls = []

        def transport(endpoint, body, headers, timeout):
            self.provider_calls.append({"endpoint": endpoint, "body": json.loads(body), "headers": headers, "timeout": timeout})
            artifact = {
                "schema_version": 1,
                "athlete_id": "provider-athlete",
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
            return json.dumps({"choices": [{"message": {"content": json.dumps(artifact)}}]}).encode("utf-8")

        self.server = server_module.make_server(
            "127.0.0.1",
            0,
            self.provider,
            bearer_token=self.token,
            revision="skillz-http-fixture",
            transport=transport,
            environ={},
        )
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_address[1]}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def payload(self):
        descriptor = runtime.REGISTRY["training_music_profile"]
        return {
            "athlete_id": "athlete-1",
            "trigger": "music_profile_requested",
            "artifact_type": "training_music_profile",
            "skill": descriptor["skill"],
            "contract": {"layer": descriptor["layer"], "version": 1, "definition": descriptor["definition"]},
            "snapshot": {"profile": {"sport": "rowing"}},
        }

    def call(self, path: str, *, method: str = "GET", payload=None, token: str | None = None):
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {}
        if payload is not None:
            headers["Content-Type"] = "application/json"
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        request = urllib.request.Request(self.base + path, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=3) as response:
                return response.status, json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read().decode("utf-8"))

    def test_health_is_available_without_bearer_and_exposes_runtime_identity(self):
        status, body = self.call("/healthz")
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertEqual(body["runtime"], runtime.RUNTIME_ID)
        self.assertEqual(body["model"], "fixture-model")
        self.assertEqual(body["skillz_revision"], "skillz-http-fixture")

    def test_wrong_bearer_is_rejected_before_provider_call(self):
        status, body = self.call("/reason", method="POST", payload=self.payload(), token="wrong")
        self.assertEqual(status, 401)
        self.assertEqual(body["error"], "unauthorized")
        self.assertEqual(self.provider_calls, [])

    def test_valid_request_calls_provider_and_returns_canonical_artifact(self):
        status, body = self.call("/reason", method="POST", payload=self.payload(), token=self.token)
        self.assertEqual(status, 200)
        self.assertEqual(body["artifact"]["athlete_id"], "athlete-1")
        self.assertEqual(body["artifact"]["schema_version"], 1)
        self.assertEqual(body["provenance"]["skillz_revision"], "skillz-http-fixture")
        self.assertEqual(len(self.provider_calls), 1)
        provider_user = json.loads(self.provider_calls[0]["body"]["messages"][1]["content"])
        self.assertEqual(provider_user["snapshot"]["profile"]["sport"], "rowing")

    def test_arbitrary_skill_is_rejected_before_provider_call(self):
        payload = self.payload()
        payload["skill"] = "../../anything"
        status, body = self.call("/reason", method="POST", payload=payload, token=self.token)
        self.assertEqual(status, 400)
        self.assertEqual(body["error"], "invalid_runtime_request")
        self.assertEqual(self.provider_calls, [])

    def test_short_configured_runtime_token_is_rejected_at_startup(self):
        with self.assertRaisesRegex(ValueError, "at least 32"):
            server_module.make_server("127.0.0.1", 0, self.provider, bearer_token="short")


if __name__ == "__main__":
    unittest.main()
