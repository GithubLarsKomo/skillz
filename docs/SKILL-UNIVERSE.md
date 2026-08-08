# Skill Universe

Status: curated architecture view  
Canonical capability source: [`skill-capability-index.json`](skill-capability-index.json)  
Canonical hard-dependency source: [`SKILL-DEPENDENCIES.md`](SKILL-DEPENDENCIES.md)

## Purpose

This document is the human-readable architecture map for the `skillz` repository. It intentionally does **not** reproduce every hard `requires` edge. The generated [`SKILL-DEPENDENCIES.md`](SKILL-DEPENDENCIES.md) remains the exact machine-derived graph; this view highlights responsibilities, lifecycle paths and feedback loops.

Current canonical inventory after the customer-service/complaint follow-up wave: **108 skills, 90 user-facing entrypoints, 108/108 evaluation suites passing, 0 evaluation errors**.

### Reading the diagrams

- **Solid arrows** show primary semantic flow or ownership handoff.
- **Dashed arrows** show temporal/governance feedback that is deliberately not encoded as a hard cyclic dependency.
- **External state** means CI, deployment, authority, notified-body, customer or issue-tracker state that must be verified rather than simulated.
- **Memory paths** carry only governed durable abstractions; concrete repository, customer, complaint, patient, regulatory and current case state remains project/run/controlled-record state.

---

## 1. Skill Universe — domain map

```mermaid
flowchart TB
    USER((User / Goal))

    subgraph ENG[Engineering]
        ENG_ENTRY[iterate-software-projects]
        ENG_SPEC[conversation-to-spec]
        ENG_ISSUES[spec-to-vertical-issues]
        ENG_IMPL[implement-from-issue]
        ENG_REVIEW[two-axis-code-review]
        ENG_DELIVERY[engineering-delivery-followup]
    end

    subgraph SERVICE[Customer Service / Complaint]
        CS_CONTACT[medical-device-customer-contact-intake]
        CS_COMPLAINT[medical-device-complaint-handling]
        CS_FOLLOW[medical-device-complaint-customer-followup]
        CS_ROUTE[medical-device-complaint-regulatory-routing]
        CS_LATE[Later customer / field information]
    end

    subgraph REG[Regulated Engineering]
        REG_CTX[regulated-product-context]
        REG_STRAT[medical-device-regulatory-strategy]
        REG_FDA[fda-complaint-mdr-reportability / FDA stack]
        REG_IVDR[ivdr-pms-vigilance / EU-IVDR stack]
        REG_QMS[QMS / Risk / Design]
        REG_PMS[medical-device-pms-system]
        REG_MR[qms-management-review-governance]
    end

    subgraph KNOW[Research & Knowledge]
        K_RESEARCH[research-to-evidence-note]
        K_TRACE[regulatory-evidence-traceability]
        K_STRUCT[structured-knowledge-artifact]
        K_MAP[knowledge-map-generator]
        K_VIEW[knowledge-view / obsidian-adapter]
    end

    subgraph PROD[Productivity]
        P_INBOX[inbox-action-triage]
        P_REVIEW[daily-and-weekly-review]
        P_FOLLOW[decision-and-follow-up-tracker]
    end

    subgraph MEM[Communication & Memory]
        M_GOV[communication-memory-governance]
        M_SYNC[memory-sync-reconciliation]
    end

    subgraph SYS[Skill System]
        S_FACTORY[composable-skill-factory]
        S_CURATE[central-skill-repository-curation]
        S_CAP[Capability index / resolver / evaluation]
    end

    subgraph FLOW[Workflow / External Verification]
        W_EXT[deferred-external-action-verification]
        W_HUMAN[human-procedure-wizard]
        W_HANDOFF[agent-handoff]
    end

    USER --> ENG_ENTRY
    USER --> REG_STRAT
    USER --> CS_CONTACT
    USER --> P_INBOX

    ENG_SPEC --> ENG_ISSUES --> ENG_IMPL --> ENG_REVIEW --> ENG_DELIVERY
    ENG_DELIVERY -. verified iteration return .-> ENG_ENTRY

    CS_CONTACT --> CS_COMPLAINT
    CS_COMPLAINT --> CS_FOLLOW
    CS_COMPLAINT -->|initial / time-critical| CS_ROUTE
    CS_FOLLOW -->|evidence delta| CS_ROUTE
    CS_ROUTE --> REG_FDA
    CS_ROUTE --> REG_IVDR
    REG_IVDR --> REG_PMS --> REG_MR
    REG_FDA --> REG_PMS
    CS_LATE --> CS_FOLLOW
    REG_FDA -. prior decision reference .-> CS_FOLLOW
    REG_IVDR -. prior decision reference .-> CS_FOLLOW

    K_RESEARCH --> K_TRACE --> REG_CTX --> REG_STRAT
    K_RESEARCH --> K_STRUCT --> K_MAP --> K_VIEW

    P_INBOX --> P_REVIEW --> P_FOLLOW

    ENG_DELIVERY --> W_EXT
    REG_FDA --> W_HUMAN
    REG_IVDR --> W_HUMAN
    ENG_ENTRY --> W_HANDOFF

    ENG_ENTRY -. durable abstractions .-> M_GOV
    CS_COMPLAINT -. durable abstractions only .-> M_GOV
    CS_FOLLOW -. durable patterns only .-> M_GOV
    REG_STRAT -. durable abstractions .-> M_GOV
    K_RESEARCH -. durable source/method patterns .-> M_GOV
    M_GOV --> M_SYNC

    S_FACTORY --> S_CURATE --> S_CAP
```

