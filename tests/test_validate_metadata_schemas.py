from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_metadata_schemas", ROOT / "scripts" / "validate_metadata_schemas.py")
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class MetadataSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index_schema = json.loads((ROOT / "schemas" / "skill-capability-index-v1.schema.json").read_text())
        cls.query_schema = json.loads((ROOT / "schemas" / "capability-query-output-v1.schema.json").read_text())
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text())

    def test_current_index_validates(self):
        self.assertEqual([], module.validate(self.index, self.index_schema))

    def test_missing_required_field_fails_with_path(self):
        data = copy.deepcopy(self.index)
        del data["skills"][0]["description"]
        errors = module.validate(data, self.index_schema)
        self.assertTrue(any("$.skills[0].description: missing required property" in item for item in errors))

    def test_wrong_evaluation_mode_fails(self):
        data = copy.deepcopy(self.index)
        data["skills"][0]["evaluation"]["mode"] = "experimental"
        errors = module.validate(data, self.index_schema)
        self.assertTrue(any("$.skills[0].evaluation.mode" in item and "unsupported value" in item for item in errors))

    def test_malformed_output_contract_fails(self):
        data = copy.deepcopy(self.index)
        data["skills"][0]["outputContracts"][0]["ambiguous"] = "no"
        errors = module.validate(data, self.index_schema)
        self.assertTrue(any("$.skills[0].outputContracts[0].ambiguous" in item and "expected type" in item for item in errors))

    def test_unsupported_schema_version_fails(self):
        data = copy.deepcopy(self.index)
        data["schemaVersion"] = 2
        errors = module.validate(data, self.index_schema)
        self.assertTrue(any("$.schemaVersion" in item and "expected constant 1" in item for item in errors))

    def test_query_list_shape_validates(self):
        self.assertEqual([], module.validate({"matches": ["a", "b"], "count": 2}, self.query_schema))

    def test_query_single_skill_shape_validates(self):
        self.assertEqual([], module.validate(self.index["skills"][0], self.query_schema))

    def test_skill_discovery_shape_validates(self):
        payload = {
            "schemaVersion": 1,
            "mode": "entrypoints",
            "query": "medical",
            "count": 1,
            "categories": [
                {
                    "category": "regulated-engineering",
                    "skills": [
                        {
                            "name": "medical-device-regulatory-strategy",
                            "description": "Regulatory strategy entrypoint",
                            "userFacing": True,
                        }
                    ],
                }
            ],
        }
        self.assertEqual([], module.validate(payload, self.query_schema))

    def test_min_length_is_enforced(self):
        errors = module.validate("", {"type": "string", "minLength": 1})
        self.assertTrue(any("minLength 1" in item for item in errors))
        self.assertEqual([], module.validate("x", {"type": "string", "minLength": 1}))

    def test_min_items_is_enforced(self):
        errors = module.validate([], {"type": "array", "minItems": 1, "items": {"type": "string"}})
        self.assertTrue(any("minItems 1" in item for item in errors))
        self.assertEqual([], module.validate(["x"], {"type": "array", "minItems": 1, "items": {"type": "string"}}))

    def test_number_minimum_and_maximum_are_enforced(self):
        schema = {"type": "number", "minimum": 0, "maximum": 1}
        self.assertEqual([], module.validate(0.4, schema))
        self.assertTrue(any("less than minimum" in item for item in module.validate(-0.1, schema)))
        self.assertTrue(any("greater than maximum" in item for item in module.validate(1.1, schema)))
        self.assertTrue(any("expected type" in item for item in module.validate(True, schema)))


if __name__ == "__main__":
    unittest.main()
