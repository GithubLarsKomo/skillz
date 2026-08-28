# Skillz Architecture P3 — Discoverability Refinement

Date: 2026-08-28

## Scope

This P3 tranche refines the visible user-facing surface without changing skill lifecycle, domain logic, output ownership, or routing semantics.

The governing distinction is:

- `public`: normal user-facing entrypoint for standard discovery;
- `advanced`: user-facing, but intentionally targeted or specialist-facing rather than part of the default surface;
- `internal`: composition-only;
- `compatibility`: deprecated explicit-use-only surface.

`implicitInvocation: false` is **not** sufficient by itself to classify a skill as `advanced`. Discoverability is an explicit governance decision based on how the skill should appear in user-facing selection and discovery.

## Contract default vs specialist surfaces

`contract-workflow` remains the preferred normal contract entrypoint and therefore stays `public`.

The following explicit contract specialist surfaces are now `advanced`:

1. `contract-matter-workflow`
2. `agreement-type-analysis`
3. `contract-review`
4. `contract-drafting`
5. `contract-legal-context`
6. `legal-negotiation-strategy`
7. `legal-redline-review-loop`

These skills remain user-facing and directly selectable. They are not deprecated and are not converted into internal workers. The change only prevents them from competing with `contract-workflow` as normal default discovery choices.

## Non-mechanical classification guard

`thought-to-concept-flow` intentionally remains `public` even though it has `implicitInvocation: false`.

This is a regression example demonstrating that explicit invocation and discoverability are separate axes:

- `implicitInvocation` controls automatic routing behavior;
- `discoverability` controls how prominently a user-facing skill should appear in discovery surfaces.

## Regression changes

The P2 and P3 architecture tests previously contained a historical lower bound on the absolute number of `public` skills. That encoded a transient inventory state as if it were an architectural invariant and would incorrectly fail valid `public -> advanced` refinements.

Those assertions were replaced with stable partition invariants:

- `public + advanced == user-facing entrypointCount`;
- `internal + compatibility == skillCount - entrypointCount`;
- all discoverability counts sum to `skillCount`.

A dedicated test, `tests/test_architecture_consolidation_p3_discoverability.py`, additionally verifies:

- `contract-workflow` stays public/default;
- the seven selected contract specialist surfaces are advanced and evaluated;
- no lifecycle/deprecation change is introduced;
- `advanced` is not mechanically inferred from `implicitInvocation: false`.

The test is permanently included in `.github/workflows/validate-skills.yml`.

## Final capability distribution

After materialization:

- Skills: **281**
- User-facing entrypoints: **231**
- Public: **222**
- Advanced: **9**
- Internal: **48**
- Compatibility: **2**
- Evaluation coverage: **281/281**
- Executed evaluation suites: **PASS**
- Ambiguous outputs: **0**
- Outputs without inferred hard-requires consumers: **274**

The number of user-facing capabilities is unchanged. Seven entrypoints moved from normal discovery to targeted advanced discovery.

## Validation evidence

The feature materialization run passed:

- dependency graph contracts;
- metadata schemas;
- role-selection schemas and routing;
- P2 architecture regression;
- P3 architecture regression;
- new P3 discoverability regression;
- OpenAI plugin build;
- agent and repository metadata reproducibility;
- Obsidian universe generation;
- repository contract validation;
- all **281** skill evaluation suites.

The temporary feature-branch metadata-sync extension was removed after materialization; the canonical `main` sync workflow is restored unchanged.

## Deferred review

Future discoverability changes should use the same evidence standard. Do not mass-classify all `implicitInvocation: false` skills as advanced. Review coherent capability families and retain `public` whenever a skill is itself a normal direct user intent rather than an expert alternative behind a preferred facade.
