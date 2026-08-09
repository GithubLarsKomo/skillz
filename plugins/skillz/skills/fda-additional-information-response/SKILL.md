---
name: fda-additional-information-response
description: Strukturiert FDA-Interactive-Review- und Additional-Information-Anfragen issue-by-issue in evidenzgebundene Response-Pakete, Fristen und Follow-ups.
---

# FDA Additional Information Response

## Zweck und Grenze

Dieser Skill verarbeitet tatsächliche FDA-Review-Fragen für 510(k)- oder De-Novo-Submissions und strukturiert sie issue-by-issue in ein evidenzgebundenes Response-Paket. Er unterscheidet insbesondere zwischen informeller/iterativer `interactive-review`-Kommunikation und formalen `additional-information`-Requests, erfasst den tatsächlichen FDA-Request als Source und verbindet jede Antwort mit Evidence, Decisions, Owners und Fristen.

Er simuliert **keine FDA-Anfrage**, keine Response Submission und keine FDA-Akzeptanz der Antwort. Fristen, Clock-/Hold-Status und Einreichungsmechanismen werden aus dem tatsächlichen FDA-Schreiben und aktuell anwendbaren offiziellen FDA-Regeln abgeleitet; historische Zahlen werden nicht als unveränderliche Skill-Konstanten behandelt.

## Kernprinzipien

- **Actual request is source of truth:** Wortlaut, Datum, Request Type, Submission Number und ggf. Due Date/Clock Status stammen aus FDA-Evidenz.
- **Interactive Review ≠ formal AI Request:** Kommunikationsform, Clock-/Hold-Auswirkung und Response-Mechanismus bleiben getrennt.
- **Issue-by-issue:** jede FDA-Frage erhält Interpretation, Evidence Need, Owner, Response, Supporting Evidence, Cross-References und Status.
- **No unsupported answer:** fehlende Daten werden als Gap/Commitment sichtbar, nicht durch rhetorische Sicherheit ersetzt.
- **Cross-response consistency:** Antworten dürfen ursprüngliche Submission, andere Responses, Risk File, Labeling oder Claims nicht widersprechen.
- **External action boundary:** Portal/eSTAR/eCopy/sonstige Einreichung bleibt autorisierte externe Aktion mit separater Verifikation.
- **Quality feedback loop:** FDA-Deficiencies, die auf systemische QMS-/Risk-/Design-Probleme hinweisen, werden an CAPA/Investigation/Design Change zurückgeführt.

## Workflow

### 1. FDA Request ingestieren

Fixiere die autoritative FDA-Quelle und erfasse mindestens:
- Submission/Interaction Reference,
- Request Type `interactive-review|additional-information|other-formal-request`,
- Request/Communication Date,
- FDA Reviewer/Division soweit relevant,
- Due Date oder Clock/Hold Information, soweit im Schreiben bzw. aktuellen FDA-Regeln belegt,
- vollständige nummerierte Request Items,
- Anhänge/Referenzen.

Wenn der tatsächliche Request fehlt, darf kein offizielles Response-Paket als FDA-spezifisch behauptet werden.

### 2. Current Process Context verifizieren

Prüfe aktuelle FDA-Review-/Response-Regeln und den tatsächlichen Letter Context. Berechne/übernehme Fristen nur aus belegten Quellen; speichere Source, `asOf`, Berechnungs-/Interpretationslogik und Confidence.

### 3. Request Items normalisieren

Für jedes Item erfasse:
- FDA Request Text Reference,
- Issue/Deficiency Interpretation,
- betroffenen Claim/Section/Requirement,
- bekannte Facts,
- Unknowns,
- Evidence Need,
- Owner,
- Response Strategy,
- Blocking Dependencies,
- Decision/Commitment Links.

Mehrteilige FDA-Fragen dürfen in interne Sub-Issues zerlegt werden, müssen aber auf das ursprüngliche Request Item zurückverweisen.

### 4. Evidence und Antwort entwickeln

Verknüpfe jede Antwort über `regulatory-evidence-traceability` mit vorhandener Submission Evidence und neu erzeugter Evidenz. Neue Studien, Analysen, Risk-/Design-/QMS-Arbeit gehen an die zuständigen Fach-Skills statt im Response-Skill improvisiert zu werden.

### 5. Cross-Consistency Review

Prüfe Antwort gegen:
- ursprüngliche eSTAR Content Map,
- Intended Use/Claims/Labeling,
- SE- oder De-Novo-Strategy,
- Risk Management,
- andere FDA-Request-Responses,
- neue Commitments/Design Changes.

Widersprüche werden vor externer Antwort als Blocker ausgewiesen.

### 6. Response Package erzeugen

`fda-response-package.md` strukturiert pro Request Item:
1. FDA Request Reference,
2. Response/Position,
3. Supporting Evidence,
4. neue/aktualisierte Dokumente,
5. Cross-References,
6. Limitations/Open Items,
7. Commitment/Follow-up falls nötig.

### 7. External Handoff und Verifikation

Übergib die tatsächliche Response Submission an autorisierte Human-Prozesse bzw. `human-procedure-wizard`. Erst verifizierte externe Evidenz darf `responseSubmissionState: submitted|received` setzen.

### 8. Lifecycle-Feedback

- Quality/System Finding → `medical-device-capa`
- unklare Ursache → `evidence-based-causal-investigation`
- Risk-Auswirkung → `medical-device-risk-management-iso14971`
- Design-/Claim-Änderung → `design-change-regulatory-impact`
- strategische neue Entscheidung → `decision-record`
- Follow-up/Commitment → `decision-and-follow-up-tracker`
- kontrollierte Response-/Supporting Documents → `controlled-quality-documentation`.

## Output-Verträge

`fda-request-issue-map.json` enthält Request Source, Type, Date, Due/Clock Context, Request Items, Interpretations, Evidence Needs, Owners, Dependencies, Status und Source References.

`response-evidence-matrix.json` verknüpft jedes Request/Sub-Issue mit Response Statement, Evidence, Updated Document/Section, Requirement/Claim/Risk Link, Verification und Remaining Gap.

`fda-response-package.md` enthält die vollständige issue-by-issue Antwortstruktur, ohne externe Einreichung oder FDA-Akzeptanz zu behaupten.

## Memory Path

Persistenzwürdig sind validierte abstrakte Deficiency-Response-Muster, wiederverwendbare Issue-Decomposition-Heuristiken und Cross-Consistency-Failure-Patterns. Konkrete FDA-Requests, Due Dates, Submission IDs, Reviewer-Kommunikation, Response-Drafts, projektspezifische FDA-Positionen und offene Commitments bleiben run-only bzw. gehören in Decision-/Follow-up-/Project Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und bei Prozessregeln `reviewAfter`. Übergib nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- tatsächlicher FDA-Request als Source fixiert ist,
- Interactive Review und formaler AI Request getrennt bleiben,
- Due/Clock-Aussagen auf Letter/current FDA source statt Erinnerung beruhen,
- jedes Request Item Evidence/Owner/Status besitzt,
- Antworten konsistent mit Submission, Claims, Risk und anderen Responses sind,
- fehlende Evidenz an bestehende Fach-Skills geroutet wird,
- externe Response Submission/FDA Acceptance nicht simuliert wird,
- konkrete FDA-Requests/Fristen/Feedbacks nicht als globales dauerhaftes Memory gespeichert werden.
