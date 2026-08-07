---
name: fda-acceptance-readiness
description: Prüft pathway-spezifisch FDA-Submission-Acceptance-Readiness für 510(k) oder De Novo gegen aktuelle eSTAR-/RTA-/Technical-Screening-Anforderungen.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - fda-estar-submission-builder
  - regulatory-evidence-traceability
  - two-axis-compliance-review
outputs:
  - fda-acceptance-preflight.json
  - acceptance-gaps.json
lastEvaluated: 2026-08-07
---

# FDA Acceptance Readiness

## Zweck und Grenze

Dieser Skill prüft, ob ein vorbereiteter 510(k)- oder De-Novo-eSTAR-Inhalt gegen die **aktuell pathway-spezifisch anwendbaren** FDA-Acceptance-/Technical-Screening-Anforderungen vollständig und konsistent erscheint. Er ist ein internes Preflight-Gate vor externer Submission.

Er bewertet **nicht** abschließend die substantive scientific sufficiency und simuliert keine FDA-Acceptance. 510(k)-RTA und De-Novo-eSTAR-/Technical-Screening werden bewusst nicht als identischer Prozess modelliert. Aktuelle Checklisten, technische Screening-Regeln und Ausnahmen werden aus offiziellen FDA-Quellen geladen.

## Kernprinzipien

- **Pathway-specific:** `510k` und `de-novo` besitzen unterschiedliche Acceptance-Mechanismen.
- **Current-source:** aktuelle RTA-/eSTAR-/Technical-Screening-Regeln werden mit `asOf` verifiziert.
- **Acceptance ≠ substantive review:** administrativ/technisch vollständig bedeutet nicht wissenschaftlich ausreichend oder cleared/granted.
- **Evidence-based omissions:** Nicht-Anwendbarkeit benötigt nachvollziehbare Rationale und Requirement Reference.
- **No silent downgrade:** Pflichtinhalte werden nicht zu redaktionellen Nice-to-haves herabgestuft.
- **Internal preflight only:** FDA kann trotz internem `ready` weitere Fragen stellen oder eine Submission nicht akzeptieren.

## Workflow

### 1. Pathway und Content Map übernehmen

Übernimm `estar-content-map.json` und `submission-readiness.json`. Verifiziere, dass genau ein Pathway aktiv ist und die verwendete eSTAR-/FDA-Quelle noch aktuell ist.

### 2. Current Acceptance Mechanism bestimmen

Für `510k` ermittle die aktuelle RTA-/Acceptance-Policy und pathway-/submission-type-spezifische Checkliste, soweit anwendbar.

Für `de-novo` ermittle die aktuelle eSTAR-/Technical-Screening-/Acceptance-Logik und behandle sie nicht automatisch wie 510(k)-RTA.

### 3. Requirement-by-Requirement Preflight

Bewerte jede aktuelle Acceptance-Anforderung als:
- `met`,
- `partial`,
- `missing`,
- `not-applicable-with-rationale`,
- `blocked`,
- `unknown-current-requirement`.

Verknüpfe Requirement, eSTAR Field/Section, Source Artifact, Evidence und Rationale über `regulatory-evidence-traceability`.

### 4. Technische und fachliche Gaps trennen

Klassifiziere Gaps mindestens als:
- administrative/technical completeness,
- eSTAR validation/format,
- missing required content,
- inconsistent cross-reference,
- substantive-evidence concern,
- current-requirement uncertainty.

Substantive Evidence Concerns werden als Risiko für Review markiert, aber nicht fälschlich als Acceptance-Checklist-Element ausgegeben, wenn FDA sie dort nicht verlangt.

### 5. Readiness State ableiten

Status mindestens `ready-for-human-submission|ready-with-nonblocking-notes|not-ready|blocked|current-requirements-unresolved`.

`ready-for-human-submission` bedeutet ausschließlich, dass der interne Acceptance-Preflight bestanden ist. Es bedeutet nicht `FDA accepted`, `cleared`, `granted` oder substantive sufficiency.

### 6. Gap Routing

- eSTAR Assembly/Mapping → `fda-estar-submission-builder`
- 510(k)-SE-/Predicate-Gap → zuständiger 510(k)-Skill
- De-Novo-/Control-Gap → zuständiger De-Novo-Skill
- Risk/Evidence Gap → jeweiliger Fach-Skill
- unklare FDA-Anforderung → FDA Regulatory Strategy / `fda-qsub-strategy`
- externe Submission → autorisierter Human-Prozess.

## Output-Verträge

`fda-acceptance-preflight.json` enthält Pathway, `asOf`, Current FDA Acceptance Sources, Requirement Checks, Content/Evidence References, Technical vs Substantive Classification, Overall Readiness, Authority Boundary und Recheck Trigger.

`acceptance-gaps.json` enthält Gap-ID, Requirement/Source, Pathway, Gap Type, Severity, Content/Evidence Link, Owner/Next Skill, Blocking State und Resolution Evidence Needed.

## Memory Path

Persistenzwürdig sind validierte pathway-spezifische Preflight-Muster, stabile Gap-Klassifikationsregeln und wiederverwendbare technische Acceptance-Failure-Patterns. Aktuelle RTA-/Technical-Screening-Checklisten, momentane eSTAR-Versionen, konkrete Submission-Readiness und aktuelle FDA-Acceptance-Ergebnisse bleiben run-only. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- 510(k) und De Novo pathway-spezifisch statt mit einer generischen Checkliste geprüft werden,
- aktuelle FDA-Acceptance-Quellen verwendet werden,
- Acceptance und substantive scientific sufficiency getrennt bleiben,
- Missing/NA-Entscheidungen Requirement-/Evidence-Referenzen besitzen,
- `ready` nicht als FDA-Acceptance ausgegeben wird,
- fachliche Gaps an bestehende Owner zurückgeroutet werden,
- aktuelle Checklist-/Readiness-Zustände nicht als dauerhaftes Memory-Faktum gespeichert werden.
