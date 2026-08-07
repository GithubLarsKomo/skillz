---
name: qms-management-review-governance
description: Bereitet Medical-Device-/IVD-QMS-Management-Reviews aus bestätigten QMS-, Audit-, CAPA-, PMS-, Vigilance-, Complaint-, Risk-, Supplier- und Performance-Evidenzen vor und trennt Inputs, Decisions, Actions und offene Datenlücken.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-qms-iso13485
  - iso13485-qms-audit
  - medical-device-capa
  - medical-device-pms-system
  - project-status-brief
outputs:
  - management-review-brief.json
  - management-review-actions.json
  - management-review-brief.md
lastEvaluated: 2026-08-08
---

# qms-management-review-governance

## Zweck

Ersetzt die breite QMR-Persona durch einen klaren Management-Review-/Governance-Skill, der keine operativen Subsysteme dupliziert. Für vermarktete Medical Devices und IVDs verbindet er den Management Review explizit mit dem aggregierten PMS-/Postmarket-Zustand, ohne einzelne Vigilance-, Complaint-, MDR-, Field-Action- oder CAPA-Entscheidungen neu zu treffen.

## Trigger

Verwenden für QMS Management Review, Quality Objectives/KPI Review, prior action follow-up, resource/quality governance oder Executive QMS Decision Preparation.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Required Review Inputs werden aus anwendbarem QMS/Regulatory Context und Organisationsverfahren bestimmt, nicht aus einer statischen universellen Agenda.
- Für vermarktete Produkt-Scope ist `pms-management-review-input.json` ein expliziter Management-Review-Input. Fehlt dieser ohne begründete Nichtanwendbarkeit, bleibt ein `dataGap`; fehlende PMS-Evidenz wird nicht als „keine Ereignisse“ interpretiert.
- Jeder Input trägt period/asOf, source, completeness und trendability; die Zustände `no-events|no-signal|no-data|not-reviewed|not-applicable|unknown` bleiben getrennt.
- Postmarket-/Vigilance-Inputs enthalten aggregierte Status- und Decision-References statt unnötiger patienten- oder fallbezogener Rohdaten.
- Ein zeitkritischer möglicher Vigilance-/Reportability-/Field-Action-Fall wartet **nie** auf den nächsten Management Review. Operative regulatorische Eskalation läuft beim zuständigen Spezialisten; Management Review bewertet Governance, Trend, Timeliness, offene High-Impact-Zustände und Follow-up.
- Ein einzelner höher-riskanter ungelöster Safety-/Quality-/Reportability-Sachverhalt darf nicht durch einen aggregierten „grünen“ KPI oder eine niedrige Gesamt-Complaint-Rate unsichtbar werden.
- Quality KPIs benötigen Definition, Datenquelle, Owner, Zeitraum und Ziel-/Escalation-Kontext; keine generischen Benchmarktargets werden erfunden.
- Decisions needed, decisions made und follow-up actions bleiben getrennt; meeting preparation ist kein Entscheidungsnachweis.
- Actions übernehmen Owner/Due Date nur wenn bestätigt und bleiben pending bis Completion-/Effectiveness-Evidence vorliegt. Ein im Management Review diskutierter Fall ist dadurch weder regulatorisch gemeldet noch extern geschlossen.
- Wenn frühere Management-Review-Actions existieren, ist `management-review-return-input.json` aus `qms-management-review-action-followup` ein expliziter Vorperioden-Input. Fehlt dieser ohne bestätigten Nachweis, dass keine Vorperioden-Actions existieren, bleibt die Prior-Action-Coverage `unknown|dataGap` statt implizit „alles geschlossen“.
- `routed|implemented|effectiveness-pending|effective|external-pending|closed` bleiben auch im Management Review getrennte Zustände. Eine Owner-Aussage „done“ oder eine Task-Checkbox wird nicht als Effectiveness- oder Closure-Evidence hochgestuft.
- Ineffektive, überfällige, blockierte, re-opened oder extern noch offene Actions bleiben als Management-Attention sichtbar; bestätigte Closure darf ihre historische Wirksamkeits-/Trend-Relevanz nicht löschen.
- QMS Suitability/Adequacy/Effectiveness Conclusions müssen auf sichtbarer Evidence, Input-Coverage und offenen Gaps beruhen. Bei materially incomplete Postmarket Coverage, unvollständiger Prior-Action-Coverage oder ungelösten High-Impact-Signalen wird die Schlussfolgerung entsprechend qualifiziert statt pauschal positiv formuliert.

