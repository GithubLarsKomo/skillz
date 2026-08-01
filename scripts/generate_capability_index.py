#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path

from evaluate_skills import run as evaluate_all
from generate_dependency_graph import build_graph
from generate_repository_metadata import parse_frontmatter, skill_files

INDEX_JSON = "docs/skill-capability-index.json"


def portable_files(skill_dir: Path) -> list[str]:
    return sorted(
        path.relative_to(skill_dir).as_posix()
        for path in skill_files(skill_dir)
        if path.name != "SKILL.md"
    )


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
            "requires": graph_meta["requires"],
            "dependents": sorted(reverse[slug]),
            "outputs": graph_meta["outputs"],
            "outputContracts": sorted(contracts_by_producer[slug], key=lambda item: str(item["output"])),
            "portableFiles": portable_files(skill_md.parent),
            "evaluation": evaluation,
        })

    return {
        "schemaVersion": 1,
        "skillCount": len(skills),
        "evaluationSuiteCount": evaluation_summary["suiteCount"],
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
