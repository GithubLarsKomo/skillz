---
name: project-beta-readiness
description: Bewertet genau ein Softwareprojekt evidenzbasiert auf den Weg zur ersten nutzbaren Beta, quantifiziert den Reifegrad, benennt Beta-Blocker und erzeugt bei erreichter Beta einen Betriebsleitfaden beziehungsweise bei ungeklärter Bedienbarkeit eine gezielte UI-Prototyp-Empfehlung. Verwenden, wenn ein einzelnes Repository anhand von Commits, PRs, Issues, CI/Actions, Tests, Roadmap und ausführbaren Nutzerpfaden auf Beta-Reife geprüft werden soll; für Portfolios den Skill pro Projekt wiederholt ausführen und Ergebnisse erst danach aggregieren.
---

# Project Beta Readiness

## Zweck und Grenze

Bewerte genau **ein** Softwareprojekt gegen eine explizite erste-Beta-Definition. Der Skill ist ein Release-/Readiness-Gate, kein allgemeiner Code-Review-, Architektur- oder Implementierungsworkflow.

Mehrere Repositories werden niemals gemeinsam in einer einzelnen Ausführung bewertet. Für eine Portfolioanalyse wird der Skill nacheinander auf jedes Projekt angewendet; ein nachgelagerter Orchestrator darf ausschließlich die standardisierten Ergebnisse aggregieren.

## Voraussetzungen

Ermittle vor der Bewertung:

- Repository und Default-Branch,
- beabsichtigten ersten Beta-Nutzer und wichtigsten End-to-End-Nutzerpfad,
- aktuellen Commit-Stand,
- aktuelle und kürzlich gemergte PRs,
- offene Issues und bekannte Blocker,
- relevante CI-/Actions-Läufe,
- Tests, Build- und Deploymenthinweise,
- Roadmap, TASKS, SPEC, README oder Release-Gates.

Wenn der Beta-Zweck nicht explizit dokumentiert ist, leite nur den kleinsten plausiblen Beta-Scope aus Repository-Evidenz ab und kennzeichne die Annahme. Erfinde keine Produktanforderungen.

## Beta-Gate

Bewerte sechs Dimensionen mit zusammen 100 Punkten:

1. **Kernnutzen und Scope – 20**: Der primäre Beta-Nutzer kann den vorgesehenen Kernnutzen verstehen und ausführen.
2. **Vertikaler End-to-End-Pfad – 20**: Mindestens ein realer Nutzerpfad läuft von Eingabe bis Ergebnis ohne manuelle Entwickler-Eingriffe außerhalb dokumentierter Beta-Schritte.
3. **Daten, Fehlerfälle und Wiederaufnahme – 15**: Persistenz, Validierung, wesentliche Fehlerfälle und erforderliche Recovery sind für den Beta-Scope beherrscht.
4. **Verifikation – 20**: Relevante Tests, Build, CI/Actions und aktuelle PR-Nachweise unterstützen den bewerteten Stand.
5. **Bedienbarkeit und Deployment – 15**: Ein Beta-Nutzer kann das System installieren/öffnen, bedienen und den Kernpfad ohne Quellcodekenntnis durchlaufen.
6. **Beta-Betrieb und Anleitung – 10**: Setup, Grenzen, bekannte Risiken, Daten-/Secret-Anforderungen und Rücksetz-/Fehlerhinweise sind dokumentierbar.

Vergib Punkte nur für nachweisbare Fähigkeiten. Ein älterer grüner Test kompensiert keinen neueren roten Lauf. Dokumentation darf nicht höher gewichtet werden als der tatsächlich gemergte und verifizierte Stand.

### Prozentwert

`readinessPercent = erreichte Punkte / 100 * 100`.

Der Wert ist eine Readiness-Messung, keine Schätzung des gesamten späteren Produktumfangs. Features außerhalb des ersten Beta-Scope senken den Wert nicht.

## Harte Beta-Blocker

Unabhängig vom Punktwert ist der Zustand **noch nicht Beta**, wenn mindestens einer dieser Punkte für den Beta-Scope zutrifft:

- der primäre End-to-End-Pfad ist nicht ausführbar,
- der aktuelle relevante CI-/Build-Stand ist rot oder unbekannt und ohne Ersatznachweis,
- Datenverlust oder irreversibler Zustand ist in einem erwartbaren Kernpfad möglich,
- notwendige Secrets/Zugänge werden unsicher behandelt,
- Installation/Start erfordert nicht dokumentiertes Expertenwissen,
- ein ausdrücklich definiertes Release-Gate ist noch offen und für die erste Beta als zwingend markiert.

## Ablauf

### 1. Aktualität bestimmen

Erzeuge einen Evidenz-Zeitstrahl aus Commit, PR, Issue und Action/CI. Nutze den jüngsten sachlich relevanten Zustand statt Repository-Erstellungsdatum oder bloßer Dateimodifikation.

Kennzeichne veraltete Roadmap-Einträge, wenn neuere gemergte Änderungen deren Status überholen.

### 2. Beta-Scope fixieren

Formuliere in einem Satz:

