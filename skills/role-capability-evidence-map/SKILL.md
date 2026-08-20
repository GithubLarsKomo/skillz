---
name: role-capability-evidence-map
description: Ordnet einen operationalisierten Rollen-Search-Brief und ein evidenzbasiertes professionelles Personenprofil kriteriumsweise zusammen und erzeugt eine nachvollziehbare Capability-Evidence-Matrix mit Stärken, Lücken, Widersprüchen und Interviewbedarf. Verwenden, wenn öffentlich belegbare berufliche Evidenz gegen konkrete Rollenanforderungen gestellt werden soll, ohne Candidate-Ranking, Persönlichkeitsbewertung oder Einstellungsentscheidung zu erzeugen.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - executive-role-search-brief
  - professional-person-research
outputs:
  - role-capability-map.json
  - role-capability-map.md
  - evidence-gaps.json
lastEvaluated: 2026-08-20
---

# Role Capability Evidence Map

## Zweck und Grenze

Vergleiche einen freigegebenen beziehungsweise ausreichend operationalisierten `role-search-brief` mit einem belastbaren `person-professional-profile` und ordne vorhandene berufliche Evidenz den konkreten Rollenanforderungen zu.

Der Skill beantwortet ausschließlich:

> **How does the available professional evidence relate to this role?**

Er ist **kein Candidate Ranking, kein automatisches Shortlisting, keine Einstellungsentscheidung, keine Persönlichkeitsdiagnostik und keine Quelle neuer Personenfakten**.

Neue Fakten oder Capabilities über die Person werden nicht erfunden. Wenn für eine Anforderung zusätzliche Personenrecherche nötig ist, wird diese als Research Gap an `professional-person-research` zurückgegeben.

## Trigger

Verwenden, wenn:

- ein operationalisierter Search Brief und ein professionelles Personenprofil vorliegen,
- für eine konkrete Person die Evidenzlage zu Rollenanforderungen sichtbar gemacht werden soll,
- öffentliche Evidenzlücken von echten Gegenindikatoren getrennt werden müssen,
- ein nachgelagerter Interviewplan aus offenen Kriterien entstehen soll,
- mehrere Personen später gegen dieselben Kriterien vergleichbar gemacht werden sollen, ohne vorab einen Gesamtscore zu erzeugen.

Nicht verwenden, wenn noch keine belastbaren Rollenanforderungen vorliegen oder die Person noch nicht sauber recherchiert wurde.

## Voraussetzungen

Benötigt mindestens:

1. `role-search-brief.json` oder äquivalent bestätigte, operationalisierte Rollenanforderungen,
2. `person-professional-profile.json`,
3. zugehörige Claim-/Source-Provenance aus `person-evidence-note.json` beziehungsweise `person-source-register.json`, soweit für die Bewertung erforderlich.

Wenn eines der beiden Kernartefakte wesentliche strukturelle Lücken enthält, keine scheinpräzise Fit-Aussage erzeugen. Stattdessen Teilresultat plus konkrete Rückgabe an den zuständigen Upstream-Skill.

## Bewertungsprinzip

Bewerte **nicht die Person als Ganzes**, sondern jedes Rollen-Kriterium separat gegen die tatsächlich vorhandene Evidenz.

Zulässige Assessment States:

- `strongly-evidenced`
- `partially-evidenced`
- `not-evidenced`
- `contradictory-evidence`
- `not-assessable-from-public-evidence`

Optional kann ein Kriterium zusätzlich `research-incomplete` tragen, wenn die vorhandene Personenrecherche erkennbar nicht ausreicht, obwohl öffentlich prüfbare Evidenz grundsätzlich möglich wäre.

Diese Zustände sind keine Wahrscheinlichkeiten und kein Ranking.

## Kernregeln

### 1. Requirement vor Evidence

Jede Zuordnung beginnt beim Rollen-Kriterium aus `role-search-brief`.

Keine nachträgliche Umdefinition der Rolle, nur weil eine Person andere interessante Stärken besitzt.

### 2. Evidence vor Interpretation

Jede positive oder negative Zuordnung benötigt konkrete `claimRefs` beziehungsweise nachvollziehbare Quellenreferenzen.

### 3. `not-evidenced` ist keine Negation

`not-evidenced` bedeutet ausschließlich:

