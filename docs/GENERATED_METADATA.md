# Generated repository metadata

`README.md` skill catalog and `.skill-sync.json` are generated repository metadata.

After adding, removing, or modifying a portable skill file, run:

```bash
python scripts/generate_repository_metadata.py
```

The command updates both generated files in one deterministic pass. `synchronizedAt` is preserved rather than rewritten so repeated runs without source changes remain byte-for-byte stable.

Before committing, verify the generated state with:

```bash
python scripts/generate_repository_metadata.py --check
```

`--check` never rewrites files. It exits non-zero and prints each stale generated path. CI uses the same read-only check before the remaining repository validation.

Portable synchronization content consists of each `SKILL.md` plus files under `references/`, `scripts/`, and `assets/`. Hashes use UTF-8 text with CRLF and CR normalized to LF and exactly one trailing LF. Evaluation fixtures are intentionally not part of `.skill-sync.json`.

The legacy commands `python scripts/generate_catalog.py` and `python scripts/verify_generated.py` remain available as compatibility wrappers around the unified generator.
