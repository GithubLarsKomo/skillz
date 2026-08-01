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
| [`agent-handoff`](skills/agent-handoff/SKILL.md) | Erzeugt einen kompakten, verifizierbaren Übergabestand für neue Sitzungen oder Agenten. Verwenden, wenn Ziel, Repositoryzustand, Entscheidungen, Evidenz, Restrisiken, blockierte Punkte und genau die nächste ausführbare Aktion ohne Informationsverlust oder doppelte Arbeit weitergegeben werden müssen. |
| [`architecture-deepening-review`](skills/architecture-deepening-review/SKILL.md) | Prüft bestehende Softwarearchitekturen evidenzbasiert auf flache Modulgrenzen, unbeabsichtigte Kopplung, duplizierte Domänenregeln und Infrastrukturleckage und empfiehlt höchstens einen kleinen, hochwirksamen Vertiefungsschritt. Verwenden, wenn Architekturqualität verbessert werden soll, ohne einen spekulativen Rewrite oder stilgetriebene Schichten einzuführen. |
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Konsolidiert wiederverwendbare Arbeitsabläufe als persönliche Skills, pflegt deren portable Fassungen im zentralen Repository GithubLarsKomo/skillz und synchronisiert beide Bestände sicher. Verwenden, wenn der Nutzer Skills lernen, zentral speichern, installieren, inventarisieren, abgleichen oder ausdrücklich in beide Richtungen synchronisieren lassen möchte. |
| [`composable-skill-factory`](skills/composable-skill-factory/SKILL.md) | Entwirft, prüft und veröffentlicht kleine, komponierbare Agent-Skills mit progressiver Offenlegung, deterministischen Hilfswerkzeugen, klaren Triggern und überprüfbaren Abschlusskriterien. Verwenden, wenn aus einem wiederholbaren Workflow ein neuer Skill werden soll oder ein bestehender Skill zu groß, unklar, fragil oder schwer kombinierbar ist. |
| [`conversation-to-spec`](skills/conversation-to-spec/SKILL.md) | Verdichtet bestätigten Gesprächs-, Grilling- und Repository-Kontext zu einer umsetzbaren, prüfbaren Spezifikation, ohne bereits beantwortete Fragen erneut zu stellen. Verwenden, wenn aus freigegebenen Festlegungen eine SPEC.md, ein technischer Umsetzungsrahmen oder eine belastbare Übergabe an Engineering entstehen soll. |
| [`deferred-external-action-verification`](skills/deferred-external-action-verification/SKILL.md) | Richtet für asynchron arbeitende externe Programme, APIs und CI/CD-Systeme eine zeitversetzte, wiederholbare Ergebnisprüfung per Cronjob oder gleichwertigem Scheduler ein. Nimmt jeden vom Agenten selbst ausgelösten CI-Lauf automatisch in eine Beobachtungsliste auf und setzt den gespeicherten Arbeitsablauf nach verifiziertem Erfolg fort. Der Skill definiert Wartefenster, Statusabfrage, Idempotenz, Sperren, Retry- und Abbruchregeln, Protokollierung sowie die sichere Aufräumlogik nach Erfolg oder endgültigem Fehler. |
| [`disciplined-diagnosis`](skills/disciplined-diagnosis/SKILL.md) | Diagnostiziert Softwarefehler reproduzierbar und evidenzbasiert, minimiert den Fehlerraum, prüft konkurrierende Hypothesen, implementiert den kleinsten sicheren Fix und belegt ihn mit Regressionstest sowie ursprünglicher Verifikation. Verwenden, wenn CI, Tests, Laufzeitverhalten oder Integrationen fehlschlagen und spekulative Änderungen vermieden werden sollen. |
| [`implement-from-issue`](skills/implement-from-issue/SKILL.md) | Implementiert ein klar abgegrenztes Repository-Issue vom verifizierten Ausgangszustand bis zu einem überprüfbaren Commit- oder Pull-Request-Stand mit vollständiger Rückverfolgbarkeit, Testevidenz, Sicherheits- und Migrationsbewertung sowie expliziter externer Nachverifikation. Verwenden, wenn ein umsetzungsreifes Issue sicher und ohne Scope-Ausweitung ausgeführt werden soll. |
| [`iterate-software-projects`](skills/iterate-software-projects/SKILL.md) | Iterative Weiterentwicklung bestehender Softwareprojekte durch den wiederkehrenden Zyklus aus Bestandsanalyse, Klärung kritischer Produktentscheidungen, Auswahl des nächsten kleinen Inkrements, präzisem Copilot- oder Coding-Agent-Prompt und evidenzbasiertem Review. Verwenden, wenn ein Repository schrittweise fortgeführt, ein Plan vor der Umsetzung geschärft, ein nächster Implementierungsauftrag formuliert, ein Agentenergebnis geprüft, ein Docker-/KI-Service diagnostiziert oder nach einem Review die nächste Iteration geplant werden soll. |
| [`merge-conflict-resolution`](skills/merge-conflict-resolution/SKILL.md) | Löst Git-Merge-Konflikte semantisch, rekonstruiert die Änderungsabsichten beider Seiten, bewahrt akzeptiertes Verhalten und Repository-Invarianten und erzeugt einen überprüfbaren Auflösungsstand mit Tests, Rollback und Restrisiken. Verwenden, wenn Konfliktmarker allein nicht zeigen, welche fachliche oder technische Kombination korrekt ist. |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Importiert ein bereits lokal vorhandenes OpenASR-Modell unter Windows robust in OpenASR Desktop, insbesondere wenn der signierte Online-Katalog wegen Proxy-, TLS- oder UnknownIssuer-Problemen nicht verwendet werden kann. |
| [`repository-skill-bootstrap`](skills/repository-skill-bootstrap/SKILL.md) | Analysiert ein bestehendes Software-Repository und richtet eine portable Agent-Arbeitsgrundlage mit CONFIG.md, CONTEXT.md und DECISIONS.md ein. Verwenden, wenn ein Repository erstmals für wiederholbare Arbeit mit mehreren Skills, Agenten oder Sitzungen vorbereitet werden soll. |
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Bei Softwareprojekten ist eine verpflichtende KI-/ML-Readiness-Prüfung einschließlich Einsatzpotenzial, Architekturvorbereitung, Datensammlung, Labeling und Governance Bestandteil des Grillings. Die generische, token-geschützte WebApp verwaltet parallele aktive und historische Grillings. Eine SPEC.md wird im Chat geprüft und erst nach Approval in ein separates Produkt-Repository übergeben. |
| [`spec-to-vertical-issues`](skills/spec-to-vertical-issues/SKILL.md) | Zerlegt eine freigegebene, konsistente Spezifikation in kleine, unabhängig abnehmbare vertikale Implementierungs-Issues mit vollständiger Rückverfolgbarkeit, Abnahmeevidenz, Abhängigkeiten und expliziten Nicht-Zielen. Verwenden, wenn aus SPEC.md und Entscheidungsregister eine geordnete Engineering-Backlog-Übergabe entstehen soll, ohne irreversible Architekturentscheidungen stillschweigend zu treffen. |
| [`synapse-orchestrator`](skills/synapse-orchestrator/SKILL.md) | Orchestrate complex or ambiguous goals by aligning on the desired outcome, routing work to direct execution, existing skills and tools, transparent expert perspectives, or explicitly requested subagents, and maintaining concise progress and next steps. Use when the user invokes Professor Synapse, Synapse_CoR, /start, /save, /reason, /settings, /new, /grill-me, or /learn-skill; asks for an expert or multi-expert analysis; wants a cross-domain task decomposed; or needs help choosing the right workflow before execution. |
| [`test-driven-vertical-slice`](skills/test-driven-vertical-slice/SKILL.md) | Implementiert ein kleines, unabhängig beobachtbares End-to-End-Verhalten durch einen disziplinierten Red-Green-Refactor-Zyklus. Verwenden, wenn ein klar begrenztes vertikales Issue mit Akzeptanzkriterien über die notwendigen Schichten hinweg umgesetzt werden soll, ohne horizontale Infrastrukturpakete, spekulative Abstraktionen oder rein mock-basierte Scheinerfolge. |
| [`two-axis-code-review`](skills/two-axis-code-review/SKILL.md) | Prüft eine Änderung unabhängig auf Anforderungsabdeckung und auf Implementierungs- sowie Lieferqualität. Verwendet zwei getrennte Evidenzachsen für Spezifikationstreue, Codequalität, Architektur, Tests, Sicherheit, Migrationen und Betriebsrisiken und liefert priorisierte, kleinste sichere Abhilfen ohne stilgetriebene Blocker oder spekulative Neuschreibung. |
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
