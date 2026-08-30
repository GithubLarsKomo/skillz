---
name: travel-option-ranking
description: Bewertet Reiseoptionen deterministisch gegen bestätigte harte Constraints und Entscheidungskriterien und trennt Reisefit, Kosten, Evidenzabdeckung und Ranking-Confidence.
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
  - travel-destination-evidence.json
  - travel-transport-options.json
  - travel-stay-options.json
  - travel-availability-snapshot.json
outputs:
  - travel-ranking.json
  - travel-ranking.md
lastEvaluated: 2026-08-30
---
# Travel Option Ranking

## Zweck und Grenze

Bewerte kombinierbare Reiseoptionen gegen bestätigte Anforderungen. Hard Gates laufen vor jedem Utility-Score. Der Skill trennt Travel Fit, Preis/Kosten, Evidence Coverage und Ranking Confidence und darf mehrere Winner-Klassen auf denselben Kandidaten vergeben.

Er recherchiert keine neuen Ziele oder Angebote und erstellt noch keinen Tagesreiseplan.

## Trigger

Verwenden, wenn Travel Context, relevante Evidence-Artefakte und – soweit Preis/Buchbarkeit materiell sind – ein aktueller Availability Snapshot vorliegen.

## Ablauf

### 1. Identity and Feasibility Gate

Prüfe, ob Destination, Transport, Stay und Offers korrekt referenziert und zeitlich kompatibel sind. Materielle Identitäts- oder Datumsunsicherheit führt zu `CONDITIONAL` oder `UNKNOWN`.

### 2. Hard Requirement Gate

Bewerte jedes bestätigte Must-have als `PASS | CONDITIONAL | FAIL | UNKNOWN`. Ein `FAIL`-Kandidat kann nie Gewinner sein.

### 3. Evidence Sufficiency

Halte `evidenceCoverage` getrennt von Attraktivität. Fehlende Evidenz wird weder als Null noch als Mittelwert imputiert.

### 4. Criterion Scores

Bewerte nur Kriterien mit nachvollziehbarer Basis. Gewichte werden nur verwendet, wenn sie bestätigt sind und auf Summe 1.0 normalisiert vorliegen bzw. explizit bestätigt normalisiert werden dürfen.

### 5. Utility und Kosten

Berechne Nutzwert transparent. Ein hartes Maximalbudget ist Gate; ein Zielbudget kann als Kriterium/Trade-off behandelt werden. Der billigste Reiseplan ist nicht automatisch der beste.

### 6. Winner Classes

Mindestens zulässige Labels:

- `best-fit`,
- `best-value`,
- `most-comfortable`,
- `most-flexible`,
- `lowest-travel-burden`.

Winner-Collisions sind zulässig.

### 7. Sensitivity

Bei gewichteten Rankings plausible Gewichtsänderungen bzw. Near Ties sichtbar machen. Ein instabiler Sieger erhält keine hohe Ranking Confidence.

## Output Contract

`travel-ranking.json` enthält mindestens:

- `schemaVersion`, `tripId`, `asOf`,
- `rankingConfidence`,
- `winners`,
- `rankedOptions`,
- `excludedOptions`,
- `sensitivity`,
- `materialUnknowns`, `limitations`.

Jede gerankte Option enthält Referenzen auf Destination, Transport, Stay und relevante Offers, Gate-Status, Criterion Scores, Kosten, Evidence Coverage, Labels sowie Hauptstärke/-schwäche.

## Prüfungen

Bestanden nur wenn:

- Hard Gates vor Scores laufen,
- `FAIL` niemals gewinnt,
- fehlende Evidenz nicht imputiert wird,
- bestätigte Gewichte nicht still verändert werden,
- Evidence Coverage und Utility getrennt bleiben,
- Preis allein keinen Winner erzeugt,
- Winner-Collisions zulässig bleiben,
- stale Availability keine aktuelle preisabhängige Winner-Aussage trägt.

## Fehlerbehandlung

Ohne bestätigte Gewichte qualitative Vergleichsmatrix statt erfundener Gesamtpunktzahl liefern. Ohne aktuelle Preise können Fit-/Comfort-Aussagen ggf. bestehen bleiben, während `best-value` unresolved ist. Materielle Unknowns begrenzen Winner-Posture.

## Übergabe

Normalpfad: `travel-itinerary-planner`.

## Abschlusskriterien

Abgeschlossen, wenn alle Optionen durch reproduzierbare Hard Gates gelaufen sind, Ranking und Confidence evidenzgebunden bleiben und die Shortlist genügend strukturiert ist, um daraus einen realistischen Reiseplan zu bauen.
