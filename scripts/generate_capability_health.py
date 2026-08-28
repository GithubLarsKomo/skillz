#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

from generate_capability_index import build_index

REPORT = "docs/CAPABILITY-HEALTH.md"


def build_health(root: Path) -> dict[str, object]:
    index = build_index(root)
    skills = index["skills"]
    missing_evaluations = sorted(
        skill["name"] for skill in skills if skill["evaluation"]["mode"] == "none"
    )
    missing_entrypoint_evaluations = sorted(
        skill["name"]
        for skill in skills
        if skill["invocation"]["userFacing"] and skill["evaluation"]["mode"] == "none"
    )
    ambiguous_outputs: list[dict[str, object]] = []
    unconsumed_outputs: list[dict[str, object]] = []
    seen: set[str] = set()
    for skill in skills:
        for contract in skill["outputContracts"]:
            output = str(contract["output"])
            if output in seen:
                continue
            seen.add(output)
            item = {
                "output": output,
                "producers": list(contract["producers"]),
                "consumerSkills": list(contract["consumerSkills"]),
            }
            if contract["ambiguous"]:
                ambiguous_outputs.append(item)
            elif not contract["consumerSkills"]:
                unconsumed_outputs.append(item)

    skill_count = int(index["skillCount"])
    entrypoint_count = int(index["entrypointCount"])
    evaluated_skill_count = skill_count - len(missing_evaluations)
    evaluated_entrypoint_count = entrypoint_count - len(missing_entrypoint_evaluations)

    return {
        "skillCount": skill_count,
        "entrypointCount": entrypoint_count,
        "discoverabilityCounts": dict(index.get("discoverabilityCounts", {})),
        "evaluationSuiteCount": index["evaluationSuiteCount"],
        "executedEvaluationsPassed": bool(index["evaluationPassed"]),
        "evaluationCoverageComplete": not missing_evaluations,
        "evaluatedSkillCount": evaluated_skill_count,
        "evaluatedEntrypointCount": evaluated_entrypoint_count,
        "missingEvaluations": missing_evaluations,
        "missingEntrypointEvaluations": missing_entrypoint_evaluations,
        "ambiguousOutputs": sorted(ambiguous_outputs, key=lambda item: item["output"]),
        "unconsumedOutputs": sorted(unconsumed_outputs, key=lambda item: item["output"]),
    }


def render_markdown(health: dict[str, object]) -> str:
    missing = health["missingEvaluations"]
    missing_entrypoints = health["missingEntrypointEvaluations"]
    ambiguous = health["ambiguousOutputs"]
    unconsumed = health["unconsumedOutputs"]
    discoverability = health["discoverabilityCounts"]
    executed_pass = "PASS" if health["executedEvaluationsPassed"] else "FAIL"
    coverage = "complete" if health["evaluationCoverageComplete"] else "incomplete"
    lines = [
        "# Capability Health",
        "",
        "Generated from the canonical skill capability index. Do not edit manually.",
        "",
        "## Summary",
        "",
        f"- Skills: **{health['skillCount']}**",
        f"- User-facing entrypoints: **{health['entrypointCount']}**",
        f"- Discoverability — public: **{discoverability.get('public', 0)}**, advanced: **{discoverability.get('advanced', 0)}**, internal: **{discoverability.get('internal', 0)}**, compatibility: **{discoverability.get('compatibility', 0)}**",
        f"- Evaluation suites: **{health['evaluationSuiteCount']}**",
        f"- Executed evaluation suites: **{executed_pass}**",
        f"- Evaluation coverage: **{coverage}**",
        f"- Skills with evaluation suite: **{health['evaluatedSkillCount']}/{health['skillCount']}**",
        f"- User-facing entrypoints with evaluation suite: **{health['evaluatedEntrypointCount']}/{health['entrypointCount']}**",
        f"- Skills without evaluation suite: **{len(missing)}**",
        f"- User-facing entrypoints without evaluation suite: **{len(missing_entrypoints)}**",
        f"- Ambiguous outputs (multiple producers): **{len(ambiguous)}**",
        f"- Outputs without inferred hard-requires consumers: **{len(unconsumed)}**",
        "",
        "Passing executed suites does not imply complete evaluation coverage. Coverage is complete only when every indexed skill has an evaluation suite.",
        "",
        "Discoverability is resolved independently from lifecycle: `public` and `advanced` are user-facing; `internal` is composition-only; `compatibility` is deprecated explicit-use-only surface.",
        "",
        "## Evaluation gaps",
        "",
    ]
    if missing:
        lines.extend(f"- `{name}`" for name in missing)
    else:
        lines.append("None.")
    lines.extend(["", "### User-facing evaluation gaps", ""])
    if missing_entrypoints:
        lines.extend(f"- `{name}`" for name in missing_entrypoints)
    else:
        lines.append("None.")
    lines.extend(["", "## Ambiguous outputs", ""])
    if ambiguous:
        for item in ambiguous:
            producers = ", ".join(f"`{name}`" for name in item["producers"])
            lines.append(f"- `{item['output']}` — producers: {producers}")
    else:
        lines.append("None.")
    lines.extend([
        "",
        "## Outputs without inferred consumers",
        "",
        "These are **not automatically defects**. The dependency graph infers consumers only from hard `requires` edges. User-facing reports, installed artifacts, runbooks, exported notes and other terminal products are expected to appear here. Treat this list as a review queue, not as an orphan verdict.",
        "",
    ])
    if unconsumed:
        for item in unconsumed:
            producers = ", ".join(f"`{name}`" for name in item["producers"])
            lines.append(f"- `{item['output']}` — producer: {producers}")
    else:
        lines.append("None.")
    lines.extend([
        "",
        "## Interpretation",
        "",
        "A true orphan requires additional evidence that an output was intended for downstream machine consumption but has no valid consumer. Absence of a hard dependency alone is insufficient to make that claim.",
    ])
    return "\n".join(lines) + "\n"


def apply(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return False
    if check:
        print(f"STALE: {path}", file=sys.stderr)
        for line in difflib.unified_diff(actual.splitlines(), expected.splitlines(), lineterm=""):
            print(line, file=sys.stderr)
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"UPDATED: {path}")
    return True


def run(root: Path, check: bool) -> int:
    try:
        stale = apply(root / REPORT, render_markdown(build_health(root)), check)
        return 1 if check and stale else 0
    except (OSError, ValueError, KeyError, UnicodeDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic capability health report.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    args = parser.parse_args()
    return run(args.root.resolve(), args.check)


if __name__ == "__main__":
    raise SystemExit(main())