> In der vorliegenden Evidenzbasis wurde das Kriterium nicht hinreichend belegt.

Es bedeutet nicht:

> Die Person besitzt diese Fähigkeit nicht.

### 4. Anti-Evidence nur bei echter Gegenindikation

`antiEvidence` aus dem Rollenbrief oder explizit widersprechende Personen-Claims dürfen zu `contradictory-evidence` führen.

Nicht gefundene positive Evidenz ist keine Anti-Evidence.

### 5. Öffentliche vs. Interview-only Kriterien

Wenn ein Kriterium im Rollenbrief als `interviewOnly: true` markiert ist oder typischerweise nicht fair aus öffentlichen Quellen bewertet werden kann, verwende `not-assessable-from-public-evidence` und erzeuge eine saubere Interviewfrage statt spekulativer Ableitung.

### 6. Keine versteckte Gesamtwertung

Kein numerischer oder ordinaler Gesamtscore wie:

- `84 % match`,
- `A candidate`,
- `top fit`,
- `rank 1 of 5`.

Auch eine implizite Rangfolge aus gewichteten Kriterien ist nicht Teil dieses Skills.

## Mapping-Ablauf

### Schritt 1 — Kriterienbasis fixieren

Übernimm aus dem Search Brief für jedes relevante Kriterium:

- `id`,
- `criterion`,
- `priority`,
- `rationale`,
- `evidenceQuestions`,
- `acceptableEvidence`,
- `antiEvidence`,
- `interviewOnly`.

Kriterien nicht umbenennen oder verschärfen, ohne die Änderung als neuen Rollenbrief zu behandeln.

### Schritt 2 — Relevante Personen-Claims auswählen

Ordne nur Claims zu, die sachlich auf die Evidence Questions einzahlen.

Beispiele:

- internationale Commercial-Verantwortung → Regionen, Sales-/GM-Scope, Launch-/Expansion-Claims,
- R&D Leadership → dokumentierte R&D-Rollen, Team-/Programmverantwortung, Produktentwicklungsclaims,
- P&L → explizit belegte Ergebnis-/BU-/Geschäftsverantwortung,
- Turnaround → konkrete Restrukturierungs-/Sanierungsverantwortung, nicht bloße Anwesenheit während einer Restrukturierung.

### Schritt 3 — Assessment State vergeben

#### `strongly-evidenced`

Verwenden, wenn mehrere belastbare Claims oder ein sehr starker direkter Claim die Evidence Questions klar beantworten und keine wesentlichen Widersprüche vorliegen.

#### `partially-evidenced`

Verwenden, wenn Evidenz relevant, aber Scope, Tiefe, Aktualität oder Attribution unvollständig ist.

#### `not-evidenced`

Verwenden, wenn die aktuelle Evidenzbasis keine hinreichende Unterstützung enthält und keine echte Gegenindikation belegt ist.

#### `contradictory-evidence`

Verwenden, wenn relevante Claims oder Quellen dem Kriterium oder einander substanziell widersprechen.

#### `not-assessable-from-public-evidence`

Verwenden, wenn die Anforderung aus öffentlichen Informationen nicht belastbar oder nicht fair beurteilbar ist.

### Schritt 4 — Confidence getrennt halten

Für die Zuordnung `confidence` als `high`, `medium` oder `low` vergeben.

Confidence bezieht sich auf die **Qualität der Zuordnung**, nicht auf die Wahrscheinlichkeit, dass die Person erfolgreich wäre.

### Schritt 5 — Gap Type bestimmen

Jede offene Stelle wird typisiert:

- `research-gap` — öffentlich prüfbare Information wurde noch nicht ausreichend recherchiert,
- `public-evidence-gap` — trotz angemessener Recherche keine belastbare öffentliche Evidenz gefunden,
- `interview-gap` — sollte im Gespräch geklärt werden,
- `reference-gap` — sinnvoll erst über Referenzen oder bestätigte Drittinformationen klärbar,
- `role-definition-gap` — Anforderung selbst noch nicht ausreichend definiert.

### Schritt 6 — Nächste Aktion routen

- `research-gap` → `professional-person-research`
- `role-definition-gap` → `executive-role-search-brief` beziehungsweise `round-based-requirements-grilling`
- `interview-gap` → `candidate-interview-evidence-plan`
- `reference-gap` → spätere Referenzprüfungs-Capability

