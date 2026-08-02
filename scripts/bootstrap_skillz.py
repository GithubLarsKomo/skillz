#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".skill-sync.json"


def normalized_bytes(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n").rstrip("\n") + "\n"
    return text.encode("utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(normalized_bytes(path)).hexdigest()


def load_manifest() -> dict:
    value = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if value.get("schemaVersion") != 2 or not isinstance(value.get("skills"), dict):
        raise ValueError("unsupported or malformed .skill-sync.json")
    return value


def verify_source(manifest: dict) -> None:
    for name, spec in manifest["skills"].items():
        files = spec.get("files")
        if not isinstance(files, dict) or not files:
            raise ValueError(f"skill {name} has no portable files")
        for rel, expected in files.items():
            source = ROOT / "skills" / name / rel
            if not source.is_file():
                raise ValueError(f"missing portable file: skills/{name}/{rel}")
            if sha256(source) != expected:
                raise ValueError(f"portable file hash mismatch: skills/{name}/{rel}")


def install(manifest: dict, target_dir: Path, selected: list[str]) -> dict:
    names = sorted(manifest["skills"]) if not selected else sorted(dict.fromkeys(selected))
    unknown = [name for name in names if name not in manifest["skills"]]
    if unknown:
        raise ValueError(f"unknown skill(s): {', '.join(unknown)}")
    target_dir.mkdir(parents=True, exist_ok=True)
    installed: list[dict] = []
    for name in names:
        dest_root = target_dir / name
        files = manifest["skills"][name]["files"]
        for rel, expected in sorted(files.items()):
            source = ROOT / "skills" / name / rel
            dest = dest_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, dest)
            if sha256(dest) != expected:
                raise ValueError(f"installed file verification failed: {name}/{rel}")
        installed.append({"name": name, "path": str(dest_root.resolve()), "fileCount": len(files)})
    return {"schemaVersion": 1, "status": "ready", "targetDir": str(target_dir.resolve()), "installed": installed}


def run_repository_validation() -> None:
    checks = [
        [sys.executable, "scripts/generate_repository_metadata.py", "--check"],
        [sys.executable, "scripts/validate_metadata_schemas.py"],
        [sys.executable, "scripts/validate_skills.py"],
        [sys.executable, "scripts/evaluate_skills.py"],
    ]
    for command in checks:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()
            raise ValueError(f"repository validation failed: {' '.join(command)}: {detail}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a skillz checkout and install portable skills into an explicit target directory.")
    parser.add_argument("--target-dir", type=Path, required=True)
    parser.add_argument("--skill", action="append", default=[], help="Skill to install; repeatable. Omit to install all portable skills.")
    parser.add_argument("--skip-repo-validation", action="store_true", help="Skip repository-wide validation; portable hashes are still verified.")
    args = parser.parse_args(argv)
    try:
        manifest = load_manifest()
        verify_source(manifest)
        if not args.skip_repo_validation:
            run_repository_validation()
        result = install(manifest, args.target_dir, args.skill)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
