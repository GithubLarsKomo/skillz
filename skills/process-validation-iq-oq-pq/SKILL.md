---
name: process-validation-iq-oq-pq
description: Plant und bewertet risikobasierte Medical-Device-Prozessvalidierung mit geeigneter IQ/OQ/PQ-Evidenz, vorab definierten Kriterien, Revalidierung und Change-Traceability.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-qms-iso13485
  - medical-device-risk-management-iso14971
  - design-control-traceability
outputs:
  - process-validation-strategy.json
  - process-validation-protocol.md
  - process-validation-assessment.json
lastEvaluated: 2026-08-07
---

# Medical Device Process Validation — IQ/OQ/PQ

## Zweck und Grenze

Dieser Skill entscheidet und strukturiert risikobasierte Prozessvalidierung für Medical-Device-/IVD-Herstell-, Prüf-, Verpackungs-, Reinigungs-, Software-/Automations- oder Serviceprozesse. Er verbindet Process Need, Risk, Process Characterization, Equipment/System Readiness, vorab definierte Acceptance Criteria, geeignete Qualification-/Validation-Evidenz und Revalidation Trigger. Er ersetzt weder Design Verification/Validation noch Measurement-System- oder Software-Assurance-Spezialarbeit.

IQ/OQ/PQ ist ein etabliertes Evidenzmuster, aber **kein blindes Pflichtformular für jeden Prozess**. Die konkrete Validierungsstrategie folgt aktuellem QMSR-/ISO-13485-Kontext, Prozessrisiko, Fähigkeit zur vollständigen Verifikation und geeigneter fachlicher Guidance. Medizinproduktespezifische GHTF/IMDRF-Prozessvalidierungsgrundsätze können ergänzend verwendet werden; FDA-Guidance aus anderen Produktbereichen wird nicht fälschlich als device-spezifische Rechtsquelle dargestellt.

## Kernprinzipien

- **Validate when needed:** zuerst klären, ob Prozessoutput vollständig verifizierbar ist und welche Validierungs-/Verifikationsstrategie regulatorisch und technisch angemessen ist.
- **Predefined acceptance criteria:** Protocol, Parameter Ranges, Worst Cases, Sample Rationale und Acceptance Criteria werden vor Durchführung festgelegt; keine post-hoc-Kriterien.
- **IQ/OQ/PQ by purpose:** IQ belegt geeignete Installation/Setup-Basis, OQ charakterisiert kontrollierte Betriebsbereiche/Parameter, PQ belegt reproduzierbare Performance unter vorgesehenen Bedingungen – soweit dieses Modell zum Prozess passt.
- **Risk drives rigor:** Produkt-/Prozess-/Patient-/Compliance-Risiko bestimmt Tiefe, Worst Cases, Wiederholungen, Sampling und Revalidation.
- **Measurement readiness:** ungeeignete Messsysteme oder unklare Methoden dürfen Process Capability/Validation nicht scheinbar bestätigen.
- **Change lineage:** Equipment-, Material-, Software-, Supplier-, Site-, Method- oder Parameter-Changes werden auf Revalidation-/Verification-Impact geprüft.
- **No execution fiction:** ein geplanter Protocol-Schritt ist keine ausgeführte oder bestandene Qualification.

## Workflow

### 1. Process Scope und Validation Need fixieren

Erfasse Process ID/Version, Product/Site/Line/Equipment/Software/Material Scope, Input/Output Requirements, Critical Quality/Performance Characteristics, aktuelle Prozesskontrollen und Fähigkeit zur vollständigen Output-Verifikation.

Entscheide nachvollziehbar `validation-required|verification-sufficient|hybrid-validation-verification|further-characterization-needed|unknown` mit Source/Risk Rationale.

### 2. Risk und Process Knowledge übernehmen

Verknüpfe relevante Hazards, Failure Modes, Risk Controls, Supplier-/Material-Abhängigkeiten, Design-/Transfer-Requirements, historische Deviations/NC/CAPA und bekannte Process Capability. Kein zweites Risk Register.

### 3. Validation Strategy ableiten

Definiere je nach Prozess geeignete Elemente:
- equipment/facility/system prerequisites,
- installation/setup qualification soweit relevant,
- operating ranges, alarms/interlocks und worst-case/edge conditions,
- performance runs unter vorgesehenen Bedingungen,
- lots/shifts/operators/material/suppliers/sites soweit risikorelevant,
- sample-size/rationale,
- measurement-method readiness,
- acceptance criteria und statistical/engineering rationale,
- data integrity / record expectations.

