---
name: talent-search-strategy
description: Übersetzt einen operationalisierten Rollen-Search-Brief in eine überprüfbare Talent-Search-Strategie mit Zielunternehmen, angrenzenden Talent Pools, Rollenfamilien, Karrierepfaden, Suchhypothesen und Lernschleifen. Verwenden, wenn geklärt werden soll, wo geeignete Führungskräfte oder Experten wahrscheinlich zu finden sind, ohne bereits konkrete Personen zu bewerten oder Suchergebnisse als Eignungsnachweis zu behandeln.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - executive-role-search-brief
outputs:
  - talent-search-strategy.json
  - talent-search-strategy.md
  - target-company-map.json
  - search-hypotheses.json
lastEvaluated: 2026-08-20
---

# Talent Search Strategy

## Zweck und Grenze

Erzeuge aus einem operationalisierten `role-search-brief` eine explizite, prüfbare Strategie dafür, **wo und nach welchen beruflichen Mustern** relevante Personen wahrscheinlich gefunden werden können.

Der Skill beantwortet ausschließlich:

> **Where might suitable people be found?**

Er ist **keine Personenrecherche, kein Scraper, kein Candidate Ranking, kein automatisches Sourcing-System und kein Ersatz für professionelle Person Research**.

Konkrete Namen können als Discovery Candidates oder Beispiele auftauchen, wenn Retrieval dies ergibt; sie sind jedoch kein Rollenfit-Nachweis. Sobald eine Person substanziell bewertet oder profiliert werden soll, erfolgt die Übergabe an `professional-person-research`.

## Trigger

Verwenden, wenn:

- für eine Führungs- oder Expertenrolle ein systematischer Suchraum entwickelt werden soll,
- relevante Target Companies oder Adjacent Companies identifiziert werden müssen,
- alternative Rollenfamilien oder Karrierepfade für die Suche benötigt werden,
- eine bestehende Suche zu eng oder ergebnisarm ist,
- Suchhypothesen explizit getestet und nach Research-Ergebnissen angepasst werden sollen.

Nicht verwenden, wenn die Rolle selbst noch diffus ist; dann zuerst `executive-role-search-brief` beziehungsweise Grilling.

## Voraussetzungen

Benötigt mindestens:

1. `role-search-brief.json`,
2. Mission und erwartete Outcomes,
3. operationalisierte `essential`- und relevante `strongly-preferred`-Kriterien,
4. bekannte Standort-, Markt-, Sprach- oder Branchenconstraints.

Suchräume dürfen nicht aus geschützten persönlichen Merkmalen abgeleitet werden.

## Strategieebenen

### 1. Core Target Companies

Unternehmen, deren Geschäftsmodell, Technologie, Markt oder Organisationssituation relevante Erfahrungen wahrscheinlich erzeugt.

Bewertungsdimensionen können sein:

- Branche und Produktkategorie,
- Technologieplattform,
- Geschäftsmodell,
- Unternehmensgröße,
- Go-to-Market-Modell,
- Internationalität,
- regulatorisches Umfeld,
- Wachstums-/Turnaround-/Integrationskontext,
- Eigentümerstruktur, soweit rollenrelevant.

Ein Target Company Record benötigt immer eine Begründung bezogen auf Rollen-Kriterien.

### 2. Adjacent Talent Pools

Suche bewusst auch angrenzende Branchen und Unternehmen, wenn die geforderten Capabilities dort plausibel entstehen können.

Beispiel:

Eine IVD-Geschäftsführungsrolle kann neben klassischen IVD-Herstellern auch relevante Talent Pools in:

- Life-Science-Instrumentierung,
- Lab Automation,
- Diagnostics Software,
- MedTech mit ähnlichem regulatorischem und internationalen Vertriebsmodell,
- Specialty Diagnostics,
- Contract Development/Manufacturing

haben, sofern die Abweichungen explizit dokumentiert sind.

### 3. Role Families

Nicht nur exakte Zieljobtitel suchen.

Je nach Rollenmission können relevante Familien sein:

- CEO,
- Managing Director,
- General Manager,
- Business Unit Leader,
- COO,
- CTO,
- CSO,
- VP R&D,
- VP Operations,
- VP Commercial,
- Head of Diagnostics,
- Scientific Director,
- Technical Director.

Die Auswahl wird aus den geforderten Capabilities hergeleitet.

### 4. Career Patterns

Formuliere Karrierepfade als Suchhypothesen, z. B.:

