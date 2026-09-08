---
name: presentation-review
description: Prüft einen Vortrag vor dem PPT-Handoff auf Storyline, Kernaussagen, Slide Density, Visual Storytelling, Daten-/Chart-Tauglichkeit, Speaker/Slide-Balance, Template-Konsistenz, Accessibility, Timing sowie sprachliche und sachliche Fidelity.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - slide-architect
  - presentation-template
  - precision-writing-revision
outputs:
  - presentation-review.json
  - presentation-handoff.json
lastEvaluated: 2026-08-23
---

# Presentation Review

## Review-Dimensionen

- Audience Fit und Zielerreichung
- Core Message / Storyline
- Message-per-Slide
- Slide Density und Scanbarkeit
- Visual Storytelling
- Daten-/Chart-Eignung
- Evidence/Fidelity
- Qualität der Speaker Notes
- Speaker/Slide-Balance
- Sprachqualität DE/EN
- Template-/Design-Konsistenz
- Accessibility
- Timing
- Closing / Call-to-Action

## Voraussetzungen

- On-Slide Copy hat `precision-writing-revision(genre=slide-copy)` durchlaufen.
- Speaker Notes haben `precision-writing-revision(genre=speaker-notes)` durchlaufen.
- Fidelity Hard Fails sind geschlossen oder explizit als nicht freigegeben markiert.

## Ablauf

1. `speaking-concept`, Narrative, Slide Plan und Designprofil gegeneinander prüfen.
2. Folien ohne klare Funktion, doppelte Botschaften und unnötige Textlast identifizieren.
3. Visualtypen gegen Inhalt prüfen; ungeeignete Charts/Tabellen markieren.
4. Timing summieren und realistische Übergänge berücksichtigen.
5. Accessibility und Quellenlesbarkeit prüfen.
6. Nur konkrete Schwachstellen zurück an die zuständigen Skills routen.

## Abschluss

Output ist ein freigabefähiger `presentation-handoff.json` für PPT-/Slides-Erzeugung oder eine klar priorisierte Liste noch offener Hard Fails.
