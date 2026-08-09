# Skillz OpenAI/Codex plugin source

This directory contains the canonical plugin manifest template. The `skills/` payload is generated from the repository's canonical skill sources by `scripts/build_openai_plugin.py` and is intentionally not duplicated here.

The repository-backed Codex marketplace materializes that template plus the portable skills into `plugins/skillz/`. Its marketplace entry lives at `.agents/plugins/marketplace.json` and points to `./plugins/skillz`.

Do not hand-edit `plugins/skillz/**`. Regenerate it with:

```bash
python scripts/build_openai_plugin.py --output plugins/skillz
```

Build, verification and Codex installation details: [`../../docs/OPENAI-PLUGIN-DISTRIBUTION.md`](../../docs/OPENAI-PLUGIN-DISTRIBUTION.md).
