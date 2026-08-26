# Sport Performance App Templates — binding reference

## Status

This document is the canonical layout/template contract for Sport applications using the Skillz `sport-performance` profile.

The confirmed reference state is the existing Impeccable UI of the two Sport applications:

1. **Sport Athlete Management** — athlete/training/adaptation application template.
2. **Masters Diagnostics** — diagnostics/data/analysis application template.

The reference screenshots/design proposal confirmed on 2026-08-26 define the intended family resemblance: related product chrome and UI grammar, product-specific marks, one shared Sport Performance color system.

## Layer ownership — binding

The design stack has two independent layers and they MUST NOT be conflated:

### Layer A — Impeccable UI template (layout and component grammar)

Impeccable owns and preserves:

- application shell and header/navigation structure;
- content width and responsive breakpoints;
- grid and card layout;
- typography scale, weights and hierarchy;
- spacing and vertical rhythm;
- card/control radii and border treatment;
- KPI card structure;
- chart/list/table module structure;
- form layout and control sizing;
- information hierarchy and density;
- responsive/mobile behavior;
- focus, hover, loading, empty and error interaction patterns;
- motion rules.

For an existing Sport application whose Impeccable UI has been accepted, this layer is **frozen by default**. A branding, logo, favicon, app-icon or palette task MUST produce no intentional layout/CSS-structure change in this layer.

### Layer B — Sport Performance branding overlay

`sport-performance` owns only:

- canonical color tokens and their semantic roles;
- product-specific logo mark;
- wordmark/lockup;
- favicon;
- app/PWA icon;
- chart/status colors where the existing component supports semantic color;
- theme metadata such as PWA `theme_color`.

Branding work may map existing CSS variables to canonical Sport Performance tokens. It MUST NOT redesign the component system or replace accepted Impeccable CSS/layout merely to apply the brand.

## Canonical colors

The palette remains defined by `../brand-profiles/sport-performance.json`. No local replacement palette is allowed unless a higher-priority corporate profile applies.

## Template 1 — Sport Athlete Management

Use this template for athlete management, training planning, adaptation, readiness, coaching and related operational Sport applications.

### Required design grammar

- dark technical application chrome with Navy hierarchy;
- compact navigation and high information density;
- calm White/Surface work area;
- dashboard/content sections built from purposeful cards, lists and strips rather than decorative card walls;
- athlete/training actions remain the strongest content hierarchy;
- responsive single-column fallback for narrow screens;
- status always combines text/symbol/marker with color;
- existing accepted spacing, typography, radii and component proportions are preserved.

### Branding mark

Use the product-specific athlete/development/adaptation mark. It must remain visually related to Masters Diagnostics through geometry, stroke character and palette, but clearly distinguishable at favicon size.

## Template 2 — Masters Diagnostics

Use this template for performance diagnostics, test review, measurement interpretation, longitudinal analysis and related diagnostic Sport applications.

### Required design grammar

- dark technical application chrome with Navy hierarchy;
- calm light analytical workspace;
- compact KPI/test summaries;
- charts, trend panels, alerts and diagnostic lists as purposeful analytical modules;
- clinical/technical clarity without turning the application into a generic hospital UI;
- responsive behavior and information density follow the accepted Impeccable implementation;
- existing accepted spacing, typography, radii and component proportions are preserved.

### Branding mark

Use the product-specific diagnostics/data/performance-curve mark. It must remain visually related to Sport Athlete Management through geometry, stroke character and palette, but clearly distinguishable at favicon size.

## New Sport applications

For a new Sport application without an accepted UI:

1. Choose the nearest template by product job-to-be-done.
2. Start from the same design grammar rather than inventing a new dashboard style.
3. Adapt information architecture to the actual product domain.
4. Preserve the family characteristics: technical dark chrome, calm light workspace, compact hierarchy, purposeful cards/lists, system-first typography, restrained motion, canonical Sport Performance colors.
5. Create a product-specific mark; do not copy either existing product mark.

The templates are starting structures, not permission to copy domain-specific labels or modules that do not belong to the new product.

## Change policy

### Branding-only change

A task whose scope is palette, logo, favicon, app icon or brand integration MUST NOT alter:

- layout structure;
- spacing scale;
- typography scale;
- component geometry;
- card/grid structure;
- navigation architecture;
- breakpoints;
- information hierarchy.

If such changes appear in the diff, treat them as a regression and revert them unless the user explicitly requested a UI redesign.

### Explicit UI redesign

A redesign of Layer A requires explicit scope such as `redesign`, `layout change`, `component redesign`, or a confirmed DESIGN grilling decision. Branding work alone is insufficient authorization.

## Acceptance gate

A Sport branding/template change is accepted only if all are true:

- canonical `sport-performance` token values remain intact;
- logo/favicon/app-icon are product-specific but family-related;
- accepted Impeccable CSS/layout is preserved for existing products;
- branding-only diffs contain no unintended layout/component restructuring;
- WCAG AA and no-color-only semantics remain satisfied;
- visual regression/spot-check confirms header proportions, cards, grids, typography and responsive behavior remain unchanged except for approved color/brand assets.

If the task says **"only logos and colors"**, this contract is literal: all non-color CSS/layout and UI structure must remain byte-for-byte or behaviorally equivalent unless a minimal technical integration change is unavoidable and explicitly documented.
