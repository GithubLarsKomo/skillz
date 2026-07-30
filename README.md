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

<!-- skill-catalog:start -->
| Skill | Zweck |
|---|---|
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Konsolidiert persönliche Skills und synchronisiert portable Inhalte konfliktgeschützt zwischen ChatGPT/Codex und diesem Repository |
| [`composable-skill-factory`](skills/composable-skill-factory/SKILL.md) | Entwirft, zerlegt, prüft und veröffentlicht kleine Skills mit progressiver Offenlegung, deterministischen Werkzeugen, dokumentierten Übergaben und Evaluation |
| [`conversation-to-spec`](skills/conversation-to-spec/SKILL.md) | Verdichtet bestätigten Gesprächs-, Grilling- und Repository-Kontext zu einer umsetzbaren, prüfbaren Spezifikation, ohne bereits beantwortete Fragen erneut zu stellen. Verwenden, wenn aus freigegebenen Festlegungen eine SPEC.md, ein technischer Umsetzungsrahmen oder eine belastbare Übergabe an Engineering entstehen soll. |
| [`deferred-external-action-verification`](skills/deferred-external-action-verification/SKILL.md) | Prüft verzögert abschließende externe Aktionen sicher per Scheduler, nimmt selbst ausgelöste CI-Läufe automatisch in die Beobachtungsliste auf und setzt den gespeicherten Workflow nach verifiziertem Erfolg fort |
| [`iterate-software-projects`](skills/iterate-software-projects/SKILL.md) | Entwickelt bestehende Softwareprojekte in kleinen, evidenzbasiert geprüften Inkrementen weiter |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Robuster Import lokal vorhandener OpenASR-Modelle bei nicht vertrauenswürdiger oder unerreichbarer Katalogverbindung |
| [`repository-skill-bootstrap`](skills/repository-skill-bootstrap/SKILL.md) | Analysiert ein Software-Repository und erzeugt eine portable Arbeitsgrundlage aus CONFIG.md, CONTEXT.md und DECISIONS.md |
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Datengetriebenes, rundenbasiertes Requirements Engineering über die Grilling-WebApp; bei Softwareprojekten einschließlich verpflichtender KI-/ML-Readiness, Architekturvorbereitung, Datensammlung, Labeling und Governance |
| [`synapse-orchestrator`](skills/synapse-orchestrator/SKILL.md) | Orchestriert komplexe Ziele über direkte Ausführung, Fach-Skills, transparente Perspektiven, Unteragenten, Recherche und Automationen |
<!-- skill-catalog:end -->

Der Katalog wird mit `python scripts/generate_catalog.py` aus dem Frontmatter der Skills erzeugt.

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
python scripts/verify_generated.py
```

GitHub Actions führt dieselben Prüfungen bei Pull Requests und Pushes auf `main` aus.

## Namenskonvention

Verzeichnis- und Skillnamen verwenden englische, kleingeschriebene Slugs mit Bindestrichen. Die eigentliche Anleitung kann deutschsprachig sein.