No single top-level orchestrator owns every domain. Narrow owners compose around shared evidence, verification, delivery, QMS and memory spines.

---

## 2. Engineering lifecycle — closed delivery loop

```mermaid
flowchart LR
    A[conversation-to-spec]
    B[spec-to-vertical-issues]
    C[test-driven-vertical-slice]
    D[implement-from-issue]
    E[two-axis-code-review]
    F[engineering-delivery-followup]
    G[iterate-software-projects]
    EXT[deferred-external-action-verification]

    A --> B --> C --> D --> E --> F
    F -. engineering-iteration-return-input.json .-> G
    G --> B
    F --> EXT

    R1{{review-approved ≠ merge-ready}}
    R2{{merged ≠ deployed}}
    R3{{tracker done ≠ requirement verified}}
    R4{{head changed → review stale}}

    E -.-> R1
    F -.-> R2
    F -.-> R3
    E -.-> R4
```

Engineering state remains explicit:

`implemented → review-approved → merge-ready → merged → deployed/released when applicable → issue-closed → requirement-verified`

A later state is never inferred solely from an earlier one.

---

## 3. Customer contact → complaint → follow-up → vigilance → reassessment

```mermaid
flowchart LR
    CONTACT[medical-device-customer-contact-intake]
    COMPLAINT[medical-device-complaint-handling]
    CFOLLOW[medical-device-complaint-customer-followup]
    ROUTE[medical-device-complaint-regulatory-routing]
    FDA[fda-complaint-mdr-reportability]
    IVDR[ivdr-pms-vigilance]
    PMS[medical-device-pms-system]
    RISK[medical-device-risk-management-iso14971]
    CAPA[medical-device-capa]
    MR[qms-management-review-governance]
    LATE[Later customer / distributor / field information]

    CONTACT -->|complaint-intake-handoff.json| COMPLAINT
    COMPLAINT -->|missing facts / follow-up need| CFOLLOW
    COMPLAINT -->|initial or time-critical handoff| ROUTE
    CFOLLOW -->|customer-followup-evidence.json| ROUTE
    ROUTE -->|US assessment| FDA
    ROUTE -->|EU-IVDR assessment| IVDR

    COMPLAINT --> RISK
    COMPLAINT --> CAPA
    FDA --> PMS
    IVDR --> PMS
    PMS --> MR

    FDA -. investigation remains open .-> COMPLAINT
    IVDR -. investigation remains open .-> COMPLAINT

    FDA -. prior decision snapshot .-> CFOLLOW
    IVDR -. prior decision snapshot .-> CFOLLOW
    LATE --> CFOLLOW
    CFOLLOW -. new material evidence .-> COMPLAINT
    CFOLLOW -->|reassessment delta| ROUTE

    S1{{customer resolved ≠ complaint closed}}
    S2{{complaint closed ≠ regulatory closed}}
    S3{{awareness evidence ≠ legal awareness conclusion}}
    S4{{known issue / user error / no return ≠ non-reportable}}
    S5{{prior not-reportable ≠ permanent immunity}}
    S6{{no response ≠ no event}}
    S7{{follow-up must not delay time-critical vigilance}}
    S8{{preserve evidence before destructive support}}

    CONTACT -.-> S1
    COMPLAINT -.-> S2
    ROUTE -.-> S3
    ROUTE -.-> S4
    ROUTE -.-> S5
    CFOLLOW -.-> S6
    CFOLLOW -.-> S7
    CFOLLOW -.-> S8
```

