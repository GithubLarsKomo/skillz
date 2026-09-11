# Second Brain Federation

Status: candidate capability  
Date: 2026-09-11  
Canonical skill: [`second-brain-federation-workflow`](../skills/second-brain-federation-workflow/SKILL.md)

## Ziel

Skillz unterstützt neben einzelnen Project Second Brains einen privaten **Super Second Brain** als föderierten Einstiegspunkt. Der Super Brain ist kein Daten-Monolith. Er speichert Registry-, Routing-, Availability- und Freshness-Metadaten und verweist von dort auf die kanonischen Child Brains.

```text
user / agent
    |
    v
Super Second Brain
    | registry + routing
    +--> domain collection brain
    |       +--> project / matter A
    |       +--> project / matter B
    |
    +--> standalone project brain
    |
    +--> standalone project brain
```

## Schichtentrennung

### Project Second Brain

`project-second-brain` dokumentiert einen konkreten Projektzustand ab dem Grilling, inklusive Events, Decisions, Evidence-Referenzen und externen Assets.

### Second Brain Federation

`second-brain-federation-workflow` kennt mehrere Project Second Brains und beantwortet nur:

- welcher Brain ist für einen Kontext zuständig,
- wo liegt er,
- ist Repository und Memory Root verifiziert erreichbar,
- welche Workflow-Familien gehören dorthin,
- wann wurde dieser Routingzustand zuletzt geprüft.

Der Federation Layer kopiert keine fachlichen Child-Artefakte.

## Privacy

Der reale Super Brain soll privat sein. Repository-Namen privater Child Brains können bereits sensible Metadaten darstellen. Deshalb enthält das öffentliche `skillz`-Repository bewusst **keine reale persönliche Federation Registry**. Es enthält nur Workflow, Contract und neutrale Beispiele.

Die reale Registry lebt im privaten Super-Brain-Repository.

## Availability

Federation unterscheidet:

- `available`: Repository und Memory Root verifiziert,
- `bootstrap-needed`: Repository vorhanden, Project Memory noch nicht materialisiert,
- `pending`: Ziel erwartet, aber derzeit nicht vollständig prüfbar,
- `unavailable`: zuvor bekannter Brain aktuell nicht erreichbar,
- `archived`: historischer Brain, kein aktives Routingziel.

Damit wird ein neu angelegtes leeres Repository nicht fälschlich als bereits gefüllter Second Brain dargestellt.

## Collection Mode

Langlebige Domänen können mehrere Projekte oder Matters in einem privaten Repository führen:

```text
docs/project-memory/            # Domain-Level-Index
projects/
  <id-a>/docs/project-memory/
  <id-b>/docs/project-memory/
```

Der Super Brain registriert das Collection Repository und kann aktive Child Roots verlinken, ohne deren Inhalte in die globale Registry zu kopieren.

## Bootstrap

Beim ersten Aufbau des privaten Super Brains:

1. bekannte Second-Brain-Kandidaten inventarisieren,
2. Repository-Zugriff, Sichtbarkeit und Default Branch prüfen,
3. Project-Memory-Root oder Bootstrap-Bedarf feststellen,
4. stabile `brainId` vergeben,
5. Scope, Modus und Workflow-Familien registrieren,
6. pro Brain eine Routing-Note erzeugen,
7. `registry.json`, `REGISTRY.md`, `INDEX.md` und Federation-Bootstrap-Event schreiben,
8. Ergebnis read-back-verifizieren.

Kein Kandidat darf stillschweigend verloren gehen.

## Workflow-Integration

Persistente Orchestratoren sollen weiterhin `project-second-brain` als lokale Memory-Schicht verwenden. Federation wird zusätzlich verwendet, wenn ein Brain strukturell registriert, gefunden, verschoben, archiviert oder global refreshed werden muss.

Damit bleibt ein lokaler Workflow auch dann funktionsfähig, wenn der Super Brain temporär nicht erreichbar ist.
