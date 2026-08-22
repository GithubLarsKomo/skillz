---
name: purchase-decision-planner
description: Orchestriert private und berufliche Kaufentscheidungen von Anforderungen über Evidenz und Preise bis zur nachvollziehbaren Empfehlung.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - product-evidence-research
  - price-availability-snapshot
  - product-comparison-ranking
outputs:
  - purchase-plan.json
  - purchase-plan.md
  - purchase-shortlist.json
lastEvaluated: 2026-08-22
---

# Purchase Decision Planner

## Zweck und Grenze

Der user-facing **Investitionsplaner** orchestriert evidenzbasierte Entscheidungen über physische Produkte, Ausstattung, Geräte, Systeme und vergleichbare beschaffbare Assets im privaten und beruflichen Kontext.

Er koordiniert Requirements-Grilling, Produktrecherche, Evidence Synthesis, aktuelle Preise und deterministisches Ranking. Komplexe professionelle Technologie-, Vendor- oder Due-Diligence-Fragen werden an bestehende Specialist Skills geroutet, nicht hier dupliziert.

**Nicht im Scope:** Aktien, ETFs, Anleihen, Krypto, Portfolioallokation oder sonstige **Finanzanlageberatung**.

## Trigger

Typische Trigger:

- „Welches Fahrrad / Notebook / Kamera / Werkzeug soll ich kaufen?“
- „Finde Qualitätssieger, Preis-/Leistungssieger und Schnäppchen.“
- „Vergleiche diese Geräte und nenne Bezugsquellen mit aktuellen Preisen.“
- „Wir müssen beruflich ein Gerät/System beschaffen und verschiedene Anbieter bewerten.“
- „Erstelle einen Investitionsplan für diese Anschaffung.“

Ein nacktes „bestes Produkt“ ohne ausreichenden Entscheidungskontext löst zuerst Grilling aus.

## Voraussetzungen

Der Orchestrator konsumiert soweit vorhanden bestätigte Requirements aus `round-based-requirements-grilling`, `product-evidence-set.json`, `price-snapshot.json`, `product-ranking.json` und bestehende Specialist Assessments bei professionellen Fällen.

Er darf fehlende Präferenzen, harte Budgetgrenzen oder Gewichte nicht erfinden.

## Ablauf

### 1. Requirement Sufficiency Gate

Prüfe, ob Produktkategorie, Intended Use, Markt, Must-haves, Budgetstatus und wesentliche Trade-offs ausreichend klar sind. Fehlende fachliche Entscheidung → `round-based-requirements-grilling`. Bereits beantwortete Fragen werden nicht erneut gestellt.

### 2. Modus bestimmen

Ordne den Fall ein als `private`, `professional-standard` oder `professional-complex-technology`.

`professional-complex-technology` ist angezeigt, wenn materielle Themen wie proprietäre Technologie, schwierige Integration, Validation/Regulatory, Scale/Supply, Licensing, Vendor Lock-in, strategisches Make/Buy oder hohe Switching Burden die normale Produktbeschaffung überschreiten.

### 3. Evidence Research ausführen

→ `product-evidence-research`

Dieser Skill verwendet die Evidence-Semantik von `research-to-evidence-note` und liefert normalisierte Kandidaten, Claims, Konflikte und Coverage.

### 4. Preis-/Verfügbarkeitssnapshot erzeugen

→ `price-availability-snapshot`

Detailpreise werden vorzugsweise erst nach Evidenzreduktion abgefragt. Jeder aktuelle Preis ist variantengenau und zeitgestempelt.

### 5. Vergleich und Winner berechnen

→ `product-comparison-ranking`

Hard Gates precede scores. **Quality Winner**, **Price/Performance Winner** und Bargain werden separat bestimmt; Winner-Collisions sind zulässig. Die finale Shortlist enthält **maximal zehn** Kandidaten.

### 6. Professional Escalation Gate

Bei `professional-standard` bleiben TCO, Service, Lifecycle und Procurement im normalen Plan, soweit ausreichend.

Bei `professional-complex-technology`:

- konkrete Vendor-/Plattformofferten → `technology-offer-assessment`,
- Licensing, Acquisition, Strategic Investment, komplexes Make/Buy oder cross-domain DD → `technology-due-diligence`,
- technische Unsicherheit, die Spezifikation/Entscheidung blockiert → `large-work-wayfinder`,
- material akzeptierte Entscheidung mit Traceability-Bedarf → optional `decision-record`.

### 7. Empfehlung synthetisieren

Gib mindestens Quality Winner, Price/Performance Winner, Bargain, bis zu zehn Kandidaten, Hauptstärke und Hauptschwäche, Evidence Coverage / Ranking Confidence, aktuelle Bezugsquellen und Preise soweit verfügbar, materielle Unknowns und bei Bedarf ausgeschlossene Kandidaten mit Must-have-Fail aus.

### 8. Price Refresh ermöglichen

Eine spätere Frage wie „Sind die Preise inzwischen besser?“ soll normalerweise nur `price-availability-snapshot` → `product-comparison-ranking` → Planner erneut ausführen.

Evidence Research wird nur erneuert, wenn neue Generationen, materielle Firmwareänderungen, neue unabhängige Evidenz, Discontinuation oder veraltete zentrale Evidenz dies rechtfertigen.

## Prüfungen

Pass nur wenn unklare fachliche Requirements zu Grilling geroutet wurden; Quellenresearch und Ranking nicht im Orchestrator dupliziert werden; alle Gewinner Hard Gates respektieren; Evidence Coverage und Ranking Score getrennt sichtbar sind; aktuelle Preise `asOf/capturedAt` tragen; maximal zehn finale Kandidaten gezeigt werden; fehlende Preise nicht erfunden werden; Quality, Price/Performance und Bargain nicht künstlich auf verschiedene Produkte verteilt werden; komplexe professionelle Fälle korrekt eskalieren und Finanzanlagefragen nicht durch diesen Skill beantwortet werden.

## Fehlerbehandlung

Statuswerte: `supportable | supportable-with-caveats | evidence-insufficient | requirements-incomplete | market-data-insufficient | professional-escalation-required`.

Wenn Preisquellen ausfallen, kann eine Qualitätsbewertung supportable bleiben, während preisabhängige Winner unresolved sind. Wenn zentrale Evidenz fehlt, nenne die konkrete Lücke statt einen definitiven Sieger zu erfinden.

## Übergabe

Erzeuge `purchase-plan.json`, `purchase-plan.md` und `purchase-shortlist.json`.

`purchase-plan.json` enthält mindestens `schemaVersion`, `asOf`, `decisionContext`, `recommendationStatus`, `winners`, `shortlist`, `purchaseSources`, `decisionDrivers`, `materialUnknowns`, `limitations` und `routing.professionalEscalation`.

`purchase-shortlist.json` enthält die kompakte Kandidaten-/SKU-Basis für spätere Price Refreshes.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn ein ausreichend geklärter privater oder beruflicher Beschaffungsfall bis zu einer nachvollziehbaren, quellen- und preisgestützten Empfehlung geführt oder mit eindeutigem Grund in den korrekten Specialist Path geroutet wurde, ohne Finanzanlageberatung, erfundene Gewichte, erfundene Preise oder duplizierte Specialist-Logik.
