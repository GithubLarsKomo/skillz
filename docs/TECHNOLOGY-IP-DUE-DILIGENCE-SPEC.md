# Technology & IP Due Diligence Skill Cluster — Specification

## Ziel

Diese Spezifikation definiert vier kleine, komponierbare Skills für wiederkehrende Technology-/Offer-/IP-/FTO-Due-Diligence-Aufgaben. Sie ergänzt bestehende Research-, Regulatory-, Supplier-Quality- und Wayfinder-Capabilities, ohne deren Fachlogik zu duplizieren.

Die vier Skills sind:

1. `technology-offer-assessment`
2. `patent-landscape-analysis`
3. `freedom-to-operate-assessment`
4. `technology-due-diligence`

Der Cluster ist insbesondere für technologieintensive IVD-/MedTech-Szenarien geeignet, bleibt aber soweit möglich domänenneutral. Medical-Device-/IVD-spezifische Regulatory- und Supplier-Fragen werden an bestehende Spezial-Skills geroutet.

> **Implementation status (2026-08-19):** implemented on `feat/technology-ip-due-diligence`, including canonical OpenAI agent metadata, three recorded evaluation cases per skill, generated capability/dependency metadata, Obsidian projections and OpenAI plugin distribution. The standard repository validation workflow passed on GitHub Actions run 542.

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

## Eingaben

Mindestens:

- `decisionContext`: welche Entscheidung soll vorbereitet werden?
- `intendedUseOrWorkflow`: geplanter Einsatz,
- `requirements`: Must-haves und Nice-to-haves,
- eine oder mehrere Offerten bzw. Herstellerunterlagen,
- `asOf` für volatile Angaben.

Optional:

- eigene Versuchs-/Pilotdaten,
- historische Anbieterperformance,
- Regulatory-/Quality-Kontext,
- aktuelle Commercial Terms,
- bestehende IP-/Lizenzinformationen.

## Bewertungsdimensionen

### Technology / analytical fit

- Mess-/Detektionsprinzip,
- Sensitivität / LOD / LOQ soweit relevant,
- Dynamikbereich,
- Präzision,
- Interferenzen / Matrixeffekte,
- Multiplexing,
- Sample Volume,
- Reagent Stability,
- Calibration / QC,
- Throughput / TAT.

### Maturity / validation

- Research Prototype,
- engineered prototype,
- pilot-ready,
- production-relevant,
- reproduzierbare Performance,
- Transferability,
- Validation Depth,
- Longitudinal / Multi-site Evidence soweit relevant.

Keine numerische TRL erzwingen, wenn sie nicht sinnvoll evidenzierbar ist.

### Integration / operations

- Automatisierbarkeit,
- Hardware-/Software-Abhängigkeiten,
- Workflow Changes,
- Data Integration,
- Maintenance,
- Training,
- Calibration/QC Burden,
- Operational Failure Modes.

### Scale / supply / quality

- kritische Komponenten,
- Single Sources,
- Capacity,
- Manufacturing Complexity,
- Lot-to-lot Risks,
- Quality-System-Kontext.

Medical-Device-/IVD-Supplier-Qualification bleibt bei `supplier-quality-medical-device`.

### IP / licensing dependencies

- bekannte proprietäre Reagenzien,
- Antikörper-/Binder-Abhängigkeiten,
- Plattformpatente,
- Software-/Algorithmuslizenzen,
- Field-of-Use Restrictions,
- Royalties.

Keine FTO-Schlussfolgerung im Offer Skill.

### Commercial model

- CAPEX,
- OPEX,
- Consumables,
- Service,
- Minimum Volumes,
- Royalties,
- Milestones,
- Switching Costs,
- Vendor Lock-in.

Preise benötigen Datum, Menge/Volumen und Quelle. Keine scheinpräzise TCO-Rechnung mit fehlenden Inputs.

## Evidence-Regeln

- Marketingclaim ≠ bestätigte Performance.
- Nicht publizierte Anbieterdaten sind als Vendor Evidence kenntlich zu machen.
- Eigene Verifikationsdaten sind von Vendor Data zu trennen.
- Für externe Recherche `research-to-evidence-note` verwenden.
- Unzugängliche oder fehlende Daten bleiben `unknown`.

## Fit-Kategorien

Pro Dimension:

- `strong`
- `conditional`
- `weak`
- `unknown`

Keine Gesamtpunktzahl ohne explizit bestätigte Gewichtung.

## Kernworkflow

