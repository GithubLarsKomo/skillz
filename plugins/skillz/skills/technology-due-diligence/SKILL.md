---
name: technology-due-diligence
description: Orchestriert evidenzbasierte Technology-Due-Diligence für Licensing, Partnership, Acquisition oder Make/Buy aus Offer/Technology Assessment, Patent Landscape, technischer FTO-Vorprüfung und optionalen Regulatory-/Supplier-Spezialbewertungen; priorisiert Red Flags, Unknowns, Entscheidungstreiber und nächste sichere Aktionen ohne Fachlogik der Spezial-Skills zu duplizieren.
---

# Technology Due Diligence

## Zweck und Grenze

Orchestriere eine entscheidungsorientierte Technology/IP/Offer-Due-Diligence aus bestehenden Spezialbewertungen. Der Skill führt Ergebnisse zusammen, priorisiert Cross-Domain-Red-Flags und Unknowns und erzeugt eine sichere nächste Aktion.

Der Orchestrator enthält **keine eigene Patent-, Claim-, Regulatory- oder Supplier-Quality-Fachlogik**. Er delegiert diese Domänen und darf deren Unsicherheit nicht durch einen künstlichen Score verdecken.

## Trigger

Verwenden bei Technology Due Diligence für Licensing, Partnership, Acquisition, Strategic Investment, Make/Buy oder Supplier Selection, wenn technische Eignung, IP/FTO, Regulatory, Supply/Scale und kommerzielle Readiness zusammengeführt werden sollen.

## Decision Context

Vor Orchestrierung mindestens erfassen:

- `decisionType`: `license | partnership | acquisition | make-buy | supplier-selection | strategic-investment | other`,
- Target Technology/Product und Intended Use,
- Commercial Objective,
- Target Markets/Jurisdictions,
- Decision Stage/Deadline soweit bekannt,
- Must-have Criteria,
- explizite Risk Appetite / irreversible Decisions soweit vorhanden,
- `asOf` für volatile Inputs.

Keine nicht bestätigte Gewichtung oder Risikoneigung erfinden.

## Workflow

### 1. Scope, Hypothesen und Unknowns fixieren

Trenne Facts, Assumptions, Hypotheses, Unknowns, Blockers und bereits autorisierte Decisions. Definiere die kleinste Due-Diligence-Frage, die für die aktuelle Entscheidung beantwortet werden muss.

### 2. Specialist Assessments koordinieren

- Technology/Offer Fit → `technology-offer-assessment`
- Patent Landscape → `patent-landscape-analysis`
- konkretes FTO Screening → `freedom-to-operate-assessment`
- Regulatory für IVD/Medical Device → bestehende Regulatory-Specialist-Skills
- Supplier/Quality/Scale → `supplier-quality-medical-device` und passende QMS-/Validation-Skills

**Specialist Evidence statt Zweitanalyse:** Der Orchestrator konsumiert die strukturierten Outputs und reproduziert keine Claim Charts, Classification oder Supplier Qualification.

### 3. Cross-Domain Dependencies modellieren

Verbinde technische Designentscheidungen mit FTO, Regulatory, Manufacturing, Supply und Commercial Model. Beispiele: ein Design-around kann Performance und Regulatory Evidence ändern; ein proprietäres Reagenz kann IP-, Supplier- und Cost-Risk koppeln.

### 4. Gemeinsame Decision Dimensions konsolidieren

Mindestens:

- technical differentiation,
- performance evidence,
- maturity/transferability,
- integration burden,
- manufacturing/scale/supply risk,
- regulatory feasibility/readiness,
- patent position / landscape density,
- FTO screening risk,
- licensing dependencies,
- commercial model / cost structure,
- strategic fit / lock-in,
- critical unknowns.

Keine Gesamtpunktzahl erfinden, wenn die Gewichtung nicht bestätigt ist.

### 5. Red Flags und Unknowns priorisieren

Jeder Red Flag Record enthält `issue`, `domain`, `evidence`, `confidence`, `impact`, `reversibility`, `decisionTiming`, `owner/authority`, `nextEvidence` und `stopCondition`.

