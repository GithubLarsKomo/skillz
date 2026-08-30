---
name: travel-transport-research
description: Recherchiert plausible Flug-, Bahn-, Auto-, Fähr- und andere Transportoptionen für einen Travel Context und normalisiert Reisezeit, Umstiege und operationelle Eigenschaften ohne finales Ranking.
---

# Travel Transport Research

## Zweck und Grenze

Ermittle plausible Transportalternativen für einen bestätigten Travel Context und normalisiere ihre relativ stabilen operationellen Eigenschaften. Der Skill trennt Routen-/Produktmerkmale von konkreten zeitgestempelten Tarifangeboten. Aktuelle Preise und Buchbarkeit gehören zu `travel-availability-snapshot`; finales Ranking zu `travel-option-ranking`.

## Trigger

Verwenden, wenn Start, relevante Ziele und Reisedaten bzw. Zeitfenster ausreichend bekannt sind, um Flug, Bahn, Auto, Fähre oder andere realistische Verkehrsmittel zu recherchieren.

## Ablauf

1. Transportanforderungen und harte Grenzen aus `travel-context.json` übernehmen.
2. Plausible Modi und Routenfamilien bestimmen, ohne verbotene Modi wieder einzuführen.
3. Anbieter-, Fahrplan- und Infrastrukturquellen laden und bei Bedarf normalisieren.
4. Routenidentität mit Origin, Destination, Modus, Betreiber und relevanten Segmenten stabil halten.
5. Dauer, Umstiege, typische Frequenz, Gepäck-/Komfortmerkmale und bekannte operationelle Einschränkungen erfassen.
6. Claims und Konflikte nach vorhandener Evidence-Semantik strukturieren.
7. Keine konkrete aktuelle Tarifverfügbarkeit als dauerhafte Transport-Evidence speichern.

## Output Contract

`travel-transport-options.json` enthält mindestens:

- `schemaVersion`, `tripId`, `asOf`,
- `options`,
- `sources`,
- `evidenceGaps`, `limitations`.

Jede Option enthält `transportId`, `mode`, `origin`, `destination`, `segments`, soweit belegt `operator`, typische/planbare Dauer, Stop-/Transferstruktur, relevante Komfort-/Gepäckmerkmale, `eligibilityPrecheck`, `evidenceCoverage` und `sourceRefs`.

## Prüfungen

Bestanden nur wenn:

- Routing und konkrete Kaufangebote getrennt bleiben,
- Codeshare/Operating Carrier bzw. Betreiberidentität soweit relevant nicht still vermischt werden,
- Transfer- und Umstiegsstruktur erhalten bleibt,
- verbotene Transportmodi ausgeschlossen bleiben,
- aktuelle Preise nicht ohne `capturedAt` als Angebotsfakt dargestellt werden,
- keine finale Gewinnerentscheidung erfolgt.

## Fehlerbehandlung

Wenn konkrete Fahrpläne oder Verbindungen noch nicht veröffentlicht sind, `scheduleStatus: unavailable | provisional | unknown` verwenden und keine Zeiten erfinden. Bei nicht belastbarer Verbindung partiell liefern und Datenlücke an Availability/Ranking weitergeben.

## Übergabe

Normalpfad: `travel-availability-snapshot` prüft konkrete Angebote; `travel-option-ranking` bewertet Transport-Fit zusammen mit Destination und Stay.

## Abschlusskriterien

Abgeschlossen, wenn relevante Transportkandidaten identitätsstabil, quellenbezogen und ohne Vermischung mit flüchtigen Tarifen für die nachgelagerte Availability-Prüfung bereitstehen.
