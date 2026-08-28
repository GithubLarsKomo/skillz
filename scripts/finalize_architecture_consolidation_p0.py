#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIVERSE = ROOT / "docs" / "SKILL-UNIVERSE.md"

STALE_INVENTORY = (
    "Current canonical inventory after the customer-service/complaint follow-up wave: "
    "**108 skills, 90 user-facing entrypoints, 108/108 evaluation suites passing, 0 evaluation errors**."
)
CURRENT_INVENTORY_POINTER = (
    "Current inventory and evaluation health are generated from the canonical capability metadata. "
    "Use [`skill-capability-index.json`](skill-capability-index.json) for the machine-readable inventory "
    "and [`CAPABILITY-HEALTH.md`](CAPABILITY-HEALTH.md) for current counts and health findings."
)


def replace_stale_inventory() -> bool:
    text = UNIVERSE.read_text(encoding="utf-8")
    if STALE_INVENTORY not in text:
        if CURRENT_INVENTORY_POINTER in text:
            return False
        raise RuntimeError(
            "docs/SKILL-UNIVERSE.md no longer contains the expected stale inventory line or the "
            "replacement pointer; review the curated document before applying this migration."
        )
    UNIVERSE.write_text(
        text.replace(STALE_INVENTORY, CURRENT_INVENTORY_POINTER, 1),
        encoding="utf-8",
        newline="\n",
    )
    return True


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    changed = replace_stale_inventory()
    print("UPDATED: docs/SKILL-UNIVERSE.md" if changed else "OK: docs/SKILL-UNIVERSE.md")

    run(sys.executable, "scripts/generate_repository_metadata.py")
    run(sys.executable, "scripts/generate_repository_metadata.py", "--check")
    run(sys.executable, "scripts/validate_metadata_schemas.py")
    run(sys.executable, "-m", "unittest", "tests.test_architecture_consolidation_contract")

    print("P0 architecture-consolidation finalization passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
