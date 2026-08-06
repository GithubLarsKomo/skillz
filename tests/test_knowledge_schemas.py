import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_metadata_schemas", ROOT / "scripts" / "validate_metadata_schemas.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)


def schema(name: str) -> dict:
    return json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))


class KnowledgeSchemaTests(unittest.TestCase):
    def assertValid(self, value, schema_name):
        self.assertEqual(mod.validate(value, schema(schema_name)), [])

    def assertInvalid(self, value, schema_name):
        self.assertTrue(mod.validate(value, schema(schema_name)))

    def test_knowledge_artifact_contract(self):
        good = {
            "schemaVersion": 1,
            "id": "D1",
            "artifactType": "decision",
            "title": "Decision",
            "content": "Use provider-neutral contracts.",
            "metadata": {"owner": "team"},
            "links": [{"type": "supports", "targetId": "R1"}],
            "provenance": [{"sourceRef": "decision-record", "observedAt": "2026-08-03T09:00:00Z"}],
            "lifecycle": {"state": "active"},
        }
        self.assertValid(good, "knowledge-artifact-v1.schema.json")
        bad_relation = dict(good)
        bad_relation["links"] = [{"type": "invented-relation", "targetId": "R1"}]
        self.assertInvalid(bad_relation, "knowledge-artifact-v1.schema.json")
        bad_lifecycle = dict(good)
        bad_lifecycle["lifecycle"] = {"state": "deleted-by-view"}
        self.assertInvalid(bad_lifecycle, "knowledge-artifact-v1.schema.json")

    def test_knowledge_view_contract(self):
        good = {
            "schemaVersion": 1,
            "id": "active-decisions",
            "sourceScopes": ["project:alpha"],
            "filters": [{"field": "artifactType", "eq": "decision"}],
            "includeStates": ["active"],
            "artifactIds": ["D1"],
            "rows": [{"artifactId": "D1", "title": "Decision"}],
            "asOf": "snapshot-1",
        }
        self.assertValid(good, "knowledge-view-v1.schema.json")
        bad = dict(good)
        bad["includeStates"] = ["silently-resolved"]
        self.assertInvalid(bad, "knowledge-view-v1.schema.json")

    def test_knowledge_map_contract(self):
        good = {
            "schemaVersion": 1,
            "nodes": [
                {"id": "D1", "type": "decision", "label": "Decision", "sourceRefs": ["D1"]},
                {"id": "R1", "type": "research-note", "label": "Research", "sourceRefs": ["R1"]},
            ],
            "edges": [
                {"id": "E1", "from": "D1", "to": "R1", "type": "supports", "sourceRefs": ["D1"]}
            ],
            "groups": [],
        }
        self.assertValid(good, "knowledge-map-v1.schema.json")
        bad = dict(good)
        bad["edges"] = [{"id": "E1", "from": "D1", "type": "supports", "sourceRefs": ["D1"]}]
        self.assertInvalid(bad, "knowledge-map-v1.schema.json")

    def test_memory_candidate_handoff_contract(self):
        good = {
            "schemaVersion": 1,
            "sourceSkill": "ivdr-device-classification",
            "asOf": "2026-08-06T20:00:00Z",
            "candidates": [
                {
                    "kind": "validated-pattern",
                    "statement": "Fix specimen type before applying the classification rule tree.",
                    "scope": "project-family:example-ivd",
                    "sourceRefs": ["classification-assessment:sha256:abc"],
                    "confidence": "high",
                    "authorityClass": "interpretation",
                    "observedAt": "2026-08-06T20:00:00Z",
                    "reviewAfter": "2027-02-06",
                    "expiresAt": None,
                }
            ],
            "rejectedRunOnly": [],
        }
        self.assertValid(good, "memory-candidate-handoff-v1.schema.json")

        missing_provenance = json.loads(json.dumps(good))
        missing_provenance["candidates"][0]["sourceRefs"] = []
        self.assertInvalid(missing_provenance, "memory-candidate-handoff-v1.schema.json")

        invented_kind = json.loads(json.dumps(good))
        invented_kind["candidates"][0]["kind"] = "current-task-status"
        self.assertInvalid(invented_kind, "memory-candidate-handoff-v1.schema.json")


if __name__ == "__main__":
    unittest.main()
