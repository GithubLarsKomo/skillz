---
name: product-comparison-ranking
description: Rankt belegte Produkte gegen bestätigte Must-haves und Gewichte und trennt Nutzwert, Evidenzabdeckung und Ranking-Confidence.
userFacing: false
implicitInvocation: true
version: 0.1.1
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - product-ranking.json
  - product-ranking.md
lastEvaluated: 2026-08-22
---

# Product Comparison Ranking

## Zweck und Grenze

Dieser Skill bewertet normalisierte Produktkandidaten gegen bestätigte Requirements und aktuelle Preis-/TCO-Daten. Er führt Hard Gates vor Scores aus, berechnet gewichteten Nutzwert nur mit bestätigten Gewichten und bestimmt `quality-winner`, `price-performance-winner`, `bargain` sowie eine Shortlist mit maximal zehn Kandidaten.

Er recherchiert keinen Markt neu und verbirgt fehlende Evidenz nicht in Scheinscores.

## Trigger

Verwenden, wenn `requirements-handoff`, `product-evidence-set` und soweit für preisabhängige Entscheidungen erforderlich `price-snapshot` vorliegen. Nicht verwenden, wenn wesentliche Must-haves, Gewichtungen oder Produktidentitäten unklar sind.

## Voraussetzungen

Benötigt werden bestätigte Must-haves mit stabilen IDs, Entscheidungskriterien, bei numerischem Utility-Score bestätigte Gewichte mit Summe 1.0, Kandidatenclaims/criterion scores mit Evidenzreferenzen, Evidence Coverage, Preis/TCO soweit Preis in die Entscheidung eingeht und eine bestätigte bzw. explizit akzeptierte Bargain-Schwelle. Standardvorschlag für `bargainQualityFloor` ist `0.80`.

Nutze `scripts/validate_requirements.py` und `scripts/rank_products.py` für deterministische Prüfungen und Berechnungen.

## Ablauf

### 1. Identity Gate

Setze Kandidaten `CONDITIONAL/UNKNOWN`, wenn Modell oder Variante für einen materiellen Claim oder Preis nicht sicher zugeordnet ist.

### 2. Hard Requirement Gate

Bewerte jedes Must-have als `PASS | CONDITIONAL | FAIL | UNKNOWN`. Kandidatenstatus ist `FAIL`, sobald mindestens ein Must-have verfehlt wird; `CONDITIONAL`, wenn kein FAIL, aber mindestens ein Conditional/Unknown vorliegt; sonst `PASS`.

Ein **FAIL**-Kandidat kann nie Gewinner sein. Ein Kandidat mit materiellem `UNKNOWN` kann keinen unbedingten Gewinnerstatus erhalten.

### 3. Evidence Sufficiency

Halte `evidenceCoverage` separat von Leistung. Schwache Coverage führt nicht automatisch zu niedrigem Produktscore, begrenzt aber `rankingConfidence` und Winner-Posture.

### 4. Criterion Scores prüfen

Numerische Kriterien dürfen auf 0–100 normalisiert werden, wenn eine nachvollziehbare Basis existiert. Jeder Score verweist auf Claims/Evidenz und trägt Confidence. **Fehlende Evidenz** ist weder 0 noch 50 und wird nicht durch einen Midpoint imputiert.

### 5. Utility berechnen

Bei vollständigen bestätigten Gewichten gilt `utilityScore = Σ(weight_i × criterionScore_i)`. Kein beliebiger Confidence-Multiplikator. Wenn ein hoch gewichtetes Kriterium fehlt und das Ergebnis kippen könnte, setze `rankingConfidence: low | unresolved`.

### 6. Quality Utility bestimmen

`qualityUtility` verwendet die bestätigten nichtpreislichen Kriterien. Ein harter Maximalpreis bleibt Eligibility-Gate; bei nur weichem Zielbudget darf ein darüber liegender Quality Winner erscheinen, muss die Abweichung aber sichtbar ausweisen.

### 7. Winner bestimmen

**Quality Winner:** stärkster nichtpreislicher Fit unter PASS-Kandidaten mit ausreichender Evidenz.

**Price/Performance Winner:** höchste bestätigte Gesamtutility einschließlich Preis/TCO; nicht automatisch `performance / price`.

**Bargain:** PASS-Kandidat mit akzeptabler Reliability/Evidence, verfügbarem Kaufpreis, `qualityUtility >= bargainQualityFloor × qualityWinnerQualityUtility` und materiell niedrigerem Preis. Der Standardvorschlag `bargainQualityFloor = 0.80` ist konfigurierbar. Das **billigste Produkt allein** genügt nie.

**Winner-Collisions** sind zulässig: dasselbe Produkt darf mehrere Labels erhalten.

