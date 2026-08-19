---
name: technology-offer-assessment
description: Bewertet konkrete Technologieofferten oder vergleichbare Anbieterangebote evidenzbasiert auf technischen Fit, Reifegrad, Performance Claims, Integration, Skalierung, Supply/Quality, kommerzielle Bedingungen, IP-Abhängigkeiten, Vendor Dependency, Red Flags und offene Fragen; keine Vertragsrechts- oder FTO-Analyse.
---

# Technology Offer Assessment

## Zweck und Grenze

Bewerte eine oder mehrere konkrete Technologieofferten gegen einen bestätigten Entscheidungskontext und ein gemeinsames Anforderungsset. Der Skill trennt Anbieterclaims von Evidenz, vergleicht technische und operative Eignung, macht kommerzielle Annahmen sichtbar und routet IP-, Regulatory- und Supplier-Themen an passende Spezial-Skills.

Der Skill ersetzt weder Vertragsprüfung noch Supplier-QMS-Qualifizierung, Regulatory Classification, Patent Landscape oder FTO. Strategische Gesamtpassung gehört in `technology-due-diligence`; hier werden nur offer-nahe Abhängigkeiten wie Vendor Lock-in und Switching Burden bewertet.

## Trigger

Verwenden bei Offerten-/Angebotsanalyse, One-Pager-/Pitch-Deck-Bewertung, Anbieter- oder Plattformvergleich, Make/Buy-Vorprüfung oder der Frage, ob eine Technologie für einen definierten Assay/Workflow geeignet ist.

## Voraussetzungen

Fixiere vor der Bewertung:

1. Zielentscheidung und Intended Use / Workflow,
2. Must-have- und Nice-to-have-Anforderungen,
3. zu vergleichende Angebote und `asOf`,
4. bekannte technische, operative und kommerzielle Constraints,
5. verfügbare Evidenz und offene Datenlücken.

Mehrere Angebote werden entlang **identischer Kriterien** bewertet. Fehlt ein Datum oder Mengenbezug für Preise, wird die kommerzielle Aussage als Annahme markiert.

## Workflow

### 1. Scope und Anforderungen normalisieren

Erfasse Technologie, Produktgrenzen, Sample/Workflow, Zielnutzer, Throughput, Performance-Ziele, Integration, Scale sowie Quality/Regulatory-Kontext. Trenne harte Anforderungen von Präferenzen.

### 2. Claim Inventory und Evidence Model erstellen

Extrahiere explizite technische, analytische, klinische, Throughput-, Robustness-, Scale-, Regulatory- und Commercial Claims je Anbieter. **Marketing Claims und bestätigte Evidenz getrennt halten.**

Jeder Claim erhält mindestens:

- `evidenceOrigin`: `vendor | customer | independent | regulatory | literature | derived | unknown`,
- `evidenceType`: `marketing | specification | raw-data | study | publication | validation | certificate | derived`,
- `independence`: `first-party | second-party | third-party | unknown`,
- Source References und Freshness,
- `confidence`: `high | medium | low | unknown`.

Für quantitative Performance Claims erfasse zusätzlich, soweit verfügbar: Testbedingungen/Matrix, Sample Size, Comparator/Reference Method, `replicationStatus: none | internal | external` und `transferabilityToTargetUse: demonstrated | plausible | unknown | unlikely`.

Informationsmenge ist keine Evidenzqualität: viele Marketingseiten schlagen keine kleinere Menge belastbarer unabhängiger oder eigener Verifikationsevidenz.

### 3. Technischen Fit bewerten

Bewerte nur soweit relevant:

- Mess-/Detektionsprinzip,
- analytische Sensitivität, Dynamikbereich, Präzision und Interferenzen,
- Matrixkompatibilität und Sample Handling,
- Multiplexing, Calibration/QC,
- Automatisierbarkeit, Software/Data Integration,
- Failure Modes und Robustness.

Keine fehlende Eigenschaft als erfüllt interpretieren.

### 4. Reifegrad und Transferability prüfen

Ordne vorhandene Evidenz als Concept/Prototype/Pilot/production-relevant ein, ohne unbelegte TRL-Zahlen zu erfinden. Prüfe Reproduzierbarkeit, Transfer auf Zielworkflow, Validation Depth, kritische Komponenten und Scale Evidence. Production Readiness ohne passende Manufacturing-/Validation-Evidenz bleibt `unknown` oder `conditional`.

### 5. Operational / Supply / Quality Hooks prüfen

Erfasse Hardware, Consumables, Calibration/QC, Training, Maintenance, Throughput, turnaround, Single Source, Capacity und kritische Reagenzien. Für Medical Device/IVD bleibt die Supplier-QMS-Tiefe beim `supplier-quality-medical-device`-Skill; hier wird nur geroutet.

