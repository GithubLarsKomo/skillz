#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
SYNC = ROOT / ".skill-sync.json"
REQUIRED_SECTIONS = [
    "Trigger", "Voraussetzungen", "Ablauf", "Prüfungen",
    "Fehlerbehandlung", "Übergabe", "Abschlusskriterien",
]


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("fehlendes YAML-Frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("nicht abgeschlossenes YAML-Frontmatter")
    raw = text[4:end]
    data: dict[str, object] = {}
    current_list: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line) and current_list:
            value = re.sub(r"^\s+-\s+", "", line).strip().strip('"\'')
            cast = data.setdefault(current_list, [])
            if isinstance(cast, list):
                cast.append(value)
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            raise ValueError(f"nicht unterstützte Frontmatter-Zeile: {line}")
        key, value = match.groups()
        value = value.strip()
        if value in ("", "[]"):
            data[key] = [] if value == "[]" else ""
            current_list = key
        else:
            data[key] = value.strip('"\'')
            current_list = None
    return data, text[end + 5 :]


def frontmatter_true(value: object) -> bool:
    return isinstance(value, str) and value.strip().lower() == "true"


def main() -> int:
    errors: list[str] = []
    skills: dict[str, Path] = {}
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        slug = skill_file.parent.name
        try:
            fm, body = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file.relative_to(ROOT)}: {exc}")
            continue
        name = fm.get("name")
        description = fm.get("description")
        if name != slug:
            errors.append(f"{skill_file.relative_to(ROOT)}: name '{name}' stimmt nicht mit '{slug}' überein")
        if not isinstance(description, str) or len(description.strip()) < 20:
            errors.append(f"{skill_file.relative_to(ROOT)}: description fehlt oder ist zu kurz")
        if slug in skills:
            errors.append(f"doppelter Skillname: {slug}")
        skills[slug] = skill_file

        evaluation = skill_file.parent / "tests" / "evaluation.json"
        status = str(fm.get("status", "")).strip().lower()
        user_facing = frontmatter_true(fm.get("userFacing"))
        if status == "stable" and user_facing and not evaluation.exists():
            errors.append(
                f"{skill_file.relative_to(ROOT)}: stabiler user-facing Entrypoint ohne tests/evaluation.json"
            )
        elif status == "candidate" and user_facing and not evaluation.exists():
            print(
                f"WARN: {skill_file.relative_to(ROOT)} ist user-facing candidate ohne tests/evaluation.json"
            )
        elif status == "deprecated" and not evaluation.exists():
            print(
                f"WARN: {skill_file.relative_to(ROOT)} ist deprecated ohne Compatibility-Evaluation"
            )
        elif not user_facing and status != "deprecated" and not evaluation.exists():
            print(f"WARN: {skill_file.relative_to(ROOT)} enthält keine Evaluation-Suite")

        for section in REQUIRED_SECTIONS:
            if not re.search(rf"^##+\s+{re.escape(section)}\s*$", body, re.MULTILINE | re.IGNORECASE):
                print(f"WARN: {skill_file.relative_to(ROOT)} enthält keinen Abschnitt '{section}'")

    readme = README.read_text(encoding="utf-8")
    for slug in skills:
        if f"skills/{slug}/SKILL.md" not in readme:
            errors.append(f"README-Katalog fehlt: {slug}")

    sync = json.loads(SYNC.read_text(encoding="utf-8"))
    sync_skills = set(sync.get("skills", {}))
    missing = set(skills) - sync_skills
    extra = sync_skills - set(skills)
    if missing:
        errors.append(".skill-sync.json fehlen Skills: " + ", ".join(sorted(missing)))
    if extra:
        errors.append(".skill-sync.json enthält unbekannte Skills: " + ", ".join(sorted(extra)))

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^]]+\]\((?!https?://|#)([^)]+)\)", text):
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: defekter Link '{target}'")

    if errors:
        print("Skill-Validierung fehlgeschlagen:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(skills)} Skills validiert")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