### 4. IQ/OQ/PQ oder alternatives Evidence Pattern

Nutze IQ/OQ/PQ, wenn es den Prozess sinnvoll strukturiert. Wenn ein anderes validierbares Evidence Pattern besser passt, dokumentiere Zweckgleichheit und Rationale statt künstlich drei Phasen zu erzwingen. Für computerisierte Produktions-/QMS-Systeme berücksichtige aktuelle FDA-Computer-Software-Assurance-Prinzipien und trenne CSA von Product-Software-Validation.

### 5. Protocol vor Ausführung kontrollieren

`process-validation-protocol.md` enthält Scope, Responsibilities, Preconditions, Equipment/Material/Software Versions, Tests/Runs, Parameter Ranges, Sampling, Acceptance Criteria, Deviations Handling, Required Records und Approval State. Ein nicht genehmigtes Protocol wird nicht als executed-ready ausgegeben.

### 6. Evidence bewerten

Bewerte Execution Evidence gegen vorab definierte Kriterien. Deviations, OOS/OOT/NC, fehlende Runs, uneindeutige Measurement Evidence oder nicht repräsentative Conditions bleiben sichtbar. Ergebnisstatus mindestens `pass|conditional-with-open-actions|fail|incomplete|not-executed`.

### 7. Revalidation / Change Trigger

Prüfe Änderungen an Equipment, Process Parameters, Software/Automation, Materials/Suppliers, Site/Layout/Utilities, Methods, Product Design/Claims sowie relevante Trends/CAPA/NC auf Revalidation-/Targeted-Verification-Need. Route regulatorisch relevante Produkt-/Designchanges an `design-change-regulatory-impact`.

### 8. Routing

- QMS-/Process-Control-Gap → `medical-device-qms-iso13485`
- Risk Gap → `medical-device-risk-management-iso14971`
- Supplier/Material Gap → `supplier-quality-medical-device`
- Design-/Regulatory Change → `design-change-regulatory-impact`
- CAPA/Systemursache → `medical-device-capa` / `evidence-based-causal-investigation`
- kontrollierte Protocols/Reports/Records → `controlled-quality-documentation`.

## Output-Verträge

`process-validation-strategy.json` enthält Process Scope, Validation-Need Decision, Source/Risk Rationale, Validation Model, Critical Parameters/Outputs, Worst Cases, Measurement Readiness, Sampling Rationale und Revalidation Triggers.

`process-validation-protocol.md` enthält kontrollierbare vorab definierte Execution-/Acceptance-Struktur, ohne Durchführung oder Approval zu simulieren.

`process-validation-assessment.json` enthält Executed Evidence References, Criteria Results, Deviations/Gaps, Coverage/Evidence Status, Overall State, Required Actions und Change/Revalidation Links.

## Memory Path

Persistenzwürdig sind validierte Process-Validation-Heuristiken, wiederverwendbare IQ/OQ/PQ- bzw. alternative Qualification-Muster, robuste Worst-Case-/Sampling-/Revalidation-Patterns und abstrahierte Process-Knowledge-Learnings. Konkrete Process Parameters, Equipment IDs, Produktionsdaten, Supplier Details, offene Deviations/CAPA, aktuelle Acceptance Results und vertrauliche Manufacturing Records bleiben run-only bzw. in kontrollierten Quality/Manufacturing Records. Kandidaten benötigen `sourceRefs`; lifecycle-/technologieabhängige Learnings zusätzlich `asOf`/`reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Validation Need vor der Protokollplanung begründet wird,
- IQ/OQ/PQ zweckgebunden statt dogmatisch angewandt wird,
- Acceptance Criteria vor Execution definiert sind,
- Risk/Worst Case/Sampling/Measurement Readiness nachvollziehbar sind,
- geplante Aktivitäten nicht als ausgeführt oder bestanden dargestellt werden,
- Deviations und offene Evidence Gaps sichtbar bleiben,
- Changes/Revalidation Trigger traceable sind,
- konkrete Manufacturing-/Validation-Zustände nicht in globales dauerhaftes Memory gelangen.