1. Decision Context und Anforderungen fixieren.
2. Offerten/Claims inventarisieren.
3. Evidence je Claim klassifizieren.
4. Technischen Fit gegen Anforderungen bewerten.
5. Maturity/Transferability bewerten.
6. Integration/Operational Burden prüfen.
7. Scale/Supply/Quality Hooks identifizieren.
8. IP/Licensing Dependencies inventarisieren.
9. Commercial Model mit expliziten Annahmen strukturieren.
10. Red Flags, Decision Drivers und offene Fragen ableiten.
11. Spezialfragen routen.

## Output-Vertrag

`technology-offer-assessment.json` enthält mindestens:

```json
{
  "scope": {},
  "decisionContext": {},
  "asOf": "YYYY-MM-DD",
  "requirements": [],
  "offers": [],
  "claims": [],
  "assessmentDimensions": [],
  "fit": [],
  "redFlags": [],
  "commercialAssumptions": [],
  "ipDependencies": [],
  "regulatoryRouting": [],
  "decisionDrivers": [],
  "recommendation": {
    "status": "...",
    "preconditions": []
  }
}
```

`technology-offer-gap-set.json` enthält offene Fragen mit:

- `question`,
- `domain`,
- `priority`,
- `decisionImpact`,
- `evidenceNeeded`,
- `ownerOrSource`.

## Übergaben

- Patent Landscape → `patent-landscape-analysis`
- konkretes FTO → `freedom-to-operate-assessment`
- Supplier QMS → `supplier-quality-medical-device`
- IVD/Medical Device Regulatory → bestehende Regulatory-Skills
- fehlende Anbieterinformationen → `external-stakeholder-questionnaire`

## Evaluation

### Happy Path

Zwei Anbieter werden anhand derselben Requirements und aktueller Evidenz verglichen; technische und kommerzielle Unterschiede sind nachvollziehbar.

### Grenzfall

Anbieter behauptet außergewöhnliche Sensitivität und Produktionsreife, liefert aber nur ausgewählte Prototype-Daten. Erwartung: Claim bleibt sichtbar, Confidence niedrig/conditional, zusätzliche Verifikation wird konkret benannt.

### Fehlerfall

Pitch Deck wird allein zur Aussage „market ready, regulatorily suitable and IP safe“ verwendet. Erwartung: stoppen, drei getrennte Fragen routen.

---

# 2. `patent-landscape-analysis`

## Skill-Grenze

Dieser Skill verwandelt eine definierte Technologiefrage und zugängliche Patent-/Registerquellen in eine deduplizierte Patentfamilienlandschaft mit reproduzierbarer Suchstrategie, Claim-Themen, Jurisdiktionen, Legal-Status-Freshness, Unsicherheiten und offenen Suchfragen.

## Trigger

- „Erstelle ein Patent Landscape zu …“
- „Welche Patentfamilien schützen diese Technologie?“
- „Welche Assignees sind in diesem Assay-/Biomarkerfeld aktiv?“
- „Welche Claims/Familien sind für diese Plattform relevant?“

Nicht für produktkonkrete FTO-Schlussfolgerungen verwenden.

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

## Suchraum

Mögliche Facetten:

- Keywords / Synonyme,
- Biomarker-/Target-Namen,
- Assay-/Detection-Prinzip,
- CPC/IPC,
- Applicant/Assignee,
- Inventor,
- Citations,
- Family Relations,
- relevante Produkte/Reagenztypen.

Eine Keyword-Suche allein ist keine belastbare Landscape-Methodik.

## Family Normalization

Pro Family mindestens:

```json
{
  "familyId": "...",
  "representativePublication": "...",
  "earliestPriority": "YYYY-MM-DD",
  "priorityApplications": [],
  "members": [],
  "assignees": [],
  "inventors": [],
  "jurisdictions": [],
  "legalStatus": [],
  "claimScopeBranches": [],
  "independentClaimThemes": [],
  "technologyTags": [],
  "relevance": "core|adjacent|contextual|excluded",
  "relevanceRationale": "...",
  "statusUncertainties": []
}
```

### Continuations / Divisionals

Gemeinsame Priorität bedeutet nicht identischen Claim Scope. Parallel laufende Continuations, Divisionals oder national unterschiedliche Claim Sets müssen sichtbar bleiben, wenn sie für die Analyse relevant unterschiedlich sind.

## Legal Status

Discovery-Datenbanken dürfen zur Suche genutzt werden. Materiell entscheidungsrelevanter aktueller Status sollte bevorzugt gegen offizielle Register/Patentämter geprüft werden.

Jede zeitabhängige Statusaussage enthält:

- Jurisdiktion,
- Member/Publication/Patent,
- Status,
- `asOf`,
- Source,
- Confidence/Uncertainty.

