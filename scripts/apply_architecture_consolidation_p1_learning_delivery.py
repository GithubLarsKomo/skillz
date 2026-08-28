#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MIGRATIONS = {
    "skills/youtube-learning-workflow/SKILL.md": (
        """requires:\n  - youtube-video-ingestion\n  - multimodal-learning-analysis\n  - learning-summary-synthesis\n  - procedure-sop-extractor\n  - learning-visual-planner\n  - learning-content-design-system\n  - learning-svg-generator\n  - learning-image-generator\n  - learning-landingpage-renderer\n  - learning-document-delivery\n  - learning-artifact-qa\n  - template-presentation-workflow\n""",
        """requires:\n  - youtube-video-ingestion\n  - multimodal-learning-analysis\n  - learning-summary-synthesis\n  - procedure-sop-extractor\n  - learning-delivery-workflow\n""",
    ),
    "skills/youtube-playlist-learning-workflow/SKILL.md": (
        """requires:\n  - youtube-learning-workflow\n  - learning-source-arbitration\n  - multi-source-learning-synthesis\n  - learning-visual-planner\n  - learning-content-design-system\n  - learning-svg-generator\n  - learning-image-generator\n  - learning-landingpage-renderer\n  - learning-document-delivery\n  - learning-artifact-qa\n  - template-presentation-workflow\n""",
        """requires:\n  - youtube-learning-workflow\n  - learning-source-arbitration\n  - multi-source-learning-synthesis\n  - learning-delivery-workflow\n""",
    ),
    "skills/youtube-course-builder-workflow/SKILL.md": (
        """requires:\n  - youtube-playlist-learning-workflow\n  - course-concept-graph\n  - learning-path-planner\n  - learning-activity-generator\n  - learning-visual-planner\n  - learning-content-design-system\n  - learning-svg-generator\n  - learning-image-generator\n  - learning-landingpage-renderer\n  - template-presentation-workflow\n  - learning-document-delivery\n  - learning-artifact-qa\n""",
        """requires:\n  - youtube-playlist-learning-workflow\n  - course-concept-graph\n  - learning-path-planner\n  - learning-activity-generator\n  - learning-delivery-workflow\n""",
    ),
}

SECTION_INSERTS = {
    "skills/youtube-learning-workflow/SKILL.md": (
        "## Ziel\n\n",
        "## Ziel\n\nDie fachliche Einzelvideo-Analyse bleibt in diesem Skill. Sobald `learning-content-model.json` fixiert ist, wird Design-, Visual-, Render- und Cross-Format-QA an `learning-delivery-workflow` delegiert; die einzelnen Renderer werden hier nicht parallel orchestriert.\n\n",
    ),
    "skills/youtube-playlist-learning-workflow/SKILL.md": (
        "## Ziel\n\n",
        "## Ziel\n\nDie Multi-Source-Arbitration und Synthese bleiben in diesem Skill. Sobald `multi-source-learning-model.json` fixiert ist, wird die gemeinsame Design-, Visual-, Render- und Cross-Format-QA-Schicht über `learning-delivery-workflow` ausgeführt.\n\n",
    ),
    "skills/youtube-course-builder-workflow/SKILL.md": (
        "## Ziel\n\n",
        "## Ziel\n\nCourse Concept, Learning Path und Activities bleiben in diesem Skill. Nach dem Lock von `course-learning-model.json` wird die gemeinsame Design-, Visual-, Render- und Cross-Format-QA-Schicht über `learning-delivery-workflow` ausgeführt.\n\n",
    ),
}


def replace_once(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return False
    if old not in text:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected migration anchor not found")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
    return True


def main() -> int:
    changed: set[str] = set()
    for relative, (old, new) in MIGRATIONS.items():
        if replace_once(ROOT / relative, old, new):
            changed.add(relative)
    for relative, (old, new) in SECTION_INSERTS.items():
        if replace_once(ROOT / relative, old, new):
            changed.add(relative)
    if changed:
        for relative in sorted(changed):
            print(f"UPDATED: {relative}")
    else:
        print("OK: learning delivery consolidation already applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
