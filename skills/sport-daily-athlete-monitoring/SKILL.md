---
name: sport-daily-athlete-monitoring
description: Erfasst einen kurzen Morning-Check, passive Wearable-/Biometrie-Kontexte und die tatsächliche Post-Session-Reaktion einschließlich sRPE, Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Schmerz und Krankheitssymptomen. Verwenden für tägliches longitudinales Monitoring; Wearable- oder Vendor-Scores nie als alleinigen Readiness-Regler oder medizinische Diagnose verwenden.
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

Erfasse minimale, wiederholbare Daten für Trainingssteuerung. Morning-Status, passive Biometrie und Post-Session-Reaktion bleiben unterscheidbare Ereignisse mit eigener Provenance. Passive Sensorik reduziert Eingabeaufwand, ersetzt aber nicht den Athletenbericht.

## Trigger

Nutze diesen Skill für tägliche Check-ins, passive Wearable-Kontexte, Session-RPE, geplante-vs.-durchgeführte Einheiten und standardisierte Belastungsreaktionen.

## Voraussetzungen

Benötigt `athlete_id`, lokales Datum/Zeitzone und für Post-Session möglichst eine `planned_session_id`. Passive Daten sind optional; fehlende Wearable-Daten machen einen manuellen Morning Check nicht ungültig.

## Ablauf

1. **Morning Check kurz halten.** Schlafqualität, Müdigkeit, Muskelkater, Stress und Motivation auf stabilen Skalen erfassen; Schlafdauer darf aus manueller oder geeigneter passiver Quelle stammen, die Quelle bleibt sichtbar.
2. **Pain/Illness Gate anwenden.** Schmerz 0–10 mit Lokalisation und Krankheitssymptome separat erfassen; relevante Red Flags sofort markieren.
3. **Passive Daten separat aufnehmen.** Ruhe-/Nacht-HF, HRV, Respiration, Schlafsummen, Hauttemperaturtrend, ausgewählte SpO₂-Werte oder vergleichbare Metriken nur mit `source`, `provider`, `device`/`method` soweit bekannt, `quality_flag`, `metric_class` und `decision_role` speichern.
4. **Vendor-Ableitungen klassifizieren.** Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age oder analoge Provider-Scores sind `provider_derived` und standardmäßig höchstens Kontext-/Anzeigeinformation; sie dürfen subjektive Angaben oder zugrunde liegende Signale nicht überschreiben.
5. **Methodengrenzen erhalten.** Körpermasse, Taille und Body-Composition-Daten nur mit Methode/Qualitätsklasse aufnehmen. BIA, DXA, Waage und Tape bleiben getrennte vergleichbare Serien; BIA-„bone density“ ist keine gemessene BMD.
6. **Baselinebezug ermöglichen.** Rohwerte unverändert erhalten. Geeignete direkte/manual/reference Metriken dürfen gegen individuelle, methodenkompatible Baselines interpretiert werden; fehlende Werte sind nicht „normal“.
7. **Health Drift kontextualisieren.** Einzelne Baselineabweichungen bleiben Kontext. Erst Persistenz, mehrere unabhängige Signale und/oder kompatible Symptome erhöhen die Relevanz. `Health Drift` beschreibt Instabilität, keine Diagnose.
8. **Post-Session erfassen.** Dauer, Session-RPE, Completion-Status, externe Belastung, lokale Ermüdung, Schmerz und Planabweichungen dokumentieren.
9. **sRPE Load berechnen.** `duration_min × session_rpe` nur als interne Belastungsgröße ausgeben; nicht als medizinischen Risikoindex interpretieren.
10. **Freitext begrenzen.** Strukturdaten priorisieren und unnötige klinische Freitexte vermeiden.

## Kein magischer Readiness Score

Kein einzelner zusammengesetzter Prozentwert darf Schlaf, HRV, RPE, Wohlbefinden oder passive Sensorik in eine scheinpräzise Freigabe verdichten. Garmin- oder andere Vendor-Scores können angezeigt werden, sind aber nicht der Regler. Biological Age, Pace of Aging, Lifespan-/„days gained“-Angaben, Metabolic Capacity/Momentum und universelle Health Scores sind keine autoritativen Monitoring-Konstrukte.

## Konflikte zwischen Mensch und Gerät

Wenn passive Daten und subjektiver Morning Check widersprechen, bleibt der Konflikt erhalten. Das System reduziert gegebenenfalls `confidence` und sucht nach Datenqualität, Kontext oder Persistenz, statt automatisch dem Gerät oder dem subjektiven Signal Vorrang zu geben.

## Prüfungen

- Sind Morning-, passive und Post-Session-Daten zeitlich/provenienzseitig unterscheidbar?
- Wurde sRPE nur aus tatsächlicher Dauer und Session-RPE berechnet?
- Sind direkte Sensorwerte und proprietäre Provider-Scores klassifiziert?
- Kann kein Vendor-Score allein eine Trainingsänderung auslösen?
- Sind Baseline-Serien methoden-/gerätekompatibel und Coverage/Qualität sichtbar?
- Sind Schmerz und Krankheitssymptome routbar?
- Sind Body-Composition-Methoden getrennt?
- Sind fehlende Daten als fehlend statt als Normalwert gespeichert?

## Sicherheitsgrenzen

Thoraxschmerz, Synkope, ungewöhnliche Dyspnoe, neurologische Warnzeichen, schwere systemische Symptome oder explizite medizinische Restriktionen dürfen nicht durch einen guten Wellness-, Recovery- oder Vendor-Score überstimmt werden.

## Fehlerbehandlung

- **Check-in unvollständig:** vorhandene Daten speichern, `uncertainties` erhöhen.
- **Passive Sync fehlt:** Morning Check normal fortsetzen; keinen Ersatzwert erfinden.
- **Wearable-Ausreißer:** Rohwert mit `quality_flag` erhalten, nicht automatisch löschen oder überinterpretieren.
- **Device-/Methodenwechsel:** neue oder nicht vergleichbare Serie markieren; Baseline nicht still fortschreiben.
- **Keine geplante Session:** completed session als manuell erfassbar kennzeichnen.

## Übergabe

Outputs sind `daily-checkin.json` und `completed-session.json` gemäß den gleichnamigen `$defs` in `schemas/sport-athlete-management-v1.schema.json`. `daily-checkin.json` kann klassifizierte `objective_metrics`, `body_measurements`, `biometric_baselines`, `biometric_anomalies` und den passiven Sync-Status enthalten. Beide Outputs gehen mit geplantem Mikrozyklus an die Adaptation Engine.

## Abschlusskriterien

Der Skill endet, wenn die verfügbaren subjektiven, passiven und Post-Session-Daten strukturiert, quellenklar, methodenbewusst, ohne Scheingenauigkeit und mit expliziten Safety Flags vorliegen.
