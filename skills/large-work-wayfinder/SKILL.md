---
name: large-work-wayfinder
description: Erschließt große, unklare oder schlecht abgegrenzte Engineering-Vorhaben durch evidenzbasierte Exploration, fokussierte Untersuchungs-Issues, Abhängigkeitsgraphen, Risikoreduktion und eine sichere Umsetzungsreihenfolge, ohne spekulative Architekturentscheidungen vorwegzunehmen.
userFacing: true
implicitInvocation: true
category: engineering
version: 0.3.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - architecture-deepening-review
  - disciplined-diagnosis
  - agent-handoff
  - project-second-brain
outputs:
  - wayfinding-brief.md
  - investigation-backlog.json
  - dependency-graph.json
lastEvaluated: 2026-09-02
---

# Large Work Wayfinder

## Trigger

Diesen Skill verwenden, wenn ein Vorhaben technisch zu groß, zu unklar oder zu risikoreich ist, um belastbar spezifiziert oder unmittelbar als Implementierungs-Issue ausgeführt zu werden.

## Routing und Abgrenzung

Wayfinder reduziert **technische und Engineering-Unsicherheit**. Er beantwortet die Frage: **Was müssen wir technisch erst verstehen oder belegen, bevor wir sicher spezifizieren oder implementieren können?**

Wayfinder ist nicht für fachliche Präferenz- oder Produktentscheidungen zuständig, führt kein Requirements-Interview, erzeugt keine normative `SPEC.md` und implementiert keinen Produktionscode.

Es gibt zwei gleichberechtigte Eintrittspfade:

### Pre-Spec Wayfinding

Verwenden, wenn Ziel und gewünschter Nutzen ausreichend verstanden sind, aber technische Evidenz für eine belastbare Spezifikation fehlt, etwa bei Legacy-Systemen, unbekannten Abhängigkeiten, Integrationen, Migrationen oder mehreren technisch plausiblen Pfaden.

Übergabe bei ausreichender Evidenz an `conversation-to-spec`. Entdeckt Wayfinder dabei eine fachliche oder produktbezogene Entscheidung, die nur der Nutzer oder Stakeholder treffen kann, wird diese an `round-based-requirements-grilling` geroutet und nicht technisch vorentschieden.

### Post-Spec Wayfinding

Verwenden, wenn eine freigegebene `SPEC.md` oder ein daraus abgeleiteter vertikaler Slice technisch noch nicht sicher ausführbar ist. Der betroffene Scope bleibt begrenzt; die gesamte Spezifikation wird nicht erneut geöffnet.

Wenn die technische Untersuchung nur den Slice klärt, geht die Evidenz zurück an `spec-to-vertical-issues`, damit der Slice neu geschnitten oder freigegeben werden kann. Wenn die Untersuchung eine SPEC-relevante Architektur-, Sicherheits-, Daten- oder Migrationsannahme verändert, geht die Evidenz zuerst an `conversation-to-spec`; erst nach aktualisierter und erneut freigegebener SPEC darf die Issue-Zerlegung fortgesetzt werden.

### Routing-Regeln

- Fachliche Entscheidungsunsicherheit → `round-based-requirements-grilling`.
- Technische oder Evidenz-Unsicherheit → `large-work-wayfinder`.
- Ausreichend geklärte Entscheidungen plus ausreichende technische Evidenz → `conversation-to-spec`.
- Technisch unklarer Slice nach SPEC-Freigabe → Wayfinder, nicht neues Grilling.
- Wayfinder entdeckt neue Produktentscheidung → Grilling.
- Wayfinder verändert eine normative SPEC-Annahme → `conversation-to-spec` vor weiterer Issue-Zerlegung.

## Voraussetzungen

Benötigt werden ein ausreichend abgegrenzter Produkt-, Repository-, Spezifikations- oder Issue-Kontext, ein unveränderlicher Head-SHA bei Repository-Arbeit, bekannte Randbedingungen, vorhandene Architektur- und Testevidenz sowie bekannte externe Systeme und irreversible Entscheidungen. Eine fertige `SPEC.md` oder bereits erzeugte vertikale Issues sind **keine Voraussetzung** für Pre-Spec Wayfinding.

Wenn ein `projectMemory`-Verweis vorliegt, vor der Exploration zuerst `state.json` und den letzten relevanten Event lesen. Bereits verifizierte Fakten und frühere Untersuchungen nicht ohne neue Freshness- oder Widerspruchsgründe wiederholen.

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

Dokumentiere Faktenlage, Unsicherheiten, Untersuchungsbacklog, Graph, Risiken, Rangfolge und genau eine ausführbare nächste Aktion mit unveränderlichem Repositoryzustand. Der Handoff benennt zusätzlich explizit das Ziel: `round-based-requirements-grilling`, `conversation-to-spec`, `spec-to-vertical-issues` oder einen nachgelagerten Engineering-Schritt.

### 7. Project Memory fortschreiben

Vor dem Routing an den nächsten Skill `project-second-brain` aktualisieren:

- Event mit `stage: wayfinding` erzeugen,
- `wayfinding-brief.md`, `investigation-backlog.json` und `dependency-graph.json` verlinken,
- relevante Repository-/Commit-/Source-Evidenz verankern,
- neu bestätigte Fakten von verbleibenden Hypothesen trennen,
- Decision Records verlinken, wenn eine wesentliche Entscheidung getroffen oder supersediert wurde,
- offene Untersuchungen und genau die nächste Aktion in `state.json` fortschreiben.

Ein einzelner Statuscheck ohne neue Evidenz erzeugt keinen neuen Event. Ein abgeschlossener Spike, eine geänderte technische Annahme oder ein Routingwechsel dagegen schon.

## Prüfungen

Vor Abschluss müssen Fakten und Annahmen getrennt, Untersuchungen dedupliziert und begrenzt, Stop-Bedingungen explizit, Abhängigkeiten konsistent, das Routingziel begründet und die nächste Aktion ohne weitere Interpretation ausführbar sein. Bei aktivem Project Memory muss der letzte wesentliche Wayfinding-Zustand vor dem Handoff verlinkt sein.

## Fehlerbehandlung

Stoppe und begrenze neu, wenn ein Framework voreilig gewählt, eine breite Neuschreibung empfohlen, Exploration und Implementierung vermischt, Annahmen als Fakten dargestellt, fachliche Entscheidungen technisch vorweggenommen oder zu viele überlappende Untersuchungen erzeugt werden.

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
  "routingTarget": "round-based-requirements-grilling|conversation-to-spec|spec-to-vertical-issues|engineering",
  "routingReason": "...",
  "risks": ["..."],
  "projectMemory": {"root": "docs/project-memory/INDEX.md", "state": "docs/project-memory/state.json", "latestEvent": "docs/project-memory/events/EVT-....md"},
  "nextAction": "exactly one executable action"
}
```

## Abschlusskriterien

Abgeschlossen ist das Wayfinding, wenn kritische technische Unsicherheit auf eine kleine, begründete Untersuchungsmenge reduziert, eine belastbare Abhängigkeits- und Umsetzungsreihenfolge erzeugt, das korrekte Routingziel festgelegt, der Zustand im Project Second Brain verankert und genau eine sichere nächste Aktion übergeben wurde.
