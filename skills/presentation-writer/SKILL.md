---
name: presentation-writer
description: Entwickelt aus einem freigegebenen Speaking-Konzept die sprachliche und dramaturgische Vortragsfassung mit Narrativ, Segmenten, Übergängen, Speaker Notes und Timing für Fach-, Wissenschafts-, Management-, Sales-, Keynote-, Schulungs- und Webinarformate.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - speaking-concept
  - speaker-profile
outputs:
  - presentation-narrative.json
  - speaker-notes.md
lastEvaluated: 2026-08-23
---

# Presentation Writer

## Zweck

Schreibt den **Vortrag**, nicht die fertige Folie. Die visuelle Übersetzung übernimmt `slide-architect`.

## Profile

- fachlich/wissenschaftlich
- Management/Board
- Sales/Pitch
- Keynote
- Schulung/Training
- Webinar

## Output

`presentation-narrative.json` enthält mindestens:

- Opening und Promise an das Publikum
- Segmente mit Ziel, Kernbotschaft und Evidence
- Übergänge zwischen Segmenten
- Speaker Notes beziehungsweise ausformulierbare Sprechpunkte
- Timing pro Segment
- geplante Interaktion/Fragen, falls relevant
- Closing und Call-to-Action

## Regeln

- keine Slide-Struktur aus Gewohnheit erzwingen;
- Speaker Notes nicht als On-Slide-Bullets behandeln;
- zentrale Daten/Claims mit Evidence Map verknüpfen;
- Storytelling dem Kommunikationsziel unterordnen;
- technische Tiefe an Audience und Format anpassen;
- Speaker Profile respektieren.

## Handoff

1. `slide-architect` für die visuelle Folienarchitektur.
2. `precision-writing-revision(genre=speaker-notes)` für die gesprochene Sprachfassung.
