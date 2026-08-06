---
name: project-status-brief
description: Verdichtet bereits erhobene Repository- und Projekt-Evidenz zu einem zeitpunktbezogenen Statusbrief mit Fortschritt, Blockern, Risiken, Entscheidungen und nächsten ausführbaren Schritten. Verwenden, wenn Projektzustand belastbar an Reviews, Meetings oder weitere Skills übergeben werden soll, ohne GitHub-, GitLab-, Jira-, CI- oder Deployment-Logik zu duplizieren.
userFacing: true
implicitInvocation: true
category: productivity
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
outputs:
  - project-status.json
  - project-status.md
lastEvaluated: 2026-08-02
---

# Project Status Brief

## Zweck und Grenze

Erzeuge aus bereits geladenen Projekt- und Repository-Fakten einen kompakten, entscheidungsorientierten Statusbrief. Der Skill synthetisiert Zustand; er ist **kein Repository-, Issue-, PR-, CI-, Deployment- oder Projektmanagement-Connector** und führt keine externen Mutationen aus.

Provider-spezifische Tools liefern Commits, PRs, Issues, Checks, Releases, Deployments, Roadmap- oder Task-Daten. Dieser Skill beginnt bei diesen bestätigten Inputs und endet bei `project-status.json` plus einer lesbaren Markdown-Sicht.

## Trigger

Verwenden, wenn:
- ein Projektstand für Daily/Weekly Review oder Meeting-Prep benötigt wird,
- mehrere technische Statussignale zu einem belastbaren Gesamtbild verdichtet werden sollen,
- Blocker, Risiken und nächste ausführbare Aktionen explizit sichtbar sein müssen,
- ein Status ohne provider-spezifische Kopplung weitergereicht werden soll.

## Voraussetzungen

Vor der Synthese fixieren:
1. Projekt-/Repository-Identität,
2. `asOf`-Zeitpunkt,
3. verfügbare Quellen und deren Standzeitpunkte,
4. bestätigte Milestone-/Roadmap-Informationen soweit vorhanden,
5. beobachtete PR-, Issue-, CI-, Release- und Deployment-Zustände,
6. bekannte Entscheidungen, Blocker und Datenlücken.

Fehlende Daten bedeuten `unknown`, niemals automatisch `healthy`, `done` oder `no blockers`.

## Kernregeln

### Beobachtung und Interpretation trennen

Jede wesentliche Aussage wird als `observed` oder `inferred` geführt. Ein grüner CI-Lauf ist eine Beobachtung; daraus abgeleitete Merge-Reife ist eine Interpretation und muss ihre Voraussetzungen nennen.

### Provenance und Aktualität erhalten

Statusfakten behalten Quelle, Referenz, beobachteten Zeitpunkt und soweit verfügbar Confidence. Veraltete Evidenz wird als `stale` markiert. Widersprüche zwischen Quellen werden nicht still aufgelöst, sondern unter `contradictions` dokumentiert.

### Externe Aktionen niemals erfinden

`merged`, `deployed`, `closed`, `released`, `rerun`, `approved` oder vergleichbare Zustände dürfen nur als ausgeführt erscheinen, wenn eine externe Quelle genau diesen Zustand bestätigt. Geplante Aktionen bleiben `pending`.

### Health nicht aus Einzelindikatoren ableiten

Ein grüner CI-Lauf allein bedeutet nicht, dass ein Projekt gesund oder releasebereit ist. Fehlende Produkt-, Review-, Security-, Migrations- oder Deployment-Evidenz bleibt sichtbar.

## Ablauf

1. **Scope fixieren** – Projekt, Branch/Release-Kontext und `asOf` festhalten.
2. **Quellen inventarisieren** – verfügbare Evidenz samt Aktualität und Lücken erfassen.
3. **Beobachtungen normalisieren** – Milestone, Änderungen, PRs, Issues, CI, Deployments und Entscheidungen als bestätigte Fakten erfassen.
4. **Widersprüche markieren** – konkurrierende Statussignale nebeneinander erhalten.
5. **Blocker und Risiken ableiten** – nur aus belegbaren Fakten; Interpretation kennzeichnen.
6. **Health bewerten** – `on-track`, `at-risk`, `blocked` oder `unknown`, jeweils mit Begründung und Confidence.
7. **Nächste Aktionen bestimmen** – wenige konkrete, ausführbare Schritte mit Preconditions; externe Ausführung nicht behaupten.
8. **Artefakte erzeugen** – strukturierte JSON-Sicht plus kompaktes Markdown.

## Output-Vertrag

### `project-status.json`

```json
{
  "schemaVersion": 1,
  "project": {"id": "...", "name": "...", "ref": "..."},
  "asOf": "ISO-8601",
  "health": {"state": "on-track|at-risk|blocked|unknown", "confidence": "high|medium|low", "rationale": []},
  "milestone": {"name": "...", "state": "confirmed|unknown", "evidence": []},
  "observations": [],
  "recentChanges": [],
  "pullRequests": [],
  "issues": [],
  "ci": [],
  "deployments": [],
  "decisions": [],
  "blockers": [],
  "risks": [],
  "contradictions": [],
  "dataGaps": [],
  "nextActions": [],
  "sources": []
}
```

Jede relevante Beobachtung referenziert ihre Quelle. `nextActions` enthalten mindestens `action`, `reason`, `preconditions` und `executionState`, wobei ohne externe Bestätigung `executionState` nicht `done` sein darf.

### `project-status.md`

Kurze menschlich lesbare Sicht:
1. Stand und Health,
2. seit dem letzten relevanten Stand geändert,
3. Blocker/Risiken,
4. offene Entscheidungen/Widersprüche,
5. nächste ausführbare Aktionen,
6. Datenlücken und Aktualität.

## Downstream-Verwendung

`daily-and-weekly-review` kann `project-status.json` als bestätigten Projektstatus-Input verwenden. `meeting-preparation` kann denselben Vertrag als Projektkontext nutzen, ohne Repository-Retrieval zu übernehmen. Downstream-Skills müssen `unknown`, `stale`, `pending` und Widersprüche erhalten.

## Datenschutz und Persistenz

Persistiere nur den für Status und Nachvollziehbarkeit nötigen Inhalt. Keine Secrets, Tokens, vollständigen privaten Diskussionen oder unnötigen personenbezogenen Inhalte in Statusartefakte kopieren. Sensible Quellinhalte bevorzugt referenzieren statt duplizieren.

## Qualitätsgate

Der Skill ist nur bestanden, wenn:
- beobachtete Fakten und Interpretationen getrennt sind,
- Quellen/Aktualität nachvollziehbar bleiben,
- fehlende Evidenz nicht in positive Zustände umgedeutet wird,
- Widersprüche sichtbar bleiben,
- keine externe Aktion erfunden wird,
- nächste Aktionen konkret und ausführbar sind,
- beide Output-Artefakte semantisch übereinstimmen.
