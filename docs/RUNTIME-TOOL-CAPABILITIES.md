# Runtime Tool Capabilities

`config/tool-capabilities.json` and `scripts/probe_toolchain.py` form a shared, read-only capability layer for engineering skills.

## Boundary

The layer answers only: **which local tool capabilities are currently available?**

It does not:

- select which skill should run,
- decide which capability a task requires,
- install or upgrade tools,
- execute engineering actions beyond bounded version inspection,
- replace the repository capability index or `synapse-orchestrator`.

Skill routing remains based on skill metadata and task intent. A consuming skill decides which capability is materially required for its current step and expresses that explicitly with `--require`.

## Registry

The registry separates abstract capabilities from local providers. For example, `version-control` can be implemented by `git`, while `container-runtime` can be implemented by `docker` or `podman`.

Profiles are **probe scopes**, not requirement sets. They reduce noise by selecting capabilities relevant to a workflow. A missing capability inside a profile is informational until the caller also marks it with `--require`.

Current profiles:

- `opaque-system-analysis`: static inspection, observation, capture, tracing, and structured-text capabilities.
- `disciplined-diagnosis`: repository, process, HTTP, tracing, container, and structured-data capabilities.
- `merge-conflict-resolution`: version-control capability.
- `repository-engineering`: common repository/runtime capabilities for deterministic helpers and local engineering work.

## Usage

Probe the full registry:

```bash
python scripts/probe_toolchain.py
```

Probe only a skill-relevant profile:

```bash
python scripts/probe_toolchain.py --profile disciplined-diagnosis
```

Require a capability only when the current engineering step genuinely depends on it:

```bash
python scripts/probe_toolchain.py \
  --profile merge-conflict-resolution \
  --require version-control
```

Persist a runtime snapshot without committing it:

```bash
python scripts/probe_toolchain.py \
  --profile opaque-system-analysis \
  --output .skillz/toolchain.json
```

List known capabilities and profiles without probing providers:

```bash
python scripts/probe_toolchain.py --list-capabilities
```

## Exit codes

- `0`: all explicitly required capabilities are available.
- `1`: at least one known, selected, explicitly required capability is unavailable.
- `2`: the request is invalid, for example an unknown profile/capability or a required capability outside the selected profile.

## Consumption rule

A skill should use this layer only when local tool availability can materially change the next safe action. It should not probe capabilities merely because they exist in a profile. Missing optional capabilities remain observations; missing required capabilities become explicit blockers or trigger an alternate evidence path.
