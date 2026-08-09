---
name: fda-qsub-strategy
description: Strukturiert FDA-Q-Submission-Fragen, Briefing Package, gewünschtes Feedback und Commitments evidenzgebunden, ohne externe FDA-Interaktion oder Zustimmung zu simulieren.
---

# FDA Q-Submission Strategy

## Zweck und Grenze

Dieser Skill verwandelt konkrete ungelöste FDA-Regulatory-/Evidence-Fragen in eine fokussierte Q-Submission-Strategie und ein Briefing Package. Er definiert, welche FDA-Rückmeldung benötigt wird, welche Fakten/Evidenz FDA dafür braucht, welche Entscheidung vom Feedback abhängt und wie erhaltenes Feedback anschließend nachvollziehbar in Entscheidungen und Follow-ups zurückgeführt wird.

Er ist **kein generischer Meeting-Skill**, reicht keine Q-Submission autonom ein, simuliert kein FDA-Feedback und behandelt informelle Diskussionen nicht automatisch als verbindliche Agency-Entscheidung. Aktuelle Q-Sub-Mechanismen und Format-/Submission-Anforderungen werden gegen die jeweils aktuellen FDA-Quellen geprüft.

## Kernprinzipien

- **Question-first:** jede Q-Sub-Frage muss eine konkrete regulatorische Unsicherheit oder Evidence-Entscheidung de-risken.
- **Keine offenen Essay-Fragen:** formuliere Fragen so, dass FDA gezielt auf vorgeschlagene Position, Option, Study Design, Control oder Evidence Scope reagieren kann.
- **Decision linkage:** jede Frage benennt, welche interne Entscheidung durch das Feedback beeinflusst wird.
- **Evidence before opinion:** Briefing Context und Proposed Position sind mit `regulatory-evidence-traceability` verknüpft.
- **Final-vs-Draft-Status erhalten:** die aktuelle Q-Submission-Program-Guidance und elektronische Template-/Format-Guidance werden mit ihrem tatsächlichen Status behandelt; Draft wird nicht als implementierte Pflicht ausgegeben.
- **Feedback ist nicht pauschale Freigabe:** FDA-Feedback wird mit Scope, Kontext, Datum und offenen Bedingungen erfasst; Änderungen des Facts/Designs können Re-evaluation erfordern.
- **External action boundary:** Submission, Meeting, Upload oder sonstige FDA-Interaktion bleibt Human-/Authorized-Action und muss separat verifiziert werden.

## Workflow

### 1. Uncertainty auswählen

Übernimm nur Fragen mit realem Entscheidungswert, z. B. Classification/Product Code, Predicate/SE, De Novo/Special Controls, Evidence Scope, Study Design, CLIA, Software/Cybersecurity, Human Factors oder andere submission-relevante Themen.

### 2. Desired Feedback definieren

Für jede Frage erfasse:

- Decision ID / Regulatory Issue,
- bekannte Facts,
- Unknowns,
- Proposed Position/Plan,
- Alternativen,
- Evidence/Source References,
- präzise gewünschte FDA-Rückmeldung,
- Entscheidung, die nach Feedback getroffen wird,
- Konsequenz bei `agree|disagree|partial|insufficient-feedback`.

### 3. Aktuellen Q-Sub-Mechanismus bestimmen

Prüfe die aktuelle finale Q-Submission-Program-Guidance und wähle den geeigneten Interaktionsmechanismus/Scope. Aktuelle Electronic-Submission-/Template-Anforderungen werden separat mit Status und `asOf` geprüft; nicht finale Guidance wird nicht als Pflicht umgesetzt.

### 4. Briefing Package strukturieren

`qsub-briefing-package.md` enthält nur Kontext, der für die Fragen erforderlich ist: Device/Product Context, Regulatory History, relevante Daten, Proposed Approach, Alternativen, Risiken und konkrete Questions. Unnötige Voll-Submission-Inhalte werden vermieden.

### 5. Preflight

Prüfe jede Frage auf:

- eindeutigen Entscheidungsbezug,
- hinreichenden Kontext,
- keine versteckten Mehrfachfragen,
- keine Faktenbehauptung ohne Evidenz,
- klare Unterscheidung zwischen Requested Feedback und bereits entschiedener Position,
- aktuelle Program-/Submission-Anforderungen.

### 6. External Handoff

Übergib die tatsächliche Einreichung/Termin-/Portalaktion an autorisierte Human-Prozesse bzw. `human-procedure-wizard`. Der Skill behauptet weder Submission noch Meeting-Durchführung ohne verifizierte externe Evidenz.

### 7. FDA-Feedback aufnehmen

Nach tatsächlich erhaltenem Feedback erfasse Aussage, Kontext/Scope, Datum, Source Reference, Bedingungen, offene Fragen und Confidence. Mappe Feedback zurück auf Decision IDs, `decision-record` und `decision-and-follow-up-tracker`.

### 8. Commitments und Re-evaluation

`qsub-commitments.json` enthält nur tatsächlich akzeptierte interne Commitments bzw. nachvollziehbar aus FDA-Feedback abgeleitete Actions. Neue Produkt-/Study-/Risk-Fakten können frühere Feedback-Relevanz begrenzen; entsprechende Re-evaluation Trigger bleiben sichtbar.

## Output-Verträge

`qsub-question-set.json` enthält Questions, Decision Links, Facts/Unknowns, Proposed Positions, Alternatives, Evidence References, Desired Feedback und Response Branches.

`qsub-briefing-package.md` enthält fokussierten Context, regulatorische Historie, relevante Evidenz, Proposed Approach und nummerierte FDA-Fragen mit klarer Desired-Feedback-Formulierung.

`qsub-commitments.json` enthält Feedback Source/Date/Scope, Internal Decision Impact, Accepted Commitments, Owners, Due/Trigger, Evidence Needed, Open Questions und Re-evaluation Conditions. Vor FDA-Feedback ist dieser Output leer bzw. ausdrücklich `pending-feedback`.

## Downstream

Q-Sub-Feedback kann an `fda-510k-predicate-strategy`, `fda-510k-substantial-equivalence`, `fda-de-novo-strategy`, `fda-de-novo-special-controls` und spätere CLIA/eSTAR-Skills zurückgehen. `decision-record` hält strategische Entscheidungen; `decision-and-follow-up-tracker` hält offene Commitments. Externe Submission-/Meeting-Aktionen bleiben verifizierte Human Actions.

## Memory Path

Persistenzwürdig sind validierte wiederverwendbare Frageformulierungs-, Evidence-Packaging- und FDA-Interaction-Heuristiken. Konkrete FDA-Feedbacks, Commitments, laufende Submission-/Meeting-States und projektspezifische Agency-Positionen gehören primär in Decision/Follow-up/Project Records und bleiben im Memory Path standardmäßig run-only. Nur abstrahierte, nicht-sensitive, ausreichend bestätigte Learnings dürfen mit `sourceRefs`, `asOf` und ggf. `reviewAfter` an `communication-memory-governance` übergeben werden. Der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- jede Frage eine konkrete interne Entscheidung de-riskt,
- Briefing Context und Proposed Position evidenzgebunden sind,
- Fragen fokussiert und nicht unnötig mehrteilig sind,
- aktuelle finale Q-Sub-Guidance und Draft-Template-Status korrekt unterschieden werden,
- Submission/Meeting/FDA-Feedback nicht simuliert werden,
- erhaltenes Feedback mit Scope und Source zurück in Decision/Follow-up-Verträge fließt,
- projektspezifische FDA-Feedbacks nicht ungeprüft als globale dauerhafte Memory-Fakten gespeichert werden.
