from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CrossDomainWorkflowE2ETest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {skill["name"]: skill for skill in cls.index["skills"]}
        cls.benchmark = json.loads((ROOT / "benchmarks" / "cross-domain-workflows-e2e-v1.json").read_text(encoding="utf-8"))

    def requires_closure(self, name: str) -> set[str]:
        seen: set[str] = set()
        pending = list(self.skills[name]["requires"])
        while pending:
            dependency = pending.pop()
            if dependency in seen:
                continue
            self.assertIn(dependency, self.skills, f"{name}: missing required skill {dependency}")
            seen.add(dependency)
            pending.extend(self.skills[dependency]["requires"])
        return seen

    def test_scenarios_have_unique_identity_and_distinct_domains(self):
        scenarios = self.benchmark["scenarios"]
        ids = [scenario["id"] for scenario in scenarios]
        domains = [scenario["domain"] for scenario in scenarios]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(domains), len(set(domains)))
        self.assertGreaterEqual(len(scenarios), 10)

    def test_entrypoints_are_supported_evaluated_noncompatibility_surfaces(self):
        for scenario in self.benchmark["scenarios"]:
            entrypoint = self.skills[scenario["entrypoint"]]
            governance = entrypoint["governance"]
            self.assertTrue(entrypoint["invocation"]["userFacing"], scenario["id"])
            self.assertIn(governance["discoverability"], {"public", "advanced"}, scenario["id"])
            self.assertNotEqual(governance["status"], "deprecated", scenario["id"])
            self.assertTrue(entrypoint["evaluation"]["passed"], scenario["id"])
            self.assertTrue(entrypoint["outputs"], scenario["id"])
            self.assertTrue(all(not contract["ambiguous"] for contract in entrypoint["outputContracts"]), scenario["id"])

    def test_every_sequence_is_reachable_from_its_entrypoint_requires_closure(self):
        for scenario in self.benchmark["scenarios"]:
            closure = self.requires_closure(scenario["entrypoint"])
            sequence = scenario["sequence"]
            self.assertEqual(len(sequence), len(set(sequence)), f"{scenario['id']}: duplicate sequence skill")
            for name in sequence:
                self.assertIn(name, closure, f"{scenario['id']}: {name} is outside entrypoint requires closure")
                skill = self.skills[name]
                self.assertNotEqual(skill["governance"]["discoverability"], "compatibility", f"{scenario['id']}: {name}")
                self.assertNotEqual(skill["governance"]["status"], "deprecated", f"{scenario['id']}: {name}")
                self.assertTrue(skill["evaluation"]["passed"], f"{scenario['id']}: {name}")

    def test_behavioral_invariants_are_not_empty_placeholders(self):
        for scenario in self.benchmark["scenarios"]:
            self.assertGreaterEqual(len(scenario["mustPreserve"]), 2, scenario["id"])
            self.assertGreaterEqual(len(scenario["mustNotDo"]), 1, scenario["id"])
            for statement in scenario["mustPreserve"] + scenario["mustNotDo"]:
                self.assertGreaterEqual(len(statement.strip()), 12, scenario["id"])

    def test_shared_delivery_boundaries_remain_at_orchestrator_level(self):
        delegated_workers = {
            "learning-artifact-qa",
            "learning-content-design-system",
            "learning-visual-planner",
            "learning-svg-generator",
            "learning-image-generator",
            "learning-landingpage-renderer",
            "learning-document-delivery",
            "template-presentation-workflow",
        }
        for scenario_id in [
            "youtube-single-video-learning",
            "youtube-playlist-arbitrated-learning",
            "youtube-course-builder",
        ]:
            scenario = next(item for item in self.benchmark["scenarios"] if item["id"] == scenario_id)
            self.assertIn("learning-delivery-workflow", scenario["sequence"])
            self.assertTrue(delegated_workers.isdisjoint(scenario["sequence"]), scenario_id)

    def test_sport_benchmark_cannot_regress_to_legacy_programming_facade(self):
        scenario = next(item for item in self.benchmark["scenarios"] if item["id"] == "sport-longitudinal-adaptation-loop")
        self.assertNotIn("sport-training-programming", scenario["sequence"])
        self.assertEqual(self.skills["sport-training-programming"]["governance"]["discoverability"], "compatibility")
        self.assertEqual(self.skills["sport-training-programming"]["governance"]["replacedBy"], "sport-training-plan-workflow")

    def test_generic_presentation_benchmark_uses_generic_template_core(self):
        scenario = next(item for item in self.benchmark["scenarios"] if item["id"] == "template-presentation-production")
        self.assertEqual(scenario["entrypoint"], "template-presentation-workflow")
        self.assertEqual(
            set(scenario["sequence"]),
            {
                "presentation-template-profiler",
                "presentation-language-rewriter",
                "presentation-layout-qa",
                "presentation-render-verifier",
            },
        )

    def test_contract_benchmark_preserves_compatibility_entrypoint_and_canonical_state_machine(self):
        scenario = next(item for item in self.benchmark["scenarios"] if item["id"] == "contract-lifecycle-to-final-gate")
        self.assertEqual(scenario["entrypoint"], "contract-workflow")
        self.assertIn("contract-matter-workflow", scenario["sequence"])
        self.assertIn("contract-matter-workflow", self.skills["contract-workflow"]["requires"])


if __name__ == "__main__":
    unittest.main()
