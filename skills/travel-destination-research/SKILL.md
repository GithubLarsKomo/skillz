---
name: travel-destination-research
description: Recherchiert und bewertet Reiseziele gegen einen bestätigten Travel Context und trennt belegte Zielmerkmale, Saisonalität, praktische Eignung und Evidenzlücken.
userFacing: false
implicitInvocation: true
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
  - travel-destination-evidence.json
  - travel-destination-evidence.md
lastEvaluated: 2026-08-30
---
# Travel Destination Research

## Zweck und Grenze

Recherchiere Reiseziele und Regionen gegen einen bestehenden `travel-context.json`. Der Skill erzeugt belegte Destination-Evidence zu Saisonalität, Klima, Erreichbarkeit auf grober Ebene, Aktivitäten, praktischer Eignung, Risiken und Ziel-Fit. Er entscheidet nicht über konkrete Flüge, Hotels oder finale Reisepläne.

Quellenbewertung und Claim-Semantik folgen `source-to-context` und `research-to-evidence-note`; Travel Research erfindet keine zweite Evidence-Klassifikation.

## Trigger

Verwenden, wenn der Zielstatus `open` oder `candidate` ist oder wenn für ein fixes Ziel belastbare Ziel-/Saison-/Praktikabilitätsevidenz benötigt wird.

## Ablauf

1. Kleinste Zielentscheidungsfrage aus `travel-context.json` fixieren.
2. Bei offenem Ziel einen hinreichend breiten, aber realistischen Kandidatenraum entdecken.
3. Quellen zu Saison, Klima, Ereignissen, praktischen Constraints, Infrastruktur, relevanten Aktivitäten und offiziellen Reiseinformationen erfassen.
4. Geladene Inhalte bei Bedarf über `source-to-context` normalisieren.
5. Relevante Claims über `research-to-evidence-note` mit Qualität, Freshness, Konflikten und Confidence strukturieren.
6. Offensichtliche Hard-Constraint-Verstöße als `eligibilityPrecheck` markieren, aber finales Ranking nicht vorwegnehmen.
7. Zielkandidaten und Evidenzlücken ausgeben.

## Travel-spezifische Evidence-Regeln

- Offizielle Einreise-, Sicherheits-, Verkehrs- oder Öffnungsinformationen sind für ihre eigene Zuständigkeit primär.
- Destination-Marketing ist primär für eigene Angebote, aber keine unabhängige Bestätigung von Vergleichssuperlativen.
- Klima-Normalwerte und konkrete Wetterprognosen werden nicht vermischt.
- Saisonale Aussagen tragen Zeitraum und `asOf`, wenn Aktualität materiell ist.
- Community- und Reiseberichte sind kontextuelle Erfahrungsquellen, keine automatische Tatsachenautorität.

## Output Contract

`travel-destination-evidence.json` enthält mindestens:

- `schemaVersion`, `tripId`, `asOf`,
- `researchQuestion`,
- `candidates`,
- `sources`, `claims`, `conflicts`,
- `excludedCandidates`,
- `evidenceGaps`, `openQuestions`.

Jeder Kandidat enthält `destinationId`, kanonische Identität/Region, `eligibilityPrecheck`, relevante Claims, `evidenceCoverage`, Hauptstärken, Hauptrisiken und Datenlücken.

## Prüfungen

Bestanden nur wenn:

- Zielidentitäten und Regionen nicht still vermischt werden,
- Saison und aktuelle Lage getrennt bleiben,
- Quellenkonflikte sichtbar sind,
- schwache Evidenz keinen sicheren Claim erzeugt,
- Hard-Constraint-Verstöße nachvollziehbar referenziert sind,
- kein finales Utility-Ranking im Research-Worker erfolgt.

## Fehlerbehandlung

Bei dünner Quellenlage oder ungeklärter Zielfrage ein partielles Evidence Set mit `evidence-insufficient` bzw. `requirements-incomplete` liefern. Keine vermeintlich exotischen oder populären Ziele künstlich hinzufügen.

## Übergabe

Downstream: `travel-option-ranking`; Transport- und Stay-Research können Zielkandidaten parallel vertiefen.

## Abschlusskriterien

Abgeschlossen, wenn die relevanten Destination-Kandidaten mit nachvollziehbarer Evidence Coverage, Konflikten, Freshness und offenen Punkten so strukturiert sind, dass Ranking und weitere Travel-Worker keine Grundrecherche wiederholen müssen.
