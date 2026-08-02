#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import build_provider_promotion_bundle as bundle_builder
import provider_config_registry
import provider_identity_key
import qualification_registry
from score_capability_interpretations import load_json

EXPECTED_BUNDLE_FILES = {"manifest.json", "provider-config.json", "qualification.json"}


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def pretty_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=False, indent=2) + "\n"


def read_json(path: Path, label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} root must be an object")
    return value


def sorted_registry(registry: dict, entry: dict) -> dict:
    entries = [*registry["entries"], entry]
    entries.sort(key=lambda row: (row["providerId"], row["modelId"], row["path"]))
    return {"schemaVersion": registry["schemaVersion"], "entries": entries}


def load_bundle(bundle_dir: Path) -> dict:
    try:
        names = {path.name for path in bundle_dir.iterdir() if path.is_file()}
    except OSError as exc:
        raise ValueError(f"cannot inspect promotion bundle: {exc}") from exc
    if names != EXPECTED_BUNDLE_FILES:
        raise ValueError("promotion bundle must contain exactly manifest.json, provider-config.json, and qualification.json")
    config = read_json(bundle_dir / "provider-config.json", "provider config")
    qualification = read_json(bundle_dir / "qualification.json", "qualification")
    manifest = read_json(bundle_dir / "manifest.json", "manifest")
    rebuilt = bundle_builder.build_bundle(config, qualification)
    if manifest != rebuilt["manifest"]:
        raise ValueError("promotion bundle manifest is stale or mismatched")
    return rebuilt


def _identity_registered(registry: dict, provider_id: str, model_id: str) -> bool:
    return any(entry.get("providerId") == provider_id and entry.get("modelId") == model_id for entry in registry["entries"])


def prepare(bundle_dir: Path, repo_root: Path) -> dict:
    repo_root = repo_root.resolve()
    bundle = load_bundle(bundle_dir)
    config = bundle["providerConfig"]
    qualification = bundle["qualification"]
    provider_id = config["providerId"]
    model_id = config["modelId"]
    identity_key = provider_identity_key.identity_key(provider_id, model_id)
    stem = f"{identity_key}.json"

    provider_registry_path = repo_root / "providers" / "index.json"
    qualification_registry_path = repo_root / "qualifications" / "index.json"
    provider_registry = provider_config_registry.load_registry(provider_registry_path)
    qualification_index = qualification_registry.load_registry(qualification_registry_path)
    if _identity_registered(provider_registry, provider_id, model_id) or _identity_registered(qualification_index, provider_id, model_id):
        raise ValueError(f"provider/model identity is already registered: {provider_id} / {model_id}")

    provider_rel = f"providers/{stem}"
    qualification_rel = f"qualifications/{stem}"
    provider_entry = provider_config_registry.validate_entry({"providerId": provider_id, "modelId": model_id, "path": provider_rel})
    qualification_entry = qualification_registry.validate_entry({"providerId": provider_id, "modelId": model_id, "path": qualification_rel})
    provider_path = repo_root / provider_rel
    qualification_path = repo_root / qualification_rel
    if provider_path.exists() or qualification_path.exists():
        raise ValueError("promotion target path already exists")

    benchmark = load_json(repo_root / "benchmarks" / "capability-interpretation-v1.json")
    capability_index = load_json(repo_root / "docs" / "skill-capability-index.json")
    qualification_registry.validate_qualification(qualification, qualification_entry, benchmark, capability_index)

    return {
        "schemaVersion": 1,
        "identityKey": identity_key,
        "providerId": provider_id,
        "modelId": model_id,
        "providerPath": provider_rel,
        "qualificationPath": qualification_rel,
        "providerEntry": provider_entry,
        "qualificationEntry": qualification_entry,
        "providerRegistry": sorted_registry(provider_registry, provider_entry),
        "qualificationRegistry": sorted_registry(qualification_index, qualification_entry),
        "providerConfig": config,
        "qualification": qualification,
        "manifest": bundle["manifest"],
    }


def public_plan(plan: dict, applied: bool) -> dict:
    return {
        "schemaVersion": 1,
        "status": "applied" if applied else "dry-run",
        "identityKey": plan["identityKey"],
        "providerId": plan["providerId"],
        "modelId": plan["modelId"],
        "writes": [
            plan["providerPath"],
            plan["qualificationPath"],
            "providers/index.json",
            "qualifications/index.json",
        ],
        "providerEntry": plan["providerEntry"],
        "qualificationEntry": plan["qualificationEntry"],
        "providerConfigSha256": plan["manifest"]["providerConfigSha256"],
        "qualificationSha256": plan["manifest"]["qualificationSha256"],
    }


def verify_applied(repo_root: Path, plan: dict) -> None:
    benchmark = load_json(repo_root / "benchmarks" / "capability-interpretation-v1.json")
    capability_index = load_json(repo_root / "docs" / "skill-capability-index.json")
    provider_registry_path = repo_root / "providers" / "index.json"
    qualification_registry_path = repo_root / "qualifications" / "index.json"
    provider_config_registry.verify(provider_registry_path)
    qualification_registry.verify(qualification_registry_path, benchmark, capability_index)
    provider_config_registry.resolve_pair(
        provider_registry_path,
        qualification_registry_path,
        plan["providerId"],
        plan["modelId"],
        benchmark,
        capability_index,
    )


def apply(plan: dict, repo_root: Path) -> dict:
    repo_root = repo_root.resolve()
    paths = {
        repo_root / plan["providerPath"]: canonical_json(plan["providerConfig"]) + "\n",
        repo_root / plan["qualificationPath"]: canonical_json(plan["qualification"]) + "\n",
        repo_root / "providers" / "index.json": pretty_json(plan["providerRegistry"]),
        repo_root / "qualifications" / "index.json": pretty_json(plan["qualificationRegistry"]),
    }
    snapshots: dict[Path, bytes | None] = {}
    for path in paths:
        try:
            snapshots[path] = path.read_bytes() if path.exists() else None
        except OSError as exc:
            raise ValueError(f"cannot snapshot {path}: {exc}") from exc
    try:
        for path, text in paths.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        verify_applied(repo_root, plan)
    except (OSError, ValueError) as exc:
        restore_errors: list[str] = []
        for path, original in snapshots.items():
            try:
                if original is None:
                    path.unlink(missing_ok=True)
                else:
                    path.write_bytes(original)
            except OSError as restore_exc:
                restore_errors.append(f"{path}: {restore_exc}")
        if restore_errors:
            raise ValueError(f"promotion failed ({exc}); rollback also failed: {'; '.join(restore_errors)}") from exc
        raise ValueError(f"promotion failed and was rolled back: {exc}") from exc
    return public_plan(plan, True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare a reviewed provider registry promotion from an extracted promotion bundle.")
    parser.add_argument("bundle_dir", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--apply", action="store_true", help="Write and verify the four registry files; default is dry-run")
    args = parser.parse_args(argv)
    try:
        plan = prepare(args.bundle_dir, args.repo_root)
        result = apply(plan, args.repo_root) if args.apply else public_plan(plan, False)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
