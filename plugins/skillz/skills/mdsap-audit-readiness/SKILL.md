---
name: mdsap-audit-readiness
description: Bereitet Medical-Device-QMS-Evidenz auf den aktuellen MDSAP Audit Approach vor, mappt Audit-Typ, Prozesse, Tasks und anwendbare Jurisdiktionsanforderungen, ohne ISO-Audit oder Authority-Entscheidungen zu duplizieren.
---

# MDSAP Audit Readiness

## Zweck und Grenze

Dieser Skill bereitet vorhandene QMS-, Regulatory- und Quality-Evidenz auf einen MDSAP-Audit vor. Er bestimmt aus Audit-Typ, Herstellertätigkeiten, Sites, Produkten und tatsächlich relevanten MDSAP-Jurisdiktionen den aktuellen Prozess-/Task-Scope, verknüpft die erwarteten Tasks mit bestehender Evidenz und macht Readiness-Gaps sichtbar.

Er ersetzt weder `iso13485-qms-audit`, noch `fda-qmsr-inspection-readiness`, CAPA, Root-Cause-Analyse oder die Entscheidung eines MDSAP Auditing Organization (AO). Er simuliert keinen Audit und vergibt selbst keine MDSAP-Nonconformity-Grades.

## Current-source discipline

MDSAP-Dokumente sind versionsabhängig und werden zur Laufzeit aus der aktuellen offiziellen MDSAP-Dokumentbibliothek aufgelöst. Als verifizierter Stand 2026-08-07 ist `MDSAP AU P0002.010 Audit Approach` mit Versionsdatum 2026-02-02 aktuell. Spätere Versionen haben Vorrang. Audit-/Report-/NC-Formulare, Audit-Time-Verfahren, Membership-/Jurisdiktionsstatus und andere Programmdetails werden nicht als zeitloses Wissen eingefroren.

## Kernprinzipien

- **Current Audit Approach first:** Task-/Prozesslogik kommt aus der aktuell gültigen MDSAP-Quelle, nicht aus historischen Audit-Model-Screenshots oder Erinnerungen.
- **Jurisdiction scope follows market scope:** nur die regulatorischen Anforderungen der tatsächlich relevanten MDSAP-Jurisdiktionen werden in den Readiness-Scope aufgenommen.
- **Process links matter:** MDSAP ist prozess- und risikobasiert; Evidenz wird entlang der aktuellen Prozess-/Task-Verknüpfungen bewertet, nicht als isolierte Clause-Checkliste.
- **Audit type changes task scope:** Initial/Stage 1/Stage 2, Surveillance, Re-certification und Special Audit dürfen nicht als identischer Task-Scope behandelt werden.
- **ISO evidence is reused, not duplicated:** bestehende ISO-13485-QMS-/Audit-Evidenz wird referenziert und um MDSAP-spezifische Jurisdiktions-/Task-Anforderungen ergänzt.
- **Readiness is not audit outcome:** vollständige vorbereitete Evidenz ist keine AO-Konformitäts- oder Zertifizierungsentscheidung.

## Workflow

### 1. Audit Context fixieren

Erfasse Manufacturer/Legal Entity, Sites/Critical Locations, Products/Device Families, Activities, Märkte/Jurisdiktionen, vorhandene Zertifikate, geplanten Audit-Typ, bekannten AO-/Audit-Kontext soweit bestätigt und `asOf`. Unbestätigte Auditpläne bleiben `unknown`.

### 2. Current MDSAP Sources auflösen

Lade den aktuellen Audit Approach und die für den konkreten Audit relevanten Audit Procedures/Forms/Guides aus der offiziellen MDSAP-Dokumentbibliothek. Dokumentiere Code, Version/Datum, Source Reference und `asOf`.

### 3. Jurisdiction Applicability bestimmen

Mappe pro MDSAP-Jurisdiktion `in-scope|not-in-scope|uncertain` anhand tatsächlicher Market-/Registration-/Intended-Market-Evidence. Die bloße Teilnahme eines Landes am MDSAP macht dessen nationale Anforderungen nicht automatisch für den Hersteller-Audit relevant.

