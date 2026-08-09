---
name: ivdr-class-d-conformity
description: Plant IVDR-Class-D-Conformity mit NB/EURL-, Performance-, Common-Specification- und Batch-Testing-Abhängigkeiten.
---

# IVDR Class D Conformity

## Zweck und Grenze

Dieser Skill plant die **Class-D-spezifischen** Conformity-Assessment-Abhängigkeiten eines bereits als Class D bewerteten IVD. Er führt weder Classification noch Performance Evaluation erneut durch und simuliert keine Entscheidung einer Benannten Stelle (NB), eines EU Reference Laboratory (EURL), einer zuständigen Behörde oder der Europäischen Kommission.

## Kernprinzipien

- **Class D confirmed first:** der Skill startet erst mit einer nachvollziehbaren Class-D-Hypothese/Decision State aus `ivdr-device-classification`.
- **Current external applicability:** NB-, EURL-, Common-Specification- und Batch-Testing-Pflichten werden für den konkreten Device Scope aus aktuellen autoritativen Quellen bestimmt.
- **EURL scope is conditional:** EURL-Beteiligung wird nur dort als konkret anwendbar behandelt, wo ein designiertes EURL und dessen Scope/aktuelle Aufgaben tatsächlich passen.
- **Performance evidence stays upstream:** Scientific Validity, Analytical und Clinical Performance bleiben Eigentum der bestehenden Performance-Skills; Class-D-Conformity referenziert diese Evidence.
- **External decisions remain external:** Review, Verification, Testing, Certificate-/Opinion-/Result-State werden nur aus verifizierter externer Evidenz gesetzt.
- **Batch release is evidence-gated:** geplante oder erwartete Batch-Testing-Schritte sind kein bestandener Batch-Release-Nachweis.

## Workflow

### 1. Class-D- und Product Scope fixieren

Übernimm Device/Variant, Intended Purpose, Analyte/Pathogen/Condition, Classification Rule/Rationale, Lifecycle Stage, Markets, relevante Performance-Evidence und bisherige NB-/Certificate-/Legacy-/Transition-States.

### 2. Current Conformity Context laden

Nutze `mdcg-guidance-navigator` und autoritative EU-/IVDR-Quellen, um aktuelle Anforderungen zu bestimmen. Prüfe insbesondere:
- anwendbaren Conformity-Assessment-Pfad und NB-Rolle,
- einschlägige Common Specifications soweit vorhanden/anwendbar,
- designierte EURLs und deren Scope,
- EURL Performance-/CS-Verification soweit anwendbar,
- Batch-Testing-/Sample-/Logistics-/Release-Abhängigkeiten soweit anwendbar,
- aktuelle Transitional-/Derogation-/Special-Arrangement-Fragen, falls tatsächlich relevant.

### 3. Evidence-to-External-Gate Mapping

Mappe jede externe Frage auf bestehende Evidence References und Status:
`ready|partial|missing|external-review-pending|external-test-pending|not-applicable-with-rationale|unknown`.

### 4. External Dependencies strukturieren

Erfasse NB/EURL/Authority Dependency, Scope, benötigte Inputs/Samples, Owner, gewünschtes Resultat, Authority Boundary, Prerequisites, Current State und Verification Evidence. Externe Termine oder Resultate werden nicht erfunden.

### 5. Batch-/Release-Abhängigkeiten planen

Wenn current-source-basiert anwendbar, dokumentiere Batch-Testing-/Sample-/Logistics-/Result-Gates und die Verbindung zum internen Release-Prozess. Ein interner Release darf ein erforderliches externes Gate nicht verdecken.

### 6. Routing

- Classification Gap → `ivdr-device-classification`
- Performance Evidence Gap → `ivdr-performance-evaluation` bzw. dessen drei Evidence-Worker
- Current Guidance/CS/EURL Scope → `mdcg-guidance-navigator`
- Risk Impact → `medical-device-risk-management-iso14971`
- Labeling/Claim Impact → `medical-device-labeling-ifu` / `regulatory-claims-consistency`
- kontrollierte Dokumente → `controlled-quality-documentation`
- NB/EURL-/Portal-/Sample-/Submission-Aktion → `human-procedure-wizard` oder autorisierter External-Action-Path.

## Output-Verträge

`class-d-conformity-plan.json` enthält Device/Class-D Context, Current Sources/`asOf`, Conformity Route, Performance/Common-Specification References, External Gates, Internal Prerequisites, Status, Gaps und Next Skills.

`class-d-external-dependencies.json` enthält Dependency ID, External Party/Role, Applicability Rationale, Scope, Required Inputs/Samples, Expected Evidence, Current State, Human/Authority Boundary und verified Completion Evidence.

## Memory Path

Persistenzwürdig sind validierte Class-D-Dependency-Heuristiken, abstrahierte NB/EURL-Gate-Muster und wiederverwendbare Evidence-to-External-Gate-Mappings. Konkrete NB/EURL-Kommunikation, aktuelle EURL-Scope-Snapshots, Sample-/Batch-IDs, Review-/Testresultate, Certificate States und aktuelle Termine bleiben run-only bzw. in kontrollierten Regulatory/Quality Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Class D confirmed first** eingehalten wird,
- EURL-/CS-/Batch-Pflichten current-source- und scope-basiert statt pauschal angenommen werden,
- vorhandene Performance-Evidence referenziert statt neu bewertet wird,
- **EURL scope is conditional** explizit geprüft wird,
- externe NB/EURL-/Authority-States nicht simuliert werden,
- erforderliche externe Batch-/Release-Gates nicht als intern erledigt ausgegeben werden,
- konkrete externe/batchbezogene Zustände nicht in globales dauerhaftes Memory gelangen.
