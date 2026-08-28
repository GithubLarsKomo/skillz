---
name: sport-training-adaptation-engine
description: Vergleicht geplante Belastung, tatsächlich absolvierte Einheit, subjektive und objektive Reaktion, passive Biomarker, Trends und Health Constraints und erzeugt eine erklärbare akute, taktische oder strategische Trainingsanpassung. Verwenden für Proceed/Modify/Recover/Review-Entscheidungen; Vendor-Readiness-Scores nicht als autonome Regler und den Skill nicht als medizinisches Clearance- oder Verletzungsvorhersagesystem verwenden.
---

# Sport Training Adaptation Engine

Schließe den Trainingsregelkreis mit einer nachvollziehbaren, auditierbaren Entscheidung. Einzelmetriken und Provider-Scores liefern höchstens Evidenz beziehungsweise Kontext; sie sind nicht der Regler.

## Trigger

Nutze diesen Skill vor einer geplanten Schlüsselbelastung, nach einer unerwarteten Trainingsreaktion, bei wiederholtem Soll/Ist-Mismatch oder bei persistenter multisignaler physiologischer Abweichung.

## Voraussetzungen

Mindestens verfügbar sein sollten:

- aktuelle Athletenprofil-Version,
- aktiver Mikro-/Mesokontext,
- nächste geplante Session,
- letzter Morning Check und/oder relevante jüngste Sessiondaten,
- bekannte aktive Health Constraints.

Soweit vorhanden zusätzlich:

- klassifizierte direkte/passive `objective_metrics`,
- individuelle `biometric_baselines`,
- `biometric_anomalies` / Health-Drift-Kontext,
- methodenbewusster Body-/Energy-Kontext,
- separat gekennzeichnete `provider_score_context`-Werte.

Fehlende Daten reduzieren `confidence`; sie werden nicht durch Annahmen ersetzt.

## Ablauf

1. **Safety Gate zuerst.** Explizite medizinische Restriktionen und Red Flags vor Performance-Optimierung prüfen. Ein günstiger Wearable- oder Vendor-Score kann das Safety Gate nie überstimmen.
2. **Inputklassen prüfen.** Direkte Sensorwerte, manuelle/reference Messungen, Sports-Journal-Ableitungen und proprietäre Provider-Scores anhand `metric_class`, `decision_role`, Qualität und Provenance unterscheiden.
3. **Soll/Ist vergleichen.** Geplante gegen absolvierte Dauer, Intensität, RPE, externe Leistung und Qualitätsmarker stellen.
4. **Reaktion kontextualisieren.** Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Schmerz, Krankheit, Training Tolerance und geeignete objektive/passive Metriken gemeinsam betrachten.
5. **Trend statt Einzelpunkt prüfen.** Individuelle Baseline, Wiederholung gleicher Standardbelastung, Persistenz und relevante Mehrtagessignale bevorzugen.
6. **Health Drift nur multisignal nutzen.** Ein isolierter HRV-, Ruhe-HF-, Temperatur-, Respirations- oder SpO₂-Ausreißer löst keine Trainingsänderung aus. `persistent` Health Drift kann zusammen mit Symptomen, Recovery-/Load-Kontext oder weiteren unabhängigen Signalen `health_route` stützen.
7. **Provider-Scores begrenzen.** Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age und analoge Vendor-Werte bleiben höchstens Kontext. Sie dürfen GREEN/YELLOW/ORANGE/RED, `action` oder Planrevision nie unabhängig bestimmen.
8. **Body-/Energy-Kontext proportional nutzen.** Körpermasse oder BIA allein erzeugen keine akute Trainingsmodifikation. Wiederholte methodenkompatible Veränderungen zusammen mit Performance-/Recovery-/Fueling-Signalen können eine Fueling-/RED-S-/Health-Review anstoßen.
9. **Entscheidungsebene wählen.** `acute`, `tactical` oder `strategic` nur so hoch eskalieren wie die Evidenz rechtfertigt.
10. **Aktion bestimmen.** `proceed`, `reduce_volume`, `reduce_intensity`, `substitute`, `move_session`, `recovery`, `progress`, `delay_progression`, `retest`, `health_route`, `medical_review` oder `review_required` verwenden.
11. **Änderung minimal halten.** Primärziel schützen und nur die kleinste sinnvolle Änderung vornehmen.
12. **Audit Trail schreiben.** Trigger, Input-Snapshot, vorherige Prescription, Änderung, `responsible_signals`, `provider_score_context`, Multi-Signal-Bestätigung, rationale, confidence, safety state und human override vollständig erhalten.

