---
name: sport-training-adaptation-engine
description: Vergleicht geplante Belastung, tatsächlich absolvierte Einheit, subjektive und objektive Reaktion, Trends und Health Constraints und erzeugt eine erklärbare akute, taktische oder strategische Trainingsanpassung. Verwenden für Proceed/Modify/Recover/Review-Entscheidungen; nicht als autonomes medizinisches Clearance- oder Verletzungsvorhersagesystem.
---

# Sport Training Adaptation Engine

Schließe den Trainingsregelkreis mit einer nachvollziehbaren, auditierbaren Entscheidung. Einzelmetriken liefern Evidenz; sie sind nicht der Regler.

## Trigger

Nutze diesen Skill vor einer geplanten Schlüsselbelastung, nach einer unerwarteten Trainingsreaktion oder bei wiederholtem Soll/Ist-Mismatch.

## Voraussetzungen

Mindestens verfügbar sein sollten:

- aktuelle Athletenprofil-Version,
- aktiver Mikro-/Mesokontext,
- nächste geplante Session,
- letzter Morning Check und/oder relevante jüngste Sessiondaten,
- bekannte aktive Health Constraints.

Fehlende Daten reduzieren `confidence`; sie werden nicht durch Annahmen ersetzt.

## Ablauf

1. **Safety Gate zuerst.** Explizite medizinische Restriktionen und Red Flags vor Performance-Optimierung prüfen.
2. **Soll/Ist vergleichen.** Geplante gegen absolvierte Dauer, Intensität, RPE, externe Leistung und Qualitätsmarker stellen.
3. **Reaktion kontextualisieren.** Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Schmerz, Krankheit und optionale objektive Metriken gemeinsam betrachten.
4. **Trend statt Einzelpunkt prüfen.** Individuelle Baseline, Wiederholung gleicher Standardbelastung und relevante Mehrtagessignale bevorzugen.
5. **Entscheidungsebene wählen.** `acute`, `tactical` oder `strategic` nur so hoch eskalieren wie die Evidenz rechtfertigt.
6. **Aktion bestimmen.** `proceed`, `reduce_volume`, `reduce_intensity`, `substitute`, `move_session`, `recovery`, `progress`, `delay_progression`, `retest`, `health_route` oder `medical_review` verwenden.
7. **Änderung minimal halten.** Primärziel schützen und nur die kleinste sinnvolle Änderung vornehmen.
8. **Audit Trail schreiben.** Trigger, Input-Snapshot, vorherige Prescription, Änderung, rationale, confidence, safety state und human override vollständig erhalten.

## Safety State Machine

- **GREEN:** keine relevante negative Evidenz; wie geplant.
- **YELLOW:** moderater Mismatch; Ziel erhalten, Last oder Recovery ggf. fein anpassen.
- **ORANGE:** mehrere negative Signale oder zunehmende lokale Symptomatik; deutliche Modifikation/Substitution und Reassessment.
- **RED:** medizinisches Warnsignal oder explizite Restriktion; keine normale Progression, geeignete medizinische Abklärung routen.

Jede Farbe braucht eine textliche Begründung und verantwortliche Signale.

## Verbotene Abkürzungen

- Kein einzelner Readiness-Prozentwert steuert Training.
- HRV darf Training nicht allein hoch- oder herunterregeln.
- ACWR darf nicht als automatischer Verletzungsvorhersager dienen.
- Alter >50 darf nicht automatisch Intensität oder Power entfernen.
- Menstruationsphase darf nicht ohne individuelle Evidenz die Periodisierung diktieren.

## Prüfungen

- Wurde das Safety Gate vor Leistungsoptimierung geprüft?
- Ist jede Entscheidung auf konkrete Inputs zurückführbar?
- Ist die Änderung kleiner als ein unnötiger Plan-Rewrite?
- Sind Confidence und fehlende Daten sichtbar?
- Bleibt bei 50+ und allen Geschlechtern die individuelle Reaktion primär?
- Ist ein späterer Human Override auditierbar?

## Fehlerbehandlung

- **Sparse data:** konservativere Confidence, aber keine automatische Trainingsreduktion ohne Signal.
- **Widersprüchliche Signale:** Schlüsselreiz ggf. schützen, Modifikation klein halten und zusätzlichen Checkpoint definieren.
- **Red Flag:** normale Adaptationslogik verlassen und Health/Medical Routing priorisieren.
- **Plan fehlt:** keine Revision erfinden; `decision=review_required` ausgeben.

## Übergabe

Output ist `training-adaptation-decision.json` gemäß `$defs.adaptationDecision`. Planrevisionen referenzieren die betroffenen IDs und erhöhen deren Version; Vorversionen bleiben auditierbar.

## Abschlusskriterien

Der Skill endet, wenn eine minimale, erklärbare und sicherheitsgeprüfte Entscheidung mit Ebene, Aktion, Begründung, Confidence, Safety State, Input-Snapshot und Revisionsreferenzen vorliegt.
