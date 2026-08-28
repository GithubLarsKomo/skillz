#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "skills/learning-summary-synthesis/tests/evaluation.json": (
        "lernwirsame Verdichtung",
        "lernwirksame Verdichtung",
    ),
    "skills/presentation-layout-qa/tests/evaluation.json": (
        "kein Render-Test",
        "keinen Render-Test",
    ),
    "skills/youtube-playlist-learning-workflow/tests/evaluation.json": (
        "Single-Source-Aussagen nicht als Konsens",
        "Single-Source-Aussagen nicht als Konsens dargestellt",
    ),
}


def main() -> int:
    changed = 0
    for relative, (old, new) in REPLACEMENTS.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        if new in text:
            print(f"OK: {relative}")
            continue
        if old not in text:
            raise RuntimeError(f"{relative}: expected anchor {old!r} not found")
        path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
        print(f"UPDATED: {relative}")
        changed += 1
    print(f"Evaluation anchors corrected: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