## Temporal Feedback Contract

Der fachliche Loop über Review-Perioden ist absichtlich **kein** harter Dependency-Zyklus:

`Management Review -> management-review-actions.json -> qms-management-review-action-followup -> management-review-return-input.json -> nächster Management Review`

Der Follow-up-Worker ist ein harter Downstream-Consumer der aktuellen Review-Actions. Der nächste Review konsumiert dessen Return Input als zeitlich vorgelagerte Evidenz. Dadurch bleibt der Capability-Graph azyklisch, während Prior-Action-Closure und Effectiveness im Review verbindlich geprüft werden.

## Workflow

### 1. Review Scope und Zeitraum fixieren

Bestimme Review Scope, Produkte/Standorte/Märkte, Review Period, anwendbare Criteria, vorherige Review Actions und `asOf`. Trenne geplanten periodischen Review von event-getriebener Top-Management-Eskalation.

### 2. Input Coverage inventarisieren

Inventarisiere mindestens soweit anwendbar:

- QMS-/Audit- und Finding-Status,
- CAPA/Nonconformity und Effectiveness,
- `pms-management-review-input.json` mit PMS Source Coverage/Data Quality,
- `management-review-return-input.json` für frühere Management-Review-Actions, sobald solche Actions existieren,
- Complaints/Feedback und Service-/Field-Quality-Signale,
- Vigilance/Adverse-Event/Reportability-Status und externe Action States pro Markt,
- Trend-/Signal-Hypothesen inklusive Denominator-/Confidence-Grenzen,
- FSCA/Recall/Correction/Removal/Advisory-Notice-Zustände,
- Risk-/Benefit-Risk-Änderungen,
- Performance/Clinical Evidence/PMPF soweit relevant,
- Supplier-/Process-/Validation-Signale,
- Regulatory Changes und prior Management Review Actions.

Verwende Specialist Decision References; kopiere keine unnötigen Rohfall- oder Patientendaten in den Review Brief.

### 3. Prior-Action Lifecycle prüfen

Für jede Vorperioden-Action prüfe Source Review/Decision Reference, Owner/Due soweit bestätigt, Target Owner, Completion Evidence, Effectiveness State/Evidence, External State und Re-open/Blocker. Nutze den Status aus `qms-management-review-action-followup`; re-decide keine specialist-owned Effectiveness- oder External-Closure-Frage.

Mindestens separat sichtbar bleiben:

- offen/überfällig/blockiert,
- implementiert aber Effectiveness noch ausstehend,
- ineffektiv/re-opened,
- external-pending,
- seit dem letzten Review verifiziert geschlossen,
- cancelled/superseded mit bestätigter Autorität und Begründung.

### 4. Completeness, Trends und High-Impact-Ausnahmen prüfen

Bewerte Input Coverage, Datenqualität, Trendability, Widersprüche und Data Gaps. Prüfe separat, ob offene High-Impact-Vigilance-, Field-Action-, CAPA-, Risk-, Regulatory- oder Prior-Action-Zustände unabhängig vom aggregierten KPI sichtbar sind.

### 5. Decision Needs vorbereiten

Leite Entscheidungen zu Ressourcen, Quality Objectives, QMS-/PMS-Verbesserungen, erforderlichen Prozess-/Design-/Labeling-/Risk-Maßnahmen und Follow-up ab. Re-decide keine specialist-owned Reportability-, CAPA-Root-Cause-, Effectiveness-, Risk-Acceptance- oder Authority-Entscheidung.

### 6. Bestätigte Decisions und Actions dokumentieren

