---
name: technology-offer-assessment
description: Bewertet konkrete Technologieofferten oder vergleichbare Anbieterangebote evidenzbasiert auf technischen Fit, Reifegrad, Performance Claims, Integration, Skalierung, Supply/Quality, kommerzielle Bedingungen, IP-Abhängigkeiten, Vendor Dependency, Red Flags und offene Fragen und leitet daraus priorisierte Fragen für Vendor-Meetings und interne Stakeholder ab; keine Vertragsrechts- oder FTO-Analyse.
---

# Technology Offer Assessment

## Zweck und Grenze

Bewerte eine oder mehrere konkrete Technologieofferten gegen einen bestätigten Entscheidungskontext und ein gemeinsames Anforderungsset. Der Skill trennt Anbieterclaims von Evidenz, vergleicht technische und operative Eignung, macht kommerzielle Annahmen sichtbar und routet IP-, Regulatory- und Supplier-Themen an passende Spezial-Skills.

Zusätzlich erzeugt der Skill aus dem Assessment einen priorisierten, meeting-tauglichen Fragenkatalog. Dieser richtet Fragen je nach Wissensinhaber an die offerierende Partei, an interne Stakeholder oder an beide. Die Fragen entstehen aus konkreten Evidenzlücken, Red Flags, unbestätigten Annahmen, offenen Entscheidungen und Unsicherheiten des Assessments und nicht aus einer generischen Due-Diligence-Checkliste.

Der Skill ersetzt weder Vertragsprüfung noch Supplier-QMS-Qualifizierung, Regulatory Classification, Patent Landscape oder FTO. Strategische Gesamtpassung gehört in `technology-due-diligence`; hier werden nur offer-nahe Abhängigkeiten wie Vendor Lock-in und Switching Burden bewertet.

## Trigger

Verwenden bei Offerten-/Angebotsanalyse, One-Pager-/Pitch-Deck-Bewertung, Anbieter- oder Plattformvergleich, Make/Buy-Vorprüfung oder der Frage, ob eine Technologie für einen definierten Assay/Workflow geeignet ist. Ebenfalls verwenden, wenn aus einem solchen Assessment Fragen für ein Vendor-Meeting, einen technischen Deep Dive oder interne Klärungstermine vorbereitet werden sollen.

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

### 8. Decision Drivers, Red Flags und Gap Set ableiten

Jeder Red Flag erhält Evidence, Confidence, Decision Impact und die nächste Information, die die Entscheidung verändern könnte. Jede relevante Lücke erhält eine stabile `gapId`, Kategorie, Priority, Decision Impact, benötigte Evidenz und den wahrscheinlich zuständigen Wissensinhaber.

Das Gap Set ist die verbindliche Quelle für den nachfolgenden Fragenkatalog. Eine Frage ohne Rückverweis auf mindestens eine Assessment-Lücke, einen Red Flag, eine unbestätigte Annahme oder eine offene Entscheidung ist nur zulässig, wenn sie ausdrücklich als `meetingContext` markiert und für die Entscheidungsfindung notwendig ist.

### 9. Assessment-abgeleiteten Fragenkatalog erzeugen

Erzeuge aus den entscheidungsrelevanten Lücken ein **Technology Offer Question Set**. Ziel ist nicht maximale Fragenzahl, sondern maximaler Informationsgewinn für die nächste Entscheidung.

Für jede Frage:

- verknüpfe `sourceGapIds` und bei Bedarf `sourceAssessmentRefs`,
- bestimme `audience: vendor | internal | both`,
- benenne `targetRole` soweit aus dem Kontext ableitbar; keine Person erfinden,
- formuliere genau eine primäre Informations- oder Entscheidungsanforderung,
- erkläre `whyNeeded` und `decisionImpact`,
- definiere `expectedEvidence` oder gewünschtes Antwortformat,
- setze `priority: blocking | high | normal | low`,
- markiere, ob die Frage `askInMeeting`, `preRead`, `followUp` oder eine Kombination davon ist,
- erlaube `unknown` beziehungsweise „not available“, wenn die Evidenz tatsächlich fehlen kann.

#### Audience-Regeln

**Vendor-Fragen** adressieren Informationen, Evidenz oder Commitments, die die offerierende Partei belastbar liefern können sollte, zum Beispiel Rohdaten, Testbedingungen, Reproduzierbarkeit, Manufacturing Capacity, Roadmap, Support, Preislogik oder Licensing Dependencies. Vendor-Fragen dürfen keine internen Budgetgrenzen, Verhandlungspositionen, strategischen Präferenzen oder vertraulichen Vergleichsinformationen offenlegen, sofern dies nicht ausdrücklich freigegeben ist.

