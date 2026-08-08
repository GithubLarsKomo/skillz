import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FieldActionAuthorityFinalizationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {skill["name"]: skill for skill in cls.index["skills"]}

    def test_finalizers_are_jurisdiction_specific_downstream_workers(self):
        effectiveness = self.skills["medical-device-field-action-effectiveness"]
        fda = self.skills["fda-recall-status-termination"]
        ivdr = self.skills["ivdr-fsca-status-final-reporting"]

        self.assertIn("medical-device-field-action-effectiveness", fda["requires"])
        self.assertIn("fda-corrections-removals", fda["requires"])
        self.assertIn("medical-device-field-action-effectiveness", ivdr["requires"])
        self.assertIn("ivdr-field-safety-corrective-action", ivdr["requires"])

        self.assertIn("fda-recall-status-termination", effectiveness["dependents"])
        self.assertIn("ivdr-fsca-status-final-reporting", effectiveness["dependents"])

        # Jurisdiction-specific finalizers must not contaminate the opposite market path.
        self.assertNotIn("ivdr-field-safety-corrective-action", fda["requires"])
        self.assertNotIn("ivdr-fsca-status-final-reporting", fda["requires"])
        self.assertNotIn("fda-corrections-removals", ivdr["requires"])
        self.assertNotIn("fda-recall-status-termination", ivdr["requires"])

        # Upstream regulatory and execution decisions cannot wait for final reporting/authority closure.
        for upstream in [
            "fda-corrections-removals",
            "ivdr-pms-vigilance",
            "ivdr-field-safety-corrective-action",
            "medical-device-field-action-communication",
            "medical-device-field-action-physical-execution",
            "medical-device-field-action-effectiveness",
        ]:
            self.assertNotIn("fda-recall-status-termination", self.skills[upstream]["requires"])
            self.assertNotIn("ivdr-fsca-status-final-reporting", self.skills[upstream]["requires"])

    def test_finalizers_have_complete_hard_evaluations(self):
        for worker in ["fda-recall-status-termination", "ivdr-fsca-status-final-reporting"]:
            evaluation = json.loads((ROOT / "skills" / worker / "tests" / "evaluation.json").read_text(encoding="utf-8"))
            self.assertEqual(len(evaluation["cases"]), 4, worker)
            self.assertEqual(self.skills[worker]["evaluation"]["caseCount"], 4, worker)
            self.assertEqual(self.skills[worker]["evaluation"]["recordedResultCount"], 4, worker)
            ids = {case["id"] for case in evaluation["cases"]}
            self.assertTrue({"happy-path", "edge-case", "failure-case"}.issubset(ids), worker)
            for case in evaluation["cases"]:
                result = ROOT / "skills" / worker / "tests" / "results" / f"{case['id']}.json"
                self.assertTrue(result.exists(), f"{worker}: {case['id']}")
                recorded = json.loads(result.read_text(encoding="utf-8"))
                self.assertEqual(recorded["overall"], "pass", f"{worker}: {case['id']}")

    def test_external_authority_states_cannot_be_simulated(self):
        fda_text = (ROOT / "skills" / "fda-recall-status-termination" / "SKILL.md").read_text(encoding="utf-8")
        ivdr_text = (ROOT / "skills" / "ivdr-fsca-status-final-reporting" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Completed ≠ terminated", fda_text)
        self.assertIn("Request ≠ decision", fda_text)
        self.assertIn("FDA state needs FDA evidence", fda_text)
        self.assertIn("806 amendment stays separate", fda_text)
        self.assertIn("New safety facts bypass termination", fda_text)

        self.assertIn("Manufacturer final ≠ authority closed", ivdr_text)
        self.assertIn("No non-reportable shortcut", ivdr_text)
        self.assertIn("Authority silence is not acceptance", ivdr_text)
        self.assertIn("Notified Body and Authority states stay distinct", ivdr_text)
        self.assertIn("New safety facts bypass finalization", ivdr_text)

    def test_authority_finalization_benchmark_resolves(self):
        bench = json.loads((ROOT / "benchmarks" / "regulated-engineering-field-action-authority-finalization-v1.json").read_text(encoding="utf-8"))
        self.assertEqual(len(bench["scenarios"]), 2)
        for scenario in bench["scenarios"]:
            for skill in scenario["sequence"]:
                self.assertIn(skill, self.skills, scenario["id"])
            self.assertGreaterEqual(len(scenario["mustPreserve"]), 6)


if __name__ == "__main__":
    unittest.main()
