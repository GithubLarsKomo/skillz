---
name: sport-training-adaptation-engine
description: Vergleicht geplante Belastung, tatsächlich absolvierte Einheit, subjektive und objektive Reaktion, Trends und Health Constraints und erzeugt eine erklärbare akute, taktische oder strategische Trainingsanpassung. Verwenden für Proceed/Modify/Recover/Review-Entscheidungen; nicht als autonomes medizinisches Clearance- oder Verletzungsvorhersagesystem.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-microcycle-planning
  - sport-daily-athlete-monitoring
outputs:
  - training-adaptation-decision.json
lastEvaluated: 2026-08-28
---

# Sport Training Adaptation Engine

Schließe den Trainingsregelkreis mit einer nachvollziehbaren, auditierbaren Entscheidung. Einzelmetriken und Provider-Scores liefern Evidenz; sie sind nicht der Regler.

## Trigger

Nutze diesen Skill vor einer geplanten Schlüsselbelastung, nach einer unerwarteten Trainingsreaktion, bei wiederholtem Soll/Ist-Mismatch oder bei persistenter multisignal-physiologischer Abweichung.

## Voraussetzungen

Mindestens verfügbar sein sollten:

- aktuelle Athletenprofil-Version,
- aktiver Mikro-/Mesokontext,
- nächste geplante Session,
- letzter Morning Check und/oder relevante jüngste Sessiondaten,
- bekannte aktive Health Constraints.

Optional einbeziehen:

- methodisch klassifizierte Wearable-/Garmin-Metriken,
- Recovery State,
- Health-Drift-/Baseline-Signale,
- Body-/Energy-Kontext,
- longitudinale Adaptation Analysis.

Fehlende Daten reduzieren `confidence`; sie werden nicht durch Annahmen ersetzt.

## Ablauf

1. **Safety Gate zuerst.** Explizite medizinische Restriktionen und Red Flags vor Performance-Optimierung prüfen.
2. **Soll/Ist vergleichen.** Geplante gegen absolvierte Dauer, Intensität, RPE, externe Leistung und Qualitätsmarker stellen.
3. **Reaktion kontextualisieren.** Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Schmerz, Krankheit und objektive Metriken gemeinsam betrachten.
4. **Signalqualität prüfen.** Metric Class, Decision Role, Qualitätsflag, Geräte-/Methodenwechsel und Vergleichbarkeit berücksichtigen.
5. **Provider-Scores begrenzen.** Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age oder vergleichbare Vendor-Scores dürfen eine Entscheidung unterstützen, aber nie als alleiniger verantwortlicher Trigger oder als medizinische Clearance dienen.
6. **Trend statt Einzelpunkt prüfen.** Individuelle Baseline, Wiederholung gleicher Standardbelastung, multisignal-Health-Drift und relevante Mehrtagessignale bevorzugen.
7. **Health Drift richtig behandeln.** Physiologische Abweichungen ohne Symptome führen zunächst zu Kontext/Reassessment. Persistente multisignal-Abweichung plus Symptome oder Red Flags kann zu `health_route`/`medical_review` führen.
8. **Body-/Energy-Kontext proportional behandeln.** Körpergewicht oder BIA-Werte lösen keine akute Trainingsreduktion allein aus; kombinierte relevante Trends können Fueling-/RED-S-/Health-Review triggern.
9. **Entscheidungsebene wählen.** `acute`, `tactical` oder `strategic` nur so hoch eskalieren wie die Evidenz rechtfertigt.
10. **Aktion bestimmen.** `proceed`, `reduce_volume`, `reduce_intensity`, `substitute`, `move_session`, `recovery`, `progress`, `delay_progression`, `retest`, `health_route` oder `medical_review` verwenden.
11. **Änderung minimal halten.** Primärziel schützen und nur die kleinste sinnvolle Änderung vornehmen.
12. **Audit Trail schreiben.** Trigger, Input-Snapshot, Metric-/Provider-Kontext, vorherige Prescription, Änderung, rationale, responsible signals, Confidence, Safety State und Human Override vollständig erhalten.

## Safety State Machine

- **GREEN:** keine relevante negative Evidenz; wie geplant.
- **YELLOW:** moderater Mismatch oder begrenzte multisignal-Abweichung; Ziel erhalten, Last oder Recovery ggf. fein anpassen.
- **ORANGE:** mehrere negative Signale, persistenter Health Drift mit passendem Kontext oder zunehmende lokale Symptomatik; deutliche Modifikation/Substitution und Reassessment.
- **RED:** medizinisches Warnsignal oder explizite Restriktion; keine normale Progression, geeignete medizinische Abklärung routen.

Jede Farbe braucht eine textliche Begründung und verantwortliche Signale. Ein Vendor-Score allein darf nie die Farbe bestimmen.

## Verbotene Abkürzungen

- Kein einzelner Readiness-Prozentwert steuert Training.
- HRV darf Training nicht allein hoch- oder herunterregeln.
- Garmin-/Hume-/andere Vendor-Scores dürfen nicht als validierte Gesamtgesundheit interpretiert werden.
- Biological Age, Pace of Aging, Lifespan Meter oder Metabolic Capacity sind keine Adaptationsregler.
- ACWR darf nicht als automatischer Verletzungsvorhersager dienen.
- Alter >50 darf nicht automatisch Intensität oder Power entfernen.
- Menstruationsphase darf nicht ohne individuelle Evidenz die Periodisierung diktieren.

## Prüfungen

- Wurde das Safety Gate vor Leistungsoptimierung geprüft?
- Ist jede Entscheidung auf konkrete Inputs zurückführbar?
- Wurde Metric Class/Decision Role berücksichtigt?
- Ist bei Vendor-Scores klar, welche zugrunde liegenden Signale die Entscheidung tragen?
- Basiert eine physiologische Eskalation auf Persistenz/Mehrfachsignalen oder echten Red Flags statt auf einem Einzelwert?
- Ist die Änderung kleiner als ein unnötiger Plan-Rewrite?
- Sind Confidence und fehlende Daten sichtbar?
- Bleibt bei 50+ und allen Geschlechtern die individuelle Reaktion primär?
- Ist ein späterer Human Override auditierbar?

## Fehlerbehandlung

- **Sparse data:** konservativere Confidence, aber keine automatische Trainingsreduktion ohne Signal.
- **Widersprüchliche Signale:** Schlüsselreiz ggf. schützen, Modifikation klein halten und zusätzlichen Checkpoint definieren.
- **Provider-Score widerspricht Roh-/Athletendaten:** Konflikt sichtbar halten; Provider-Score nicht privilegieren.
- **Red Flag:** normale Adaptationslogik verlassen und Health/Medical Routing priorisieren.
- **Plan fehlt:** keine Revision erfinden; `decision=review_required` ausgeben.

## Übergabe

Output ist `training-adaptation-decision.json` gemäß `$defs.adaptationDecision`. Planrevisionen referenzieren die betroffenen IDs und erhöhen deren Version; Vorversionen bleiben auditierbar.

## Abschlusskriterien

Eine minimale, erklärbare und sicherheitsgeprüfte Entscheidung liegt mit Ebene, Aktion, Begründung, Confidence, Safety State, Input-Snapshot, verantwortlichen Signalen, Provider-Kontext und Revisionsreferenzen vor.
