---
name: slide-architect
description: Übersetzt ein Speaking-Konzept und Presentation Narrative in einen strukturierten Slide-Plan. Definiert pro Folie Zweck, Kernaussage, Visualtyp, Evidenz, On-Slide-Text, Speaker Message, Übergang und Timing und verhindert unnötig textlastige Standardfolien.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - presentation-writer
outputs:
  - slide-plan.json
lastEvaluated: 2026-08-23
---

# Slide Architect

## Grundsatz

**Eine Folie ist keine Textseite.** Default ist eine Kernaussage pro Folie; Ausnahmen müssen durch Informationsstruktur oder Vergleichsbedarf begründet sein.

## Pro Folie

- `purpose`
- `keyMessage`
- `visualType`
- `evidence`
- `onSlideText.headline`
- `onSlideText.body`
- `speakerMessage`
- `transition`
- `timeSeconds`

## Visualtypen

`photo|diagram|process|timeline|chart|table|quote|minimal-text|comparison|architecture|other`

## Regeln

- Aussageorientierte Headlines bevorzugen, wenn Evidenz sie trägt.
- Keine automatische "Headline + 6 Bullets"-Struktur.
- Daten bevorzugt als passende Visualisierung statt als Textliste planen.
- Komplexe Erklärung in Speaker Notes auslagern, nicht durch aggressive Kürzung verfälschen.
- Quellen-/Footnote-Bedarf pro Folie markieren.
- Summe der Folienzeiten gegen das Timing-Budget prüfen.

## Handoff

On-Slide Copy muss vor Finalisierung durch `precision-writing-revision(genre=slide-copy)`; Design-/Template-Mapping geht an `presentation-template`.
