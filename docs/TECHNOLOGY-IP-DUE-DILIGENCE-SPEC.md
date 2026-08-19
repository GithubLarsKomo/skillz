# Technology & IP Due Diligence Skill Cluster — Specification

## Ziel

Diese Spezifikation definiert vier kleine, komponierbare Skills für wiederkehrende Technology-/Offer-/IP-/FTO-Due-Diligence-Aufgaben. Sie ergänzt bestehende Research-, Regulatory-, Supplier-Quality- und Wayfinder-Capabilities, ohne deren Fachlogik zu duplizieren.

Die vier Skills sind:

1. `technology-offer-assessment`
2. `patent-landscape-analysis`
3. `freedom-to-operate-assessment`
4. `technology-due-diligence`

Der Cluster ist insbesondere für technologieintensive IVD-/MedTech-Szenarien geeignet, bleibt aber soweit möglich domänenneutral. Medical-Device-/IVD-spezifische Regulatory- und Supplier-Fragen werden an bestehende Spezial-Skills geroutet.

---

## Architekturprinzipien

### Ein Skill = eine primäre Aufgabe

- `technology-offer-assessment` bewertet eine konkrete Technologieofferte oder mehrere vergleichbare Offerten.
- `patent-landscape-analysis` strukturiert die relevante Schutzrechtslandschaft.
- `freedom-to-operate-assessment` mappt eine definierte Produkt-/Prozesskonfiguration gegen aktive Patentansprüche in Zieljurisdiktionen als technische FTO-Vorprüfung.
- `technology-due-diligence` orchestriert die Fach-Skills zu einer entscheidungsorientierten Gesamtbewertung.

Der Orchestrator enthält keine eigene Patent-, Claim-, Regulatory- oder Supplier-Quality-Fachlogik.

### Evidence first

Alle entscheidungsrelevanten Aussagen müssen auf zugängliche Quellen oder explizit markierte Nutzer-/Projektangaben zurückgeführt werden. `research-to-evidence-note` ist die gemeinsame Evidenzbasis für externe Recherche.

### Zeit- und Jurisdiktionsbezug

Patentstatus, Patentfamilien, Pending Applications, Assignments, Oppositions, Term/Expiry, Regulatory Status, Preise und Lieferbedingungen sind volatil. Relevante Ergebnisse benötigen `asOf` sowie einen expliziten geografischen bzw. juristischen Scope.

### Keine simulierte Rechtsberatung

Der Cluster darf technische und evidenzbasierte Patent-/FTO-Screenings erzeugen, aber keine anwaltliche FTO Opinion, keine verbindliche Claim Construction, keine Aussage wie „infringes“, „does not infringe“, „valid“, „invalid“ oder „enforceable“ als abschließendes Rechtsurteil.

Wenn ein potenzieller Claim Read-on für ein wirtschaftlich relevantes Produkt in einer Zieljurisdiktion identifiziert wird, muss der Skill klar an qualifizierten Patent Counsel eskalieren.

---

# 1. `technology-offer-assessment`

## Skill-Grenze

Dieser Skill verwandelt eine oder mehrere konkrete Technologieofferten zusammen mit Zielanforderungen und zugänglicher Evidenz in eine nachvollziehbare technische, operative und kommerzielle Bewertungsmatrix und endet, wenn Claims, Evidenz, Red Flags, offene Fragen und Entscheidungstreiber explizit sind.

## Trigger

Verwenden bei Formulierungen wie:

- „Analysiere diese Offerte / dieses Angebot / diesen One-Pager / Pitch Deck.“
- „Vergleiche Anbieter A und B technisch und wirtschaftlich.“
- „Ist diese Plattform für unseren Assay / Workflow geeignet?“
- „Welche Red Flags und offenen Fragen hat dieses Technologieangebot?“

Nicht verwenden für reine Supplier-QMS-Qualifizierung, Vertragsauslegung, reine Marktanalyse oder reine Patentrecherche.

## Vorgeschlagenes Frontmatter

