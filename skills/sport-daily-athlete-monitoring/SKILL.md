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
lastEvaluated: 2026-08-28
---

# Sport Daily Athlete Monitoring

Erfasse minimale, wiederholbare Daten für Trainingssteuerung. Morning-Status, passive Wearable-Daten und Post-Session-Reaktion bleiben unterscheidbare Ereignisse und behalten ihre Provenance.

## Trigger

Nutze diesen Skill für tägliche Check-ins, Session-RPE, geplante-vs.-durchgeführte Einheiten, standardisierte Belastungsreaktionen und die Einordnung automatisch importierter Wearable-/Health-Metriken.

## Voraussetzungen

Benötigt `athlete_id`, lokales Datum/Zeitzone und für Post-Session möglichst eine `planned_session_id`. Passive Daten sind optional; ihr Fehlen darf den Morning Check nicht blockieren.

## Ablauf

1. **Passive Daten zuerst einordnen.** Automatisch importierte Messwerte wie Schlafdauer, Ruhe-HF, HRV, Atemfrequenz, Hauttemperatur oder SpO₂ mit Messzeit, Quelle, Gerät, Methode und Qualitätsflag aufnehmen.
2. **Metric Class festlegen.** Jeden objektiven Wert als `direct_sensor`, `provider_derived`, `journal_derived`, `reference_measurement` oder `manual_measurement` klassifizieren.
3. **Decision Role festlegen.** Für jeden Wert sichtbar machen, ob er `primary_evidence`, `context_only`, `display_only` oder `excluded_from_adaptation` ist. Proprietäre Vendor-Scores wie Garmin Training Readiness, Body Battery, Sleep Score, Training Status oder Fitness Age sind standardmäßig höchstens Kontext und nie alleiniger Regler.
4. **Morning Check kurz halten.** Schlafqualität, Müdigkeit, Muskelkater, Stress und Motivation auf stabilen Skalen erfassen. Passive Sensorik reduziert Eingabeaufwand, ersetzt subjektive Athleteninformation aber nicht.
5. **Pain/Illness Gate anwenden.** Schmerz 0–10 mit Lokalisation und Krankheitssymptome separat erfassen; relevante Red Flags sofort markieren.
6. **Baselinebezug ermöglichen.** Rohwerte unverändert erhalten und nur methodisch vergleichbare Serien für individuelle Baselines freigeben. Geräte-/Methodenwechsel beginnen bei Bedarf eine neue `comparable_series_id`.
7. **Body-/Structural-Daten sauber trennen.** Körpergewicht, Taillenumfang, BIA- und DXA-Werte mit Methode und Qualitätsklasse erfassen. BIA-Schätzungen werden nicht als DXA-Referenzwerte behandelt; aus BIA abgeleitete „Knochendichte“ gilt nicht als echte BMD-Messung.
8. **Post-Session erfassen.** Dauer, Session-RPE, Completion-Status, externe Belastung, lokale Ermüdung, Schmerz und Planabweichungen dokumentieren.
9. **sRPE Load berechnen.** `duration_min × session_rpe` nur als interne Belastungsgröße ausgeben; nicht als medizinischen Risikoindex interpretieren.
10. **Freitext begrenzen.** Strukturdaten priorisieren und unnötige klinische Freitexte vermeiden.

## Provider-Score-Policy

Provider-Scores dürfen gespeichert und angezeigt werden, wenn ihre Quelle klar ist. Sie werden aber nicht in scheinbar direkte physiologische Messwerte umetikettiert.

Beispiele:

- Garmin HR/HRV/Respiration: Mess-/Sensorwerte mit Geräte- und Qualitätskontext.
- Garmin Sleep Score, Body Battery, Training Readiness, Training Status, Fitness Age: `provider_derived`, normalerweise `context_only` oder `display_only`.
- Journal-basierte Baselineabweichung oder Health Drift: `journal_derived`; nur erklärbar aus den zugrunde liegenden Messwerten.
- Biological Age, Pace of Aging, „gewonnene Lebenstage“ oder vergleichbare Longevity-Zahlen: `excluded_from_adaptation`; nicht als Gesundheitswahrheit persistieren.

## Kein magischer Readiness Score

Kein einzelner zusammengesetzter Prozentwert darf Schlaf, HRV, RPE oder Wohlbefinden in eine scheinpräzise Freigabe verdichten. Ampelzustände müssen aus expliziten Signalen und Regeln erklärbar bleiben.

## Prüfungen

- Sind Morning-, passive Sensor- und Post-Session-Daten zeitlich und semantisch getrennt?
- Haben objektive Metriken Quelle, Metric Class, Decision Role und Qualitätsflag?
- Wurden Vendor-Scores nicht als direkte Messwerte behandelt?
- Bleiben subjektive Daten trotz Wearable-Sync erhalten?
- Wurde sRPE nur aus tatsächlicher Dauer und Session-RPE berechnet?
- Sind Schmerz und Krankheitssymptome routbar?
- Sind fehlende Daten als fehlend statt als Normalwert gespeichert?
- Sind BIA/DXA/Scale/Tape-Serien methodisch getrennt?

## Sicherheitsgrenzen

Thoraxschmerz, Synkope, ungewöhnliche Dyspnoe, neurologische Warnzeichen, schwere systemische Symptome oder explizite medizinische Restriktionen dürfen nicht durch gute Wearable- oder Wellness-Scores überstimmt werden. Physiologische Abweichungen sind Signale, keine Diagnose.

## Fehlerbehandlung

- **Check-in unvollständig:** vorhandene Daten speichern, `uncertainties` erhöhen.
- **Keine geplante Session:** completed session als manuell erfassbar kennzeichnen.
- **Wearable-Ausreißer:** Rohwert mit `quality_flag` erhalten, nicht automatisch löschen oder überinterpretieren.
- **Provider-Sync fehlt:** subjektiven Check-in normal fortsetzen.
- **Geräte-/Methodenwechsel:** Vergleichsserie trennen oder Transferability explizit begründen.

## Übergabe

Outputs sind `daily-checkin.json` und `completed-session.json` gemäß den gleichnamigen `$defs` in `schemas/sport-athlete-management-v1.schema.json`. Beide gehen mit geplantem Mikrozyklus an die Adaptation Engine; Baselines, Health-Drift-Signale und Body-/Energy-Kontext werden nachgelagert in Recovery-/Adaptation-Analysen verdichtet.

## Abschlusskriterien

Die verfügbaren Morning-, Sensor- oder Post-Session-Daten liegen strukturiert, quellenklar, methodenbewusst, ohne Scheingenauigkeit und mit expliziten Safety Flags vor.
