# EUROIMMUN report brand reference

## Status

This skill ships a **public-reference** report template, not an internally controlled corporate stationery master.

As of 2026-08-19, Euroimmun publicly uses the visual identity introduced in July 2025: a modernized lowercase `euroimmun` wordmark, `From Revvity` endorsement and a green titerplane symbol. Euroimmun states that the new design creates visual alignment with Revvity and is being rolled out progressively.

Public logo asset identified on the current Euroimmun website:

`https://www.euroimmun.com/fileadmin/user_upload/Locations/Logos/EUROIMMUN_short_head_RGB.svg`

Public rebrand references:

- `https://www.euroimmunblog.com/euroimmun-rebranding/`
- `https://www.euroimmunblog.com/what-you-know-and-trust-soon-with-a-new-shine/`
- `https://www.euroimmun.com/contact/`

Current public legal/contact reference:

- EUROIMMUN Medizinische Labordiagnostika AG
- Seekamp 31
- 23560 Lübeck
- Tel. +49 451 2032-0
- Fax +49 451 2032-100

## Bundled working design

The bundled DOCX template snapshot (stored as `assets/euroimmun-report-template.docx.b64`) reproduces the public logo structure with an editable local reference asset and uses a working green for deterministic rendering. This green is **not represented as an internally controlled corporate Pantone/RGB specification**.

For formal, external or document-controlled use, supply the current approved internal DOCX template with the required placeholder contract. The approved template takes precedence over every bundled visual value.

## Corporate icon library

When the approved runtime EUROIMMUN icon bundle is supplied with the task, apply `docs/corporate/euroimmun/ICON_SYSTEM.md`.

Confirmed analyzed bundle as of 2026-08-28:

- source name: `Icons.zip`
- SHA-256: `533f9adda32bb5746ab061a95b8e392be7511071a18d23e2c56e819b89ae8fde`
- 1,019 SVG assets across Essential, Portfolio & Indication, Technique and Project families
- dominant square icon geometry: `viewBox 0 0 256 256`
- typical supplied variants: black, clover, white, white-black, white-clover

Report-specific use:

- Use icons **sparingly**; the report remains text-, evidence- and decision-led.
- Good placements are executive-summary pillars, section openers, compact process steps, decision/risk/info callouts and small portfolio/technology legends.
- Do not replace normal body bullets with an icon on every line.
- On white/light report pages prefer supplied `_clover` or `_black` variants.
- Use `_white` only on a sufficiently dark/green/image background; prefer supplied `_white-clover` or `_white-black` badge variants if the surrounding surface is visually busy.
- Never recolor proprietary SVGs to arbitrary colors when a supplied variant exists.
- Use Portfolio/Indication or Technique icons instead of generic symbols when the content specifically concerns a diagnostic field or assay technology.
- Project icons are reserved for the named branded project and must not be repurposed as generic document symbols.
- Typical printed size is about 5–9 mm for inline markers and 9–15 mm for section/process anchors, followed by full render inspection.
- If the renderer cannot preserve SVG reliably, use a high-quality transparent raster derivative while retaining SVG provenance; verify the DOCX and final PDF render.
- Icons never imply scientific evidence, regulatory status, intended use or a clinical claim. Pair material icons with visible text and alt text where supported.

The proprietary icon bundle MUST NOT be committed to the public Skillz repository.

## Header contract

The public-reference header uses:

- logo / wordmark at upper left,
- document type, document ID and date at upper right,
- a restrained green rule below the header,
- no legacy blue EUROIMMUN branding.

## Footer contract

The bundled template footer uses the current legal entity and Lübeck headquarters address plus the requested confidentiality classification. It deliberately avoids renderer-dependent page-number fields. An approved corporate template may provide its own page fields and footer structure.

## Fonts

No font files are bundled. The template uses common Office/system font families with normal fallback behavior. Do not copy fonts from a workstation into this skill.