### 4. Process-/Task-Scope erzeugen

Mappe die aktuell anwendbaren Audit-Prozesse und Tasks einschließlich ihrer Verknüpfungen. Berücksichtige Audit-Typ und Organization Scope. Aktuelle MDSAP-Prozesslogik wird referenziert statt vollständig im Skilltext kopiert.

### 5. Evidence Readiness prüfen

Für jeden in-scope Task dokumentiere:
- Task/Process Reference,
- ISO-/Jurisdiction Requirement Reference,
- Site/Product/Process Scope,
- Evidence/Record References,
- Owner/Custodian,
- Version/Effective Date,
- Retrieval/Language State,
- Implementation-/Effectiveness Evidence,
- Gap/Unknown,
- Next Action.

Nutze vorhandene ISO-/QMS-/Supplier-/Design-/Production-/CAPA-/Complaint-/Regulatory Records über stabile Referenzen statt Shadow-Kopien.

### 6. Cross-owner Routing

- ISO-13485-Audit-/QMS-Finding → `iso13485-qms-audit`
- FDA-QMSR-spezifische Inspection Readiness → `fda-qmsr-inspection-readiness`
- Supplier → `supplier-quality-medical-device`
- Process Validation → `process-validation-iq-oq-pq`
- Risk → `medical-device-risk-management-iso14971`
- CAPA/System Gap → `medical-device-capa` / `evidence-based-causal-investigation`
- Regulatory Registration/Reporting Requirements → zuständiger Markt-Spezialist
- tatsächlicher Audit-Finding-/NC-Response → `audit-inspection-finding-response`.

### 7. Readiness State bilden

Pro Task mindestens `ready|partial|evidence-gap|retrieval-gap|effectiveness-gap|jurisdiction-uncertain|not-applicable|unknown`. Ein Task ist nicht `ready`, wenn nur eine Procedure existiert, aber Implementation-/Effectiveness-Evidence fehlt.

## Output-Verträge

`mdsap-audit-scope.json` enthält Audit Context, Audit Type, Sites/Activities, in-scope Jurisdictions, Current MDSAP Source Set, Processes/Tasks und Uncertainties.

`mdsap-task-readiness.json` enthält pro Process/Task Requirement/Jurisdiction Links, Evidence References, Implementation/Effectiveness State, Retrieval State, Owner, Gap und Next Action.

`mdsap-evidence-gaps.json` enthält priorisierte Gaps, betroffene Task-/Jurisdiction-Scopes, Risk/Compliance Impact, zuständigen Specialist Owner und Re-evaluation Trigger.

## Memory Path

Persistenzwürdig sind validierte MDSAP-Readiness-Muster, abstrahierte Process-/Task-Evidence-Heuristiken und stabile Jurisdiction-Scope-Patterns. Konkrete AO-Kommunikation, Auditpläne, Site-spezifische Findings, aktuelle NC-Grades, vertrauliche QMS-Records, momentane Zertifizierungszustände und volatile MDSAP-Dokumentversionen bleiben run-only bzw. kontrollierte Quality/Regulatory Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`; übergib nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- aktuelle offizielle MDSAP-Quellen mit Version/`asOf` verwendet werden,
- Audit-Typ, Sites/Activities und Jurisdiktionsscope belegt oder als Unknown markiert sind,
- MDSAP-Task-/Prozessverknüpfungen statt einer generischen ISO-Clause-Checkliste genutzt werden,
- nationale Requirements nur bei belegtem Jurisdiktionsscope angewendet werden,
- bestehende ISO-/QMS-Evidenz referenziert statt dupliziert wird,
- Procedure-Existenz nicht mit Implementation/Effectiveness gleichgesetzt wird,
- keine AO-/Zertifizierungsentscheidung oder NC-Graduierung simuliert wird,
- konkrete Audit-/Site-/Finding-Zustände nicht in globales dauerhaftes Memory gelangen.
