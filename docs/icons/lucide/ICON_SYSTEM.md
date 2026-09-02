# Lucide Generic Icon Provider

Status: **normative open-provider contract** for Skillz-generated unbranded or non-corporate artifacts that use Lucide icons.

## 1. Purpose and provider boundary

`lucide-generic` is the default open icon provider for Skillz when:

- no registered corporate/provider-specific icon library is required;
- the artifact is a Skillz web app, generic presentation/document, Sport/Travel/learning artifact, prototype or other neutral product surface;
- the active design system permits outline icons.

It MUST NOT silently replace a registered Corporate provider. If brand context resolves to `euroimmun-corporate` or another future brand provider, that provider has priority.

Lucide contains no brand logos by design. Brand marks, certification marks, regulatory symbols and named project logos are out of scope.

## 2. Upstream identity and license

Profiled upstream state:

- repository: `lucide-icons/lucide`
- profiled release: `1.27.0`
- profiled release commit: `4aec3f8`
- review date: `2026-09-02`
- license: ISC
- upstream icon inventory: canonical in the release's `icons/*.svg` and `icons/*.json` metadata
- upstream metadata schema: `icon.schema.json`
- upstream categories are the canonical category vocabulary for the profiled release.

Skillz does **not** vendor the full Lucide icon inventory. The local `icon-semantic-catalog.json` is a routing overlay, not a fork of upstream metadata.

When Lucide SVG/code is copied or distributed outside an installed package, preserve the applicable ISC copyright/permission notice. Do not strip notices from package distributions.

A newer upstream release is a new provider revision. Do not assume names, aliases or deprecations remain unchanged; re-profile before updating `profiledRelease`.

## 3. Canonical geometry and rendering

Default Lucide rendering contract:

- `viewBox="0 0 24 24"`
- `fill="none"`
- `stroke="currentColor"`
- `stroke-width="2"`
- `stroke-linecap="round"`
- `stroke-linejoin="round"`
- default logical size: 24 × 24.

Unlike the EUROIMMUN provider, Lucide intentionally supports color/stroke customization. For Skillz:

- inherit `currentColor` from the active design system;
- use existing foreground/accent/status tokens rather than introducing a new palette;
- default to stroke width 2;
- change stroke width only when the active design system defines a consistent Lucide treatment;
- never stretch the 24×24 aspect ratio;
- do not add arbitrary fills, gradients, 3D effects, bevels or mixed third-party strokes to mimic a different family.

## 4. Inventory model

The **complete inventory** remains upstream. Skillz resolves an icon name only when it exists in the pinned/profiled Lucide release or an explicitly accepted newer revision.

The semantic overlay contains:

- the complete upstream category vocabulary;
- bilingual DE/EN intent aliases for high-value Skillz concepts;
- preferred icon names for common product, analysis, sport, travel, science, learning and workflow intents;
- ambiguity rules;
- status/claim-safety rules;
- neutral fallbacks.

Do not invent a Lucide icon merely because its name sounds plausible. If a preferred mapping is absent in the resolved runtime release, use upstream aliases/metadata to find a valid replacement or emit `no-approved-match`.

## 5. Provider resolution

Use `lucide-generic` when the request is explicitly generic/unbranded or when all are true:

1. no registered brand alias/provider matches;
2. no user-supplied icon family is mandatory;
3. the artifact allows an open generic icon family;
4. icon semantics can be expressed without a brand/regulatory/project-specific symbol.

Provider priority:

1. explicit task-specific approved provider;
2. registered corporate/brand provider inferred from context;
3. explicit `lucide-generic`;
4. implicit `lucide-generic` only for clearly unbranded/general Skillz artifacts;
5. otherwise `unresolved-provider`.

## 6. Semantic routing

Read `icon-semantic-catalog.json` before selecting. Prefer `preferredRouting` for exact high-value concepts, then the narrowest matching `semanticDomains` group, then upstream metadata.

Representative disambiguations:

- **goal/objective** → `target`; measured performance/capacity → `gauge`;
- **find/research retrieval** → `search`; laboratory observation/science → `microscope`;
- **broad security** → `shield`; protected access → `lock`; identity/authentication → `fingerprint`;
- **travel/flight** → `plane`; itinerary/path → `route`; physical location → `map-pin`;
- **training/strength** → `dumbbell`; competition/winning → `trophy`; result/award → `medal`;
- **document/report** → `file-text`; learning/knowledge → `book-open`;
- **workflow/process** → `workflow`; multi-stop handoff/route → `waypoints`.

