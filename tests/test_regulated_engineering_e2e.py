import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_resolver():
    spec = importlib.util.spec_from_file_location("resolve_capabilities", ROOT / "scripts/resolve_capabilities.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RegulatedEngineeringE2ETest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {s["name"]: s for s in cls.index["skills"]}
        cls.resolver = load_resolver()

    def test_all_e2e_sequences_resolve(self):
        bench = json.loads((ROOT / "benchmarks/regulated-engineering-e2e-v1.json").read_text(encoding="utf-8"))
        for scenario in bench["scenarios"]:
            for name in scenario["sequence"]:
                self.assertIn(name, self.skills, f"{scenario['id']}: {name}")
            self.assertTrue(scenario["mustPreserve"])

    def test_routing_benchmark_resolves_unique_specialist_artifacts(self):
        bench = json.loads((ROOT / "benchmarks/regulated-engineering-routing-v1.json").read_text(encoding="utf-8"))
        for case in bench["cases"]:
            target = self.skills[case["expectedSkill"]]
            self.assertTrue(target.get("description"))
            constraints = self.resolver.normalize_constraints(case["desiredOutputs"], [], [], "irrelevant")
            result = self.resolver.resolve(self.index, constraints)
            self.assertEqual(
                [candidate["name"] for candidate in result["candidates"]],
                [case["expectedSkill"]],
                case["id"],
            )
            for companion in case.get("companionSkills", []):
                self.assertIn(companion, self.skills)
            for other in case.get("notPrimary", []):
                self.assertIn(other, self.skills)
                self.assertNotEqual(other, case["expectedSkill"])

    def test_regulatory_strategy_is_thin_orchestrator(self):
        req = set(self.skills["medical-device-regulatory-strategy"]["requires"])
        self.assertTrue({"eu-mdr-ivdr-regulatory-specialist", "fda-medical-device-ivd-regulatory-specialist", "large-work-wayfinder"}.issubset(req))

    def test_audits_share_compliance_review_core(self):
        for name in ["iso13485-qms-audit", "iso27001-isms-audit"]:
            self.assertIn("two-axis-compliance-review", self.skills[name]["requires"])

    def test_customer_contact_to_vigilance_chain_is_hard_wired(self):
        complaint = self.skills["medical-device-complaint-handling"]
        router = self.skills["medical-device-complaint-regulatory-routing"]
        fda = self.skills["fda-complaint-mdr-reportability"]
        ivdr = self.skills["ivdr-pms-vigilance"]

        self.assertIn("medical-device-customer-contact-intake", complaint["requires"])
        self.assertIn("medical-device-complaint-handling", router["requires"])
        self.assertIn("medical-device-complaint-regulatory-routing", fda["requires"])
        self.assertIn("medical-device-complaint-regulatory-routing", ivdr["requires"])

        intake_contract = next(
            c
            for c in self.skills["medical-device-customer-contact-intake"]["outputContracts"]
            if c["output"] == "complaint-intake-handoff.json"
        )
        complaint_contract = next(
            c
            for c in complaint["outputContracts"]
            if c["output"] == "complaint-regulatory-handoff.json"
        )
        routing_contract = next(
            c
            for c in router["outputContracts"]
            if c["output"] == "complaint-regulatory-routing.json"
        )

        self.assertEqual(intake_contract["consumerSkills"], ["medical-device-complaint-handling"])
        self.assertEqual(complaint_contract["consumerSkills"], ["medical-device-complaint-regulatory-routing"])
        self.assertEqual(
            set(routing_contract["consumerSkills"]),
            {"fda-complaint-mdr-reportability", "ivdr-pms-vigilance"},
        )

        self.assertNotIn("medical-device-customer-contact-intake", fda["requires"])
        self.assertNotIn("medical-device-customer-contact-intake", ivdr["requires"])
        self.assertNotIn("medical-device-complaint-handling", fda["requires"])
        self.assertNotIn("medical-device-complaint-handling", ivdr["requires"])


if __name__ == "__main__":
    unittest.main()
