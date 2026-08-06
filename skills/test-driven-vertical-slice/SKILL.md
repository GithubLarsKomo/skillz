---
name: test-driven-vertical-slice
description: Implementiert ein kleines, unabhängig beobachtbares End-to-End-Verhalten durch einen disziplinierten Red-Green-Refactor-Zyklus. Verwenden, wenn ein klar begrenztes vertikales Issue mit Akzeptanzkriterien über die notwendigen Schichten hinweg umgesetzt werden soll, ohne horizontale Infrastrukturpakete, spekulative Abstraktionen oder rein mock-basierte Scheinerfolge.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - spec-to-vertical-issues
  - disciplined-diagnosis
outputs:
  - vertical-slice-evidence.json
  - verification-report.md
  - vertical-slice-residual-risk-handoff.json
lastEvaluated: 2026-07-31
implicitInvocation: true
---

# Test-Driven Vertical Slice

## Trigger

Diesen Skill verwenden, wenn ein kleines vertikales Issue mit eindeutigen Akzeptanzkriterien als durchgängiges, unabhängig demonstrierbares Verhalten implementiert werden soll.

## Voraussetzungen

Erfasse vor Änderungen:

- Issue, Zielnutzer und beobachtbaren Wert,
- Akzeptanzkriterien und Nicht-Ziele,
- betroffene Schichten und bestehende Testnähte,
- Sicherheits-, Daten-, Migrations- und Kompatibilitätsinvarianten,
- ausführbare lokale und CI-Prüfungen,
- externe Grenzen, die in CI nicht verfügbar sind.

Ist das Issue nicht klein, unabhängig abnehmbar oder ausreichend präzise, übergib es zunächst an `spec-to-vertical-issues`.

## Leitprinzip

Implementiere den kleinsten End-to-End-Pfad, der genau ein Akzeptanzkriterium sichtbar erfüllt. Arbeite in der Reihenfolge **Red → Green → Refactor**. Vermische die Nachweise nicht.

Mock-Interaktionen allein gelten nicht als beobachtbarer Wert. Mindestens eine Akzeptanznaht muss Ergebnis, Zustand, Ausgabe oder öffentliches Verhalten prüfen.

## Ablauf

### 1. Slice begrenzen

Formuliere Nutzer- oder Systemauslöser, beobachtbares Ergebnis, notwendige Schichten, explizite Nicht-Ziele, Rollback und Restrisiko. Teile mehrere unabhängige Verhaltensweisen in getrennte Slices.

### 2. Red erzeugen

Erstelle vor Produktionscode eine ausführbare, akzeptanzorientierte Prüfung, soweit technisch möglich. Sie muss auf ein konkretes Akzeptanzkriterium rückverfolgbar sein, aus dem erwarteten fachlichen Verhalten scheitern, einen reproduzierbaren Befehl besitzen und mehr als interne Mock-Aufrufe prüfen. Dokumentiere Befehl, erwartetes Scheitern und tatsächliche Fehlerevidenz. Ist ein Vorher-Nachher-Test technisch unmöglich, begründe den Ersatznachweis ausdrücklich.

### 3. Green herstellen

Implementiere nur den kleinsten Pfad durch die erforderlichen Schichten. Bewahre bestehende Invarianten und vermeide breite Framework- oder Architekturumbauten, allgemeine Infrastruktur vor dem ersten Wert, fachfremde Bereinigung, Dependency-Upgrades ohne zwingenden Bezug sowie deaktivierte oder abgeschwächte Prüfungen. Führe die Red-Prüfung erneut aus und dokumentiere den erfolgreichen Nachweis.

### 4. Externe Grenze stabilisieren

Kann ein externer Dienst nicht in CI laufen, definiere einen stabilen Vertrag, verwende einen deterministischen lokalen Fake oder eine Contract-Fixture, erhalte mindestens eine beobachtbare End-to-End-Akzeptanznaht, markiere reale externe Verifikation als offen und übergib asynchrone Prüfung an `deferred-external-action-verification`. Der Fake darf das erwartete Ergebnis nicht unabhängig vom Produktionspfad vorwegnehmen.

### 5. Refactor nach Green

Refactoriere erst nach belegtem Green und ausschließlich verhaltensbewahrend. Erlaubt sind kleine Benennungs-, Duplikations- oder Strukturverbesserungen im berührten Pfad. Führe danach dieselbe Akzeptanzprüfung und die relevanten Regressionstests erneut aus. Neue Abstraktionen benötigen einen aktuellen, belegten Wiederverwendungsfall.

### 6. Vollständig verifizieren

Prüfe mindestens ursprüngliche Akzeptanzprüfung, relevante Unit-, Integrations- und Contract-Tests, Schema-, Migrations-, Sicherheits- und Kompatibilitätsprüfungen sowie Repository-Validierung und CI. Bei Fehlern wechsle zu `disciplined-diagnosis`, statt den Slice spekulativ zu verbreitern.

## Prüfungen

Vor Abschluss müssen getrennt belegt sein:

- `red`: Test oder Ersatznachweis scheitert vor Implementierung,
- `green`: derselbe Nachweis besteht nach kleinstem Produktionspfad,
- `refactor`: Umfang ist verhaltensbewahrend und erneut geprüft,
- beobachtbarer unabhängiger Wert,
- erhaltene Invarianten,
- externe Restverifikation,
- Rollback und Restrisiken.

## Fehlerbehandlung

Lehne den Ansatz ab und begrenze neu, wenn zuerst ein breites Framework-Refactoring geplant wird, mehrere unabhängige Verhaltensweisen gekoppelt werden, ausschließlich Mock-Interaktionen geprüft werden, Green ohne ursprüngliches Akzeptanzkriterium behauptet wird oder Tests beziehungsweise Sicherheitskontrollen für Green deaktiviert werden.

## Übergabe

```json
{
  "issue": "...",
  "acceptanceCriterion": "...",
  "slice": {"trigger": "...", "observableOutcome": "...", "layers": ["..."], "nonGoals": ["..."]},
  "red": {"command": "...", "status": "failed-as-expected|replacement-evidence", "evidence": ["..."]},
  "green": {"implementationScope": ["..."], "command": "...", "status": "passed", "evidence": ["..."]},
  "refactor": {"scope": ["..."], "behaviorPreserving": true, "verification": ["..."]},
  "externalVerification": {"status": "complete|deferred|not-required", "items": ["..."]},
  "residualRisks": ["..."],
  "rollback": "...",
  "nextSkill": "iterate-software-projects|disciplined-diagnosis|deferred-external-action-verification|implement-from-issue"
}
```

## Abschlusskriterien

Abgeschlossen ist der Slice, wenn genau ein begrenztes Verhalten unabhängig beobachtbar ist, Red-, Green- und Refactor-Evidenz reproduzierbar getrennt vorliegt, relevante Invarianten und Regressionen bestehen und externe Restprüfungen sowie Risiken ausdrücklich übergeben sind.
