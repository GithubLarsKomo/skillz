import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RegulatedEngineeringContractsTest(unittest.TestCase):
 def test_contract_schemas_parse_and_are_closed(self):
  for name in ["regulatory-source-evidence-v1.schema.json","compliance-traceability-v1.schema.json","regulated-product-baseline-v1.schema.json"]:
   value=json.loads((ROOT/"contracts"/name).read_text(encoding="utf-8")); self.assertEqual(value["$schema"],"https://json-schema.org/draft/2020-12/schema"); self.assertEqual(value["type"],"object"); self.assertFalse(value.get("additionalProperties",True)); self.assertTrue(value.get("required"))
 def test_source_contract_distinguishes_claim_class_and_freshness(self):
  value=json.loads((ROOT/"contracts/regulatory-source-evidence-v1.schema.json").read_text()); self.assertIn("claimClass",value["required"]); self.assertIn("asOf",value["required"]); self.assertEqual(set(value["properties"]["claimClass"]["enum"]),{"regulation-law","standard","guidance","organizational-policy","interpretation"})
 def test_traceability_has_required_chain_node_types(self):
  value=json.loads((ROOT/"contracts/compliance-traceability-v1.schema.json").read_text()); types=set(value["properties"]["nodes"]["items"]["properties"]["type"]["enum"]); self.assertTrue({"obligation","product-requirement","risk-rationale","implementation-control","verification","evidence","status"}.issubset(types))
if __name__=="__main__": unittest.main()
