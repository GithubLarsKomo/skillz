#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONSUMES: dict[str, list[str]] = {
    "euroimmun-pdf-report-renderer": [
        "euroimmun-report.docx",
    ],
    "legal-negotiation-strategy": [
        "client-strategy.json",
        "legal-decision-boundaries.json",
        "legal-risk-register.json",
        "commercial-exposure-analysis.json",
        "legal-risk-decision-handoff.json",
    ],
    "legal-redline-review-loop": [
        "contract-review.json",
        "contract-issue-list.json",
        "negotiation-positions.json",
    ],
    "legal-matter-final-gate": [
        "legal-risk-register.json",
        "legal-risk-decision-handoff.json",
        "privilege-routing.json",
        "counsel-scope.json",
    ],
    "contract-matter-workflow": [
        "agreement-deal-model.json",
        "agreement-clause-coverage.json",
        "agreement-specialist-routes.json",
        "contract-review.json",
        "contract-issue-list.json",
        "contract-risk-input.json",
        "contract-draft.md",
        "contract-drafting-report.json",
        "contract-open-points.md",
        "negotiation-positions.json",
        "redline-delta.json",
        "negotiation-state.json",
        "legal-final-gate.json",
        "legal-open-points.md",
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
    cleaned: list[str] = []
    i = 0
    while i < len(frontmatter):
        if frontmatter[i] == "consumes:":
            i += 1
            while i < len(frontmatter) and frontmatter[i].startswith("  - "):
                i += 1
            continue
        cleaned.append(frontmatter[i])
        i += 1

    try:
        outputs_index = cleaned.index("outputs:")
    except ValueError as exc:
        raise ValueError("frontmatter has no outputs key") from exc

    block = ["consumes:", *[f"  - {artifact}" for artifact in consumes]]
    return cleaned[:outputs_index] + block + cleaned[outputs_index:]


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
    changed: list[str] = []
    for slug, consumes in CONSUMES.items():
        if migrate(slug, consumes):
            changed.append(slug)
    print(f"P3 legal/document handoff migration: {len(changed)} changed")
    for slug in changed:
        print(f"- {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
