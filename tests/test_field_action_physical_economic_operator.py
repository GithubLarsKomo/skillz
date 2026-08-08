import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FieldActionPhysicalEconomicOperatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {s["name"]: s for s in cls.index["skills"]}

    def test_benchmark_sequences_resolve(self):
        bench = json.loads((ROOT / "benchmarks/regulated-engineering-field-action-physical-v1.json").read_text(encoding="utf-8"))
        for scenario in bench["scenarios"]:
            self.assertTrue(scenario["mustPreserve"], scenario["id"])
            for name in scenario["sequence"]:
                self.assertIn(name, self.skills, f"{scenario['id']}: {name}")

    def test_physical_execution_is_hard_downstream_but_not_regulatory_gate(self):
        physical = self.skills["medical-device-field-action-physical-execution"]
        effectiveness = self.skills["medical-device-field-action-effectiveness"]
        communication = self.skills["medical-device-field-action-communication"]
        ivdr = self.skills["ivdr-pms-vigilance"]
        fsca = self.skills["ivdr-field-safety-corrective-action"]
        fda806 = self.skills["fda-corrections-removals"]

        self.assertIn("medical-device-field-action-communication", physical["requires"])
        self.assertIn("medical-device-field-action-physical-execution", effectiveness["requires"])

        for upstream in [ivdr, fsca, fda806]:
            self.assertNotIn("medical-device-field-action-physical-execution", upstream["requires"])
            self.assertNotIn("medical-device-field-action-effectiveness", upstream["requires"])

        communication_contract = next(
            c for c in communication["outputContracts"]
            if c["output"] == "field-action-communication-state.json"
        )
        self.assertIn("medical-device-field-action-physical-execution", communication_contract["consumerSkills"])
        self.assertIn("medical-device-field-action-effectiveness", communication_contract["consumerSkills"])

        disposition_contract = next(
            c for c in physical["outputContracts"]
            if c["output"] == "field-action-disposition-evidence.json"
        )
        self.assertEqual(disposition_contract["consumerSkills"], ["medical-device-field-action-effectiveness"])

    def test_ivdr_economic_operator_sidecar_does_not_contaminate_generic_execution(self):
        eo = self.skills["ivdr-economic-operator-postmarket-propagation"]
        communication = self.skills["medical-device-field-action-communication"]
        physical = self.skills["medical-device-field-action-physical-execution"]
        effectiveness = self.skills["medical-device-field-action-effectiveness"]
        fda806 = self.skills["fda-corrections-removals"]

        self.assertIn("regulated-product-context", eo["requires"])
        self.assertIn("regulatory-evidence-traceability", eo["requires"])
        self.assertIn("quality-record-integrity", eo["requires"])

        for generic_worker in [communication, physical, effectiveness, fda806]:
            self.assertNotIn("ivdr-economic-operator-postmarket-propagation", generic_worker["requires"])

    def test_new_workers_have_four_recorded_hardness_cases(self):
        for worker in [
            "medical-device-field-action-physical-execution",
            "ivdr-economic-operator-postmarket-propagation",
        ]:
            evaluation = json.loads((ROOT / "skills" / worker / "tests" / "evaluation.json").read_text(encoding="utf-8"))
            self.assertEqual(len(evaluation["cases"]), 4, worker)
            self.assertEqual(self.skills[worker]["evaluation"]["caseCount"], 4, worker)
            self.assertEqual(self.skills[worker]["evaluation"]["recordedResultCount"], 4, worker)
            ids = {case["id"] for case in evaluation["cases"]}
            self.assertTrue({"happy-path", "edge-case", "failure-case"}.issubset(ids), worker)
            for case in evaluation["cases"]:
                self.assertTrue((ROOT / "skills" / worker / "tests" / "results" / f"{case['id']}.json").exists(), worker)

    def test_hardness_anchors_are_present(self):
        physical_text = (ROOT / "skills" / "medical-device-field-action-physical-execution" / "SKILL.md").read_text(encoding="utf-8")
        eo_text = (ROOT / "skills" / "ivdr-economic-operator-postmarket-propagation" / "SKILL.md").read_text(encoding="utf-8")
        effectiveness_text = (ROOT / "skills" / "medical-device-field-action-effectiveness" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("RMA ≠ return", physical_text)
        self.assertIn("Evidence preservation precedes destructive action", physical_text)
        self.assertIn("Correction performed ≠ correction verified", physical_text)
        self.assertIn("Third-party custody is still custody", physical_text)
        self.assertIn("Serious risk bypasses manufacturer response", eo_text)
        self.assertIn("Forwarded ≠ propagated", eo_text)
        self.assertIn("Own register remains own evidence", eo_text)
        self.assertIn("Physical execution evidence is authoritative for unit state", effectiveness_text)


if __name__ == "__main__":
    unittest.main()