```text
technical expert → R&D leader → business unit leader
commercial leader → regional GM → global commercial leadership
operations leader → site leader → COO
scientist → product development → technology leadership
```

Diese Muster dienen Discovery, nicht als normative Karriereanforderung.

## Search Hypothesis Model

Jede substanzielle Suchannahme wird als Hypothese dokumentiert:

```json
{
  "id": "H1",
  "hypothesis": "Mid-sized European IVD manufacturers are likely to contain leaders combining technical depth with international commercial exposure.",
  "linkedCriteria": ["R2", "R5"],
  "targets": [],
  "rationale": [],
  "evidence": [],
  "status": "untested"
}
```

Zulässige Status:

- `untested`
- `supported`
- `partially-supported`
- `rejected`

Keine Hypothese wird allein aufgrund plausibler Branchenintuition als `supported` markiert.

## Target Company Model

Beispiel:

```json
{
  "company": "Example Diagnostics",
  "poolType": "core",
  "relevance": [
    {
      "criterionId": "R3",
      "reason": "Develops and internationally commercializes regulated immunoassays."
    }
  ],
  "knownLimitations": [
    "company scale larger than target"
  ],
  "sourceRefs": []
}
```

Die Quelle für Company-Eigenschaften muss nachvollziehbar bleiben, sobald konkrete Unternehmen genannt werden.

## Discovery Queries

Aus Rollen-Kriterien dürfen Suchmuster abgeleitet werden, z. B. Kombinationen aus:

- Rolle,
- Technologie,
- Produkt,
- Unternehmen,
- Region,
- Transformationserfahrung,
- Market-/Commercial-Scope.

Keine Query-Strategie darf sensible Merkmale oder Alters-/Geschlechtsproxies enthalten.

## Search Breadth

Plane mindestens drei Ebenen, sofern der Auftrag nicht bewusst enger ist:

1. `core` — sehr nahe Branchen-/Rollenpassung,
2. `adjacent` — übertragbare Capabilities bei moderater Distanz,
3. `wildcard` — weniger offensichtliche, aber begründete Talent Pools.

Wildcard bedeutet nicht beliebig. Jede Erweiterung benötigt einen Bezug zu konkreten Rollen-Kriterien.

## Search Learning Loop

Der Skill ist iterativ.

Nach mehreren Person-Research-Artefakten oder Discovery-Runden werden Suchhypothesen geprüft.

Beispiele:

- Core IVD R&D Leaders liefern technische Tiefe, aber selten P&L → zusätzliche GM-/BU-Pools öffnen.
- Große Konzerne liefern internationale Erfahrung, aber wenig Mittelstands-Scope → Target Company Size Segment anpassen.
- Gewünschte Kombination aus Wissenschaft und Commercial findet sich häufiger in Specialty-Diagnostics-BU-Leitern → Hypothese aktualisieren.

Diese Erkenntnisse verändern die **Search Strategy**, nicht rückwirkend Personenfakten oder Rollenanforderungen.

## Stop Conditions

Eine Search Strategy ist nicht dadurch fertig, dass viele Namen gefunden wurden.

Stop beziehungsweise Review auslösen, wenn:

- Core/Adjacent/Wildcard Pools ausreichend abgedeckt sind,
- neue Quellen nur noch redundante Unternehmen/Rollen liefern,
- zentrale Kriterien in keinem Pool plausibel erreichbar erscheinen,
- Constraints den Suchraum faktisch leer machen,
- Person Research wiederholt dieselbe systematische Evidence Gap zeigt.

Im letzten Fall den Search Brief oder die Hypothesen überprüfen, statt unendlich weiterzusuchen.

## Ausgabe

`talent-search-strategy.json`:

```json
{
  "schemaVersion": 1,
  "roleRef": "role-search-brief.json",
  "strategyAsOf": "YYYY-MM-DD",
  "searchPrinciples": [],
  "targetPools": {
    "core": [],
    "adjacent": [],
    "wildcard": []
  },
  "roleFamilies": [],
  "careerPatterns": [],
  "searchHypotheses": [],
  "discoveryQueries": [],
  "constraints": [],
  "exclusions": [],
  "learningLog": [],
  "openQuestions": []
}
```

`target-company-map.json` enthält konkrete Company-Pools mit Kriterienbezug, Quellen und Limitierungen.

`search-hypotheses.json` enthält Hypothesen, Status, Evidenz und Lernverlauf.

`talent-search-strategy.md` ist die menschlich lesbare Search Map.

## Person Discovery Boundary

