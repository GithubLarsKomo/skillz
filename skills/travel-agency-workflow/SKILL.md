---
name: travel-agency-workflow
description: Orchestriert private Reisen von geklärten Anforderungen über Ziel-, Transport- und Unterkunftsrecherche sowie aktuelle Verfügbarkeit bis zu Ranking und zeitlich-räumlich geprüftem Reiseplan.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
discoverability: public
owners:
  - GithubLarsKomo
requires:
  - travel-context-builder
  - travel-destination-research
  - travel-transport-research
  - travel-stay-research
  - travel-availability-snapshot
  - travel-option-ranking
  - travel-itinerary-planner
outputs:
  - travel-plan.json
  - travel-plan.md
  - travel-shortlist.json
lastEvaluated: 2026-08-30
---
# Travel Agency Workflow

## Zweck und Grenze

Der user-facing Travel-Orchestrator führt private Reiseaufträge von ausreichend geklärten Anforderungen über Evidence Research, aktuelle Marktverfügbarkeit, transparentes Ranking und einen zeitlich-räumlich plausiblen Reiseplan.

Der Orchestrator dupliziert keine Worker-Logik. Er besitzt nur die finale Reiseempfehlung und Shortlist, nicht die kanonischen Worker-Artefakte.

Kostenpflichtige oder anderweitig verbindliche Buchungsaktionen sind eine eigene Commit-Grenze und benötigen explizite Nutzerautorisierung.

## Trigger

Typische Trigger:

- „Plane mir zehn Tage Japan.“
- „Wo könnten wir im Oktober für eine Woche hin?“
- „Finde Flug, Hotel und Mietwagen und vergleiche sinnvolle Optionen.“
- „Prüfe meine bereits gebuchte Reise und baue einen realistischen Ablauf.“
- „Sind für meine Shortlist inzwischen bessere Reiseangebote verfügbar?“

## Modus

Klassifiziere früh als:

- `destination-discovery`,
- `trip-planning`,
- `trip-operations`.

## Ablauf

### 1. Requirement Sufficiency Gate

Prüfe, ob Reisende, Zeitrahmen, Zielstatus und für die konkrete Entscheidung materielle Constraints ausreichend klar sind.

Fehlende fachliche Präferenz- oder Scope-Entscheidung → `round-based-requirements-grilling`.

Bereits beantwortete Fragen nicht erneut stellen. Der Orchestrator erfindet weder Budget noch Gewichte oder No-gos.

### 2. Travel Context

→ `travel-context-builder`

Alle Downstream-Worker referenzieren denselben kanonischen Context.

### 3. Destination Evidence

→ `travel-destination-research`

Bei fixem Ziel kann der Scope auf Ziel-/Saison-/Praktikabilitätsevidenz begrenzt werden.

### 4. Transport und Stay Research

→ `travel-transport-research`  
→ `travel-stay-research`

Beide dürfen parallel arbeiten, soweit ihre Inputs feststehen.

### 5. Current Availability

→ `travel-availability-snapshot`

Stabile Reiseevidenz und volatile aktuelle Offers bleiben getrennt. Jede als aktuell dargestellte Preis-/Verfügbarkeitsaussage trägt `capturedAt`.

### 6. Ranking

→ `travel-option-ranking`

Hard Gates vor Scores. Evidence Coverage, Kosten und Ranking Confidence bleiben getrennte Dimensionen.

### 7. Itinerary

→ `travel-itinerary-planner`

Der Reiseplan muss räumliche und zeitliche Machbarkeit, Transfers, Puffer und verifizierte/ungeprüfte Constraints sichtbar halten.

### 8. Synthese

Erzeuge:

- `travel-plan.json`,
- `travel-plan.md`,
- `travel-shortlist.json`.

Die Synthese referenziert Worker-Artefakte, kopiert deren Ownership aber nicht.

### 9. SEARCH → RECOMMEND → COMMIT

`SEARCH`: Recherche darf autonom erfolgen.  
`RECOMMEND`: Empfehlung darf der Workflow erzeugen.  
`COMMIT`: kostenpflichtige, nicht stornierbare oder anderweitig verbindliche Buchung nur nach expliziter Nutzerautorisierung.

### 10. Refresh

Bei späteren Preis-/Verfügbarkeitsfragen normalerweise nur:

`travel-availability-snapshot → travel-option-ranking → travel-agency-workflow`.

Evidence Research wird nur wiederholt, wenn neue Ziele, neue Routen, materielle Property-/Schedule-Änderungen oder veraltete zentrale Evidenz dies rechtfertigen.

## Output Contract

`travel-plan.json` enthält mindestens:

- `schemaVersion`, `tripId`, `asOf`,
- `mode`, `recommendationStatus`,
- `recommendedOption`, `winners`, `shortlist`,
- `itineraryRef`,
- `currentOfferRefs`,
- `decisionDrivers`,
- `materialUnknowns`,
- `limitations`,
- `commitGate`.

`travel-shortlist.json` enthält die kompakte Kandidatenbasis für spätere Availability Refreshes.

## Prüfungen

Bestanden nur wenn:

- unvollständige Requirements korrekt an Grilling geroutet werden,
- Worker-Reasoning nicht im Orchestrator dupliziert wird,
- stabile Evidence und aktuelle Availability getrennt bleiben,
- aktuelle Preise zeitgestempelt sind,
- Hard Gates vor Ranking laufen,
- billigste Option nicht automatisch gewinnt,
- der Itinerary-Worker vor finaler Reiseplanbehauptung zeitliche/räumliche Machbarkeit prüft,
- keine Commit-Aktion ohne explizite Nutzerfreigabe erfolgt.

## Fehlerbehandlung

Mögliche Statuswerte:

`supportable | supportable-with-caveats | requirements-incomplete | evidence-insufficient | market-data-insufficient | itinerary-conflict | commit-authorization-required`.

Bei partiellen Provider-Ausfällen eine begrenzte Empfehlung mit sichtbaren Lücken liefern statt Preise oder Verfügbarkeiten zu erfinden.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn eine Reise aus bestätigten Anforderungen nachvollziehbar geplant, gegen aktuelle relevante Offers geprüft, transparent verglichen und in einen realistischen Itinerary überführt wurde oder mit eindeutigem Status an Grilling, Nachrecherche oder Nutzerautorisierung zurückgegeben wird.
