# Sport Performance App Templates — binding reference

## Status

This document is the canonical layout/template contract for Sport applications using the Skillz `sport-performance` profile.

The confirmed reference state is the existing Impeccable UI of the two Sport applications:

1. **Sport Athlete Management** — athlete/training/adaptation application template.
2. **Masters Diagnostics** — diagnostics/data/analysis application template.

## Layer ownership — binding

### Layer A — Impeccable UI template

Owns application shell, header/navigation, content width, breakpoints, grid/card layout, typography, spacing, radii, KPI/chart/list/form structures, information hierarchy, responsive behavior and interaction patterns.

For an existing Sport application whose Impeccable UI has been accepted, this layer is **frozen by default** during branding work.

### Layer B — Sport Performance branding overlay

Owns only canonical color tokens/semantic roles, product-specific logo/wordmark, favicon, app/PWA icons, supported chart/status colors and theme metadata.

Branding work MUST NOT redesign the accepted Impeccable component system or CSS/layout.

## Template 1 — Sport Athlete Management

Use for athlete management, training planning, adaptation, readiness and coaching. Preserve dark technical chrome, calm light work surfaces, compact hierarchy, purposeful cards/lists and responsive operational flows. Use the athlete/development/adaptation mark.

## Template 2 — Masters Diagnostics

Use for performance diagnostics, test review, measurement interpretation and longitudinal analysis. Preserve dark technical chrome, calm analytical workspace, compact KPI/test summaries, charts/trends/alerts and responsive diagnostic modules. Use the diagnostics/data/performance-curve mark.

## New Sport applications

Choose the nearest template by job-to-be-done and start from the same design grammar, adapting only domain-specific information architecture and modules. Create a product-specific mark rather than copying either existing mark.

## Change policy

A branding-only task MUST NOT alter layout structure, spacing scale, typography scale, component geometry, card/grid structure, navigation architecture, breakpoints or information hierarchy.

A redesign of Layer A requires explicit redesign scope or a confirmed DESIGN grilling decision.

## Acceptance gate

A Sport branding/template change is accepted only if canonical tokens remain intact, product marks are distinct but related, accepted Impeccable CSS/layout is preserved, WCAG/no-color-only rules remain satisfied, and a visual spot-check confirms unchanged header proportions, cards, grids, typography and responsive behavior except for approved colors/brand assets.

If the task says **"only logos and colors"**, all non-color CSS/layout and UI structure must remain unchanged or behaviorally equivalent unless a minimal technical integration change is unavoidable and documented.
