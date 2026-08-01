---
name: decision-record
description: Erfasst wesentliche technische und fachliche Entscheidungen als unveränderliche, nachvollziehbare Records mit Kontext, Alternativen, Evidenz, Autorität, Folgen, Risiken und Ablösungspfad.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - large-work-wayfinder
  - throwaway-prototype
  - two-axis-code-review
  - agent-handoff
outputs:
  - decision-record.md
  - decision-record.json
lastEvaluated: 2026-08-01
---

# Decision Record

## Trigger

Verwenden bei irreversiblen, querschnittlichen oder sicherheits-, migrations-, architektur-, produkt-, compliance- oder betriebsrelevanten Entscheidungen.

## Voraussetzungen

Benötigt werden eine präzise Entscheidungsfrage, ein unveränderlicher Repository- oder Artefaktstand, Fakten, Annahmen, Constraints, Alternativen, Kriterien, Evidenz, Entscheidungsverantwortung und genehmigungsberechtigte Person.

## Ablauf

### 1. Entscheidungsrahmen fixieren

Dokumentiere Frage, Scope, Fakten, Annahmen, Hypothesen, Constraints, Präferenzen und Autorisierungsgrenzen getrennt.

### 2. Alternativen bewerten

Erfasse alle realistischen Optionen einschließlich Nichtstun. Bewerte sie anhand vorab benannter Kriterien und belastbarer Evidenz.

### 3. Autorität prüfen

Akzeptierte Entscheidungen benötigen einen benannten Entscheider und einen autorisierten Genehmiger. Fehlt Autorität oder Evidenz, bleibt der Status `proposed` und irreversible Umsetzung ist blockiert.

### 4. Entscheidung dokumentieren

Halte gewählte Option, Begründung, Folgen, Risiken, Rollback- oder Exit-Pfad, Nachfolgepflichten und Links zu Issues, PRs, Spezifikationen, Migrationen, Reviews und Prototypen fest.

### 5. Historie schützen

Bestehende akzeptierte Records werden nie überschrieben. Änderungen erzeugen einen neuen Record, der den früheren mit `supersedes` referenziert; der alte Record wird als `superseded` markiert.

### 6. Übergabe erzeugen

Erzeuge menschenlesbaren ADR-Text und maschinenlesbares JSON mit genau einer ausführbaren nächsten Aktion.

## Prüfungen

Prüfe Trennung von Fakten und Annahmen, Vollständigkeit der Alternativen, Evidenzbezug, Autorität, unveränderliche Referenzen, Folgen, Risiken, Rollback und Supersession.

## Fehlerbehandlung

Stoppe bei stiller Architekturwahl, nachträglicher Rationalisierung, fehlenden Alternativen, ungeklärter Autorität, Überschreiben historischer Records oder Nutzung grüner CI als Entscheidungsbefugnis.

## Übergabe

```json
{
  "id": "ADR-...",
  "state": "proposed|accepted|rejected|superseded|deprecated",
  "question": "...",
  "repository": {"name": "...", "headSha": "..."},
  "facts": ["..."],
  "assumptions": ["..."],
  "constraints": ["..."],
  "alternatives": [{"name": "...", "evidence": ["..."], "tradeoffs": ["..."]}],
  "criteria": ["..."],
  "decision": "...",
  "authority": {"owner": "...", "approver": "..."},
  "consequences": ["..."],
  "risks": ["..."],
  "rollback": "...",
  "links": ["..."],
  "supersedes": null,
  "nextAction": "exactly one executable action"
}
```

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Status, Autorität, Evidenz, Alternativen, Entscheidung, Folgen, Risiken, Rollback, unveränderliche Referenzen und genau eine nächste Aktion dokumentiert sind.
