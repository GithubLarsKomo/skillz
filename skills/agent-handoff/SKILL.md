---
name: agent-handoff
description: Erzeugt einen kompakten, verifizierbaren Übergabestand für neue Sitzungen oder Agenten. Verwenden, wenn Ziel, Repositoryzustand, Entscheidungen, Evidenz, Restrisiken, blockierte Punkte und genau die nächste ausführbare Aktion ohne Informationsverlust oder doppelte Arbeit weitergegeben werden müssen.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - iterate-software-projects
outputs:
  - agent-handoff.json
  - agent-handoff.md
lastEvaluated: 2026-07-31
---

# Agent Handoff

## Trigger

Diesen Skill verwenden, wenn eine laufende oder abgeschlossene Arbeit an eine neue Sitzung, einen anderen Agenten oder eine andere Person übergeben werden soll und der Folgeschritt ohne erneute Bestandsaufnahme sicher fortgesetzt werden muss.

## Voraussetzungen

Erfasse vor der Übergabe mindestens:

- bestätigtes Ziel und aktuellen Scope,
- Repository, Branch, Head-Commit und Arbeitsbaumstatus,
- zugehörige Issues, Pull Requests und externe Läufe,
- akzeptierte Entscheidungen und ausdrücklich verworfene Alternativen,
- abgeschlossene Änderungen und bereits ausgeführte Befehle,
- Verifikationsevidenz mit Status und Zeitpunkt,
- offene Risiken, Blocker und unbestätigte Annahmen,
- genau eine nächste ausführbare Aktion.

Zugangsdaten, personenbezogene Inhalte, vollständige Logs und unnötige Repositoryinhalte werden nicht in die Übergabe kopiert.

## Grundsätze

Trenne konsequent:

- **bestätigte Fakten:** direkt durch Repository, Toolausgabe, Test oder freigegebene Entscheidung belegt,
- **Annahmen:** plausible, aber noch nicht verifizierte Aussagen,
- **offene Prüfungen:** externe oder zeitabhängige Zustände ohne Abschlussnachweis,
- **abgeschlossene Arbeit:** bereits erledigte Schritte, die nicht wiederholt werden dürfen,
- **nächste Aktion:** kleinster ausführbarer Schritt, der den Workflow fortsetzt.

Eine Übergabe ist kein Ort für neue Produkt- oder Architekturentscheidungen.

## Ablauf

### 1. Ziel und Grenzen fixieren

Formuliere das bestätigte Ziel in einem Satz. Ergänze In-Scope, Nicht-Ziele und das erwartete Abschlusskriterium. Widersprüchliche oder unbestätigte Ziele werden als offen markiert, nicht stillschweigend aufgelöst.

### 2. Repositoryzustand sichern

Dokumentiere Repository, Branch, unveränderlichen Head-SHA, Basisbranch, Arbeitsbaumstatus sowie relevante Datei- und Pfadangaben. Ist der Head-SHA unbekannt oder veraltet, darf die Übergabe keine schreibende Folgeaktion freigeben.

### 3. Entscheidungen und erledigte Arbeit erfassen

Liste nur Entscheidungen auf, die belegt oder ausdrücklich bestätigt sind. Erfasse anschließend abgeschlossene Schritte, zugehörige Commits, Befehle und Resultate. Kennzeichne Versuche, die fehlgeschlagen oder verworfen wurden, damit sie nicht blind wiederholt werden.

### 4. Evidenz und Freshness bewerten

Jeder Verifikationspunkt enthält Quelle, Ergebnis, Zeitpunkt und Freshness-Status:

- `fresh`: Zustand ist für die nächste Aktion noch belastbar,
- `stale`: Zustand muss vor Verwendung erneut geprüft werden,
- `pending`: asynchrone Prüfung läuft noch,
- `unverified`: kein ausreichender Nachweis vorhanden.

CI, Deployments, Reviews, Mergefähigkeit, Dienststatus und externe Integrationen gelten als volatil. Ihre Übergabe benötigt einen Prüfzeitpunkt, eine Watch-Bedingung und bei schreibenden Aktionen einen erwarteten Head-SHA.

