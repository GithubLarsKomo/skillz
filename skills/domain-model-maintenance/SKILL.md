---
name: domain-model-maintenance
description: Hält Domänenbegriffe, Invarianten, Zustände, Grenzen und Repräsentationen während Softwareänderungen konsistent und steuert kompatible Migrationen über Code, Persistenz, APIs, Events, Tests und Dokumentation.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - decision-record
  - architecture-deepening-review
  - two-axis-code-review
  - test-driven-vertical-slice
  - agent-handoff
outputs:
  - domain-model-map.json
  - domain-change-plan.md
  - domain-validation.json
lastEvaluated: 2026-08-01
---

# Domain Model Maintenance

## Trigger

Verwenden bei Änderungen an Domänenbegriffen, Entitätsgrenzen, Value Objects, Zustandsmaschinen, Invarianten, Verantwortlichkeiten, Identifikatoren, Persistenzmodellen, API-Verträgen, Events oder Kontextabbildungen.

## Voraussetzungen

Erforderlich sind ein unveränderlicher Ausgangsstand sowie Evidenz aus Code, Tests, Spezifikationen, Schemas, Migrationen, Decision Records und gegebenenfalls Laufzeitbeobachtungen.

## Ablauf

### 1. Aktuelles Modell verifizieren

Erfasse kanonische Konzepte, Aliase, Eigentümer, Grenzen, Invarianten, Zustände, Übergänge, Identifikatoren und Repräsentationen. Trenne Domänenmodell von Transport-, Persistenz-, UI-, Vendor- und Legacy-Begriffen.

### 2. Drift und Inkonsistenzen lokalisieren

Suche nach mehrdeutigen Namen, duplizierten Regeln, ungültigen Übergängen, widersprüchlichen IDs, anämischen Grenzen und Infrastrukturleckage. Ordne jeden Befund einer konkreten Oberfläche und Evidenz zu.

### 3. Änderung klassifizieren

Klassifiziere die Änderung als additiv, kompatible Umbenennung, Verhaltensänderung, Grenzverschiebung, Split, Merge oder Entfernung. Destruktive oder irreversible Änderungen benötigen einen akzeptierten `decision-record` und autorisierte Freigabe.

### 4. Kompatibilität und Migration planen

Bewerte Persistenz, APIs, Events, Integrationen, Tests, Fixtures und Dokumentation. Definiere Reihenfolge, Koexistenz, Adapter, Backfill, Rollback und Entfernungskriterien. Externe Aliase bleiben auf benannte Grenzen beschränkt.

### 5. Vertikal umsetzen und prüfen

Nutze kleine vertikale Änderungen. Belege Invarianten und Übergänge mit Tests und prüfe beide Achsen: fachliche Modelltreue sowie Implementierungs- und Lieferqualität. Grüne CI allein beweist keine semantische Gleichwertigkeit.

### 6. Modellartefakte aktualisieren

Aktualisiere Glossar und maschinenlesbare Domänenkarte mit unveränderlichen Referenzen. Historische Migrationen und akzeptierte Entscheidungen werden nicht überschrieben.

### 7. Übergabe erzeugen

Übergebe betroffene Oberflächen, Migrationsreihenfolge, Validierung, Rollback oder Koexistenz, Restrisiken und genau eine ausführbare nächste Aktion.

## Prüfungen

Prüfe kanonische Begriffe, Aliasgrenzen, Eigentümer, Invarianten, Zustände, Übergänge, Repräsentationen, Persistenz-, API-, Event-, Integrations-, Test-, Fixture- und Dokumentationsauswirkungen.

## Fehlerbehandlung

Stoppe bei layerweisen Einzelumbenennungen, stillen destruktiven Migrationen, duplizierten Invarianten, nicht autorisierten Grenzverschiebungen oder der Annahme, Typprüfung beziehungsweise grüne CI beweise semantische Korrektheit.

## Übergabe

```json
{
  "repository": {"name": "...", "headSha": "..."},
  "changeClass": "additive|compatible-rename|behavioral|boundary-move|split|merge|removal",
  "canonicalConcepts": [{"name": "...", "owner": "...", "boundary": "..."}],
  "aliases": [{"term": "...", "boundary": "...", "removalCriteria": "..."}],
  "invariants": ["..."],
  "states": ["..."],
  "transitions": ["..."],
  "representations": ["domain|persistence|api|event|integration|ui"],
  "affectedSurfaces": ["..."],
  "compatibility": ["..."],
  "migrationOrder": ["..."],
  "validationEvidence": ["..."],
  "rollbackOrCoexistence": "...",
  "residualRisks": ["..."],
  "nextAction": "exactly one executable action"
}
```

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Domänenmodell und Repräsentationen konsistent, Invarianten und Übergänge belegt, Migration und Kompatibilität nachvollziehbar, historische Artefakte geschützt und genau eine nächste Aktion übergeben sind.
