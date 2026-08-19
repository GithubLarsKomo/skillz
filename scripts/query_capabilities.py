#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from skill_status import (
    installed_identity,
    load_distribution_manifest,
    render_human as render_status_human,
    resolve_status,
)

SCHEMA_VERSION = 1
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "docs" / "skill-capability-index.json"
DEFAULT_VERSION = ROOT / "VERSION"
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


def invocation(skill: dict) -> dict:
    value = skill.get("invocation", {})
    return value if isinstance(value, dict) else {}


def query_skill_listing(index: dict, query: str | None) -> tuple[str, list[dict]]:
    normalized = (query or "").strip().casefold()
    include_all = normalized == "all"
    terms = [] if include_all else [term for term in normalized.split() if term]
    matches: list[dict] = []
    for skill in index["skills"]:
        meta = invocation(skill)
        if not include_all and not bool(meta.get("userFacing", False)):
            continue
        category = str(meta.get("category") or "internal")
        haystack = " ".join((skill.get("name", ""), skill.get("description", ""), category)).casefold()
        if terms and not all(term in haystack for term in terms):
            continue
        matches.append(skill)
    return ("all" if include_all else "entrypoints"), sorted(
        matches,
        key=lambda item: (str(invocation(item).get("category") or "internal"), item["name"]),
    )


def listing_payload(mode: str, query: str | None, skills: list[dict]) -> dict:
    categories: dict[str, list[dict]] = {}
    for skill in skills:
        meta = invocation(skill)
        category = str(meta.get("category") or "internal")
        categories.setdefault(category, []).append({
            "name": skill["name"],
            "description": skill.get("description", ""),
            "userFacing": bool(meta.get("userFacing", False)),
        })
    return {
        "schemaVersion": 1,
        "mode": mode,
        "query": None if not query or query.strip().casefold() == "all" else query.strip(),
        "count": len(skills),
        "categories": [
            {"category": category, "skills": categories[category]}
            for category in sorted(categories)
        ],
    }


def provenance(index: dict) -> dict:
    value = index.get("provenance", {})
    return value if isinstance(value, dict) else {}


def repository_version(index: dict, override: str | None = None) -> str | None:
    if override and override.strip():
        return override.strip()
    value = provenance(index).get("version")
    if value is not None and str(value).strip():
        return str(value).strip()
    try:
        return DEFAULT_VERSION.read_text(encoding="utf-8").strip() or None
    except OSError:
        return None


def build_status_payload(
    index: dict,
    *,
    repository_head: str | None,
    repository_version_override: str | None,
    installed_manifest: Path | None,
    installed_commit: str | None,
    installed_version: str | None,
) -> dict:
    meta = provenance(index)
    head = repository_head or (str(meta.get("commitSha")) if meta.get("commitSha") is not None else None)
    runtime_version = installed_version
    runtime_commit = installed_commit
    if installed_manifest is not None:
        manifest_version, manifest_commit = installed_identity(load_distribution_manifest(installed_manifest))
        runtime_version = runtime_version or manifest_version
        runtime_commit = runtime_commit or manifest_commit
    return resolve_status(
        repository_head=head,
        repository_version=repository_version(index, repository_version_override),
        installed_commit=runtime_commit,
        installed_version=runtime_version,
    )


def render_human(kind: str, value: object) -> str:
    if kind == "skill":
        assert isinstance(value, dict)
        meta = invocation(value)
        lines = [value["name"], f"description: {value.get('description', '')}"]
        lines.append(f"userFacing: {str(bool(meta.get('userFacing', False))).lower()}")
        lines.append(f"category: {meta.get('category') or '—'}")
        lines.append("requires: " + (", ".join(value.get("requires", [])) or "—"))
        lines.append("dependents: " + (", ".join(value.get("dependents", [])) or "—"))
        lines.append("outputs: " + (", ".join(value.get("outputs", [])) or "—"))
        lines.append(f"evaluation: {value.get('evaluation', {}).get('mode', 'none')}")
        return "\n".join(lines)
    if kind == "skills":
        assert isinstance(value, dict)
        lines: list[str] = []
        for group in value["categories"]:
            lines.append(f"[{group['category']}]")
            for skill in group["skills"]:
                suffix = "" if skill["userFacing"] else " [internal]"
                lines.append(f"- {skill['name']}{suffix} — {skill['description']}")
        return "\n".join(lines) if lines else "(no matches)"
    if kind == "status":
        assert isinstance(value, dict)
        return render_status_human(value)
    assert isinstance(value, list)
    return "\n".join(value) if value else "(no matches)"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query the committed skill capability index deterministically.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Emit stable JSON output.")
    parser.add_argument("--repository-head", help="Live repository HEAD SHA used by `/skills status`.")
    parser.add_argument("--repository-version", help="Repository version override used by `/skills status`.")
    parser.add_argument("--installed-manifest", type=Path, help="Installed skillz-distribution-manifest.json used by `/skills status`.")
    parser.add_argument("--installed-commit", help="Installed source commit override used by `/skills status`.")
    parser.add_argument("--installed-version", help="Installed plugin version override used by `/skills status`.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill")
    group.add_argument("--skills", nargs="?", const="", metavar="QUERY", help="List user-facing entrypoints; use 'all' for every skill or 'status' for freshness.")
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
        elif args.skills is not None and args.skills.strip().casefold() == "status":
            kind = "status"
            result = build_status_payload(
                index,
                repository_head=args.repository_head,
                repository_version_override=args.repository_version,
                installed_manifest=args.installed_manifest,
                installed_commit=args.installed_commit,
                installed_version=args.installed_version,
            )
        elif args.skills is not None:
            mode, matches = query_skill_listing(index, args.skills)
            kind, result = "skills", listing_payload(mode, args.skills, matches)
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
        if kind in {"skill", "skills", "status"}:
            payload = result
        else:
            payload = {"matches": result, "count": len(result)}
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(kind, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
