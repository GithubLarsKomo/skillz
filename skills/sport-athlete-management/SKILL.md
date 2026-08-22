---
name: sport-athlete-management
description: Orchestriert den geschlossenen Sport-Trainingsregelkreis von Athletenprofil und Zielmodell über Saison-, Meso- und Mikroplanung zu Daily Monitoring, spezialisierten Kraft-/Ausdauer-/Recovery-/Fueling-/Health-Modulen und auditierbarer Adaptation. Verwenden für longitudinale Trainingssteuerung über mehrere Ebenen; Fachlogik der Spezialskills nicht duplizieren.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-goal-performance-model
  - sport-season-periodization
  - sport-mesocycle-planning
  - sport-microcycle-planning
  - sport-daily-athlete-monitoring
  - sport-strength-power-programming
  - sport-endurance-programming
  - sport-recovery-sleep
  - sport-nutrition-fueling
  - sport-injury-rehabilitation
  - sport-return-after-illness
  - sport-testing-battery
  - sport-adaptation-analysis
  - sport-training-adaptation-engine
outputs:
  - athlete-management-state.json
  - next-training-decision.json
  - plan-revision.json
lastEvaluated: 2026-08-22
---

# Sport Athlete Management

Koordiniere die Sport-Skills als persistenten Regelkreis. Strukturierte Artefakte sind die fachliche Wahrheit; Reports und Web-UIs sind abgeleitete Ansichten.

## Trigger

Nutze diesen Orchestrator, wenn nicht nur ein einmaliger Trainingsplan, sondern fortlaufende Zielsetzung, Planung, tägliche Rückmeldung und Anpassung verlangt werden.

Für reine Testauswertung weiterhin `sport-performance-diagnostics`; für einen einmaligen Plan kann `sport-training-programming` direkt verwendet werden.

## Voraussetzungen

Mindestens Athletenidentität und Ziel müssen bekannt sein. Für laufende Steuerung werden die jeweils aktuellen Versionen von Profil, Performance-Modell, Saison/Meso/Mikro, Monitoring, relevanten P1-Spezialartefakten und Adaptationsentscheidungen referenziert.

## Ablauf

1. **State laden.** Aktuelle IDs und Versionen der kanonischen Sport-Artefakte bestimmen.
2. **Fehlende Ebene routen.** Profil → Zielmodell → Saison → Meso → Mikro nur dort erzeugen, wo Zustand fehlt oder abgelaufen ist.
3. **Fachmodule selektiv routen.** Je nach Ziel und Sessiontyp `sport-strength-power-programming` und/oder `sport-endurance-programming` verwenden; Recovery/Fueling/Testplanung nur bei fachlichem Bedarf aktualisieren.
4. **Health Routing priorisieren.** Dokumentierte Verletzung → `sport-injury-rehabilitation`; Rückkehr nach akuter Erkrankung → `sport-return-after-illness`. Diese Module erzeugen Kriterien und Grenzen, keine Diagnose oder medizinische Freigabe.
5. **Heute bestimmen.** Geplante Session, jüngsten Morning Check und relevante aktuelle Recovery-/Health-Artefakte zusammenführen.
6. **Training protokollieren.** Completed Session und sRPE über `sport-daily-athlete-monitoring` erfassen.
7. **Trend analysieren.** Bei ausreichender longitudinaler Datenbasis `sport-adaptation-analysis` verwenden; Einzelmetriken nicht als Regler behandeln.
8. **Adaptation ausführen.** `sport-training-adaptation-engine` nur bei relevantem Checkpoint oder Mismatch aufrufen. P1-Spezialisten liefern Evidenz und Optionen; die Engine besitzt die übergreifende Proceed/Modify/Recover/Review-Entscheidung.
9. **Versioniert revidieren.** Betroffene Fach- und Mikro-/Meso-/Saisonobjekte über ihre Eigentümer-Skills neu erzeugen; alte Version behalten.
10. **State fortschreiben.** Nächste Entscheidung, offene Unsicherheiten, Safety Flags und nächste Re-Evaluation zusammenfassen.

## P1-Routingregeln

