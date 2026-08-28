#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

from evaluate_skills import run as evaluate_all
from generate_dependency_graph import build_graph
from generate_repository_metadata import parse_frontmatter, skill_files

INDEX_JSON = "docs/skill-capability-index.json"
CATEGORY_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def portable_files(skill_dir: Path) -> list[str]:
    return sorted(
        path.relative_to(skill_dir).as_posix()
        for path in skill_files(skill_dir)
        if path.name != "SKILL.md"
    )


def invocation_metadata(frontmatter: dict[str, object], path: Path) -> dict[str, object]:
    raw_user_facing = frontmatter.get("userFacing", "false")
    if isinstance(raw_user_facing, list):
        raise ValueError(f"{path}: userFacing muss true oder false sein")
    normalized = str(raw_user_facing).strip().lower()
    if normalized not in {"true", "false"}:
        raise ValueError(f"{path}: userFacing muss true oder false sein")
    user_facing = normalized == "true"

    raw_category = frontmatter.get("category")
    if isinstance(raw_category, list):
        raise ValueError(f"{path}: category muss ein einzelner Slug sein")
    category = str(raw_category).strip() if raw_category is not None else None
    if category == "":
        category = None
    if category is not None and not CATEGORY_RE.fullmatch(category):
        raise ValueError(f"{path}: category muss ein kebab-case Slug sein")
    if user_facing and category is None:
        raise ValueError(f"{path}: userFacing=true erfordert category")
    if not user_facing and category is not None:
        raise ValueError(f"{path}: category ist nur zusammen mit userFacing=true erlaubt")
    return {"userFacing": user_facing, "category": category}


def build_index(root: Path) -> dict[str, object]:
    graph = build_graph(root)
    graph_skills = {item["name"]: item for item in graph["skills"]}
    reverse: dict[str, list[str]] = {name: [] for name in graph_skills}
    for edge in graph["requirementEdges"]:
        reverse[edge["to"]].append(edge["from"])
    contracts_by_producer: dict[str, list[dict[str, object]]] = {name: [] for name in graph_skills}
    for contract in graph["outputContracts"]:
        for producer in contract["producers"]:
            contracts_by_producer[producer].append({
                "output": contract["output"],
                "ambiguous": contract["ambiguous"],
                "producers": contract["producers"],
                "consumerSkills": contract["consumerSkills"],
            })

    evaluation_summary, evaluation_errors = evaluate_all(root)
    evaluations = {suite["skill"]: suite for suite in evaluation_summary["suites"]}

    skills: list[dict[str, object]] = []
    for skill_md in sorted((root / "skills").glob("*/SKILL.md")):
        slug = skill_md.parent.name
        fm = parse_frontmatter(skill_md)
        graph_meta = graph_skills[slug]
        suite = evaluations.get(slug)
        if suite is None:
            evaluation = {
                "mode": "none",
                "caseCount": 0,
                "recordedResultCount": 0,
                "passed": None,
            }
        else:
            evaluation = {
                "mode": "compatibility" if suite["compatibilityMode"] else "rubric",
                "caseCount": len(suite["cases"]),
                "recordedResultCount": len(suite["recordedResults"]),
                "passed": suite["passed"],
            }
        skills.append({
            "name": slug,
            "description": str(fm.get("description", "")),
            "invocation": invocation_metadata(fm, skill_md),
            "requires": graph_meta["requires"],
            "dependents": sorted(reverse[slug]),
            "outputs": graph_meta["outputs"],
            "outputContracts": sorted(contracts_by_producer[slug], key=lambda item: str(item["output"])),
            "portableFiles": portable_files(skill_md.parent),
            "evaluation": evaluation,
        })

    entrypoint_skills = [skill for skill in skills if skill["invocation"]["userFacing"]]
    entrypoint_categories = sorted({str(skill["invocation"]["category"]) for skill in entrypoint_skills})
    evaluated_skills = [skill for skill in skills if skill["evaluation"]["mode"] != "none"]
    evaluated_entrypoints = [
        skill for skill in entrypoint_skills if skill["evaluation"]["mode"] != "none"
    ]
    return {
        "schemaVersion": 1,
        "skillCount": len(skills),
        "entrypointCount": len(entrypoint_skills),
        "entrypointCategories": entrypoint_categories,
        "evaluationSuiteCount": evaluation_summary["suiteCount"],
        "evaluatedSkillCount": len(evaluated_skills),
        "evaluatedEntrypointCount": len(evaluated_entrypoints),
        "evaluationCoverageComplete": len(evaluated_skills) == len(skills),
        "evaluationPassed": evaluation_summary["passed"],
        "evaluationErrorCount": len(evaluation_errors),
        "skills": skills,
    }


def render_json(index: dict[str, object]) -> str:
    return json.dumps(index, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def apply(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return False
    if check:
        print(f"STALE: {path}", file=sys.stderr)
        for line in difflib.unified_diff(
            actual.splitlines(), expected.splitlines(),
            fromfile=f"{path} (committed)", tofile=f"{path} (generated)", lineterm="",
        ):
            print(line, file=sys.stderr)
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"UPDATED: {path}")
    return True


def run(root: Path, check: bool) -> int:
    try:
        stale = apply(root / INDEX_JSON, render_json(build_index(root)), check)
        return 1 if check and stale else 0
    except (ValueError, KeyError, UnicodeDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic skill capability index.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    args = parser.parse_args()
    return run(args.root.resolve(), args.check)


if __name__ == "__main__":
    raise SystemExit(main())
