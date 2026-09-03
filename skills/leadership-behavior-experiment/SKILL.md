---
name: leadership-behavior-experiment
description: Übersetzt ein Leadership-Entwicklungsziel oder eine Reflexionshypothese in ein kleines reales Verhaltensexperiment mit Zielkontext, Cue, Verhalten, Dosis, Messsignalen, erwarteter Wirkung und Stop-Bedingungen. Verwenden für testbares Führungslernen statt abstrakter Vorsätze.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
consumes:
  - leadership-development-model.json
  - leadership-reflection.json
outputs:
  - leadership-behavior-experiment.json
lastEvaluated: 2026-09-03
---

# Leadership Behavior Experiment

## Zweck

Macht Leadership-Entwicklung als kleines überprüfbares Experiment ausführbar. Das Experiment soll Verhalten testen, nicht Menschen manipulieren oder versteckte soziale Tests durchführen.

## Ablauf

1. genau eine priorisierte Hypothese bzw. ein Development Goal wählen.
2. reale Zielsituation und auslösenden Cue definieren.
3. konkretes eigenes Verhalten formulieren.
4. minimale Dosis bzw. Anzahl realer Gelegenheiten festlegen.
5. Verhaltensmaß und erwarteten Outcome getrennt definieren.
6. Failure Signals und Stop Conditions ergänzen.
7. Status `planned` setzen; erst reale Evidenz erlaubt `active`/`reviewed`.

## Output

`leadership-behavior-experiment.json` enthält mindestens `schemaVersion`, `experimentId`, `developmentGoalId`, `hypothesis`, `targetSituation`, `cue`, `behavior`, `dose`, `measures`, `expectedEffect`, `failureSignals`, `stopConditions`, `status` und `createdAt`.

Zulässige Statuswerte: `planned | active | reviewed | retained | modified | stopped`.

## Regeln

- Experiment betrifft primär das eigene Führungsverhalten.
- Keine Täuschung, Manipulation oder verdeckte Tests an Mitarbeitern.
- Verhalten und Outcome getrennt messen.
- Kleine reversible Experimente bevorzugen; bei relevantem HR-/Legal-/Safety-Risiko vorher `coaching-safety-routing`.
- Keine garantierte Wirkung behaupten.

## Übergabe

Nach realen Anwendungen → `leadership-coaching-review`; neue Beobachtungen können zusätzlich an `leadership-reflection` gehen.

## Abschlusskriterien

Cue, Verhalten, Dosis, Messsignal und Review-Bedingung sind konkret genug, dass die Führungskraft das Experiment in realen Situationen durchführen und danach auswerten kann.
