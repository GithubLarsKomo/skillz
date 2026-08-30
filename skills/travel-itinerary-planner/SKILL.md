---
name: travel-itinerary-planner
description: Verwandelt ausgewählte oder gerankte Reiseoptionen in einen zeitlich und räumlich konsistenten Reiseplan mit Transfers, Öffnungszeiten, Reservierungsfenstern, Puffern und expliziten Unsicherheiten.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
discoverability: internal
owners:
  - GithubLarsKomo
requires:
  - travel-option-ranking
consumes:
  - travel-context.json
  - travel-ranking.json
  - travel-availability-snapshot.json
outputs:
  - travel-itinerary.json
  - travel-itinerary.md
lastEvaluated: 2026-08-30
---
# Travel Itinerary Planner

## Zweck und Grenze

Verwandle ausgewählte oder gerankte Reiseoptionen in einen zeitlich und räumlich konsistenten Reiseplan. Der Worker optimiert nicht nur eine Wunschliste, sondern prüft Transferzeiten, lokale Zeit, Reservierungsfenster, Öffnungszeiten soweit verfügbar, notwendige Puffer und Abhängigkeiten.

Er tätigt keine Buchung und darf ungeprüfte zeitliche Machbarkeit nicht als sicher darstellen.

## Trigger

Verwenden, wenn mindestens eine tragfähige Reiseoption aus `travel-ranking.json` ausgewählt oder als führend markiert ist und ein konkreter Tages-/Segmentplan benötigt wird.

## Ablauf

1. Lokale Zeitzonen und Reisetage fixieren.
2. Fixe Segmente wie Flüge, Züge, Check-in/out oder Reservierungen zuerst platzieren.
3. Transfer- und Wegezeiten zwischen geographischen Punkten berücksichtigen.
4. Öffnungs-/Reservierungsfenster aus zugänglichen Quellen einbeziehen; nicht verifizierte Constraints markieren.
5. Realistische Puffer für Flughäfen, Bahnhöfe, Gepäck, Check-in und kritische Verbindungen einplanen.
6. Aktivitäten nach Geografie, Zeit und Reisetempo clustern.
7. Überladene Tage reduzieren statt nominell alle Wünsche unterzubringen.
8. Bei unsicheren oder ausfallgefährdeten Segmenten Alternativen oder Recovery-Pfade hinterlegen.

## Output Contract

`travel-itinerary.json` enthält mindestens:

- `schemaVersion`, `tripId`, `timezonePolicy`,
- `days`,
- `transfers`,
- `reservations`,
- `buffers`,
- `dependencies`,
- `alternatives`,
- `unverifiedConstraints`,
- `limitations`.

Jedes Tagessegment enthält soweit relevant `start`, `end`, `location`, `duration`, `travelToNext`, `reservationRequirement`, `openingHoursConstraint`, `sourceRefs` und `confidence`.

## Prüfungen

Bestanden nur wenn:

- fixe Transportzeiten nicht durch Freizeitplanung überschrieben werden,
- Transferzeiten zwischen entfernten Orten nicht Null sind,
- lokale Zeitzonen konsistent behandelt werden,
- erforderliche Puffer sichtbar sind,
- unbekannte Öffnungszeiten/Reservierungen nicht als bestätigt erscheinen,
- Reisegeschwindigkeit und Wechselhäufigkeit den bestätigten Constraints entsprechen,
- finanziell verbindliche Aktionen nicht ausgeführt werden.

## Fehlerbehandlung

Wenn ein Tag oder eine Verbindung nicht belastbar machbar ist, nicht optimistisch komprimieren. Status `itinerary-conflict` mit konkretem Konflikt und mindestens einer realistischen Änderungsoption liefern.

## Übergabe

Der Orchestrator synthetisiert `travel-plan.json` und `travel-plan.md` aus Itinerary, Ranking und referenzierten Worker-Artefakten.

## Abschlusskriterien

Abgeschlossen, wenn der Plan geographisch und zeitlich plausibel, kritische Abhängigkeiten sichtbar, Unsicherheiten gekennzeichnet und alle verpflichtenden Segmente ohne bekannte Konflikte integriert sind.
