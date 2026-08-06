#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

START = "<!-- skill-catalog:start -->"
END = "<!-- skill-catalog:end -->"
PORTABLE_DIRS = {"references", "scripts", "assets", "agents"}


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: fehlendes YAML-Frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: nicht abgeschlossenes YAML-Frontmatter")
    data: dict[str, object] = {}
    current_list: str | None = None
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line) and current_list:
            value = re.sub(r"^\s+-\s+", "", line).strip().strip('"\'')
            cast = data.get(current_list)
            if not isinstance(cast, list):
                raise ValueError(f"{path}: {current_list} muss eine YAML-Liste sein")
            cast.append(value)
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            raise ValueError(f"{path}: nicht unterstützte Frontmatter-Zeile: {line}")
        key, value = match.groups()
        value = value.strip()
        if value == "":
            data[key] = []
            current_list = key
        elif value == "[]":
            data[key] = []
            current_list = None
        else:
            data[key] = value.strip('"\'')
            current_list = None
    return data


def normalize_bytes(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    text = text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n") + "\n"
    return text.encode("utf-8")


def sha256_normalized(path: Path) -> str:
    return hashlib.sha256(normalize_bytes(path)).hexdigest()


def skill_files(skill_dir: Path) -> list[Path]:
    files = [skill_dir / "SKILL.md"]
    for dirname in sorted(PORTABLE_DIRS):
        base = skill_dir / dirname
        if base.exists():
            files.extend(sorted(path for path in base.rglob("*") if path.is_file()))
    return files


def build_catalog(root: Path) -> str:
    rows = ["| Skill | Zweck |", "|---|---|"]
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        data = parse_frontmatter(path)
        slug = path.parent.name
        name = data.get("name")
        if name != slug:
            raise ValueError(f"{path}: name '{name}' stimmt nicht mit '{slug}' überein")
        description = str(data.get("description", "")).replace("|", "\\|")
        rows.append(f"| [`{slug}`](skills/{slug}/SKILL.md) | {description} |")
    return START + "\n" + "\n".join(rows) + "\n" + END


def render_readme(root: Path) -> str:
    path = root / "README.md"
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise ValueError("README enthält keine Katalog-Marker")
    return re.sub(re.escape(START) + r".*?" + re.escape(END), build_catalog(root), text, flags=re.DOTALL)


def render_manifest(root: Path) -> str:
    path = root / ".skill-sync.json"
    existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    skills: dict[str, object] = {}
    for skill_md in sorted((root / "skills").glob("*/SKILL.md")):
        slug = skill_md.parent.name
        files: dict[str, str] = {}
        for file in skill_files(skill_md.parent):
            relative = file.relative_to(skill_md.parent).as_posix()
            files[relative] = sha256_normalized(file)
        skills[slug] = {"files": files}
    manifest = {
        "schemaVersion": existing.get("schemaVersion", 2),
        "repository": existing.get("repository", "GithubLarsKomo/skillz"),
        "hashNormalization": "UTF-8; CRLF and CR converted to LF; exactly one trailing LF",
        "synchronizedAt": existing.get("synchronizedAt", "1970-01-01T00:00:00Z"),
        "skills": skills,
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def apply_or_check(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return False
    if check:
        print(f"STALE: {path}", file=sys.stderr)
        return True
    path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"UPDATED: {path}")
    return True


def run_subgenerator(root: Path, script_name: str, check: bool) -> int:
    script = root / "scripts" / script_name
    if not script.exists():
        return 0
    cmd = [sys.executable, str(script), "--root", str(root)]
    if check:
        cmd.append("--check")
    return subprocess.run(cmd, cwd=root, check=False).returncode


def run(root: Path, check: bool) -> int:
    try:
        stale = False
        stale |= apply_or_check(root / "README.md", render_readme(root), check)
        stale |= apply_or_check(root / ".skill-sync.json", render_manifest(root), check)
        for script_name in ("generate_dependency_graph.py", "generate_capability_index.py"):
            result = run_subgenerator(root, script_name, check)
            if result == 2:
                return 2
            stale |= result == 1
        return 1 if check and stale else 0
    except (ValueError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate reproducible repository metadata.")
    parser.add_argument("--check", action="store_true", help="Fail without writing when generated metadata is stale.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    args = parser.parse_args()
    return run(args.root.resolve(), args.check)


if __name__ == "__main__":
    raise SystemExit(main())
