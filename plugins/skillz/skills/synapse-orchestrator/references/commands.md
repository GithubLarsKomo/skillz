# Command semantics

Use these commands as conversational conventions. Do not claim they are native application commands unless the current interface explicitly exposes them.

## `/start`

Identify the user's desired outcome and the most important missing constraint. If the request is already actionable, summarize the understood goal in one sentence and begin.

## `/save`

Return a compact handoff containing:

1. SMART goal,
2. completed work and evidence,
3. decisions and assumptions,
4. unresolved risks or blockers,
5. exact recommended next action.

Create or update a persistent artifact only when the user asks for one or the active workflow already requires it.

## `/reason`

Analyze the decision with:

- relevant facts and source quality,
- assumptions and uncertainties,
- viable options,
- trade-offs and failure modes,
- recommendation and why it wins under the stated priorities.

Use transparent analytical perspectives unless independent subagents are explicitly requested or otherwise authorized.

## `/settings`

Update the active goal, constraints, preferred mode, or completion criteria. Restate only what changed and its practical consequence.

## `/new`

Treat the next request as a new task and avoid carrying over irrelevant working assumptions. Do not claim to erase platform history, saved memory, files, or external records. If deletion is requested, clarify the exact target and use the appropriate supported operation.

## `/grill-me`

Use an available requirements-grilling skill when present. Otherwise gather requirements in focused rounds:

1. establish the decision or product boundary,
2. ask only questions that can change architecture or acceptance criteria,
3. preserve earlier decisions,
4. expose contradictions,
5. finish with an approved specification or a clearly scoped next round.

Do not generate a final specification while material decisions remain unresolved.

## `/learn-skill`

Use the skill-creator workflow to convert a completed, repeatable process into a reusable skill:

1. identify observed triggers and concrete examples,
2. separate effective patterns from accidental details,
3. capture anti-patterns and safety boundaries,
4. include scripts or references only when they reduce repeated work,
5. initialize, validate, forward-test when appropriate, and save the skill,
6. update an external repository only when the user explicitly includes it in scope.

Do not copy third-party implementation text or code unless its license permits reuse.
