---
name: product-evidence-research
description: Recherchiert und normalisiert Produkte für bestätigte Kaufanforderungen und erzeugt ein quellenkritisches Evidence Set ohne Preisranking.
---

# Product Evidence Research

## Zweck und Grenze

Dieser Skill verwandelt bestätigte Kauf- oder Beschaffungsanforderungen in einen normalisierten, quellenkritisch belegten Kandidatenbestand. Er entdeckt den Markt hinreichend breit, hält exakte Produktidentitäten auseinander, bewertet Quellen nach ihrer Eignung für den konkreten Claim und übergibt ein `product-evidence-set.json`.

Er berechnet keine finale Rangliste, bestimmt keinen Preis-/Leistungssieger und ersetzt weder `research-to-evidence-note` noch professionelle Technology Due Diligence. Retrieval erfolgt mit den verfügbaren Web-, Such- oder Connector-Werkzeugen; die Evidenzsemantik folgt `research-to-evidence-note`.

## Trigger

Verwenden, wenn ein bestätigter Kaufkontext vorliegt und konkrete Produkte aus Herstellerseiten, Fachmagazinen, seriösen Testberichten, Nutzererfahrungen, Firmenwebseiten, YouTube oder vergleichbaren Quellen recherchiert und vergleichbar gemacht werden sollen.

Nicht verwenden, wenn Budget, Intended Use, Must-haves oder wesentliche Präferenzen noch ungeklärt sind; dann an `round-based-requirements-grilling` routen. Finanzinstrumente wie Aktien, ETFs oder Krypto sind ausdrücklich kein Trigger.

## Voraussetzungen

Benötigt werden mindestens:

- `decisionType: purchase`,
- Modus `private | professional-standard | professional-complex-technology`,
- Produktkategorie und Intended Use,
- Markt/Region,
- Must-haves und Ausschlüsse,
- bestätigte oder ausdrücklich noch ungewichtete Entscheidungskriterien,
- Budgetstatus soweit entscheidungsrelevant,
- `asOf` für zeitabhängige Recherche.

Fehlende fachliche Anforderungen werden nicht durch plausible Standardannahmen ersetzt.

## Ablauf

### 1. Recherchefrage fixieren

Formuliere die kleinste Entscheidungsfrage, die der Kandidatenmarkt beantworten muss. Trenne Must-haves von Präferenzen und notiere zulässige Produktzustände `new | refurbished | used`.

### 2. Kandidatenmarkt breit entdecken

Suche typischerweise etwa 15–30 plausible Kandidaten, sofern der reale Markt dies trägt. Stoppe früher, wenn die Kategorie kleiner ist oder harte Requirements den Markt nachweislich verengen. Eine Zielzahl darf nie durch künstliche Kandidaten aufgefüllt werden.

### 3. Produktidentität normalisieren

Jeder Kandidat erhält eine kanonische Identität mit soweit verfügbar `manufacturer`, `productFamily`, `model`, `generation`, `revision`, `variant`, `region`, `sku`/`mpn`, `status` und `identityConfidence`.

Nutze `scripts/normalize_product_identity.py` für deterministische Feldnormalisierung. Ambige Generationen, Kapazitäten, Größen oder Bundles werden nicht automatisch zusammengeführt. Evidenz eines anderen Modells darf nur mit expliziter Transferability-Begründung verwendet werden.

### 4. Quellen inventarisieren

Erfasse relevante Quellenkanäle: Hersteller/Firmenwebseite und offizielle Distributoren, Fachmagazine und professionelle Reviews, unabhängige Testlabore und Verbraucherorganisationen, Händler/Marktplätze, User-Rating-/Review-Plattformen und Communities, YouTube, technische/wissenschaftliche Literatur sowie Behörden/Zertifizierer soweit relevant.

Jede Quelle erhält mindestens `sourceClass`, `channel`, `independence`, Datum/Freshness, Produktidentitäts-Fit, Sponsoring/Affiliate-Hinweise soweit erkennbar und methodische Grenzen.

### 5. Quellen relativ zum Claim bewerten

Die Klassen aus `research-to-evidence-note` bleiben maßgeblich: `primary | strong-secondary | contextual | weak/unknown`.

Herstellerquellen sind primär für eigene Spezifikationen, Kompatibilität, Garantie und offizielle Features, aber nicht automatisch starke Evidenz für Vergleichssuperlative. Unabhängige Tests gewinnen an Gewicht durch transparente Methodik, vergleichbare Testbedingungen, objektive Messungen und eindeutige Modellidentität.

