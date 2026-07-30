#!/usr/bin/env python3
"""Create a minimal agent context scaffold without overwriting existing files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

FILES = {
    "CONFIG.md": """# Agent Configuration – {project_name}\n\n## Repository\n\n- Project: `{project_name}`\n- Context path: `{context_path}`\n\n## Verified commands\n\n> Add only commands verified in package manifests, Makefiles, task runners, or CI workflows.\n\n- Build: _open_\n- Test: _open_\n- Lint: _open_\n- Type check: _open_\n- Development: _open_\n\n## Relevant paths\n\n- Application code: _open_\n- Tests: _open_\n- Documentation: _open_\n- Migrations: _not confirmed_\n\n## Tracker and workflow\n\n- Issue tracker: _open_\n- Required labels: _open_\n- Branch convention: _open_\n- Pull-request convention: _open_\n\n## Write boundaries\n\n- Allowed targets: _open_\n- Protected targets: secrets, credentials, generated vendor content, and unrelated user changes\n\n## Sources\n\n- Add repository-relative links for every verified command or rule.\n""",
    "CONTEXT.md": """# Domain Context – {project_name}\n\n## Purpose\n\n_open_\n\n## Actors\n\n_open_\n\n## Core concepts\n\n| Term | Meaning | Source | Status |\n|---|---|---|---|\n| _open_ | _open_ | _open_ | unconfirmed |\n\n## System boundaries\n\n- In scope: _open_\n- Out of scope: _open_\n- External systems: _open_\n\n## Important abbreviations\n\n_open_\n\n## Invariants\n\n_open_\n""",
    "DECISIONS.md": """# Decisions – {project_name}\n\n## Existing decision records\n\n- ADR location: _not confirmed_\n\n## Confirmed decisions\n\n| Decision | Rationale | Source | Date |\n|---|---|---|---|\n| _none recorded_ |  |  |  |\n\n## Open decisions\n\n| Question | Options | Owner | Needed by |\n|---|---|---|---|\n| _open_ | _open_ | _open_ | _open_ |\n\n## Superseded decisions\n\n_none recorded_\n""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="Repository root")
    parser.add_argument("--project-name", required=True, help="Human-readable project name")
    parser.add_argument("--target", default="docs/agents", help="Repository-relative output directory")
    parser.add_argument("--dry-run", action="store_true", help="Print planned paths without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = args.repo.expanduser().resolve()
    if not repo.is_dir():
        print(f"error: repository path does not exist: {repo}", file=sys.stderr)
        return 2
    if not (repo / ".git").exists():
        print(f"error: not a git repository root: {repo}", file=sys.stderr)
        return 2

    target = Path(args.target)
    if target.is_absolute() or ".." in target.parts:
        print("error: --target must be a safe repository-relative path", file=sys.stderr)
        return 2

    output_dir = repo / target
    planned = [output_dir / name for name in FILES]
    collisions = [path for path in planned if path.exists()]
    if collisions:
        for path in collisions:
            print(f"error: refusing to overwrite existing file: {path}", file=sys.stderr)
        return 3

    for path in planned:
        print(path.relative_to(repo))
    if args.dry_run:
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    values = {"project_name": args.project_name, "context_path": target.as_posix()}
    for name, template in FILES.items():
        (output_dir / name).write_text(template.format(**values), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
