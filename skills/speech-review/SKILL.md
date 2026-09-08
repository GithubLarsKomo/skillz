---
name: speech-review
description: Prüft und verbessert eine sprachoptimierte Rede auf Audience Fit, Kernbotschaft, Dramaturgie, Evidenz/Fidelity, Sprechbarkeit, Authentizität, rhetorische Angemessenheit, Erinnerungswert, Timing und Call-to-Action.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - precision-writing-revision
outputs:
  - speech-review.json
  - final-speech.md
lastEvaluated: 2026-08-23
---

# Speech Review

## Review-Dimensionen

Bewerte jeweils mit Begründung:

- Audience Fit
- Core Message Clarity
- Narrative Coherence
- Evidence/Fidelity
- Spoken-Language Quality
- Speaker-Profile Fit
- Rhetorical Appropriateness
- Memorability
- Timing
- Call-to-Action

## Ablauf

1. Konzept gegen Rede prüfen.
2. Fidelity-Status aus `precision-writing-revision` übernehmen und offene Punkte prüfen.
3. Vorlese-/Sprechbarkeitsprüfung simulieren: Satzlänge, Atemeinheiten, Zungenbrecher, Zahlen und Fachbegriffe.
4. Timing anhand Wortzahl, Pausen und vorgesehenem Vortragstempo plausibilisieren.
5. Nur konkrete Schwachstellen revidieren; keine vollständige Neuschreibung ohne Grund.
6. Geänderte Stellen erneut durch Fidelity-Gate führen.

## Hard Fails

- neuer oder veränderter fachlicher Claim;
- nicht auflösbarer Widerspruch zum Konzept;
- deutliche Überschreitung einer harten Zeitgrenze;
- rhetorische Zuspitzung, die Evidenz oder Compliance-Grenzen verletzt.

## Abschluss

Final, wenn alle Hard Fails geschlossen und die wesentlichen Review-Dimensionen freigabefähig sind.