### 8. Shortlist auf maximal zehn reduzieren

Sortiere nach Entscheidungseignung und vermeide redundante Varianten ohne eigenständigen Entscheidungswert. Vielfalt darf einen klar besseren Kandidaten nicht künstlich verdrängen.

### 9. Sensitivity analysieren

Führe standardmäßig eine deterministische One-at-a-time-Gewichtssensitivität mit `sensitivityDelta = 0.05` aus: Erhöhe und reduziere jedes Kriterium einzeln um **5 Prozentpunkte** und renormalisiere alle übrigen Gewichte proportional auf Summe 1.0. Ein fachlich begründeter anderer Delta-Wert darf explizit konfiguriert werden.

Prüfe für jedes Szenario getrennt, ob sich **Quality Winner** oder **Price/Performance Winner** ändern. Jede Winner-Reversal wird mit veränderten Gewichten ausgewiesen. Wenn mindestens ein getestetes plausibles Gewichtsszenario den Gewinner ändert, gilt der entsprechende Gewinner als instabil und `rankingConfidence` darf nicht `high` sein.

Prüfe zusätzlich den Baseline-Abstand zwischen Platz 1 und 2. Standardmäßig gilt `nearTieThreshold = 1.0` Utility-Punkt auf der 0–100-Skala, getrennt für `qualityUtility` und `utilityScore`. Ein Abstand `<= nearTieThreshold` ist ein **Near Tie** und reduziert `rankingConfidence` auch dann, wenn die getesteten Gewichtungsänderungen den Sieger nicht umkehren. Damit darf ein numerischer Vorsprung ohne praktische Trennschärfe nicht als stabiler eindeutiger Sieger dargestellt werden.

Der Sensitivity-Output enthält mindestens Methode, Delta, Near-Tie-Schwelle, Zahl der getesteten Szenarien, Baseline-Winner, Score-Abstände, Near-Tie-Flags, Stabilitätsflags und alle Winner-Reversals.

## Prüfungen

Prüfe, dass Hard Gates vor Scores laufen; FAIL nie gewinnt; Conditional/Unknown nur caveated gewinnen kann; nur bestätigte Gewichte einfließen und 1.0 ergeben; fehlende Scores nicht imputiert werden; `utilityScore`, `qualityUtility`, `evidenceCoverage` und `rankingConfidence` getrennt bleiben; kein willkürlicher Confidence-Multiplikator verwendet wird; Bargain nicht bloß der billigste Kandidat ist; maximal zehn Kandidaten in der finalen Shortlist stehen; Winner-Collisions erlaubt sind; preisabhängige Gewinner bei fehlendem Preis unresolved bleiben; Sensitivity die Gewichte nach jeder Änderung wieder auf 1.0 normalisiert; Winner-Reversals sichtbar sind; und Near Ties oder instabile Winner kein `rankingConfidence: high` erhalten.

## Fehlerbehandlung

Fehlen bestätigte Gewichte, liefere eine qualitative Vergleichsmatrix statt erfundener Gesamtpunktzahl. Fehlen aktuelle Preise, kann Quality Winner ggf. bestimmt werden, während Price/Performance/Bargain unresolved bleiben. Wenn ein Missing Criterion das Ergebnis materiell verändern könnte, reduziere Ranking-Confidence und nenne die konkrete Evidenz, die die Entscheidung klären würde. Ungültige `sensitivityDelta`- oder `nearTieThreshold`-Werte werden abgelehnt statt still korrigiert.

## Übergabe

`product-ranking.json` enthält mindestens `schemaVersion`, `asOf`, `rankingConfidence`, `winners`, `rankedCandidates`, `excludedCandidates`, `sensitivity` und `limitations`. `sensitivity` enthält mindestens `method`, `delta`, `nearTieThreshold`, `scenarioCount`, `baseline`, `margins`, `nearTie`, `qualityWinnerStable`, `pricePerformanceWinnerStable` und `winnerChanges`. Jeder Ranked Candidate enthält `rank`, `candidateId`, `gate`, `utilityScore`, `qualityUtility`, `evidenceCoverage`, `labels`, `criterionScores`, Hauptstärke/-schwäche, `materialUnknowns` und `bestKnownOfferRef`.

Nächster Normalpfad: `purchase-decision-planner`.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn alle Kandidaten deterministisch durch Hard Gates gelaufen, Scores ausschließlich aus belegten Kriterien und bestätigten Gewichten berechnet, Evidence Confidence separat gehalten, Winner-Klassen reproduzierbar bestimmt, **Sensitivity** inklusive Near-Tie-Erkennung bei knappen Ergebnissen sichtbar und höchstens zehn finale Kandidaten übergeben sind.
