---
name: quality-record-integrity
description: Prüft Medical-Device-Qualitätsaufzeichnungen auf Integrität, Attribution, Zeitbezug, Version/Quelle, Korrekturen, Audit Trail, Zugriff und verlässliche Retrieval-Evidenz.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - controlled-quality-documentation
  - medical-device-qms-iso13485
  - two-axis-compliance-review
outputs:
  - quality-record-integrity-assessment.json
  - record-integrity-gaps.json
  - record-retrieval-index.json
lastEvaluated: 2026-08-07
---

# Quality Record Integrity for Medical Devices

## Zweck und Grenze

Dieser Skill prüft, ob Medical-Device-/IVD-Qualitätsaufzeichnungen als verlässliche Evidenz genutzt werden können. Er bewertet Record Identity, Attribution, zeitlichen Bezug, Original-/True-Copy-/Source-Bezug, Version/Status, Korrekturen, Audit-Trail-/Metadata-Kontext, Vollständigkeit, Zugriff/Retrieval und Schutz vor unkontrollierter Änderung.

Er ersetzt **nicht** `controlled-quality-documentation`: Dokumentenlenkung besitzt Template/Revision/Approval/Effective-State/Supersession; dieser Skill besitzt ausschließlich die Integritäts- und Evidenzfrage bereits erzeugter Records. Er ist auch kein generisches Enterprise-Data-Governance- oder Cybersecurity-System.

## Kernprinzipien

- **Document ≠ record:** ein kontrolliertes Blanko-Formular oder eine Procedure ist keine ausgefüllte Evidence-Aufzeichnung.
- **Evidence must be attributable:** relevante Einträge müssen nachvollziehbar auf Ersteller/System, Zeitpunkt, Gegenstand und Quelle zurückführbar sein.
- **Contemporaneous and traceable changes:** verspätete Einträge, Corrections und Ergänzungen bleiben erkennbar; ursprüngliche Information wird nicht unkontrolliert überschrieben.
- **Original/true-copy context:** Scan, Export, Report, Screenshot oder Transcription benötigt nachvollziehbaren Source-/True-Copy-Kontext, wenn er als kontrollierte Evidenz dienen soll.
- **Electronic context matters:** bei elektronischen Records werden relevante Metadata, Audit Trail, Access/Role, Time/Sequence, System Version und Export-/Migration-Kontext berücksichtigt.
- **Retrievable evidence:** Record Existenz allein genügt nicht, wenn Identity, Version, Vollständigkeit oder Retrieval nicht belastbar sind.
- **No record repair fiction:** fehlende oder unzuverlässige Records werden nicht rückdatiert, still überschrieben oder durch nachträgliche Narrative in historische Primärevidenz verwandelt.

## Workflow

### 1. Record Purpose und Scope fixieren

Erfasse Record Type/ID, Process/Requirement Link, Product/Site/Lot/Study/Equipment/Software Scope soweit relevant, Intended Evidence Use, System/Repository und erforderliche Retention/Access-Kontexte aus aktuellen QMS-/Regulatory Sources.

### 2. Identity und Source prüfen

Prüfe eindeutige Record Identity, Source System/Original, Version/Revision soweit anwendbar, Ersteller/System Attribution, Date/Time/Sequence, referenced objects und Beziehungen zu kontrollierten Procedures/Templates. Unklare Kopien/Exports werden als solche markiert.

### 3. Completeness und Consistency

Prüfe Required Fields/Attachments/Signatures/Approvals soweit für den Record verlangt, erwartete Sequence/Chronology, Cross-References und Widersprüche zu verwandten Records. Fehlende Information wird als Gap sichtbar, nicht ergänzt erfunden.

### 4. Corrections und Audit Trail

Bewerte, ob Korrekturen/Änderungen ursprüngliche Information erhalten, Reason/Actor/Time nachvollziehbar machen und autorisierte Controls nutzen. Bei elektronischen Systemen prüfe verfügbare Audit-Trail-/Metadata-Evidence risikobasiert; ein PDF-Export allein darf relevante elektronische Historie nicht unsichtbar machen.

### 5. Retrieval und Preservation

Prüfe, ob Records im vorgesehenen Zeitraum lesbar, vollständig, versionsklar und mit relevanten Metadata/Attachments abrufbar bleiben. Migration/Archive/Backup/Format Conversion werden auf Evidenzverlust oder Provenance-Brüche bewertet.

### 6. Integrity State klassifizieren

Mindestens:
- `reliable-evidence`,
- `reliable-with-context-limitations`,
- `integrity-gap-open`,
- `identity-or-source-ambiguous`,
- `incomplete`,
- `unreliable-for-intended-evidence-use`,
- `unknown`.

Ein formaler Approval-/Signature-State allein erzwingt kein `reliable-evidence`.

### 7. Gap Routing

- Dokumenten-/Record-Control-Prozess → `controlled-quality-documentation`
- QMS-Systemgap → `medical-device-qms-iso13485`
- systemischer Integrity-/Process-Finding → `medical-device-capa` / `evidence-based-causal-investigation`
- Inspection Retrieval → `fda-qmsr-inspection-readiness`
- NC/MRB aufgrund unzuverlässiger Evidence → `nonconformance-mrb-disposition`
- Produktions-/Process Validation Record → `process-validation-iq-oq-pq`
- Measurement Evidence → `measurement-system-validation`.

## Output-Verträge

`quality-record-integrity-assessment.json` enthält Record Identity/Source, Intended Evidence Use, Attribution/Time/Version Context, Completeness, Correction/Audit-Trail/Metadata State, Retrieval/Preservation State, Overall Integrity State und Source References.

`record-integrity-gaps.json` enthält Gap ID, Record/Process Link, Gap Type, Evidence Impact, Risk/Compliance Impact, Needed Action, Owner/Next Skill und Stop Condition.

`record-retrieval-index.json` enthält Record Location/Repository, Source/Copy State, Format/Language, Version/Time Range, Custodian, Retrieval Test State und relevante Metadata/Attachment Links ohne unnötige Record-Inhalte zu duplizieren.

## Memory Path

Persistenzwürdig sind validierte Record-Integrity-/Retrieval-Heuristiken, wiederverwendbare Audit-Trail-/True-Copy-/Correction-Prüfmuster und abstrahierte Preservation-/Migration-Learnings. Konkrete Record-Inhalte, personenbezogene Daten, Lot/Serial/Patient/Employee-Daten, Signaturen, Audit Trails, Access Logs, aktuelle Integrity Findings und vertrauliche Quality Records bleiben run-only bzw. in kontrollierten Systemen. Kandidaten benötigen `sourceRefs`; system-/regulatory-abhängige Learnings zusätzlich `asOf`/`reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Dokument und Record semantisch getrennt werden,
- Record Identity, Attribution, Time/Source und Intended Evidence Use nachvollziehbar sind,
- Corrections/Audit Trail ursprüngliche Information und Änderungskontext erhalten,
- Export/Kopie nicht ohne Source-Kontext als Original-Evidenz behandelt wird,
- Retrieval/Vollständigkeit als Teil der Evidenzfähigkeit geprüft werden,
- fehlende oder problematische Records nicht rückdatiert oder narrativ repariert werden,
- konkrete Record-/Audit-Trail-/Personenzustände nicht in globales dauerhaftes Memory gelangen.
