# EUROIMMUN Corporate Icon System

Status: **normative runtime asset contract** for Skillz-generated EUROIMMUN presentations, DOCX reports and PDF derivatives when the approved icon bundle is available in the task context.

## 1. Provenance and identity

Approved runtime source analyzed on 2026-08-28:

- runtime/source name: `Icons.zip`
- SHA-256: `533f9adda32bb5746ab061a95b8e392be7511071a18d23e2c56e819b89ae8fde`
- archive files: 1,019 SVG assets plus directory entries
- RGB asset families only in the supplied archive
- the binary/icon files are proprietary runtime assets and MUST NOT be committed to the public Skillz repository

A future bundle with a different SHA-256 is a new asset revision and must be re-profiled before it inherits this contract.

### Catalog companions

When semantic icon selection is required, this contract MUST be used together with:

- `ICON_CATALOG.md` — human-readable complete semantic catalog, ambiguity rules, aliases and selection guidance;
- `icon-semantic-catalog.json` — machine-readable Skillz routing taxonomy;
- `icon-capability-index.json` — canonical inventory of named stems exposed by the approved bundle.

The machine index currently enumerates 176 Essential names, while the original profile below estimated approximately 177 Essential semantic motifs. Preserve the machine index as the canonical named inventory until the proprietary source bundle is re-profiled; do not silently invent or rename a missing motif.

### Skillz selector integration

Whenever a Skillz presentation, DOCX/report, web/design or other artifact workflow decides to use an icon from this Corporate library, semantic selection and supplied-variant routing MUST be delegated to the internal `icon-selector` skill with provider `euroimmun-corporate` before the asset is placed.

The selector receives at least the intended meaning and provider; where relevant also pass message context, domain, medium, background and whether the meaning is critical. Its `icon-selection.json` is the selection decision record for that icon use.

This is an **on-demand soft dependency**, not a mandatory hard `requires` edge for every EUROIMMUN renderer: workflows that do not use icons do not invoke the selector. PDF derivatives inherit icon selection from the canonical PPTX/DOCX and MUST NOT independently re-select or restyle icons during PDF post-processing.

If `icon-selector` returns `ambiguous`, `unresolved-provider` or `no-approved-match`, the calling workflow MUST NOT silently choose a different icon. Resolve the missing context, omit the icon, or document a justified non-icon alternative. The runtime asset is still resolved only from the authorized proprietary bundle; `icon-selection.json` does not authorize copying the binary into Skillz.

## 2. Inventory

The supplied bundle contains four functional families:

| Family | SVG files | Approx. semantic motifs | Primary use |
|---|---:|---:|---|
| Essential icons | 875 | 177 | generic business, process, people, IT, lab, risk, finance and navigation concepts |
| Portfolio & Indication icons | 70 | 14 | clinical/diagnostic portfolio and indication framing |
| Technique Icons | 35 | 9 | assay/platform technologies such as ELISA, ChLIA, IFA, Immunoblot, Microarray, PCR |
| Project icons | 39 | 13 | named EUROIMMUN projects/academy/campus activities; not generic symbols |

The dominant icon geometry is a square `viewBox="0 0 256 256"` (980 SVGs). Project/wordmark-like assets use wider viewBoxes and MUST NOT be treated as interchangeable square icons.

## 3. Supplied color variants

For most square icons, five supplied RGB variants exist:

- `_black` — black/dark icon on transparent background
- `_clover` — clover icon on transparent background
- `_white` — white icon on transparent background
- `_white-black` — white glyph on black circular field
- `_white-clover` — white glyph on clover circular field

Observed clover token: `#73C054`, consistent with the authoritative EUROIMMUN corporate palette. Black artwork may use artwork-specific near-black values such as `#1D1D1B`; do not normalize these by eye.

Rule: **use a supplied variant instead of recoloring an SVG whenever a suitable variant exists.** Do not recolor proprietary icons to arbitrary accent colors.

## 4. Document-safe variant selection

### White/light background

Prefer in order:

1. `_clover` for positive, navigational, process or branded semantic emphasis.
2. `_black` for neutral, technical, legal, dense or evidence-heavy contexts.
3. `_white-clover` only when a circular badge is intentionally part of the composition.

Never place `_white` directly on a white/light background.

### Dark/green/photo background

Prefer:

1. `_white` when the background itself provides sufficient contrast.
2. `_white-clover` or `_white-black` when the icon needs a self-contained badge or the photo/background is visually busy.

Do not add ad-hoc colored circles behind transparent icons when a supplied circular variant already exists.

## 5. Semantic routing

Choose the most specific available icon. For complete selection and query normalization, use `ICON_CATALOG.md` and `icon-semantic-catalog.json`. Recommended routing examples:

### Executive / business / governance

