---
name: fda-qmsr-inspection-readiness
description: Bereitet Medical-Device-QMS-Evidenz auf aktuelle FDA-QMSR-Inspektionen vor, identifiziert Retrieval-, Record-, Evidence- und Remediation-Gaps und vermeidet QSIT-Legacy.
---

# FDA QMSR Inspection Readiness

## Zweck und Grenze

Dieser Skill bereitet vorhandene Medical-Device-QMS-Evidenz auf eine aktuelle FDA-QMSR-Inspektion vor. Er baut einen prüfbaren Evidence-/Record-Index, identifiziert Retrieval-, Coverage-, Effectiveness-, Record-Integrity- und Remediation-Gaps und priorisiert diese nach Inspection-/Compliance-/Patient-Impact. Er **simuliert keine FDA-Inspektion**, erzeugt keine rückdatierten Records und ersetzt weder `iso13485-qms-audit` noch CAPA oder QMS-Prozessverantwortung.

Seit 2. Februar 2026 gilt QMSR; aktuelle FDA-Inspektionen folgen dem jeweils gültigen Medical-Device-Inspection-Programm und nicht QSIT. Volatile FDA-Inspection-Informationen werden deshalb mit autoritativer Quelle und `asOf` geladen statt dauerhaft in den Skilltext eingebrannt.

## Kernprinzipien

- **Current inspection model:** aktuelle QMSR-/FDA-Inspection-Quellen statt QSIT-/QS-Reg-Legacy.
- **Evidence retrieval matters:** Compliance-Evidenz muss nicht nur existieren, sondern identifizierbar, versionsklar, zugänglich und rechtzeitig abrufbar sein.
- **Record visibility:** QMS-Records werden nach aktuellem FDA-Zugriffs-/Inspection-Kontext bewertet; historische Annahmen über pauschale Ausnahmen werden nicht übernommen.
- **No evidence manufacturing:** fehlende Records bleiben Gaps; keine nachträgliche Erfindung, Rückdatierung oder kosmetische Rekonstruktion.
- **Audit ≠ inspection:** interne/ISO-Audits liefern Evidenz und Findings, sind aber keine Simulation einer FDA-Authority-Entscheidung.
- **Remediation routing:** echte System-/Process-Gaps gehen an QMS/CAPA/Controlled Documentation statt in ein separates Inspection-CAPA-System.

## Workflow

### 1. Inspection Context fixieren

Erfasse Site, Legal Manufacturer/Establishment Context, Products/Processes, Inspection Anlass soweit bekannt, aktuelle QMSR-/Inspection-Programm-Quelle, `asOf`, Sprachen/Record Locations und verfügbare Ansprechpartner. Unbestätigte FDA-Absichten werden als unbekannt markiert.

### 2. Existing Evidence übernehmen

Konsumiere `qmsr-iso13485-delta.json`, aktuelle interne/ISO-Audit-Evidenz, relevante CAPA-/Complaint-/Supplier-/Management-/Design-/Production-/Validation-/Record-Signale und vorhandene kontrollierte QMS-Records. Inhalte werden referenziert, nicht in eine Shadow-QMS-Ablage kopiert.

### 3. Inspection Evidence Index

Erfasse pro Evidence Item mindestens:
- Record/Artifact ID und kontrollierte Quelle,
- Requirement/Process Link,
- Site/Product Scope,
- Version/Effective Date,
- Owner/Custodian,
- Retrieval Location/Format/Language,
- Coverage-/Evidence-/Effectiveness Status,
- Confidentiality/handling note,
- Gap/Action.

### 4. Retrieval- und Record-Readiness prüfen

Prüfe, ob relevante Records tatsächlich gefunden, geöffnet, versionsrichtig zugeordnet und bei Bedarf in geeigneter Sprache bereitgestellt werden können. Records vor dem QMSR-Effektivtatum werden nicht pauschal ausgeschlossen; aktuelle FDA-Regeln/FAQ bestimmen die Review-Relevanz.

### 5. High-risk Gaps priorisieren

Klassifiziere mindestens `missing-record|stale-record|version-ambiguity|retrieval-gap|coverage-gap|effectiveness-gap|open-capa|supplier-gap|validation-gap|record-integrity-gap|unknown`. Priorisierung folgt Compliance-/Patient-/Inspection-Impact, nicht Präsentationsästhetik.

### 6. Remediation und Human Boundary

- QMS-Prozess-/QMSR-Gap → `medical-device-qms-iso13485` / `fda-qmsr-iso13485-gap`
- Audit/Systemfinding → `medical-device-capa` / `evidence-based-causal-investigation`
- Dokument-/Record-Kontrolle → `controlled-quality-documentation`
- Supplier Gap → `supplier-quality-medical-device`
- Process Validation Gap → `process-validation-iq-oq-pq`
- konkrete externe FDA-Kommunikation, Record Request oder On-site-Aktion → autorisierter Mensch/Prozess; Status nur nach externer Evidenz als erfolgt markieren.

## Output-Verträge

`inspection-evidence-index.json` enthält Inspection Context, `asOf`, Evidence Items, Requirement/Process Links, Retrieval Metadata, Version/Language/Owner, Coverage/Evidence Status und Gaps.

`qmsr-inspection-readiness.json` enthält Readiness Summary, High-risk Gaps, Remediation Routing, Open CAPA/Validation/Supplier/Record Issues, Human/Authority Boundaries und Stop Conditions.

## Memory Path

Persistenzwürdig sind validierte Inspection-Readiness-Muster, wiederverwendbare Record-Retrieval-Heuristiken und abstrahierte Evidence-Index-Praktiken. Konkrete Inspection-Signale, FDA-Anfragen, Site-spezifische Findings, vertrauliche Records, aktuelle CAPA-Zustände und momentane FDA-Inspection-Snapshots bleiben run-only bzw. in kontrollierten Quality Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- aktuelle QMSR-/Inspection-Quellen statt QSIT-Legacy verwendet werden,
- Evidence Existenz, Version, Retrieval und Effectiveness getrennt sichtbar sind,
- historische Record-Ausnahmen nicht ungeprüft übernommen werden,
- fehlende Records nicht erfunden oder rückdatiert werden,
- interne Audits nicht als FDA-Inspection-Ergebnis dargestellt werden,
- echte Systemgaps an QMS/CAPA/Validation/Supplier Owner geroutet werden,
- konkrete FDA-/Site-/Inspection-Zustände nicht in globales dauerhaftes Memory gelangen.
