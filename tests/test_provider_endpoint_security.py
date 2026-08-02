from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import openai_compatible_provider as provider


class ProviderEndpointSecurityTests(unittest.TestCase):
    def config(self, endpoint: str) -> dict:
        return {
            "schemaVersion": 1,
            "providerId": "endpoint-security-test",
            "endpoint": endpoint,
            "modelId": "fixture-model",
            "apiKeyEnv": "CAPABILITY_PROVIDER_API_KEY",
            "timeoutSeconds": 60,
        }

    def test_plain_http_and_https_endpoints_are_allowed(self):
        for endpoint in (
            "http://localhost:11434/v1/chat/completions",
            "https://provider.example/v1/chat/completions",
            "https://provider.example:8443/custom/path",
        ):
            with self.subTest(endpoint=endpoint):
                self.assertEqual(provider.validate_config(self.config(endpoint))["endpoint"], endpoint)

    def test_url_userinfo_is_rejected(self):
        for endpoint in (
            "https://user@provider.example/v1/chat/completions",
            "https://user:password@provider.example/v1/chat/completions",
        ):
            with self.subTest(endpoint=endpoint):
                with self.assertRaisesRegex(ValueError, "must not contain URL credentials"):
                    provider.validate_config(self.config(endpoint))

    def test_query_parameters_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "must not contain query parameters"):
            provider.validate_config(self.config("https://provider.example/v1/chat/completions?api_key=top-secret"))

    def test_fragments_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "must not contain a fragment"):
            provider.validate_config(self.config("https://provider.example/v1/chat/completions#secret"))

    def test_hostname_and_port_are_validated(self):
        with self.assertRaisesRegex(ValueError, "must include a hostname"):
            provider.validate_config(self.config("https:///v1/chat/completions"))
        with self.assertRaisesRegex(ValueError, "invalid port"):
            provider.validate_config(self.config("https://provider.example:not-a-port/v1/chat/completions"))

    def test_invalid_endpoint_blocks_transport_before_other_runtime_checks(self):
        called = False

        def transport(*args):
            nonlocal called
            called = True
            return b"{}"

        config = self.config("https://user:password@provider.example/v1/chat/completions")
        with self.assertRaisesRegex(ValueError, "URL credentials"):
            provider.invoke({}, config, {}, {}, {}, transport=transport, environ={})
        self.assertFalse(called)


if __name__ == "__main__":
    unittest.main()
