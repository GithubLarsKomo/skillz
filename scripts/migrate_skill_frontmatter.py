#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SYNC = ROOT / ".skill-sync.json"

METADATA = {
    "central-skill-repository-curation": {
        "version": "1.0.0",
        "status": "stable",
        "requires": ["composable-skill-factory"],
        "outputs": ["updated skill repository", "synchronization manifest"],
    },
    "composable-skill-factory": {
        "version": "0.2.0",
        "status": "candidate",
        "requires": [],
        "outputs": ["skills/<skill-name>/SKILL.md", "evaluation evidence", "pull request"],
    },
    "conversation-to-spec": {
        "version": "0.1.0",
        "status": "candidate",
        "requires": [],
        "outputs": ["SPEC.md", "decision register", "consistency report"],
    },
    "deferred-external-action-verification": {
        "version": "1.0.0",
        "status": "stable",
        "requires": [],
        "outputs": ["watch record", "verified terminal status", "continuation result"],
    },
    "iterate-software-projects": {
        "version": "1.0.0",
        "status": "stable",
        "requires": [],
        "outputs": ["review findings", "next increment", "verification evidence"],
    },
    "openasr-offline-model-import": {
        "version": "0.2.0",
        "status": "candidate",
        "requires": [],
        "outputs": ["installed OpenASR model", "import verification"],
    },
    "repository-skill-bootstrap": {
        "version": "0.2.0",
        "status": "candidate",
        "requires": [],
        "outputs": ["docs/agents/CONFIG.md", "docs/agents/CONTEXT.md", "docs/agents/DECISIONS.md"],
    },
    "round-based-requirements-grilling": {
        "version": "1.0.0",
        "status": "stable",
        "requires": [],
        "outputs": ["GRILL-REPORT.md", "approved SPEC.md"],
    },
    "synapse-orchestrator": {
        "version": "0.2.0",
        "status": "candidate",
        "requires": [],
        "outputs": ["execution plan", "expert handoff", "progress summary"],
    },
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data, text[end + 5 :]


def emit_list(key: str, values: list[str]) -> list[str]:
    if not values:
        return [f"{key}: []"]
    return [f"{key}:", *[f"  - {value}" for value in values]]


def normalized_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    text = text.rstrip("\n") + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def migrate_skill(slug: str, metadata: dict[str, object]) -> None:
    path = SKILLS / slug / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    current, body = parse_frontmatter(text)
    name = current.get("name")
    description = current.get("description")
    if name != slug or not description:
        raise ValueError(f"invalid existing frontmatter for {slug}")

    lines = [
        "---",
        f"name: {name}",
        f"description: {description}",
        f"version: {metadata['version']}",
        f"status: {metadata['status']}",
        "owners:",
        "  - GithubLarsKomo",
    ]
    lines.extend(emit_list("requires", metadata["requires"]))
    lines.extend(emit_list("outputs", metadata["outputs"]))
    lines.extend(["lastEvaluated: 2026-07-31", "---", ""])
    path.write_text("\n".join(lines) + body, encoding="utf-8", newline="\n")


def refresh_manifest() -> None:
    manifest = json.loads(SYNC.read_text(encoding="utf-8"))
    manifest["schemaVersion"] = 2
    manifest["synchronizedAt"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    skills: dict[str, object] = {}
    for skill_dir in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        files: dict[str, str] = {}
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                files[path.relative_to(skill_dir).as_posix()] = normalized_sha256(path)
        skills[skill_dir.name] = {"files": files}
    manifest["skills"] = skills
    SYNC.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    expected = set(METADATA)
    if actual != expected:
        raise SystemExit(f"skill set mismatch: missing={sorted(actual - expected)} extra={sorted(expected - actual)}")
    for slug, metadata in METADATA.items():
        migrate_skill(slug, metadata)
    refresh_manifest()


if __name__ == "__main__":
    main()
