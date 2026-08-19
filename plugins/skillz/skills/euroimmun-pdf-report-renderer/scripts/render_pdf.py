#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


def convert(input_docx: Path, output_pdf: Path) -> None:
    if input_docx.suffix.lower() != '.docx':
        raise ValueError('input must be a .docx file')
    if not input_docx.is_file():
        raise ValueError(f'input DOCX not found: {input_docx}')
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice:
        raise ValueError('LibreOffice/soffice is required for DOCX-to-PDF conversion')
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='euroimmun_pdf_') as td:
        work = Path(td)
        profile = work / 'lo-profile'
        profile.mkdir()
        cmd = [soffice, f'-env:UserInstallation={profile.as_uri()}', '--headless', '--norestore', '--invisible', '--convert-to', 'pdf', '--outdir', str(work), str(input_docx.resolve())]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
        candidate = work / (input_docx.stem + '.pdf')
        if proc.returncode != 0 or not candidate.is_file() or candidate.stat().st_size == 0:
            detail = (proc.stderr or proc.stdout or '').strip()
            raise ValueError('DOCX-to-PDF conversion failed' + (f': {detail}' if detail else ''))
        shutil.copy2(candidate, output_pdf)


def main() -> int:
    parser = argparse.ArgumentParser(description='Convert the canonical EUROIMMUN DOCX report to PDF without re-authoring content.')
    parser.add_argument('input', type=Path, help='Input .docx produced by euroimmun-docx-report-renderer')
    parser.add_argument('output', type=Path, help='Output .pdf')
    args = parser.parse_args()
    try: convert(args.input, args.output)
    except ValueError as exc: print(f'ERROR: {exc}'); return 2
    print(args.output); return 0


if __name__ == '__main__':
    raise SystemExit(main())
