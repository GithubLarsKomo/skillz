---
name: ivdr-companion-diagnostic-consultation
description: Bewertet IVDR-Companion-Diagnostic-Scope und bereitet die Notified-Body-Konsultation mit EMA oder zuständiger Arzneimittelbehörde nach Artikel 48 evidenzgebunden vor, ohne Performance Evaluation oder externe Stellungnahme zu simulieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - ivdr-device-classification
  - ivdr-performance-evaluation
  - regulatory-evidence-traceability
  - decision-record
outputs:
  - cdx-scope-assessment.json
  - cdx-consultation-readiness.json
  - cdx-medicinal-product-linkage.json
lastEvaluated: 2026-08-07
---

# IVDR Companion Diagnostic Consultation

## Zweck und Grenze

Dieser Skill bewertet, ob ein IVD im konkreten Intended-Use-/Medicinal-Product-Kontext die IVDR-Definition eines Companion Diagnostic (CDx) erfüllt, und bereitet die für das Notified Body erforderliche wissenschaftliche Konsultation mit EMA oder einer zuständigen Arzneimittelbehörde nach Artikel 48 IVDR vor.

Er ersetzt weder `ivdr-performance-evaluation`, Arzneimittel-Zulassungsbewertung noch die Entscheidung des Notified Body oder die wissenschaftliche Stellungnahme von EMA/NCA. Externe Einreichung und Behördenkommunikation bleiben verifizierte Human-/External-Actions.

## Kernprinzipien

- **Definition before procedure:** CDx-Scope wird aus Artikel 2(7), Intended Use und dem konkreten Medicinal-Product-Linkage abgeleitet.
- **Essential-use linkage must be explicit:** bloße Biomarker-Assoziation oder prognostische Information ist nicht automatisch ein CDx.
- **Performance truth stays upstream:** analytische/klinische Performance und Scientific Validity werden referenziert, nicht neu bewertet.
- **NB owns consultation initiation:** der Hersteller bereitet Evidence vor; die formale Konsultation wird durch das Notified Body initiiert.
- **Opinion is not certificate:** EMA/NCA Scientific Opinion und spätere NB-Conformity-Decision bleiben getrennte externe Zustände.

## Workflow

### 1. Product- und Medicinal-Product-Kontext fixieren

Erfasse Intended Use, Biomarker/Analyte, Patient Selection/Risk Function, korrespondierendes Arzneimittel bzw. Arzneimittelklasse, Treatment Phase, Label-/SmPC-/Development Context und `asOf`.

### 2. CDx-Definition prüfen

Bewerte, ob das IVD für die sichere und wirksame Anwendung des korrespondierenden Arzneimittels wesentlich ist, insbesondere zur Identifikation von Patienten mit wahrscheinlichem Nutzen oder erhöhtem Risiko schwerwiegender Nebenwirkungen. Klassifiziere `cdx|not-cdx|borderline|evidence-missing` mit Rationale.

### 3. Evidence Linkage aufbauen

Referenziere Scientific Validity, Analytical/Clinical Performance, Intended Use/Claims, Risk und medicinal-product-relevante Evidence. Erzeuge keine zweite Performance-Evaluation.

### 4. Consultation Route bestimmen

Prüfe den aktuellen Artikel-48-/EMA/NCA-Kontext und dokumentiere `ema|national-competent-authority|route-to-be-decided-by-nb|uncertain`. Für EMA werden aktuelle procedural guidance, Practical Arrangements/Q&A, Form-/Letter-of-Intent-/Timetable-Anforderungen mit `asOf` geladen. Volatile Fristen/Fees/Form-Versionen werden nicht dauerhaft festgeschrieben.

### 5. Consultation Readiness

Mappe erforderliche Device-/Medicinal-Product-/Performance-/Labeling-/Risk-Evidence, offene Fragen, NB-owned Schritte, EMA/NCA Interaction Dependencies und Follow-up-/Change-Consultation Trigger.

### 6. Routing

- Performance Gap → `ivdr-performance-evaluation` bzw. Scientific/Analytical/Clinical Performance Owner.
- Label/Claim Gap → `medical-device-labeling-ifu` / `regulatory-claims-consistency`.
- Conformity/NB State → passender IVDR-Conformity-Pfad.
- tatsächliche NB→EMA/NCA Consultation → `human-procedure-wizard` oder autorisierter External-Action-Path.

## Output-Verträge

`cdx-scope-assessment.json` enthält Product/Medicinal Context, Article-2(7)-Mapping, CDx State, Evidence/Rationale, Sources/`asOf` und Uncertainty.

`cdx-medicinal-product-linkage.json` enthält Medicinal Product/Indication/Patient Selection Linkage, Intended Use/Claims, Evidence References, gaps und change triggers.

`cdx-consultation-readiness.json` enthält Consultation Route, NB-owned Steps, current procedural requirements, evidence package map, open questions, external state und verification needs.

## Memory Path

Persistenzwürdig sind nur abstrahierte, validierte CDx-Scope-/Consultation-Dependency-Muster mit Provenance/Freshness. Konkrete Arzneimittelentwicklungen, Sponsor-/NB-/EMA-Kommunikation, nicht veröffentlichte Biomarker-/Performance-Daten, Form-/Fee-/Timetable-Snapshots und aktuelle Opinion/Certificate States bleiben run-only oder kontrollierte Regulatory Records. Geeignete Kandidaten gehen ausschließlich an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- CDx-Scope aus Definition, Intended Use und Medicinal-Product-Linkage statt aus dem Schlagwort Biomarker abgeleitet wird,
- Performance-Evidence referenziert statt dupliziert wird,
- NB-Initiation und EMA/NCA Scientific Opinion als externe Zustände behandelt werden,
- Opinion und NB-Zertifizierungsentscheidung nicht gleichgesetzt werden,
- aktuelle EMA/NCA-Verfahrensinformationen mit `asOf` geführt werden,
- konkrete Arzneimittel-/Sponsor-/Consultation-Zustände nicht in globales dauerhaftes Memory gelangen.
