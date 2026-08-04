#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ENTRYPOINTS = {
    "engineering": [
        "agent-handoff",
        "architecture-deepening-review",
        "conversation-to-spec",
        "disciplined-diagnosis",
        "implement-from-issue",
        "iterate-software-projects",
        "large-work-wayfinder",
        "project-beta-readiness",
        "spec-to-vertical-issues",
        "throwaway-prototype",
        "two-axis-code-review",
    ],
    "regulated-engineering": [
        "controlled-quality-documentation",
        "eu-mdr-ivdr-regulatory-specialist",
        "fda-medical-device-ivd-regulatory-specialist",
        "iso13485-qms-audit",
        "iso27001-isms-audit",
        "medical-device-capa",
        "medical-device-isms-governance",
        "medical-device-privacy-gdpr-bdsg",
        "medical-device-qms-iso13485",
        "medical-device-regulatory-strategy",
        "medical-device-risk-management-iso14971",
        "qms-management-review-governance",
    ],
    "productivity": [
        "daily-and-weekly-review",
        "decision-and-follow-up-tracker",
        "inbox-action-triage",
        "meeting-preparation",
        "project-status-brief",
    ],
    "research-knowledge": [
        "research-to-evidence-note",
        "structured-knowledge-artifact",
    ],
    "communication-memory": [
        "communication-memory-governance",
    ],
    "skill-system": [
        "central-skill-repository-curation",
        "composable-skill-factory",
        "repository-skill-bootstrap",
    ],
}


def annotate(path: Path, category: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"unterminated frontmatter: {path}")
    frontmatter = text[4:end]
    body = text[end:]
    frontmatter = re.sub(r"(?m)^userFacing:\s*.*\n?", "", frontmatter)
    frontmatter = re.sub(r"(?m)^category:\s*.*\n?", "", frontmatter)
    lines = frontmatter.splitlines()
    insert_at = next((i + 1 for i, line in enumerate(lines) if line.startswith("description:")), 2)
    lines[insert_at:insert_at] = ["userFacing: true", f"category: {category}"]
    rendered = "---\n" + "\n".join(lines).rstrip() + body
    if rendered == text:
        return False
    path.write_text(rendered, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    assigned: dict[str, str] = {}
    for category, names in ENTRYPOINTS.items():
        for name in names:
            if name in assigned:
                raise ValueError(f"duplicate entrypoint assignment: {name}")
            assigned[name] = category
            path = ROOT / "skills" / name / "SKILL.md"
            if not path.exists():
                raise ValueError(f"unknown skill in entrypoint map: {name}")
            annotate(path, category)

    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        if skill_md.parent.name in assigned:
            continue
        text = skill_md.read_text(encoding="utf-8")
        if re.search(r"(?m)^userFacing:\s*true\s*$", text):
            raise ValueError(f"unexpected pre-existing user-facing skill outside curated map: {skill_md.parent.name}")

    return subprocess.run([sys.executable, str(ROOT / "scripts" / "generate_repository_metadata.py")], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
