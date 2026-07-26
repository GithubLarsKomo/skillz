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
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Datengetriebenes, rundenbasiertes Requirements Engineering über die Grilling-WebApp | Konsolidiert aus `GithubLarsKomo/grilling` |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Robuster Import lokal vorhandener OpenASR-Modelle bei nicht vertrauenswürdiger oder unerreichbarer Katalogverbindung | Aus dem erfolgreich erprobten Windows-Workflow rekonstruiert |
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Erkennt wiederverwendbare Verfahren, konsolidiert sie als Skills und hält Repository, Katalog und lokale Kopien konsistent | Aus der Festlegung zur zentralen Pflege aller bisher und künftig erzeugten Skills |

## Pflegeprinzipien

- Skills sind produktunabhängig und wiederverwendbar.
- Fachliche Änderungen werden im jeweiligen `SKILL.md` versioniert.
- Projektdateien, Zugangsdaten, Tokens und personenbezogene Inhalte gehören nicht in dieses Repository.
- Ein Skill beschreibt Trigger, Voraussetzungen, Ablauf, Prüfungen, Fehlerbehandlung und Abschlusskriterien.
- Änderungen an einem Skill werden zuerst hier eingepflegt; projektspezifische Repositories dürfen darauf verweisen oder eine bewusst fixierte Kopie verwenden.
- Das Verfahren zur Erkennung, Konsolidierung und laufenden Pflege ist selbst im Skill `central-skill-repository-curation` festgelegt.

## Namenskonvention

Verzeichnis- und Skillnamen verwenden englische, kleingeschriebene Slugs mit Bindestrichen. Die eigentliche Anleitung kann deutschsprachig sein.
