# EUROIMMUN NDD Icon Routing Reference

Status: **domain-specific visual routing reference** for EUROIMMUN/Revvity neurodegeneration (NDD) presentations and related corporate documents.

This file does not contain proprietary icon binaries. It maps NDD concepts to the approved runtime icon bundle described in `ICON_SYSTEM.md` and to the visual catalog generated from that bundle.

## Provenance

Approved icon bundle:

- runtime/source: `Icons.zip`
- SHA-256: `533f9adda32bb5746ab061a95b8e392be7511071a18d23e2c56e819b89ae8fde`
- 1,019 SVG assets

Corporate storytelling reference:

- `Town Hall_BL Meeting_180826.pptx`
- SHA-256: `72a082c769abe5f18f53079ccfa7c59dc73ed53e285e4107f096ff587043bfb9`

Runtime visual catalog generated from these sources:

- `EUROIMMUN_Corporate_Icon_Catalog_Reference_NDD.pptx`
- `EUROIMMUN_Corporate_Icon_Catalog_Reference_NDD.pdf`
- machine mapping: `EUROIMMUN_Corporate_Icon_Catalog_Mapping.json`

These binaries are runtime/user artifacts and are not committed to the public Skillz repository.

## NDD semantic routing

| NDD concept | Preferred corporate icon | Use |
|---|---|---|
| Neurodegeneration / disease area | `Neurology` | Portfolio context, section opener, NDD framing |
| Blood biomarker / plasma sample | `Tube` | Sample, analyte, blood-first pathway |
| Cohort / sample collection | `Tubes-2X`, `Tubes-3X` | Study cohorts, serial sampling, longitudinal evidence |
| Biomarker science / experimental evidence | `microscope` | Science, assay biology, validation work |
| Analytical performance / robustness | `Precision` | Precision, lot consistency, analytical validation |
| Research / evidence generation | `magnifying glass` | Research, literature, cohort characterization |
| Clinical pathway / treatment context | `Patient care` | Treatment readiness, patient workflow |
| Specialist / clinical stakeholder | `Doctor` | Memory clinic, neurology, physician workflow |
| pTau217 / biomarker trend / response | `chart increased` | Quantitative change, longitudinal response, market growth only when labeled accordingly |
| Development / evidence workflow | `process` | RUO-to-IVD, protocol, clinical evidence engine |
| Stage gate / go-hold-stop | `traffic light` | Development and capital decision gates |
| Risk / safety / clinical caution | `risk protection` | Clinical, regulatory or program risk; pair with explicit text |
| Strategy / target use case | `hit the bullseye` | Strategic objective, intended decision target |
| Business case / investment | `euro`, `Money bag` | Revenue, cost, funding, investment envelope |
| Partnership / external access | `handshake` | Pharma/CRO/KOL/licensing collaboration |
| Integrated portfolio | `puzzle` | Portfolio architecture, cross-Revvity integration |
| Roadmap / timeline | `calender`, `stopwatch` | Milestones, timing, urgency |
| AI / multi-marker model | `AI-Enhanced` | Algorithmic or multi-marker option only when actually in scope |
| Automation / scalable lab workflow | `automatic lab`, `Automation` | Automation and platform integration |
| ELISA technology | `Techniques_ELISA` | EUROIMMUN ELISA track; technology identity only |
| ChLIA technology | `Techniques_ChLIA` | EUROIMMUN ChLIA track; technology identity only |
| IFA / Immunoblot / Microarray / PCR | corresponding `Techniques_*` icon | Use only when that technique is materially part of the slide |
| Controlled evidence / dossier | `Document`, `Paper`, `PDF` | Evidence package, report, submission/dossier context |
| Compliance / governance | `shield`, `shield lock` | Governance, protected data, compliance context |

## Preferred NDD visual narrative

For the next revision of the Corporate NDD strategy deck, prefer the following visible sequence where it fits the actual content:

`Neurology -> Tube -> microscope -> Techniques_ELISA / Techniques_ChLIA -> Precision -> traffic light -> risk protection -> chart increased / euro`

Interpretation:

