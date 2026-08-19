---
name: freedom-to-operate-assessment
description: Erstellt für eine definierte Produkt-/Prozesskonfiguration und Zieljurisdiktionen eine evidenzbasierte technische FTO-Vorprüfung mit Claim-by-Claim-Mapping, Legal-Status-Freshness, Screening-Risikokategorien, Unsicherheiten, Counsel-Eskalation und Design-around-Hypothesen; keine anwaltliche FTO Opinion oder verbindliche Claim Construction.
---

# Freedom to Operate Assessment

## Zweck und Grenze

Erzeuge für eine **konkrete** Produkt-/Prozesskonfiguration, Zieljurisdiktionen und relevante wirtschaftliche Handlungen eine technische FTO-Vorprüfung. Der Kern ist ein elementweises Claim Mapping gegen verifizierte oder ausdrücklich unsichere Patentansprüche.

Der Skill liefert **keine anwaltliche FTO Opinion**, keine verbindliche Claim Construction und kein abschließendes Urteil zu Infringement, Validity oder Enforceability. Verwende Formulierungen wie `potential read-on`, `screening concern` oder `no current full read-on identified`.

## Trigger

Verwenden bei FTO-Heatmap, Claim-by-Claim-Mapping, produktbezogener Patentrisikoprüfung in definierten Märkten oder der Suche nach technisch plausiblen Design-around-Optionen.

Nicht verwenden für eine breite Patentlandschaft ohne konkrete Produktbaseline; diese gehört zu `patent-landscape-analysis`.

## Voraussetzungen

Vor dem Claim Mapping fixieren:

1. konkrete Produkt-/Assay-/Prozesskonfiguration,
2. Technical Feature Baseline mit Quellen,
3. Zieljurisdiktionen,
4. relevante Commercial Acts soweit bekannt, z. B. `make`, `use`, `sell`, `offer for sale`, `import`,
5. `asOf`,
6. relevante Patentfamilien, konkrete Claims und Statusquellen,
7. bekannte License-/Ownership-Informationen.

**Scope/Jurisdiktion/asOf fixieren:** Fehlt eine dieser Grundlagen, bleibt die Analyse `GREY` oder partiell; eine globale FTO-Aussage ist unzulässig.

## Workflow

### 1. FTO Scope einfrieren

Erzeuge `fto-scope.json` mit Produktkonfiguration, Technical Feature Baseline, Jurisdiktionen, Commercial Acts, `asOf`, Exclusions und Assumptions. Varianten werden getrennt geführt, wenn sie claim-relevant unterschiedlich sind.

### 2. Relevante Claims auswählen

Konsumiere die Patentlandschaft, prüfe aber für das konkrete Screening einzelne Patent-/Application-Member, Jurisdiktion und Claim-Version. Behandle Family-Level-Relevanz nur als Discovery-Signal.

**Patentfamilie nicht mit einem einzigen Claim Scope gleichsetzen.** Continuations, divisionals, amended claims und jurisdiktionsspezifische Claim Sets werden separat bewertet.

### 3. Claim Elemente zerlegen

Für jeden relevanten Independent Claim dokumentiere:

- Claim-Identifier, Patent/Application und Jurisdiktion,
- granted/pending und verified current status bzw. uncertainty,
- erforderliche Claim-Elemente,
- Product/Process Feature Evidence,
- Mapping je Element: `present | likely-present | absent | unknown | interpretation-dependent`,
- Mapping Confidence und Source References,
- relevante Dependent Claims,
- prosecution-/claim-construction questions,
- Escalation Flag.

Ein Claim darf nur dann als potentieller Full Read-on klassifiziert werden, wenn **alle erforderlichen Elemente** berücksichtigt wurden.

### 4. Granted und Pending trennen

**Pending und granted getrennt halten.** Pending Claims können sich ändern und werden als strategisches zukünftiges Risiko sichtbar gemacht, aber nicht wie ein aktuelles Ausschließlichkeitsrecht behandelt.

### 5. Screening-Risikokategorie vergeben

