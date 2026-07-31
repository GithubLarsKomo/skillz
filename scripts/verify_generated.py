#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
subprocess.run(["python", "scripts/generate_catalog.py"], cwd=ROOT, check=True)
result = subprocess.run(["git", "diff", "--exit-code", "--", "README.md"], cwd=ROOT)
if result.returncode:
    raise SystemExit("README-Katalog ist nicht aktuell. Führe python scripts/generate_catalog.py aus.")
