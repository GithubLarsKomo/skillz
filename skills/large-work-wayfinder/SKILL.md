---
name: large-work-wayfinder
description: Erschließt große, unklare oder schlecht abgegrenzte Engineering-Vorhaben durch evidenzbasierte Exploration, fokussierte Untersuchungs-Issues, Abhängigkeitsgraphen, Risikoreduktion und eine sichere Umsetzungsreihenfolge, ohne spekulative Architekturentscheidungen vorwegzunehmen.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - architecture-deepening-review
  - disciplined-diagnosis
  - spec-to-vertical-issues
  - agent-handoff
outputs:
  - wayfinding-brief.md
  - investigation-backlog.json
  - dependency-graph.json
lastEvaluated: 2026-08-01
---

# Large Work Wayfinder

## Trigger

Diesen Skill verwenden, wenn ein Vorhaben zu groß, zu unklar oder zu risikoreich ist, um unmittelbar als Implementierungs-Issue ausgeführt zu werden.

## Voraussetzungen

Benötigt werden Repository, unveränderlicher Head-SHA, Produkt- oder Spezifikationskontext, bekannte Randbedingungen, offene Issues, vorhandene Architektur- und Testevidenz sowie bekannte externe Systeme und irreversible Entscheidungen.

## Ablauf

### 1. Ausgangslage fixieren

Verifiziere Repositoryzustand, Scope, betroffene Bereiche und vorhandene Entscheidungen. Trenne bestätigte Fakten, Annahmen, Hypothesen, Unbekannte, Blocker und autorisierungspflichtige Entscheidungen.

### 2. Kritische Unsicherheit bestimmen

Bewerte Unbekannte nach Auswirkung, Eintrittswahrscheinlichkeit, Irreversibilität, Abhängigkeiten und Kosten einer Fehlentscheidung. Wähle nur die kleinste Menge an Untersuchungen, die den nächsten sicheren Umsetzungsschritt ermöglicht.

### 3. Untersuchungs-Issues schneiden

Jede Untersuchung erhält eine einzige begrenzte Frage, zu erhebende Evidenz, Stop-Bedingung, Nicht-Ziele, erwartete Ausgabe und Handoff. Vermeide doppelte Spikes, offene Forschung und Vermischung mit Produktionsimplementierung.

### 4. Abhängigkeiten modellieren

Erzeuge einen Graphen aus Untersuchungen, Entscheidungen, Migrationen, externen Nachweisen und späteren vertikalen Issues. Kennzeichne harte Blocker, optionale Pfade und parallel ausführbare Arbeiten.

### 5. Reihenfolge ableiten

Priorisiere nach Risikoreduktion, Abhängigkeitsordnung, Reversibilität, Nutzerwert und Aufwand. Irreversible Architektur- oder Produktentscheidungen werden zur Autorisierung blockiert statt stillschweigend getroffen.

### 6. Wayfinding-Handoff erzeugen

Dokumentiere Faktenlage, Unsicherheiten, Untersuchungsbacklog, Graph, Risiken, Rangfolge und genau eine ausführbare nächste Aktion mit unveränderlichem Repositoryzustand.

## Prüfungen

Vor Abschluss müssen Fakten und Annahmen getrennt, Untersuchungen dedupliziert und begrenzt, Stop-Bedingungen explizit, Abhängigkeiten konsistent und die nächste Aktion ohne weitere Interpretation ausführbar sein.

## Fehlerbehandlung

Stoppe und begrenze neu, wenn ein Framework voreilig gewählt, eine breite Neuschreibung empfohlen, Exploration und Implementierung vermischt, Annahmen als Fakten dargestellt oder zu viele überlappende Untersuchungen erzeugt werden.

## Übergabe

```json
{
  "repository": {"name": "...", "headSha": "..."},
  "facts": ["..."],
  "assumptions": ["..."],
  "hypotheses": ["..."],
  "unknowns": ["..."],
  "blockers": ["..."],
  "decisions": [{"question": "...", "authorizationRequired": true}],
  "investigations": [{"id": "...", "question": "...", "evidence": ["..."], "stopCondition": "...", "nonGoals": ["..."], "output": "..."}],
  "dependencies": [{"from": "...", "to": "...", "type": "blocks|informs|optional"}],
  "rankedSequence": ["..."],
  "risks": ["..."],
  "nextAction": "exactly one executable action"
}
```

## Abschlusskriterien

Abgeschlossen ist das Wayfinding, wenn kritische Unsicherheit auf eine kleine, begründete Untersuchungsmenge reduziert, eine belastbare Abhängigkeits- und Umsetzungsreihenfolge erzeugt und genau eine sichere nächste Aktion übergeben wurde.
