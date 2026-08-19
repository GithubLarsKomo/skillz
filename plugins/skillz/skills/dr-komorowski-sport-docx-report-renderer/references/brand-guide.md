# Dr. Komorowski Sport Report Brand Guide

## Canonical source

For new reports the DOCX template in `dr-komorowski-sport-docx-report-renderer` is the canonical layout source. The legacy ReportLab renderer is retained only for reproducibility of older direct-PDF reports.

## Brand

- Name: **Dr. Komorowski Sportdiagnose und Trainingszentrum**
- Primary navy: `#173652`
- Dark text: `#1C2B3A` / `#24313E`
- Teal accent: `#2B8884`
- Teal text: `#246F6C`
- Border: `#D6E0E6`
- Table fill: `#EDF3F6`
- Warning fill/border: `#FFF4D6` / `#9A6500`

## Layout

A4, 18 mm side margins, restrained header/footer, generous white space and a clear hierarchy. Long tables must remain readable without shrinking body text below a normal report size. Repeat table headers across pages and keep individual data rows together.

## Typography

Use system fonts only. Preferred family is Arial with Aptos and Liberation Sans fallbacks. Do not bundle or distribute font files.

## Charts

Lactate/heart-rate charts are representations of already interpreted data. Navy denotes lactate, teal heart rate, and threshold bands use restrained teal/warning tints. The renderer does not infer thresholds.

## QA

Every DOCX page must be rendered and visually inspected. The final PDF must be derived from that DOCX and compared page-by-page for clipping, reflow, missing glyphs, header/footer drift and table pagination.