```yaml
name: technology-offer-assessment
description: Bewertet konkrete Technologieofferten oder vergleichbare Anbieterangebote evidenzbasiert auf technischen Fit, Reifegrad, Performance Claims, Integration, Skalierung, Supply/Quality, kommerzielle Bedingungen, IP-Abhängigkeiten, Red Flags und offene Fragen; keine Vertragsrechts- oder FTO-Analyse.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - research-to-evidence-note
outputs:
  - technology-offer-assessment.json
  - technology-offer-assessment.md
  - technology-offer-gap-set.json
```

## Bewertungsdimensionen

1. **Scope & intended use** — angebotene Technologie, Produktgrenzen, Zielanwendung, Sample/Workflow, Nutzeranforderungen.
2. **Claim inventory** — explizite technische, Performance-, Kosten-, Throughput-, Robustness-, Regulatory- und Scale Claims.
3. **Evidence quality** — direct/derived/unknown; Primärdaten vs. Marketing; unabhängige Replikation; Aktualität.
4. **Technical fit** — Messprinzip, Sensitivität, Dynamikbereich, Interferenzen, Multiplexing, Matrixkompatibilität, Automatisierbarkeit, Software/Data Integration.
5. **Maturity & validation** — Prototype/Pilot/production-relevant evidence; keine erfundene TRL-Zahl bei fehlender Evidenz.
6. **Operational fit** — Hardware, Consumables, Calibration/QC, Training, Maintenance, throughput, turnaround, failure modes.
7. **Scale & supply** — Fertigung, kritische Komponenten, Single Source, reproducibility, transferability, capacity evidence.
8. **Quality/regulatory hooks** — für Medical Device/IVD nur Screening und Routing; Detailanalyse an bestehende Skills.
9. **IP/licensing dependencies** — bekannte proprietäre Reagenzien, Software, Patente, Lizenzen, field-of-use restrictions; keine FTO-Schlussfolgerung.
10. **Commercial model** — CAPEX/OPEX, consumables, minimum volumes, license/royalty, service, switching cost, lock-in, assumptions.
11. **Strategic fit** — Differenzierung, internal capability gap, make/buy implications, reversibility.
12. **Red flags / questions** — nur entscheidungsrelevante Punkte.

## Routing

- belastbare externe Recherche → `research-to-evidence-note`
- Medical-Device-/IVD-Supplier-QMS → `supplier-quality-medical-device`
- Regulatory Strategy → `medical-device-regulatory-strategy` bzw. passende EU/FDA-Spezial-Skills
- fehlende Informationen des Anbieters → `external-stakeholder-questionnaire`
- IP/FTO-Vertiefung → `patent-landscape-analysis` / `freedom-to-operate-assessment`

## Output-Vertrag

`technology-offer-assessment.json` enthält mindestens:

- `scope`, `decisionContext`, `asOf`
- `offers[]`
- `requirements[]`
- `claims[]` mit Evidence-Referenzen
- `assessmentDimensions[]`
- `fit`: `strong | conditional | weak | unknown`
- `redFlags[]`
- `commercialAssumptions[]`
- `ipDependencies[]`
- `regulatoryRouting[]`
- `decisionDrivers[]`
- `recommendation` mit expliziten Preconditions

`technology-offer-gap-set.json` enthält offene technische, evidenzielle, regulatorische, IP-, kommerzielle und Supplier-Fragen mit Priorität und `decisionImpact`.

## Qualitätsgate

Pass nur wenn:

- Marketing Claims und bestätigte Evidenz getrennt sind,
- mehrere Angebote entlang identischer Kriterien verglichen werden,
- fehlende Daten als `unknown` statt positiv interpretiert werden,
- Preis-/Kostenannahmen zeitlich und mengenbezogen kenntlich sind,
- Regulatory-/Supplier-/IP-Fragen korrekt geroutet werden,
- keine Vertragsrechts- oder FTO-Opinion simuliert wird.

## Evaluation

### Happy Path

Zwei Anbieter bieten Biosensor-Plattformen für denselben IVD-Workflow an. Technische Spezifikationen, Pilotdaten und Preisannahmen liegen vor. Ergebnis: vergleichbare Matrix, evidenzbasierte Fit-Bewertung, Red Flags und priorisierte Anbieterfragen.

### Edge Case

Ein Anbieter behauptet sehr hohe analytische Sensitivität, liefert aber nur Marketinggrafiken und keine unabhängigen oder methodisch ausreichenden Daten. Ergebnis: Claim bleibt sichtbar, Evidence Confidence niedrig, Entscheidung wird an konkrete Verifikationsdaten geknüpft.

