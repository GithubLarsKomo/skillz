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

Nur tatsächlich benötigte Unterverzeichnisse werden angelegt. Die übergreifende Zielarchitektur ist in [`docs/SKILL-ARCHITECTURE.md`](docs/SKILL-ARCHITECTURE.md) beschrieben.

## Enthaltene Skills

| Skill | Zweck | Quelle |
|---|---|---|
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Datengetriebenes, rundenbasiertes Requirements Engineering über die Grilling-WebApp; bei Softwareprojekten einschließlich verpflichtender KI-/ML-Readiness, Architekturvorbereitung, Datensammlung, Labeling und Governance | Konsolidiert aus `GithubLarsKomo/grilling` und erweitert um die verbindliche KI-/ML-Prüfung für Softwareprojekte |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Robuster Import lokal vorhandener OpenASR-Modelle bei nicht vertrauenswürdiger oder unerreichbarer Katalogverbindung | Aus dem erfolgreich erprobten Windows-Workflow rekonstruiert |
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Konsolidiert persönliche Skills und synchronisiert portable Inhalte konfliktgeschützt zwischen ChatGPT/Codex und diesem Repository | Aus der Festlegung zur zentralen und bidirektionalen Pflege aller persönlichen Skills |
| [`composable-skill-factory`](skills/composable-skill-factory/SKILL.md) | Entwirft, zerlegt, prüft und veröffentlicht kleine Skills mit progressiver Offenlegung, deterministischen Werkzeugen, dokumentierten Übergaben und Evaluation | Lizenzsaubere Eigenentwicklung, inspiriert von den modularen Engineering-Prinzipien aus `mattpocock/skills` |
| [`deferred-external-action-verification`](skills/deferred-external-action-verification/SKILL.md) | Prüft verzögert abschließende externe Aktionen sicher per Scheduler, nimmt selbst ausgelöste CI-Läufe automatisch in die Beobachtungsliste auf und setzt den gespeicherten Workflow nach verifiziertem Erfolg fort | Aus dem wiederkehrenden Bedarf abgeleitet, CI-, Deployment- und andere externe Jobs nach einer angemessenen Wartezeit automatisch erneut zu prüfen |
| [`iterate-software-projects`](skills/iterate-software-projects/SKILL.md) | Entwickelt bestehende Softwareprojekte in kleinen, evidenzbasiert geprüften Inkrementen weiter | Aus den wiederkehrenden Repository-, Copilot- und Coding-Agent-Iterationen konsolidiert |
| [`synapse-orchestrator`](skills/synapse-orchestrator/SKILL.md) | Orchestriert komplexe Ziele über direkte Ausführung, Fach-Skills, transparente Perspektiven, Unteragenten, Recherche und Automationen | Lizenzsaubere Eigenentwicklung auf Basis des gewünschten Professor-Synapse-Arbeitsstils |

## Pflegeprinzipien

- Skills sind produktunabhängig, klein und wiederverwendbar.
- Ein Fach-Skill besitzt eine primäre Aufgabe; Orchestratoren koordinieren, ohne Fachlogik zu duplizieren.
- Fachliche Änderungen werden im jeweiligen `SKILL.md` versioniert.
- Umfangreiche oder selten benötigte Details werden progressiv in `references/` ausgelagert.
- Reproduzierbare Transformationen, Validierungen und Dateiarbeit werden nach Möglichkeit in `scripts/` implementiert und getestet.
- Projektdateien, Zugangsdaten, Tokens und personenbezogene Inhalte gehören nicht in dieses Repository.
- Ein Skill beschreibt Trigger, Voraussetzungen, Ablauf, Prüfungen, Fehlerbehandlung, Übergaben und Abschlusskriterien.
- Änderungen an einem Skill werden zuerst hier eingepflegt; projektspezifische Repositories dürfen darauf verweisen oder eine bewusst fixierte Kopie verwenden.
- Das Verfahren zur Erkennung, Konsolidierung und laufenden Pflege ist selbst im Skill `central-skill-repository-curation` festgelegt.
- Neue oder wesentlich überarbeitete Skills durchlaufen Happy Path, Grenzfall und Fehlerfall.
- Eine ausdrücklich bestätigte Skill-Ergänzung wird bei vorhandenem Schreibzugriff im selben Arbeitsgang geprüft, committed und auf GitHub veröffentlicht.
- Portable Skill-Inhalte werden anhand des Frontmatter-Namens bidirektional mit den installierten persönlichen ChatGPT/Codex-Skills abgeglichen; System- und Plugin-Skills sowie lokale UI-Metadaten bleiben ausgeschlossen.

## Namenskonvention

Verzeichnis- und Skillnamen verwenden englische, kleingeschriebene Slugs mit Bindestrichen. Die eigentliche Anleitung kann deutschsprachig sein.