## Capability-Provenance

Eine vorhandene `derived-capability` aus dem Personenprofil darf verwendet werden, sofern ihre zugrunde liegenden `claimRefs` erhalten bleiben.

Die Traceability lautet:

```text
SOURCE
  ↓
CLAIM
  ↓
CAPABILITY
  ↓
ROLE CRITERION
  ↓
ASSESSMENT
```

Kein Assessment ohne nachvollziehbare Rückverfolgung mindestens bis zu Claims.

## Beispiel

Rollenanforderung:

```json
{
  "id": "R4",
  "criterion": "direct P&L responsibility",
  "priority": "essential",
  "evidenceQuestions": [
    "Was direct revenue and profit responsibility documented?",
    "Was the person responsible for a business unit or legal entity with explicit financial accountability?"
  ],
  "interviewOnly": false
}
```

Personenevidenz:

```text
C17: General Manager of Business Unit X.
C18: Company biography states responsibility for global sales and operations.
C19: No public source found that explicitly states P&L ownership.
```

Zulässiges Ergebnis:

```json
{
  "criterionId": "R4",
  "assessment": "partially-evidenced",
  "confidence": "medium",
  "supportingClaimRefs": ["C17", "C18"],
  "contradictingClaimRefs": [],
  "reasoning": "Business-unit scope is documented, but explicit P&L ownership is not established.",
  "gaps": [
    {
      "type": "interview-gap",
      "question": "What direct revenue, margin and P&L accountability did you hold in this role?"
    }
  ]
}
```

Nicht zulässig:

> `P&L fit = 80 %`

oder:

> `Die Person hat keine P&L-Erfahrung.`

## Ausgabe

`role-capability-map.json`:

```json
{
  "schemaVersion": 1,
  "role": {
    "title": "...",
    "organization": "...",
    "searchBriefRef": "..."
  },
  "person": {
    "name": "...",
    "profileRef": "...",
    "researchedAt": "YYYY-MM-DD"
  },
  "criteria": [
    {
      "criterionId": "R1",
      "criterion": "...",
      "priority": "essential",
      "assessment": "strongly-evidenced",
      "confidence": "high",
      "supportingClaimRefs": ["C1", "C4"],
      "supportingCapabilityRefs": ["CAP2"],
      "contradictingClaimRefs": [],
      "reasoning": "...",
      "limitations": [],
      "gaps": []
    }
  ],
  "summary": {
    "wellSupportedAreas": [],
    "partialAreas": [],
    "unresolvedAreas": [],
    "contradictions": []
  },
  "routing": {
    "researchGaps": [],
    "interviewGaps": [],
    "referenceGaps": [],
    "roleDefinitionGaps": []
  },
  "decisionBoundary": {
    "candidateRankingProduced": false,
    "hireRecommendationProduced": false
  }
}
```

`role-capability-map.md` enthält eine kriteriumsweise Evidence Matrix und eine kurze, neutrale Synthese.

`evidence-gaps.json` enthält alle offenen Punkte, Typ, Ursprungskriterium, Relevanz und empfohlenen nächsten Skill.

## Mehrere Personen

Bei mehreren Kandidaten wird für jede Person **zunächst eine separate `role-capability-map`** erzeugt.

Ein späterer Vergleich darf dieselben Kriterien nebeneinanderstellen, aber dieser Skill selbst erzeugt keine Gesamtrangfolge.

Zulässig ist zum Beispiel:

| Criterion | Person A | Person B | Person C |
|---|---|---|---|
| International IVD | strongly-evidenced | strongly-evidenced | partially-evidenced |
| P&L | not-evidenced | strongly-evidenced | partially-evidenced |

Nicht zulässig:

| Rank | Candidate | Score |
|---|---|---|
| 1 | A | 91 |
| 2 | B | 84 |

## Bias- und Fairness-Grenzen

Nur beruflich relevante und im Rollenbrief zulässige Kriterien dürfen gemappt werden.

Nicht verwenden oder rekonstruieren:

- Alter als Qualitätsproxy,
- Geschlecht,
- Familienstand,
- ethnische Zugehörigkeit,
- Religion,
- Gesundheitsinformationen,
- politische Überzeugungen,
- sexuelle Orientierung,
- Gewerkschaftszugehörigkeit,
- sonstige geschützte oder sachlich irrelevante Merkmale.