### Failure Case

Eine Offerte wird allein anhand der Broschüre als „marktreif, regulatorisch geeignet und IP-sicher“ bewertet. Der Skill muss diese Schlussfolgerung verwerfen und die drei Dimensionen getrennt behandeln.

---

# 2. `patent-landscape-analysis`

## Skill-Grenze

Dieser Skill verwandelt eine definierte Technologiefrage, Suchstrategie und zugängliche Patentquellen in eine deduplizierte, zeitbezogene Patentfamilienlandschaft und endet, wenn relevante Familien, Claim-Themen, Status, Jurisdiktionen, Suchabdeckung, Konflikte und offene Suchlücken nachvollziehbar dokumentiert sind.

## Trigger

- „Erstelle eine Patentlandschaft zu …“
- „Welche Patentfamilien und Assignees sind in diesem Feld relevant?“
- „Welche Schutzrechte decken diese Technologie / diesen Biomarker / dieses Assayprinzip ab?“
- „Zeige White Spaces, Prioritäten und relevante Familien.“

Nicht verwenden als Patentability Opinion, Prior-Art-Gutachten oder FTO-Schlussfolgerung.

## Vorgeschlagenes Frontmatter

```yaml
name: patent-landscape-analysis
description: Erstellt für eine abgegrenzte Technologiefrage eine evidenzbasierte, nach Patentfamilien deduplizierte Schutzrechtslandschaft mit Suchlogik, Prioritäten, Assignees, Jurisdiktionen, Legal-Status-Freshness und Independent-Claim-Themen; keine Patentability- oder FTO-Opinion.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - research-to-evidence-note
outputs:
  - patent-landscape.json
  - patent-landscape.md
  - patent-search-log.json
```

## Suchmodell

Die Suchstrategie kombiniert soweit relevant:

- Kernbegriffe und Synonyme,
- Biomarker-/Target-Namen und Aliasnamen,
- Mess-/Assayprinzipien,
- CPC/IPC-Klassen,
- Assignee/Applicant/Inventor,
- Citation chains,
- priority/continuation/divisional relationships,
- Familienmitglieder in Zieljurisdiktionen.

Die Suche muss iterativ dokumentiert werden. Ein einzelner Keyword Search darf nicht als vollständige Landschaft ausgegeben werden.

## Familienmodell

Pro Familie mindestens:

- `familyId`
- `representativePublication`
- `earliestPriority`
- `priorityApplications[]`
- `members[]`
- `assignees[]`
- `inventors[]`
- `jurisdictions[]`
- `legalStatus[]` mit `asOf` und Source
- `independentClaimThemes[]`
- `technologyTags[]`
- `relevance`: `core | adjacent | contextual | excluded`
- `relevanceRationale`
- `statusUncertainties[]`

Deduplizierung nach nachvollziehbarer Family-Definition; unterschiedliche Continuation-/Divisional-Claim-Scope-Pfade dürfen nicht durch grobe Familienbildung unsichtbar werden.

## Quellenhierarchie

Bevorzugt werden aktuelle offizielle Register bzw. Patentamtquellen für Status und bibliografische Daten. Aggregatoren können Discovery beschleunigen, ersetzen aber bei entscheidungsrelevantem Legal Status nicht die verifizierte Primärquelle.

## Claim-Themen

Der Skill darf Independent Claims semantisch thematisieren und relevante Claim-Elemente für nachgelagerte Analyse markieren. Er darf keine endgültige Claim Construction behaupten.

## Output-Vertrag

`patent-landscape.json` enthält Scope, asOf, Search Coverage, Families, Assignee Map, Technology Clusters, Jurisdiction Coverage, Status Uncertainties und Open Search Questions.

`patent-search-log.json` enthält Query, Quelle, Datum, Filter, Trefferzahl soweit verfügbar, Ein-/Ausschlusslogik und Iterationsgrund.

## Qualitätsgate

Pass nur wenn:

