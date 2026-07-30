# skillz

Zentrales, versioniertes Repository für wiederverwendbare Skills und Arbeitsabläufe.

## Struktur

Jeder Skill liegt in einem eigenen Verzeichnis unter `skills/` und besitzt mindestens eine `SKILL.md` mit YAML-Frontmatter:

```text
skills/
  <skill-name>/
    SKILL.md
```

## Enthaltene Skills

| Skill | Zweck | Quelle |
|---|---|---|
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Datengetriebenes, rundenbasiertes Requirements Engineering über die Grilling-WebApp; bei Softwareprojekten einschließlich verpflichtender KI-/ML-Readiness, Architekturvorbereitung, Datensammlung, Labeling und Governance | Konsolidiert aus `GithubLarsKomo/grilling` und erweitert um die verbindliche KI-/ML-Prüfung für Softwareprojekte |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Robuster Import lokal vorhandener OpenASR-Modelle bei nicht vertrauenswürdiger oder unerreichbarer Katalogverbindung | Aus dem erfolgreich erprobten Windows-Workflow rekonstruiert |
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Konsolidiert persönliche Skills und synchronisiert portable Inhalte konfliktgeschützt zwischen ChatGPT/Codex und diesem Repository | Aus der Festlegung zur zentralen und bidirektionalen Pflege aller persönlichen Skills |
| [`deferred-external-action-verification`](skills/deferred-external-action-verification/SKILL.md) | Prüft verzögert abschließende externe Aktionen sicher per Scheduler, nimmt selbst ausgelöste CI-Läufe automatisch in die Beobachtungsliste auf und setzt den gespeicherten Workflow nach verifiziertem Erfolg fort | Aus dem wiederkehrenden Bedarf abgeleitet, CI-, Deployment- und andere externe Jobs nach einer angemessenen Wartezeit automatisch erneut zu prüfen |
| [`iterate-software-projects`](skills/iterate-software-projects/SKILL.md) | Entwickelt bestehende Softwareprojekte in kleinen, evidenzbasiert geprüften Inkrementen weiter | Aus den wiederkehrenden Repository-, Copilot- und Coding-Agent-Iterationen konsolidiert |
| [`synapse-orchestrator`](skills/synapse-orchestrator/SKILL.md) | Orchestriert komplexe Ziele über direkte Ausführung, Fach-Skills, transparente Perspektiven, Unteragenten, Recherche und Automationen | Lizenzsaubere Eigenentwicklung auf Basis des gewünschten Professor-Synapse-Arbeitsstils |

## Pflegeprinzipien

- Skills sind produktunabhängig und wiederverwendbar.
- Fachliche Änderungen werden im jeweiligen `SKILL.md` versioniert.
- Projektdateien, Zugangsdaten, Tokens und personenbezogene Inhalte gehören nicht in dieses Repository.
- Ein Skill beschreibt Trigger, Voraussetzungen, Ablauf, Prüfungen, Fehlerbehandlung und Abschlusskriterien.
- Änderungen an einem Skill werden zuerst hier eingepflegt; projektspezifische Repositories dürfen darauf verweisen oder eine bewusst fixierte Kopie verwenden.
- Das Verfahren zur Erkennung, Konsolidierung und laufenden Pflege ist selbst im Skill `central-skill-repository-curation` festgelegt.
- Eine ausdrücklich bestätigte Skill-Ergänzung wird bei vorhandenem Schreibzugriff im selben Arbeitsgang geprüft, committed und auf GitHub veröffentlicht.

- Portable Skill-Inhalte werden anhand des Frontmatter-Namens bidirektional mit den installierten persönlichen ChatGPT/Codex-Skills abgeglichen; System- und Plugin-Skills sowie lokale UI-Metadaten bleiben ausgeschlossen.

## Namenskonvention

Verzeichnis- und Skillnamen verwenden englische, kleingeschriebene Slugs mit Bindestrichen. Die eigentliche Anleitung kann deutschsprachig sein.