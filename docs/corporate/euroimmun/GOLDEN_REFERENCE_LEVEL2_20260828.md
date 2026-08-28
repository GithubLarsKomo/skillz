# EUROIMMUN Level 2 Controlled-Master Golden Reference — 2026-08-28

Status: **LEVEL_2_PASS**

This record certifies the first Level 2 run defined by `docs/corporate/euroimmun/GOLDEN_REFERENCE.md`. The proprietary PowerPoint source and generated business binaries are intentionally not stored in the Skillz repository. Their SHA-256 identities and QA evidence are recorded instead.

## Binary source

- Runtime source: `260828 NDD Review.pptx`
- SHA-256: `349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e`
- Template status: `confirmed-reference-binary`
- Source slides: `12`
- Slide size: `13.333 x 7.5 in` (16:9)
- Slide masters: `3`
- PowerPoint-visible layouts: `51`
- Theme parts: `4`
- Primary theme font: `Hanken Grotesk Light` / `Hanken Grotesk`

The source is deliberately not promoted to `approved-controlled`: no independent approval metadata accompanied the runtime file. `confirmed-reference-binary` is sufficient for a Level 2 template-derived certification under the Golden Reference policy.

## Primary template theme evidence

The primary theme contains:

- `dk1 #000000`
- `lt1 #FFFFFF`
- `dk2 #7F7F7F`
- `lt2 #FFEB0F`
- `accent1 #208528`
- `accent2 #7F03B0`
- `accent3 #148087`
- `accent4 #C94D00`
- `accent5 #9E306E`
- `accent6 #000000`

The active template green (`#208528`) differs slightly from the cross-format `euroimmun-corporate` forest token (`#218529`). For this template-derived run, the source-of-truth precedence in `DESIGN.md` applies: newly authored green elements use the active PowerPoint theme value and the discrepancy is recorded rather than normalized by eye.

## Derived Golden Reference

- Generated artifact: `euroimmun_neuro_24h_level2_template_derived.pptx`
- SHA-256: `5308f30c30f99288f6e192a9e49dd13125d6780649cfd6307a8ef43041d1fa7d`
- Derivation: `template-derived`
- Slides: `7`
- Repository storage: `false`

The content is the existing 27–28 Aug 2026 neurodegeneration Golden-Reference stress set; the proprietary scientific/business contents of the runtime source presentation were not reused as Golden-Reference facts merely because the file supplied the design master.

Layouts exercised:

1. `Title Slide 05`
2. `Section Header 03`
3. `Title + 2 Column Content`
4. `Titel und Inhalt`
5. `Charts: Title and Content 02`
6. `Content 02 Euroimmun`
7. `Title Only`

This covers corporate cover, section header, analytical content, two-column comparison, structured portfolio/table-like content, management plan and decision slide behavior. The supplied runtime layout set did not expose a dedicated `figure + bullets + conclusion` layout under that name; the run records the available grammar rather than inventing a missing layout.

## Structural and render evidence

- slide-size parity: `PASS`
- master/layout inheritance: `PASS`
- theme behavior: `PASS`
- logo geometry/aspect ratio: `PASS`
- footer/proprietary line geometry: `PASS`
- slide-number behavior: `PASS`
- safe-area/out-of-bounds objects: `0`
- generated slides rendered and inspected: `7/7`
- presentation PDF pages rendered and inspected: `7/7`
- source/PDF visible-layout parity: `PASS`

## Master-owned pixel parity

The runtime source and derived Golden Reference were rendered through the same LibreOffice stack at the same resolution. Master-owned regions were compared directly rather than recreated from coordinates.

The following comparison regions were **100% pixel-identical**:

- cover EUROIMMUN branding at top left;
- cover Revvity branding at lower left;
- cover right-side corporate artwork;
- standard content footer left region;
- standard content footer center region;
- standard content footer rule.

This is direct evidence that these master-owned elements were inherited from the supplied binary source rather than reconstructed.

## Findings

Unresolved Critical findings: `0`.

Unresolved Major findings: `0`.

Warnings:

- `FONT-RUNTIME-001`: the PowerPoint theme encodes Hanken Grotesk, but that font is not installed in the Linux/LibreOffice render runtime. A runtime substitution occurred; the complete artifact was rendered and master-owned comparison regions remained pixel-identical.
- `TEMPLATE-STATUS-001`: certification is `confirmed-reference-binary`, not `approved-controlled`, because separate approval metadata was not supplied.
- `THEME-PALETTE-001`: template `accent1 #208528` differs from cross-format corporate `forest #218529`; template precedence applies within this artifact.

## Acceptance

- derivation: `template-derived`
- runtime binary SHA-256 recorded: yes
- required master-owned elements inherited: yes
- Critical: `0`
- Major: `0`
- slide render coverage: `7/7`
- PDF render coverage: `7/7`
- PDF parity: `PASS`
- Corporate Design Gate: `PASS`

**Golden Reference: LEVEL_2_PASS**

This Level 2 run supersedes Level 1 for controlled-presentation fidelity claims for this binary source identity. Level 1 remains the permanent fallback regression. A materially different future PowerPoint source SHA-256, master/layout/theme/logo/footer change, material design-contract change or render-stack change requires a new Level 2 run.
