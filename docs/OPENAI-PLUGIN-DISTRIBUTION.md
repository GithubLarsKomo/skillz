# OpenAI plugin distribution

`skillz` keeps `skills/*` and `.skill-sync.json` as its only authoritative skill source. The OpenAI plugin bundle is generated, never hand-maintained.

## Build

```bash
python scripts/build_openai_plugin.py \
  --output build/skillz \
  --archive build/skillz-plugin.tar
```

The generated bundle contains:

```text
skillz/
├── .codex-plugin/plugin.json
├── skillz-distribution-manifest.json
└── skills/<skill-name>/...
```

The builder verifies every canonical portable file against `.skill-sync.json`. For `SKILL.md`, it deterministically projects the canonical frontmatter to the OpenAI Agent Skill trigger contract (`name` + `description`) while preserving the instruction body. The distribution manifest records both source and packaged SHA-256 values.

`VERSION` is the canonical plugin version. The committed plugin manifest template must match it.

## Local skill installation in Codex

For one skill, current Codex installations can use the built-in `$skill-installer` with a GitHub skill-directory URL, for example:

```text
$skill-installer install https://github.com/GithubLarsKomo/skillz/tree/main/skills/large-work-wayfinder
```

Restart Codex after installation so newly installed skills are discovered.

For the complete bundle, build the plugin and install/enable the generated `skillz/` directory through the Codex plugin/local-marketplace mechanism supported by the installed Codex client. The plugin root is the directory containing `.codex-plugin/plugin.json`; its manifest exposes `./skills/`.

## ChatGPT versus Codex

OpenAI's plugin platform can combine skills, MCP servers and optional app/UI surfaces. This slice is deliberately **skill-only**: no `.mcp.json` or `.app.json` is declared because no such runtime component exists in this repository.

A valid local/plugin skill bundle is not the same as publication in the ChatGPT app/plugin marketplace. Marketplace/app publication, workspace approval, authentication and any hosted MCP/App surface are separate distribution steps and are not fabricated by this builder.

In a ChatGPT environment that supports installing the resulting plugin package, the same generated skill bundle can be used. In environments that do not expose arbitrary user plugin installation, the repository can still be consumed through GitHub or individual Agent Skill installation in Codex.

## Verification

```bash
python -m unittest tests.test_build_openai_plugin
```

Normal repository CI also builds the distribution twice and proves deterministic output, version alignment, OpenAI-compatible packaged frontmatter and source-hash enforcement.