### Ownership boundaries

- `medical-device-customer-contact-intake` owns source-preserving intake for first and unsolicited follow-up contacts and the earliest possible Complaint/Safety handoff. It does not investigate or decide reportability.
- `medical-device-complaint-handling` owns the individual complaint QMS record, investigation decision, evidence preservation, versioned supplemental evidence, reopen state and complaint-closure readiness. It does not decide FDA MDR or EU vigilance.
- `medical-device-complaint-customer-followup` owns controlled, criteria-based customer evidence acquisition after complaint opening: neutral questions, contact-attempt evidence, data minimization, support/return evidence preservation and the versioned evidence delta. It does not own investigation or reportability.
- `medical-device-complaint-regulatory-routing` owns jurisdiction/role routing, awareness-evidence chronology, follow-up-delta consumption and jurisdiction-specific reassessment triggers. It does not convert evidence into a legal awareness date or final reportability decision.
- `fda-complaint-mdr-reportability` owns FDA-specific awareness, MDR criteria, timing and versioned reassessment when material evidence changes.
- `ivdr-pms-vigilance` owns IVDR-specific vigilance/serious-incident assessment, versioned reassessment and PMS feedback; non-complaint PMS/trend/literature/field signals remain valid inputs.

### Hard customer-service invariants

1. Customer wording does not determine whether a possible complaint exists.
2. Troubleshooting, refund, replacement or a solved service ticket never erase the Quality path.
3. Potential safety information is escalated before final root cause, returned-device analysis, customer follow-up completion or complaint closure.
4. Every complaint keeps an individual record; a prior investigation may be referenced only with documented applicability.
5. Follow-up questions require a documented information gap/purpose and are not selected by customer commercial value.
6. `no-response`, `unable-to-contact` and `declined` are missing-information states, never evidence of no injury/no malfunction/non-reportability.
7. Potentially relevant returned devices, samples, logs and raw evidence are protected before reset, repair, update, cleaning, disposal or other destructive handling.
8. One complaint can require multiple independent jurisdiction assessments.
9. Customer/distributor/employee/QA/regulatory/follow-up timestamps remain separate evidence facts; the market specialist owns the legal awareness conclusion.
10. External customer or authority communication is not `sent|delivered|received|accepted` without external evidence.
11. Complaint closure and prior `not-reportable` decisions remain historical evidence, not immunity against later facts.
12. Reassessment is versioned per jurisdiction; US and EU decisions remain independent.
13. New material follow-up information is appended as an evidence delta; prior complaint/regulatory decisions are not overwritten.
14. New time-critical information bypasses customer follow-up, previous service resolution, complaint closure and management-review cadence.

---

## 4. Regulated Engineering — lifecycle universe

```mermaid
flowchart TB
    subgraph FOUNDATION[Foundations]
        CTX[regulated-product-context]
        RES[research-to-evidence-note]
        TRACE[regulatory-evidence-traceability]
        QMS[medical-device-qms-iso13485]
        RISK[medical-device-risk-management-iso14971]
        DESIGN[design-control-traceability]
    end

    subgraph MARKET[Market access]
        STRAT[medical-device-regulatory-strategy]
        EU[EU / IVDR capabilities]
        US[FDA capabilities]
    end

    subgraph POST[Postmarket]
        CONTACT[Customer contact]
        COMPLAINT[Complaint handling / reopen]
        CFOLLOW[Customer follow-up evidence]
        ROUTE[Regulatory routing / reassessment]
        FDA_MDR[FDA MDR / reassessment]
        EU_VIG[IVDR vigilance / reassessment]
        PMS[PMS system]
        CAPA[CAPA]
        PERF[Performance / PMPF]
        CHANGE[Change impact]
    end

    subgraph GOV[Governance]
        MR[Management Review]
        MRF[Management Review action follow-up]
        AUDIT[ISO 13485 / MDSAP / FDA inspection]
        MON[Regulatory change monitoring]
        ORCH[Regulatory change impact orchestrator]
    end

    RES --> TRACE --> CTX
    CTX --> STRAT --> EU
    STRAT --> US
    CTX --> QMS --> DESIGN
    CTX --> RISK

    CONTACT --> COMPLAINT
    COMPLAINT --> CFOLLOW --> ROUTE
    COMPLAINT -->|time-critical| ROUTE
    ROUTE --> FDA_MDR
    ROUTE --> EU_VIG
    FDA_MDR --> PMS
    EU_VIG --> PMS
    COMPLAINT --> CAPA
    COMPLAINT --> RISK
    PMS --> PERF
    PMS --> CAPA
    PMS --> RISK
    RISK --> CHANGE

    FDA_MDR -. new material evidence .-> CFOLLOW
    EU_VIG -. new material evidence .-> CFOLLOW

    PMS --> MR --> MRF
    MRF -. management-review-return-input.json .-> MR
    QMS --> AUDIT
    MON --> ORCH --> CHANGE
    ORCH --> PMS
    ORCH --> PERF
```

