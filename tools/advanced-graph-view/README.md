# Advanced Graph View — Skillz Semantic patch

This patch adds a deterministic semantic color layer for the generated Skillz Obsidian universe without changing canonical Skillz metadata.

## Result

Advanced Graph View gains:

- categorical metric `Skill category`
  - reads the generated `skill-category/<category>` tag
  - exposes only the category tail, e.g. `regulated-engineering`
- color scheme `Skillz Semantic`
  - exact category → color overrides
  - normal hashed palette fallback for non-Skillz categories
- theme-aware override colors
- matching legend swatches
- regression tests for extraction and rendering

Recommended view:

- Size: `PageRank`
- Color: `Skill category`
- Glow: off
- Color scheme: `Skillz Semantic`

## Semantic palette

| Category | Color |
|---|---|
| analysis | `#56B4E9` |
| communication-memory | `#CC79A7` |
| engineering | `#009E73` |
| legal-specialist | `#A78BFA` |
| productivity | `#22D3EE` |
| regulated-engineering | `#E15759` |
| research-knowledge | `#F0E442` |
| skill-system | `#D1D5DB` |
| tax-specialist | `#F28E2B` |
| workflow | `#C49A6C` |
| internal | `#6B7280` |

## Apply to a fork / clone

The repository tool cannot create a GitHub fork, so create `GithubLarsKomo/advanced_graph_view` once in GitHub from `n23eos/advanced_graph_view`. After that, on Windows PowerShell:

```powershell
git clone https://github.com/GithubLarsKomo/advanced_graph_view.git C:\programming\advanced_graph_view
cd C:\programming\skillz
python .\tools\advanced-graph-view\apply_skillz_semantic_patch.py C:\programming\advanced_graph_view
cd C:\programming\advanced_graph_view
npm install
npm run verify
npm run build
git checkout -b feat/skillz-semantic

git add src
git commit -m "feat: add Skillz semantic graph coloring"
git push -u origin feat/skillz-semantic
```

The patcher is idempotent for its own changes and intentionally fails when expected upstream source markers have drifted instead of silently producing a partial patch.

## BRAT

Once the fork has a build/release layout compatible with upstream, add the fork in BRAT as:

```text
GithubLarsKomo/advanced_graph_view
```

Then use the Advanced Graph View expert panel and save the configured view as `Skill Universe · Domains`.

## Upstream compatibility

The change is deliberately small:

- `src/encoding/metrics.ts`
- `src/encoding/colorScales.ts`
- `src/encoding/encode.ts`
- `src/encoding/themeContrast.ts`
- `src/ui/Legend.ts`
- locale files under `src/i18n/locales/`
- new `src/encoding/skillzSemantic.test.ts`

The generic extension is the exact categorical override map. The Skillz-specific pieces are the `skill-category/` extractor and the bundled semantic palette.
