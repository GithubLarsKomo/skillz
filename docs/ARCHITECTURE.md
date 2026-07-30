# Skill-Architektur

`skillz` ist ein portabler Werkzeugkasten aus kleinen Fach-Skills, Orchestratoren und deterministischen Hilfsprogrammen.

## Schichten

1. **Orchestratoren** koordinieren Ziele und Übergaben, ohne Fachlogik zu duplizieren.
2. **Fach-Skills** lösen genau eine wiederkehrende Aufgabe mit klaren Triggern und Abschlusskriterien.
3. **Adapter-Skills** kapseln Anbieter, Agenten, Issue-Tracker oder Deployment-Ziele.
4. **Deterministische Werkzeuge** in `scripts/` übernehmen Parsing, Validierung, Transformation, Hashing und reproduzierbare Dateierzeugung.
5. **Referenzen** in `references/` enthalten selten benötigte Details, Formate und umfangreiche Beispiele.

## Repo-Konfiguration

Projektabhängige Angaben werden nicht in Fach-Skills eingebrannt. Zielprojekte verwenden stattdessen eine versionierte Konfiguration:

```text
docs/agents/
  CONFIG.md
  CONTEXT.md
  DECISIONS.md
```

`repository-skill-bootstrap` erzeugt und aktualisiert diese Grundlage nach Analyse und Prüfung.

## Kompositionsregeln

- Übergaben erfolgen bevorzugt über Markdown, JSON, Issues, Pull Requests oder Dateien.
- Jeder Skill dokumentiert Eingang, Ausgang, Vorbedingungen, Fehlerzustand und Eigentümer des nächsten Schritts.
- Ein Orchestrator behandelt einen Skill erst nach vorliegendem Abschlussnachweis als abgeschlossen.
- Gesprächskontext allein ist kein dauerhaftes Übergabeformat für mehrstufige oder unterbrechbare Workflows.
- Abhängigkeiten werden im Frontmatter unter `requires`, Ergebnisse unter `outputs` dokumentiert.

## Qualitätsstufen

- **Draft:** Trigger und Ablauf sind formuliert, aber noch nicht praktisch evaluiert.
- **Candidate:** Happy Path, Grenzfall und Fehlerfall wurden geprüft.
- **Stable:** Der Skill wurde in mehreren realen Abläufen erfolgreich wiederverwendet und besitzt stabile Übergaben.
- **Deprecated:** Ein Nachfolger ist benannt; Migration und verbleibende Nutzer sind dokumentiert.

## Validierungsmodell

Der Repository-Validator prüft mindestens:

- gültiges und abgeschlossenes Frontmatter,
- eindeutige Skillnamen,
- Übereinstimmung von Verzeichnis- und Frontmatter-Namen,
- vollständigen README-Katalog,
- vollständiges Synchronisationsmanifest,
- funktionierende relative Markdown-Links.

Strukturelle Empfehlungen zu Triggern, Prüfungen und Übergaben werden zunächst als Warnungen ausgegeben, damit bestehende Skills schrittweise migriert werden können.

## Kern-Workflow

```text
repository-skill-bootstrap
→ conversation-to-spec
→ spec-to-vertical-issues
→ iterate-software-projects
→ deferred-external-action-verification
```

Noch nicht vorhandene Skills dieses Workflows werden in `ROADMAP.md` geführt.
