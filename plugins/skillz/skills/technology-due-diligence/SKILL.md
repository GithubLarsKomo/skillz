---
name: technology-due-diligence
description: Orchestriert evidenzbasierte Technology-Due-Diligence für Licensing, Partnership, Acquisition, Make/Buy, Supplier Selection oder Investment, entscheidet zuerst über benötigte Specialist Depth und priorisiert Red Flags, Unknowns und nächste sichere Aktionen ohne Fachlogik der Spezial-Skills zu duplizieren.
---

# Technology Due Diligence

## Zweck und Grenze

Orchestriere eine entscheidungsorientierte Technology Due Diligence aus bestehenden oder bei Bedarf erzeugten Spezialbewertungen. Der Skill führt Ergebnisse zusammen, priorisiert Cross-Domain-Red-Flags und Unknowns und erzeugt eine sichere nächste Aktion.

Der Orchestrator enthält **keine eigene Patent-, Claim-, Regulatory- oder Supplier-Quality-Fachlogik**. Er delegiert diese Domänen und darf deren Unsicherheit nicht durch einen künstlichen Score verdecken.

## Trigger

Verwenden bei Technology Due Diligence für Licensing, Partnership, Acquisition, Strategic Investment, Make/Buy oder Supplier Selection, wenn mehrere technische, IP-, Regulatory-, Supply/Scale- oder kommerzielle Aspekte zusammengeführt werden sollen.

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

### 2. Specialist-Routing-Gate

Klassifiziere jede Domäne vor einem Specialist-Aufruf als:

`REQUIRED | OPTIONAL | NOT_REQUIRED | ALREADY_AVAILABLE | BLOCKED`

Mindestens für:

- technology / offer,
- patent landscape,
- FTO,
- regulatory,
- supplier / quality,
- commercial / strategic.

Routing-Regeln:

- frühes Technology Scouting ohne konkrete Commercialization-Entscheidung → FTO normalerweise `NOT_REQUIRED` oder `OPTIONAL`,
- Licensing/Acquisition mit konkretem Produkt und Zielmärkten vor Commercialization → FTO typischerweise `REQUIRED`,
- vorhandene belastbare Counsel-/Regulatory-/Supplier-Outputs → `ALREADY_AVAILABLE` und konsumieren statt erneut analysieren,
- Supplier Selection ohne relevante proprietäre IP-Trigger → Patent Landscape/FTO nicht automatisch starten,
- Make/Buy vor Architektur-Freeze → Claim-by-Claim-FTO kann verfrüht sein und bleibt ggf. `OPTIONAL` oder `BLOCKED` bis eine stabile Baseline existiert.

Nicht anwendbare Domänen werden als `NOT_REQUIRED` dokumentiert; fehlende Domains dürfen nicht künstlich mit Findings gefüllt werden.

### 3. Specialist Assessments koordinieren

Je nach Routing Gate:

- Technology/Offer Fit → `technology-offer-assessment`,
- Patent Landscape → `patent-landscape-analysis`,
- konkretes FTO Screening → `freedom-to-operate-assessment`,
- Regulatory für IVD/Medical Device → bestehende Regulatory-Specialist-Skills,
- Supplier/Quality/Scale → `supplier-quality-medical-device` und passende QMS-/Validation-Skills,
- komplexe begrenzte Investigationen → `large-work-wayfinder` nur bei Bedarf.

**Specialist Evidence statt Zweitanalyse:** Der Orchestrator konsumiert vorhandene strukturierte Outputs und reproduziert keine Claim Charts, Classification oder Supplier Qualification.

### 4. Cross-Domain Dependencies modellieren

Verbinde technische Designentscheidungen mit FTO, Regulatory, Manufacturing, Supply und Commercial Model. Beispiele: ein Design-around kann Performance und Regulatory Evidence ändern; ein proprietäres Reagenz kann IP-, Supplier- und Cost-Risk koppeln.

### 5. Anwendbare Decision Dimensions konsolidieren

Bewerte nur anwendbare Dimensionen und markiere andere als `not-applicable`:

- technical differentiation,
- performance evidence,
- maturity/transferability,
- integration burden,
- manufacturing/scale/supply risk,
- regulatory feasibility/readiness,
- patent position / landscape density,
- FTO screening concern,
- licensing dependencies,
- commercial model / cost structure,
- strategic fit / lock-in,
- critical unknowns.

Keine Gesamtpunktzahl erfinden, wenn die Gewichtung nicht bestätigt ist.

### 6. Red Flags und Unknowns priorisieren

Jeder Red Flag Record enthält `issue`, `domain`, `evidence`, `confidence`, `impact`, `reversibility`, `decisionTiming`, `owner/authority`, `nextEvidence` und `stopCondition`.