- Suchstrategie reproduzierbar dokumentiert ist,
- Familien nachvollziehbar dedupliziert sind,
- relevante Continuation-/Divisional-Strukturen nicht verschluckt werden,
- aktuelle Statusaussagen eine Freshness-/Source-Referenz besitzen,
- Patentfamilie und Claim Scope nicht gleichgesetzt werden,
- kein FTO-/Validity-/Patentability-Urteil simuliert wird.

## Evaluation

### Happy Path

Für ein diagnostisches Biomarker-/Assayfeld werden Keyword-, Classification-, Assignee- und Citation-Suchen kombiniert. Ergebnis: deduplizierte Kernfamilien, Claim-Themen, Status und dokumentierte Search Coverage.

### Edge Case

Eine Kernfamilie besitzt parallele US continuations und EP divisionals mit abweichenden Independent Claims. Ergebnis: gemeinsame Priorität bleibt sichtbar, unterschiedliche Claim-Scope-Pfade werden separat markiert.

### Failure Case

Ein Aggregator zeigt „active“, während das offizielle Register ein anderes Statusbild nahelegt. Der Skill darf den Aggregatorstatus nicht als endgültige Wahrheit übernehmen.

---

# 3. `freedom-to-operate-assessment`

## Skill-Grenze

Dieser Skill verwandelt eine klar definierte Produkt-/Prozesskonfiguration, Zieljurisdiktionen, Commercial Acts und relevante aktive/pending Patentansprüche in eine elementweise technische FTO-Screening-Heatmap und endet, wenn potenzielle Read-ons, fehlende Elemente, Statusunsicherheiten, Design-around-Hypothesen und Counsel-Eskalationen explizit sind.

## Trigger

- „Mach eine FTO-Analyse / FTO-Heatmap.“
- „Mappe dieses Produkt gegen Patentclaims.“
- „Welche Patentfamilien sind für die Vermarktung in EU/US kritisch?“
- „Welche Design-around-Optionen gibt es?“

## Vorgeschlagenes Frontmatter

```yaml
name: freedom-to-operate-assessment
description: Erstellt für eine definierte Produkt-/Prozesskonfiguration und Zieljurisdiktionen eine evidenzbasierte technische FTO-Vorprüfung mit Claim-by-Claim-Mapping, Legal-Status-Freshness, Screening-Risikokategorien, Unsicherheiten, Counsel-Eskalation und Design-around-Hypothesen; keine anwaltliche FTO Opinion oder verbindliche Claim Construction.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - research-to-evidence-note
  - patent-landscape-analysis
outputs:
  - fto-scope.json
  - fto-claim-map.json
  - fto-risk-heatmap.md
  - fto-design-around-options.json
```

## Voraussetzungen

Vor Claim-Mapping fixieren:

1. konkrete Produkt-/Assay-/Prozesskonfiguration,
2. wesentliche technische Merkmale,
3. Zieljurisdiktionen,
4. relevante wirtschaftliche Handlungen soweit bekannt (`make`, `use`, `sell`, `offer for sale`, `import` oder jurisdiktionsspezifische Entsprechungen),
5. `asOf`,
6. relevante Patentfamilien/Claims,
7. bekannte Lizenz-/Ownership-Informationen.

Eine FTO ohne konkrete Konfiguration oder Jurisdiktion bleibt unzulässig breit und muss als Scope Gap markiert werden.

## Claim-by-Claim-Modell

Pro relevantem Independent Claim:

- Claim-Identifier und Jurisdiktion
- verified current status / uncertainty
- decomposed required elements
- product/process feature evidence
- element mapping: `present | likely-present | absent | unknown | interpretation-dependent`
- mapping confidence
- source references
- dependent claims mit zusätzlicher Relevanz
- prosecution/claim-construction questions, wenn entscheidungsrelevant
- escalation flag

Der Skill verwendet bewusst `potential read-on` oder `screening concern`, nicht `infringement`.

## Screening-Risikokategorien

### RED — potential full read-on

Alle erforderlichen Elemente eines relevanten aktuell durchsetzbar erscheinenden Independent Claims sind auf Basis der verfügbaren technischen Evidenz `present`/`likely-present`; oder es fehlt nur eine claim-construction-relevante Auslegung. Zwingende Counsel-Eskalation.

### AMBER — material uncertainty

Plausible Überschneidung, aber Status, Claim Construction, Produktausprägung, Pending Claim Scope, Prosecution History oder ein technisches Element bleibt entscheidungsrelevant unklar.

