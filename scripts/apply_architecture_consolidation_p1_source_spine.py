#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = {
    "skills/research-to-evidence-note/SKILL.md": (
        "requires: []\noutputs:\n",
        "requires: []\nconsumes:\n  - source-context.json\noutputs:\n",
    ),
    "skills/multimodal-learning-analysis/SKILL.md": (
        "requires: []\noutputs:\n",
        "requires: []\nconsumes:\n  - source-context.json\noutputs:\n",
    ),
}


def apply_target(relative: str, old: str, new: str) -> bool:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if new in text:
        return False
    if old not in text:
        raise RuntimeError(f"{relative}: expected migration anchor not found")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
    return True


def main() -> int:
    changed = []
    for relative, (old, new) in TARGETS.items():
        if apply_target(relative, old, new):
            changed.append(relative)
    if changed:
        for relative in changed:
            print(f"UPDATED: {relative}")
    else:
        print("OK: P1 source-context consumers already migrated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
