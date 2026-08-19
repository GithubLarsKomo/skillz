---
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
lastEvaluated: 2026-08-19
---

# Patent Landscape Analysis

## Zweck und Grenze

Erzeuge für eine klar abgegrenzte Technologiefrage eine reproduzierbare Patentlandschaft. Der Skill strukturiert Recherche, dedupliziert Patentfamilien, hält abweichende Continuation-/Divisional-Claim-Pfade sichtbar und bewertet Status/Freshness evidenzgebunden.

Der Skill ist **keine Patentability-, Validity-, Enforceability- oder FTO-Opinion**. Independent Claims dürfen semantisch thematisiert und für nachgelagerte Analyse markiert werden; verbindliche Claim Construction bleibt Patent Counsel vorbehalten.

## Trigger

Verwenden bei Patentlandschaft, Patentfamilien, Assignee-/Applicant-Landscape, Schutzrechtslage eines Biomarkers oder Assayprinzips, White-Space-Exploration oder der Frage, welche Familien für eine Technologie relevant sind.

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

Für jede Suchiteration dokumentiere Query, Quelle, Datum, Filter, Trefferzahl soweit verfügbar, Ein-/Ausschlusslogik und den Grund für die nächste Iteration.

### 3. Patentfamilien normalisieren

Gruppiere Publikationen anhand dokumentierter Priority-/Family-Beziehungen. Pro Familie erfasse mindestens:

- `familyId`, `representativePublication`, `earliestPriority`,
- `priorityApplications[]`, `members[]`,
- `assignees[]`, `inventors[]`, `jurisdictions[]`,
- `legalStatus[]` mit `asOf` und Source,
- `independentClaimThemes[]`, `technologyTags[]`,
- `relevance` als `core | adjacent | contextual | excluded`,
- `relevanceRationale`, `statusUncertainties[]`.

**Continuation-/Divisional-Strukturen separat halten:** gemeinsame Priorität darf unterschiedliche Independent-Claim-Scope-Pfade nicht unsichtbar machen. Wo eine Familie mehrere substantiell unterschiedliche Anspruchspfade besitzt, dokumentiere diese als separate `claimScopeBranches` innerhalb der Familie.

### 4. Status mit Quellenhierarchie prüfen

Für bibliografische Discovery dürfen Aggregatoren genutzt werden. Entscheidungsrelevanter Legal Status wird jedoch bevorzugt anhand aktueller offizieller Patentamt-/Registerquellen verifiziert. Ein Aggregatorstatus allein ist keine abschließende Statusfeststellung.

Wenn Quellen kollidieren, markiere `statusUncertainties[]`, dokumentiere beide Quellen und senke die Confidence. Zeitabhängige Statusaussagen benötigen immer `asOf`.

### 5. Claim-Themen extrahieren

Fasse Independent Claims semantisch in atomare Themen zusammen, zum Beispiel Target/Biomarker, Reagent/Antibody, Sample, Assay Format, Detection Principle, Signal Processing oder Workflow Steps. Patentfamilie und Claim Scope dürfen nicht gleichgesetzt werden.

Kennzeichne relevante Claim-Elemente, die ein nachgelagertes FTO-Screening prüfen sollte, ohne selbst Read-on oder Infringement festzustellen.

### 6. Landscape synthetisieren

Erzeuge Technology Clusters, Assignee Map, Jurisdiction Coverage, zeitliche Prioritätslinien und Suchlücken. White Spaces sind als **Recherchehypothesen** zu formulieren, nicht als gesicherte Patentfreiheit.

## Output-Verträge

`patent-landscape.json` enthält mindestens:

```json
{
  "scope": {},
  "asOf": "YYYY-MM-DD",
  "searchCoverage": [],
  "families": [],
  "assigneeMap": [],
  "technologyClusters": [],
  "jurisdictionCoverage": [],
  "statusUncertainties": [],
  "openSearchQuestions": []
}
```

`patent-search-log.json` enthält jede Suchiteration mit Quelle, Query, Datum, Filtern, Ergebnisumfang soweit verfügbar, In-/Exclusion-Entscheidungen und Iterationsgrund.

`patent-landscape.md` ist die menschenlesbare Synthese mit Scope, Methodik, Kernfamilien, Claim-Themen, Status/Freshness, Clustern, Suchlücken und Grenzen.

## Routing

- Evidenzsynthese und Quellenqualität → `research-to-evidence-note`
- konkrete produktbezogene Claim-by-Claim-Prüfung → `freedom-to-operate-assessment`
- regulatorische Bewertung → bestehende Regulatory-Specialist-Skills
- rechtliche Claim Construction, Validity oder Enforceability → qualifizierter Patent Counsel

## Memory Path

Persistenzwürdig sind generische Suchheuristiken, Family-Normalisierungsregeln und abstrahierte Clusterlogik. Konkrete aktuelle Legal-Status-Feststellungen, vertrauliche Produktbezüge und ungeprüfte Assignee-/Ownership-Hypothesen bleiben run-only bzw. benötigen `asOf` und Source References.

## Qualitätsgate

Pass nur wenn:

- **Suchstrategie reproduzierbar dokumentiert** ist,
- Familien nachvollziehbar dedupliziert sind,
- relevante **Continuation-/Divisional-Strukturen separat halten** und nicht verschluckt werden,
- aktuelle Statusaussagen Freshness und Source besitzen,
- **Patentfamilie und Claim Scope dürfen nicht gleichgesetzt werden**,
- Aggregatorstatus bei entscheidungsrelevantem Konflikt nicht die Primärquelle ersetzt,
- keine FTO-/Validity-/Patentability-Opinion simuliert wird.

## Fehlerbehandlung

Wenn offizielle Statusquellen fehlen, die Family-Struktur unklar ist oder Suchfacetten große Lücken aufweisen, liefere eine partielle Landschaft mit expliziter Coverage und offenen Fragen. Keine scheinbare Vollständigkeit erzeugen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Scope und `asOf` fixiert, Suchiterationen nachvollziehbar, relevante Familien und Claim-Scope-Branches strukturiert, Statusunsicherheiten sichtbar und Suchlücken so dokumentiert sind, dass ein nachgelagertes FTO-Screening ohne erneute Grundlageninventur starten kann.