**Kritische Unknowns nicht in Scores verstecken.** Ein materieller FTO-Screening-Concern oder instabiler Regulatory Context kann eine positive technische Bewertung blockieren.

### 7. Investigations begrenzen

Nur wenn kritische Unsicherheit die nächste Entscheidung blockiert und eine mehrstufige Untersuchung nötig ist, übergib eine kleine Menge begrenzter Untersuchungen an `large-work-wayfinder`. Jede Investigation benötigt eine einzelne Frage, Evidence Need, Stop Condition und Nicht-Ziele.

Für einfache DDs ohne solche offenen Investigationen wird Wayfinder **nicht** aufgerufen.

### 8. Decision Posture mit Preconditions formulieren

Der Orchestrator trifft keine Board-/Management-/Legal-/Regulatory-Entscheidung. Er erzeugt stattdessen:

- `decisionPosture.status`: `supportable | supportable-with-preconditions | not-yet-supportable | evidence-insufficient | material-blocker-identified`,
- `decisionOwner`,
- `authorityRequired`,
- `decisionDrivers[]`,
- `preconditions[]`,
- `materialBlockers[]`,
- `stopConditions[]`,
- `nextSafeAction`.

## Output-Verträge

`technology-due-diligence.json` enthält:

```json
{
  "scope": {},
  "decisionContext": {},
  "asOf": "YYYY-MM-DD",
  "domainRouting": [],
  "specialistAssessments": [],
  "crossDomainDependencies": [],
  "redFlags": [],
  "unknowns": [],
  "decisionDrivers": [],
  "options": [],
  "preconditions": [],
  "decisionPosture": {}
}
```

`due-diligence-handoff.json` ist Wayfinder-kompatibel und enthält mindestens `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks, nextSafeAction`. Es wird auch dann erzeugt, wenn keine Wayfinder-Investigation nötig ist.

`technology-due-diligence.md` ist das Executive Assessment mit Scope, Domain Routing, Kernbefunden, Red Flags, Preconditions, Decision Posture und nächster sicherer Aktion.

## IVD-Komposition

Bei IVD-/MedTech-Fällen können Referenzszenarien wie Autoantikörpertests, Anti-Nephrin oder pTau217 die Komposition testen. Der Orchestrator selbst speichert keine anbieter- oder projektspezifischen Geheimnisse und enthält keine assay-spezifische Fachlogik.

## Legal-/Regulatory-Grenzen

FTO bleibt technische Vorprüfung und Counsel-Eskalation; Regulatory Readiness bleibt Specialist Assessment. Der Orchestrator darf keine entsprechende Rechts- oder Behördenfreigabe simulieren.

## Memory Path

Persistenzwürdig sind generische DD-Dimensionen, Routing-Regeln, Handoff-Schema und abstrahierte Cross-Domain-Abhängigkeiten. Konkrete Transaktionsdaten, Preise, vertrauliche Target-Daten, Patentstatus, Legal Advice und Entscheidungsfristen bleiben run-only oder kontrolliert projektgebunden.

## Qualitätsgate

Pass nur wenn:

- jede relevante Domäne vor Aufruf durch das Routing Gate klassifiziert wurde,
- keine eigene Patent-, Claim-, Regulatory- oder Supplier-Quality-Fachlogik dupliziert wird,
- `ALREADY_AVAILABLE`-Outputs konsumiert statt erneut erzeugt werden,
- `NOT_REQUIRED` nicht künstlich analysiert wird,
- `large-work-wayfinder` nur bei tatsächlich komplexen Investigationen aufgerufen wird,
- Specialist Ergebnisse auf deren Evidence zurückgeführt werden,
- kritische Unknowns nicht in Scores versteckt werden,
- volatile Inputs `asOf` besitzen,
- Decision Posture statt autoritativem Go/No-Go verwendet wird,
- `nextSafeAction` ohne versteckte Fachannahmen ausführbar ist.

## Fehlerbehandlung

Wenn ein `REQUIRED` Specialist Assessment fehlt oder `BLOCKED` ist, darf der Orchestrator dessen Fachresultat nicht erfinden. Er markiert den Domain-Status entsprechend und setzt den Decision Posture auf `not-yet-supportable` oder `evidence-insufficient`, sofern die Lücke entscheidungsrelevant ist.

Ein pauschaler Score, der technische Stärke und materielle FTO-/Regulatory-Unknowns mittelt, ist ein Qualitätsfehler.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Domain Routing explizit, vorhandene Specialist Assessments wiederverwendet, nur erforderliche neue Assessments angestoßen, Cross-Domain-Abhängigkeiten sichtbar, Red Flags priorisiert, Decision Posture und Preconditions explizit und genau eine nächste sichere Aktion definiert sind.
