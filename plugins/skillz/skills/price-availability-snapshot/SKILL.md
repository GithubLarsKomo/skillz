---
name: price-availability-snapshot
description: Erfasst SKU-genaue aktuelle Preise, Bezugsquellen und Verfügbarkeit für bekannte Produktkandidaten ohne Qualitätsranking.
---

# Price Availability Snapshot

## Zweck und Grenze

Dieser Skill erzeugt für bereits identifizierte Produktkandidaten einen zeitgestempelten, SKU-/variantenbezogenen Preis- und Verfügbarkeitssnapshot. Er trennt Produktzustand, Bundle, Versand, Steuerstatus und bei beruflichen Käufen bekannte TCO-Komponenten. Er entscheidet nicht, welches Produkt qualitativ besser ist, und erfindet keine Preise.

## Trigger

Verwenden, wenn konkrete Produktkandidaten feststehen und aktuelle Bezugsquellen, Preise, Lieferbarkeit oder professionelle Kostenkomponenten benötigt werden. Ebenfalls für spätere reine Preis-Refreshes einer bestehenden Shortlist verwenden.

Nicht für breite Produktsuche oder unklare Produktidentität verwenden.

## Voraussetzungen

Benötigt werden Kandidaten-IDs und kanonische Produktidentitäten, Zielmarkt und Währung, zulässiger Zustand `new | refurbished | used`, `asOf` und bei TCO ein definierter Horizont plus bekannte Kostenannahmen.

## Ablauf

### 1. Abfrageumfang begrenzen

Detailpreise werden vorzugsweise erst für den evidenzbasiert reduzierten Pool erhoben, typischerweise höchstens 10–15 Kandidaten. Breite Discovery-Preise dürfen zuvor nur als klar markierte Preisbänder dienen.

### 2. Exakte Offer-Identität prüfen

Jedes Angebot muss soweit verfügbar zu Modell, Generation, Variante, Region und SKU/MPN passen. Body-only, Kits, Speichergrößen, Gerätegrößen, Neuware, Refurbished und Gebrauchtware werden nicht still zusammengeführt.

### 3. Bezugsquellen erfassen

Klassifiziere Verkäufer soweit belegbar als `manufacturer-direct | authorized-dealer | specialist-retailer | large-retailer | marketplace-seller | refurbished-specialist | used-marketplace | unknown`. Ein niedriger Preis allein ist kein Vertrauenssignal.

### 4. Preis normalisieren

Erfasse Basispreis, Währung, Steuerstatus, Versand, effektiven Preis soweit berechenbar, Bundle-Inhalt, Zustand, Verfügbarkeit, Lieferhinweis, `capturedAt` und Quellenreferenz. Nutze `scripts/validate_price_snapshot.py` zur strukturellen Prüfung.

### 5. Fehlende Preise sichtbar halten

Wenn kein belastbarer Preis verfügbar ist, verwende `priceStatus: unavailable | quote-required | uncertain`. **MSRP** darf nur ausdrücklich als Listenpreis erscheinen und nicht als aktueller Straßenpreis.

### 6. Professionelle Kosten ergänzen

Bei beruflichen Anschaffungen erfasse, soweit relevant und belegt, CAPEX, Installation, Training, Servicevertrag, Pflichtzubehör, Lizenzen, Verbrauchsmaterial, Kalibrierung, Wartung, Ersatzteile, Switching/Disposal und explizit bereitgestellte Downtime-Kosten.

Berechne **TCO** nur mit definiertem Horizont und transparenten Annahmen. Bekannte und angenommene Kosten bleiben getrennt.

### 7. Freshness dokumentieren

Jeder aktuelle Preis trägt `capturedAt`. Das Resultat darf später unabhängig von der stabileren Produktevidenz aktualisiert werden.

## Prüfungen

Prüfe, dass Kandidaten- und Offer-SKU kompatibel sind, Produktzustände nicht vermischt werden, Währungen explizit sind, effektive Preise nachvollziehbar sind, alle als aktuell dargestellten Preise `capturedAt` tragen, fehlende Preise nicht geschätzt werden, Bundle-Unterschiede sichtbar sind und TCO Horizon/Annahmen zeigt.

## Fehlerbehandlung

Bei nicht erreichbarer Quelle, unklarer SKU oder widersprüchlichem Preis keine Schätzung erzeugen. Markiere das Offer als `uncertain` oder den Kandidaten als `unavailable`. Wenn der Preis-Pool zu dünn ist, liefere einen partiellen Snapshot; der Ranking-Skill muss preisabhängige Gewinner anschließend als unsicher behandeln.

## Übergabe

`price-snapshot.json` enthält mindestens `schemaVersion`, `asOf`, `market`, `offers`, optionale `tco` und `limitations`. Jedes Offer enthält `offerId`, `candidateId`, `seller`, `sellerType`, `condition`, `sku`, `priceStatus`, Preis/Währung, Versand, `effectivePrice`, `availability`, `bundle`, `capturedAt` und `sourceRef` soweit verfügbar.

Nächster Normalpfad: `product-comparison-ranking`.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn verfügbare Kaufangebote für die relevanten Kandidaten variantengenau und zeitgestempelt erfasst, nicht vergleichbare Offers getrennt, fehlende Preise explizit, professionelle TCO-Annahmen transparent und die Daten maschinenlesbar für Ranking oder späteren Price Refresh übergeben sind.
