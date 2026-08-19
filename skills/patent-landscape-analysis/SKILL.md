---
name: patent-landscape-analysis
description: Erstellt für eine abgegrenzte Technologiefrage eine evidenzbasierte, nach Patentfamilien deduplizierte Schutzrechtslandschaft mit reproduzierbarer Suchlogik, Search-Saturation, Claim-Scope-Branches, Jurisdiktionen, Legal-Status-Freshness und sauber getrennten Applicant-/Assignee-/Ownership-Daten; keine Patentability- oder FTO-Opinion.
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
lastEvaluated: 2026-08-19
---

# Patent Landscape Analysis

## Zweck und Grenze

Erzeuge für eine klar abgegrenzte Technologiefrage eine reproduzierbare Patentlandschaft. Der Skill strukturiert Recherche, dedupliziert Patentfamilien, hält abweichende Continuation-/Divisional-Claim-Pfade sichtbar und bewertet Status/Freshness evidenzgebunden.

Der Skill ist **keine Patentability-, Validity-, Enforceability- oder FTO-Opinion**. Independent Claims dürfen semantisch thematisiert und für nachgelagerte Analyse markiert werden; verbindliche Claim Construction bleibt Patent Counsel vorbehalten.

## Trigger

Verwenden bei Patentlandschaft, Patentfamilien, Applicant-/Assignee-Landscape, Schutzrechtslage eines Biomarkers oder Assayprinzips, White-Space-Exploration oder der Frage, welche Familien für eine Technologie relevant sind.

Nicht verwenden, wenn bereits ein konkretes Produkt gegen konkrete Claims in Zieljurisdiktionen gemappt werden soll; das gehört zu `freedom-to-operate-assessment`.

## Voraussetzungen

Vor der Suche fixieren:

1. Technologiefrage und Entscheidungskontext,
2. ein- und ausgeschlossene technische Konzepte,
3. Zieljurisdiktionen, soweit entscheidungsrelevant,
4. `asOf`,
5. bekannte Targets/Biomarker, Synonyme, Assay-/Messprinzipien und Akteure,
6. zugängliche Patent- und Registerquellen.

Fehlende Suchabdeckung wird als Gap dokumentiert, nicht durch Vollständigkeitsbehauptungen ersetzt.

## Workflow

### 1. Suchraum zerlegen

Erzeuge Suchfacetten aus Kernbegriffen und Synonymen, Biomarker-/Target-Aliasnamen, Mess-/Assayprinzipien, CPC/IPC-Klassen, Applicant/Assignee/Inventor sowie relevanten Produkten oder Reagenztypen. Trenne Discovery-Begriffe von späteren Ein-/Ausschlusskriterien.

### 2. Iterative Suche dokumentieren

Kombiniere soweit sinnvoll Keyword-, Classification-, Applicant-/Assignee-, Inventor-, Citation- und Family-Relationship-Suchen. Ein einzelner Keyword Search darf nicht als vollständige Landschaft ausgegeben werden.

Für jede Suchiteration dokumentiere Query, Quelle, Datum, Filter, Trefferzahl soweit verfügbar, Ein-/Ausschlusslogik, neu identifizierte `core`-Familien und den Grund für die nächste Iteration.

### 3. Search Saturation und Stop-Regel anwenden

Eine breit angelegte Discovery-Suche darf beendet werden, wenn alle folgenden Bedingungen erfüllt sind:

1. mindestens zwei aufeinanderfolgende sinnvolle Suchiterationen erzeugen keine neuen `core`-Familien,
2. zentrale CPC/IPC-Klassen wurden geprüft,
3. Kern-Applicants/-Assignees sowie Forward-/Backward-Citations der `core`-Familien wurden geprüft, soweit zugänglich,
4. bekannte Synonyme/Targets/Messprinzipien sind abgedeckt,
5. verbleibende High-Value-Suchlücken sind explizit dokumentiert.

Führe im Output:

- `searchSaturation.status`: `reached | partial | not-reached`,
- `searchSaturation.rationale`,
- `searchSaturation.remainingHighValueSearches[]`.

Saturation ist eine methodische Stop-Regel, keine Garantie vollständiger Patentabdeckung.

### 4. Patentfamilien normalisieren

Gruppiere Publikationen anhand dokumentierter Priority-/Family-Beziehungen. Pro Familie erfasse mindestens:

- `familyId`, `representativePublication`, `earliestPriority`,
- `priorityApplications[]`, `members[]`,
- `applicants[]`, `recordedAssignees[]`, `inventors[]`, `jurisdictions[]`,
- `currentOwnership { value, verified, asOf, source }`,
- `legalStatus[]` mit `asOf` und Source,
- `independentClaimThemes[]`, `technologyTags[]`,
- `relevance` als `core | adjacent | contextual | excluded`,
- `relevanceRationale`, `statusUncertainties[]`.

**Applicant, recorded assignee und current ownership nicht gleichsetzen.** Bibliografische Assignee-Angaben dürfen nicht als verifizierte aktuelle Rechteinhaberschaft dargestellt werden. `currentOwnership.verified` bleibt `false`, solange keine geeignete aktuelle Ownership-/Assignment-Evidenz vorliegt.

