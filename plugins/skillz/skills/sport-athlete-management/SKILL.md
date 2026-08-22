---
name: sport-athlete-management
description: Orchestriert den geschlossenen Sport-Trainingsregelkreis von Athletenprofil und Zielmodell über Saison-, Meso- und Mikroplanung zu Daily Monitoring, Session-Completion und auditierbarer Adaptation. Verwenden für longitudinale Trainingssteuerung über mehrere Ebenen; Fachlogik der Spezialskills nicht duplizieren.
---

# Sport Athlete Management

Koordiniere die Sport-Skills als persistenten Regelkreis. Strukturierte Artefakte sind die fachliche Wahrheit; Reports und Web-UIs sind abgeleitete Ansichten.

## Trigger

Nutze diesen Orchestrator, wenn nicht nur ein einmaliger Trainingsplan, sondern fortlaufende Zielsetzung, Planung, tägliche Rückmeldung und Anpassung verlangt werden.

Für reine Testauswertung weiterhin `sport-performance-diagnostics`; für einen einmaligen Plan kann `sport-training-programming` direkt verwendet werden.

## Voraussetzungen

Mindestens Athletenidentität und Ziel müssen bekannt sein. Für laufende Steuerung werden die jeweils aktuellen Versionen von Profil, Performance-Modell, Saison/Meso/Mikro, Monitoring und Adaptationsentscheidungen referenziert.

## Ablauf

1. **State laden.** Aktuelle IDs und Versionen der kanonischen Sport-Artefakte bestimmen.
2. **Fehlende Ebene routen.** Profil → Zielmodell → Saison → Meso → Mikro nur dort erzeugen, wo Zustand fehlt oder abgelaufen ist.
3. **Heute bestimmen.** Geplante Session und jüngsten Morning Check zusammenführen.
4. **Safety Routing sichern.** Health Flags dürfen von Planungszielen nicht überschrieben werden.
5. **Training protokollieren.** Completed Session und sRPE über `sport-daily-athlete-monitoring` erfassen.
6. **Adaptation ausführen.** `sport-training-adaptation-engine` nur bei relevantem Checkpoint oder Mismatch aufrufen; nicht jede kleine Schwankung zum Rewrite machen.
7. **Versioniert revidieren.** Betroffene Mikro-/Meso-/Saisonobjekte über ihre Eigentümer-Skills neu erzeugen; alte Version behalten.
8. **State fortschreiben.** Nächste Entscheidung, offene Unsicherheiten, Safety Flags und nächste Re-Evaluation zusammenfassen.

## Systemgrenzen

Die WebApp und relationale Datenbank leben in einem separaten Produkt-Repository. `skillz` besitzt Fachlogik und JSON-Verträge, aber keine produktive Web-/DB-Implementierung. Die Produkt-App darf diese Verträge konsumieren und persistieren.

## Alters- und Geschlechtsregeln

Alle nachgelagerten Entscheidungen verwenden Alter und Geschlecht als Kontextmodifier. Individuelle Trainingsreaktion bleibt primär; keine pauschale Masters-Abwertung und keine starre Zyklusperiodisierung.

## Prüfungen

- Ist jede Ebene über IDs/Versionen statt impliziten Chat-Kontext verbunden?
- Besitzt jede Fachentscheidung genau einen verantwortlichen Skill?
- Sind Reports/UI nicht Source of Truth?
- Bleiben Audit Trail und Vorversionen erhalten?
- Können fehlende Daten ohne erfundene Werte weitergereicht werden?

## Fehlerbehandlung

- **Unvollständiger State:** nur fehlende Ebene erzeugen und Abhängigkeiten erhalten.
- **Widersprüchliche Versionen:** keine stille Überschreibung; Konflikt als Reconciliation-Bedarf markieren.
- **Safety Red Flag:** Performance-Orchestrierung unterbrechen und Health/Medical Routing priorisieren.
- **Produkt-App nicht verfügbar:** Fachartefakte bleiben als JSON unabhängig nutzbar.

## Übergabe

Kanonische Vertragsdefinition ist `schemas/sport-athlete-management-v1.schema.json`. Das separate WebApp-Repository konsumiert diese Verträge über versionierte API-/Persistenzmodelle; Report-Workflows können dieselben Artefakte lesen.

## Abschlusskriterien

Der Orchestrator ist abgeschlossen, wenn der aktuelle Athlete-Management-State konsistent ist, die nächste Trainingsentscheidung eindeutig referenziert wird, nötige Revisionen versioniert sind und keine Fachlogik aus Spezialskills dupliziert wurde.