Meaning beats lexical similarity.

## 7. Status and claim safety

Lucide status symbols are visually strong and therefore require explicit semantics.

- `circle-check`, `badge-check`, `shield-check` or similar MUST NOT imply regulatory approval, certification, verification, clinical validation or quality release unless that status is explicitly established by the content.
- `triangle-alert` may signal a warning/risk but does not quantify severity.
- medical/science icons do not establish diagnosis, intended use, performance or evidence.
- `criticalMeaning=true` always requires an adjacent text label or status statement.
- status color alone is never sufficient for critical distinctions.

For regulated or safety-relevant artifacts, the icon is secondary communication, not evidence.

## 8. Accessibility

- meaningful icons need an accessible name or adjacent visible label unless the surrounding control already supplies one;
- purely decorative icons should be hidden from assistive technology where the target framework supports it;
- icon-only interactive controls require an accessible label and adequate hit target;
- do not encode state solely through color or a subtle icon-shape change;
- verify contrast after applying design-system colors.

## 9. Medium-specific use

### Web/UI

- prefer framework-native Lucide packages and tree-shaken imports;
- use one semantic icon per control/action;
- do not use decorative icons where text already communicates the same information unless visual scanning benefits;
- keep peer icons at consistent logical size/stroke.

### Presentations

- use Lucide for generic/unbranded decks only when no corporate library supersedes it;
- prefer 3–5 coherent icons in repeated structures;
- use the presentation's palette through `currentColor`;
- avoid tiny dense icon grids.

### DOCX/PDF

- use sparingly as orientation or callout anchors;
- rasterize only when the document toolchain cannot preserve SVG;
- retain sufficient print resolution;
- PDF inherits icon semantics/layout from the canonical source document rather than reselecting icons during PDF post-processing.

## 10. Brand and provider isolation

MUST NOT:

- mix `lucide-generic` into a branded icon system when the brand contract prohibits it;
- use Lucide as a fake company/product/project logo;
- replace a missing corporate icon with Lucide without documenting the provider change;
- style Lucide to imitate a proprietary icon library;
- infer brand endorsement from the use of a generic icon.

MAY:

- use Lucide in a branded artifact only when that artifact's explicit design contract authorizes Lucide as a secondary utility family and defines how it coexists with corporate icons.

## 11. Runtime resolution

Preferred runtime sources, in order:

1. the Lucide package already native to the target framework/project;
2. `@lucide/icons` data/builders where framework-neutral icon data is required;
3. official SVG from the pinned/profiled upstream release.

Record the actual runtime package/release when reproducibility matters.

Do not fetch `main` opportunistically during a deterministic artifact build. Prefer a locked dependency or pinned release.

## 12. QA gate

For every Skillz-selected Lucide icon verify:

- provider resolution is correct and no corporate provider should have won;
- canonical name exists in the runtime/pinned Lucide version;
- semantic choice is the narrowest justified mapping;
- design-system color and stroke treatment are consistent;
- no unsupported positive/regulatory/clinical status is implied;
- critical meaning also appears as text;
- accessibility requirements are met;
- license/source provenance is retained where distribution requires it.

A semantically misleading icon is a **Major** finding. A non-existent/deprecated runtime name is a **Major** implementation finding. Minor optical inconsistency is at least a **Warning**.

## 13. Maintenance

When updating the provider:

1. inspect the newest stable Lucide release and release notes;
2. verify ISC license status and upstream brand-logo policy;
3. diff mapped icon names against release metadata, including aliases/deprecations;
4. update `profiledRelease`, commit and review date;
5. adjust semantic mappings only where upstream changes require it;
6. run all `icon-selector` evaluations;
7. do not mass-copy upstream SVG/JSON files into Skillz.

## 14. Completion rule

`lucide-generic` is correctly applied when a valid Lucide icon from the profiled/runtime release is selected for the intended meaning, uses the active design system without geometric distortion, remains accessible, does not displace a higher-priority corporate provider and does not imply unsupported status or claims.