The key regulated-engineering loops remain separate but connected:

1. **Customer/Complaint:** contact → complaint → criteria-based customer follow-up where needed → jurisdiction routing → market-specific vigilance/reportability → later evidence → versioned reassessment.
2. **Postmarket:** complaints/vigilance/field signals → PMS → Risk/CAPA/Performance.
3. **Management governance:** PMS → Management Review → Action Follow-up → next Management Review.
4. **Regulatory intelligence:** source change → change monitoring → impact orchestration → specialist lifecycle update.

Time-critical reportability, vigilance, reassessment or field action never waits for customer follow-up, device return, complaint closure or a periodic management-review cadence.

---

## 5. Evidence, knowledge and memory spine

```mermaid
flowchart LR
    SOURCE[Authoritative / project / controlled sources]
    RESEARCH[research-to-evidence-note]
    TRACE[regulatory-evidence-traceability]
    STRUCT[structured-knowledge-artifact]
    MAP[knowledge-map-generator]
    VIEW[knowledge-view / obsidian-adapter]

    SKILLS[Engineering / Customer Service / Regulated Engineering]
    MEM[communication-memory-governance]
    SYNC[memory-sync-reconciliation]

    SOURCE --> RESEARCH --> TRACE
    RESEARCH --> STRUCT --> MAP --> VIEW
    SKILLS -. memory-candidate-handoff-v1 .-> MEM --> SYNC

    RULE{{Concrete customer, complaint, patient, awareness, regulatory, repository and secret state is not global Memory}}
    MEM -. enforces .-> RULE
```

Knowledge and Memory remain different concerns:

- Knowledge artifacts preserve explicit source/provenance relationships.
- Memory governance decides whether an abstracted learning is durable and safe enough to persist.
- Current contacts, complaints, patients/reporters, device/lot IDs, original customer responses, awareness dates, reportability decisions, submissions, findings, SHAs, CI state and credentials remain outside global Memory.

---

## 6. Closed-loop architecture at a glance

```mermaid
flowchart TB
    subgraph ELOOP[Engineering]
        E1[Spec / Issue] --> E2[Implement] --> E3[Review] --> E4[CI / Merge / Delivery] --> E5[Verified iteration state]
        E5 -. next increment .-> E1
    end

    subgraph CLOOP[Customer / Complaint]
        C1[Customer / Distributor / Field contact] --> C2[Complaint intake & investigation]
        C2 --> C2F[Criteria-based customer follow-up]
        C2 -->|time-critical| C3[Regulatory routing]
        C2F --> C3 --> C4[FDA MDR / IVDR vigilance]
        C4 -. prior decision snapshot .-> C5[Later material information]
        C5 --> C2F
    end

    subgraph PLOOP[Postmarket]
        P1[PMS aggregation] --> P2[Risk / CAPA / Performance] --> P3[Management attention]
        P2 -. updated state .-> P1
    end

    subgraph MLOOP[Management Review]
        M1[Management Review] --> M2[Confirmed actions] --> M3[Specialist implementation] --> M4[Effectiveness / external closure] --> M5[Return input]
        M5 -. next review .-> M1
    end

    subgraph RLOOP[Regulatory intelligence]
        R1[Source monitoring] --> R2[Verified change event] --> R3[Impact orchestration] --> R4[Specialist lifecycle updates]
        R4 -. new baseline .-> R1
    end

    C4 --> P1
    P3 --> M1
    R4 --> P1
    R4 --> E1
    E5 --> P1
```

---

## Canonical vs curated views

Use this document for **“How does the whole skill system fit together?”**

Use [`SKILL-DEPENDENCIES.md`](SKILL-DEPENDENCIES.md) for **exact hard `requires` and inferred output-consumer edges**.

Use [`skill-capability-index.json`](skill-capability-index.json) for the canonical machine-readable inventory and evaluation state.

The Universe remains curated and semantically stable. Individual workers belong here only when they introduce a new architectural responsibility, lifecycle boundary or feedback loop; ordinary workers stay visible in the generated dependency graph.