### GREEN — no current full read-on identified

Mindestens ein erforderliches Element ist evidenzbasiert `absent`, oder der relevante Anspruch ist für die betrachtete Jurisdiktion verifiziert nicht mehr in Kraft. Dies ist ausdrücklich **keine globale FTO-Freigabe**.

### GREY — insufficient evidence

Scope, Produktkonfiguration, Status oder Claim-Text reicht für eine belastbare technische Vorprüfung nicht aus.

## Pending Applications

Pending Claims werden getrennt von erteilten Ansprüchen bewertet. Mögliche zukünftige Claim Scope darf nicht wie ein aktuelles Ausschließlichkeitsrecht behandelt werden, muss aber als strategisches Risiko sichtbar bleiben.

## Design-around

Design-around-Hypothesen müssen:

- auf konkrete notwendige Claim-Elemente zielen,
- technisch plausibel beschrieben sein,
- Performance-/Regulatory-/Manufacturing-Auswirkungen markieren,
- neue Patent-/FTO-Fragen ausweisen,
- keine Umgehung gesetzlicher Pflichten empfehlen.

## Output-Vertrag

`fto-scope.json`: Produktkonfiguration, Technical Feature Baseline, Jurisdiktionen, Commercial Acts, asOf, Exclusions, Assumptions.

`fto-claim-map.json`: Familien/Patente/Claims, Elementzerlegung, Feature Mapping, Status/Freshness, Evidence und Risk Category.

`fto-design-around-options.json`: Option, targeted claim element, technical change, feasibility, performance impact, regulatory impact, new-IP implications, validation needs.

## Counsel-Eskalation

Mandatory bei:

- RED,
- AMBER mit hoher kommerzieller Relevanz,
- unklarer Claim Construction,
- komplexer prosecution history,
- Doctrine-of-Equivalents-/Äquivalenzfragen,
- unklarer Ownership/License Chain,
- imminent launch / transaction closing.

## Qualitätsgate

Pass nur wenn:

- Scope/Jurisdiktion/asOf fixiert sind,
- relevante Claims elementweise statt nur thematisch gemappt werden,
- Status aktuell verifiziert oder ausdrücklich unsicher ist,
- Patentfamilie nicht mit einem einzigen Claim Scope gleichgesetzt wird,
- Pending und granted getrennt bleiben,
- `GREEN` nie als globale Non-Infringement-Freigabe formuliert wird,
- Counsel-Eskalationen sichtbar sind,
- Design-arounds an konkrete Claim-Elemente gebunden sind.

## Evaluation

### Happy Path

Ein diagnostischer Bluttest ist technisch detailliert beschrieben; US- und EP-Zielmarkt sind definiert; mehrere relevante Patentfamilien liegen vor. Ergebnis: Claim-by-Claim-Heatmap, RED/AMBER/GREEN/GREY, konkrete Design-around-Hypothesen und Counsel-Eskalation.

### Edge Case

Eine Familie ist in EP abgelaufen, besitzt aber eine laufende US continuation mit abweichenden Claims. Ergebnis: keine globale Familienbewertung; Jurisdiktion und Claim Scope bleiben getrennt.

### Failure Case

Der Skill schreibt „Produkt verletzt Patent X nicht“, weil ein Aggregator die Familie als expired zeigt. Diese Aussage muss verworfen werden; Status, Jurisdiktion, konkrete Claims und technische Elemente sind erneut zu prüfen.

---

# 4. `technology-due-diligence`

## Skill-Grenze

Dieser Skill verwandelt einen bestätigten Due-Diligence-Entscheidungskontext in einen priorisierten, evidenzbasierten Technology/IP/Offer-Due-Diligence-Status und endet, wenn Fach-Skills koordiniert, kritische Unsicherheiten sichtbar, Entscheidungstreiber priorisiert und nächste sichere Aktionen festgelegt sind.

## Trigger

- „Mach eine Technology Due Diligence zu Unternehmen/Plattform X.“
- „Bewerte diese Technologie für Licensing, Partnership, Acquisition oder Make/Buy.“
- „Führe Technik, IP/FTO, Regulatory, Supplier/Scale und Commercial Readiness zusammen.“
- „Erstelle ein Executive DD Assessment.“

