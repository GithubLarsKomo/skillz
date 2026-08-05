#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA_VERSION = 1
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"
VALID_MODES = {"rubric", "compatibility", "none"}
ROUTE_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "i", "in", "is", "it", "of", "on",
    "or", "the", "this", "to", "with", "und", "oder", "der", "die", "das", "ein", "eine", "einer", "eines", "einen",
    "einem", "für", "mit", "von", "zu", "zur", "zum", "ich", "möchte", "will", "soll", "sollen", "wie", "was",
}


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


def route_terms(query: str) -> list[str]:
    tokens = re.findall(r"[\wäöüß-]+", query.casefold(), flags=re.UNICODE)
    return [token for token in tokens if len(token) > 1 and token not in ROUTE_STOPWORDS]


def route_capabilities(index: dict, query: str, limit: int = 5) -> list[dict]:
    terms = route_terms(query)
    if not terms:
        raise ValueError("route query contains no meaningful terms")
    ranked: list[dict] = []
    for skill in index["skills"]:
        meta = invocation(skill)
        if not bool(meta.get("userFacing", False)):
            continue
        name = str(skill.get("name", "")).casefold()
        category = str(meta.get("category") or "").casefold()
        description = str(skill.get("description", "")).casefold()
        outputs = " ".join(str(value) for value in skill.get("outputs", [])).casefold()
        matched: list[str] = []
        score = 0
        for term in terms:
            term_score = 0
            if term == name or term in name.split("-"):
                term_score = max(term_score, 8)
            elif term in name:
                term_score = max(term_score, 6)
            if term in category:
                term_score = max(term_score, 4)
            if term in description:
                term_score = max(term_score, 3)
            if term in outputs:
                term_score = max(term_score, 2)
            if term_score:
                matched.append(term)
                score += term_score
        if not matched:
            continue
        ranked.append({
            "name": skill["name"],
            "category": meta.get("category"),
            "description": skill.get("description", ""),
            "score": score,
            "matchedTerms": matched,
            "coverage": len(set(matched)) / len(set(terms)),
            "requires": list(skill.get("requires", [])),
            "likelyNext": list(skill.get("dependents", [])),
            "outputs": list(skill.get("outputs", [])),
        })
    ranked.sort(key=lambda item: (-item["coverage"], -item["score"], item["name"]))
    return ranked[:limit]


def route_payload(query: str, recommendations: list[dict]) -> dict:
    return {
        "schemaVersion": 1,
        "mode": "route",
        "query": query.strip(),
        "count": len(recommendations),
        "recommendations": recommendations,
        "executionPolicy": "advisory-only",
    }


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
    if kind == "route":
        assert isinstance(value, dict)
        lines: list[str] = []
        for position, item in enumerate(value["recommendations"], start=1):
            lines.append(f"{position}. {item['name']} [{item.get('category') or 'internal'}] score={item['score']}")
            lines.append(f"   matched: {', '.join(item['matchedTerms'])}")
            lines.append("   requires: " + (", ".join(item["requires"]) or "—"))
            lines.append("   likely-next: " + (", ".join(item["likelyNext"]) or "—"))
        return "\n".join(lines) if lines else "(no route matches)"
    assert isinstance(value, list)
    return "\n".join(value) if value else "(no matches)"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query the committed skill capability index deterministically.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Emit stable JSON output.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill")
    group.add_argument("--skills", nargs="?", const="", metavar="QUERY", help="List user-facing entrypoints; use 'all' for every skill.")
    group.add_argument("--route", metavar="QUERY", help="Rank user-facing entrypoints for a natural-language goal without executing them.")
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
        elif args.skills is not None:
            mode, matches = query_skill_listing(index, args.skills)
            kind, result = "skills", listing_payload(mode, args.skills, matches)
        elif args.route:
            kind, result = "route", route_payload(args.route, route_capabilities(index, args.route))
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
        if kind in {"skill", "skills", "route"}:
            payload = result
        else:
            payload = {"matches": result, "count": len(result)}
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(kind, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
