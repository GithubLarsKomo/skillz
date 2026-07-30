# Skill-Architektur

`skillz` wird als portabler Werkzeugkasten aus kleinen Fach-Skills, Orchestratoren und deterministischen Hilfsprogrammen gepflegt.

## Schichten

1. **Orchestratoren** koordinieren ein Ziel, wählen Fach-Skills aus und verwalten Übergaben. Sie duplizieren keine Fachlogik.
2. **Fach-Skills** lösen genau eine wiederkehrende Aufgabe mit klaren Triggern und Abschlusskriterien.
3. **Adapter-Skills** kapseln Anbieter, Agenten, Issue-Tracker oder Deployment-Ziele.
4. **Deterministische Werkzeuge** in `scripts/` übernehmen Parsing, Validierung, Transformation, Hashing und reproduzierbare Dateierzeugung.
5. **Referenzen** in `references/` enthalten selten benötigte Details, Formate und umfangreiche Beispiele.

## Repo-Konfiguration

Projektabhängige Angaben sollen nicht in Fach-Skills eingebrannt werden. Zielprojekte können stattdessen eine versionierte Konfiguration verwenden, beispielsweise:

```text
docs/agents/
  CONFIG.md
  CONTEXT.md
  DECISIONS.md
```

- `CONFIG.md`: Tracker, Labels, Dokumentationspfade, Build-/Testbefehle und erlaubte Schreibziele.
- `CONTEXT.md`: gemeinsame Domänensprache und zentrale Begriffe.
- `DECISIONS.md`: Index oder Verweis auf Architekturentscheidungen und verbindliche Festlegungen.

Ein späterer Bootstrap-Skill soll diese Dateien aus dem vorhandenen Repository ermitteln, Vorschläge anzeigen und erst nach Prüfung schreiben.

## Kompositionsregeln

- Übergaben erfolgen bevorzugt über Markdown, JSON, Issues, Pull Requests oder Dateien.
- Jeder Skill dokumentiert Eingang, Ausgang, Vorbedingungen, Fehlerzustand und Eigentümer des nächsten Schritts.
- Ein Orchestrator darf einen Skill nur als abgeschlossen behandeln, wenn dessen Abschlussnachweis vorliegt.
- Gesprächskontext allein ist kein dauerhaftes Übergabeformat für mehrstufige oder unterbrechbare Workflows.

## Qualitätsstufen

- **Draft:** Trigger und Ablauf sind formuliert, aber noch nicht praktisch evaluiert.
- **Candidate:** Happy Path, Grenzfall und Fehlerfall wurden geprüft.
- **Stable:** Der Skill wurde in mehreren realen Abläufen erfolgreich wiederverwendet und besitzt stabile Übergaben.
- **Deprecated:** Ein Nachfolger ist benannt; Migration und verbleibende Nutzer sind dokumentiert.

## Empfohlene nächste Skills

1. `repository-skill-bootstrap`: erzeugt projektbezogene Agent-Konfiguration und Domänendokumente.
2. `conversation-to-spec`: synthetisiert bestätigten Gesprächskontext ohne erneutes Interview in eine umsetzbare Spezifikation.
3. `spec-to-vertical-issues`: zerlegt eine Spezifikation in unabhängig umsetzbare vertikale Issues.
4. `disciplined-diagnosis`: reproduzieren, minimieren, Hypothesen bilden, instrumentieren, beheben und Regressionstest ergänzen.
5. `test-driven-vertical-slice`: Red-Green-Refactor pro kleinem End-to-End-Schnitt.
6. `architecture-deepening-review`: findet flache Module, Kopplung und fehlende Domänengrenzen.
7. `agent-handoff`: erzeugt einen kompakten, überprüfbaren Übergabestand für eine neue Sitzung oder einen anderen Agenten.

Diese Skills sollen in eigenen Worten und mit eigener Governance umgesetzt werden; fremde Repositories dienen als Inspiration, nicht als ungeprüfte Kopiervorlage.