**Kritische Unknowns nicht in Scores verstecken.** Ein materielles RED/AMBER-FTO oder instabiler Regulatory Context kann eine positive technische Bewertung blockieren.

### 6. Investigations begrenzen

Wenn kritische Unsicherheit die nächste Entscheidung blockiert, übergib eine kleine Menge begrenzter Untersuchungen an `large-work-wayfinder`. Jede Investigation benötigt eine einzelne Frage, Evidence Need, Stop Condition und Nicht-Ziele.

### 7. Recommendation mit Preconditions formulieren

Recommendation kann z. B. `go | conditional-go | hold | no-go | insufficient-evidence` sein, muss aber Decision Drivers, Preconditions, Autoritätsgrenzen und Abbruchkriterien nennen. Der Skill simuliert keine Board-, Legal-, Regulatory- oder Investment-Committee-Freigabe.

## Output-Verträge

`technology-due-diligence.json` enthält:

```json
{
  "scope": {},
  "decisionContext": {},
  "asOf": "YYYY-MM-DD",
  "specialistAssessments": [],
  "crossDomainDependencies": [],
  "redFlags": [],
  "unknowns": [],
  "decisionDrivers": [],
  "options": [],
  "preconditions": [],
  "recommendation": {}
}
```

`due-diligence-handoff.json` ist Wayfinder-kompatibel und enthält mindestens `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks, nextSafeAction`.

`technology-due-diligence.md` ist das Executive Assessment mit Scope, Kernbefunden, Domain-Status, Red Flags, Preconditions und nächster sicherer Aktion.

## IVD-Komposition

Bei IVD-/MedTech-Fällen können Referenzszenarien wie Autoantikörpertests, Anti-Nephrin oder pTau217 die Komposition testen. Der Orchestrator selbst speichert keine anbieter- oder projektspezifischen Geheimnisse und enthält keine assay-spezifische Fachlogik.

## Legal-/Regulatory-Grenzen

FTO bleibt technische Vorprüfung und Counsel-Eskalation; Regulatory Readiness bleibt Specialist Assessment. Der Orchestrator darf weder „IP safe“ noch „regulatory approved“ behaupten, wenn diese Aussage nicht durch zuständige Evidenz/Autorität belegt ist.

## Memory Path

Persistenzwürdig sind generische DD-Dimensionen, Handoff-Schema und abstrahierte Cross-Domain-Abhängigkeiten. Konkrete Transaktionsdaten, Preise, vertrauliche Target-Daten, Patentstatus, Legal Advice und Entscheidungsfristen bleiben run-only oder kontrolliert projektgebunden.

## Qualitätsgate

Pass nur wenn:

- **keine eigene Patent-, Claim-, Regulatory- oder Supplier-Quality-Fachlogik** dupliziert wird,
- Specialist Ergebnisse auf deren Evidence zurückgeführt werden,
- **Kritische Unknowns nicht in Scores verstecken** eingehalten wird,
- FTO als Screening und nicht als Legal Opinion behandelt wird,
- volatile Inputs `asOf` besitzen,
- Recommendation Preconditions und Stop Conditions enthält,
- `nextSafeAction` ohne versteckte Fachannahmen ausführbar ist.

## Fehlerbehandlung

Wenn Specialist Assessments fehlen, darf der Orchestrator deren Fachresultat nicht erfinden. Er markiert den Domain-Status als `unknown/not-assessed`, erzeugt bei Entscheidungsrelevanz eine begrenzte Investigation und stoppt vor einer scheinpräzisen Gesamtbewertung.

Ein pauschaler Score wie `82/100`, der technische Stärke, FTO-RED und regulatorische Unsicherheit mittelt, ist ein Qualitätsfehler.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Specialist Assessments sauber koordiniert, Cross-Domain-Abhängigkeiten und kritische Unsicherheiten sichtbar, Red Flags priorisiert, Recommendation und Preconditions explizit und genau eine nächste sichere Aktion definiert sind.