## Claim-Themen

Independent Claims semantisch zerlegen, z. B.:

- Target/Biomarker,
- Reagent/Antibody,
- Sample,
- Assay Format,
- Detection Principle,
- Signal Processing,
- Workflow Steps.

Keine verbindliche Claim Construction simulieren.

## Search Log

Jede Search Iteration dokumentiert:

```json
{
  "source": "...",
  "query": "...",
  "date": "YYYY-MM-DD",
  "filters": [],
  "resultCount": null,
  "inclusionLogic": "...",
  "exclusionLogic": "...",
  "iterationReason": "..."
}
```

## White Space

White Spaces werden als **Recherchehypothese** formuliert. Kein „niemand hat das patentiert“ aus einer begrenzten Suche ableiten.

## Übergabe an FTO

Markiere pro Kernfamilie:

- relevante Jurisdiction Members,
- potenziell relevante Independent Claims,
- Claim-Element-Themen,
- Statusunsicherheiten,
- offene Search/Prosecution-Fragen.

## Evaluation

### Happy Path

Keyword/CPC/Assignee/Citation-Suche identifiziert überlappende Publikationen, dedupliziert sie in Familien und hält Claim-Scope-Unterschiede sichtbar.

### Grenzfall

US Continuation und EP Divisional teilen Priorität, aber Claims unterscheiden sich. Erwartung: gemeinsame Family-Beziehung plus separate Claim-Scope-Branches.

### Fehlerfall

Aggregator nennt Family „active“, offizielles Register widerspricht oder ist unklar. Erwartung: Statusunsicherheit bleibt sichtbar, keine definitive Statusaussage.

---

# 3. `freedom-to-operate-assessment`

## Skill-Grenze

Dieser Skill verwandelt eine definierte Produkt-/Prozesskonfiguration, Zieljurisdiktionen und relevante Claims in eine technische Claim-by-Claim-FTO-Vorprüfung mit evidenzbasiertem Element-Mapping, Screening-Risikokategorien, Design-around-Hypothesen und Counsel-Eskalationen.

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

## FTO Scope

Vor jeder Bewertung fixieren:

```json
{
  "productConfiguration": {},
  "technicalFeatureBaseline": [],
  "jurisdictions": [],
  "commercialActs": [],
  "asOf": "YYYY-MM-DD",
  "exclusions": [],
  "assumptions": []
}
```

Keine Aussage „FTO“ ohne diesen Scope.

## Claim Mapping

Pro Claim:

```json
{
  "patentOrApplication": "...",
  "jurisdiction": "...",
  "claimId": "...",
  "claimType": "independent",
  "grantState": "granted|pending|unknown",
  "legalStatus": "...",
  "statusAsOf": "YYYY-MM-DD",
  "statusSource": "...",
  "elements": [
    {
      "element": "...",
      "mapping": "present|likely-present|absent|unknown|interpretation-dependent",
      "featureEvidence": [],
      "confidence": "high|medium|low"
    }
  ],
  "dependentClaims": [],
  "screeningRisk": "RED|AMBER|GREEN|GREY",
  "counselEscalation": false,
  "openQuestions": []
}
```

## Kernregel

Ein potentieller Full Read-on benötigt Betrachtung **aller erforderlichen Claim-Elemente**. Topic Similarity oder Patent-Family-Relevance ersetzt kein Claim Chart.

## Risikokategorien

### RED — potential full read-on

Alle erforderlichen Elemente eines relevant erscheinenden aktuellen Independent Claims sind `present`/`likely-present`, oder eine materielle Claim-Construction-Frage trennt vom Full Read-on.

→ Mandatory Patent Counsel.

### AMBER — material uncertainty

Materielle Überschneidung, aber entscheidende Unsicherheit bei:

- Claim Construction,
- Produkteigenschaft,
- Status,
- Pending Claim Scope,
- Prosecution History,
- Ownership/License.

→ Counsel/Investigation abhängig von Commercial Impact.

### GREEN — no current full read-on identified

Mindestens ein erforderliches Element ist evidenzbasiert `absent`, oder der konkret betrachtete Claim ist in der betrachteten Jurisdiktion verifiziert nicht relevant in Kraft.

**Nicht formulieren:** „Product does not infringe.“

Stattdessen:

> No current full read-on was identified for the reviewed claims, configuration, jurisdiction and as-of date.

### GREY — insufficient evidence

Scope, Produktfeature, Claim Text oder Status reicht nicht zur belastbaren technischen Vorprüfung.

## Granted vs Pending

Pending Claims separat behandeln:

