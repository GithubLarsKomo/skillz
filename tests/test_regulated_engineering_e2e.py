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
        followup = self.skills["medical-device-complaint-customer-followup"]
        router = self.skills["medical-device-complaint-regulatory-routing"]
        fda = self.skills["fda-complaint-mdr-reportability"]
        ivdr = self.skills["ivdr-pms-vigilance"]

        self.assertIn("medical-device-customer-contact-intake", complaint["requires"])
        self.assertIn("medical-device-complaint-handling", followup["requires"])
        self.assertIn("medical-device-complaint-handling", router["requires"])
        self.assertIn("medical-device-complaint-customer-followup", router["requires"])
        self.assertIn("fda-complaint-mdr-reportability", router["requires"])
        self.assertIn("ivdr-pms-vigilance", router["requires"])

        # Market specialists stay reusable for controlled non-router event/signal sources.
        self.assertNotIn("medical-device-complaint-regulatory-routing", fda["requires"])
        self.assertNotIn("medical-device-complaint-regulatory-routing", ivdr["requires"])

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
        followup_contract = next(
            c
            for c in followup["outputContracts"]
            if c["output"] == "customer-followup-evidence.json"
        )
        fda_return_contract = next(
            c
            for c in fda["outputContracts"]
            if c["output"] == "complaint-regulatory-actions.json"
        )
        ivdr_return_contract = next(
            c
            for c in ivdr["outputContracts"]
            if c["output"] == "vigilance-decision-log.json"
        )

        self.assertEqual(intake_contract["consumerSkills"], ["medical-device-complaint-handling"])
        self.assertIn("medical-device-complaint-regulatory-routing", complaint_contract["consumerSkills"])
        self.assertEqual(followup_contract["consumerSkills"], ["medical-device-complaint-regulatory-routing"])
        self.assertIn("medical-device-complaint-regulatory-routing", fda_return_contract["consumerSkills"])
        self.assertIn("medical-device-complaint-regulatory-routing", ivdr_return_contract["consumerSkills"])

        self.assertNotIn("medical-device-customer-contact-intake", fda["requires"])
        self.assertNotIn("medical-device-customer-contact-intake", ivdr["requires"])
        self.assertNotIn("medical-device-complaint-handling", fda["requires"])
        self.assertNotIn("medical-device-complaint-handling", ivdr["requires"])
        self.assertNotIn("medical-device-complaint-regulatory-routing", followup["requires"])

    def test_customer_followup_reassessment_contract_is_hard_wired(self):
        reassessment_skills = [
            "medical-device-customer-contact-intake",
            "medical-device-complaint-handling",
            "medical-device-complaint-customer-followup",
            "medical-device-complaint-regulatory-routing",
            "fda-complaint-mdr-reportability",
            "ivdr-pms-vigilance",
        ]

        expected_behavior_fragments = {
            "medical-device-customer-contact-intake": "record the follow-up as a separate evidence event",
            "medical-device-complaint-handling": "preserve the historical closure and prior investigation decision",
            "medical-device-complaint-customer-followup": "record the later reply as a new immutable follow-up evidence event",
            "medical-device-complaint-regulatory-routing": "set reassessment-required independently for US and EU",
            "fda-complaint-mdr-reportability": "treat the prior not-reportable decision as historical",
            "ivdr-pms-vigilance": "treat the prior not-reportable and complaint-closure states as historical",
        }

        extra_hardness_cases = {
            "medical-device-complaint-regulatory-routing": "dispatch-ownership-case",
            "fda-complaint-mdr-reportability": "standalone-controlled-event-case",
            "ivdr-pms-vigilance": "non-complaint-signal-case",
        }

        for name in reassessment_skills:
            evaluation = json.loads((ROOT / "skills" / name / "tests" / "evaluation.json").read_text(encoding="utf-8"))
            case = next((c for c in evaluation["cases"] if c["id"] == "reassessment-case"), None)
            self.assertIsNotNone(case, name)
            self.assertGreaterEqual(self.skills[name]["evaluation"]["caseCount"], 4, name)
            self.assertEqual(self.skills[name]["evaluation"]["caseCount"], len(evaluation["cases"]), name)
            self.assertTrue(
                any(expected_behavior_fragments[name] in behavior for behavior in case["requiredBehaviors"]),
                name,
            )
            self.assertTrue((ROOT / "skills" / name / "tests" / "results" / "reassessment-case.json").exists(), name)

            extra_case_id = extra_hardness_cases.get(name)
            if extra_case_id:
                self.assertTrue(any(c["id"] == extra_case_id for c in evaluation["cases"]), name)
                self.assertTrue((ROOT / "skills" / name / "tests" / "results" / f"{extra_case_id}.json").exists(), name)

        router_text = (ROOT / "skills" / "medical-device-complaint-regulatory-routing" / "SKILL.md").read_text(encoding="utf-8")
        complaint_text = (ROOT / "skills" / "medical-device-complaint-handling" / "SKILL.md").read_text(encoding="utf-8")
        followup_text = (ROOT / "skills" / "medical-device-complaint-customer-followup" / "SKILL.md").read_text(encoding="utf-8")
        fda_text = (ROOT / "skills" / "fda-complaint-mdr-reportability" / "SKILL.md").read_text(encoding="utf-8")
        ivdr_text = (ROOT / "skills" / "ivdr-pms-vigilance" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Prior decisions are historical, not immunity", router_text)
        self.assertIn("Complaint-origin Orchestrator", router_text)
        self.assertIn("Customer Follow-up ist ein Evidence-Zulieferer", router_text)
        self.assertIn("reassessment-required", router_text)
        self.assertIn("Closure is not immunity", complaint_text)
        self.assertIn("complaintClosureState=reopened", complaint_text)
        self.assertIn("Follow-up never delays time-critical escalation", followup_text)
        self.assertIn("Evidence preservation precedes destructive support", followup_text)
        self.assertIn("Router is optional provenance, not a prerequisite", fda_text)
        self.assertIn("Non-complaint vigilance remains valid", ivdr_text)


if __name__ == "__main__":
    unittest.main()