1. **Context** — NDD / neurodegeneration.
2. **Sample** — blood biomarker strategy.
3. **Science** — clinical and biomarker evidence.
4. **Platform** — actual EUROIMMUN assay track.
5. **Robustness** — analytical feasibility and validation.
6. **Gate** — development / capital decision.
7. **Risk** — regulatory, clinical, IP/FTO or commercial uncertainty.
8. **Value** — commercial pull, revenue, strategic option value.

Do not force every slide through this sequence. It is a deck-level visual grammar, not a mandatory per-slide template.

## NDD slide-type recommendations

### Executive summary

Use 3–4 icons maximum, typically:

- `Neurology` — category / portfolio;
- `Techniques_ELISA` or `Tube` — current asset / entry point;
- `traffic light` — gated investment logic;
- `chart increased` or `euro` — value pool / commercial evidence.

### Market / why now

Prefer:

- `chart increased` for category growth;
- `Patient care` or `Doctor` for workflow shift;
- `stopwatch` only when urgency/timing is explicitly discussed.

### Scientific evidence

Prefer:

- `microscope`;
- `Precision`;
- `Tube`;
- `magnifying glass`.

Icons must remain secondary to plots, cohorts, performance metrics and references.

### Reagent / assay platform slides

Prefer:

- `Techniques_ELISA`;
- `Techniques_ChLIA`;
- `automatic lab` / `Automation`;
- `Precision`.

Technique icons indicate format only. They MUST NOT imply CE-IVDR, FDA clearance, clinical matrix validation, intended use, measurement range or diagnostic performance.

### RUO vs IVD / transfer gate

Prefer a staged flow using:

- `microscope` / `magnifying glass` — research evidence;
- `Tube` — clinical matrix;
- `Precision` — analytical validation;
- `Document` — controlled evidence package;
- `traffic light` — regulatory/development gate.

The actual intended use, matrix, measuring range, validation and regulatory status must be written and sourced explicitly.

### Treatment response / longitudinal program

Prefer:

- `Patient care`;
- `Tubes-2X` / `Tubes-3X`;
- `chart increased`;
- `process`.

Ensure the chart icon does not imply a specific direction of biomarker response unless the data shown support it.

### Differential neurodegeneration

Use `Neurology` as the portfolio anchor and add separate text labels for AD, synucleinopathy, mixed pathology and neuronal injury. Do not invent disease-specific corporate icons that are not present in the approved bundle.

### Capital / decision slide

Prefer:

- `traffic light` — gate;
- `Money bag` / `euro` — investment;
- `risk protection` — downside / uncertainty;
- `hit the bullseye` — target use case.

The decision statement remains primary; icons are visual anchors only.

## Color and variant rules for NDD

- On standard white/light scientific slides: use `_clover` for navigational/portfolio/process meaning and `_black` for neutral technical/legal structures.
- On green section fields or dark/photo regions: use `_white` or the supplied circular white variants.
- Do not recolor NDD icons purple/orange merely to differentiate biomarkers. Use text labels, shapes, line styles or chart semantics instead.
- Do not use color alone for evidence maturity, risk or regulatory status.

## NDD-specific anti-patterns

Do not:

- use `Neurology` as proof that a product has a neurologic intended use;
- use technique icons as a proxy for regulatory status;
- create a unique icon for every biomarker when the corporate library does not provide one;
- decorate dense evidence slides with multiple icons that compete with data or sources;
- use `AI-Enhanced` unless an algorithmic/multi-marker/AI proposition is actually discussed;
- use a green positive icon to visually overstate an unresolved scientific, IP/FTO, regulatory or commercial question.

## QA for NDD decks

In addition to `ICON_SYSTEM.md` and presentation QA, verify:

- NDD icon routing matches the actual claim of the slide;
- `Neurology`, assay-technique and automation icons do not imply unsupported intended use or regulatory status;
- scientific evidence remains visually dominant on scientific slides;
- management gates are labeled in text, not encoded by icon/color alone;
- icon scale and clover/black variant use are consistent across the core deck;
- appendix deep dives may use denser technical iconography than the 20-minute executive core, but still require one clear visual hierarchy.

## Completion rule

The NDD icon routing is correctly applied when the Corporate NDD deck uses a small, repeatable visual vocabulary that improves orientation across context, science, platform, robustness, gates, risk and value without altering or overstating scientific, regulatory, IP or commercial claims.