### 6. IP- und Licensing-Abhängigkeiten inventarisieren

Dokumentiere bekannte proprietäre Reagenzien, Antikörper, Software, Patente, Lizenzmodelle, Field-of-Use Restrictions und Royalties als Dependencies. **Keine FTO-Schlussfolgerung** aus Angebotsunterlagen ableiten. Vertiefe bei Bedarf über `patent-landscape-analysis` oder direkt über `freedom-to-operate-assessment`, wenn ein geeignetes Claim Set bereits vorliegt.

### 7. Commercial Model transparent machen

Erfasse CAPEX, OPEX, Consumables, Service, Minimum Volumes, Royalties, Milestones, Switching Costs und Lock-in nur mit Mengen-/Zeitbezug und Quelle. Rechne Szenarien nur mit expliziten Annahmen; kein scheinpräziser TCO bei fehlender Datengrundlage.

Technischer Fit und Commercial Feasibility bleiben getrennte Dimensionen; eine technisch starke Offerte kann kommerziell schwach oder nicht tragfähig sein.

### 8. Decision Drivers, Red Flags und Fragen ableiten

Jeder Red Flag erhält Evidence, Confidence, Decision Impact und die nächste Information, die die Entscheidung verändern könnte. Fehlende Anbieterinformationen können an `external-stakeholder-questionnaire` geroutet werden.

## Bewertungsdimensionen

Mindestens: technical fit, performance evidence, maturity/validation, operational fit, integration burden, scale/supply, quality/regulatory hooks, IP/licensing dependencies, commercial model, vendor dependency/switching burden und critical unknowns.

**Strategic fit gehört nicht in diesen Skill.** Es wird im `technology-due-diligence`-Orchestrator bewertet.

Fit wird je Dimension als `strong | conditional | weak | unknown` angegeben; keine Gesamtpunktzahl ohne bestätigte Gewichtung.

## Output-Verträge

`technology-offer-assessment.json` enthält Scope, Decision Context, `asOf`, Offers, Requirements, Claims mit differenziertem Evidence Model, Assessment Dimensions, Fit, Red Flags, Commercial Assumptions, IP Dependencies, Vendor Dependency, Regulatory Routing und Decision Drivers.

`technology-offer-gap-set.json` enthält offene technische, evidenzielle, regulatorische, IP-, kommerzielle und Supplier-Fragen mit Priority, Decision Impact, Evidence Needed und Owner/Source.

`technology-offer-assessment.md` ist die menschenlesbare Vergleichsmatrix plus Synthese.

## Routing

- externe Evidenz → `research-to-evidence-note`
- Supplier-QMS → `supplier-quality-medical-device`
- Medical-Device-/IVD-Regulatory → passende Regulatory-Skills
- Patent Landscape → `patent-landscape-analysis`
- konkretes FTO Screening → `freedom-to-operate-assessment`
- strategische Gesamtpassung → `technology-due-diligence`
- fehlende Anbieterinformationen → `external-stakeholder-questionnaire`

## Memory Path

Persistenzwürdig sind generische Bewertungsdimensionen und Vergleichsheuristiken. Konkrete Preise, vertrauliche Offerten, Vertragsbedingungen, Anbieter-Roadmaps und nicht öffentliche Performance-Daten bleiben run-only/projektgebunden.

## Qualitätsgate

Pass nur wenn:

- Marketing Claims und bestätigte Evidenz getrennt bleiben,
- Evidence Origin, Type, Independence und Confidence sichtbar sind,
- quantitative Performance Claims ihre Bedingungen/Replication soweit verfügbar tragen,
- mehrere Angebote entlang identischer Kriterien verglichen werden,
- fehlende Daten als `unknown` statt positiv interpretiert werden,
- Informationsmenge nicht als Evidenzqualität gewertet wird,
- technischer und kommerzieller Fit nicht zusammenfallen,
- Strategic Fit nicht vorweggenommen wird,
- Regulatory-/Supplier-/IP-Fragen korrekt geroutet werden,
- keine FTO-Schlussfolgerung oder Vertragsrechts-Opinion simuliert wird.

## Fehlerbehandlung

Wenn nur Marketingmaterial ohne belastbare Performance- oder Scale-Evidenz vorliegt, bleibt der relevante Fit `unknown` oder `conditional`; die Offerte darf nicht allein daraus als marktreif oder regulatorisch geeignet bezeichnet werden.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Anforderungen und Claims vergleichbar normalisiert, Evidence Quality differenziert sichtbar, technische/operative/kommerzielle Fit-Treiber getrennt bewertet, Vendor Dependency statt Strategic Fit erfasst, Red Flags priorisiert und nachgelagerte IP-/Regulatory-/Supplier-Fragen sauber geroutet sind.