## Vorgeschlagenes Frontmatter

```yaml
name: technology-due-diligence
description: Orchestriert evidenzbasierte Technology-Due-Diligence für Licensing, Partnership, Acquisition oder Make/Buy aus Offer/Technology Assessment, Patent Landscape, technischer FTO-Vorprüfung und optionalen Regulatory-/Supplier-Spezialbewertungen; priorisiert Red Flags, Unknowns, Entscheidungstreiber und nächste sichere Aktionen ohne Fachlogik der Spezial-Skills zu duplizieren.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - technology-offer-assessment
  - patent-landscape-analysis
  - freedom-to-operate-assessment
  - large-work-wayfinder
outputs:
  - technology-due-diligence.json
  - technology-due-diligence.md
  - due-diligence-handoff.json
```

## Decision Context

Mindestens erfassen:

- transaction/decision type: `license | partnership | acquisition | make-buy | supplier-selection | strategic-investment | other`
- target technology/product
- intended use / commercial objective
- target markets/jurisdictions
- decision deadline / stage soweit bekannt
- must-have criteria
- risk appetite / irreversible decisions soweit explizit bekannt

## Orchestrationslogik

1. **Scope & hypotheses** fixieren.
2. **Evidence base** über `research-to-evidence-note` in den Fach-Skills aufbauen.
3. **Technology/offer fit** über `technology-offer-assessment`.
4. **Patent landscape** über `patent-landscape-analysis`.
5. **FTO screening** nur für konkret definierte Produkt-/Prozesskonfigurationen über `freedom-to-operate-assessment`.
6. **Regulatory** bei IVD/Medical Device an bestehende Regulatory Skills routen.
7. **Supplier/quality/scale** bei Medical Device/IVD an `supplier-quality-medical-device` und passende QMS-/Validation-Skills routen.
8. Ergebnisse in gemeinsame Decision Dimensions überführen.
9. Red Flags, Unknowns, Evidence Gaps, reversible/irreversible decisions und investigation backlog priorisieren.
10. Bei blockierender Unsicherheit begrenzte Investigations an `large-work-wayfinder` übergeben.

## Gemeinsame Decision Dimensions

- technical differentiation
- performance evidence
- maturity/transferability
- integration burden
- manufacturing/scale/supply risk
- regulatory feasibility/readiness
- patent position / landscape density
- FTO screening risk
- licensing dependencies
- commercial model / cost structure
- strategic fit / lock-in
- critical unknowns

## Red-Flag-Priorisierung

Jeder Red Flag Record enthält:

- `issue`
- `domain`
- `evidence`
- `confidence`
- `impact`
- `reversibility`
- `decisionTiming`
- `owner/authority`
- `nextEvidence`
- `stopCondition`

Keine Gesamtpunktzahl erfinden, wenn die Gewichtung nicht vom Nutzer/Entscheidungskontext bestätigt ist.

## Output-Vertrag

`technology-due-diligence.json` enthält Scope, Decision Context, Specialist Assessments, Cross-Domain Dependencies, Red Flags, Unknowns, Decision Drivers, Options, Preconditions und Recommendation.

`due-diligence-handoff.json` ist Wayfinder-kompatibel mit mindestens:

`facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks, nextSafeAction`.

## Qualitätsgate

Pass nur wenn:

- der Orchestrator keine Claim-/Regulatory-/Supplier-Fachanalyse dupliziert,
- Ergebnisse auf Specialist Evidence zurückgeführt werden,
- kritische Unknowns nicht in Scores versteckt werden,
- FTO als Screening und nicht als Legal Opinion behandelt wird,
- volatile Inputs `asOf` besitzen,
- eine Empfehlung Preconditions und Abbruchkriterien enthält,
- nächste Aktionen ohne versteckte Annahmen ausführbar sind.

## Evaluation

### Happy Path

Eine neue Biosensorplattform soll für mehrere Immunoassay-Anwendungen lizenziert werden. Es liegen technische Unterlagen, Pilotdaten, Preisannahmen und öffentliche Patentquellen vor. Der Orchestrator koordiniert Offer Assessment, Patent Landscape, FTO Screening und relevante IVD-Spezialbewertungen und liefert ein Executive DD mit klaren Go/Conditional-Go/No-Go-Treibern.

