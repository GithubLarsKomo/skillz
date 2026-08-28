#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONSUMES: dict[str, list[str]] = {
    "sport-goal-performance-model": [
        "athlete-profile.json",
    ],
    "sport-season-periodization": [
        "sport-performance-model.json",
    ],
    "sport-mesocycle-planning": [
        "sport-season-plan.json",
    ],
    "sport-microcycle-planning": [
        "sport-mesocycle.json",
    ],
    "sport-strength-power-programming": [
        "athlete-profile.json",
        "sport-performance-model.json",
        "sport-mesocycle.json",
        "sport-microcycle.json",
    ],
    "sport-endurance-programming": [
        "athlete-profile.json",
        "sport-diagnostics.json",
        "sport-performance-model.json",
        "sport-mesocycle.json",
        "sport-microcycle.json",
    ],
    "sport-training-plan-workflow": [
        "athlete-profile.json",
        "sport-diagnostics.json",
        "sport-performance-model.json",
        "sport-season-plan.json",
        "sport-mesocycle.json",
        "sport-microcycle.json",
        "strength-power-plan.json",
        "endurance-plan.json",
    ],
    "dr-komorowski-sport-pdf-report-renderer": [
        "dr-komorowski-sport-report.docx",
    ],
    "sport-diagnostics-training-report-workflow": [
        "sport-diagnostics.json",
        "sport-training-plan.json",
        "dr-komorowski-sport-report.docx",
        "dr-komorowski-sport-report.pdf",
    ],
    "presentation-layout-qa": [
        "presentation-template-profile.json",
    ],
    "presentation-render-verifier": [
        "presentation-layout-qa.json",
    ],
    "template-presentation-workflow": [
        "presentation-template-profile.json",
        "presentation-revised-text",
        "presentation-language-report.json",
        "presentation-layout-qa.json",
        "presentation-layout-qa.md",
        "presentation-render-qa.json",
        "presentation-render-qa.md",
        "presentation-preview.pdf",
    ],
    "person-profile-document-delivery": [
        "final-revised-text",
        "precision-writing-report.json",
    ],
}


def split_frontmatter(text: str) -> tuple[list[str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc
    return lines[1:end], lines[end + 1 :]


def replace_consumes(frontmatter: list[str], consumes: list[str]) -> list[str]:
    result: list[str] = []
    i = 0
    while i < len(frontmatter):
        if frontmatter[i] == "consumes:":
            i += 1
            while i < len(frontmatter) and frontmatter[i].startswith("  - "):
                i += 1
            continue
        result.append(frontmatter[i])
        i += 1

    try:
        outputs_index = result.index("outputs:")
    except ValueError as exc:
        raise ValueError("frontmatter has no outputs key") from exc

    block = ["consumes:", *[f"  - {artifact}" for artifact in consumes]]
    return result[:outputs_index] + block + result[outputs_index:]


def migrate(slug: str, consumes: list[str]) -> bool:
    path = ROOT / "skills" / slug / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    migrated = replace_consumes(frontmatter, consumes)
    rendered = "\n".join(["---", *migrated, "---", *body]) + "\n"
    if rendered == text:
        return False
    path.write_text(rendered, encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for slug, consumes in CONSUMES.items():
        if migrate(slug, consumes):
            changed.append(slug)
    print(f"P3 artifact-contract migration: {len(changed)} changed")
    for slug in changed:
        print(f"- {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