Dokumentiere nur tatsächlich bestätigte Management Decisions/Actions. Route Auswirkungen zurück an die bestehenden Owner, z. B. PMS-Plan-/Source-Änderung an `medical-device-pms-system`, CAPA an `medical-device-capa`, Risk an `medical-device-risk-management-iso14971`, Regulatory/Change-Fragen an die jeweiligen Fach-Skills. Neue oder geänderte Management-Review-Actions gehen anschließend an `qms-management-review-action-followup`. Externe Closure bleibt separat verifiziert.

## Output-Verträge

`management-review-brief.json` enthält Scope/Period/`asOf`, Input-Coverage, Data Gaps, KPI-/Trend-Kontext, eine `postmarketGovernance`-Sicht sowie `priorActionGovernance` mit Vorperioden-Action-Coverage, offenen/überfälligen/ineffektiven/external-pending Zuständen, verified closures und Effectiveness Gaps. Suitability/Adequacy/Effectiveness Conclusions bleiben evidenzgebunden und qualifiziert.

`management-review-actions.json` enthält bestätigte Decision/Action, Source Review/Decision Reference, Owner, Due Date soweit bestätigt, Target Skill/System, benötigte Completion-/Effectiveness-Evidence, externe Closure-Anforderungen, Status und Follow-up Trigger. Diskussion oder Routing allein zählt nicht als Closure. Der kanonische Downstream-Consumer ist `qms-management-review-action-followup`.

`management-review-brief.md` spiegelt die entscheidungsrelevanten Inputs, Gaps, High-Impact-Ausnahmen, Prior-Action-States, Decisions Needed, bestätigten Decisions und Actions für den menschlichen Review.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Memory Path

Persistenzwürdig sind validierte, abstrahierte Management-Review-Coverage-Muster, stabile Governance-Heuristiken und wiederverwendbare Eskalations-/Follow-up-Prinzipien. Konkrete Complaints, Vigilance-/Reportability-Fälle, Patienten-/Anwenderdaten, aktuelle KPI-/Trendwerte, offene CAPA/FSCA/Recall-Zustände, aktuelle Managemententscheidungen und Authority States bleiben run-only bzw. kontrollierte Quality/Regulatory Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`; übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`. Dieser Skill persistiert nichts selbst.

## Grenzen

- Keine Managemententscheidung erfinden.
- Keine generischen KPI-Zielwerte als Norm.
- Kein Ersatz für Audit, PMS, Vigilance, Complaint, CAPA, Risk, Effectiveness Verification oder Regulatory Strategy.
- Management Review ist kein Gate, das zeitkritische regulatorische Eskalation oder Reporting verzögern darf.
- Keine Prior-Action als geschlossen behandeln, nur weil sie aus dem aktuellen Agenda-/Task-Snapshot verschwunden ist.

## Qualitätsgate

Pass nur, wenn:

- Facts/Interpretations getrennt und Freshness sichtbar sind,
- zentrale Claims rückverfolgbar sind und Unknowns nicht positiv umgedeutet werden,
- für vermarktete Produkte der aggregierte PMS-/Postmarket-Input vorhanden oder sein Fehlen explizit als Gap/Nichtanwendbarkeit geklärt ist,
- bei vorhandenen Vorperioden-Actions ein aktueller Return Input vorliegt oder dessen Fehlen als Prior-Action-Coverage-Gap sichtbar bleibt,
- `no-events|no-signal|no-data|not-reviewed|not-applicable` nicht vermischt werden,
- `routed|implemented|effectiveness-pending|effective|external-pending|closed` nicht vermischt werden,
- offene High-Impact-Vigilance-/Safety-/Regulatory-/Prior-Action-Zustände nicht durch aggregierte KPIs verdeckt werden,
- zeitkritische Vigilance-/Reportability-Aktionen nicht auf den Management Review warten,
- Specialist Decisions, Effectiveness und externe Closure nicht vom Management Review neu erfunden werden,
- Suitability/Adequacy/Effectiveness bei materiellen Data Gaps, unvollständiger Prior-Action-Coverage oder offenen High-Impact-Zuständen sichtbar qualifiziert werden,
- Cross-Skill-Grenzen respektiert sind und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