### Edge Case

Technische Daten sind stark, aber FTO ist AMBER/RED und regulatorische Intended-Use-/Performance-Annahmen sind noch instabil. Ergebnis: keine pauschale positive DD; klare Preconditions, Counsel-/Regulatory-Eskalationen und begrenzte Investigations.

### Failure Case

Der Orchestrator erzeugt selbst Claim Charts, erfindet eine Regulatory Classification und mittelt alle Unsicherheiten in einen „82/100“-Score. Der Lauf muss als Architektur-/Qualitätsfehler gelten.

---

# Kompositionsgraph

```text
research-to-evidence-note
        │
        ├── technology-offer-assessment
        │       ├── optional: external-stakeholder-questionnaire
        │       ├── optional: supplier-quality-medical-device
        │       └── optional: regulatory specialist skills
        │
        └── patent-landscape-analysis
                 │
                 └── freedom-to-operate-assessment

technology-offer-assessment ─┐
patent-landscape-analysis ────┼── technology-due-diligence ── large-work-wayfinder
freedom-to-operate-assessment ┘
```

---

# IVD-spezifische Referenzfälle für spätere Evaluation

Die folgenden Fälle sind geeignete Fixtures, ohne produktspezifische vertrauliche Daten im Skill zu verankern:

## Autoantikörper-Test / Typ-1-Diabetes

Prüfpunkte: Antigenpräsentation, Konformation, Multiplexing, Cutoff-/Calibration-Konzept, Präzision, Interferenzen, Probenmatrix, Reagent/antigen IP, assay-method claims.

## Anti-Nephrin-Autoantikörper

Prüfpunkte: native/rekombinante Antigenkonformation, Antikörperbindung, CBA-vs.-solid-phase implications, analytische/klinische Evidenz, target/epitope/method claims, Plattformtransfer.

## pTau217-Antigentest in Blut

Prüfpunkte: sehr niedrige Konzentrationen, capture/detection antibody pair, phospho-epitope specificity, high-sensitivity detection, matrix/sample handling, antibody/epitope/method patent families, licensing dependencies.

Die Referenzfälle dürfen Evaluation und Beispiele speisen, aber die Skills selbst bleiben technologieagnostisch und enthalten keine Anbieter- oder Projektgeheimnisse.

---

# Nicht-Ziele des Clusters

Nicht Bestandteil:

- verbindliche Rechtsberatung oder Legal Opinion,
- Patentability-/Validity-/Enforceability-Gutachten,
- Vertragsprüfung oder Vertragsverhandlung,
- automatische Patentüberwachung als Dauerprozess,
- eigenständige Marktgrößen-/TAM-/Forecast-Modellierung,
- eigenständige Regulatory Classification außerhalb bestehender Regulatory Skills,
- eigenständiges Supplier-QMS-System,
- Investment-Committee-Memo- oder Board-Drafting; nachgelagerte Document Skills können die DD-Artefakte konsumieren.

---

# Implementierungsreihenfolge

1. `patent-landscape-analysis`
2. `freedom-to-operate-assessment`
3. `technology-offer-assessment`
4. `technology-due-diligence`

Begründung: FTO benötigt einen stabilen Patent-Landscape-Vertrag; der Orchestrator soll erst entstehen, wenn die drei Fach-Skills belastbar definiert und evaluiert sind.

---

# Definition of Done für die Implementierung

Der Cluster ist implementiert, wenn:

- für alle vier Skills `SKILL.md` mit eindeutiger Grenze, Triggern, Workflow, Output-Verträgen und Qualitätsgate existiert,
- pro Skill mindestens Happy Path, Edge Case und Failure Case als `tests/evaluation.json` vorliegen,
- die Dependencies im Repository-Graph valide sind,
- der Capability Index die vier neuen Entry Points enthält,
- bestehende Skills nicht funktional dupliziert werden,
- FTO-Sicherheits-/Legal-Grenzen in Routing und Outputs explizit getestet werden,
- die IVD-Referenzfälle mindestens einmal als integrierte Komposition evaluiert wurden,
- der Branch-Diff geprüft und die Repository-Evaluation grün ist.
