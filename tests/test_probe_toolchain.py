from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "probe_toolchain.py"
spec = importlib.util.spec_from_file_location("probe_toolchain", SCRIPT)
probe_toolchain = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(probe_toolchain)


def registry() -> dict:
    return {
        "schemaVersion": 1,
        "capabilities": {
            "binary-inspection": {"providers": ["objdump"]},
            "version-control": {"providers": ["git"]},
        },
        "versionArgs": {},
        "profiles": {
            "opaque-system-analysis": ["binary-inspection"],
            "merge-conflict-resolution": ["version-control"],
        },
    }


class ProbeToolchainTests(unittest.TestCase):
    def test_probe_groups_tools_by_capability(self) -> None:
        def which(command: str) -> str | None:
            return "/usr/bin/objdump" if command == "objdump" else None

        with mock.patch.object(probe_toolchain.shutil, "which", side_effect=which), mock.patch.object(
            probe_toolchain, "first_version_line", return_value="objdump 1.0"
        ):
            result = probe_toolchain.probe(registry())

        by_capability = {entry["capability"]: entry for entry in result["capabilities"]}
        self.assertTrue(by_capability["binary-inspection"]["available"])
        self.assertEqual(by_capability["binary-inspection"]["providers"][0]["provider"], "objdump")
        self.assertFalse(by_capability["version-control"]["available"])
        self.assertEqual(result["schemaVersion"], 2)

    def test_profile_limits_probe_without_implying_requirement(self) -> None:
        with mock.patch.object(probe_toolchain.shutil, "which", return_value=None), mock.patch.object(
            probe_toolchain, "first_version_line", return_value=None
        ):
            result = probe_toolchain.probe(registry(), ["version-control"])
        self.assertEqual([item["capability"] for item in result["capabilities"]], ["version-control"])
        self.assertFalse(result["capabilities"][0]["available"])

    def test_main_writes_json_and_reports_missing_requirement(self) -> None:
        fake = {
            "schemaVersion": 2,
            "verifiedAt": "2026-08-02T18:00:00Z",
            "platform": {"system": "Test", "release": "1", "machine": "x"},
            "capabilities": [{"capability": "binary-inspection", "available": False, "providers": []}],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            registry_path = Path(temp_dir) / "registry.json"
            registry_path.write_text(json.dumps(registry()), encoding="utf-8")
            output = Path(temp_dir) / "toolchain.json"
            argv = [
                "probe_toolchain.py",
                "--registry", str(registry_path),
                "--profile", "opaque-system-analysis",
                "--output", str(output),
                "--require", "binary-inspection",
            ]
            with mock.patch.object(probe_toolchain, "probe", return_value=fake), mock.patch("sys.argv", argv):
                code = probe_toolchain.main()
            payload = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(code, 1)
        self.assertEqual(payload["requirements"]["missing"], ["binary-inspection"])
        self.assertEqual(payload["profile"], "opaque-system-analysis")

    def test_requirement_outside_profile_has_distinct_exit_code(self) -> None:
        fake = {
            "schemaVersion": 2,
            "verifiedAt": "2026-08-02T18:00:00Z",
            "platform": {"system": "Test", "release": "1", "machine": "x"},
            "capabilities": [{"capability": "binary-inspection", "available": True, "providers": []}],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            registry_path = Path(temp_dir) / "registry.json"
            registry_path.write_text(json.dumps(registry()), encoding="utf-8")
            argv = [
                "probe_toolchain.py",
                "--registry", str(registry_path),
                "--profile", "opaque-system-analysis",
                "--require", "version-control",
            ]
            with mock.patch.object(probe_toolchain, "probe", return_value=fake), mock.patch("sys.argv", argv), mock.patch("builtins.print"):
                code = probe_toolchain.main()
        self.assertEqual(code, 2)

    def test_registry_rejects_profile_with_unknown_capability(self) -> None:
        bad = registry()
        bad["profiles"]["bad"] = ["does-not-exist"]
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "registry.json"
            path.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaises(ValueError):
                probe_toolchain.load_registry(path)


if __name__ == "__main__":
    unittest.main()
