#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- skill-catalog:start -->"
END = "<!-- skill-catalog:end -->"


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.+)$", line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip('"\'')
    return data


def main() -> int:
    rows = ["| Skill | Zweck |", "|---|---|"]
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        data = frontmatter(path)
        slug = path.parent.name
        description = data.get("description", "").replace("|", "\\|")
        rows.append(f"| [`{slug}`](skills/{slug}/SKILL.md) | {description} |")
    block = START + "\n" + "\n".join(rows) + "\n" + END
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("README enthält keine Katalog-Marker")
    text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.DOTALL)
    README.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
