# Impeccable Provenance

## Sources

This skill family is an independent adaptation inspired by:

- `pbakaus/impeccable` — current canonical upstream examined on 2026-08-20.
- `DevvGwardo/impeccable` — Hermes Agent port examined as an integration reference.

Both trace the frontend-design methodology around project context, brand/product registers, shaping before implementation, design critique, visual hierarchy, typography, color, layout, interaction, responsive design, accessibility and anti-pattern detection.

## License

`pbakaus/impeccable` and the referenced Hermes port identify Impeccable as Apache License 2.0 work. This repository does not copy the provider-specific installation system, hooks, transformers, CLI machinery or the full upstream reference corpus. The frontend-design skill family uses independently written workflow contracts and selected methodology concepts appropriate to `GithubLarsKomo/skillz`.

When future versions copy or vendor upstream source files, they must preserve the applicable Apache-2.0 notices and provenance for those files.

## Deliberate v1 omissions

- Provider/harness-specific hooks.
- Impeccable CLI installation/update logic.
- Provider transformers and command emission.
- Automatic post-edit enforcement hooks.
- Wholesale duplication of the upstream command/reference tree.

These omissions keep v1 portable and consistent with `composable-skill-factory`.
