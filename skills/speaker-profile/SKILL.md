---
name: speaker-profile
description: Erstellt oder pflegt ein evidenzbasiertes Sprecherprofil für deutsche oder englische Reden und Vorträge mit Präferenzen zu Direktheit, Satzbau, Fachlichkeit, Humor, Emotionalität, Rhetorik, Aussprache und unerwünschten Mustern. Erfindet keine persönliche Stimme ohne belastbare Grundlage.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - author-voice-profiler
outputs:
  - speaker-profile.json
lastEvaluated: 2026-08-23
---

# Speaker Profile

## Zweck

Erweitert Author Voice um performative Merkmale für gesprochene Kommunikation. Profile werden mindestens nach Sprache und bei Bedarf nach Kontext getrennt.

## Merkmale

- Direktheit und Formalität
- Satz-/Atemeinheiten und bevorzugter Rhythmus
- technische Tiefe und Terminologiedichte
- Humor und Emotionalität
- rhetorische Mittel und deren Intensität
- bevorzugte bzw. unerwünschte Übergänge und Phrasen
- Umgang mit Zahlen, Abkürzungen und Fremdwörtern
- Aussprachehinweise
- Verhältnis Manuskriptfreiheit zu vollständigem Script

## Regeln

- Nur beobachtbare oder ausdrücklich bestätigte Merkmale aufnehmen.
- Keine psychologischen, demografischen oder sonstigen persönlichen Eigenschaften ableiten.
- Bestehendes `author-voice-profile.json` darf als Evidenz dienen, wird aber nicht blind auf gesprochene Sprache übertragen.
- Fehlende Evidenz führt zu Genre-Defaults, nicht zu erfundener Personalität.

## Handoff

Kompatibler Input für `speech-writer`, `presentation-writer` und `precision-writing-revision(mode=author)`.
