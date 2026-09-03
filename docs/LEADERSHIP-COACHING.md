# Leadership Coaching in Skillz

Status: candidate architecture, P0 + P1 implemented, 2026-09-03

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

## Core skills (P0)

- `leadership-coaching-intake`: contracting, scope, confidentiality, persistence and initial outcome definition.
- `leadership-development-model`: converts challenges into observable development goals.
- `leadership-reflection`: separates observations, actions, interpretations, alternative explanations and learning hypotheses.
- `leadership-behavior-experiment`: defines small real-world behavior experiments.
- `leadership-coaching-review`: separates adherence, behavior change, outcome and interpretation.
- `coaching-safety-routing`: routes health, HR, Employment Law, Compliance and urgent concerns out of normal coaching when needed.
- `leadership-coaching-workflow`: stateful orchestration of the loop and situational routing.

## Situational leadership workflows (P1)

- `leadership-feedback`: evidence-bound feedback preparation for giving or receiving feedback.
- `leadership-delegation`: outcome, authority, autonomy, resources, checkpoints and escalation contract.
- `leadership-1on1-workflow`: development-oriented recurring 1:1 preparation using confirmed meeting and follow-up context.
- `difficult-conversation-workflow`: fact/interpretation separation, feedback, boundaries and professional routing for difficult conversations.
- `performance-management-workflow`: expectation, evidence, performance gap, competing cause hypotheses, employee perspective, support, commitments and review.

P1 does not introduce a second state machine. Its artifacts can be referenced from `leadership-coaching-state.json` when relevant to the active coaching case.

## Reuse of existing Skillz capabilities

Leadership Coaching does not replace:

- `role-requirements-grilling` / `role-architecture` for normative role definition;
- `round-based-requirements-grilling` for unresolved user/stakeholder decisions;
- `meeting-preparation` for evidence-bound meeting prep;
- `decision-and-follow-up-tracker` for confirmed decisions, commitments and delegated states;
- legal/compliance specialists for formal matters;
- `project-second-brain` for ordinary project memory.

P1 deliberately composes these capabilities. For example, a 1:1 is prepared through `meeting-preparation`, leadership-specific agenda logic is added by `leadership-1on1-workflow`, and only confirmed commitments are written to `decision-and-follow-up-tracker` afterward.

## Grilling boundary

Grilling is used when the coachee must make or clarify a real contracting decision: coaching purpose, scope, desired change, success evidence, sponsor boundaries, confidentiality, persistence and re-contracting.

Reflection, behavior experiments, experiment reviews and situational P1 planning are not Grilling rounds. Their task is analysis, preparation and learning rather than requirements clarification.

The portable example `GithubLarsKomo/grilling/examples/leadership-coaching-intake-v2.json` contains only the first intake round and is marked progressive. Follow-up rounds should be generated from the Grilling v2 round-handoff contract only where unresolved contracting uncertainty remains.

## Privacy model

Default persistence is conservative:

- structured coaching contract: allowed when confirmed;
- development goals: allowed when confirmed;
- behavior experiments and reviews: allowed when confirmed;
- situational P1 artifacts: persist only to the extent necessary for the coaching purpose and allowed by the contract;
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
          +-------------------------+
          |                         |
          v                         v
leadership-reflection.json     situational P1 artifact
          |                    /   |   |   |   \
          v            feedback delegation 1:1 difficult performance
leadership-behavior-experiment.json
          |
          v
leadership-coaching-review.json
          |
          +---- retain / modify / stop

leadership-coaching-state.json references these artifacts without copying their full contents.
```

## Safety and formal-process boundary

Coaching must not become a substitute for crisis support, mental-health care, HR process, Employment Law analysis, Compliance investigation or formal disciplinary decisions. `coaching-safety-routing` owns the cross-cutting gate.

For difficult conversations and performance management, formal triggers such as disciplinary action, warning, termination, harassment, discrimination, works-council/participation issues or investigations must leave the normal coaching path and be routed to the appropriate professional workflow or specialist. Coaching can remain supportive, but it cannot manufacture evidence or authorize the formal action.

## P1 artifact contracts

The P1 schemas are:

- `schemas/leadership-feedback-plan-v1.schema.json`
- `schemas/leadership-delegation-plan-v1.schema.json`
- `schemas/leadership-1on1-plan-v1.schema.json`
- `schemas/difficult-conversation-plan-v1.schema.json`
- `schemas/performance-management-plan-v1.schema.json`

Their regression suite is `tests/test_leadership_coaching_p1_artifact_schemas.py`. The dedicated `Leadership coaching contracts` CI workflow validates P0/P1 schemas, skill metadata and evaluation suites on pull requests and on relevant changes to `main`.

## Next architecture layer (P2)

The next useful layer is senior/team leadership rather than more variants of the same conversation workflows:

- `leadership-conflict-analysis`
- `leadership-team-effectiveness`
- `leadership-stakeholder-map`
- `stakeholder-influence-workflow`
- `change-leadership-workflow`

These should reuse P0/P1 contracts and only be added where they introduce genuinely new analysis logic.
