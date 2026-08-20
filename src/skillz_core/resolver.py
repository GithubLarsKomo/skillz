from __future__ import annotations

from .catalog import skills_by_name

VALID_MODES = {"rubric", "compatibility", "none"}
VALID_PORTABLE = {"required", "forbidden", "irrelevant"}


def normalize_constraints(outputs: list[str], dependencies: list[str], modes: list[str], portable_files: str) -> dict:
    outputs = sorted(set(outputs))
    dependencies = sorted(set(dependencies))
    modes = sorted(set(modes))
    unknown_modes = [mode for mode in modes if mode not in VALID_MODES]
    if unknown_modes:
        raise ValueError(f"unsupported evaluation mode(s): {', '.join(unknown_modes)}")
    if portable_files not in VALID_PORTABLE:
        raise ValueError(f"unsupported portable-files constraint: {portable_files}")
    return {"outputs": outputs, "dependencies": dependencies, "evaluationModes": modes, "portableFiles": portable_files}


def validate_known_constraints(index: dict, constraints: dict) -> None:
    skill_names = set(skills_by_name(index))
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
            candidates.append({
                "name": skill["name"],
                "matchReasons": sorted(reasons),
                "matchedOutputContracts": sorted(output_contracts, key=lambda item: item.get("output", "")),
            })
    return {
        "schemaVersion": 1,
        "constraints": constraints,
        "candidateCount": len(candidates),
        "candidates": candidates,
        "rejections": rejections,
    }
