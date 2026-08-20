# SPEC — People Research & Executive Search Capability Path

Status: draft
Repository: `GithubLarsKomo/skillz`
Branch: `feat/people-research-executive-search`

## Ziel

Einen modularen, evidenzbasierten Skill-Pfad für die Definition, Suche, berufliche Hintergrundrecherche und rollenbezogene Beurteilung von Personen für Führungs- und Expertenpositionen schaffen.

Der Pfad soll vorhandene Fähigkeiten wiederverwenden, insbesondere:

- `round-based-requirements-grilling` für Requirements Engineering,
- `research-to-evidence-note` für Claim-/Source-/Confidence-Logik,
- bestehende Meeting-, Dokumentations- und Decision-Record-Skills als nachgelagerte Verbraucher.

Es darf weder eine zweite Grilling-Implementierung noch eine parallele generische Recherche-/Evidence-Schicht entstehen.

## Kernprinzip

`Requirements != Search != Research != Evidence != Employment Decision`

Zielkette:

```text
Grilling
  -> Role Mission & Search Brief
  -> Search Strategy
  -> Person Discovery
  -> Professional Background Research
  -> Role Capability Evidence Map
  -> Interview Evidence Plan
  -> Human Review / Decision
  -> Search Learning Loop
```

## Capability-Slices

### 1. `executive-role-search-brief`

Übersetzt Unternehmenskontext und Grilling-Ergebnisse in einen operationalisierbaren Search Brief.

Outputs:

- `role-search-brief.json`
- `role-search-brief.md`

### 2. `professional-person-research`

Verdichtet öffentlich zugängliche, berufsbezogene Quellen zu einem nachvollziehbaren professionellen Personenprofil.

Outputs:

- `person-professional-profile.json`
- `person-professional-profile.md`
- `person-evidence-note.json`
- `person-source-register.json`

### 3. `talent-search-strategy`

Definiert Target Companies, Adjacent Companies, Role Families, Career Patterns und Search Hypotheses.

Outputs:

- `talent-search-strategy.json`
- `talent-search-strategy.md`
- `target-company-map.json`
- `search-hypotheses.json`

### 4. `role-capability-evidence-map`

Vergleicht Rollenanforderungen mit vorhandener beruflicher Evidenz, ohne Hiring-Entscheidung oder automatisches Ranking.

Outputs:

- `role-capability-map.json`
- `role-capability-map.md`
- `evidence-gaps.json`

### 5. `candidate-interview-evidence-plan`

Überführt Evidenzlücken, Konflikte und unklare Verantwortungszuordnung in gezielte Interview- und Referenzfragen.

Outputs:

- `candidate-interview-plan.md`
- `candidate-evidence-questions.json`
- `reference-check-topics.json`

## Skill-Grenzen

### `executive-role-search-brief`

Frage: `WHAT is required?`

Keine Kandidatensuche, keine Personenbewertung, keine Grilling-Runtime.

### `talent-search-strategy`

Frage: `WHERE might suitable people be found?`

Keine detaillierte Personenrecherche und kein Candidate Ranking.

### `professional-person-research`

Frage: `WHAT professional evidence exists about this person?`

Keine Aussage zur Eignung für eine konkrete Rolle; keine Persönlichkeitsdiagnostik.

### `role-capability-evidence-map`

Frage: `HOW does that evidence relate to this role?`

Keine automatische Hire/Reject-Entscheidung.

### `candidate-interview-evidence-plan`

Frage: `WHAT must a human clarify next?`

Keine Interviewdurchführung oder psychometrische Bewertung.

## Role Model

Das Rollenmodell muss mindestens enthalten:

- Unternehmens- und Besetzungsanlass,
- Mission der Rolle,
- erwartete Outcomes nach 12–24 Monaten,
- Verantwortungsumfang,
- Unternehmenssituation,
- fachliche Anforderungen,
- Führungskontext als beobachtbare Erfahrung,
- Constraints,
- Muss-/Soll-/Kontext-/trainierbare Kriterien,
- Evidence Questions pro Kriterium,
- Interview-only Questions.

Nicht operationalisierte Begriffe wie `strategisch`, `unternehmerisch`, `dynamisch`, `charismatisch` dürfen nicht unverändert als Bewertungskriterien übernommen werden. Sie müssen auf beobachtbare berufliche Evidenz zurückgeführt oder als ungeklärt markiert werden.

## Person Evidence Model

Ein Personenprofil muss trennen zwischen:

- direkt belegten Fakten,
- beruflichen Selbstaussagen,
- abgeleiteten Capabilities,
- unbekannten Informationen,
- widersprüchlicher Evidenz.

Wichtige Regeln:

- Job Title ist nicht automatisch Capability.
- Unternehmenserfolg ist nicht automatisch Individual Achievement.
- Anwesenheit während eines Ereignisses ist nicht automatisch Verantwortlichkeit.
- `not found` ist nicht `does not exist`.

