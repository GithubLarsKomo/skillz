#!/usr/bin/env python3
from __future__ import annotations

import json
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
        "Single-Source-Aussagen werden nicht als Konsens dargestellt",
    ),
}


def main() -> int:
    changed = 0
    for relative, (old, new) in REPLACEMENTS.items():
        path = ROOT / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        replaced = 0
        seen_new = False
        for case in data.get("cases", []):
            anchors = case.get("skillAnchors", [])
            for index, anchor in enumerate(anchors):
                if anchor == old:
                    anchors[index] = new
                    replaced += 1
                if anchors[index] == new:
                    seen_new = True
        if replaced:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            print(f"UPDATED: {relative} ({replaced} anchor)")
            changed += replaced
        elif seen_new:
            print(f"OK: {relative}")
        else:
            raise RuntimeError(
                f"{relative}: neither expected anchor {old!r} nor replacement {new!r} found"
            )
    print(f"Evaluation anchors corrected: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
