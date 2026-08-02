#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import qualify_model_provider as qualifier
from score_capability_interpretations import load_json

REGISTRY_SCHEMA_VERSION = 1
QUALIFICATION_SCHEMA_VERSION = 1
DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "qualifications" / "index.json"
DEFAULT_BENCHMARK = Path(__file__).resolve().parents[1] / "benchmarks" / "capability-interpretation-v1.json"
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_registry(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read qualification registry: {exc}") from exc
    if not isinstance(value, dict) or set(value) != {"schemaVersion", "entries"}:
        raise ValueError("qualification registry must contain exactly schemaVersion and entries")
    if value.get("schemaVersion") != REGISTRY_SCHEMA_VERSION:
        raise ValueError(f"unsupported qualification registry schemaVersion {value.get('schemaVersion')!r}")
    entries = value.get("entries")
    if not isinstance(entries, list):
        raise ValueError("qualification registry entries must be an array")
    return value


def validate_entry(entry: object) -> dict:
    required = {"providerId", "modelId", "path"}
    if not isinstance(entry, dict) or set(entry) != required:
        raise ValueError("qualification registry entry must contain exactly providerId, modelId, and path")
    for field in required:
        if not isinstance(entry.get(field), str) or not entry[field].strip():
            raise ValueError(f"qualification registry entry {field} must be non-empty")
    path = Path(entry["path"])
    if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] != "qualifications":
        raise ValueError("qualification artifact path must stay under qualifications/")
    if path.as_posix() == "qualifications/index.json":
        raise ValueError("qualification artifact path cannot reference registry index")
    return entry


def validate_qualification(artifact: object, entry: dict, benchmark: object, capability_index: object) -> dict:
    if not isinstance(artifact, dict):
        raise ValueError("qualification artifact root must be an object")
    if artifact.get("schemaVersion") != QUALIFICATION_SCHEMA_VERSION:
        raise ValueError("unsupported qualification artifact schemaVersion")
    if artifact.get("qualified") is not True:
        raise ValueError("qualification artifact is not qualified")
    if artifact.get("providerId") != entry["providerId"]:
        raise ValueError("qualification artifact providerId does not match registry entry")
    if artifact.get("modelId") != entry["modelId"]:
        raise ValueError("qualification artifact modelId does not match registry entry")
    if artifact.get("benchmarkSha256") != qualifier.fingerprint(benchmark):
        raise ValueError("qualification artifact benchmark fingerprint is stale or mismatched")
    if artifact.get("capabilityIndexSha256") != qualifier.fingerprint(capability_index):
        raise ValueError("qualification artifact capability-index fingerprint is stale or mismatched")
    return artifact


def verify(registry_path: Path, benchmark: object, capability_index: object) -> dict:
    registry = load_registry(registry_path)
    root = registry_path.resolve().parents[1]
    seen: set[tuple[str, str]] = set()
    verified: list[dict] = []
    for raw_entry in registry["entries"]:
        entry = validate_entry(raw_entry)
        identity = (entry["providerId"], entry["modelId"])
        if identity in seen:
            raise ValueError(f"duplicate qualification identity: {identity[0]} / {identity[1]}")
        seen.add(identity)
        artifact_path = root / entry["path"]
        try:
            artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"cannot read qualification artifact {entry['path']}: {exc}") from exc
        validate_qualification(artifact, entry, benchmark, capability_index)
        verified.append({"providerId": entry["providerId"], "modelId": entry["modelId"], "path": entry["path"]})
    return {"schemaVersion": REGISTRY_SCHEMA_VERSION, "entryCount": len(verified), "entries": verified}


def lookup(registry_path: Path, provider_id: str, model_id: str, benchmark: object, capability_index: object) -> dict:
    verified = verify(registry_path, benchmark, capability_index)
    matches = [entry for entry in verified["entries"] if entry["providerId"] == provider_id and entry["modelId"] == model_id]
    if not matches:
        raise ValueError(f"qualification not registered for provider/model: {provider_id} / {model_id}")
    entry = matches[0]
    root = registry_path.resolve().parents[1]
    return json.loads((root / entry["path"]).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify or query the reviewed provider qualification registry.")
    sub = parser.add_subparsers(dest="command", required=True)
    verify_parser = sub.add_parser("verify")
    lookup_parser = sub.add_parser("lookup")
    lookup_parser.add_argument("provider_id")
    lookup_parser.add_argument("model_id")
    for child in (verify_parser, lookup_parser):
        child.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
        child.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
        child.add_argument("--capability-index", type=Path, default=DEFAULT_INDEX)
    args = parser.parse_args(argv)
    try:
        benchmark = load_json(args.benchmark)
        capability_index = load_json(args.capability_index)
        if args.command == "verify":
            result = verify(args.registry, benchmark, capability_index)
        else:
            result = lookup(args.registry, args.provider_id, args.model_id, benchmark, capability_index)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
