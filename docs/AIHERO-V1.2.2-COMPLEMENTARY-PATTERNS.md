# Matt Pocock / AI Hero v1.2.2 — complementary patterns for `skillz`

This note records the comparison of `mattpocock/skills` **v1.2.2** and the AI Hero skill documentation with the current `GithubLarsKomo/skillz` architecture. The source repository is MIT-licensed; this document adopts concepts in independent wording rather than copying skill bodies.

Primary references:

- https://github.com/mattpocock/skills/tree/v1.2.2
- https://www.aihero.dev/skills
- https://github.com/mattpocock/skills/blob/v1.2.2/CHANGELOG.md

## Executive conclusion

Do **not** mirror the external catalog. `skillz` already has stronger capability metadata, dependency/output contracts, evaluation evidence, regulated-engineering coverage, memory/communication governance, provider-neutral knowledge tooling, and deterministic repository metadata. Most of the external engineering spine already has a direct or stronger analogue here.

The useful additions are therefore cross-cutting operating rules rather than duplicate skills:

1. clearer routing ergonomics without creating a second capability router,
2. explicit separation of discovery from model-implicit invocation,
3. cheaper and clearer phase-boundary choices before creating a handoff,
4. stronger writing rules for documents consumed by agents,
5. dedicated skills for human-only procedures and external stakeholder questionnaires,
6. preserving useful prototype evidence without promoting prototype code to production.

## Existing overlap — do not duplicate

The following external concepts already have a natural home in `skillz`:

| External concept | Existing `skillz` capability |
|---|---|
| wayfinder | `large-work-wayfinder` |
| to-spec | `conversation-to-spec` |
| to-tickets | `spec-to-vertical-issues` |
| implement / TDD | `implement-from-issue`, `test-driven-vertical-slice` |
| diagnosing bugs | `disciplined-diagnosis` |
| code review | `two-axis-code-review` |
| domain modeling | `domain-model-maintenance` |
| codebase deepening | `architecture-deepening-review` |
| handoff | `agent-handoff` |
| prototype | `throwaway-prototype` |
| writing skills | `composable-skill-factory` plus repository metadata validation |

Creating aliases for these names would raise cognitive load, split evaluation evidence, and create routing ambiguity without adding capability.

## 1. Router ergonomics without another router

AI Hero's `ask-matt` is valuable because humans forget which workflow fits. `skillz` already has a richer routing stack, so adding a new name-based scorer to `query_capabilities.py` would weaken rather than improve the architecture.

Keep the existing layers explicit:

- `query_capabilities.py` — deterministic inventory and exact metadata lookup; no natural-language routing.
- `resolve_capabilities.py` — deterministic intersection of explicit capability constraints; no semantic interpretation.
- `run_model_capability_pipeline.py` — natural-language interpretation through a qualified provider, review/admission, then deterministic resolution.
- conversational `/skills` orientation — a human-facing discovery surface over the current capability index, not a new canonical router.

The complementary lesson from `ask-matt` is therefore **orientation quality**, not another routing implementation. A conversational assistant may recommend the most relevant current entrypoint, explain why it fits and mention likely adjacent skills, but it should read the capability index first and keep the recommendation advisory until execution is requested.

### Routing rule

A router should orient, not work. Once an entrypoint is chosen, hand control to that skill. Never let a router silently accumulate specialist logic or become a second catalog.

## 2. Discovery and implicit invocation are different axes

AI Hero v1.2.x adds OpenAI/Codex metadata beside each skill so a user-invoked orchestrator can remain explicitly invoked while model-oriented helpers stay discoverable to the model.

`skillz` previously packaged only the portable `name` and `description`. The OpenAI builder now emits a generated `agents/openai.yaml` for every packaged skill and supports this optional canonical field:

```yaml
implicitInvocation: false
```

It projects to:

```yaml
policy:
  allow_implicit_invocation: false
```

Important distinction:

- `userFacing` answers **should this appear as a deliberate entrypoint?**
- `implicitInvocation` answers **may this harness choose it automatically?**

Do not derive one from the other. A specialist can be user-facing and still legitimately model-invokable; a commitment-forming or surprising orchestrator may be user-facing but require explicit invocation.

## 3. Phase boundaries: use the cheapest safe transition

The external v1.2.2 router sharpened an important point: a handoff is not the default response to context pressure.

Use this order at a phase boundary:

1. **Continue** — same session, primary context still present, next phase is directly related.
2. **Delegate/subagent** — a bounded side question can return evidence without replacing the main context.
3. **Compact in place** — same harness/workspace continues but context pressure is material.
4. **Handoff** — state must travel to a different session, harness, workspace, repository context, person, or independently resumed branch.

`agent-handoff` remains the stronger portable artifact when portability is actually needed. The rule prevents paying its structural cost when nothing has to travel.

## 4. Writing for agents: treat pointers and instructions as executable interfaces

The most reusable idea in AI Hero v1.2.2 is that an agent-facing document is not merely prose for a human reader; it is part of an execution interface.

