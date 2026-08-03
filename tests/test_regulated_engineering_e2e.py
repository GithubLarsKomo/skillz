import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RegulatedEngineeringE2ETest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.index=json.loads((ROOT/"docs/skill-capability-index.json").read_text(encoding="utf-8")); cls.skills={s["name"]:s for s in cls.index["skills"]}
 def test_all_e2e_sequences_resolve(self):
  bench=json.loads((ROOT/"benchmarks/regulated-engineering-e2e-v1.json").read_text())
  for scenario in bench["scenarios"]:
   for name in scenario["sequence"]: self.assertIn(name,self.skills,f"{scenario['id']}: {name}")
   self.assertTrue(scenario["mustPreserve"])
 def test_routing_benchmark_targets_exist_and_are_specific(self):
  bench=json.loads((ROOT/"benchmarks/regulated-engineering-routing-v1.json").read_text())
  for case in bench["cases"]:
   target=self.skills[case["expectedSkill"]]; self.assertTrue(target.get("description"))
   for companion in case.get("companionSkills",[]): self.assertIn(companion,self.skills)
   for other in case.get("notPrimary",[]): self.assertIn(other,self.skills)
 def test_regulatory_strategy_is_thin_orchestrator(self):
  req=set(self.skills["medical-device-regulatory-strategy"]["requires"]); self.assertTrue({"eu-mdr-ivdr-regulatory-specialist","fda-medical-device-ivd-regulatory-specialist","large-work-wayfinder"}.issubset(req))
 def test_audits_share_compliance_review_core(self):
  for name in ["iso13485-qms-audit","iso27001-isms-audit"]: self.assertIn("two-axis-compliance-review",self.skills[name]["requires"])
if __name__=="__main__": unittest.main()
