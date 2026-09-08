---
name: speaking-concept
description: Entwickelt aus einem belastbaren Speaking-Brief die freigabefähige Kommunikationsarchitektur für Rede oder Vortrag: Audience Insight, Kernthese, Supporting Messages, Dramaturgie, Evidence Map, Opening, Peak, Closing, Call-to-Action und Timing.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - speaking-grilling
outputs:
  - speaking-concept.json
lastEvaluated: 2026-08-23
---

# Speaking Concept

## Grundsatz

**Konzept vor Text.** Dieser Skill schreibt noch kein vollständiges Manuskript und keine fertigen Folien.

## Output-Struktur

- Kommunikationsziel
- Audience Insight
- Kernthese in einem Satz
- 3–5 Supporting Messages
- Evidence Map inklusive Confidence/Quellenbedarf
- Dramaturgie und Spannungsbogen
- Opening
- zentrale Wendepunkte und Peak
- Closing
- Call-to-Action
- Timing-Budget pro Segment
- sensible Aussagen, Compliance-/Reputationsrisiken und No-go-Aussagen
- Empfehlung `speech|presentation`

## Regeln

- Keine Claims erfinden, um eine Story zu schließen.
- Fehlende Evidenz als Recherchebedarf markieren.
- Dramaturgie aus Anlass und Audience ableiten, nicht aus Standardtemplates.
- Storytelling nur einsetzen, wenn es Botschaft und Glaubwürdigkeit unterstützt.
- Timing muss zur Gesamtzeit passen.

## Handoff

- `speech` → `speech-writer`
- `presentation` → `presentation-writer` und anschließend `slide-architect`
