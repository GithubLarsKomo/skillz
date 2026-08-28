---
name: sport-daily-athlete-monitoring
description: Erfasst einen kurzen Morning-Check und die tatsächliche Post-Session-Reaktion einschließlich sRPE, Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Schmerz, Krankheitssymptomen und optionalen objektiven Metriken. Verwenden für tägliches longitudinales Monitoring; nicht als alleiniger Readiness-Score oder medizinische Diagnose.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
outputs:
  - daily-checkin.json
  - completed-session.json
lastEvaluated: 2026-08-22
---

# Sport Daily Athlete Monitoring

Erfasse minimale, wiederholbare Daten für Trainingssteuerung. Morning-Status und Post-Session-Reaktion bleiben getrennte Ereignisse.

## Trigger

Nutze diesen Skill für tägliche Check-ins, Session-RPE, geplante-vs.-durchgeführte Einheiten und standardisierte Belastungsreaktionen.

## Voraussetzungen

Benötigt `athlete_id`, lokales Datum/Zeitzone und für Post-Session möglichst eine `planned_session_id`.

## Ablauf

1. **Morning Check kurz halten.** Schlafdauer, Schlafqualität, Müdigkeit, Muskelkater, Stress und Motivation auf stabilen Skalen erfassen.
2. **Pain/Illness Gate anwenden.** Schmerz 0–10 mit Lokalisation und Krankheitssymptome separat erfassen; relevante Red Flags sofort markieren.
3. **Objektive Daten optional aufnehmen.** Ruhe-HF, HRV oder weitere Metriken mit Quelle und Qualitätsflag speichern; sie dürfen nie allein die Entscheidung dominieren.
4. **Post-Session erfassen.** Dauer, Session-RPE, Completion-Status, externe Belastung, lokale Ermüdung, Schmerz und Planabweichungen dokumentieren.
5. **sRPE Load berechnen.** `duration_min × session_rpe` nur als interne Belastungsgröße ausgeben; nicht als medizinischen Risikoindex interpretieren.
6. **Baselinebezug ermöglichen.** Rohwerte unverändert erhalten; Trends werden nachgelagert gegen individuelle Baselines interpretiert.
7. **Freitext begrenzen.** Strukturdaten priorisieren und unnötige klinische Freitexte vermeiden.

## Kein magischer Readiness Score

Kein einzelner zusammengesetzter Prozentwert darf Schlaf, HRV, RPE oder Wohlbefinden in eine scheinpräzise Freigabe verdichten. Ampelzustände müssen aus expliziten Signalen und Regeln erklärbar bleiben.

## Prüfungen

- Sind Morning- und Post-Session-Daten zeitlich getrennt?
- Wurde sRPE nur aus tatsächlicher Dauer und Session-RPE berechnet?
- Bleiben HRV/Ruhe-HF optionale Kontextsignale?
- Sind Schmerz und Krankheitssymptome routbar?
- Sind fehlende Daten als fehlend statt als Normalwert gespeichert?

## Sicherheitsgrenzen

Thoraxschmerz, Synkope, ungewöhnliche Dyspnoe, neurologische Warnzeichen, schwere systemische Symptome oder explizite medizinische Restriktionen dürfen nicht durch einen guten Wellness-Score überstimmt werden.

## Fehlerbehandlung

- **Check-in unvollständig:** vorhandene Daten speichern, `uncertainties` erhöhen.
- **Keine geplante Session:** completed session als manuell erfassbar kennzeichnen.
- **Wearable-Ausreißer:** Rohwert mit `quality_flag` erhalten, nicht automatisch löschen oder überinterpretieren.

## Übergabe

Outputs sind `daily-checkin.json` und `completed-session.json` gemäß den gleichnamigen `$defs` in `schemas/sport-athlete-management-v1.schema.json`. Beide gehen mit geplantem Mikrozyklus an die Adaptation Engine.

## Abschlusskriterien

Der Skill endet, wenn die verfügbaren Morning- oder Post-Session-Daten strukturiert, quellenklar, ohne Scheingenauigkeit und mit expliziten Safety Flags vorliegen.
