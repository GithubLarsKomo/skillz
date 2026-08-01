from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


compiler = load_module("compile_capability_intent", ROOT / "scripts" / "compile_capability_intent.py")
schemas = load_module("validate_metadata_schemas", ROOT / "scripts" / "validate_metadata_schemas.py")


class CompileCapabilityIntentTests(unittest.TestCase):
    def test_happy_path_and_duplicate_normalization(self):
        intent = {
            "schemaVersion": 1,
            "desiredOutputs": ["b.json", "a.json", "a.json"],
            "requiredDependencies": ["z", "a", "z"],
            "allowedEvaluationModes": ["rubric", "none", "rubric"],
            "portableFiles": "required",
        }
        payload = compiler.compile_intent(intent)
        self.assertEqual(payload["outputs"], ["a.json", "b.json"])
        self.assertEqual(payload["dependencies"], ["a", "z"])
        self.assertEqual(payload["evaluationModes"], ["none", "rubric"])

    def test_empty_intent_compiles(self):
        self.assertEqual(
            compiler.compile_intent({"schemaVersion": 1}),
            {"schemaVersion": 1, "outputs": [], "dependencies": [], "evaluationModes": [], "portableFiles": "irrelevant"},
        )

    def test_invalid_inputs_fail(self):
        with self.assertRaisesRegex(ValueError, "unsupported intent schemaVersion"):
            compiler.compile_intent({"schemaVersion": 2})
        with self.assertRaisesRegex(ValueError, "unknown intent field"):
            compiler.compile_intent({"schemaVersion": 1, "freeText": "x"})
        with self.assertRaisesRegex(ValueError, "unsupported evaluation mode"):
            compiler.compile_intent({"schemaVersion": 1, "allowedEvaluationModes": ["mystery"]})

    def test_output_validates_as_resolver_request(self):
        payload = compiler.compile_intent({"schemaVersion": 1, "desiredOutputs": ["x.json"]})
        schema = json.loads((ROOT / "schemas" / "capability-resolver-request-v1.schema.json").read_text())
        self.assertEqual(schemas.validate(payload, schema), [])

    def test_file_and_stdin_are_byte_equivalent(self):
        intent = {"schemaVersion": 1, "desiredOutputs": ["b.json", "a.json"], "portableFiles": "forbidden"}
        raw = json.dumps(intent)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            handle.write(raw)
            path = handle.name
        command = [sys.executable, str(ROOT / "scripts" / "compile_capability_intent.py")]
        file_result = subprocess.run(command + [path], text=True, capture_output=True, check=False)
        stdin_result = subprocess.run(command + ["-"], input=raw, text=True, capture_output=True, check=False)
        self.assertEqual(file_result.returncode, 0)
        self.assertEqual(stdin_result.returncode, 0)
        self.assertEqual(file_result.stdout, stdin_result.stdout)


if __name__ == "__main__":
    unittest.main()