**Continuation-/Divisional-Strukturen separat halten:** gemeinsame Priorität darf unterschiedliche Independent-Claim-Scope-Pfade nicht unsichtbar machen. Wo eine Familie mehrere substantiell unterschiedliche Anspruchspfade besitzt, dokumentiere diese als separate `claimScopeBranches` innerhalb der Familie.

### 5. Status nach Relevanz-Tier prüfen

Für bibliografische Discovery dürfen Aggregatoren genutzt werden. Entscheidungsrelevanter Legal Status wird bevorzugt anhand aktueller offizieller Patentamt-/Registerquellen verifiziert.

- `core`: offizielle Statusverifikation, soweit entscheidungsrelevant und zugänglich,
- `adjacent`: vertiefen, wenn der Status Schlussfolgerungen ändern kann,
- `contextual`: bibliografischer/discovery-level Status genügt normalerweise,
- `excluded`: kein Status-Deep-Dive.

Ein Aggregatorstatus allein ist keine abschließende Statusfeststellung. Wenn Quellen kollidieren, markiere `statusUncertainties[]`, dokumentiere beide Quellen und senke die Confidence. Zeitabhängige Statusaussagen benötigen immer `asOf`.

### 6. Claim-Themen extrahieren

Fasse Independent Claims semantisch in atomare Themen zusammen, zum Beispiel Target/Biomarker, Reagent/Antibody, Sample, Assay Format, Detection Principle, Signal Processing oder Workflow Steps. Patentfamilie und Claim Scope dürfen nicht gleichgesetzt werden.

Kennzeichne relevante Claim-Elemente, die ein nachgelagertes FTO-Screening prüfen sollte, ohne selbst Read-on oder Infringement festzustellen.

### 7. Landscape synthetisieren

Erzeuge Technology Clusters, Applicant-/Assignee Map, Jurisdiction Coverage, zeitliche Prioritätslinien und Suchlücken. White Spaces sind als **Recherchehypothesen** zu formulieren, nicht als gesicherte Patentfreiheit.

## Output-Verträge

`patent-landscape.json` enthält mindestens:

```json
{
  "scope": {},
  "asOf": "YYYY-MM-DD",
  "searchCoverage": [],
  "searchSaturation": {
    "status": "reached|partial|not-reached",
    "rationale": "",
    "remainingHighValueSearches": []
  },
  "families": [],
  "applicantAssigneeMap": [],
  "technologyClusters": [],
  "jurisdictionCoverage": [],
  "statusUncertainties": [],
  "openSearchQuestions": []
}
```

`patent-search-log.json` enthält jede Suchiteration mit Quelle, Query, Datum, Filtern, Ergebnisumfang soweit verfügbar, neuen `core`-Familien, In-/Exclusion-Entscheidungen und Iterationsgrund.

`patent-landscape.md` ist die menschenlesbare Synthese mit Scope, Methodik, Search Saturation, Kernfamilien, Claim-Themen, Status/Freshness, Ownership-Uncertainty, Clustern, Suchlücken und Grenzen.

## Routing

- Evidenzsynthese und Quellenqualität → `research-to-evidence-note`
- konkrete produktbezogene Claim-by-Claim-Prüfung → `freedom-to-operate-assessment`
- regulatorische Bewertung → bestehende Regulatory-Specialist-Skills
- rechtliche Claim Construction, Validity oder Enforceability → qualifizierter Patent Counsel

## Memory Path

Persistenzwürdig sind generische Suchheuristiken, Saturation-Regeln, Family-Normalisierungsregeln und abstrahierte Clusterlogik. Konkrete aktuelle Legal-Status-/Ownership-Feststellungen, vertrauliche Produktbezüge und ungeprüfte Ownership-Hypothesen bleiben run-only bzw. benötigen `asOf` und Source References.

## Qualitätsgate

Pass nur wenn:

- Suchstrategie reproduzierbar dokumentiert ist,
- `searchSaturation` explizit begründet ist,
- Familien nachvollziehbar dedupliziert sind,
- Applicant/recorded Assignee/current Ownership getrennt bleiben,
- relevante Continuation-/Divisional-Strukturen separat bleiben,
- aktuelle Statusaussagen Freshness und Source besitzen,
- Status-Deep-Dive nach Relevanz-Tier erfolgt statt undifferenziert über alle Treffer,
- Patentfamilie und Claim Scope nicht gleichgesetzt werden,
- keine FTO-/Validity-/Patentability-Opinion simuliert wird.

## Fehlerbehandlung

Wenn offizielle Statusquellen fehlen, die Family-Struktur unklar ist oder Suchfacetten große Lücken aufweisen, liefere eine partielle Landschaft mit expliziter Coverage, `searchSaturation.status = partial|not-reached` und offenen Fragen. Keine scheinbare Vollständigkeit erzeugen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Scope und `asOf` fixiert, Suchiterationen nachvollziehbar, Search Saturation begründet, relevante Familien und Claim-Scope-Branches strukturiert, Applicant/Assignee/Ownership sauber getrennt, Statusunsicherheiten sichtbar und Suchlücken dokumentiert sind.