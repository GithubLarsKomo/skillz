# Large Golden Reference — PCR/qPCR Course Builder

Status: **binding render-based golden reference**  
Version: 1.0  
Date: 2026-08-28

## Purpose

This reference exercises the complete Course Builder on a realistically sized source set. It is intentionally larger than the compact PCR/qPCR semantic fixture and verifies that one canonical course model can drive a landing page, course-map SVG, instructor presentation and study guide without semantic drift.

## Real source set

The fixture freezes 12 publicly identifiable YouTube videos that were manually verified on 2026-08-28:

- Thermo Fisher Scientific — PCR introduction, components and primer design;
- Addgene — practical PCR protocol/workflow;
- Bio-Rad Laboratories — the seven-part *Achieving the Ultimate qPCR Experiment* sequence covering introduction, planning, major error sources, primer/sample validation, reference genes, data analysis and workflow synthesis;
- University of Western Australia BIOC3001 student teaching material — melt-curve analysis.

CI deliberately does **not** download videos, captions or transcripts. Live retrieval would turn a golden reference into a network/platform availability test. Source identity and didactic role are frozen in `tests/fixtures/youtube-learning/pcr-qpcr-course-large-golden.json`; source refresh is a separate manual verification activity.

## Canonical learning path

The Course Builder must reorganize the source set around competencies rather than video order:

1. **M1 — Why PCR works**: purpose and functional components.
2. **M2 — PCR cycle mental model**: denaturation, annealing, extension.
3. **M3 — Primer design and specificity**.
4. **M4 — Laboratory workflow and error localization**.
5. **M5 — qPCR as quantitative extension**.
6. **M6 — qPCR planning and validation**.
7. **M7 — Normalization and reference genes**.
8. **M8 — Data analysis, melt curve and qualified interpretation**.

Mandatory prerequisite edges form a DAG. qPCR remains an extension/variant of the PCR core rather than being flattened into the foundation layer.

## Generated package

`scripts/generate_youtube_course_large_golden.py` produces from the frozen fixture:

- `course-learning-model.json` — canonical semantic model and Course-Fingerprint;
- `course-map.svg` — prerequisite-oriented learning-path visual;
- `index.html` — responsive self-study landing page;
- `instructor-deck.pptx` — overview plus one module slide per module and formative-check slide;
- `study-guide.docx` — printable study guide with module objectives, checkpoints and source map;
- `artifact-manifest.json` — package provenance.

The workflow then converts:

- PPTX -> PDF with headless LibreOffice;
- DOCX -> PDF with headless LibreOffice;
- HTML -> browser screenshot/PDF with Chromium via Playwright.

## Render-based QA

`scripts/verify_youtube_course_large_golden_render.py` enforces:

- the HTML carries the exact canonical Course-Fingerprint;
- all eight modules render in HTML;
- wide and 390 px narrow browser renders are generated;
- narrow HTML has no horizontal overflow;
- the instructor deck renders to at least 10 PDF pages;
- every presentation PDF page contains meaningful extracted text and is rasterized to PNG;
- the study guide renders to at least 9 PDF pages;
- every study-guide PDF page contains meaningful extracted text and is rasterized to PNG;
- the visible short Course-Fingerprint survives both office-rendering paths;
- `render-qa.json` reports `PASS` only after all checks complete.

All rendered pages are included in the CI artifact `youtube-course-large-golden` for manual visual inspection.

## Source/evidence boundary

This golden reference tests architecture, course planning and rendering against real source identities. It does not claim that CI has re-ingested every transcript on every run. Detailed scientific claims remain governed by the existing evidence-bound single- and multi-video workflows.

Generated diagrams and course visuals are illustrative learning artifacts, not experimental evidence.

## Acceptance

PASS requires:

1. 12 unique real YouTube source IDs from at least four source organizations/teaching contexts;
2. eight competency-based modules with valid prerequisite DAG;
3. every module has objectives, exit criteria, source scope and formative checkpoint;
4. identical Course-Fingerprint across JSON, HTML, PPTX/PDF and DOCX/PDF;
5. HTML wide + narrow browser rendering PASS;
6. every PPTX slide rendered and inspected through PDF/PNG;
7. every DOCX page rendered and inspected through PDF/PNG;
8. generated package uploaded as a CI artifact;
9. unresolved Critical/Major findings = 0.

A semantic-only unit test is insufficient for this reference: the render step is mandatory.
