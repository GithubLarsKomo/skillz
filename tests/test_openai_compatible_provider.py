from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_model_interpretation_request as request_builder
import openai_compatible_provider as provider
import qualify_model_provider as qualifier
import score_capability_interpretations as scorer


class OpenAICompatibleProviderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
        cls.benchmark = scorer.load_json(ROOT / "benchmarks" / "capability-interpretation-v1.json")
        cls.proposals = scorer.load_json(ROOT / "benchmarks" / "capability-interpretation-baseline-v1.json")
        cls.config = {
            "schemaVersion": 1,
            "providerId": "openai-compatible:test",
            "endpoint": "http://localhost:11434/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }
        cls.qualification = qualifier.qualify(
            cls.config["providerId"], cls.config["modelId"], cls.benchmark, cls.proposals, cls.index
        )
        cls.request = request_builder.build_request("Create the review decision artifact.", cls.index)
        cls.proposal = cls.proposals["proposals"][0]["proposal"]

    def response_bytes(self, proposal=None):
        payload = self.proposal if proposal is None else proposal
        return json.dumps({"choices": [{"message": {"content": json.dumps(payload)}}]}).encode("utf-8")

    def test_request_rendering_is_deterministic(self):
        a = provider.render_request_body(self.request, self.config)
        b = provider.render_request_body(self.request, self.config)
        self.assertEqual(provider.canonical_json(a), provider.canonical_json(b))
        self.assertEqual(a["model"], self.config["modelId"])
        self.assertEqual(a["temperature"], 0)

    def test_auth_header_omitted_without_env_name(self):
        headers = provider.build_headers(self.config, {})
        self.assertNotIn("Authorization", headers)

    def test_auth_header_uses_named_environment_variable(self):
        config = dict(self.config, apiKeyEnv="TEST_PROVIDER_KEY")
        headers = provider.build_headers(config, {"TEST_PROVIDER_KEY": "secret-token"})
        self.assertEqual(headers["Authorization"], "Bearer secret-token")
        self.assertNotIn("secret-token", provider.canonical_json(config))

    def test_missing_named_api_key_fails(self):
        config = dict(self.config, apiKeyEnv="TEST_PROVIDER_KEY")
        with self.assertRaisesRegex(ValueError, "missing API key environment variable"):
            provider.build_headers(config, {})

    def test_qualification_mismatch_blocks_transport(self):
        called = False
        def transport(*args):
            nonlocal called
            called = True
            return self.response_bytes()
        bad = dict(self.qualification, modelId="different-model")
        with self.assertRaisesRegex(ValueError, "modelId does not match"):
            provider.invoke(self.request, self.config, bad, self.benchmark, self.index, transport=transport, environ={})
        self.assertFalse(called)

    def test_stale_index_qualification_blocks_transport(self):
        stale_index = json.loads(json.dumps(self.index))
        stale_index["skillCount"] = stale_index["skillCount"] + 1
        with self.assertRaisesRegex(ValueError, "capability-index fingerprint"):
            provider.verify_qualification(self.config, self.qualification, self.benchmark, stale_index)

    def test_http_failure_mapping_from_transport_is_preserved(self):
        def transport(*args):
            raise ValueError("provider HTTP error: 503")
        with self.assertRaisesRegex(ValueError, "provider HTTP error: 503"):
            provider.invoke(self.request, self.config, self.qualification, self.benchmark, self.index, transport=transport, environ={})

    def test_malformed_provider_response_rejected(self):
        with self.assertRaisesRegex(ValueError, "does not contain choices"):
            provider.parse_provider_response(b'{"unexpected":true}')

    def test_forbidden_control_fields_rejected_by_existing_adapter(self):
        bad = dict(self.proposal, reviewRequired=False)
        with self.assertRaises(ValueError):
            provider.parse_provider_response(self.response_bytes(bad))

    def test_normalized_proposal_output_is_byte_stable(self):
        first = provider.canonical_json(provider.parse_provider_response(self.response_bytes()))
        second = provider.canonical_json(provider.parse_provider_response(self.response_bytes()))
        self.assertEqual(first, second)

    def test_model_identity_is_bound_to_provider_config(self):
        spoofed = dict(self.proposal, model="spoofed-model")
        bound = provider.bind_model_identity(provider.parse_provider_response(self.response_bytes(spoofed)), self.config["modelId"])
        self.assertEqual(bound["model"], self.config["modelId"])

    def test_invoke_passes_expected_transport_contract(self):
        captured = {}
        def transport(endpoint, body, headers, timeout):
            captured.update(endpoint=endpoint, body=body, headers=headers, timeout=timeout)
            return self.response_bytes()
        proposal = provider.invoke(
            self.request, self.config, self.qualification, self.benchmark, self.index,
            transport=transport, environ={}
        )
        expected = dict(self.proposal, model=self.config["modelId"])
        self.assertEqual(proposal, expected)
        self.assertEqual(captured["endpoint"], self.config["endpoint"])
        self.assertEqual(captured["timeout"], 5)
        self.assertEqual(captured["headers"]["Content-Type"], "application/json")


if __name__ == "__main__":
    unittest.main()