### 6. User Ratings als Signale auswerten

Ein **Sternmittelwert wird nie direkt in einen Qualitätsscore übersetzt**. Erfasse stattdessen soweit sinnvoll Review-Anzahl/-Verteilung, Aktualität, Verified-Purchase-Hinweise, wiederkehrende positive Themen, Fehler-/Service-Themen, Chargen-/Revisionsunterschiede und erkennbare Manipulationsrisiken.

### 7. YouTube methodisch klassifizieren

YouTube wird nicht pauschal auf- oder abgewertet. Reproduzierbare Messungen, offengelegte Setups, Side-by-side-Tests und Rohdaten können starke Sekundärevidenz liefern. Langzeiterfahrungen können kontextuell nützlich sein. Unboxings, sponsorgetriebene Promotion oder Affiliate-Listicles ohne Methodik bleiben schwach. Sponsoring und Affiliate-Bezug werden sichtbar gehalten, soweit erkennbar.

### 8. Evidenzfamilien deduplizieren

Mehrere Seiten, die dieselbe Hersteller-Pressemitteilung, denselben Labordatensatz oder denselben syndizierten Review wiederholen, sind keine unabhängige Bestätigung. Verknüpfe solche Quellen über `evidenceFamilyId`.

### 9. Claims und Konflikte strukturieren

Nutze die Semantik von `research-to-evidence-note`: `direct | derived | unknown`, Support, Contradictions und Confidence. Konflikte zwischen hochwertigen Quellen bleiben sichtbar und werden nicht still gemittelt.

### 10. Evidence Coverage bestimmen

Jeder Kandidat erhält `high | medium | low | insufficient`. **Evidence Coverage** ist getrennt von erwarteter Produktqualität.

### 11. Kandidaten vorfiltern

Offensichtliche Must-have-Verstöße dürfen als `excludedCandidates` markiert werden, aber das abschließende Hard Gate gehört zu `product-comparison-ranking`.

## Prüfungen

Vor Übergabe prüfen:

- Produktidentitäten sind eindeutig oder ausdrücklich unsicher,
- Varianten/Generationen wurden nicht stillschweigend vermischt,
- Herstellerclaims und unabhängige Evidenz sind getrennt,
- User-Sterne wurden nicht direkt als Qualitätsscore verwendet,
- YouTube wurde nach Methodik statt Plattform bewertet,
- Sponsoring/Affiliate-Hinweise sind sichtbar, soweit erkennbar,
- duplizierte Evidenzfamilien zählen nicht als unabhängige Bestätigung,
- negative Evidenz und Quellenkonflikte bleiben erhalten,
- Freshness ist bei revisions-/firmwareabhängigen Claims dokumentiert,
- Evidence Coverage bleibt getrennt von Produktqualität.

## Fehlerbehandlung

Wenn zentrale Quellen nicht zugänglich sind, Kandidatenidentitäten nicht sicher getrennt werden können oder Evidenz für zentrale Kriterien dünn ist, liefere ein partielles Evidence Set mit expliziten `evidenceGaps` und reduzierter Coverage.

Wenn die Recherche eine neue fachliche Entscheidung offenlegt, route an Grilling. Bei technischer Untersuchung jenseits normaler Produktrecherche route an `large-work-wayfinder` oder bei komplexen Vendor-Technologien an `technology-offer-assessment`.

## Übergabe

Erzeuge mindestens `product-evidence-set.json` mit `schemaVersion`, `asOf`, `decisionContextRef`, `candidateCountDiscovered`, `candidates`, `sources`, `evidenceFamilies`, `excludedCandidates` und `openQuestions`. Jeder Kandidat enthält `candidateId`, `identity`, `eligibilityPrecheck`, `claims`, `reviewSignals`, `evidenceCoverage` und `evidenceGaps`.

`product-evidence-set.md` fasst Kandidaten, wichtigste Claims, Konflikte, Evidenzlücken und Quellen zusammen. Nächster Normalpfad: `price-availability-snapshot`.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn ein hinreichend breiter Kandidatenmarkt gegen bestätigte Anforderungen recherchiert, Produktidentitäten normalisiert, relevante Quellen/Claims mit Independence, Freshness und Konflikten strukturiert, Evidence Coverage separat ausgewiesen und ein nachgelagerter Preis- oder Ranking-Skill den Bestand ohne erneute Grundrecherche übernehmen kann.
