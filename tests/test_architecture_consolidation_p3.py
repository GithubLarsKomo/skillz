from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ArchitectureConsolidationP3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {skill["name"]: skill for skill in cls.index["skills"]}
        cls.benchmark = json.loads((ROOT / "benchmarks" / "cross-domain-workflows-e2e-v1.json").read_text(encoding="utf-8"))

    def test_capability_health_remains_complete_after_benchmark_governance_addition(self):
        self.assertGreaterEqual(self.index["skillCount"], 281)
        self.assertGreaterEqual(self.index["entrypointCount"], 231)
        counts = self.index["discoverabilityCounts"]
        self.assertGreaterEqual(counts["public"], 229)
        self.assertGreaterEqual(counts["advanced"], 2)
        self.assertGreaterEqual(counts["internal"], 48)
        self.assertGreaterEqual(counts["compatibility"], 2)
        self.assertEqual(sum(counts.values()), self.index["skillCount"])
        self.assertEqual(self.index["evaluationSuiteCount"], self.index["skillCount"])
        self.assertEqual(self.index["evaluatedSkillCount"], self.index["skillCount"])
        self.assertEqual(self.index["evaluatedEntrypointCount"], self.index["entrypointCount"])
        self.assertTrue(self.index["evaluationCoverageComplete"])
        self.assertTrue(self.index["evaluationPassed"])
        self.assertEqual(self.index["evaluationErrorCount"], 0)

    def test_workflow_benchmark_authoring_is_internal_evaluated_governance_worker(self):
        skill = self.skills["workflow-benchmark-authoring"]
        self.assertFalse(skill["invocation"]["userFacing"])
        self.assertEqual(skill["governance"]["discoverability"], "internal")
        self.assertNotEqual(skill["governance"]["status"], "deprecated")
        self.assertTrue(skill["evaluation"]["passed"])
        self.assertEqual(skill["evaluation"]["caseCount"], 3)
        self.assertEqual(skill["evaluation"]["recordedResultCount"], 3)
        self.assertEqual(
            set(skill["requires"]),
            {"skill-evaluation-suite-authoring", "artifact-contract-normalizer"},
        )

    def test_new_governance_outputs_are_unambiguous(self):
        skill = self.skills["workflow-benchmark-authoring"]
        self.assertEqual(
            set(skill["outputs"]),
            {
                "workflow-benchmark-spec.json",
                "workflow-benchmark-regression.py",
                "workflow-benchmark-authoring-report.md",
            },
        )
        self.assertTrue(all(not contract["ambiguous"] for contract in skill["outputContracts"]))
        all_contracts = [contract for item in self.index["skills"] for contract in item["outputContracts"]]
        self.assertFalse(any(contract["ambiguous"] for contract in all_contracts))

    def test_cross_domain_benchmark_covers_broad_nonregulated_workflows(self):
        domains = {scenario["domain"] for scenario in self.benchmark["scenarios"]}
        expected = {
            "software-performance",
            "frontend-design",
            "contract-lifecycle",
            "person-research",
            "presentation",
            "youtube-single",
            "youtube-playlist",
            "youtube-course",
            "sport-athlete-management",
            "thought-to-concept",
            "purchase-decision",
        }
        self.assertTrue(expected.issubset(domains))


if __name__ == "__main__":
    unittest.main()