- können sich ändern,
- sind strategisch relevant,
- sind nicht identisch mit einem aktuell erteilten Ausschließlichkeitsrecht.

## Design-around

Jede Hypothese benötigt:

```json
{
  "targetClaimElement": "...",
  "technicalChange": "...",
  "feasibility": "high|medium|low|unknown",
  "performanceImpact": "...",
  "manufacturingImpact": "...",
  "regulatoryImpact": "...",
  "newIpQuestions": [],
  "verificationNeeded": []
}
```

Ein Design-around ist keine FTO-Freigabe und wird nach Änderung erneut gescreent.

## Counsel Escalation

Mandatory bei:

- RED,
- kommerziell relevantem AMBER,
- Claim-Construction-Frage,
- komplexer Prosecution History,
- Equivalents-/Äquivalenzfragen,
- Ownership-/License-Uncertainty,
- imminent Launch / Closing.

## Verbotene Schlussfolgerungen

Der Skill darf als abschließendes Rechtsurteil nicht behaupten:

- „infringes“,
- „does not infringe“,
- „valid/invalid“,
- „enforceable/unenforceable“.

## Evaluation

### Happy Path

Definierter Assay + konkrete US/EP Claims + aktueller Status → elementweises Mapping und jurisdiction-spezifische Heatmap.

### Grenzfall

EP Family Member expired, US Continuation live, weitere Pending Continuation. Erwartung: keine Family-weite grüne Freigabe; Claims/Jurisdiktionen getrennt.

### Fehlerfall

User fordert „Product X does not infringe because Google Patents says expired“. Erwartung: verweigert definitive Aussage, prüft Jurisdiktion/Claim/Status, nutzt GREY/AMBER soweit Evidenz fehlt.

---

# 4. `technology-due-diligence`

## Rolle

Dünner Orchestrator für Licensing, Partnership, Acquisition, Strategic Investment, Make/Buy oder Supplier Selection.

Er konsumiert Specialist Outputs; er erzeugt keine zweite Patent-/FTO-/Regulatory-/Supplier-Analyse.

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

Mindestens:

- Decision Type,
- Target Technology/Product,
- Intended Use,
- Commercial Objective,
- Target Markets/Jurisdictions,
- Decision Stage/Deadline,
- Must-have Criteria,
- Risk Appetite soweit explizit bestätigt,
- `asOf`.

## Orchestrierung

### Technology

`technology-offer-assessment`

### IP Landscape

`patent-landscape-analysis`

### FTO

`freedom-to-operate-assessment`

### Regulatory

Für IVD/Medical Device passende bestehende Regulatory-Skills.

### Supplier / Quality / Scale

`supplier-quality-medical-device` und bestehende QMS/Validation Skills.

## Cross-Domain Dependencies

Der Orchestrator modelliert Abhängigkeiten, z. B.:

- Design-around → Performance + Regulatory Evidence ändern,
- proprietärer Binder → IP + Supply + Cost koppeln,
- neue Sample Prep → Technical Fit + FTO + Regulatory ändern,
- Manufacturing Change → Scale + Quality + Regulatory beeinflussen.

## Decision Dimensions

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

Keine Gesamtpunktzahl ohne bestätigte Gewichtung.

## Red Flag Record

```json
{
  "issue": "...",
  "domain": "technology|ip|fto|regulatory|quality|supply|commercial|strategy",
  "evidence": [],
  "confidence": "high|medium|low",
  "impact": "...",
  "reversibility": "...",
  "decisionTiming": "...",
  "ownerOrAuthority": "...",
  "nextEvidence": "...",
  "stopCondition": "..."
}
```

## Recommendation

Mögliche Zustände:

- `go`
- `conditional-go`
- `hold`
- `no-go`
- `insufficient-evidence`

Recommendation benötigt immer:

- Decision Drivers,
- Preconditions,
- Blockers,
- Authority Boundaries,
- Next Safe Action.

## Wayfinder-Handoff

```json
{
  "facts": [],
  "assumptions": [],
  "hypotheses": [],
  "unknowns": [],
  "blockers": [],
  "decisions": [],
  "investigations": [],
  "risks": [],
  "nextSafeAction": "..."
}
```

Investigations sind begrenzt und enthalten Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele.

---

# IVD-Referenzfälle für integrierte Evaluation

Die Skills bleiben generisch. Für End-to-End-Evaluationen sollen jedoch drei typische IVD-Szenarien als Fixtures verwendet werden.

## T1D Autoantikörper

Beispielkontext:

- Autoantibody Detection,
- mehrere Antigene/Targets,
- hoher Wert von Multiplexing,
- Sensitivitäts-/Spezifitäts- und Interferenzfragen,
- Antigen-/Assayformat-IP,
- Plattform-/Detection-IP.

