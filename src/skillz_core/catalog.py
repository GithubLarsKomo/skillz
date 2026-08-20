from __future__ import annotations

import json
from pathlib import Path

SCHEMA_VERSION = 1
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
    if not isinstance(data.get("skills"), list):
        raise ValueError("capability index skills must be a list")
    return data


def skills_by_name(index: dict) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for item in index["skills"]:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            raise ValueError("capability index contains an invalid skill record")
        if item["name"] in result:
            raise ValueError(f"duplicate skill: {item['name']}")
        result[item["name"]] = item
    return result


def get_skill(index: dict, name: str) -> dict:
    skill = skills_by_name(index).get(name)
    if skill is None:
        raise LookupError(f"unknown skill: {name}")
    return skill


def invocation(skill: dict) -> dict:
    value = skill.get("invocation", {})
    return value if isinstance(value, dict) else {}


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


def query_portable(index: dict, with_files: bool) -> list[dict]:
    return sorted(
        [skill for skill in index["skills"] if bool(skill.get("portableFiles", [])) is with_files],
        key=lambda item: item["name"],
    )


def names(items: list[dict]) -> list[str]:
    return [item["name"] for item in items]


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
