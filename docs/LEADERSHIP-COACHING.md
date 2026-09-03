# Leadership Coaching in Skillz

Status: candidate architecture, 2026-09-03

## Goal

The Leadership Coaching domain turns real leadership situations into a longitudinal learning loop without duplicating existing role, meeting, decision, follow-up, legal or Grilling capabilities.

Canonical entry point: `leadership-coaching-workflow`.

## Core loop

```text
contract
  -> development goal
  -> real situation
  -> reflection
  -> behavior experiment
  -> real situation
  -> review
  -> retain / modify / stop
```

The loop intentionally focuses on observable leadership behavior rather than personality classification.

## Core skills

- `leadership-coaching-intake`: contracting, scope, confidentiality, persistence and initial outcome definition.
- `leadership-development-model`: converts challenges into observable development goals.
- `leadership-reflection`: separates observations, actions, interpretations, alternative explanations and learning hypotheses.
- `leadership-behavior-experiment`: defines small real-world behavior experiments.
- `leadership-coaching-review`: separates adherence, behavior change, outcome and interpretation.
- `coaching-safety-routing`: routes health, HR, Employment Law, Compliance and urgent concerns out of normal coaching when needed.
- `leadership-coaching-workflow`: stateful orchestration of the loop.

## Reuse of existing Skillz capabilities

Leadership Coaching does not replace:

- `role-requirements-grilling` / `role-architecture` for normative role definition;
- `round-based-requirements-grilling` for unresolved user/stakeholder decisions;
- `meeting-preparation` for evidence-bound meeting prep;
- `decision-and-follow-up-tracker` for confirmed decisions, commitments and delegated states;
- legal/compliance specialists for formal matters;
- `project-second-brain` for ordinary project memory.

## Grilling boundary

Grilling is used when the coachee must make or clarify a real contracting decision: coaching purpose, scope, desired change, success evidence, sponsor boundaries, confidentiality, persistence and re-contracting.

Reflection, behavior experiments and experiment reviews are not Grilling rounds. They are coaching workers because their task is analysis and learning rather than requirements clarification.

The portable example `GithubLarsKomo/grilling/examples/leadership-coaching-intake-v2.json` contains only the first intake round and is marked progressive. Follow-up rounds should be generated from the Grilling v2 round-handoff contract only where unresolved contracting uncertainty remains.

## Privacy model

Default persistence is conservative:

- structured coaching contract: allowed when confirmed;
- development goals: allowed when confirmed;
- behavior experiments and reviews: allowed when confirmed;
- raw reflections: session-only unless explicitly enabled;
- raw conversation: session-only;
- unnecessary third-party personal data: do not persist;
- sensitive employee/health/investigation information: minimize and route to appropriate professional systems rather than copying into coaching state.

`project-second-brain` is therefore disabled by default for coaching material. Explicit consent and a suitable private memory target are required before persistent project-memory use.

## Artifact spine

```text
leadership-coaching-contract.json
          |
          v
leadership-development-model.json
          |
          +--------------------+
          |                    |
          v                    v
leadership-reflection.json     |
          |                    |
          v                    |
leadership-behavior-experiment.json
          |
          v
leadership-coaching-review.json
          |
          +---- retain / modify / stop

leadership-coaching-state.json references these artifacts without copying their full contents.
```

## Safety boundary

Coaching must not become a substitute for crisis support, mental-health care, HR process, Employment Law analysis, Compliance investigation or formal disciplinary decisions. `coaching-safety-routing` owns this gate.

## Planned P1 extension

The core is designed to support the next layer without changing the state model:

- `leadership-feedback`
- `leadership-delegation`
- `leadership-1on1-workflow`
- `difficult-conversation-workflow`
- `performance-management-workflow`

These should compose the P0 workers and existing Skillz productivity/legal capabilities rather than introduce a second coaching state machine.