Testziel:

- Technology Fit und FTO nicht vermischen,
- target-/reagent-/format-/detectionbezogene Patent Claims differenzieren.

## Anti-Nephrin-Autoantikörper

Beispielkontext:

- neuer/entwickelnder Biomarker,
- begrenztere Evidenzbasis,
- Target-/Epitope-/Reagent-Fragen,
- mögliche proprietäre Binder/Antigene,
- erhöhte Unsicherheit bei Clinical/Commercial Maturity.

Testziel:

- Evidence Gaps bleiben sichtbar,
- Patent Search behauptet keine Vollständigkeit,
- Commercial Potential ersetzt keine Analytical/Clinical Evidence.

## pTau217 im Blut

Beispielkontext:

- sehr niedrige Analytenkonzentration,
- hohe Sensitivitätsanforderung,
- Antibody Pair / Epitope / Calibration / Detection Platform,
- intensive Biomarker-/Immunoassay-IP-Landschaft,
- mögliche Licensing Dependencies.

Testziel:

- assay-spezifische Product Baseline vor FTO fixieren,
- Binder-/Epitope-/Format-/Detection Claims getrennt mappen,
- Design-around auf Performance-/Regulatory-Auswirkungen prüfen.

---

# Gemeinsame Qualitätsregeln

## Quellenhierarchie

Je nach Claim:

1. offizielle/primäre Register bzw. Patentdokumente,
2. Hersteller-/Vertrags-/Projektquelle für eigene Eigenschaften,
3. hochwertige wissenschaftliche Primär-/Sekundärliteratur,
4. Aggregatoren zur Discovery,
5. schwächere kontextuelle Quellen nur mit sichtbarer Einschränkung.

## Freshness

Aktualitätskritisch:

- Patent Legal Status,
- Pending Claim Scope,
- Ownership/Assignment,
- Preise,
- Lieferbedingungen,
- Regulatory Status,
- Produkt-/Plattformverfügbarkeit.

Diese Claims benötigen `asOf`.

## Confidentiality / Memory

Run-only bzw. projektgebunden:

- konkrete vertrauliche Offerten,
- Preise/Vertragsbedingungen,
- nicht öffentliche Performance-Daten,
- konkrete Produktfeatures vor Launch,
- Counsel Advice,
- aktuelle License Negotiations.

Persistenzwürdig:

- generische Bewertungsdimensionen,
- Claim-Mapping-Schema,
- Search-/Family-Heuristiken,
- Risikokategorien,
- abstrahierte DD-Kompositionsmuster.

---

# Dependency Graph

```text
research-to-evidence-note
    ├── technology-offer-assessment
    └── patent-landscape-analysis
            └── freedom-to-operate-assessment

technology-offer-assessment ─┐
patent-landscape-analysis ────┼── technology-due-diligence
freedom-to-operate-assessment ┤
large-work-wayfinder ─────────┘

optional IVD/MedTech routing:
technology-due-diligence
    ├── regulatory specialist skills
    └── supplier-quality-medical-device
```

Der Regulatory-/Supplier-Pfad ist bewusst kein harter `requires`-Pfad des generischen Orchestrators.

---

# Implementierungsreihenfolge

1. `patent-landscape-analysis`
2. `freedom-to-operate-assessment`
3. `technology-offer-assessment`
4. `technology-due-diligence`
5. Capability Index / Dependency Graph regenerieren
6. integrierte IVD-Fixtures ausführen
7. fokussierten Pull Request eröffnen

Diese Reihenfolge minimiert die Gefahr, dass der Orchestrator Fachlogik enthält, bevor stabile Specialist Outputs existieren.

---

# Definition of Done für den Cluster

Der Cluster ist implementiert, wenn:

- alle vier `SKILL.md` vorhanden sind,
- jeder Skill einen präzisen Trigger und Nicht-Ziele besitzt,
- keine Output-Namenskollision mit vorhandenen Skills besteht,
- Dependencies im Capability Graph korrekt erscheinen,
- jeder Skill Happy Path, Grenzfall und Fehlerfall besitzt,
- FTO niemals Legal Counsel simuliert,
- Legal Status/Freshness/Jurisdiction in Patent-/FTO-Outputs sichtbar sind,
- der Orchestrator keine Specialist Logic dupliziert,
- die drei IVD-Referenzfälle die integrierte Komposition erfolgreich prüfen,
- Capability Index und README aktualisiert sind,
- Repository-Evaluation grün ist,
- ein Review-fähiger PR existiert.