- **Kraft/Power:** `sport-strength-power-programming` besitzt Satz-/Wiederholungs-/Last-/RIR-/Power-Prescription. 50+ ist kein automatischer Grund, Power oder hohe Intensität zu entfernen.
- **Ausdauer:** `sport-endurance-programming` besitzt Intensitätsdomänen, Intervallstruktur und Pace/Power/HR-Regeln. HRV allein darf die Prescription nicht steuern.
- **Recovery:** `sport-recovery-sleep` interpretiert Schlaf, Fatigue und Kontext mehrdimensional und liefert keinen opaken Readiness-Score.
- **Fueling:** `sport-nutrition-fueling` unterstützt Leistungsversorgung und RED-S-Risikoerkennung für alle Geschlechter, ersetzt aber keine klinische Ernährungsmedizin.
- **Rehabilitation:** `sport-injury-rehabilitation` arbeitet nur auf dokumentierten medizinischen/physiotherapeutischen Constraints und kriteriumsorientiert, nicht kalenderbasiert.
- **Illness return:** `sport-return-after-illness` stoppt normale Progression bei kardio-pulmonalen/systemischen Red Flags und routet medizinische Abklärung.
- **Testing:** `sport-testing-battery` wählt minimale, entscheidungsrelevante Testbatterien nach Sport, Ziel und Saisonphase.
- **Longitudinale Analyse:** `sport-adaptation-analysis` trennt beobachtete Signale, Unsicherheit und Missing-Data-Effekte; ACWR ist kein kausaler Verletzungsprädiktor.

## Systemgrenzen

Die WebApp und relationale Datenbank leben in einem separaten Produkt-Repository. `skillz` besitzt Fachlogik und JSON-Verträge, aber keine produktive Web-/DB-Implementierung. Die Produkt-App darf diese Verträge konsumieren und persistieren.

## Alters- und Geschlechtsregeln

Alle nachgelagerten Entscheidungen verwenden Alter und Geschlecht als Kontextmodifier. Individuelle Trainingsreaktion bleibt primär; keine pauschale Masters-Abwertung und keine starre Zyklusperiodisierung. Optionale menstruelle/peri-/postmenopausale Kontexte werden symptom- und evidenzbasiert behandelt.

## Prüfungen

- Ist jede Ebene über IDs/Versionen statt impliziten Chat-Kontext verbunden?
- Besitzt jede Fachentscheidung genau einen verantwortlichen Skill?
- Informieren P1-Spezialisten die zentrale Adaptation, ohne deren Entscheidungslogik zu duplizieren?
- Sind Reports/UI nicht Source of Truth?
- Bleiben Audit Trail und Vorversionen erhalten?
- Können fehlende Daten ohne erfundene Werte weitergereicht werden?
- Werden Health/Medical Red Flags vor Performance-Optimierung geroutet?

## Fehlerbehandlung

- **Unvollständiger State:** nur fehlende Ebene erzeugen und Abhängigkeiten erhalten.
- **Widersprüchliche Versionen:** keine stille Überschreibung; Konflikt als Reconciliation-Bedarf markieren.
- **Safety Red Flag:** Performance-Orchestrierung unterbrechen und Health/Medical Routing priorisieren.
- **P1-Artefakt fehlt:** nicht erfinden; Unsicherheit markieren und nur dann erzeugen, wenn die Entscheidung es benötigt.
- **Produkt-App nicht verfügbar:** Fachartefakte bleiben als JSON unabhängig nutzbar.

## Übergabe

P0-Vertragsdefinition bleibt `schemas/sport-athlete-management-v1.schema.json`. P1-Spezialartefakte verwenden `schemas/sport-athlete-management-p1-v1.schema.json`, sodass Produktintegrationen P1 bewusst und versioniert übernehmen können. Das separate WebApp-Repository konsumiert diese Verträge über versionierte API-/Persistenzmodelle; Report-Workflows können dieselben Artefakte lesen.

## Abschlusskriterien

Der Orchestrator ist abgeschlossen, wenn der aktuelle Athlete-Management-State konsistent ist, die nächste Trainingsentscheidung eindeutig referenziert wird, erforderliche P1-Fachartefakte aktuell oder bewusst als fehlend markiert sind, nötige Revisionen versioniert sind und keine Fachlogik aus Spezialskills dupliziert wurde.