Keine Persönlichkeit oder vermeintlichen Motive aus Medienauftritten, Schreibstil, Fotos, Namen, Herkunft oder Karrierepausen ableiten.

## Prüfungen

Vor Übergabe prüfen:

- jedes Assessment verweist auf ein existierendes Rollen-Kriterium,
- jede positive/negative Zuordnung besitzt nachvollziehbare Claim-Provenance,
- `not-evidenced` wird nicht als Abwesenheit einer Fähigkeit formuliert,
- echte Widersprüche sind nicht zu bloßen Lücken abgeschwächt,
- Interview-only Kriterien werden nicht aus öffentlichen Proxies bewertet,
- Confidence beschreibt Evidenzqualität, nicht Erfolgsaussicht,
- keine versteckte Gesamtwertung oder Rangfolge wurde erzeugt,
- sensible/geschützte Merkmale spielen keine Rolle,
- Research-, Interview-, Reference- und Role-Definition-Gaps sind sauber getrennt.

## Fehlerbehandlung

### Rollenbrief zu diffus

Wenn wesentliche Kriterien keine klaren Evidence Questions besitzen, stoppe die Zuordnung für diese Kriterien und route sie als `role-definition-gap` zurück.

### Personenprofil zu dünn

Wenn öffentlich prüfbare Bereiche kaum recherchiert wurden, verwende `research-incomplete` und route an `professional-person-research`, statt vorschnell `not-evidenced` zu vergeben.

### Widerspruch in Evidenz

Wenn starke Quellen kollidieren, verwende `contradictory-evidence`, reduziere Confidence und dokumentiere die konkrete Konfliktauflösung, die noch fehlt.

### Unzulässiges Kriterium

Wenn der Rollenbrief ein sensibles, geschütztes oder nicht fair operationalisierbares Kriterium enthält, mappe es nicht. Route die Rollenanforderung zur Korrektur zurück.

## Übergaben

Geeignete nachgelagerte Verbraucher:

- `candidate-interview-evidence-plan` für Interviewfragen aus Evidenzlücken,
- `professional-person-research` für gezielte Nachrecherche,
- `executive-role-search-brief` / `round-based-requirements-grilling` für unklare Anforderungen,
- `document-production` für freigegebene Candidate Evidence Briefs.

## Qualitätsfälle

### Happy Path

Ein Search Brief enthält sechs klar operationalisierte Kriterien; das Personenprofil enthält aktuelle Primärquellen und mehrere abgeleitete Capabilities. Ergebnis: kriteriumsweise Zuordnung mit sauberer Provenance, mehreren `strongly-evidenced`- und `partially-evidenced`-Bereichen sowie wenigen Interview-Gaps.

### Grenzfall

Die Person war General Manager einer BU, aber direkte P&L-Verantwortung ist nicht explizit belegt. Ergebnis: `partially-evidenced`, nicht `strongly-evidenced`; P&L-Scope wird als Interview-Gap markiert.

### Widerspruch

Eine aktuelle Unternehmensbiografie beschreibt globale Verantwortung, eine ältere Quelle nur regionale Verantwortung im überlappenden Zeitraum. Ergebnis: Konflikt sichtbar halten, zeitlichen Kontext prüfen und Confidence entsprechend begrenzen.

### Interview-only

Die Rolle verlangt Konfliktfähigkeit in einer Matrixorganisation. Öffentliche Quellen enthalten Interviews und Podcasts. Ergebnis: keine Persönlichkeitsinferenz; `not-assessable-from-public-evidence` und konkrete Verhaltensfrage für das Interview.

### Fehlerfall

Eine vorgeschlagene Map erzeugt `87 % fit`, setzt nicht gefundene Evidenz mit fehlender Fähigkeit gleich und wertet das Alter der Person als Nachteil. Stoppe und korrigiere Bewertungsmodell, Negative-Evidence-Regel und Fairnessgrenze.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn jedes relevante Rollen-Kriterium separat gegen nachvollziehbare professionelle Evidenz gestellt wurde, Assessment State und Confidence begründet sind, alle verwendeten Aussagen auf Claims zurückführen, Lücken und Widersprüche typisiert und geroutet sind und keinerlei automatisches Candidate-Ranking oder Hiring-Urteil erzeugt wurde.
