---
name: travel-stay-research
description: Recherchiert geeignete Unterkünfte und bewertet Lage, Eigenschaften, Qualitäts- und Review-Signale gegen den Travel Context ohne aktuelle Zimmerangebote als dauerhafte Produktevidenz zu behandeln.
userFacing: false
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
discoverability: internal
owners:
  - GithubLarsKomo
requires:
  - source-to-context
  - research-to-evidence-note
consumes:
  - travel-context.json
outputs:
  - travel-stay-options.json
  - travel-stay-options.md
lastEvaluated: 2026-08-30
---
# Travel Stay Research

## Zweck und Grenze

Recherchiere geeignete Hotels, Apartments, Gästehäuser und andere Unterkünfte gegen einen `travel-context.json`. Bewerte relativ stabile Eigenschaften wie Lage, Unterkunftstyp, Ausstattung und belastbare Qualitäts-/Review-Signale. Konkrete Zimmerpreise, Kontingente, Cancellation-/Prepayment-Konditionen und Buchbarkeit gehören ausschließlich zu `travel-availability-snapshot`.

## Trigger

Verwenden, wenn Zielregion und ungefähre Reisedaten bekannt sind und Unterkünfte gegen harte Anforderungen und Präferenzen untersucht werden sollen.

## Ablauf

1. Stay-Must-haves und Lageanforderungen aus dem Travel Context übernehmen.
2. Einen ausreichenden Kandidatenpool über verfügbare Provider, Web- und offizielle Quellen entdecken.
3. Property-Identität, Adresse/Region und Unterkunftstyp eindeutig halten.
4. Lage relativ zu relevanten Reiseankern und Mobilitätsanforderungen bewerten.
5. Ausstattung und offizielle Property-Claims von unabhängigen Review-/Erfahrungssignalen trennen.
6. Review-Mittelwerte nicht direkt in einen Qualitätsutility-Score umwandeln; wiederkehrende Themen, Aktualität und methodische Grenzen erfassen.
7. Zeitabhängige Zimmerangebote nicht in das stabile Stay-Evidence-Objekt kopieren.

## Output Contract

`travel-stay-options.json` enthält mindestens:

- `schemaVersion`, `tripId`, `asOf`,
- `properties`,
- `sources`,
- `reviewSignals`,
- `excludedProperties`,
- `evidenceGaps`, `limitations`.

Jede Property enthält `propertyId`, kanonische Identität, Lage/Region, Typ, relevante Ausstattung, `eligibilityPrecheck`, belegte Claims, Review-Signale, `evidenceCoverage` und `sourceRefs`.

## Prüfungen

Bestanden nur wenn:

- Property und konkrete Zimmer-/Rate-Angebote getrennt bleiben,
- unterschiedliche Häuser einer Kette nicht vermischt werden,
- offizielle Ausstattung und unabhängige Qualitätsaussagen getrennt sind,
- Review-Sterne nicht automatisch Produktqualität bedeuten,
- Lageanforderungen gegen reale Geografie betrachtet werden,
- keine veraltete Rate als aktuelle Buchbarkeit erscheint.

## Fehlerbehandlung

Bei unklarer Property-Identität oder dünner Evidenz den Kandidaten `conditional | unknown` markieren. Keine Ausstattung oder Lagequalität aus Markenimage ableiten.

## Übergabe

Normalpfad: `travel-availability-snapshot` prüft konkrete Zimmer-/Rate-Angebote; `travel-option-ranking` kombiniert Stay Fit mit Transport, Destination und Kosten.

## Abschlusskriterien

Abgeschlossen, wenn ein normalisierter Unterkunftspool mit belastbaren Eigenschaften, Lagebezug, Review-Signalen und Evidenzlücken vorliegt, ohne volatile Zimmerangebote als dauerhafte Evidenz zu behandeln.
