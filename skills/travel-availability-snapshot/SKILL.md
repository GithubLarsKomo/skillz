---
name: travel-availability-snapshot
description: Erfasst zeitgestempelte aktuelle Transport-, Unterkunfts-, Mietwagen- und Aktivitätsangebote für bekannte Travel-Kandidaten einschließlich Preis, Verfügbarkeit und buchungsrelevanter Konditionen.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
discoverability: internal
owners:
  - GithubLarsKomo
requires: []
consumes:
  - travel-context.json
  - travel-transport-options.json
  - travel-stay-options.json
outputs:
  - travel-availability-snapshot.json
  - travel-availability-snapshot.md
lastEvaluated: 2026-08-30
---
# Travel Availability Snapshot

## Zweck und Grenze

Erzeuge einen zeitgestempelten Snapshot tatsächlich beobachteter Reiseangebote für bereits bekannte Kandidaten. Dieser Worker besitzt die volatile Commercial-/Availability-Schicht und trennt konkrete Tarife, Zimmer-Rates, Mietwagen- oder Aktivitätsangebote von der stabileren Destination-, Transport- und Stay-Evidence.

Er entscheidet nicht über den besten Reiseplan und erfindet keine Preise oder Buchbarkeit.

## Trigger

Verwenden, wenn konkrete Reise-, Transport- oder Unterkunftskandidaten feststehen und aktuelle Preise, Verfügbarkeit oder buchungsrelevante Konditionen benötigt werden. Ebenfalls für spätere reine Availability-/Price-Refreshes verwenden.

## Ablauf

1. Abfrage auf relevante Shortlist/Kandidaten beschränken.
2. Provider- und Offer-Identität exakt erfassen.
3. Preise mit Währung, Steuer-/Fee-Status und soweit möglich effektivem Gesamtpreis normalisieren.
4. `capturedAt` für jedes als aktuell dargestellte Offer speichern.
5. Transport-Offers mit Segmenten, Tarif, Gepäck, Umbuchung und Refundability soweit verfügbar erfassen.
6. Stay-Offers mit Property, Zimmer-/Rate-Typ, Belegung, Mahlzeiten, Cancellation, Prepayment, Steuern/Gebühren und Aufenthaltspreis erfassen.
7. Mietwagen-/Aktivitätsangebote nur aufnehmen, wenn sie für den Travel Context relevant sind.
8. Fehlende oder unklare Daten als `unavailable | quote-required | uncertain | unknown` markieren.

## Output Contract

`travel-availability-snapshot.json` enthält mindestens:

- `schemaVersion`, `tripId`, `capturedAt`, `currency`,
- `transportOffers`,
- `stayOffers`,
- optionale `carOffers`, `activityOffers`,
- `limitations`.

Jedes Offer enthält stabile Kandidatenreferenz, Provider/Verkäufer, konkrete Variant-/Rate-Identität, Verfügbarkeitsstatus, Preisstruktur, `capturedAt` und `sourceRef`.

## Prüfungen

Bestanden nur wenn:

- jedes aktuelle Offer einen Zeitstempel besitzt,
- Währungen explizit sind,
- Gesamtpreis und Preis-pro-Nacht/-Segment nicht verwechselt werden,
- unterschiedliche Tarif- oder Zimmerbedingungen sichtbar bleiben,
- non-refundable und free-cancellation nicht still zusammengeführt werden,
- fehlende Preise nicht geschätzt werden,
- Provider-Marketing nicht als unabhängige Qualitätsbewertung behandelt wird.

## Fehlerbehandlung

Wenn Provider- oder Webzugriff ausfällt, partiellen Snapshot liefern und betroffene Kandidaten `unknown` bzw. `unavailable` markieren. Kein gecachter oder historischer Preis darf ohne klare Kennzeichnung als aktuell dargestellt werden.

## Übergabe

Normalpfad: `travel-option-ranking`. Ein späterer Refresh kann nur diesen Worker plus Ranking und Orchestrator erneut ausführen, solange stabile Reiseevidenz nicht materiell veraltet ist.

## Abschlusskriterien

Abgeschlossen, wenn die für die Entscheidung relevanten aktuellen Offers variantengenau, konditionsbezogen und zeitgestempelt vorliegen oder Datenlücken explizit genug sind, dass Ranking keine Scheingenauigkeit erzeugt.
