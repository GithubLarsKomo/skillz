from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_capability_pipeline.py"
COMPILER = ROOT / "scripts" / "compile_capability_intent.py"
RESOLVER = ROOT / "scripts" / "resolve_capabilities.py"


def run_script(script: Path, *args: str, stdin: str | None = None):
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
    )


class CapabilityPipelineCliTests(unittest.TestCase):
    def write_intent(self, payload: dict) -> Path:
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        json.dump(payload, handle)
        handle.close()
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        return Path(handle.name)

    def test_successful_pipeline_matches_manual_composition(self):
        intent = {"schemaVersion": 1, "requiredDependencies": ["iterate-software-projects"]}
        path = self.write_intent(intent)
        pipeline = run_script(SCRIPT, str(path), "--json")
        self.assertEqual(pipeline.returncode, 0, pipeline.stderr)

        compiled = run_script(COMPILER, str(path))
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        request = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        request.write(compiled.stdout)
        request.close()
        self.addCleanup(lambda: Path(request.name).unlink(missing_ok=True))
        resolved = run_script(RESOLVER, "--request", request.name, "--json")
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertEqual(pipeline.stdout, resolved.stdout)

    def test_valid_empty_candidate_set_succeeds(self):
        intent = {
            "schemaVersion": 1,
            "requiredDependencies": ["iterate-software-projects"],
            "portableFiles": "forbidden",
            "allowedEvaluationModes": ["rubric"],
        }
        result = run_script(SCRIPT, str(self.write_intent(intent)), "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["candidateCount"], 0)

    def test_compiler_stage_diagnostic_is_distinct(self):
        result = run_script(SCRIPT, "-", "--json", stdin='{"schemaVersion":2}')
        self.assertEqual(result.returncode, 2)
        self.assertIn("compiler stage:", result.stderr)

    def test_resolver_stage_diagnostic_is_distinct(self):
        result = run_script(
            SCRIPT,
            "-",
            "--json",
            stdin='{"schemaVersion":1,"desiredOutputs":["definitely-not-known.json"]}',
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("resolver stage:", result.stderr)
        self.assertIn("unknown output", result.stderr)

    def test_stdin_and_file_are_byte_equivalent_and_stable(self):
        intent = {
            "schemaVersion": 1,
            "requiredDependencies": ["iterate-software-projects", "iterate-software-projects"],
            "allowedEvaluationModes": ["compatibility", "compatibility"],
        }
        serialized = json.dumps(intent)
        path = self.write_intent(intent)
        file_run = run_script(SCRIPT, str(path), "--json")
        stdin_run = run_script(SCRIPT, "-", "--json", stdin=serialized)
        repeat = run_script(SCRIPT, str(path), "--json")
        self.assertEqual(file_run.returncode, 0, file_run.stderr)
        self.assertEqual(file_run.stdout, stdin_run.stdout)
        self.assertEqual(file_run.stdout, repeat.stdout)


if __name__ == "__main__":
    unittest.main()
