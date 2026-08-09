---
name: iec62304-software-lifecycle
description: Bewertet Medical-Device-Software-Lifecycle, Safety Class und Evidence Gaps entlang IEC 62304 ohne QMS oder Risk zu duplizieren.
---

# IEC 62304 Software Lifecycle

## Zweck und Grenze

Dieser Skill bewertet Software-Lifecycle-Evidence für Medical-Device-Software nach der organisationsseitig autorisierten aktuellen IEC-62304-Ausgabe und marktbezogenen Zusatzanforderungen. Er erzeugt kein zweites QMS/Risk Register und ersetzt weder Medical-Device-Systemvalidierung noch finale Produktfreigabe.

## Kernprinzipien

- **Authorized standard source:** konkrete normative Anforderungen werden aus der autorisierten aktuellen Normquelle referenziert, nicht aus reproduziertem Normtext.
- **Software scope first:** Software Item/System, Intended Use, Architecture, Interfaces, SOUP/Third-Party Components, Lifecycle State und Baseline müssen eindeutig sein.
- **Safety classification is evidence-backed:** Software Safety Class und Rationale werden auf Hazard-/Risk-/Control-Kontext zurückgeführt; Unsicherheit bleibt sichtbar.
- **Lifecycle evidence is linked:** Planning, Requirements, Architecture/Design, Implementation, Verification, Integration/System Interfaces, Problem Resolution, Configuration/Change und Maintenance werden über Evidence References verbunden.
- **Risk ownership stays ISO14971:** softwarebezogene Hazard-/Risk-Information wird im bestehenden Risk Lifecycle geführt.
- **Lifecycle completion ≠ device validation:** vollständige Software-Lifecycle-Evidence ersetzt keine finale Device/System Validation oder Release Authority.

## Workflow

### 1. Software Scope und Baseline fixieren

Erfasse Software System/Items, Device/IVD-Kontext, Intended Use, Interfaces, Version/Baseline, Deployment/Runtime, SOUP/Third-Party Dependencies und Lifecycle Stage.

### 2. Current Standard/Market Context laden

Verifiziere aktuelle IEC-62304-Ausgabe/Amendments und relevante marktbezogene Software-Guidance/Recognized-Standard-Stände mit `asOf`. Normtexte werden nur aus autorisierter Quelle angewendet.

### 3. Safety Classification und Risk Links

Dokumentiere Safety Class State, Rationale, Hazard/Risk References, Risk Controls und offene Klassifikationsfragen. Keine Class wird nur aus Projektkonvention übernommen.

### 4. Lifecycle Evidence Map

Mappe relevante Lifecycle-Aktivitäten auf kontrollierte Artefakte, Versionen und Verification Evidence. Klassifiziere `covered|partial|missing|stale-baseline|not-applicable-with-rationale|unknown`.

### 5. SOUP/Dependency und Change Lineage

Erfasse Third-Party/SOUP Identity, Version, Intended Role, Known Issue/Security/Risk References, Verification/Integration Evidence und Change Impact. Supplier-/Cybersecurity-Themen werden an bestehende Owner geroutet.

### 6. Routing

- Risk/Hazard → `medical-device-risk-management-iso14971`
- Design Traceability → `design-control-traceability`
- Usability/User Interface → `iec62366-usability-engineering`
- Cybersecurity → `medical-device-cybersecurity-lifecycle`
- QMS/Process Gap → `medical-device-qms-iso13485`
- Design/Software Change → `design-change-regulatory-impact`
- Controlled Records → `controlled-quality-documentation` / `quality-record-integrity`.

## Output-Verträge

`software-lifecycle-assessment.json` enthält Software Scope/Baseline, Current Standard Context, Lifecycle Evidence Map, SOUP/Dependency References, Change Lineage, Coverage/Evidence State und `asOf`.

`software-safety-classification.json` enthält Software Item/System, Safety Class State, Rationale, Risk/Hazard/Control References, Evidence, Uncertainty und Human Approval State.

`software-evidence-gaps.json` enthält Gap ID, Lifecycle Area, Artifact/Baseline, Risk/Requirement Link, Missing Evidence, Impact, Owner/Next Skill und Closure Evidence.

## Memory Path

Persistenzwürdig sind validierte Lifecycle-Mapping-Heuristiken, abstrahierte Safety-Classification-Decision-Factors und wiederverwendbare SOUP-/Baseline-Gap-Muster. Konkrete Source Code/Architecture, Versionsstände, Vulnerabilities, unresolved anomalies, aktuelle Safety-Class Decisions und unreleased Software Details bleiben run-only bzw. in kontrollierten Engineering/Quality Records. Norm-/Guidance-Kandidaten benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Authorized standard source** verwendet wird,
- Software Scope/Baseline eindeutig sind,
- **Safety classification is evidence-backed** statt bloß übernommen wird,
- Lifecycle Evidence versioniert und traceable ist,
- Risk Management nicht dupliziert wird,
- SOUP/Third-Party-/Change-Gaps sichtbar bleiben,
- **Lifecycle completion ≠ device validation** respektiert wird,
- konkrete Software-/Security-/Class-Zustände nicht in globales dauerhaftes Memory gelangen.