Jede abgeleitete Capability muss auf konkrete Claims zurückgeführt werden können; jeder Claim auf konkrete Quellen.

```text
SOURCE -> CLAIM -> CAPABILITY -> ROLE REQUIREMENT
```

## Quellenlogik

Priorität:

1. Primärquellen: Arbeitgeberseiten, Management-Biografien, Geschäftsberichte, offizielle Meldungen, Patente, wissenschaftliche Publikationen, Konferenzprogramme, Hochschulseiten.
2. Starke professionelle Sekundärquellen: Fach- und Wirtschaftsmedien, belastbare Branchenpublikationen.
3. Berufliche Selbstdarstellung: LinkedIn und vergleichbare Profile, persönliche professionelle Websites, Speaker Bios; als Selbstaussage kennzeichnen.
4. Kontextquellen: Podcasts, öffentliche Präsentationen und eindeutig berufsbezogene Social-Media-Inhalte.

`research-to-evidence-note` bleibt die generische Evidenz- und Confidence-Schicht.

## Datenschutz und Fairness

Standardmäßig nicht erheben oder bewerten:

- private Wohnadressen,
- private Telefonnummern,
- Familienverhältnisse,
- Religion,
- ethnische Zugehörigkeit,
- sexuelle Orientierung,
- Gesundheitsinformationen,
- politische Überzeugungen,
- Gewerkschaftszugehörigkeit,
- private Freizeitaktivitäten ohne berufliche Relevanz.

Keine Proxy-Ableitungen solcher Merkmale.

Der Pfad dient der strukturierten professionellen Recherche und menschlichen Entscheidungsvorbereitung, nicht automatisierten Beschäftigungsentscheidungen.

## Capability Assessment

Zulässige Evidenzzustände pro Rollenanforderung:

- `strongly-evidenced`
- `partially-evidenced`
- `not-evidenced`
- `contradictory-evidence`
- `not-assessable-from-public-evidence`

Kein künstlicher Gesamtscore als Ersatz für menschliches Urteil.

## Batch Research

Mehrere Personen müssen zunächst unabhängig recherchiert werden. Erst danach darf ein rollenbezogener Vergleich erstellt werden.

Damit wird verhindert, dass Evidenzsammlung und Interpretation einer Person durch Eindrücke aus anderen Profilen verzerrt werden.

## Aktualität

Jedes Personenprofil enthält mindestens:

- `researchedAt`,
- `evidenceCurrentThrough`,
- Quellenstand,
- sichtbare Aktualitätsgrenzen.

Bei Wiederverwendung muss geprüft werden, ob sich Rolle, Arbeitgeber, Board-Mandate oder sonstige relevante berufliche Fakten geändert haben.

## Search Learning Loop

Search-Hypothesen sollen als explizite Hypothesen mit Status geführt werden:

- `untested`
- `supported`
- `partially-supported`
- `rejected`

Lernergebnisse dürfen die Search Strategy verändern, aber nicht rückwirkend die Evidenz einzelner Personen.

## Nicht-Ziele

Kein:

- ATS,
- Candidate CRM,
- LinkedIn-Scraper,
- Data Broker,
- automatischer Headhunter,
- personenbezogener Data Lake,
- Personality Profiler,
- automatisches Candidate Ranking,
- automatisches Hire/Reject-System,
- privater Background Check.

## Evaluationsfälle

Für jeden neuen Skill mindestens:

- Happy Path,
- Sparse Evidence,
- Conflicting Sources,
- Self-Reported Profile,
- Sensitive Information,
- Role Bias / nicht operationalisierte Kriterien.

## Implementierungsreihenfolge

1. `executive-role-search-brief`
2. `professional-person-research`
3. `role-capability-evidence-map`
4. `talent-search-strategy`
5. `candidate-interview-evidence-plan`
6. End-to-End-Evaluation und Capability-Index

## Definition of Done

- fünf klar getrennte Domain-Skills implementiert,
- Grilling bleibt autoritative Requirements-Schnittstelle,
- `research-to-evidence-note` wird statt eigener Evidence-Logik wiederverwendet,
- Fakten, Selbstaussagen, Ableitungen und Unknowns bleiben unterscheidbar,
- jede Capability besitzt Provenance zu Claims und Quellen,
- `not found` und `does not exist` bleiben getrennt,
- Konflikte und Aktualität werden explizit geführt,
- sensible/private Informationen sind aus dem normalen Research Scope ausgeschlossen,
- automatisches Hiring/Rejecting ist nicht Teil des Pfades,
- Batch-Recherche ist ohne wechselseitige Kandidatenverzerrung möglich,
- Capability Index und Dependencies sind aktualisiert,
- Evaluation Cases bestehen.
