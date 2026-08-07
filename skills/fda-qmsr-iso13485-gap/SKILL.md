---
name: fda-qmsr-iso13485-gap
description: Trennt ISO-13485-QMS-Evidenz von aktuellen FDA-QMSR-spezifischen Pflichten, Inspection-Impacts und Gaps, ohne ein zweites QMS-Prozessmodell zu erzeugen.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-qms-iso13485
  - two-axis-compliance-review
  - regulatory-evidence-traceability
outputs:
  - qmsr-iso13485-delta.json
  - qmsr-gap-assessment.md
lastEvaluated: 2026-08-07
---

# FDA QMSR vs ISO 13485 Gap Assessment

## Zweck und Grenze

Dieser Skill bewertet, welche vorhandene ISO-13485-QMS-Evidenz aktuelle FDA-QMSR-Anforderungen bereits trägt und wo US-spezifische Regulatory-, Record-, Inspection- oder Implementierungs-Gaps verbleiben. Er **dupliziert kein QMS-Prozessmodell**: `medical-device-qms-iso13485` bleibt Eigentümer der QMS-Prozesse; dieser Skill erzeugt ausschließlich die US-FDA-Deltas und Evidence Gaps.

Der Skill reproduziert keine urheberrechtlich geschützten Normtexte. ISO-13485-Anforderungen werden aus der organisationsseitig verfügbaren autorisierten Normquelle referenziert; QMSR/21-CFR-/FDA-Quellen werden aktuell und autoritativ geladen.

## Kernprinzipien

- **ISO baseline, FDA delta:** vorhandene ISO-13485-Prozesse/Evidenz werden wiederverwendet; nur zusätzliche oder anders gelagerte FDA-Anforderungen werden als Delta modelliert.
- **Current QMSR:** effektive 21-CFR-Part-820-/QMSR-Anforderungen, FDA-FAQ/Guidance und Inspection-Programm werden mit `asOf` geprüft.
- **Requirement vs evidence:** Prozess vorhanden ≠ Compliance belegt. `two-axis-compliance-review` trennt Coverage von Evidence/Effectiveness.
- **Inspection visibility:** Records, die FDA unter QMSR prüfen darf, werden als Inspection Evidence gekennzeichnet; historische QS-Reg-Annahmen dürfen nicht ungeprüft fortgeführt werden.
- **No QSIT legacy:** aktuelle Inspection Readiness folgt QMSR/CP-7382.850-Kontext, nicht alten QSIT-Playbooks.
- **No silent equivalence:** ISO-13485-Zertifizierung ist relevante Evidenz, aber kein automatischer Nachweis vollständiger FDA-QMSR-Compliance.

## Workflow

### 1. QMS Baseline fixieren

Übernimm Scope, Sites, Products, QMS-Prozesse, vorhandene ISO-13485-Evidenz, Audit-/CAPA-/Supplier-/Management-Review-/Design-/Production-/Complaint-/Record-Strukturen aus `medical-device-qms-iso13485` und vorhandenen kontrollierten Records.

### 2. Current FDA Requirements laden

Verifiziere aktuelle QMSR-/21-CFR-Part-820-Anforderungen und relevante FDA-Inspection-/FAQ-/Guidance-Quellen. Erfasse Source Type, Status, `asOf` und Scope. Historische QS-Reg-/QSIT-Regeln werden nur verwendet, wenn ein historischer Sachverhalt bewertet wird.

### 3. Requirement Mapping

Für jede relevante FDA-Anforderung erfasse:
- FDA Requirement/Source Reference,
- zugehörigen ISO-/QMS-Prozess,
- vorhandene Procedure/Record Evidence,
- US-spezifisches Delta,
- Inspection Visibility,
- Coverage Status,
- Evidence/Effectiveness Status,
- Gap/Next Action.

### 4. Inspection Impact bewerten

Markiere Records/Prozesse, deren Bereitstellung/Review unter aktuellem QMSR-Inspection-Kontext relevant ist. Prüfe insbesondere, ob veraltete Annahmen zu Audit-, Supplier-Audit- oder Management-Review-Record-Ausnahmen bestehen.

### 5. Gaps priorisieren

Klassifiziere `no-delta|documentation-gap|implementation-gap|evidence-gap|inspection-readiness-gap|regulatory-interpretation-gap|unknown`. Priorisiere nach Compliance-/Patient-/Inspection-Impact statt nur Dokumentaufwand.

### 6. Routing

- QMS-Prozessänderung → `medical-device-qms-iso13485`
- Compliance-/Evidence-Verifikation → `two-axis-compliance-review`
- Finding/Systemursache → `medical-device-capa` / `evidence-based-causal-investigation`
- kontrollierte Dokument-/Record-Änderung → `controlled-quality-documentation`
- Inspection Readiness → später `fda-qmsr-inspection-readiness`
- Design-/Change-Gap → `design-control-traceability` / `design-change-regulatory-impact`.

## Output-Verträge

`qmsr-iso13485-delta.json` enthält QMS Scope, `asOf`, FDA Requirements, ISO/QMS Mapping, Existing Evidence, Delta Type, Inspection Visibility, Coverage/Evidence Status, Gaps, Owners und Source References.

`qmsr-gap-assessment.md` fasst wesentliche US-spezifische Deltas, Inspection Impacts, Evidence Gaps, Prioritäten und notwendige Actions zusammen, ohne vollständige ISO-Normtexte zu reproduzieren.

## Memory Path

Persistenzwürdig sind validierte QMSR↔ISO-Mapping-Muster, wiederverwendbare US-spezifische Delta-Heuristiken und bestätigte Inspection-Evidence-Patterns. Aktuelle FDA-FAQ-/Inspection-Program-Snapshots, momentane Gap-Status, konkrete Audit-/Inspection-Findings und organisationsspezifische vertrauliche Records bleiben run-only bzw. in Quality Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- ISO-QMS-Prozesse wiederverwendet statt dupliziert werden,
- aktuelle QMSR-/Inspection-Quellen statt QSIT-Legacy verwendet werden,
- Requirement Coverage und Evidence/Effectiveness getrennt bewertet werden,
- ISO-Zertifizierung nicht mit vollständiger FDA-Compliance gleichgesetzt wird,
- Inspection-relevante Records sichtbar berücksichtigt werden,
- Normtexte nicht unnötig reproduziert werden,
- aktuelle Gap-/Inspection-Zustände nicht als globales dauerhaftes Memory gespeichert werden.