Wenn konkrete Personen als Ergebnis einer Suche auftauchen, dürfen zunächst nur minimale Discovery-Daten übernommen werden, z. B.:

- Name,
- aktuelle/letzte öffentlich belegte Rolle,
- Organisation,
- Discovery-Grund,
- Quellenreferenz.

Keine umfangreiche Capability-Bewertung im Search-Strategy-Artefakt.

Übergabe konkreter Personen:

```text
Discovery Candidate
       ↓
professional-person-research
```

## Fairness und Datenschutz

Search Pools beruhen ausschließlich auf professionell relevanten Kriterien.

Nicht verwenden:

- Alter oder Abschlussjahr als Senioritätsproxy,
- Geschlecht,
- ethnische Zugehörigkeit,
- Nationalität, sofern nicht eine rechtlich/operativ legitime Arbeitserlaubnisfrage separat geklärt werden muss,
- Familienstatus,
- Religion,
- Gesundheit,
- politische Überzeugungen,
- sonstige geschützte Merkmale.

Geografische Constraints werden als reale Rollenconstraints behandelt, nicht als Proxy für Herkunft oder Nationalität.

## Prüfungen

Vor Übergabe prüfen:

- jeder Target Pool ist an Rollen-Kriterien rückgebunden,
- Core, Adjacent und Wildcard sind nachvollziehbar getrennt,
- Rollenfamilien sind nicht nur Synonyme des Zieltitels,
- Suchhypothesen besitzen Status und prüfbare Evidenzlogik,
- konkrete Unternehmen haben Quellenbezug, sobald ihre Eigenschaften behauptet werden,
- konkrete Personen werden nicht bereits gerankt oder profiliert,
- Search Learning verändert Strategie, nicht historische Personen-Evidenz,
- keine sensiblen oder geschützten Merkmale strukturieren die Suche.

## Fehlerbehandlung

### Zu enger Search Brief

Wenn Constraints praktisch keinen plausiblen Pool übrig lassen, dokumentiere den Engpass und route zur Rollen-/Constraint-Prüfung zurück.

### Zu breiter Search Space

Wenn nahezu jede Branche oder Rolle eingeschlossen würde, priorisiere nach Essential Criteria und trenne Core/Adjacent/Wildcard sauber.

### Quellenarme Unternehmensannahmen

Wenn ein Target Company Fit nur aus Markenimage oder Bekanntheit stammt, nicht als bestätigte Company-Eigenschaft behandeln. Recherchiere oder markiere als Hypothese.

### Candidate Drift

Wenn während Strategy-Arbeit detaillierte Personenbewertung beginnt, stoppe diese und übergebe die Person an `professional-person-research`.

## Übergaben

Geeignete nachgelagerte Verbraucher:

- `professional-person-research` für konkrete Discovery Candidates,
- `role-capability-evidence-map` nach abgeschlossener Personenrecherche,
- `executive-role-search-brief` bei strukturell unerfüllbaren oder unklaren Anforderungen,
- `decision-record` für wesentliche Änderungen an der Suchstrategie.

## Qualitätsfälle

### Happy Path

Ein Search Brief verlangt internationale IVD-Erfahrung, technische Glaubwürdigkeit und Geschäftsverantwortung. Ergebnis: Core-Pool aus IVD-Unternehmen, Adjacent-Pools aus Lab Automation und Specialty Diagnostics, mehrere begründete Rollenfamilien und überprüfbare Karrierehypothesen.

### Grenzfall

Die Rolle kombiniert sehr tiefe wissenschaftliche Expertise mit voller CEO-P&L-Erfahrung in einem kleinen Mittelständler. Ergebnis: mehrere alternative Talent Pools und Karrierepfade; die Seltenheit der Kombination wird als Search-Risiko dokumentiert, nicht durch weichere heimliche Kriterien kaschiert.

### Fehlerfall

Eine vorgeschlagene Strategie sucht bevorzugt Personen unter 45 Jahren, verwendet nur exakte CEO-Titel und erklärt prominente Unternehmen ohne Quellen automatisch zu Top Targets. Stoppe und korrigiere Fairness, Rollenfamilienlogik und Evidence-Anforderungen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn ein rollenbezogener, begründeter und überprüfbarer Suchraum mit Core-/Adjacent-/Wildcard-Pools, Rollenfamilien, Karrierepfaden und Search Hypotheses vorliegt, konkrete Personen sauber an Professional Person Research übergeben werden können und die Strategie anhand späterer Evidenz iteriert werden kann, ohne Candidate Ranking oder diskriminierende Suchlogik einzuführen.