- **RED — potential full read-on:** alle erforderlichen Elemente eines aktuell relevant erscheinenden Independent Claims sind `present`/`likely-present`, oder nur claim-construction-relevante Auslegung trennt vom Full Read-on. Mandatory Counsel Escalation.
- **AMBER — material uncertainty:** plausible Überschneidung, aber Status, Claim Construction, Produkteigenschaft, Pending Scope oder Prosecution History bleibt entscheidungsrelevant unklar.
- **GREEN — no current full read-on identified:** mindestens ein erforderliches Element ist evidenzbasiert `absent`, oder der konkrete Anspruch ist in der betrachteten Jurisdiktion verifiziert nicht mehr in Kraft.
- **GREY — insufficient evidence:** Scope, Claim Text, Produktkonfiguration oder Status reicht nicht aus.

**GREEN nie als globale Non-Infringement-Freigabe formulieren.** GREEN bezieht sich nur auf die geprüften Claims, Konfiguration, Jurisdiktion, Handlungen und den angegebenen Zeitpunkt.

### 6. Design-around-Hypothesen entwickeln

Design-arounds müssen an ein konkretes notwendiges Claim-Element gebunden sein. Pro Option dokumentiere:

- targeted claim element,
- technische Änderung,
- Plausibilität/Feasibility,
- Performance-Auswirkung,
- Manufacturing-/Scale-Auswirkung,
- Regulatory Impact,
- neue IP/FTO-Fragen,
- benötigte Verifikation/Validation.

Ein Design-around ist keine Freigabe; die geänderte Konfiguration benötigt erneutes Screening.

### 7. Counsel-Eskalationen markieren

Mandatory bei RED, kommerziell relevantem AMBER, unklarer Claim Construction, komplexer Prosecution History, Doctrine-of-Equivalents-/Äquivalenzfragen, unklarer Ownership/License Chain sowie imminent launch oder transaction closing.

## Output-Verträge

`fto-scope.json` enthält die eingefrorene Produkt-/Prozessbaseline, Jurisdiktionen, Commercial Acts, `asOf`, Exclusions und Assumptions.

`fto-claim-map.json` enthält Families/Patent Members/Claims, Elementzerlegung, Feature Mapping, Status/Freshness, Evidence, Screening Risk und Escalation.

`fto-risk-heatmap.md` fasst pro Claim/Jurisdiktion RED/AMBER/GREEN/GREY, entscheidende Elemente, Confidence, Status und nächste Aktion zusammen.

`fto-design-around-options.json` enthält Design-around-Hypothesen mit Target Element, technischem Change, Feasibility, Performance-, Regulatory-, Manufacturing- und New-IP-Impact.

## Legal- und Sicherheitsgrenze

Verbotene Schlussformulierungen sind insbesondere „infringes“, „does not infringe“, „valid“, „invalid“ oder „enforceable“, wenn sie als abschließendes Rechtsurteil gemeint sind. Bei materieller rechtlicher Unsicherheit ist **Mandatory Counsel Escalation** Teil des Outputs.

## Memory Path

Persistenzwürdig sind generische Claim-Mapping-Schemata, Risikokategorien und abstrahierte Design-around-Prüfmuster. Konkrete Legal-Status-Feststellungen, vertrauliche Produktfeatures, License Chains und aktuelle Counsel-Fragen bleiben run-only bzw. projektgebunden und benötigen Source/`asOf`.

## Qualitätsgate

Pass nur wenn:

- **Scope/Jurisdiktion/asOf fixieren** erfolgt ist,
- Claims elementweise statt nur thematisch gemappt werden,
- aktuelle Statusangaben verifiziert oder ausdrücklich unsicher sind,
- **Pending und granted getrennt halten** eingehalten wird,
- Family-Level-Relevanz nicht als Claim-Level-Schluss ersetzt wird,
- **GREEN nie als globale Non-Infringement-Freigabe formulieren** eingehalten wird,
- Counsel-Eskalationen sichtbar sind,
- Design-arounds konkrete notwendige Claim-Elemente adressieren.

## Fehlerbehandlung

Wenn konkrete Claim-Texte, Statusquellen, Jurisdiktion oder Feature Evidence fehlen, stoppe die definitive Klassifizierung und verwende GREY/AMBER mit konkretem Evidence Gap. Ein Aggregator-Label wie `expired` darf niemals allein eine globale Freigabe begründen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Scope und Zeitpunkt eingefroren, alle relevanten Claims elementweise dokumentiert, Risk Categories pro Claim/Jurisdiktion nachvollziehbar, Statusunsicherheiten sichtbar, Design-around-Hypothesen claim-elementbezogen und erforderliche Counsel-Eskalationen eindeutig markiert sind.
