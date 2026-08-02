from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import qualify_model_provider as qualifier


class ProviderQualificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = json.loads((ROOT / "benchmarks/capability-interpretation-v1.json").read_text(encoding="utf-8"))
        cls.proposals = json.loads((ROOT / "benchmarks/capability-interpretation-baseline-v1.json").read_text(encoding="utf-8"))
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))

    def test_known_baseline_qualifies(self):
        result = qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index)
        self.assertTrue(result["qualified"])
        self.assertEqual(result["failedCount"], 0)
        self.assertEqual(result["passedCount"], result["caseCount"])

    def test_failed_baseline_is_not_qualified(self):
        proposals = copy.deepcopy(self.proposals)
        proposals["proposals"][0]["proposal"]["intent"]["desiredOutputs"] = []
        result = qualifier.qualify("fixture", "fixture-model", self.benchmark, proposals, self.index)
        self.assertFalse(result["qualified"])
        self.assertGreater(result["failedCount"], 0)

    def test_fingerprints_change_with_content(self):
        baseline = qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index)
        changed_benchmark = copy.deepcopy(self.benchmark)
        changed_benchmark["cases"][0]["sourceText"] += " changed"
        changed = qualifier.qualify("fixture", "fixture-model", changed_benchmark, self.proposals, self.index)
        self.assertNotEqual(baseline["benchmarkSha256"], changed["benchmarkSha256"])
        changed_index = copy.deepcopy(self.index)
        changed_index["skills"][0]["description"] += " changed"
        changed2 = qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, changed_index)
        self.assertNotEqual(baseline["capabilityIndexSha256"], changed2["capabilityIndexSha256"])

    def test_byte_stable(self):
        first = qualifier.render_json(qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index))
        second = qualifier.render_json(qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index))
        self.assertEqual(first, second)

    def test_malformed_index_fails(self):
        bad = copy.deepcopy(self.index)
        bad["schemaVersion"] = 999
        with self.assertRaisesRegex(ValueError, "unsupported capability index schemaVersion"):
            qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, bad)


if __name__ == "__main__":
    unittest.main()
