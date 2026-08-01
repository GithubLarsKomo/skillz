---
name: throwaway-prototype
description: Prüft unsichere technische oder fachliche Annahmen mit bewusst kurzlebigen, isolierten Prototypen, trennt Lernnachweise von Produktionsabnahme und verhindert die unbeabsichtigte Übernahme experimentellen Codes.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - large-work-wayfinder
  - disciplined-diagnosis
  - spec-to-vertical-issues
  - agent-handoff
outputs:
  - prototype-brief.md
  - prototype-evidence.json
  - disposal-record.json
lastEvaluated: 2026-08-01
---

# Throwaway Prototype

## Trigger

Verwenden, wenn eine einzelne unsichere Annahme vor einer Produktionsimplementierung mit minimalem Aufwand diskriminiert werden muss.

## Voraussetzungen

Erforderlich sind eine explizite Hypothese oder Entscheidungsfrage, Evidenzschwelle, Zeit- oder Scope-Box, Nicht-Ziele, Isolationsstrategie, Entsorgungsplan sowie ein unveränderlicher Ausgangsstand.

## Ablauf

### 1. Experimentvertrag festlegen

Definiere genau eine Hypothese, die erforderliche Evidenz, Abbruchkriterien, Prototypklasse und die Grenzen zulässiger Schlussfolgerungen.

### 2. Sicher isolieren

Nutze einen separaten Branch, ein temporäres Verzeichnis oder ein eigenständiges Harness. Produktions-Secrets, personenbezogene Daten, Sicherheitsbypässe und direkte Produktivpfade sind verboten.

### 3. Kleinsten diskriminierenden Prototyp bauen

Implementiere nur das Minimum, das die Hypothese unterscheiden kann. Dokumentiere Mocks, Abkürzungen, ignorierte Qualitätsmerkmale, Datenquellen und Sicherheitsgrenzen.

### 4. Evidenz erheben

Erfasse beobachtbare Ergebnisse gegen die vorab definierte Schwelle. Trenne Prototypnachweise ausdrücklich von Produktions-Akzeptanzkriterien.

### 5. Schlussfolgerung begrenzen

Bewerte die Hypothese als gestützt, widerlegt oder unentschieden und benenne verbleibende Unsicherheit sowie externe Nachweise, die noch fehlen.

### 6. Entsorgen oder archivieren

Lösche oder archiviere den Prototyp nach dokumentiertem Lernen. Eine Übernahme in Produktion erfordert ein neues, begrenztes Implementierungs-Issue und Review.

### 7. Übergabe erzeugen

Übergebe unveränderliche Referenzen, Beobachtungen, Schlussfolgerungsstärke, Grenzen, Entsorgungsstatus und genau eine nächste Aktion.

## Prüfungen

Vor Abschluss müssen Hypothese, Evidenzschwelle, Isolation, Daten- und Sicherheitsgrenzen, Trennung zur Produktionsabnahme sowie Entsorgung oder autorisierte Umwandlung belegt sein.

## Fehlerbehandlung

Stoppe bei Scope-Ausweitung, polierter Mini-Produktentwicklung, Nutzung sensibler Daten, Sicherheitsabschwächung, fehlender Hypothese oder stiller Übernahme experimentellen Codes.

## Übergabe

```json
{
  "repository": {"name": "...", "headSha": "..."},
  "hypothesis": "...",
  "evidenceThreshold": "...",
  "prototypeClass": "code|interface|data|integration|migration|performance|user-flow",
  "isolation": "...",
  "shortcuts": ["..."],
  "observations": ["..."],
  "conclusion": {"state": "supported|rejected|inconclusive", "strength": "..."},
  "limitations": ["..."],
  "productionAcceptanceEvidence": "not established",
  "disposal": {"state": "deleted|archived|authorized-conversion", "evidence": "..."},
  "residualUncertainty": ["..."],
  "nextAction": "exactly one executable action"
}
```

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn die Hypothese mit begrenzter Evidenz bewertet, Lern- und Produktionsnachweis getrennt, der experimentelle Stand entsorgt oder autorisiert archiviert und genau eine nächste Aktion übergeben wurde.
