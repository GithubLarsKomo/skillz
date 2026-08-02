#!/usr/bin/env python3
"""Probe locally available engineering tools without installing or routing anything."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import platform
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "config" / "tool-capabilities.json"


def load_registry(path: Path = DEFAULT_REGISTRY) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schemaVersion") != 1:
        raise ValueError(f"unsupported capability registry schema: {data.get('schemaVersion')!r}")
    capabilities = data.get("capabilities")
    profiles = data.get("profiles")
    if not isinstance(capabilities, dict) or not isinstance(profiles, dict):
        raise ValueError("capability registry requires object-valued capabilities and profiles")
    for name, spec in capabilities.items():
        providers = spec.get("providers") if isinstance(spec, dict) else None
        if not isinstance(name, str) or not name or not isinstance(providers, list) or not providers:
            raise ValueError(f"invalid capability definition: {name!r}")
        if not all(isinstance(provider, str) and provider for provider in providers):
            raise ValueError(f"invalid provider list for capability: {name}")
    known = set(capabilities)
    for profile, selected in profiles.items():
        if not isinstance(profile, str) or not profile or not isinstance(selected, list) or not selected:
            raise ValueError(f"invalid profile definition: {profile!r}")
        unknown = set(selected) - known
        if unknown:
            raise ValueError(f"profile {profile!r} references unknown capabilities: {sorted(unknown)}")
    return data


def first_version_line(command: str, path: str, version_args: dict[str, list[str]]) -> str | None:
    args = version_args.get(command, ["--version"])
    try:
        completed = subprocess.run(
            [path, *args],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=3,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    for line in completed.stdout.splitlines():
        line = line.strip()
        if line:
            return line[:300]
    return None


def probe(registry: dict | None = None, selected_capabilities: list[str] | None = None) -> dict:
    registry = registry or load_registry()
    capability_specs = registry["capabilities"]
    version_args = registry.get("versionArgs", {})
    selected = sorted(set(selected_capabilities or capability_specs.keys()))
    unknown = sorted(set(selected) - set(capability_specs))
    if unknown:
        raise ValueError(f"unknown capabilities requested: {unknown}")

    verified_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    capabilities = []
    for capability in selected:
        providers = []
        for command in capability_specs[capability]["providers"]:
            path = shutil.which(command)
            if path:
                providers.append(
                    {
                        "capability": capability,
                        "provider": command,
                        "path": path,
                        "version": first_version_line(command, path, version_args),
                        "available": True,
                        "verifiedAt": verified_at,
                    }
                )
        capabilities.append(
            {"capability": capability, "available": bool(providers), "providers": providers}
        )
    return {
        "schemaVersion": 2,
        "verifiedAt": verified_at,
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "capabilities": capabilities,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Probe known local engineering-tool capabilities. No tools are installed, modified, selected for a task, or executed beyond version inspection."
    )
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY, help="Capability registry JSON.")
    parser.add_argument("--profile", help="Probe only the capability bundle declared for this profile.")
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout.")
    parser.add_argument("--require", action="append", default=[], help="Capability that must be available; repeatable.")
    parser.add_argument("--list-capabilities", action="store_true", help="List registry capabilities and profiles as JSON without probing providers.")
    args = parser.parse_args()

    try:
        registry = load_registry(args.registry)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

    if args.list_capabilities:
        print(json.dumps({
            "schemaVersion": 1,
            "capabilities": sorted(registry["capabilities"]),
            "profiles": {name: sorted(values) for name, values in sorted(registry["profiles"].items())},
        }, indent=2, sort_keys=True))
        return 0

    if args.profile and args.profile not in registry["profiles"]:
        payload = {
            "schemaVersion": 2,
            "profile": args.profile,
            "error": "unknown-profile",
            "knownProfiles": sorted(registry["profiles"]),
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 2

    selected = registry["profiles"].get(args.profile) if args.profile else None
    try:
        result = probe(registry=registry, selected_capabilities=selected)
    except ValueError as exc:
        print(json.dumps({"schemaVersion": 2, "error": str(exc)}, indent=2, sort_keys=True))
        return 2

    known = {entry["capability"]: entry["available"] for entry in result["capabilities"]}
    registry_known = set(registry["capabilities"])
    unknown = sorted(set(args.require) - registry_known)
    outside_profile = sorted(cap for cap in args.require if cap in registry_known and cap not in known)
    missing = sorted(cap for cap in args.require if cap in known and not known[cap])
    result["profile"] = args.profile
    result["requirements"] = {
        "requested": args.require,
        "unknown": unknown,
        "outsideProfile": outside_profile,
        "missing": missing,
    }

    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

    if unknown or outside_profile:
        return 2
    if missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
