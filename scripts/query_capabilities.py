#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCHEMA_VERSION = 1
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"
VALID_MODES = {"rubric", "compatibility", "none"}


def load_index(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read capability index: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("capability index root must be an object")
    if data.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError(
            f"unsupported capability index schemaVersion {data.get('schemaVersion')!r}; expected {SCHEMA_VERSION}"
        )
    skills = data.get("skills")
    if not isinstance(skills, list):
        raise ValueError("capability index skills must be a list")
    return data


def skills_by_name(index: dict) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for item in index["skills"]:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            raise ValueError("capability index contains an invalid skill record")
        result[item["name"]] = item
    return result


def get_skill(index: dict, name: str) -> dict:
    skill = skills_by_name(index).get(name)
    if skill is None:
        raise LookupError(f"unknown skill: {name}")
    return skill


def query_requires(index: dict, dependency: str) -> list[dict]:
    if dependency not in skills_by_name(index):
        raise LookupError(f"unknown skill: {dependency}")
    return sorted(
        [skill for skill in index["skills"] if dependency in skill.get("requires", [])],
        key=lambda item: item["name"],
    )


def query_output(index: dict, output: str) -> list[dict]:
    matches = sorted(
        [skill for skill in index["skills"] if output in skill.get("outputs", [])],
        key=lambda item: item["name"],
    )
    if not matches:
        raise LookupError(f"unknown output: {output}")
    return matches


def query_mode(index: dict, mode: str) -> list[dict]:
    if mode not in VALID_MODES:
        raise ValueError(f"unsupported evaluation mode: {mode}")
    return sorted(
        [skill for skill in index["skills"] if skill.get("evaluation", {}).get("mode") == mode],
        key=lambda item: item["name"],
    )


def query_portable(index: dict, with_files: bool) -> list[dict]:
    return sorted(
        [skill for skill in index["skills"] if bool(skill.get("portableFiles", [])) is with_files],
        key=lambda item: item["name"],
    )


def names(items: list[dict]) -> list[str]:
    return [item["name"] for item in items]


def render_human(kind: str, value: object) -> str:
    if kind == "skill":
        assert isinstance(value, dict)
        lines = [value["name"], f"description: {value.get('description', '')}"]
        lines.append("requires: " + (", ".join(value.get("requires", [])) or "—"))
        lines.append("dependents: " + (", ".join(value.get("dependents", [])) or "—"))
        lines.append("outputs: " + (", ".join(value.get("outputs", [])) or "—"))
        lines.append(f"evaluation: {value.get('evaluation', {}).get('mode', 'none')}")
        return "\n".join(lines)
    assert isinstance(value, list)
    return "\n".join(value) if value else "(no matches)"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query the committed skill capability index deterministically.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Emit stable JSON output.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill")
    group.add_argument("--requires")
    group.add_argument("--output")
    group.add_argument("--evaluation-mode", choices=sorted(VALID_MODES))
    group.add_argument("--with-portable-files", action="store_true")
    group.add_argument("--without-portable-files", action="store_true")
    group.add_argument("--dependencies")
    group.add_argument("--dependents")
    args = parser.parse_args(argv)

    try:
        index = load_index(args.index)
        kind = "list"
        if args.skill:
            kind, result = "skill", get_skill(index, args.skill)
        elif args.requires:
            result = names(query_requires(index, args.requires))
        elif args.output:
            result = names(query_output(index, args.output))
        elif args.evaluation_mode:
            result = names(query_mode(index, args.evaluation_mode))
        elif args.with_portable_files:
            result = names(query_portable(index, True))
        elif args.without_portable_files:
            result = names(query_portable(index, False))
        elif args.dependencies:
            result = sorted(get_skill(index, args.dependencies).get("requires", []))
        else:
            result = sorted(get_skill(index, args.dependents).get("dependents", []))
    except (ValueError, LookupError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        payload = result if kind == "skill" else {"matches": result, "count": len(result)}
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(kind, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
