#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillz_core import (
    VALID_MODES,
    build_status_payload,
    get_skill,
    invocation,
    listing_payload,
    load_index,
    names,
    query_mode,
    query_output,
    query_portable,
    query_requires,
    query_skill_listing,
    render_status_human,
)

DEFAULT_INDEX = ROOT / "docs" / "skill-capability-index.json"
DEFAULT_VERSION = ROOT / "VERSION"


def render_human(kind: str, value: object) -> str:
    if kind == "skill":
        assert isinstance(value, dict)
        meta = invocation(value)
        lines = [value["name"], f"description: {value.get('description', '')}"]
        lines.append(f"userFacing: {str(bool(meta.get('userFacing', False))).lower()}")
        lines.append(f"category: {meta.get('category') or '—'}")
        lines.append("requires: " + (", ".join(value.get("requires", [])) or "—"))
        lines.append("dependents: " + (", ".join(value.get("dependents", [])) or "—"))
        lines.append("outputs: " + (", ".join(value.get("outputs", [])) or "—"))
        lines.append(f"evaluation: {value.get('evaluation', {}).get('mode', 'none')}")
        return "\n".join(lines)
    if kind == "skills":
        assert isinstance(value, dict)
        lines: list[str] = []
        for group in value["categories"]:
            lines.append(f"[{group['category']}]")
            for skill in group["skills"]:
                suffix = "" if skill["userFacing"] else " [internal]"
                lines.append(f"- {skill['name']}{suffix} — {skill['description']}")
        return "\n".join(lines) if lines else "(no matches)"
    if kind == "status":
        assert isinstance(value, dict)
        return render_status_human(value)
    assert isinstance(value, list)
    return "\n".join(value) if value else "(no matches)"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query the committed skill capability index deterministically.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Emit stable JSON output.")
    parser.add_argument("--repository-head", help="Live repository HEAD SHA used by `/skills status`.")
    parser.add_argument("--repository-version", help="Repository version override used by `/skills status`.")
    parser.add_argument("--installed-manifest", type=Path, help="Installed skillz-distribution-manifest.json used by `/skills status`.")
    parser.add_argument("--installed-commit", help="Installed source commit override used by `/skills status`.")
    parser.add_argument("--installed-version", help="Installed plugin version override used by `/skills status`.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill")
    group.add_argument("--skills", nargs="?", const="", metavar="QUERY", help="List user-facing entrypoints; use 'all' for every skill or 'status' for freshness.")
    group.add_argument("--requires")
    group.add_argument("--output")
    group.add_argument("--evaluation-mode", choices=sorted(VALID_MODES))
    group.add_argument("--with-portable-files", action="store_true")
    group.add_argument("--without-portable-files", action="store_true")
    group.add_argument("--dependencies")
    group.add_argument("--dependents")
    args = parser.parse_args(argv)

    try:
        index = load_index(args.index)
        kind = "list"
        if args.skill:
            kind, result = "skill", get_skill(index, args.skill)
        elif args.skills is not None and args.skills.strip().casefold() == "status":
            kind = "status"
            result = build_status_payload(
                index,
                version_path=DEFAULT_VERSION,
                repository_head=args.repository_head,
                repository_version_override=args.repository_version,
                installed_manifest=args.installed_manifest,
                installed_commit=args.installed_commit,
                installed_version=args.installed_version,
            )
        elif args.skills is not None:
            mode, matches = query_skill_listing(index, args.skills)
            kind, result = "skills", listing_payload(mode, args.skills, matches)
        elif args.requires:
            result = names(query_requires(index, args.requires))
        elif args.output:
            result = names(query_output(index, args.output))
        elif args.evaluation_mode:
            result = names(query_mode(index, args.evaluation_mode))
        elif args.with_portable_files:
            result = names(query_portable(index, True))
        elif args.without_portable_files:
            result = names(query_portable(index, False))
        elif args.dependencies:
            result = sorted(get_skill(index, args.dependencies).get("requires", []))
        else:
            result = sorted(get_skill(index, args.dependents).get("dependents", []))
    except (ValueError, LookupError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        if kind in {"skill", "skills", "status"}:
            payload = result
        else:
            payload = {"matches": result, "count": len(result)}
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(kind, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
