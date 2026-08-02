#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import openai_compatible_provider as provider
import qualification_registry
from score_capability_interpretations import load_json

REGISTRY_SCHEMA_VERSION = 1
DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "providers" / "index.json"
DEFAULT_QUALIFICATION_REGISTRY = Path(__file__).resolve().parents[1] / "qualifications" / "index.json"
DEFAULT_BENCHMARK = Path(__file__).resolve().parents[1] / "benchmarks" / "capability-interpretation-v1.json"
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_registry(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read provider config registry: {exc}") from exc
    if not isinstance(value, dict) or set(value) != {"schemaVersion", "entries"}:
        raise ValueError("provider config registry must contain exactly schemaVersion and entries")
    if value.get("schemaVersion") != REGISTRY_SCHEMA_VERSION:
        raise ValueError(f"unsupported provider config registry schemaVersion {value.get('schemaVersion')!r}")
    if not isinstance(value.get("entries"), list):
        raise ValueError("provider config registry entries must be an array")
    return value


def validate_entry(entry: object) -> dict:
    required = {"providerId", "modelId", "path"}
    if not isinstance(entry, dict) or set(entry) != required:
        raise ValueError("provider config registry entry must contain exactly providerId, modelId, and path")
    for field in required:
        if not isinstance(entry.get(field), str) or not entry[field].strip():
            raise ValueError(f"provider config registry entry {field} must be non-empty")
    path = Path(entry["path"])
    if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] != "providers":
        raise ValueError("provider config path must stay under providers/")
    if path.as_posix() == "providers/index.json":
        raise ValueError("provider config path cannot reference registry index")
    return entry


def load_config(root: Path, entry: dict) -> dict:
    try:
        config = json.loads((root / entry["path"]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read provider config {entry['path']}: {exc}") from exc
    config = provider.validate_config(config)
    if config["providerId"] != entry["providerId"]:
        raise ValueError("provider config providerId does not match registry entry")
    if config["modelId"] != entry["modelId"]:
        raise ValueError("provider config modelId does not match registry entry")
    return config


def verify(registry_path: Path) -> dict:
    registry = load_registry(registry_path)
    root = registry_path.resolve().parents[1]
    seen: set[tuple[str, str]] = set()
    verified: list[dict] = []
    for raw in registry["entries"]:
        entry = validate_entry(raw)
        identity = (entry["providerId"], entry["modelId"])
        if identity in seen:
            raise ValueError(f"duplicate provider config identity: {identity[0]} / {identity[1]}")
        seen.add(identity)
        load_config(root, entry)
        verified.append(entry)
    return {"schemaVersion": REGISTRY_SCHEMA_VERSION, "entryCount": len(verified), "entries": verified}


def lookup(registry_path: Path, provider_id: str, model_id: str) -> dict:
    registry = load_registry(registry_path)
    root = registry_path.resolve().parents[1]
    matches = []
    for raw in registry["entries"]:
        entry = validate_entry(raw)
        if entry["providerId"] == provider_id and entry["modelId"] == model_id:
            matches.append(entry)
    if not matches:
        raise ValueError(f"provider config not registered for provider/model: {provider_id} / {model_id}")
    if len(matches) != 1:
        raise ValueError(f"duplicate provider config identity: {provider_id} / {model_id}")
    return load_config(root, matches[0])


def resolve_pair(provider_registry_path: Path, qualification_registry_path: Path, provider_id: str, model_id: str, benchmark: object, capability_index: object) -> tuple[dict, dict]:
    config = lookup(provider_registry_path, provider_id, model_id)
    qualification = qualification_registry.lookup(
        qualification_registry_path, provider_id, model_id, benchmark, capability_index
    )
    provider.verify_qualification(config, qualification, benchmark, capability_index)
    return config, qualification


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify or query the reviewed provider config registry.")
    sub = parser.add_subparsers(dest="command", required=True)
    verify_parser = sub.add_parser("verify")
    lookup_parser = sub.add_parser("lookup")
    pair_parser = sub.add_parser("resolve-pair")
    for child in (verify_parser, lookup_parser, pair_parser):
        child.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    for child in (lookup_parser, pair_parser):
        child.add_argument("provider_id")
        child.add_argument("model_id")
    pair_parser.add_argument("--qualification-registry", type=Path, default=DEFAULT_QUALIFICATION_REGISTRY)
    pair_parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    pair_parser.add_argument("--capability-index", type=Path, default=DEFAULT_INDEX)
    args = parser.parse_args(argv)
    try:
        if args.command == "verify":
            result = verify(args.registry)
        elif args.command == "lookup":
            result = lookup(args.registry, args.provider_id, args.model_id)
        else:
            benchmark = load_json(args.benchmark)
            capability_index = load_json(args.capability_index)
            config, qualification = resolve_pair(
                args.registry, args.qualification_registry, args.provider_id, args.model_id, benchmark, capability_index
            )
            result = {"providerConfig": config, "qualification": qualification}
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
