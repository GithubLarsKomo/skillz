---
name: fda-pccp-change-control
description: Bewertet bestätigte Medical-Device-Änderungen gegen einen tatsächlich autorisierten oder cleared FDA-PCCP-Scope, trennt PCCP-konforme Umsetzung von neuer Submission und routet Abweichungen in bestehende Change-/Submission-Pfade.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - design-change-regulatory-impact
  - regulatory-evidence-traceability
  - medical-device-risk-management-iso14971
  - decision-record
outputs:
  - pccp-applicability.json
  - pccp-change-evidence.json
  - pccp-deviation-routing.json
lastEvaluated: 2026-08-07
---

# FDA PCCP Change Control

## Zweck und Grenze

Dieser Skill bewertet eine **konkret beschriebene Änderung** gegen einen für das konkrete Device tatsächlich von FDA autorisierten/cleared Predetermined Change Control Plan (PCCP). Er nutzt Section 515C des FD&C Act als gesetzliche Grundlage und prüft zusätzlich die zum Device Scope passende aktuelle FDA-Guidance. Die allgemeine Device-PCCP-Guidance bleibt solange als Draft zu behandeln, wie FDA sie nicht finalisiert; für AI-enabled Device Software Functions kann die aktuelle finale AI-PCCP-Guidance einschlägig sein.

Der Skill erzeugt keine neue technische Änderung, ersetzt nicht `design-change-regulatory-impact`, erfindet keinen autorisierten PCCP und simuliert keine FDA-Freigabe.

## Kernprinzipien

- **Authorized PCCP first:** PCCP-Anwendung setzt nachweisbaren Authorization-/Clearance-Scope voraus.
- **Change-to-plan match:** geplante Änderung, Modification Description, Modification Protocol und Impact Assessment werden explizit abgeglichen.
- **No scope expansion by interpretation:** ähnliche Änderungen werden nicht still in den PCCP hineingelesen.
- **Evidence before implementation release:** die im PCCP verlangte Verifikation/Validierung und Kontrolllogik muss für die konkrete Änderung erfüllt sein.
- **PCCP does not erase other obligations:** Risk, Labeling, Cybersecurity, QMS, Corrections/Removals, MDR und Registration/Listing bleiben eigene Pflichten.

## Workflow

### 1. Device- und PCCP-Baseline fixieren

Erfasse Device, Authorization/510(k)/PMA/De-Novo-Kontext, PCCP-Identifier/Decision Evidence, genehmigten bzw. cleared Scope, aktuelle Labeling-/Software-/Manufacturing-Baseline und `asOf`.

### 2. Change aus bestehendem Change-Control übernehmen

Übernimm Change ID, Before/After, betroffene Komponenten/Software/Prozesse/Claims/Risks und V&V Needs aus `design-change-regulatory-impact`. Keine zweite Change-Analyse erzeugen.

### 3. PCCP Applicability prüfen

Ordne die konkrete Änderung ein als `within-authorized-pccp|partially-matched|outside-pccp|authorization-evidence-missing|uncertain`. Prüfe insbesondere, ob die Änderung von der beschriebenen Modification abgedeckt ist und ob der vorgesehene Modification Protocol/Impact Assessment anwendbar bleibt.

### 4. Evidence Gates prüfen

Mappe PCCP-spezifische Test-/Validation-/Monitoring-/Rollback-/Labeling-/Risk-/Cybersecurity-Gates auf vorhandene Evidence. Offene Gates bleiben blockierend sichtbar.

### 5. Regulatory Routing

- `within-authorized-pccp` + alle Evidence Gates erfüllt → PCCP-konforme Implementierungsentscheidung kann intern vorbereitet werden.
- `partially-matched|outside-pccp|uncertain` → zurück an `design-change-regulatory-impact`; bei Submission-/FDA-Feedback-Fragen an passenden 510(k)/PMA/De-Novo-/Q-Sub-Pfad.
- tatsächliche externe Submission/Receipt/Authorization → nur verifizierter Human-/External-Action-Path.

## Output-Verträge

`pccp-applicability.json` enthält Device/PCCP Baseline, Authorization Evidence, Change ID, Scope Match, Current Sources/`asOf`, Decision State, Rationale und Human/Authority Boundary.

`pccp-change-evidence.json` enthält PCCP Requirement/Protocol Step, Required Evidence, Existing Evidence, Gap, Owner, Completion Evidence und Release Gate.

`pccp-deviation-routing.json` enthält außerhalb/teilweise passende Änderungen, Reason, Regulatory Question, Next Skill/Action und Re-evaluation Trigger.

## Memory Path

Persistenzwürdig sind nur abstrahierte validierte PCCP-Scope-/Evidence-Muster mit Provenance/Freshness. Konkrete Device-PCCPs, Authorization IDs, FDA-Feedback, unreleased Changes, Testresultate und aktuelle Submission-/Decision-States bleiben run-only oder in kontrollierten Regulatory/Design Records. Übergib geeignete Kandidaten ausschließlich an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- ein realer PCCP-/Authorization-Scope nachgewiesen oder explizit als fehlend markiert ist,
- die Änderung nicht allein aufgrund Ähnlichkeit als PCCP-konform eingestuft wird,
- Modification Protocol und Impact Assessment gegen konkrete Evidence geprüft werden,
- allgemeine Draft- und finale scope-spezifische FDA-Guidance nicht vermischt werden,
- offene PCCP-/Risk-/V&V-Gates Release nicht verdecken,
- interne PCCP-Readiness nicht als FDA-Authorization dargestellt wird,
- konkrete Change-/Authorization-Daten nicht in globales dauerhaftes Memory gelangen.
