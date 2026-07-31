---
name: test-driven-vertical-slice
description: Implementiert ein klar abgegrenztes vertikales Issue durch einen reproduzierbaren Red-Green-Refactor-Zyklus mit beobachtbarer Abnahmeevidenz, enger Änderungsspanne und erhaltenen Sicherheits-, Migrations- und Domänengrenzen. Verwenden, wenn ein Issue aus spec-to-vertical-issues testgetrieben über alle erforderlichen Schichten umgesetzt werden soll.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - spec-to-vertical-issues
  - disciplined-diagnosis
outputs:
  - vertical-slice-evidence.json
  - acceptance-proof.md
  - residual-risk-handoff.json
lastEvaluated: 2026-07-31
---

# Test-Driven Vertical Slice

## Trigger

Diesen Skill verwenden, wenn genau ein begrenztes vertikales Issue mit unabhängig beobachtbarem Nutzen durch Red-Green-Refactor umgesetzt werden soll.

## Voraussetzungen

Benötigt werden:

- ein freigegebenes vertikales Issue mit Requirement-IDs und Abnahmekriterien,
- Repository- und Branchzustand,
- bekannte Domänen-, Sicherheits-, Migrations- und Kompatibilitätsgrenzen,
- vorhandene Testseams und relevante Prüfkommandos,
- explizite Nicht-Ziele und Abhängigkeiten.

Fehlt eine irreversible Architekturentscheidung, darf sie nicht stillschweigend getroffen werden.

## Ablauf

### 1. Slice eingrenzen

Formuliere ein einziges beobachtbares Verhalten. Ordne Requirement-IDs, Abnahmekriterien, betroffene Schichten, Nicht-Ziele und notwendige Querschnittsaufgaben zu. Lehne horizontale Infrastrukturpakete ohne eigenständigen Nutzen ab.

### 2. Red belegen

Erzeuge zuerst einen ausführbaren, abnahmeorientierten Test oder gleichwertigen Check, der wegen des fehlenden Verhaltens fehlschlägt. Dokumentiere Befehl, erwarteten Fehler und tatsächliche Ausgabe.

Kann eine externe Grenze nicht in CI ausgeführt werden, verwende eine stabile Schnittstelle und einen deterministischen lokalen Fake oder Contract-Fixture. Bewahre mindestens eine beobachtbare End-to-End-Abnahmeseam und kennzeichne verbleibende externe Verifikation.

### 3. Green minimal erreichen

Implementiere nur den kleinsten End-to-End-Pfad, der den Red-Nachweis grün macht. Ändere nur notwendige Schichten. Bewahre Invarianten, Sicherheitsprüfungen, Migrationen und Kompatibilität.

Nicht zulässig sind:

- abgeschwächte Assertions,
- gelöschte oder übersprungene Tests,
- mehrere unabhängige Verhaltensänderungen,
- breite Dependency-Upgrades,
- spekulative Abstraktionen,
- fachfremde Refactorings.

### 4. Refactor begrenzen

Refaktoriere erst nach Green und ausschließlich verhaltensbewahrend. Halte den Umfang klein, führe nach jedem Schritt die fokussierten Tests aus und stoppe bei wachsendem Scope.

### 5. Verifizieren

Führe aus:

- den ursprünglichen Red-Test,
- fokussierte Komponenten- und Contract-Tests,
- relevante Regressionstests,
- erforderliche Migrations-, Typ-, Lint-, Sicherheits- oder Build-Prüfungen.

Abnahmeevidenz muss das ursprüngliche Kriterium direkt belegen; reine Mock-Interaktionen genügen nicht.

## Prüfungen

Vor Abschluss müssen separat dokumentiert sein:

- Red-Evidenz vor Produktionsänderung,
- Green-Evidenz nach kleinstem End-to-End-Fix,
- Refactor-Umfang und Verhaltenserhalt,
- Rückverfolgbarkeit zu Requirement-IDs,
- relevante Regressionen,
- Restunsicherheit, Rollback und externe Nachprüfung.

## Fehlerbehandlung

Wenn Red nicht reproduzierbar ist, wechsle zu `disciplined-diagnosis`. Wenn das Issue nicht vertikal oder zu groß ist, übergib es an `spec-to-vertical-issues`. Externe asynchrone Prüfungen werden mit `deferred-external-action-verification` fortgesetzt.

## Übergabe

Erzeuge mindestens:

```json
{
  "issueId": "...",
  "requirementIds": ["..."],
  "red": {"command": "...", "failure": "..."},
  "green": {"changeScope": ["..."], "evidence": "..."},
  "refactor": {"scope": ["..."], "behaviorPreserved": true},
  "verification": {"focused": ["..."], "regression": ["..."]},
  "externalVerification": ["..."],
  "residualRisks": ["..."],
  "rollback": "...",
  "nextSkill": "implement-from-issue|iterate-software-projects|disciplined-diagnosis"
}
```

## Abschlusskriterien

Der Slice ist abgeschlossen, wenn ein abnahmeorientierter Check nachweislich vor der Implementierung fehlschlug und danach besteht, nur notwendige End-to-End-Änderungen enthalten sind, Refactoring verhaltensbewahrend blieb und relevante Regressionen, Restrisiken sowie Rückverfolgbarkeit dokumentiert sind.
