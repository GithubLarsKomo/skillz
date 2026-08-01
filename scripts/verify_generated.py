#!/usr/bin/env python3
from __future__ import annotations

from generate_repository_metadata import run
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    raise SystemExit(run(ROOT, check=True))
