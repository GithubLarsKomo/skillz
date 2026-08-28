from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz
from playwright.sync_api import sync_playwright


def inspect_pdf(path: Path, render_dir: Path, fingerprint_short: str, minimum_pages: int) -> dict:
    doc = fitz.open(path)
    if doc.page_count < minimum_pages:
        raise AssertionError(f"{path.name}: expected at least {minimum_pages} pages, got {doc.page_count}")
    pages = []
    seen_fingerprint = False
    render_dir.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(doc):
        text = page.get_text("text").strip()
        if len(text) < 20:
            raise AssertionError(f"{path.name}: page {i+1} appears blank or underfilled")
        if fingerprint_short in text:
            seen_fingerprint = True
        pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False)
        png = render_dir / f"page-{i+1:02d}.png"
        pix.save(png)
        if pix.width < 500 or pix.height < 500:
            raise AssertionError(f"{path.name}: page {i+1} render unexpectedly small")
        pages.append({"page": i + 1, "textChars": len(text), "width": pix.width, "height": pix.height, "png": str(png)})
    if not seen_fingerprint:
        raise AssertionError(f"{path.name}: fingerprint {fingerprint_short} not visible in rendered PDF text")
    return {"file": str(path), "pageCount": doc.page_count, "pages": pages, "fingerprintVisible": True}


def render_html(html_path: Path, out_dir: Path, fingerprint: str) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        actual = page.locator("body").get_attribute("data-course-fingerprint")
        if actual != fingerprint:
            raise AssertionError("HTML course fingerprint mismatch")
        if page.locator("section.module").count() != 8:
            raise AssertionError("HTML must render all 8 modules")
        page.screenshot(path=str(out_dir / "landing-wide.png"), full_page=True)
        page.pdf(path=str(out_dir / "landing.pdf"), format="A4", print_background=True)
        results.append({"mode": "wide", "width": 1440})
        page.set_viewport_size({"width": 390, "height": 844})
        page.reload(wait_until="networkidle")
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
        if overflow:
            raise AssertionError("HTML narrow render has horizontal overflow")
        page.screenshot(path=str(out_dir / "landing-narrow.png"), full_page=True)
        results.append({"mode": "narrow", "width": 390, "horizontalOverflow": False})
        browser.close()
    return {"html": str(html_path), "renders": results}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.dir / "artifact-manifest.json").read_text(encoding="utf-8"))
    fp = manifest["courseFingerprint"]
    short = fp[:12]
    reports = {
        "courseFingerprint": fp,
        "html": render_html(args.dir / "index.html", args.dir / "renders" / "html", fp),
        "pptxPdf": inspect_pdf(args.dir / "instructor-deck.pdf", args.dir / "renders" / "pptx", short, 10),
        "docxPdf": inspect_pdf(args.dir / "study-guide.pdf", args.dir / "renders" / "docx", short, 9),
    }
    reports["status"] = "PASS"
    (args.dir / "render-qa.json").write_text(json.dumps(reports, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "courseFingerprint": fp, "pptxPages": reports["pptxPdf"]["pageCount"], "docxPages": reports["docxPdf"]["pageCount"]}, indent=2))


if __name__ == "__main__":
    main()
