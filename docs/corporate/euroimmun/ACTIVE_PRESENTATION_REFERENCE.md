# EUROIMMUN Active Presentation Reference

Status: **normative pointer** for the currently preferred confirmed EUROIMMUN PowerPoint reference used by `euroimmun-presentation-workflow`.

## Preferred current reference

- Runtime/source name: `260828 NDD Review.pptx`
- Status: `confirmed-reference-binary`
- SHA-256: `349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e`
- Certified Golden Reference level: `LEVEL_2_PASS`
- Certification date: 2026-08-28
- Slide size: 16:9, 13.333 × 7.5 in
- Source slides: 12
- Slide masters: 3
- Visible PowerPoint layouts: 51
- Themes: 4
- Primary theme fonts: `Hanken Grotesk Light` / `Hanken Grotesk`
- Primary active green theme accent: `#208528`

The binary file itself is proprietary and MUST NOT be committed to Skillz. At runtime, a supplied file with this identity may be verified against the SHA-256 above and used as the preferred confirmed reference. If a newer approved or confirmed reference is supplied, its runtime identity and provenance must be evaluated before this pointer is changed.

## Secondary corporate-storytelling reference

For internal corporate storytelling, Town Hall, Leadership Briefing, Change/Transformation, People/Organization and Alignment decks, the following binary is confirmed as a **secondary style reference**:

- Runtime/source name: `Town Hall_BL Meeting_180826.pptx`
- SHA-256: `72a082c769abe5f18f53079ccfa7c59dc73ed53e285e4107f096ff587043bfb9`
- Source slides: 57
- Slide masters: 1
- Visible layouts: 44
- Themes: 3
- Primary binary theme font: Arial
- Revvity theme clover: `#73C054`
- Revvity theme forest: `#218529`

This binary **does not replace the preferred active template source**. It contributes visual storytelling grammar such as generous white space, large statement-led hierarchy, strong photo anchors, curved image masks, section dividers, process cards, directional flows and leadership-oriented summary structures. The derived normative rules are stored in `docs/corporate/euroimmun/PRESENTATION_STORYTELLING_REFERENCE.md`.

## Corporate icon reference

When the approved runtime icon archive is available, use `docs/corporate/euroimmun/ICON_SYSTEM.md`. The analyzed 2026-08-28 source `Icons.zip` has SHA-256 `533f9adda32bb5746ab061a95b8e392be7511071a18d23e2c56e819b89ae8fde`. The proprietary binary assets are runtime-only and must not be committed to Skillz.

## Historical reference

`260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`, remains a historical confirmed reference. Its derived layout observations remain useful where compatible, but it is no longer the preferred current PowerPoint reference.

## Precedence

For a presentation task:

1. A user-supplied approved controlled template for the specific artifact has highest precedence.
2. Otherwise, if the preferred current confirmed binary `260828 NDD Review.pptx` is available and its identity is verified, use it as the template source of truth.
3. Otherwise, use `references/euroimmun-template-spec.md` as a `template-compatible` fallback and disclose that no binary-master parity was verified.
4. The historical `260610 Innovation Topics.pptx` may be used only when explicitly supplied or required for compatibility/history; it MUST NOT silently displace the preferred current reference.

The secondary storytelling reference and icon system are orthogonal overlays: they may guide archetypes, imagery and semantic assets where compatible, but they do not override the active master/template source.

The shared `docs/corporate/euroimmun/DESIGN.md` and Golden Reference policy remain mandatory in every case.