### 5. Risiken und Blocker trennen

Ein **Risiko** erlaubt Fortsetzung mit dokumentierter Vorsicht. Ein **Blocker** verhindert die nächste Aktion bis zu einer klar benannten Auflösung. Annahmen dürfen weder als Risiken noch als Fakten getarnt werden.

### 6. Genau eine nächste Aktion bestimmen

Definiere einen konkreten Befehl, Toolaufruf oder Review-Schritt mit Vorbedingungen und erwarteter Evidenz. Mehrere unabhängige nächste Schritte werden priorisiert; nur der erste wird als ausführbar markiert.

### 7. Übergabe prüfen

Verifiziere vor Abschluss:

- Head-SHA und Branch sind vorhanden,
- Fakten, Annahmen und offene Prüfungen sind getrennt,
- erledigte Arbeit und Nicht-Wiederholen-Hinweise sind enthalten,
- volatile Zustände besitzen Freshness und Prüfregel,
- genau eine nächste Aktion ist ausführbar,
- keine Geheimnisse oder unnötigen Logs enthalten sind.

## Externe oder ausstehende Zustände

Bei laufender CI oder ausstehendem Deployment:

1. lokale Arbeit als abgeschlossen oder unvollständig kennzeichnen,
2. externen Status als `pending` erfassen,
3. unveränderlichen Head-SHA sichern,
4. Watch-Bedingung und Abbruchkriterium dokumentieren,
5. an `deferred-external-action-verification` übergeben,
6. keine Erfolgsaussage vor verifiziertem Abschluss treffen.

## Fehlerbehandlung

Lehne die Übergabe ab und rekonstruiere sie, wenn sie nur eine vage Zusammenfassung enthält, Commit- oder Branchzustand fehlt, Annahmen mit Fakten vermischt werden, bereits erledigte Arbeit erneut beauftragt wird, mehrere konkurrierende nächste Aktionen offenbleiben oder externer Erfolg ohne Evidenz behauptet wird.

Fehlt entscheidende Evidenz, übergib an `disciplined-diagnosis` oder `iterate-software-projects`. Ist ein klar begrenztes Issue als Nächstes umzusetzen, verwende `test-driven-vertical-slice`.

## Übergabeformat

```json
{
  "goal": "...",
  "scope": {"in": ["..."], "out": ["..."], "doneWhen": "..."},
  "repository": {
    "name": "owner/repo",
    "baseBranch": "main",
    "branch": "...",
    "headSha": "...",
    "workingTree": "clean|dirty|unknown"
  },
  "references": {"issues": ["#..."], "pullRequests": ["#..."], "externalRuns": ["..."]},
  "facts": [{"statement": "...", "evidence": "..."}],
  "assumptions": [{"statement": "...", "verification": "..."}],
  "decisions": [{"decision": "...", "evidence": "..."}],
  "completed": [{"action": "...", "commit": "...", "evidence": "..."}],
  "doNotRepeat": ["..."],
  "verification": [{"check": "...", "status": "passed|failed|pending|unverified", "checkedAt": "...", "freshness": "fresh|stale|pending|unverified"}],
  "risks": ["..."],
  "blockers": ["..."],
  "nextAction": {"action": "...", "preconditions": ["..."], "expectedEvidence": "..."},
  "nextSkill": "iterate-software-projects|disciplined-diagnosis|test-driven-vertical-slice|deferred-external-action-verification"
}
```

Der menschlich lesbare Brief fasst Ziel, Repositoryzustand, bestätigte Entscheidungen, erledigte Arbeit, offene Risiken und die nächste Aktion kompakt zusammen, ohne die maschinenlesbaren Details zu ersetzen.

## Abschlusskriterien

Die Übergabe ist abgeschlossen, wenn ein neuer Agent ohne erneute Vollanalyse den verifizierten Zustand versteht, nichts bereits Erledigtes wiederholt, volatile externe Zustände korrekt nachprüft und genau die nächste sichere Aktion ausführen kann.