## Safety State Machine

- **GREEN:** keine relevante negative Evidenz; wie geplant.
- **YELLOW:** moderater Mismatch; Ziel erhalten, Last oder Recovery ggf. fein anpassen.
- **ORANGE:** mehrere negative Signale, persistenter plausibler Health Drift oder zunehmende lokale Symptomatik; deutliche Modifikation/Substitution und Reassessment.
- **RED:** medizinisches Warnsignal oder explizite Restriktion; keine normale Progression, geeignete medizinische Abklärung routen.

Jede Farbe braucht eine textliche Begründung und explizite verantwortliche Signale. Provider-Scores dürfen als sekundärer Kontext genannt werden, aber nie allein verantwortliches Signal sein.

## Verbotene Abkürzungen

- Kein einzelner Readiness-, Health- oder Longevity-Prozentwert steuert Training.
- Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age oder analoge Vendor-Scores bestimmen keine Ampel allein.
- Biological Age, Pace of Aging, Lifespan-/„days gained“-Angaben und Metabolic Capacity/Momentum sind keine Adaptationsregler.
- HRV darf Training nicht allein hoch- oder herunterregeln.
- ACWR darf nicht als automatischer Verletzungsvorhersager dienen.
- Körpergewicht oder BIA darf keine akute Trainingsentscheidung allein auslösen.
- Alter >50 darf nicht automatisch Intensität oder Power entfernen.
- Menstruationsphase darf nicht ohne individuelle Evidenz die Periodisierung diktieren.

## Prüfungen

- Wurde das Safety Gate vor Leistungsoptimierung geprüft?
- Ist jede Entscheidung auf konkrete `responsible_signals` zurückführbar?
- Sind Vendor-Scores von zugrunde liegenden/direct Signalen getrennt?
- Kann kein einzelner Vendor-Score oder Biomarker die Ampel/Planrevision allein bestimmen?
- Wurde bei Health Drift Persistenz, Multi-Signal-Bestätigung und Kontext geprüft?
- Sind Methoden-/Device-Wechsel und Datenqualität berücksichtigt?
- Ist die Änderung kleiner als ein unnötiger Plan-Rewrite?
- Sind Confidence und fehlende Daten sichtbar?
- Bleibt bei 50+ und allen Geschlechtern die individuelle Reaktion primär?
- Ist ein späterer Human Override auditierbar?

## Fehlerbehandlung

- **Sparse data:** konservativere Confidence, aber keine automatische Trainingsreduktion ohne Signal.
- **Passive Sync fehlt:** subjektive und Sessiondaten normal verarbeiten; keinen Wearable-Ersatzwert erfinden.
- **Widersprüchliche Signale:** Konflikt sichtbar halten, Schlüsselreiz ggf. schützen, Modifikation klein halten und zusätzlichen Checkpoint definieren.
- **Vendor-Score ohne Rohkontext:** als `context_only`/`display_only` behandeln, nicht als Entscheidungsbeleg hochstufen.
- **Device-/Methodenwechsel:** Baseline-/Trendvergleich bis zur geklärten Vergleichbarkeit abwerten.
- **Red Flag:** normale Adaptationslogik verlassen und Health/Medical Routing priorisieren.
- **Plan fehlt:** keine Revision erfinden; `decision=review_required` ausgeben.

## Übergabe

Output ist `training-adaptation-decision.json` gemäß `$defs.adaptationDecision`. Er enthält insbesondere `responsible_signals`, optional `provider_score_context` und `multi_signal_confirmation`. Planrevisionen referenzieren die betroffenen IDs und erhöhen deren Version; Vorversionen bleiben auditierbar.

## Abschlusskriterien

Der Skill endet, wenn eine minimale, erklärbare und sicherheitsgeprüfte Entscheidung mit Ebene, Aktion, Begründung, Confidence, Safety State, Input-Snapshot, verantwortlichen Signalen, Vendor-Kontexttrennung und Revisionsreferenzen vorliegt.
