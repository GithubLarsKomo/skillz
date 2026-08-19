---
name: freedom-to-operate-assessment
description: Erstellt für eine definierte Produkt-/Prozesskonfiguration und Zieljurisdiktionen eine evidenzbasierte technische FTO-Vorprüfung mit Claim-by-Claim-Mapping, getrenntem Technical Mapping und Rights Status, Screening-Priorität, Unsicherheiten, Counsel-Eskalation und versionierten Design-around-Hypothesen; keine anwaltliche FTO Opinion oder verbindliche Claim Construction.
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
  - fto-scope.json
  - fto-claim-map.json
  - fto-risk-heatmap.md
  - fto-design-around-options.json
lastEvaluated: 2026-08-19
---

# Freedom to Operate Assessment

## Zweck und Grenze

Erzeuge für eine **konkrete** Produkt-/Prozesskonfiguration, Zieljurisdiktionen und faktisch beschriebene wirtschaftliche Aktivitäten eine technische FTO-Vorprüfung. Der Kern ist ein elementweises Claim Mapping gegen verifizierte oder ausdrücklich unsichere Patentansprüche.

Der Skill liefert **keine anwaltliche FTO Opinion**, keine verbindliche Claim Construction und kein abschließendes Urteil zu Infringement, Validity oder Enforceability. Verwende Formulierungen wie `technical full match`, `screening concern`, `no full technical match identified` oder `status unresolved`.

## Trigger

Verwenden bei FTO-Heatmap, Claim-by-Claim-Mapping, produktbezogener Patentrisikoprüfung in definierten Märkten oder der Suche nach technisch plausiblen Design-around-Optionen.

Nicht verwenden für eine breite Patentlandschaft ohne konkrete Produktbaseline; diese gehört zu `patent-landscape-analysis`.

## Voraussetzungen

Vor dem Claim Mapping fixieren:

1. konkrete Produkt-/Assay-/Prozesskonfiguration mit `configurationId`,
2. Technical Feature Baseline mit Quellen,
3. Zieljurisdiktionen,
4. `commercialActivityContext` als faktische Beschreibung von Herstellung, Import, Angebot, Verkauf, Nutzung oder anderen relevanten Aktivitäten,
5. `asOf`,
6. konkrete Claims und Statusquellen,
7. bekannte License-/Ownership-Informationen.

Relevante Claims dürfen aus `patent-landscape-analysis`, einem von Patent Counsel bereitgestellten Claim Set, Nutzer-/Projektinput oder einem anderen verifizierten Source Set stammen. Eine neue Patentlandschaft ist **keine Voraussetzung**, wenn das relevante Claim Set bereits ausreichend definiert und verifiziert ist.

**Scope/Jurisdiktion/asOf fixieren:** Fehlt eine dieser Grundlagen, bleibt die Analyse partiell oder `INDETERMINATE`; eine globale FTO-Aussage ist unzulässig.

## Workflow

### 1. FTO Scope einfrieren

Erzeuge `fto-scope.json` mit `configurationId`, Produktkonfiguration, Technical Feature Baseline, Jurisdiktionen, `commercialActivityContext`, `asOf`, Exclusions und Assumptions. Varianten werden getrennt geführt, wenn sie claim-relevant unterschiedlich sind.

Der Skill beschreibt Commercial Activities faktisch und bestimmt nicht selbst deren jurisdiktionsspezifische rechtliche Bedeutung, sofern diese nicht durch qualifizierten Counsel oder belastbare Rechtsquelle vorgegeben ist.

### 2. Relevante Claims auswählen

Konsumiere ein verifiziertes Claim Set aus Landscape, Counsel-Input oder anderer geeigneter Quelle und prüfe für das konkrete Screening einzelne Patent-/Application-Member, Jurisdiktion und Claim-Version. Behandle Family-Level-Relevanz nur als Discovery-Signal.

**Patentfamilie nicht mit einem einzigen Claim Scope gleichsetzen.** Continuations, divisionals, amended claims und jurisdiktionsspezifische Claim Sets werden separat bewertet.

### 3. Claim-Elemente zerlegen

Für jeden relevanten Independent Claim dokumentiere:

- Claim-Identifier, Patent/Application und Jurisdiktion,
- granted/pending und verifizierten aktuellen Status bzw. uncertainty,
- erforderliche Claim-Elemente,
- Product/Process Feature Evidence,
- Mapping je Element: `present | likely-present | absent | unknown | interpretation-dependent`,
- Mapping Confidence und Source References,
- relevante Dependent Claims,
- prosecution-/claim-construction questions,
- Escalation Flag.

### 4. Technical Mapping, Rights Status und Priorität getrennt klassifizieren

Pro Claim/Jurisdiktion müssen drei getrennte Achsen geführt werden:

- `technicalMapping`: `FULL_MATCH | PARTIAL_MATCH | NO_FULL_MATCH | INDETERMINATE`
- `rightsStatus`: `GRANTED_CURRENT | PENDING | EXPIRED_OR_LAPSED_VERIFIED | STATUS_UNCERTAIN | NOT_APPLICABLE_IN_JURISDICTION`
- `screeningPriority`: `HIGH | MEDIUM | LOW | UNRESOLVED`

Regeln:

