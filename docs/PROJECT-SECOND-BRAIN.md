# Project Second Brain

Status: active capability  
Date: 2026-09-02  
Canonical skill: [`project-second-brain`](../skills/project-second-brain/SKILL.md)

## Ziel

Skillz führt projektbezogene Arbeit ab dem Requirements-Grilling als GitHub-versionierten, Obsidian-kompatiblen Projektgraphen fort. Der Graph macht Entscheidungen, Evidenz, Artefakte, Iterationen und Übergaben nachvollziehbar, ohne eine zweite fachliche Wahrheit neben den kanonischen Producer-Artefakten zu erzeugen.

## Lifecycle

```text
round-based-requirements-grilling
        |
        v
project-second-brain bootstrap
        |
        +--> large-work-wayfinder --------+
        |                                  |
        +----------------------------------v
                               conversation-to-spec
                                         |
                                         v
                              spec-to-vertical-issues
                                         |
                                         v
                              iterate-software-projects
                                | implementation
                                | review
                                | delivery / closure
                                v
                                  next iteration
                                         |
                                         v
                                    agent-handoff
```

`project-second-brain` ist ein Querschnittsvertrag. Die fachlichen Skills behalten ihre Artefaktverantwortung; Project Memory erzeugt nur verlinkte Ereignis- und Zustandsprojektionen.

## Zielstruktur im Projekt-Repository

```text
docs/project-memory/
├── INDEX.md
├── TIMELINE.md
├── state.json
├── events/
├── decisions/
├── knowledge/
└── retrospectives/
```

### `INDEX.md`

Map of Content für Mensch und Obsidian. Enthält Projektziel, aktuellen Status, normative Artefakte, wichtige Decisions, letzte Events, offene Schleifen und den nächsten Schritt.

### `TIMELINE.md`

Append-orientierter chronologischer Index auf Event-Notes. Alte Zustände werden nicht gelöscht, sondern durch Folgeevents oder Supersession weitergeführt.

### `state.json`

Kompakte maschinenlesbare Projektion für Skill-Handoffs. Enthält `latestEvent`, `currentStage`, kanonische Artefakte, Decision-Referenzen, offene Schleifen, verifizierten Repositoryzustand und nächste Aktion.

### `events/`

Atomare Ereignisnotizen mit YAML-Frontmatter und normalen relativen Markdown-Links. Dadurch funktionieren dieselben Dateien in GitHub, Obsidian Properties, Dataview und Graph View.

## Verlinkungsprinzip

Project Memory kopiert keine `SPEC.md`, Wayfinding-Artefakte, Review-Evidenz oder Delivery-Daten. Es verweist auf die kanonischen Artefakte und dokumentiert ihren Status.

Beispiel:

```markdown
## Inputs

- [Requirements Handoff](../../requirements-handoff.json)
- [Wayfinding Brief](../../wayfinding-brief.md)

## Outputs

- [SPEC v1](../../SPEC.md)
- [DEC-004](../decisions/DEC-004.md)
```

Relative Markdown-Links sind bewusst die Standardform, weil sie sowohl GitHub als auch Obsidian verstehen.

## Event-Grenzen

Ein neuer Event entsteht bei semantischer Zustandsänderung, insbesondere:

- Grilling abgeschlossen oder wieder geöffnet,
- Wayfinding-/Research-Ergebnis,
- SPEC erstellt, geändert oder freigegeben,
- wesentliche Decision erstellt oder supersediert,
- Backlog erzeugt oder neu geschnitten,
- Engineering-Inkrement erreicht einen neuen verifizierbaren Zustand,
- Review-Entscheidung für einen fixierten SHA,
- Merge/Deployment/Requirement-Closure,
- Handoff oder Projektabschluss.

Keine Event-Flut für Low-Level-Kommandos, reine Lesezugriffe oder unveränderte Status-Polls.

## Historie und Auditierbarkeit

- Event-Notes sind nach Abschluss inhaltlich stabil.
- Substantielle Korrekturen erzeugen Folgeevents und Links auf den ersetzten Zustand.
- `INDEX.md`, `TIMELINE.md` und `state.json` sind aktualisierbare Projektionen.
- Git-Commits und immutable SHAs gehören zur Evidenz.
- Force-Rewrites werden nicht verwendet, um Projektgeschichte zu glätten.

## Datenschutz und Reasoning-Grenze

Persistiert werden nachvollziehbare Rationale, Alternativen, Entscheidungen, Annahmen, Evidenz und Ergebnisse. Nicht persistiert werden private Chain-of-Thought, Scratchpads, Secrets, unnötige personenbezogene Informationen oder vollständige Logs ohne dokumentarischen Mehrwert.

## Obsidian-Nutzung

Der Projekt-Repository-Root kann direkt als Vault geöffnet werden; alternativ kann nur `docs/project-memory/` in einen bestehenden Vault gespiegelt werden. Für den Graphen sind keine speziellen Plugins erforderlich. Dataview kann später auf YAML-Felder wie `stage`, `status`, `source_skill`, `previous_event` und `tags` zugreifen.

## Integrationspunkte in Skillz

Die Capability ist direkt in folgende Lifecycle-Entrypoints eingebunden:

- `round-based-requirements-grilling` — Bootstrap des ersten Project-Memory-Events,
- `large-work-wayfinder` — technische Evidenz und Routing,
- `conversation-to-spec` — normative Spezifikation und Freigabe,
- `spec-to-vertical-issues` — Backlog und Requirement-Traceability,
- `iterate-software-projects` — Implementation, Review, Delivery und nächste Iteration,
- `agent-handoff` — Fortsetzung ohne erneute Vollanalyse.

Die tieferen Producer-Skills behalten ihre bisherigen Output-Verträge; die Engineering-Orchestrierung verankert deren Ergebnisse an den semantischen Phasengrenzen.