> Die erste Beta ist erreicht, wenn **Nutzer X** den Pfad **A → B → C** mit dokumentiertem Setup und ohne kritischen Beta-Blocker ausführen kann.

### 3. Evidenz gegen das Gate mappen

Für jede der sechs Dimensionen dokumentiere:

- Punkte,
- positive Evidenz,
- fehlende Evidenz,
- Unsicherheit,
- den kleinsten Schritt, der den Score sinnvoll erhöht.

### 4. Blocker prüfen

Trenne strikt:

- **Beta-Blocker** – verhindern die erste Beta,
- **Beta-Follow-ups** – dürfen nach Beta erfolgen,
- **spätere Produkt-Roadmap** – gehört nicht in den Readiness-Prozentwert.

### 5. Beta-Status entscheiden

- **Beta erreicht:** 100 Punkte im definierten Beta-Scope und kein harter Blocker. Erzeuge `beta-runbook.md`.
- **Noch nicht Beta:** unter 100 Punkten oder harter Blocker. Erzeuge eine priorisierte Lücke mit maximal drei nächsten vertikalen Schritten.

Verwende 100 % bewusst als Gate-Zustand. Ein Projekt kann nach der ersten Beta weiter viele offene Features besitzen.

### 6. UI-Prototypbedarf entscheiden

Ein UI-Prototyp ist sinnvoll, wenn mindestens eine für den Beta-Pfad relevante Unsicherheit primär durch Interaktion statt Backend-Implementierung entschieden werden muss, zum Beispiel:

- Informationsarchitektur oder Navigationsfluss ist ungeklärt,
- mehrere konkurrierende Darstellungen beeinflussen die Nutzerentscheidung,
- ein komplexer Workflow besitzt technisch funktionierende, aber noch nicht validierte Bedienpfade,
- Dashboard, Editor, Visualisierung oder mobile Interaktion ist ein wesentlicher Beta-Risikotreiber.

Kein UI-Prototyp, wenn die UI bereits den Kernpfad abdeckt und die offenen Risiken vorwiegend Deployment, Daten, Tests oder Backend betreffen.

Wenn ein Prototyp sinnvoll ist, erzeuge `ui-prototype-plan.md` als **Hypothesen- und Testanleitung**, nicht als Produktionsimplementierung. Für einen tatsächlich zu bauenden Wegwerfprototyp an `throwaway-prototype` übergeben.

### 7. Beta-Runbook erzeugen

Bei 100 % dokumentiere ausschließlich den ersten Beta-Betrieb:

- Voraussetzungen,
- Installation/Deployment,
- Konfiguration und Secrets,
- Start/Healthcheck,
- primären Beta-Nutzerpfad,
- erwartetes Ergebnis,
- bekannte Grenzen,
- Fehlerdiagnose/Recovery,
- Feedbackkanal und zu erfassende Beta-Evidenz,
- sichere Aktualisierung/Rollback soweit vorhanden.

## Ausgabeformat

`beta-readiness.json` muss mindestens enthalten:

```json
{
  "schemaVersion": 1,
  "repository": {"name": "owner/repo", "headSha": "..."},
  "betaDefinition": "...",
  "readinessPercent": 0,
  "betaReached": false,
  "dimensions": [
    {"name": "core-scope", "max": 20, "score": 0, "evidence": [], "gaps": []}
  ],
  "hardBlockers": [],
  "betaFollowUps": [],
  "uiPrototype": {"recommended": false, "reason": "..."},
  "nextActions": []
}
```

`nextActions` enthält höchstens drei nach Wirkung priorisierte Schritte.

## Komposition

- `iterate-software-projects`: liefert Repositoryzustand und kann die priorisierten Beta-Lücken anschließend umsetzen.
- `throwaway-prototype`: übernimmt einen klar formulierten UI-/Interaktions-Hypothesentest, wenn ein Prototyp empfohlen wurde.
- `disciplined-diagnosis`: übernimmt konkrete rote CI-, Test- oder Laufzeitfehler.
- `agent-handoff`: kann den verifizierten Beta-Stand an eine neue Sitzung übergeben.

Der Skill dupliziert weder deren Implementierungs- noch Diagnoseverfahren.

## Fehlerbehandlung

Stoppe eine definitive Beta-Aussage und markiere den Score als vorläufig, wenn Repositoryzugriff, aktuelle CI-Evidenz oder der zentrale Nutzerpfad nicht überprüfbar sind. Fehlende Evidenz wird nicht als Erfolg gewertet.

Bei widersprüchlichen Quellen gilt: ausführbarer aktueller Code/CI > gemergte PR-Evidenz > aktuelle Issues > Roadmap/README > ältere Planung.

## Abschlusskriterien

Abgeschlossen ist eine Ausführung, wenn genau ein Projekt bewertet wurde, Beta-Scope und Evidenz nachvollziehbar sind, der Prozentwert aus den sechs Dimensionen hervorgeht, harte Blocker getrennt sind und entweder ein Beta-Runbook oder maximal drei nächste Schritte vorliegen. Eine UI-Prototyp-Empfehlung muss eine konkrete Interaktionshypothese besitzen.