**Interne Fragen** adressieren eigene Anforderungen, Akzeptanzkriterien, Integrationsentscheidungen, Ressourcen, Verantwortlichkeiten, Risk Appetite, regulatorische Zielbilder oder wirtschaftliche Schwellen. Sie dürfen nicht so formuliert werden, als müsse der Vendor interne Entscheidungen treffen.

**`both`** ist nur zulässig, wenn tatsächlich dieselbe Sachfrage von beiden Seiten beantwortet oder abgeglichen werden muss. Wenn der Informationsbedarf gleich, die Formulierung aber aus Vertraulichkeits- oder Rollen-Gründen unterschiedlich ist, verwende eine gemeinsame `questionIntent` und getrennte `vendorWording` und `internalWording` statt identischer Wortwahl.

#### Ableitungslogik

Priorisiere Fragen in dieser Reihenfolge:

1. Informationen, die einen Go/No-Go- oder grundlegenden Fit-Befund ändern können,
2. Evidenz, die einen derzeit `unknown` oder `conditional` bewerteten Must-have-Fit klärt,
3. Red Flags mit hohem Decision Impact,
4. Annahmen mit starkem Einfluss auf TCO, Scale, Integration oder Timeline,
5. Fragen, deren Antwort mehrere nachgelagerte Fragen überflüssig machen kann,
6. Detailfragen.

Bereits durch belastbare Evidenz beantwortete Punkte werden nicht erneut gefragt. Allgemeine „Tell us more about your technology“-Fragen ohne Assessment-Bezug sind zu vermeiden.

### 10. Meeting- und Follow-up-Verwendung vorbereiten

Das Question Set muss direkt in ein Vendor- oder internes Meeting übernehmbar sein. Gruppiere bei Bedarf nach `topic` wie `technology`, `performance`, `validation`, `manufacturing`, `integration`, `quality-regulatory`, `ip-licensing`, `commercial`, `support` und `internal-decision`.

Für einen bestätigten Termin kann das priorisierte Question Set an `meeting-preparation` übergeben werden. Soll ein Teil der Vendor-Fragen vorab schriftlich versandt werden, kann dieser Teil an `external-stakeholder-questionnaire` übergeben werden. Nach dem Meeting gehen zugesagte Daten, offene Antworten und Commitments an `decision-and-follow-up-tracker` beziehungsweise zurück in das Assessment.

## Bewertungsdimensionen

Mindestens: technical fit, performance evidence, maturity/validation, operational fit, integration burden, scale/supply, quality/regulatory hooks, IP/licensing dependencies, commercial model, vendor dependency/switching burden und critical unknowns.

**Strategic fit gehört nicht in diesen Skill.** Es wird im `technology-due-diligence`-Orchestrator bewertet.

Fit wird je Dimension als `strong | conditional | weak | unknown` angegeben; keine Gesamtpunktzahl ohne bestätigte Gewichtung.

## Output-Verträge

`technology-offer-assessment.json` enthält Scope, Decision Context, `asOf`, Offers, Requirements, Claims mit differenziertem Evidence Model, Assessment Dimensions, Fit, Red Flags, Commercial Assumptions, IP Dependencies, Vendor Dependency, Regulatory Routing und Decision Drivers.

`technology-offer-gap-set.json` enthält offene technische, evidenzielle, regulatorische, IP-, kommerzielle und Supplier-Fragen mit stabiler `gapId`, Priority, Decision Impact, Evidence Needed und Owner/Source.

`technology-offer-assessment.md` ist die menschenlesbare Vergleichsmatrix plus Synthese.

`technology-offer-question-set.json` enthält den assessment-abgeleiteten Master-Fragenkatalog, mindestens in folgender Form:

```json
{
  "schemaVersion": 1,
  "assessmentAsOf": "YYYY-MM-DD",
  "decisionContext": "...",
  "questions": [
    {
      "id": "Q1",
      "topic": "performance",
      "sourceGapIds": ["G3"],
      "sourceAssessmentRefs": ["offerA.claims.C7"],
      "questionIntent": "Clarify transferability of claimed LoD to the target matrix",
      "audience": "vendor",
      "targetRole": "assay development lead",
      "question": "Please provide the LoD study design and results in the target matrix, including sample count, replicates and acceptance criteria.",
      "vendorWording": null,
      "internalWording": null,
      "priority": "blocking",
      "whyNeeded": "Current LoD evidence is prototype-only and does not establish target-matrix transferability.",
      "decisionImpact": "Could change technical fit from conditional to strong or weak.",
      "expectedEvidence": "study protocol plus raw or summarized replicate-level data",
      "allowUnknown": true,
      "use": ["preRead", "askInMeeting"]
    }
  ]
}
```