Apply these rules when editing `SKILL.md`, `AGENTS.md`, system-prompt snippets, or documents reached by them.

### Context pointers

A pointer must answer both:

- what resource exists,
- under which distinct conditions the agent should load it.

Weak pointer wording is a routing defect even when the target document is excellent. Prefer one concrete trigger per genuine branch instead of synonym lists.

### Context load versus cognitive load

Every always-loaded instruction spends model context. Every separate user-visible entrypoint spends human navigation effort. Neither should be minimized blindly.

- Inline rules required on nearly every execution.
- Disclose branch-specific reference material behind a precise pointer.
- Keep meaningful user choices visible rather than automating them away merely to reduce cognitive load.

### Environment as source of truth

Do not copy cheap-to-query facts into agent docs. Package scripts, configuration files, directory layout, schemas, and command `--help` output are already authoritative.

Document what the environment cannot reveal cheaply:

- reasons behind a choice,
- stable conventions,
- safety boundaries,
- known traps,
- decision criteria.

A prose copy of readily queryable configuration is a cache that can go stale.

### Completion criteria

Each workflow step should end in an observable condition. Prefer criteria such as:

- every modified interface is accounted for,
- the failing case is reproduced by a test before the fix,
- all declared outputs exist and validate against their schema,
- the target branch and immutable head SHA are verified.

Avoid vague completion states such as “understood”, “cleaned up”, or “looks good”.

### Positive steering

State the target behavior directly. Use prohibitions only for genuine guardrails, and pair them with the desired alternative. Repeated negative examples can accidentally prime the behavior they are meant to suppress.

## 5. Human-only procedure pattern → `human-procedure-wizard`

AI Hero's `wizard` addresses a real gap: some engineering work is blocked by steps an agent cannot perform safely or at all — dashboard clicks, approvals, credential reveal, physical confirmation, or irreversible cutover gates.

This pattern is now implemented as `human-procedure-wizard`. The dedicated skill owns the transition from an identified human-only execution boundary back to a verifiable agent workflow. Its core rules are:

1. Inspect the repository and authoritative vendor documentation before asking the human.
2. Separate agent-executable work from genuinely human-only work.
3. Present the ordered human stages and captured values before generating automation.
4. Mark each value as secret/public and its destination (`.env`, secret store, nowhere).
5. Open or link the exact authoritative location before asking for a value.
6. Require confirmation immediately before irreversible actions.
7. Keep secrets out of logs, generated Markdown, and command history.
8. Verify the resulting state independently when possible; do not claim interactive browser work was completed without evidence.
9. Return a machine-readable verification/result contract to the original workflow.

The skill deliberately does not replace domain decisions, diagnosis, requirements elicitation, or `agent-handoff`.

## 6. External questionnaire pattern → `external-stakeholder-questionnaire`

A second useful gap is a decision that the current user cannot answer because another stakeholder holds the knowledge.

This pattern is now implemented as `external-stakeholder-questionnaire`. It is used when the current user has already established that the missing fact or decision belongs to another knowledge holder. The dedicated skill:

- identifies the confirmed recipient or role and known authority,
- asks one information or decision gap per question,
- puts the highest-value and blocking questions first,
- allows explicit `unknown` and partial answers,
- avoids leading or incomplete answer options,
- never invents a deadline,
- records how each answer will be used downstream.

It remains complementary to `meeting-preparation` and `decision-and-follow-up-tracker`: the questionnaire acquires missing stakeholder evidence; those skills prepare meetings or track the resulting commitments and open loops. It also remains distinct from `round-based-requirements-grilling`, which elicites structured requirements from the current user rather than routing a known knowledge gap to an external holder.

## 7. Prototype evidence: throw away code, not learning

`throwaway-prototype` correctly prevents experimental code from silently becoming production code. AI Hero v1.2.2 adds a useful nuance: the runnable prototype can remain findable as primary evidence even when it never belongs on the production branch.

Recommended refinement when the prototype is useful to reviewers or non-developers:

- prefer a self-contained artifact when feasible, especially a single HTML file for state/interaction exploration,
- keep the experiment isolated from the production branch,
- retain the artifact on an explicitly experimental branch or archive when future replay has value,
- record the validated decision in the durable issue/ADR/spec,
- never treat prototype behavior as production acceptance evidence without a separate implementation and review.

The disposal state therefore has three legitimate outcomes: deleted, archived evidence, or explicitly authorized conversion into a new implementation task.

## 8. Adoption policy for external skill systems

When reviewing another skill repository:

1. Compare **capabilities**, not names.
2. Prefer strengthening an existing skill, schema, distribution adapter, or documented boundary over adding an alias.
3. Preserve deliberate boundaries between deterministic query, exact resolution, and probabilistic interpretation.
4. Add a new skill only when the `composable-skill-factory` boundary test passes.
5. Keep harness-specific metadata generated from canonical portable sources.
6. Preserve provenance and license notes for substantial borrowed ideas.
7. Add tests around new behavior before promoting it as a stable entrypoint.

This keeps `skillz` smaller at the user-facing surface while increasing what the system can reliably do.
