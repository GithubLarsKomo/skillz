---
name: medical-device-cybersecurity-lifecycle
description: Steuert Medical-Device-Cybersecurity über Design, Premarket Evidence, Vulnerability Management und Postmarket Actions.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - design-control-traceability
  - iec62304-software-lifecycle
outputs:
  - cybersecurity-lifecycle-assessment.json
  - cybersecurity-evidence-map.json
  - cybersecurity-postmarket-actions.json
lastEvaluated: 2026-08-07
---

# Medical Device Cybersecurity Lifecycle

## Zweck und Grenze

Dieser Skill strukturiert Medical-Device-Cybersecurity als Lifecycle über Secure Design, Risk/Evidence, Premarket-Readiness, Vulnerability Management und Postmarket-Actions. Er ersetzt weder Product Security Engineering noch ISO14971, Software Lifecycle, CAPA/PMS oder externe FDA/EU-Entscheidungen.

## Kernprinzipien

- **Current cyber-device applicability:** FDA-524B-/Cyber-Device- und andere marktbezogene Pflichten werden current-source-basiert auf den konkreten Device Scope angewendet, nicht pauschal auf jedes Softwareprodukt.
- **Security risk links to safety and performance:** Cyber Threats/Vulnerabilities werden mit Security Impact, Safety/Essential Performance/Clinical Impact und bestehenden Risk Controls verbunden.
- **Secure architecture is evidence-backed:** Security Architecture, Trust Boundaries, Assets, Interfaces, Authentication/Authorization, Update/Recovery und Logging werden über kontrollierte Evidence referenziert.
- **SBOM is controlled evidence:** SBOM/Component Inventory muss zur aktuellen Software-/SOUP-Baseline passen; eine Liste ohne Version/Provenance/Change Lineage ist kein ausreichender Lifecycle-Nachweis.
- **Premarket and postmarket are continuous:** Submission Evidence beendet Vulnerability Monitoring, Coordinated Disclosure, Patch/Update-, Incident-/Risk-/CAPA-/PMS-Aktivitäten nicht.
- **Security change follows change control:** Remediation/Patch/Config Change wird auf Verification, Risk, Usability, Regulatory und Release Impact geprüft.

## Workflow

### 1. Cybersecurity Scope fixieren

Erfasse Device/Software Baseline, Connectivity, Assets/Data, Interfaces, Deployment/Update Model, Users/Roles, Network/Cloud/Mobile Dependencies, SOUP/Third-Party Components und Zielmärkte.

### 2. Current Regulatory/Standard Context laden

Verifiziere aktuelle FDA Cybersecurity Guidance/gesetzliche Applicability, EU-/MDCG-/harmonisierte/recognized Standards soweit relevant sowie organisationsseitig autorisierte Security-Normen mit `asOf`. Alte Guidance-Versionen werden nicht ungeprüft weiterverwendet.

### 3. Security Architecture und Threat/Risk Evidence

Mappe Assets, Trust Boundaries, Threats/Vulnerabilities, Attack Paths, Security Controls, Detection/Recovery und Residual Security/Safety Impact auf Design-/Software-/Risk-Evidence. Kein zweites Product Risk Register.

### 4. Component/SBOM Evidence

Prüfe Component Identity/Version/Source, SOUP Links, Known Vulnerability/Support State, Patch/Update Path und Baseline Traceability. Stale oder unauflösbare Components bleiben Gap.

### 5. Premarket Evidence Map

Mappe current-source-basiert erforderliche/empfohlene Cybersecurity Submission Evidence auf vorhandene Artifacts. Klassifiziere `ready|partial|missing|not-applicable-with-rationale|stale-baseline|unknown`.

### 6. Postmarket/Vulnerability Loop

Erfasse Vulnerability/Incident Signal, Triage, Exploitability/Impact, Risk Update, Mitigation/Compensating Control, Patch/Update Need, Verification, Disclosure/Communication, Reporting/PMS/CAPA/Recall Routing und Closure Evidence.

### 7. Routing

- Software/SOUP Baseline → `iec62304-software-lifecycle`
- Product/Safety Risk → `medical-device-risk-management-iso14971`
- UI/Security-Use Impact → `iec62366-usability-engineering`
- Security Change → `design-change-regulatory-impact`
- Labeling/Instructions → `medical-device-labeling-ifu`
- FDA Submission → FDA Front Door/eSTAR/Response Skills
- Complaint/MDR → `fda-complaint-mdr-reportability`
- EU PMS/Vigilance → `ivdr-pms-vigilance`
- Systemic Cause/CAPA → existing RCA/CAPA Lifecycle.

## Output-Verträge

`cybersecurity-lifecycle-assessment.json` enthält Device/Software Scope/Baseline, Current Regulatory Applicability/`asOf`, Architecture/Threat/Risk State, Component/SBOM State, Premarket/Postmarket Readiness und Gaps.

`cybersecurity-evidence-map.json` enthält Security Requirement/Threat/Control, Design/Software/Risk References, Verification Evidence, Submission/Market Relevance, Baseline und Status.

`cybersecurity-postmarket-actions.json` enthält Vulnerability/Incident Signal, Assessment, Risk/Design Links, Mitigation/Patch/Verification, Disclosure/Reporting/PMS/CAPA Routing, Owner, External State und Closure Evidence.

## Memory Path

Persistenzwürdig sind validierte Threat-/Control-/Evidence-Mapping-Heuristiken, abstrahierte SBOM-/Baseline-Checks und wiederverwendbare Vulnerability-Triage-/Change-Routing-Muster. Konkrete Vulnerabilities, exploit details, product architectures, credentials/secrets, SBOM contents, current incidents, unpatched states, submission details und security findings bleiben run-only bzw. in kontrollierten Security/Engineering/Quality Records. Regulatory/Security Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Current cyber-device applicability** geprüft ist,
- Security Risk mit Safety/Performance/Risk Evidence verknüpft ist,
- **SBOM is controlled evidence** statt bloßer Liste ist,
- Premarket/Postmarket als kontinuierlicher Lifecycle behandelt werden,
- Security Changes durch Design-/Risk-/Verification-/Regulatory-Change-Control laufen,
- externe Reporting-/Submission-/Authority-States nicht simuliert werden,
- Secrets/Vulnerability-/Incident-/Architekturdetails nicht in globales dauerhaftes Memory gelangen.
