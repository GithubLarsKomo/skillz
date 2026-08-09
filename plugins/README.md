# Generated Codex plugins

`plugins/skillz/` is a generated Codex plugin bundle built from the canonical skill sources under `skills/`.

Do not hand-edit generated plugin files. Regenerate them with:

```bash
python scripts/build_openai_plugin.py --output plugins/skillz
```

The repository marketplace manifest is `.agents/plugins/marketplace.json` and points to `./plugins/skillz`.