Für `audience: both` dürfen `vendorWording` und `internalWording` verwendet werden. In diesem Fall beschreibt `questionIntent` die gemeinsame Sachfrage; die beiden Formulierungen müssen dieselbe Entscheidungslücke adressieren, ohne vertrauliche interne Informationen nach außen zu übertragen.

`technology-offer-question-set.md` enthält:

- kurze Meeting-/Decision-Zielsetzung,
- einen priorisierten Abschnitt **Questions for the Offering Party**,
- einen priorisierten Abschnitt **Questions for Internal Stakeholders**,
- optional **Joint Clarifications** für echte `both`-Fragen,
- je Frage auf Wunsch einen knappen Hinweis auf `whyNeeded` beziehungsweise die erwartete Evidenz,
- einen Abschnitt **Items to close after the meeting** für bewusst nachgelagerte Evidenz oder Commitments.

Der Markdown-Output soll in professioneller Sprache direkt für Meeting-Vorbereitung oder Vorabversand weiterverwendbar sein. Er darf interne Notizen nicht in den Vendor-Abschnitt mischen.

## Routing

- externe Evidenz → `research-to-evidence-note`
- Supplier-QMS → `supplier-quality-medical-device`
- Medical-Device-/IVD-Regulatory → passende Regulatory-Skills
- Patent Landscape → `patent-landscape-analysis`
- konkretes FTO Screening → `freedom-to-operate-assessment`
- strategische Gesamtpassung → `technology-due-diligence`
- schriftlicher Versand ausgewählter Vendor-Fragen → `external-stakeholder-questionnaire`
- bestätigtes Vendor-/Stakeholder-Meeting → `meeting-preparation`
- Zusagen, offene Antworten und Follow-up → `decision-and-follow-up-tracker`

## Memory Path

Persistenzwürdig sind generische Bewertungsdimensionen, Vergleichsheuristiken und die Ableitungslogik von Assessment-Lücken zu Stakeholder-Fragen. Konkrete Preise, vertrauliche Offerten, Vertragsbedingungen, Anbieter-Roadmaps, interne Schwellenwerte und nicht öffentliche Performance-Daten bleiben run-only/projektgebunden.

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
- keine FTO-Schlussfolgerung oder Vertragsrechts-Opinion simuliert wird,
- jede entscheidungsrelevante Frage auf eine konkrete Assessment-Lücke, einen Red Flag, eine Annahme oder offene Entscheidung zurückgeführt werden kann,
- Vendor- und interne Fragen nach Wissensinhaber und Entscheidungskompetenz getrennt sind,
- `both` nur bei echter gemeinsamer Klärung verwendet wird,
- vertrauliche interne Schwellen oder Verhandlungspositionen nicht unbeabsichtigt in Vendor-Fragen erscheinen,
- bereits evidenzbasiert beantwortete Punkte nicht erneut gefragt werden,
- Blocking-/High-Priority-Fragen vor Detailfragen stehen,
- das Question Set ohne Neuerfindung der Assessment-Logik in Meeting Prep oder Vorabversand übernommen werden kann.

## Fehlerbehandlung

Wenn nur Marketingmaterial ohne belastbare Performance- oder Scale-Evidenz vorliegt, bleibt der relevante Fit `unknown` oder `conditional`; die Offerte darf nicht allein daraus als marktreif oder regulatorisch geeignet bezeichnet werden.

Wenn der Fragenkatalog zu einer generischen Checkliste wird, stoppe und leite jede Frage erneut aus Gap Set, Red Flags, Annahmen oder Decision Drivers ab. Wenn der Wissensinhaber unklar ist, markiere `audience` oder `targetRole` als ungeklärt statt die Frage willkürlich extern oder intern zuzuordnen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Anforderungen und Claims vergleichbar normalisiert, Evidence Quality differenziert sichtbar, technische/operative/kommerzielle Fit-Treiber getrennt bewertet, Vendor Dependency statt Strategic Fit erfasst, Red Flags priorisiert und nachgelagerte IP-/Regulatory-/Supplier-Fragen sauber geroutet sind **und** ein priorisierter, assessment-abgeleiteter Fragenkatalog für offerierende Partei und interne Stakeholder vorliegt, dessen Fragen auf ihre Entscheidungsgrundlage zurückverfolgbar sind.
