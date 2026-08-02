#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import openai_compatible_provider as provider
from model_interpretation_request_contract import canonical_json
from provider_qualification_config import fingerprint as config_fingerprint

BUNDLE_SCHEMA_VERSION = 1
QUALIFICATION_SCHEMA_VERSION = 2


def sha256(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def build_bundle(config: object, qualification: object) -> dict:
    config = provider.validate_config(config)
    if not isinstance(qualification, dict):
        raise ValueError("qualification root must be an object")
    if qualification.get("schemaVersion") != QUALIFICATION_SCHEMA_VERSION:
        raise ValueError("promotion requires qualification schemaVersion 2")
    if qualification.get("qualified") is not True:
        raise ValueError("promotion requires qualified evidence")
    if qualification.get("providerId") != config["providerId"] or qualification.get("modelId") != config["modelId"]:
        raise ValueError("provider/model identity mismatch between config and qualification")
    expected_config_sha = config_fingerprint(config["providerId"], config["modelId"], config)
    if qualification.get("providerConfigSha256") != expected_config_sha:
        raise ValueError("qualification provider-config fingerprint is stale or mismatched")
    manifest = {
        "schemaVersion": BUNDLE_SCHEMA_VERSION,
        "providerId": config["providerId"],
        "modelId": config["modelId"],
        "providerConfigSha256": expected_config_sha,
        "qualificationSha256": sha256(qualification),
        "benchmarkSha256": qualification.get("benchmarkSha256"),
        "capabilityIndexSha256": qualification.get("capabilityIndexSha256"),
    }
    return {"manifest": manifest, "providerConfig": config, "qualification": qualification}


def write_bundle(bundle: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "provider-config.json").write_text(canonical_json(bundle["providerConfig"]) + "\n", encoding="utf-8")
    (output_dir / "qualification.json").write_text(canonical_json(bundle["qualification"]) + "\n", encoding="utf-8")
    (output_dir / "manifest.json").write_text(canonical_json(bundle["manifest"]) + "\n", encoding="utf-8")


def load(path: Path, label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} root must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a secrets-free provider qualification promotion bundle.")
    parser.add_argument("provider_config", type=Path)
    parser.add_argument("qualification", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args(argv)
    try:
        bundle = build_bundle(load(args.provider_config, "provider config"), load(args.qualification, "qualification"))
        write_bundle(bundle, args.output_dir)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(bundle["manifest"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
