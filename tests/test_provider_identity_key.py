from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import provider_identity_key


class ProviderIdentityKeyTests(unittest.TestCase):
    def test_key_is_deterministic_and_filesystem_safe(self):
        provider_id = "openai-compatible:test"
        model_id = "hf.co/example/model:Q4_K_M"
        first = provider_identity_key.identity_key(provider_id, model_id)
        second = provider_identity_key.identity_key(provider_id, model_id)
        self.assertEqual(first, second)
        self.assertRegex(first, r"^[0-9a-f]{24}$")

    def test_exact_identity_changes_change_key(self):
        base = provider_identity_key.identity_key("provider", "org/model:tag")
        self.assertNotEqual(base, provider_identity_key.identity_key("provider-2", "org/model:tag"))
        self.assertNotEqual(base, provider_identity_key.identity_key("provider", "org/model:tag-2"))

    def test_empty_identity_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "provider id must be non-empty"):
            provider_identity_key.identity_key("", "model")
        with self.assertRaisesRegex(ValueError, "model id must be non-empty"):
            provider_identity_key.identity_key("provider", " ")


if __name__ == "__main__":
    unittest.main()
