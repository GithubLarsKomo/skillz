#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat
except ImportError as exc:
    raise SystemExit("ERROR: Pillow is required for visual parity verification") from exc


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise ValueError(f"required tool not found: {name}")
    return path


def run(cmd: list[str], *, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        raise ValueError(f"command failed ({' '.join(cmd)}): {detail}")
    return proc


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_docx_reference(docx: Path, out_pdf: Path) -> None:
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        raise ValueError("LibreOffice/soffice is required for DOCX reference rendering")
    with tempfile.TemporaryDirectory(prefix="dk_visual_ref_") as td:
        work = Path(td)
        profile = work / "lo-profile"
        profile.mkdir()
        run([
            soffice,
            f"-env:UserInstallation={profile.as_uri()}",
            "--headless",
            "--norestore",
            "--invisible",
            "--convert-to",
            "pdf",
            "--outdir",
            str(work),
            str(docx.resolve()),
        ])
        candidate = work / f"{docx.stem}.pdf"
        if not candidate.is_file() or candidate.stat().st_size == 0:
            raise ValueError("DOCX reference rendering did not produce a PDF")
        out_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(candidate, out_pdf)


def rasterize(pdf: Path, out_dir: Path, dpi: int) -> list[Path]:
    pdftoppm = require_tool("pdftoppm")
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = out_dir / "page"
    run([pdftoppm, "-png", "-r", str(dpi), str(pdf), str(prefix)], timeout=180)
    pages = sorted(out_dir.glob("page-*.png"))
    if not pages:
        raise ValueError(f"no page images produced for {pdf}")
    normalized: list[Path] = []
    for index, page in enumerate(pages, 1):
        target = out_dir / f"page-{index:03d}.png"
        if page != target:
            page.replace(target)
        normalized.append(target)
    return normalized


def extract_page_text(pdf: Path, page: int) -> str:
    pdftotext = require_tool("pdftotext")
    proc = run([pdftotext, "-f", str(page), "-l", str(page), "-layout", str(pdf), "-"])
    lines = [line.rstrip() for line in proc.stdout.replace("\r\n", "\n").split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def make_comparison(reference: Image.Image, candidate: Image.Image, diff: Image.Image, output: Path) -> None:
    width, height = reference.size
    gutter = 24
    label_h = 36
    canvas = Image.new("RGB", (width * 3 + gutter * 2, height + label_h), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    for idx, (label, image) in enumerate([
        ("DOCX-rendered reference", reference),
        ("candidate PDF", candidate),
        ("absolute pixel diff", diff),
    ]):
        x = idx * (width + gutter)
        draw.text((x + 4, 10), label, fill="black", font=font)
        canvas.paste(image, (x, label_h))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def compare_page(
    reference_path: Path,
    candidate_path: Path,
    output_dir: Path,
    page_number: int,
    max_mae: float,
    max_changed_fraction: float,
    pixel_threshold: int,
) -> dict:
    reference = Image.open(reference_path).convert("RGB")
    candidate = Image.open(candidate_path).convert("RGB")
    dimensions_equal = reference.size == candidate.size
    if not dimensions_equal:
        return {
            "page": page_number,
            "pass": False,
            "dimensionsEqual": False,
            "referenceSize": list(reference.size),
            "candidateSize": list(candidate.size),
            "meanAbsoluteDifference": None,
            "maxChannelDifference": None,
            "changedPixelFraction": 1.0,
        }

    diff = ImageChops.difference(reference, candidate)
    stat = ImageStat.Stat(diff)
    mae = sum(stat.mean) / len(stat.mean)
    extrema = diff.getextrema()
    max_channel_diff = max(high for _low, high in extrema)
    gray = diff.convert("L")
    mask = gray.point(lambda value: 255 if value > pixel_threshold else 0)
    histogram = mask.histogram()
    changed = histogram[255]
    pixels = reference.size[0] * reference.size[1]
    changed_fraction = changed / pixels if pixels else 1.0

    diff_output = output_dir / "diff" / f"page-{page_number:03d}.png"
    diff_output.parent.mkdir(parents=True, exist_ok=True)
    diff.save(diff_output)
    make_comparison(
        reference,
        candidate,
        diff,
        output_dir / "comparison" / f"page-{page_number:03d}.png",
    )

    passed = mae <= max_mae and changed_fraction <= max_changed_fraction
    return {
        "page": page_number,
        "pass": passed,
        "dimensionsEqual": True,
        "referenceSize": list(reference.size),
        "candidateSize": list(candidate.size),
        "meanAbsoluteDifference": round(mae, 6),
        "maxChannelDifference": int(max_channel_diff),
        "changedPixelFraction": round(changed_fraction, 8),
    }


def verify(
    docx: Path,
    candidate_pdf: Path,
    output_dir: Path,
    *,
    dpi: int,
    max_mae: float,
    max_changed_fraction: float,
    pixel_threshold: int,
) -> dict:
    if docx.suffix.lower() != ".docx" or not docx.is_file():
        raise ValueError(f"valid DOCX required: {docx}")
    if candidate_pdf.suffix.lower() != ".pdf" or not candidate_pdf.is_file():
        raise ValueError(f"valid candidate PDF required: {candidate_pdf}")
    require_tool("pdftoppm")
    require_tool("pdftotext")

    output_dir.mkdir(parents=True, exist_ok=True)
    reference_pdf = output_dir / "docx-reference.pdf"
    render_docx_reference(docx, reference_pdf)

    ref_pages = rasterize(reference_pdf, output_dir / "docx-pages", dpi)
    cand_pages = rasterize(candidate_pdf, output_dir / "pdf-pages", dpi)
    page_count_equal = len(ref_pages) == len(cand_pages)

    page_results: list[dict] = []
    text_results: list[dict] = []
    comparable_pages = min(len(ref_pages), len(cand_pages))
    for page in range(1, comparable_pages + 1):
        ref_text = extract_page_text(reference_pdf, page)
        cand_text = extract_page_text(candidate_pdf, page)
        ref_hash = text_hash(ref_text)
        cand_hash = text_hash(cand_text)
        text_equal = ref_hash == cand_hash
        text_results.append({
            "page": page,
            "pass": text_equal,
            "referenceTextSha256": ref_hash,
            "candidateTextSha256": cand_hash,
        })
        page_result = compare_page(
            ref_pages[page - 1],
            cand_pages[page - 1],
            output_dir,
            page,
            max_mae,
            max_changed_fraction,
            pixel_threshold,
        )
        page_result["textEqual"] = text_equal
        page_result["pass"] = bool(page_result["pass"] and text_equal)
        page_results.append(page_result)

    text_page_mapping_equal = page_count_equal and all(item["pass"] for item in text_results)
    pixel_parity = page_count_equal and all(item["pass"] for item in page_results)
    reflow_detected = not (page_count_equal and text_page_mapping_equal and pixel_parity)
    passed = not reflow_detected

    result = {
        "schemaVersion": 1,
        "pass": passed,
        "reflowDetected": reflow_detected,
        "inputs": {
            "docx": str(docx),
            "docxSha256": sha256(docx),
            "candidatePdf": str(candidate_pdf),
            "candidatePdfSha256": sha256(candidate_pdf),
            "referencePdfSha256": sha256(reference_pdf),
        },
        "criteria": {
            "dpi": dpi,
            "pageCountMustMatch": True,
            "perPageTextHashMustMatch": True,
            "meanAbsoluteDifferenceMax": max_mae,
            "changedPixelFractionMax": max_changed_fraction,
            "pixelDifferenceThreshold": pixel_threshold,
        },
        "summary": {
            "referencePages": len(ref_pages),
            "candidatePages": len(cand_pages),
            "pageCountEqual": page_count_equal,
            "textPageMappingEqual": text_page_mapping_equal,
            "pixelParity": pixel_parity,
        },
        "pages": page_results,
    }
    report_path = output_dir / "visual-parity.json"
    report_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify DOCX↔PDF visual parity for Dr. Komorowski sport reports.")
    parser.add_argument("docx", type=Path)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=171)
    parser.add_argument("--max-mae", type=float, default=0.25)
    parser.add_argument("--max-changed-fraction", type=float, default=0.001)
    parser.add_argument("--pixel-threshold", type=int, default=8)
    args = parser.parse_args()
    if not 72 <= args.dpi <= 300:
        print("ERROR: --dpi must be between 72 and 300")
        return 2
    if args.max_mae < 0 or not 0 <= args.max_changed_fraction <= 1 or not 0 <= args.pixel_threshold <= 255:
        print("ERROR: invalid comparison thresholds")
        return 2
    try:
        result = verify(
            args.docx,
            args.pdf,
            args.output_dir,
            dpi=args.dpi,
            max_mae=args.max_mae,
            max_changed_fraction=args.max_changed_fraction,
            pixel_threshold=args.pixel_threshold,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    print(json.dumps(result["summary"], sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
