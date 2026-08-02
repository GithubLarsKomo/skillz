#!/usr/bin/env python3
"""Probe locally available engineering-analysis tools without installing anything."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import platform
import shutil
import subprocess
from pathlib import Path

PROVIDERS = {
    "binary-inspection": ["objdump", "llvm-objdump", "readelf", "otool", "dumpbin"],
    "archive-extraction": ["7z", "7zz", "unzip", "tar"],
    "structured-text": ["jq", "python", "python3"],
    "network-capture": ["tshark", "tcpdump", "dumpcap"],
    "http-observation": ["curl", "mitmproxy", "mitmdump"],
    "runtime-tracing": ["strace", "dtruss", "procmon", "ltrace"],
    "file-identification": ["file"],
    "string-extraction": ["strings"],
}

VERSION_ARGS = {
    "dumpbin": ["/?"],
    "procmon": ["/?"],
    "tar": ["--version"],
    "unzip": ["-v"],
}


def first_version_line(command: str, path: str) -> str | None:
    args = VERSION_ARGS.get(command, ["--version"])
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


def probe() -> dict:
    verified_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    capabilities = []
    for capability, commands in sorted(PROVIDERS.items()):
        providers = []
        for command in commands:
            path = shutil.which(command)
            if path:
                providers.append(
                    {
                        "capability": capability,
                        "provider": command,
                        "path": path,
                        "version": first_version_line(command, path),
                        "available": True,
                        "verifiedAt": verified_at,
                    }
                )
        capabilities.append(
            {
                "capability": capability,
                "available": bool(providers),
                "providers": providers,
            }
        )
    return {
        "schemaVersion": 1,
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
        description="Probe known local tools and emit capability-oriented JSON. No tools are installed or modified."
    )
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout.")
    parser.add_argument("--require", action="append", default=[], help="Capability that must be available; repeatable.")
    args = parser.parse_args()

    result = probe()
    known = {entry["capability"]: entry["available"] for entry in result["capabilities"]}
    unknown = sorted(set(args.require) - set(known))
    missing = sorted(cap for cap in args.require if cap in known and not known[cap])
    result["requirements"] = {"requested": args.require, "unknown": unknown, "missing": missing}

    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

    if unknown:
        return 2
    if missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
