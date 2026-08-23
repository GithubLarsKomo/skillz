---
name: speaking-grilling
description: Erhebt systematisch das Briefing für Reden und Vorträge: Anlass, Ziel, Publikum, Kernbotschaft, Sprecherrolle, Dauer, Ton, Evidenz, Risiken, Call-to-Action, Visuals und PPT-Template. Nutzt bei unvollständigem Kontext ein rundebasiertes Grilling statt Annahmen zu erfinden.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
outputs:
  - speaking-brief.json
lastEvaluated: 2026-08-23
---

# Speaking Grilling

## Zweck

Erzeuge vor Konzept und Draft ein belastbares Briefing für `speech|presentation`.

## Pflichtdimensionen

- Anlass und Format
- Ziel und gewünschte Wirkung
- Zielgruppe, Vorwissen, Haltung/Widerstände
- Sprecherrolle und Sprache (`de|en`, bei Englisch Zielvariante)
- Kernbotschaft
- Dauer und harte Zeitgrenzen
- Pflichtinhalte und No-go-Themen
- Evidenz-/Quellenbedarf
- Tonalität und gewünschte rhetorische Intensität
- vorhandenes Story-/Beispielmaterial
- Call-to-Action
- bei Präsentationen: Visual-Bedarf, bestehende Folien, Template/Referenzdeck

## Ablauf

1. Vorhandenen Kontext extrahieren und nicht erneut abfragen.
2. Fehlende entscheidungsrelevante Informationen priorisieren.
3. Fragen in kleinen logisch zusammenhängenden Runden stellen.
4. Antwortkonflikte sichtbar machen und auflösen.
5. Erst abschließen, wenn Ziel, Audience, Kernbotschaft und Dauer belastbar sind.
6. `speaking-brief.json` erzeugen und offene Annahmen kennzeichnen.

## Gate

Kein Handoff an `speaking-concept`, wenn `objective`, `audience`, `coreMessage` oder `durationMinutes` ungeklärt sind.
