---
name: leadership-coaching-review
description: Bewertet ein Leadership-Verhaltensexperiment nach realer Anwendung und trennt Adherence, beobachtete Verhaltensänderung, Outcome, Interpretation und Lernentscheidung. Verwenden für Retain/Modify/Stop-Entscheidungen und Re-Kalibrierung von Entwicklungszielen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
consumes:
  - leadership-behavior-experiment.json
  - leadership-development-model.json
outputs:
  - leadership-coaching-review.json
lastEvaluated: 2026-09-03
---

# Leadership Coaching Review

## Zweck

Prüft, was aus einem realen Verhaltensexperiment gelernt werden kann, ohne subjektive Nützlichkeit mit tatsächlicher Verhaltens- oder Outcome-Wirkung gleichzusetzen.

## Ablauf

1. geplante und tatsächlich beobachtete Anwendungen vergleichen.
2. Adherence separat bewerten.
3. Verhaltensevidenz gegen die definierten Measures prüfen.
4. Outcomes getrennt bewerten und Störfaktoren sichtbar halten.
5. Interpretation und Unsicherheit dokumentieren.
6. Entscheidung `retain | modify | stop | insufficient-evidence` treffen.
7. Development Goal bei Bedarf fortführen, revidieren oder schließen.

## Output

`leadership-coaching-review.json` enthält mindestens `schemaVersion`, `reviewId`, `experimentRef`, `adherence`, `behaviorChange`, `outcome`, `confounders`, `learning`, `decision`, `nextExperimentChanges`, `developmentGoalStatus`, `confidence` und `reviewedAt`.

## Regeln

- fehlende Durchführung ist keine Aussage über Wirksamkeit.
- gutes Gefühl ist kein ausreichender Outcome-Nachweis.
- einzelne Situationen nicht zu stabilen Persönlichkeitsschlüssen verallgemeinern.
- bei unzureichender Evidenz `insufficient-evidence` statt erzwungener Entscheidung.

## Übergabe

`modify` → `leadership-behavior-experiment`; neues oder verändertes Ziel → `leadership-development-model`; relevante Situation → `leadership-reflection`.

## Abschlusskriterien

Adherence, Verhalten, Outcome und Unsicherheit sind getrennt bewertet und eine nachvollziehbare nächste Lernentscheidung liegt vor.
