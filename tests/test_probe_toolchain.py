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


class ProbeToolchainTests(unittest.TestCase):
    def test_probe_groups_tools_by_capability(self) -> None:
        def which(command: str) -> str | None:
            return "/usr/bin/objdump" if command == "objdump" else None

        with mock.patch.object(probe_toolchain.shutil, "which", side_effect=which), mock.patch.object(
            probe_toolchain, "first_version_line", return_value="objdump 1.0"
        ):
            result = probe_toolchain.probe()

        by_capability = {entry["capability"]: entry for entry in result["capabilities"]}
        binary = by_capability["binary-inspection"]
        self.assertTrue(binary["available"])
        self.assertEqual(binary["providers"][0]["provider"], "objdump")
        self.assertFalse(by_capability["network-capture"]["available"])

    def test_main_writes_json_and_reports_missing_requirement(self) -> None:
        fake = {
            "schemaVersion": 1,
            "verifiedAt": "2026-08-02T18:00:00Z",
            "platform": {"system": "Test", "release": "1", "machine": "x"},
            "capabilities": [
                {"capability": "binary-inspection", "available": False, "providers": []}
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "toolchain.json"
            argv = ["probe_toolchain.py", "--output", str(output), "--require", "binary-inspection"]
            with mock.patch.object(probe_toolchain, "probe", return_value=fake), mock.patch("sys.argv", argv):
                code = probe_toolchain.main()
            payload = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(code, 1)
        self.assertEqual(payload["requirements"]["missing"], ["binary-inspection"])

    def test_unknown_requirement_has_distinct_exit_code(self) -> None:
        fake = {
            "schemaVersion": 1,
            "verifiedAt": "2026-08-02T18:00:00Z",
            "platform": {"system": "Test", "release": "1", "machine": "x"},
            "capabilities": [],
        }
        argv = ["probe_toolchain.py", "--require", "does-not-exist"]
        with mock.patch.object(probe_toolchain, "probe", return_value=fake), mock.patch("sys.argv", argv), mock.patch("builtins.print"):
            code = probe_toolchain.main()
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
