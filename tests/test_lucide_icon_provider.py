import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_lucide_icon_provider.py"
SPEC = importlib.util.spec_from_file_location("validate_lucide_icon_provider", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class LucideIconProviderContractTests(unittest.TestCase):
    def test_offline_contract_and_snapshot_are_consistent(self):
        snapshot, refs = MODULE.validate_offline()
        self.assertEqual(snapshot["provider"], "lucide-generic")
        self.assertEqual(snapshot["release"], "1.27.0")
        self.assertEqual(len(refs), 145)
        self.assertEqual(refs, snapshot["referencedIcons"])

    def test_high_value_skillz_icons_are_pinned(self):
        _, refs = MODULE.validate_offline()
        for icon in (
            "dumbbell",
            "trophy",
            "gauge",
            "plane",
            "route",
            "map-pin",
            "search",
            "microscope",
            "workflow",
            "waypoints",
            "milestone",
            "test-tubes",
            "layout-template",
            "presentation",
        ):
            with self.subTest(icon=icon):
                self.assertIn(icon, refs)

    def test_claim_safety_and_corporate_priority_are_mandatory(self):
        catalog = MODULE._load_json(MODULE.CATALOG_PATH)
        registry = MODULE._load_json(MODULE.REGISTRY_PATH)
        safety = catalog["statusSafety"]
        self.assertTrue(safety["positiveStatusRequiresEvidence"])
        self.assertTrue(safety["regulatoryApprovalMayNotBeInferredFromIcon"])
        self.assertTrue(safety["medicalIconMayNotImplyDiagnosisOrPerformance"])
        self.assertEqual(registry["providers"]["euroimmun-corporate"]["providerPriority"], "corporate")
        self.assertEqual(registry["providers"]["lucide-generic"]["providerPriority"], "generic-fallback")

    def test_snapshot_uses_immutable_full_git_ids(self):
        snapshot, _ = MODULE.validate_offline()
        self.assertEqual(len(snapshot["commit"]), 40)
        self.assertEqual(len(snapshot["sourceTree"]), 40)
        self.assertEqual(len(snapshot["inventoryTree"]), 40)
        self.assertEqual(snapshot["commit"], "4aec3f892fd6c23063bc2fead83c899b5d412b1c")
        self.assertEqual(snapshot["sourceTree"], "595ccdd85394acb59eac77042444a2ad2a2fcc88")
        self.assertEqual(snapshot["inventoryTree"], "468ecb61d104ef0374943b29112e1611d5cec12d")


if __name__ == "__main__":
    unittest.main()