- `FULL_MATCH` nur, wenn **alle erforderlichen Elemente evidenzbasiert `present`** sind.
- Ein `likely-present`, `unknown` oder `interpretation-dependent` verhindert `FULL_MATCH` und führt mindestens zu `INDETERMINATE` oder `PARTIAL_MATCH` mit sichtbarer Unsicherheit.
- `NO_FULL_MATCH` erfordert mindestens ein evidenzbasiert `absent`es notwendiges Element.
- `rightsStatus` wird unabhängig vom technischen Mapping geführt; ein technisch passender Claim kann z. B. `EXPIRED_OR_LAPSED_VERIFIED` sein.
- `screeningPriority` ist eine **Workflow-Priorität**, kein Rechtsurteil. Ein `FULL_MATCH` gegen `GRANTED_CURRENT` ist typischerweise `HIGH`; `STATUS_UNCERTAIN` bleibt `UNRESOLVED`; ein `NO_FULL_MATCH` oder verifiziert nicht anwendbares Recht kann `LOW` sein.

### 5. Granted und Pending trennen

**Pending und granted getrennt halten.** Pending Claims können sich ändern und werden als strategisches zukünftiges Risiko sichtbar gemacht, aber nicht wie ein aktuell erteiltes Ausschließlichkeitsrecht behandelt.

### 6. Design-around-Hypothesen entwickeln

Design-arounds müssen an konkrete notwendige Claim-Elemente und versionierte Produktkonfigurationen gebunden sein. Pro Option dokumentiere mindestens:

- `baselineConfigurationId`,
- `proposedConfigurationId`,
- `targetClaims[]`,
- `targetClaimElements[]`,
- technische Änderung,
- Plausibilität/Feasibility,
- Performance-Auswirkung,
- Manufacturing-/Scale-Auswirkung,
- Regulatory Impact,
- neue IP/FTO-Fragen,
- benötigte Verifikation/Validation,
- `requiresRescreening: true`.

Ein Design-around ist keine Freigabe; die geänderte Konfiguration benötigt erneutes Screening gegen den dokumentierten Claim-Stand.

### 7. Counsel-Eskalationen markieren

Mandatory bei `FULL_MATCH` gegen `GRANTED_CURRENT`, kommerziell relevantem `INDETERMINATE`/`UNRESOLVED`, unklarer Claim Construction, komplexer Prosecution History, Doctrine-of-Equivalents-/Äquivalenzfragen, unklarer Ownership/License Chain sowie imminent launch oder transaction closing.

## Output-Verträge

`fto-scope.json` enthält die eingefrorene Produkt-/Prozessbaseline, `configurationId`, Jurisdiktionen, `commercialActivityContext`, `asOf`, Exclusions und Assumptions.

`fto-claim-map.json` enthält Families/Patent Members/Claims, Elementzerlegung, Feature Mapping, `technicalMapping`, `rightsStatus`, Status/Freshness, Evidence, `screeningPriority` und Escalation.

`fto-risk-heatmap.md` fasst pro Claim/Jurisdiktion Technical Mapping, Rights Status, Screening Priority, entscheidende Elemente, Confidence und nächste Aktion zusammen. Farben dürfen nur die Workflow-Priorität visualisieren, nicht Rechtsstatus oder Infringement behaupten.

`fto-design-around-options.json` enthält versionierte Design-around-Hypothesen mit Baseline-/Proposed-Configuration, Target Claims/Elements, technischem Change, Feasibility, Performance-, Regulatory-, Manufacturing- und New-IP-Impact sowie `requiresRescreening`.

## Legal- und Sicherheitsgrenze

Verbotene Schlussformulierungen sind insbesondere „infringes“, „does not infringe“, „valid“, „invalid“ oder „enforceable“, wenn sie als abschließendes Rechtsurteil gemeint sind. Bei materieller rechtlicher Unsicherheit ist **Mandatory Counsel Escalation** Teil des Outputs.

## Memory Path

Persistenzwürdig sind generische Claim-Mapping-Schemata, getrennte Technical-/Rights-/Priority-Kategorien und abstrahierte Design-around-Prüfmuster. Konkrete Legal-Status-Feststellungen, vertrauliche Produktfeatures, License Chains und aktuelle Counsel-Fragen bleiben run-only bzw. projektgebunden und benötigen Source/`asOf`.

## Qualitätsgate

Pass nur wenn:

- Scope/Jurisdiktion/`asOf` fixiert sind,
- Claims elementweise statt nur thematisch gemappt werden,
- `technicalMapping`, `rightsStatus` und `screeningPriority` getrennt sind,
- `likely-present` niemals allein einen `FULL_MATCH` ermöglicht,
- aktuelle Statusangaben verifiziert oder ausdrücklich unsicher sind,
- Pending und granted getrennt bleiben,
- Family-Level-Relevanz nicht als Claim-Level-Schluss ersetzt wird,
- Counsel-Eskalationen sichtbar sind,
- Design-arounds versionierte Baseline/Proposed Configurations und `requiresRescreening: true` besitzen.

## Fehlerbehandlung

Wenn konkrete Claim-Texte, Statusquellen, Jurisdiktion oder Feature Evidence fehlen, stoppe die definitive Klassifizierung und verwende `INDETERMINATE` und/oder `STATUS_UNCERTAIN` mit konkretem Evidence Gap. Ein Aggregator-Label wie `expired` darf niemals allein eine globale Freigabe begründen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Scope und Zeitpunkt eingefroren, relevante Claims elementweise dokumentiert, Technical Mapping und Rights Status getrennt nachvollziehbar, Screening Priority als Workflow-Priorität begründet, Statusunsicherheiten sichtbar, Design-around-Hypothesen versioniert und erforderliche Counsel-Eskalationen eindeutig markiert sind.