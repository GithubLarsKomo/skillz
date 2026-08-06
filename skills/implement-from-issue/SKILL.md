---
name: implement-from-issue
description: Implementiert ein klar abgegrenztes Repository-Issue vom verifizierten Ausgangszustand bis zu einem überprüfbaren Commit- oder Pull-Request-Stand mit vollständiger Rückverfolgbarkeit, Testevidenz, Sicherheits- und Migrationsbewertung sowie expliziter externer Nachverifikation. Verwenden, wenn ein umsetzungsreifes Issue sicher und ohne Scope-Ausweitung ausgeführt werden soll.
userFacing: true
implicitInvocation: true
category: engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - test-driven-vertical-slice
  - disciplined-diagnosis
  - agent-handoff
  - deferred-external-action-verification
outputs:
  - implementation-evidence.json
  - reviewable-change-brief.md
  - residual-risk-handoff.json
lastEvaluated: 2026-08-01
---

# Implement From Issue

## Trigger

Diesen Skill verwenden, wenn genau ein klar begrenztes Issue mit überprüfbaren Akzeptanzkriterien in einem bestehenden Repository umgesetzt werden soll.

## Voraussetzungen

Benötigt werden Issue-ID und Wortlaut, Akzeptanzkriterien, Abhängigkeiten und Nicht-Ziele, Repository-, Branch- und Commitzustand, bekannte Invarianten sowie relevante Test-, Migrations-, Sicherheits- und Betriebsgrenzen. Fehlt eine irreversible Produkt- oder Architekturentscheidung, wird die Umsetzung blockiert statt stillschweigend entschieden.

## Ablauf

### 1. Ausgangszustand verifizieren

Lies Issue und Repositoryzustand erneut. Halte Base-Branch, Head-SHA, Arbeitsbaum, bestehende PRs, relevante Dateien und bereits erledigte Arbeit fest. Vermeide doppelte oder parallele Umsetzung.

### 2. Änderungsspanne begrenzen

Leite den kleinsten relevanten Dateisatz, Testseams, Migrationswirkung, Sicherheitsgrenzen, Rollback und explizite Nicht-Ziele ab. Begründe jede vorgesehene Dateiänderung gegen das Issue.

### 3. Testgetrieben implementieren

Nutze `test-driven-vertical-slice`, wenn ein beobachtbarer Red-Green-Refactor-Nachweis möglich ist. Implementiere nur den kleinsten End-to-End-Pfad. Unzulässig sind fachfremde Refactorings, breite Dependency-Upgrades, abgeschwächte Tests, übersprungene Sicherheitsprüfungen oder mehrere unabhängige Verhaltensänderungen.

### 4. Fehler diszipliniert behandeln

Bei unerwarteten Fehlern wechsle zu `disciplined-diagnosis`. Wiederhole Checks nicht blind und behaupte keine Root Cause ohne unterscheidende Evidenz.

### 5. Vollständig verifizieren

Führe Akzeptanzprüfung, fokussierte Tests, relevante Regressionen sowie erforderliche Typ-, Lint-, Build-, Schema-, Migrations- und Sicherheitsprüfungen aus. Verknüpfe Evidenz direkt mit den Akzeptanzkriterien.

### 6. Reviewbaren Zustand erzeugen

Erzeuge einen Commit oder Draft-PR mit Issue-Bezug, engem Diff, dokumentierten Prüfungen, Rollback und Restrisiken. Bewahre den unveränderlichen Head-SHA für nachgelagerte Prüfung.

### 7. Externe Prüfung abgrenzen

Nicht verfügbare CI-, Deployment-, Migrations- oder Dienstprüfungen werden getrennt von lokal abgeschlossener Arbeit markiert und mit `deferred-external-action-verification` beobachtet. Vollständiger Erfolg darf erst nach externer Evidenz behauptet werden.

## Prüfungen

Vor Abschluss müssen Issue-Rückverfolgbarkeit, rationale Dateiauswahl, Akzeptanz- und Regressionsevidenz, Migrations- und Sicherheitswirkung, Rollback, Restrisiken, unveränderlicher Repositoryzustand und genau der nächste Handoff dokumentiert sein.

## Fehlerbehandlung

Stoppe und begrenze neu, wenn der Scope wächst, das ursprüngliche Akzeptanzkriterium nicht direkt belegt wird, Architekturentscheidungen stillschweigend entstehen, Tests geschwächt werden oder externe Erfolge nur angenommen sind.

## Übergabe

```json
{
  "issueId": "...",
  "repository": {"name": "...", "base": "...", "head": "...", "headSha": "..."},
  "acceptanceCriteria": [{"id": "...", "evidence": ["..."]}],
  "changedFiles": [{"path": "...", "rationale": "..."}],
  "verification": {"focused": ["..."], "regression": ["..."], "external": ["..."]},
  "impacts": {"migration": "...", "security": "...", "compatibility": "..."},
  "rollback": "...",
  "residualRisks": ["..."],
  "status": "locally-verified|externally-pending|complete",
  "nextSkill": "two-axis-code-review|agent-handoff|deferred-external-action-verification|disciplined-diagnosis"
}
```

## Abschlusskriterien

Abgeschlossen ist die lokale Umsetzung, wenn das Issue eng und rückverfolgbar implementiert, alle verfügbaren relevanten Prüfungen bestanden, der reviewbare Commit- oder PR-Zustand verifiziert und verbleibende externe Bedingungen ehrlich getrennt übergeben wurden.
