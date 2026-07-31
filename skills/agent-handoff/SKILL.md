---
name: agent-handoff
description: Erzeugt einen kompakten, überprüfbaren Übergabestand für eine neue Sitzung oder einen anderen Agenten mit exaktem Repositoryzustand, bestätigten Entscheidungen, Evidenz, offenen Risiken und genau einem ausführbaren nächsten Schritt. Verwenden, wenn Arbeit ohne Informationsverlust fortgesetzt werden soll.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - iterate-software-projects
  - deferred-external-action-verification
outputs:
  - agent-handoff.json
  - HANDOFF.md
lastEvaluated: 2026-07-31
---

# Agent Handoff

## Trigger

Diesen Skill verwenden, wenn eine laufende Arbeit an eine neue Sitzung, einen anderen Agenten oder einen späteren Fortsetzungspunkt übergeben werden soll.

## Voraussetzungen

Erfasse mindestens Ziel, Repository, Branch, aktuellen Commit, relevante PRs und Issues, bestätigte Entscheidungen, abgeschlossene Arbeit, ausgeführte Prüfungen, offene Risiken, Blocker und den nächsten ausführbaren Schritt.

Trenne strikt zwischen bestätigten Fakten, Annahmen und unbestätigten externen Zuständen. Secrets, personenbezogene Inhalte und vollständige Logs gehören nicht in die Übergabe.

## Ablauf

### 1. Zustand verankern

Dokumentiere Repository, Branch, Commit-SHA, Arbeitsbaum, PR- und Issue-Referenzen sowie relevante Dateipfade und Befehle.

### 2. Erledigtes und Nicht-Wiederholbares festhalten

Liste abgeschlossene Änderungen, bereits geprüfte Hypothesen, verworfene Ansätze und Schritte auf, die nicht erneut ausgeführt werden sollen.

### 3. Evidenz klassifizieren

Markiere jede Aussage als `verified`, `assumed` oder `unverified`. Verknüpfe Verifikation mit konkreten Befehlen, CI-Läufen, Commit-SHAs oder Review-Ergebnissen.

### 4. Flüchtige Zustände kennzeichnen

CI, Deployments, Reviews, Servicezustände und externe Freigaben erhalten Zeitpunkt, Head-SHA, Prüfbedingung und Frischegrenze. Ein laufender externer Vorgang wird an `deferred-external-action-verification` übergeben und nicht als erfolgreich behauptet.

### 5. Nächsten Schritt begrenzen

Formuliere genau eine ausführbare nächste Aktion mit Startbedingung, erwarteter Evidenz und Abbruchbedingung. Neue Produkt- oder Architekturentscheidungen werden nicht während der Übergabe erfunden.

## Prüfungen

Vor Abschluss müssen Repository, Branch, Commit, Entscheidungen, Evidenz, offene Risiken, externe Zustände und nächster Schritt explizit vorhanden sein. Vage Formulierungen wie „weitermachen“ oder „CI prüfen“ ohne Referenz und Bedingung sind unzulässig.

## Fehlerbehandlung

Fehlen verifizierbare Zustandsdaten, kennzeichne sie als unbestätigt und nenne den exakten Beschaffungsbefehl. Enthält die Vorlage widersprüchliche SHAs oder doppelte Arbeit, stoppe und rekonstruiere den aktuellen Zustand vor der Übergabe.

## Übergabe

```json
{
  "goal": "...",
  "repository": "owner/repo",
  "branch": "...",
  "headSha": "...",
  "pullRequests": ["..."],
  "issues": ["..."],
  "decisions": [{"statement": "...", "status": "verified|assumed"}],
  "completed": ["..."],
  "verification": [{"commandOrRun": "...", "status": "verified|unverified", "checkedAt": "..."}],
  "doNotRepeat": ["..."],
  "risks": ["..."],
  "externalState": [{"subject": "...", "status": "pending|verified|failed", "headSha": "...", "freshUntil": "...", "watchCondition": "..."}],
  "nextAction": {"action": "...", "startCondition": "...", "expectedEvidence": "...", "stopCondition": "..."}
}
```

## Abschlusskriterien

Die Übergabe ist abgeschlossen, wenn ein neuer Agent ohne erneute Grundanalyse den bestätigten Zustand nachvollziehen, bereits erledigte Arbeit vermeiden und genau den dokumentierten nächsten Schritt sicher ausführen kann.
