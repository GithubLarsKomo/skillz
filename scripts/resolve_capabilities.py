#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCHEMA_VERSION = 1
INDEX_SCHEMA_VERSION = 1
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"
VALID_MODES = {"rubric", "compatibility", "none"}
VALID_PORTABLE = {"required", "forbidden", "irrelevant"}


def load_index(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read capability index: {exc}") from exc
    if not isinstance(data, dict) or data.get("schemaVersion") != INDEX_SCHEMA_VERSION:
        raise ValueError(
            f"unsupported capability index schemaVersion {data.get('schemaVersion') if isinstance(data, dict) else None!r}; expected {INDEX_SCHEMA_VERSION}"
        )
    if not isinstance(data.get("skills"), list):
        raise ValueError("capability index skills must be a list")
    return data


def normalize_constraints(
    outputs: list[str],
    dependencies: list[str],
    modes: list[str],
    portable_files: str,
) -> dict:
    outputs = sorted(set(outputs))
    dependencies = sorted(set(dependencies))
    modes = sorted(set(modes))
    unknown_modes = [mode for mode in modes if mode not in VALID_MODES]
    if unknown_modes:
        raise ValueError(f"unsupported evaluation mode(s): {', '.join(unknown_modes)}")
    if portable_files not in VALID_PORTABLE:
        raise ValueError(f"unsupported portable-files constraint: {portable_files}")
    return {
        "outputs": outputs,
        "dependencies": dependencies,
        "evaluationModes": modes,
        "portableFiles": portable_files,
    }


def validate_known_constraints(index: dict, constraints: dict) -> None:
    skill_names = {item.get("name") for item in index["skills"] if isinstance(item, dict)}
    known_outputs = {
        output
        for item in index["skills"]
        if isinstance(item, dict)
        for output in item.get("outputs", [])
        if isinstance(output, str)
    }
    unknown_dependencies = [name for name in constraints["dependencies"] if name not in skill_names]
    unknown_outputs = [name for name in constraints["outputs"] if name not in known_outputs]
    if unknown_dependencies:
        raise ValueError(f"unknown dependency skill(s): {', '.join(unknown_dependencies)}")
    if unknown_outputs:
        raise ValueError(f"unknown output(s): {', '.join(unknown_outputs)}")


def evaluate_skill(skill: dict, constraints: dict) -> tuple[list[str], list[str]]:
    reasons: list[str] = []
    failed: list[str] = []
    skill_outputs = set(skill.get("outputs", []))
    skill_requires = set(skill.get("requires", []))
    mode = skill.get("evaluation", {}).get("mode")
    has_portable = bool(skill.get("portableFiles", []))

    for output in constraints["outputs"]:
        label = f"output:{output}"
        (reasons if output in skill_outputs else failed).append(label)
    for dependency in constraints["dependencies"]:
        label = f"dependency:{dependency}"
        (reasons if dependency in skill_requires else failed).append(label)
    if constraints["evaluationModes"]:
        label = f"evaluationMode:{mode}"
        (reasons if mode in constraints["evaluationModes"] else failed).append(label)
    portable = constraints["portableFiles"]
    if portable == "required":
        (reasons if has_portable else failed).append("portableFiles:required")
    elif portable == "forbidden":
        (reasons if not has_portable else failed).append("portableFiles:forbidden")
    return reasons, failed


def resolve(index: dict, constraints: dict) -> dict:
    validate_known_constraints(index, constraints)
    candidates: list[dict] = []
    rejections: list[dict] = []
    for skill in sorted(index["skills"], key=lambda item: item["name"]):
        reasons, failed = evaluate_skill(skill, constraints)
        if failed:
            rejections.append({"name": skill["name"], "failedConstraints": sorted(failed)})
        else:
            output_contracts = [
                contract
                for contract in skill.get("outputContracts", [])
                if contract.get("output") in constraints["outputs"]
            ]
            candidates.append(
                {
                    "name": skill["name"],
                    "matchReasons": sorted(reasons),
                    "matchedOutputContracts": sorted(
                        output_contracts, key=lambda item: item.get("output", "")
                    ),
                }
            )
    return {
        "schemaVersion": SCHEMA_VERSION,
        "constraints": constraints,
        "candidateCount": len(candidates),
        "candidates": candidates,
        "rejections": rejections,
    }


def render_human(payload: dict) -> str:
    if not payload["candidates"]:
        return "No candidates match all explicit constraints."
    lines = []
    for candidate in payload["candidates"]:
        reasons = ", ".join(candidate["matchReasons"]) or "no constraints"
        lines.append(f"{candidate['name']}: {reasons}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve an unranked capability candidate set from exact structured constraints.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Emit stable machine-readable JSON.")
    parser.add_argument("--output", action="append", default=[], help="Require an exact declared output; repeatable.")
    parser.add_argument("--requires", action="append", default=[], help="Require an exact direct skill dependency; repeatable.")
    parser.add_argument("--evaluation-mode", action="append", default=[], help="Allow an exact evaluation mode; repeatable.")
    parser.add_argument(
        "--portable-files",
        choices=sorted(VALID_PORTABLE),
        default="irrelevant",
        help="Require, forbid, or ignore portable files.",
    )
    args = parser.parse_args(argv)
    try:
        constraints = normalize_constraints(args.output, args.requires, args.evaluation_mode, args.portable_files)
        payload = resolve(load_index(args.index), constraints)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
