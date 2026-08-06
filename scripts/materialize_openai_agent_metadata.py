#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPLICIT_ONLY_DEFAULTS = {
    "central-skill-repository-curation",
    "composable-skill-factory",
    "round-based-requirements-grilling",
    "synapse-orchestrator",
}


def normalized_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n").rstrip("\n") + "\n"


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str], int]:
    lines = normalized_text(path).splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: unterminated YAML frontmatter") from exc
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip().strip('"\'')
    return metadata, lines, end


def _yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def policy_for(metadata: dict[str, str], slug: str) -> bool:
    value = metadata.get("implicitInvocation")
    if value is None:
        return slug not in EXPLICIT_ONLY_DEFAULTS
    normalized = value.casefold()
    if normalized not in {"true", "false"}:
        raise ValueError(f"{slug}: implicitInvocation must be true or false")
    return normalized == "true"


def render_agent_metadata(skill_md: Path, allow_implicit: bool) -> str:
    metadata, _, _ = parse_frontmatter(skill_md)
    name = metadata.get("name")
    description = metadata.get("description")
    if not name or not description:
        raise ValueError(f"{skill_md}: name and description are required")
    display_name = " ".join(part.capitalize() for part in name.split("-") if part)
    short_description = description if len(description) <= 120 else description[:117].rstrip() + "..."
    return (
        "interface:\n"
        f"  display_name: {_yaml_quote(display_name)}\n"
        f"  short_description: {_yaml_quote(short_description)}\n"
        "policy:\n"
        f"  allow_implicit_invocation: {'true' if allow_implicit else 'false'}\n"
    )


def render_skill_with_explicit_policy(skill_md: Path, allow_implicit: bool) -> str:
    metadata, lines, end = parse_frontmatter(skill_md)
    desired = "true" if allow_implicit else "false"
    found = False
    for i in range(1, end):
        if lines[i].startswith("implicitInvocation:"):
            lines[i] = f"implicitInvocation: {desired}"
            found = True
            break
    if not found:
        insert_at = end
        for i in range(1, end):
            if lines[i].startswith("userFacing:"):
                insert_at = i + 1
                break
        lines.insert(insert_at, f"implicitInvocation: {desired}")
    return "\n".join(lines).rstrip("\n") + "\n"


def run(root: Path, check: bool) -> int:
    stale: list[str] = []
    try:
        for skill_md in sorted((root / "skills").glob("*/SKILL.md")):
            slug = skill_md.parent.name
            metadata, _, _ = parse_frontmatter(skill_md)
            allow = policy_for(metadata, slug)
            expected_skill = render_skill_with_explicit_policy(skill_md, allow)
            agent_path = skill_md.parent / "agents" / "openai.yaml"
            expected_agent = render_agent_metadata(skill_md, allow)
            if normalized_text(skill_md) != expected_skill:
                if check:
                    stale.append(str(skill_md.relative_to(root)))
                else:
                    skill_md.write_text(expected_skill, encoding="utf-8", newline="\n")
            actual_agent = normalized_text(agent_path) if agent_path.exists() else ""
            if actual_agent != expected_agent:
                if check:
                    stale.append(str(agent_path.relative_to(root)))
                else:
                    agent_path.parent.mkdir(parents=True, exist_ok=True)
                    agent_path.write_text(expected_agent, encoding="utf-8", newline="\n")
        if stale:
            for path in stale:
                print(f"STALE: {path}", file=sys.stderr)
            return 1
        return 0
    except (OSError, ValueError, UnicodeDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize canonical per-skill OpenAI agent metadata and explicit invocation policies.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    return run(args.root.resolve(), args.check)


if __name__ == "__main__":
    raise SystemExit(main())
