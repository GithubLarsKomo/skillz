# YouTube Learning Golden Reference

This document defines a reproducible **artifact-free Golden Reference** for the `youtube-learning-workflow` and `docs/learning-content/DESIGN.md`. It records the source, expected evidence state, render coverage and acceptance criteria of a real end-to-end learning run without committing generated binary deliverables to the repository.

## Reference run

- Date: 2026-08-28
- Source: `PCR explained | biology animation`
- Publisher: yourgenome / Wellcome Sanger Institute
- YouTube video ID: `Q2847XA-Rfk`
- Mode: `full`
- Language: German
- Audience: professional training
- Design authority: `docs/learning-content/DESIGN.md` plus project-local `DESIGN.md`
- Final status: `Learning Artifact QA: PASS`
- Unresolved Critical findings: `0`
- Unresolved Major findings: `0`
- Documented warnings: `3`

The generated test package contained:

- Landingpage-style HTML with wide, narrow and print rendering;
- a 9-slide learning presentation plus presentation-PDF render;
- a 4-page DOCX learning document;
- a 4-page PDF derivative;
- three original explanatory SVGs;
- `learning-content-model.json`, `youtube-learning-run.json` and a QA report.

Generated binary artifacts are deliberately not committed. The fixture captures the durable behavioral and QA expectations.

## Why this source is useful

The PCR video exercises the core YouTube Learner behaviors in a compact source:

- a clear multi-step process;
- spoken numerical anchors;
- a reaction-component model;
- a repeated thermal cycle;
- an idealized exponential-amplification explanation;
- a useful distinction between conceptual explanation and executable laboratory SOP.

It therefore tests transcript-grounded learning extraction, process reconstruction, evidence classification, visual planning, cross-format consistency and SOP boundaries without requiring source-frame reproduction.

## Canonical learning anchors

A conforming rerun must preserve these source-derived learning anchors while keeping their evidence status explicit:

- denaturation at approximately `95 °C`;
- annealing at approximately `50 °C` **as the simplified value used by the source, not a universal PCR default**;
- extension at approximately `72 °C`;
- `35` cycles in the source explanation;
- idealized amplification by repeated doubling, with `2^35 > 34 billion` copies from one starting molecule as the mathematical illustration;
- a thermostable DNA polymerase is required to survive repeated high-temperature denaturation and remain active for extension;
- primers delimit where synthesis begins;
- the source does not provide enough execution-critical detail for a lab-ready controlled SOP.

## Evidence-state rules

The run intentionally distinguishes:

- `observed`: directly supported by the accessible source transcript/metadata;
- `derived`: reconstructed from source evidence, such as conceptual process structure or approximate chapter windows;
- `recommended`: external educational clarification or best-practice context;
- `unknown/open`: information not supported by the source.

No frame-specific claim is allowed when direct frame-level inspection is unavailable. Generated diagrams are explanatory assets and must never be represented as source evidence.

## Derived instructional SOP boundary

The reference run produces a **derived instructional SOP** only.

It must remain visibly classified as:

- not approved;
- not lab-ready;
- unsuitable as a controlled procedure without expert/Quality verification.

Missing concentrations, volumes, reagent specifications, annealing-temperature optimization, exact dwell times, initial/final extension conditions and product-control steps must not be invented.

## Visual reference state

The run uses three newly generated explanatory SVGs:

1. PCR reaction mixture;
2. PCR thermal cycle;
3. idealized exponential amplification.

Expected properties:

- original explanatory construction rather than copied source frames;
- semantic fit to the canonical learning model;
- restrained instructional palette;
- SVG `<title>` and `<desc>` accessibility metadata;
- no new scientific claims introduced by the visual;
- source/generated provenance remains distinguishable.

## Render reference state

The accepted run achieved:

| Surface | Coverage | Expected result |
|---|---:|---|
| HTML Wide | 1/1 full-page | PASS |
| HTML Narrow | 1/1 full-page | PASS |
| HTML Print | 7/7 pages | PASS |
| PPTX | 9/9 slides + presentation PDF | PASS |
| DOCX | 4/4 pages | PASS |
| PDF | 4/4 pages | PASS |
| SVG | 3/3 assets | PASS |

The presentation required an intermediate correction for image clipping/text overflow and was then re-rendered. The final delivered revision is the revision that passed QA.

## Expected non-blocking warnings

A faithful rerun may retain these warnings when the same source-access conditions apply:

- `TS-001`: exact caption timestamps unavailable; chapter links use derived approximate windows;
- `VIS-001`: direct frame-level source inspection unavailable; therefore no source-frame-dependent claims or reused frames;
- `SOP-001`: procedure is a derived instructional SOP and not lab-ready.

Removing a warning without improving the underlying source/evidence state is suspicious.

## Cross-format acceptance checks

A conforming rerun must prove:

- one canonical `learning-content-model.json` revision is used for all requested formats;
- source identity is stable;
- key numbers and caveats agree across HTML, PPTX, DOCX and PDF;
- `observed`, `derived`, `recommended` and open/unknown distinctions are not silently collapsed;
- the derived SOP remains explicitly non-approved/non-lab-ready;
- generated SVGs are identified as explanatory, not source evidence;
- all requested surfaces are rendered and inspected;
- DOCX-to-PDF visible parity is checked;
- unresolved Critical findings = `0`;
- unresolved Major findings = `0`;
- final status is exactly `Learning Artifact QA: PASS`.

The regression test `tests/test_youtube_learning_golden_reference.py` validates these repository-level invariants against `tests/fixtures/youtube-learning/pcr-golden.json`.