- strategy/target: `hit the bullseye`, `direction signal arrow`, `light bulb`
- decision/approval: `check mark`, `tick`, `Thumbs up`, `traffic light`
- leadership: `CEO`, `Employees`, `public speaker`
- collaboration/partnering: `handshake`, `puzzle`
- company/organization: `Company`, `large company`
- finance/business case: `euro`, `Dollar`, `Money bag`, `chart increased`, `double line chart`
- risk/security: `shield`, `risk protection`, `security`, `lock`, `guard`
- time/roadmap: `calender`, `stopwatch`, `appointment`
- process: `process`, `Gear`, `four Arrows`, `three way arrows`

### Digital / automation / data

- AI: `AI-Enhanced`
- automation: `automatic lab`, Portfolio icon `Automation`
- software/data: `Desktop`, `Desktop with Content`, `Desktop with Excel table`, `Web browser`, `Website content`
- LIS: specific `laboratory information system (LIS)` variants
- cyber/security: `cyber security`, `malware protection`, `network protection`, `password`, `shield lock`

### Scientific / laboratory / IVD

- lab/science: `microscope`, `Tube`, `Tubes-2X`, `Tubes-3X`, `Doctor`, `Patient`
- neurology/NDD: Portfolio icon `Neurology`
- assay technology: Technique icons `Techniques_ELISA`, `Techniques_ChLIA`, `Techniques_IFA`, `Techniques_Immunblot`, `Techniques_Microarray`, `Techniques_Real-Time PCR`
- diagnostic portfolios: use the corresponding Portfolio & Indication icon rather than a generic medical symbol when available

### Communication / learning / documentation

- document: `Document`, `Paper`, `PDF`
- search/research: `magnifying glass`
- training: `Graduation hat`, `online training`, `webinar`, project icons only when the named branded activity is actually intended
- external link/download: `External Link`, `download`, `Link`

## 6. Use in presentations

- Icons are information architecture, not decoration.
- Use at most one icon per message block/card unless the slide is explicitly an icon taxonomy.
- Prefer 3–5 repeated icons in parallel structures; do not mix multiple visual icon families within one structure.
- Keep icon optical sizes consistent across peers even when path extents differ.
- Preferred icon size for standard 16:9 content slides: roughly 0.25–0.55 in for inline/label use and 0.55–0.9 in for a primary card/process anchor; larger use requires a deliberate hero treatment.
- Section dividers usually rely on photography/large imagery rather than icon grids.
- Technique and indication icons are especially suitable for portfolio maps, assay workflows and strategy matrices.
- Preserve editability where the presentation toolchain supports native SVG; otherwise use a high-quality transparent raster derivative while retaining the SVG as source provenance.

## 7. Use in DOCX/PDF reports

- Default to restrained icon use; reports remain text/evidence led.
- Suitable placements: executive-summary pillars, section openers, compact process steps, risk/decision/info callouts and small portfolio/technology legends.
- Do not use icons as bullet replacements throughout body prose.
- Typical printed size: about 5–9 mm for inline markers and 9–15 mm for section/process anchors, subject to actual rendering and readability.
- Keep icons out of running headers/footers unless the controlled template already defines them there.
- Add alt text when supported and when the icon carries meaning not already stated in adjacent text.
- PDF inherits icon placement from the canonical PPTX/DOCX; do not restyle icons in PDF post-processing.

## 8. Accessibility and meaning

- Critical meaning MUST NOT be encoded by icon alone. Pair with a label, number, title or status text.
- Critical status distinctions should also use text or shape, not only color.
- Decorative icons may be marked decorative/empty-alt when the output format supports it.
- Do not use disease/indication icons to imply a clinical claim not supported by the content.

## 9. Asset integrity

MUST NOT:

- redraw or trace supplied icons;
- change aspect ratio;
- apply arbitrary rotations, skew, bevel, 3D effects, glow or heavy drop shadows;
- mix these icons with unrelated third-party icon styles in the same visual system without an explicit reason;
- commit the proprietary icon bundle into the public Skillz repository;
- convert a named Project icon into a generic icon for another purpose;
- infer regulatory status, intended use or scientific evidence from the presence of an icon.

MAY:

- crop only transparent whitespace if required by a renderer and if the visible geometry is unchanged;
- rasterize for compatibility at sufficient resolution;
- use supplied black/clover/white/circular variants according to the background rules above.

## 10. QA gate

For any artifact using the corporate icon system, QA must verify:

- asset provenance/source bundle recorded;
- correct semantic icon selected, using the catalog/semantic routing when selection is non-trivial;
- when Skillz performs the selection, a successful `icon-selector` decision exists for provider `euroimmun-corporate`;
- supplied color variant used where available;
- no distortion or clipping;
- optical peer sizing is consistent;
- icon contrast is adequate in final render;
- critical meaning is also expressed in text;
- no mixed/unapproved icon style is introduced without rationale;
- SVG/raster fallback does not visibly degrade in PPTX, DOCX or PDF render.

A wrong or misleading icon is a **Major** content/design finding when it changes interpretation; a merely inconsistent icon treatment is at least a **Warning** and becomes **Major** when it harms comprehension.

## 11. Completion rule

The icon system is correctly applied only when the selected asset is semantically appropriate, visually consistent with the active EUROIMMUN template, uses an approved supplied variant, remains legible in the final rendered medium and does not imply unsupported claims.
