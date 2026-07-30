# skillz

Zentrales, versioniertes Repository für wiederverwendbare, kleine und komponierbare Agent-Skills und Arbeitsabläufe.

## Struktur

Jeder Skill liegt in einem eigenen Verzeichnis unter `skills/` und besitzt mindestens eine `SKILL.md` mit YAML-Frontmatter:

```text
skills/
  <skill-name>/
    SKILL.md
    references/   # optionale vertiefende Regeln und Beispiele
    scripts/      # optionale deterministische Hilfsprogramme
    assets/       # optionale Vorlagen und Ressourcen
    tests/        # optionale Fixtures und Prüfungen
```

Nur tatsächlich benötigte Unterverzeichnisse werden angelegt. Die übergreifende Zielarchitektur ist in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) beschrieben; geplante Erweiterungen stehen in [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Enthaltene Skills

| Skill | Zweck | Quelle |
|---|---|---|
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Datengetriebenes, rundenbasiertes Requirements Engineering über die Grilling-WebApp | Konsolidiert aus `GithubLarsKomo/grilling` |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Robuster Import lokal vorhandener OpenASR-Modelle | Aus dem erprobten Windows-Workflow rekonstruiert |
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Konfliktgeschützte Konsolidierung und Synchronisierung portabler Skills | Aus der zentralen Skill-Pflege abgeleitet |
| [`composable-skill-factory`](skills/composable-skill-factory/SKILL.md) | Entwirft, zerlegt, prüft und veröffentlicht kleine komponierbare Skills | Eigenentwicklung nach modularen Engineering-Prinzipien |
| [`repository-skill-bootstrap`](skills/repository-skill-bootstrap/SKILL.md) | Erzeugt eine portable Arbeitsgrundlage aus Repository-Kontext | Consumer der komponierbaren Skill-Architektur |
| [`deferred-external-action-verification`](skills/deferred-external-action-verification/SKILL.md) | Überwacht verzögert abschließende externe Aktionen und setzt Workflows fort | Aus CI- und Deployment-Überwachung abgeleitet |
| [`iterate-software-projects`](skills/iterate-software-projects/SKILL.md) | Entwickelt Softwareprojekte in kleinen, evidenzbasierten Inkrementen weiter | Aus wiederkehrender Repository-Arbeit konsolidiert |
| [`synapse-orchestrator`](skills/synapse-orchestrator/SKILL.md) | Orchestriert komplexe Ziele über Fach-Skills, Recherche und Automationen | Eigenentwicklung für den Professor-Synapse-Arbeitsstil |
| [`conversation-to-spec`](skills/conversation-to-spec/SKILL.md) | Verdichtet bestätigten Gesprächs- und Repository-Kontext zu einer prüfbaren Spezifikation | Aus dem rundenbasierten Grilling-Workflow abgeleitet |

## Qualitäts- und Metadatenmodell

Neue Skills sollen zusätzlich zu `name` und `description` folgende Frontmatter-Felder führen:

- `version`: semantische Version
- `status`: `draft`, `candidate`, `stable` oder `deprecated`
- `owners`: verantwortliche Personen oder Teams
- `requires`: benötigte Skills
- `outputs`: dokumentierte Übergabeformate
- `lastEvaluated`: Datum der letzten Evaluation

Die Vorlage liegt unter [`templates/SKILL.template.md`](templates/SKILL.template.md), das Schema unter [`schemas/skill.schema.json`](schemas/skill.schema.json).

## Pflegeprinzipien

- Skills sind produktunabhängig, klein und wiederverwendbar.
- Ein Fach-Skill besitzt eine primäre Aufgabe; Orchestratoren koordinieren, ohne Fachlogik zu duplizieren.
- Umfangreiche Details werden progressiv in `references/` ausgelagert.
- Reproduzierbare Transformationen und Validierungen werden nach Möglichkeit in `scripts/` implementiert.
- Projektdateien, Zugangsdaten, Tokens und personenbezogene Inhalte gehören nicht in dieses Repository.
- Ein Skill beschreibt Trigger, Voraussetzungen, Ablauf, Prüfungen, Fehlerbehandlung, Übergaben und Abschlusskriterien.
- Neue oder wesentlich überarbeitete Skills durchlaufen Happy Path, Grenzfall und Fehlerfall.
- Portable Skill-Inhalte werden konfliktgeschützt über `.skill-sync.json` abgeglichen.

## Validierung

Lokal:

```bash
python scripts/validate_skills.py
```

GitHub Actions führt dieselbe Prüfung bei Pull Requests und Pushes auf `main` aus.

## Namenskonvention

Verzeichnis- und Skillnamen verwenden englische, kleingeschriebene Slugs mit Bindestrichen. Die eigentliche Anleitung kann deutschsprachig sein.
