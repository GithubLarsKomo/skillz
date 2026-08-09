# OpenAI plugin distribution

`skillz` keeps `skills/*` and `.skill-sync.json` as its only authoritative skill source. The OpenAI/Codex plugin bundle is generated, never hand-maintained.

## Build

For an ad-hoc archive build:

```bash
python scripts/build_openai_plugin.py \
  --output build/skillz \
  --archive build/skillz-plugin.tar
```

For the repository-backed Codex marketplace, materialize the committed plugin bundle with:

```bash
python scripts/build_openai_plugin.py --output plugins/skillz
```

The generated bundle contains:

```text
skillz/
├── .codex-plugin/plugin.json
├── skillz-distribution-manifest.json
└── skills/<skill-name>/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── ...portable files...
```

The builder verifies every canonical portable file against `.skill-sync.json`. For `SKILL.md`, it deterministically projects the canonical frontmatter to the OpenAI Agent Skill trigger contract (`name` + `description`) while preserving the instruction body. It also packages `agents/openai.yaml` for every skill so display metadata and invocation policy remain harness-specific rather than becoming a second canonical skill source. The distribution manifest records source and packaged SHA-256 values.

`VERSION` is the canonical plugin version. The committed plugin manifest template must match it.

## Repository marketplace layout

The Git repository is directly consumable as a Codex Git marketplace:

```text
skillz/
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── plugins/
│   └── skillz/
│       ├── .codex-plugin/plugin.json
│       ├── skillz-distribution-manifest.json
│       └── skills/...
├── skills/...                    # canonical sources
└── distribution/openai-plugin/  # plugin manifest template
```

`.agents/plugins/marketplace.json` points to `./plugins/skillz`. This follows the Codex repository/team marketplace convention and deliberately keeps the installable plugin below `plugins/<plugin-name>` rather than at the repository root.

`plugins/skillz/**` is generated output. Never edit it directly; change the canonical source and regenerate the bundle.

## Install the complete marketplace in Codex

In Codex Desktop, add a plugin marketplace from Git with:

```text
Source:      https://github.com/GithubLarsKomo/skillz.git
Git ref:     main
Sparse paths: leave empty
```

Leaving sparse paths empty is the least surprising option. If the installed Codex version supports multiple sparse paths reliably, the minimal repository subset is:

```text
.agents/plugins
plugins/skillz
```

Do not use the old `plugins/codex` sparse path; that path is not the marketplace root and does not contain the required manifest.

After the marketplace is added, install/enable the `skillz` plugin and start a new Codex thread so the packaged skills are rediscovered.

CLI-capable Codex installations can use the equivalent Git-marketplace flow with the repository URL and then install `skillz@skillz`.

## Install one skill only

For one skill, current Codex installations can still use the built-in `$skill-installer` with a GitHub skill-directory URL, for example:

```text
$skill-installer install https://github.com/GithubLarsKomo/skillz/tree/main/skills/large-work-wayfinder
```

Restart Codex or start a new thread after installation so newly installed skills are discovered.

## Discovery versus implicit invocation

These are deliberately separate concerns:

- `userFacing: true` controls whether the skill appears as a deliberate entrypoint in the repository capability index and `/skills` discovery.
- `implicitInvocation` controls whether an OpenAI/Codex harness may select the skill automatically when the skill is packaged.

A skill may therefore be easy to discover while still requiring an explicit user choice, or may remain an internal/model-oriented helper without being promoted as a user-facing entrypoint.

The optional canonical frontmatter field is:

```yaml
implicitInvocation: false
```

During packaging it becomes:

```yaml
policy:
  allow_implicit_invocation: false
```

Use `false` only for workflows where silent automatic execution would be surprising or where an explicit human choice is part of the contract. Do not infer this setting from `userFacing`; discovery and execution policy remain independent.

The generated `agents/openai.yaml` also contains deterministic `interface.display_name` and `interface.short_description` values derived from the canonical skill name and description. These are presentation metadata only.

## ChatGPT versus Codex

OpenAI's plugin platform can combine skills, MCP servers and optional app/UI surfaces. This slice is deliberately **skill-only**: no `.mcp.json` or `.app.json` is declared because no such runtime component exists in this repository.

A valid Codex Git marketplace/plugin bundle is not the same as publication in a hosted ChatGPT app/plugin marketplace. Workspace approval, authentication and any hosted MCP/App surface are separate distribution steps.

## Verification

```bash
python -m unittest tests.test_build_openai_plugin
```

Normal repository CI proves deterministic output, version alignment, OpenAI-compatible packaged frontmatter, generated OpenAI metadata, invocation-policy projection, source-hash enforcement, the repository marketplace contract, and that the committed `plugins/skillz` bundle is current.
