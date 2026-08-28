---
name: skill-portfolio-audit
description: Analysiert das Skillz-Portfolio als Capability-System anhand von Capability Index, Dependency Graph, Evaluation Health, Lifecycle, Discoverability und Artefakt-Ownership. Verwenden für Konsolidierungs-, Redundanz-, Orphan-, Entrypoint- und Governance-Audits; keine Skills allein aufgrund semantischer Nähe löschen oder zusammenführen.
userFacing: true
implicitInvocation: true
category: workflow
discoverability: advanced
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - skill-portfolio-audit.json
  - skill-portfolio-audit.md
lastEvaluated: 2026-08-28
---

# Skill Portfolio Audit

## Trigger

Nutze den Skill, wenn das Repository auf Redundanz, Architekturdrift, zu viele Entrypoints, fehlende Evaluationen, unklare Output-Ownership, veraltete Skills oder sinnvolle neue Meta-Capabilities geprüft werden soll.

Nicht verwenden, um zwei fachlich verschiedene Spezialisten nur wegen ähnlicher Begriffe automatisch zu verschmelzen.

## Voraussetzungen

Bevorzugte Quellen sind die kanonischen Repository-Artefakte:

- `docs/skill-capability-index.json`;
- `docs/skill-dependency-graph.json`;
- `docs/CAPABILITY-HEALTH.md`;
- betroffene `SKILL.md`-Verträge und Evaluation Suites;
- Governance-/Architekturdokumentation.

Generierte Projektionen dienen zur Breitenanalyse; bei einer konkreten Entscheidung bleibt `SKILL.md` die normative Quelle.

## Ablauf

1. **Inventar fixieren.** Skill-, Entrypoint-, Discoverability-, Lifecycle- und Evaluation-Zahlen erfassen.
2. **Topologie prüfen.** Orchestratoren, interne Worker, Spezialisten, Renderer und Compatibility-Oberflächen anhand realer `requires`-/Artifact-Verträge untersuchen.
3. **Ownership prüfen.** Ambiguous outputs, doppelte Producer und scheinbar ungenutzte Outputs unterscheiden. Unconsumed terminal artifacts sind nicht automatisch Orphans.
4. **Entrypoints prüfen.** `public`, `advanced`, `internal` und `compatibility` getrennt bewerten; userFacing allein nicht mit Default-Discovery gleichsetzen.
5. **Redundanz klassifizieren.** Zwischen echter Duplikation, Compatibility-Fassade, Domain-Spezialisierung, Provider-/Brand-Wrapper und sinnvoller Orchestrierung unterscheiden.
6. **Evaluation prüfen.** Execution PASS und Coverage getrennt auswerten; besonders unevaluierte user-facing oder stable Skills hervorheben.
7. **Lifecycle prüfen.** Deprecations auf `replacedBy`, Migrationspfad, aktive Dependents und doppelte Output-Ownership prüfen.
8. **Maßnahmen priorisieren.** Findings in P0/P1/P2/P3 oder vergleichbare Risikoklassen ordnen; konkrete Files/Skills und Acceptance Criteria nennen.
9. **Audit ausgeben.** JSON für maschinelle Weiterverarbeitung plus Markdown-Zusammenfassung erzeugen.

## Prüfungen

- Werden Zahlen aus generierten Quellen zitiert statt geschätzt?
- Wird semantische Nähe nicht mit Redundanz gleichgesetzt?
- Werden terminale Outputs nicht pauschal als Orphans bezeichnet?
- Sind Lifecycle und Discoverability getrennt bewertet?
- Hat jede Konsolidierung einen Consumer-/Output-Migrationspfad?
- Bleiben regulierte, rechtliche, wissenschaftliche oder sportliche Fachgrenzen erhalten, sofern ihre Verträge tatsächlich verschieden sind?

## Fehlerbehandlung

- **Generierte Metadaten stale:** Audit als nicht belastbar markieren und Regeneration verlangen.
- **Ambiguous output:** Producer-Ownership zuerst klären, nicht durch willkürliche Consumer-Zuweisung kaschieren.
- **Unklarer Spezialisten-Unterschied:** beide Skills erhalten und konkrete Vertragsdifferenzen untersuchen.
- **Deprecated mit aktivem Consumer:** Removal blockieren und Migration planen.
- **PASS bei unvollständiger Coverage:** als Coverage-Risiko melden, nicht als vollständige Validierung ausgeben.

## Übergabe

`skill-portfolio-audit.json` enthält mindestens Inventory, Discoverability-Verteilung, Evaluation Health, Ownership Findings, Lifecycle Findings, Redundancy Candidates, bewusst erhaltene Grenzen und priorisierte Actions. `skill-portfolio-audit.md` fasst Entscheidungen und Begründungen lesbar zusammen.

## Abschlusskriterien

Der Audit ist abgeschlossen, wenn jede priorisierte Maßnahme auf überprüfbare Repository-Evidenz zurückgeführt ist, echte Defekte von Review-Queues getrennt sind und keine Konsolidierung ohne expliziten Migrations-/Ownership-Pfad empfohlen wird.
