# Sport Performance App Templates — binding reference

## Status

This document is the canonical template contract for Sport applications using the Skillz `sport-performance` profile.

The confirmed reference state is the **accepted Impeccable UI/CSS** of the two Sport applications with the **2026-08-26 Sport Performance logos and color spectrum applied as an overlay**:

1. **Sport Athlete Management** — athlete/training/adaptation application template.
2. **Masters Diagnostics** — diagnostics/data/analysis application template.

The visual proposal confirmed on 2026-08-26 does **not** replace the previously accepted CSS. It confirms the product-specific logos, shared color spectrum and family relationship. Existing non-color CSS remains authoritative.

## Layer ownership — binding

The design stack has two independent layers and they MUST NOT be conflated.

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

For an existing Sport application whose Impeccable UI has been accepted, this layer is **frozen by default**. A branding, logo, favicon, app-icon or palette task MUST produce no intentional non-color layout/CSS-structure change in this layer.

### Layer B — Sport Performance branding overlay

`sport-performance` owns only:

- the confirmed canonical color tokens and semantic mappings;
- product-specific logo mark;
- wordmark/lockup;
- favicon;
- app/PWA icon;
- chart/status colors where the existing component supports semantic color;
- theme metadata such as PWA `theme_color`.

Branding work may map existing CSS variables to canonical Sport Performance tokens. It MUST NOT redesign the component system or replace accepted Impeccable CSS/layout merely to apply the brand.

## Canonical confirmed color spectrum

These are the binding colors shown in the confirmed 2026-08-26 proposal:

| Role | HEX |
| --- | --- |
| Navy | `#173652` |
| Teal | `#246F6C` |
| Bright Teal | `#2B8884` |
| Energy | `#B54708` |
| Critical | `#B42318` |
| Recovery | `#6D5BD0` |
| Success | `#2E7D32` |
| Surface 0 | `#FFFFFF` |
| Surface 1 | `#F5F7FA` |
| Surface 2 | `#EEF2F7` |
| Text Primary | `#0F172A` |
| Text Secondary | `#475569` |
| Border | `#E2E8F0` |

The machine-readable source of truth remains `../brand-profiles/sport-performance.json`. Compatibility aliases such as `dark`, `body`, `muted`, `warning`, `surface`, and `surface_subtle` MUST resolve to this confirmed spectrum rather than introduce additional brand colors.

No local replacement palette is allowed unless a higher-priority corporate profile applies.

## Template 1 — Sport Athlete Management

Use this template for athlete management, training planning, adaptation, readiness, coaching and related operational Sport applications.

The **existing accepted Sport Athlete Management CSS/layout is the reference implementation**. Preserve its current application shell, content hierarchy, cards/lists, typography, spacing, control geometry and responsive behavior. Apply the confirmed Sport Performance spectrum and the product-specific athlete/development/adaptation mark without redesigning that structure.

The mark must remain visually related to Masters Diagnostics through geometry, stroke character and palette, but clearly distinguishable at favicon size.

## Template 2 — Masters Diagnostics

Use this template for performance diagnostics, test review, measurement interpretation, longitudinal analysis and related diagnostic Sport applications.

The **existing accepted Masters Diagnostics Impeccable CSS/layout is the reference implementation**. Preserve its current application shell, data views, typography, spacing, controls, cards/tables/charts and responsive behavior. Apply the confirmed Sport Performance spectrum and diagnostics/data/performance-curve mark without redesigning that structure.

The mark must remain visually related to Sport Athlete Management through geometry, stroke character and palette, but clearly distinguishable at favicon size.

## New Sport applications

For a new Sport application without an accepted UI:

1. Choose the nearest template by product job-to-be-done.
2. Start from the same Impeccable design grammar rather than inventing an unrelated dashboard style.
3. Adapt information architecture to the actual product domain.
4. Use the exact confirmed Sport Performance spectrum above.
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
- information hierarchy;
- other non-color CSS behavior.

If such changes appear in the diff, treat them as a regression and revert them unless the user explicitly requested a UI redesign.

### Explicit UI redesign

A redesign of Layer A requires explicit scope such as `redesign`, `layout change`, `component redesign`, or a confirmed DESIGN grilling decision. Branding work alone is insufficient authorization.

## Acceptance gate

A Sport branding/template change is accepted only if all are true:

- the exact confirmed `sport-performance` spectrum remains intact;
- logo/favicon/app-icon are product-specific but family-related;
- accepted Impeccable CSS/layout is preserved for existing products;
- branding-only diffs contain no unintended layout/component restructuring;
- WCAG AA and no-color-only semantics remain satisfied;
- visual regression/spot-check confirms layout, card/grid structure, typography, spacing and responsive behavior remain unchanged except for approved color/brand assets.

If the task says **"only logos and colors"**, this contract is literal: all non-color CSS/layout and UI structure must remain byte-for-byte or behaviorally equivalent unless a minimal technical integration change is unavoidable and explicitly documented.
