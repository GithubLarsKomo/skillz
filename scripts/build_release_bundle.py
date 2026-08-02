#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?\Z")


def canonical_json(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_version() -> str:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_RE.fullmatch(version):
        raise ValueError(f"invalid VERSION: {version!r}")
    return version


def load_sync_manifest() -> dict:
    value = json.loads((ROOT / ".skill-sync.json").read_text(encoding="utf-8"))
    if value.get("schemaVersion") != 2 or not isinstance(value.get("skills"), dict):
        raise ValueError("unsupported or malformed .skill-sync.json")
    return value


def payload_paths(sync: dict) -> list[Path]:
    paths = {
        Path("VERSION"),
        Path("README.md"),
        Path(".skill-sync.json"),
        Path("docs/BETA-RUNBOOK.md"),
        Path("docs/BOOTSTRAP.md"),
        Path("scripts/bootstrap_skillz.py"),
    }
    for path in (ROOT / "schemas").glob("*.json"):
        paths.add(path.relative_to(ROOT))
    for skill, spec in sync["skills"].items():
        files = spec.get("files")
        if not isinstance(files, dict) or not files:
            raise ValueError(f"skill {skill} has no portable files")
        for rel in files:
            paths.add(Path("skills") / skill / rel)
    return sorted(paths, key=lambda p: p.as_posix())


def collect_payload() -> tuple[str, dict[str, bytes]]:
    version = load_version()
    sync = load_sync_manifest()
    payload: dict[str, bytes] = {}
    for rel in payload_paths(sync):
        source = ROOT / rel
        if not source.is_file():
            raise ValueError(f"release payload file missing: {rel.as_posix()}")
        payload[rel.as_posix()] = source.read_bytes()
    return version, payload


def build_manifest(version: str, payload: dict[str, bytes]) -> dict:
    return {
        "schemaVersion": 1,
        "name": "skillz",
        "version": version,
        "fileCount": len(payload),
        "files": {path: sha256(data) for path, data in sorted(payload.items())},
    }


def add_bytes(archive: tarfile.TarFile, name: str, data: bytes) -> None:
    info = tarfile.TarInfo(name=name)
    info.size = len(data)
    info.mtime = 0
    info.mode = 0o644
    info.uid = 0
    info.gid = 0
    info.uname = ""
    info.gname = ""
    archive.addfile(info, io.BytesIO(data))


def build(output: Path) -> dict:
    version, payload = collect_payload()
    manifest = build_manifest(version, payload)
    root = f"skillz-{version}"
    output.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(output, mode="w", format=tarfile.PAX_FORMAT) as archive:
        add_bytes(archive, f"{root}/release-manifest.json", canonical_json(manifest))
        for rel, data in sorted(payload.items()):
            add_bytes(archive, f"{root}/{rel}", data)
    return {**manifest, "archive": str(output), "archiveSha256": sha256(output.read_bytes())}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a deterministic skillz release tar archive.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = build(args.output)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
