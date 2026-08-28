---
name: legal-redline-review-loop
description: Vergleicht neue Vertrags- oder Legal-Redline-Versionen mit dem letzten bewerteten Stand, hält Issue-Lineage und Verhandlungszustand stabil und klassifiziert Änderungen als improved, accepted, neutral, deteriorated, new-risk, resolved oder regression. Verwenden in iterativen Vertragsverhandlungen nach initialem Review und Negotiation Strategy.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - contract-review
  - legal-negotiation-strategy
outputs:
  - redline-delta.json
  - negotiation-state.json
  - redline-review.md
lastEvaluated: 2026-08-28
---

# Legal Redline Review Loop

## Zweck

Bewerte jede neue Fassung als Delta zum letzten verifizierten Stand. Bereits gelöste Issues bleiben geschlossen, sofern die neue Version sie nicht materiell wieder öffnet.

## Version Gate

Vor dem Vergleich erfasse soweit möglich Dokumentversion, Dateiname, Hash, Zeitstand und direkten Vorgänger. Ist die Baseline unklar, markiere `baseline-uncertain` statt Änderungen zu erfinden.

## Issue Lineage

Jedes bestehende Issue behält seine `issueId`. Neue Issues erhalten neue IDs. Zusammenführungen oder Aufspaltungen werden über `derivedFrom` dokumentiert, damit Risiko- und Verhandlungsentscheidungen nachvollziehbar bleiben.

## Delta Classes

- `improved` – Position ist gegenüber dem letzten Stand besser, Issue aber noch offen.
- `accepted` – bewusste, autorisierte Übernahme einer Gegenposition.
- `neutral` – keine materielle Veränderung.
- `deteriorated` – Position hat sich materiell verschlechtert.
- `new-risk` – neue materielle Belastung oder neuer Konflikt.
- `resolved` – Issue ist nach bestätigtem Ziel erledigt.
- `regression` – bereits gelöstes oder akzeptabel begrenztes Risiko wurde wieder geöffnet oder verschlechtert.

## Review Workflow

1. Neue Version gegen direkten Vorgänger diffen.
2. Änderungen auf bestehende Issue IDs mappen.
3. Neue Klauseln, Löschungen und Cross-Clause-Effekte erfassen.
4. Jede materielle Änderung einer Delta Class zuordnen.
5. Gegen `negotiation-positions.json` prüfen: Target, Fallback, Red Line und Authority.
6. Regressions und neue Risiken priorisiert hervorheben.
7. Nur bei tatsächlich geänderter Grundlage bereits gelöste Punkte neu öffnen.
8. `negotiation-state.json` fortschreiben, nicht neu erfinden.

## Negotiation State

Erfasse pro Issue mindestens `status`, `currentPosition`, `lastDelta`, `authorityState`, `counterpartyPosition`, `nextMove` und relevante VersionRefs.

## Kernregeln

- Eine sprachliche Änderung ist nicht automatisch materiell; bewerte Rechts-/Risikoauswirkung.
- Eine entfernte Klausel kann über Querverweise oder andere Klauseln materiell fortwirken; Cross-Clause Review bleibt erforderlich.
- `accepted` verlangt dokumentierte Autorität, wenn die Position eine Freigabegrenze berührt.
- Ein `regression` wird nie durch den Status einer älteren Fassung verdeckt.

## Qualitätsgate

Pass nur, wenn Baseline, Version Lineage, Issue Lineage, Delta Classification, Authority und nächste Verhandlungsschritte nachvollziehbar sind und kein bereits gelöstes Risiko unbemerkt zurückkehrt.