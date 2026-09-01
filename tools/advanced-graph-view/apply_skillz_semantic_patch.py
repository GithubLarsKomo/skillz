#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


SKILLZ_COLORS = {
    "analysis": "0x56b4e9",
    "communication-memory": "0xcc79a7",
    "engineering": "0x009e73",
    "legal-specialist": "0xa78bfa",
    "productivity": "0x22d3ee",
    "regulated-engineering": "0xe15759",
    "research-knowledge": "0xf0e442",
    "skill-system": "0xd1d5db",
    "tax-specialist": "0xf28e2b",
    "workflow": "0xc49a6c",
    "internal": "0x6b7280",
}

LOCALES = (
    "de.ts",
    "en.ts",
    "es.ts",
    "fr.ts",
    "it.ts",
    "ja.ts",
    "ko.ts",
    "pl.ts",
    "pt-BR.ts",
    "ru.ts",
    "uk.ts",
    "zh.ts",
)


class PatchError(RuntimeError):
    pass


def read(path: Path) -> str:
    if not path.is_file():
        raise PatchError(f"Missing expected file: {path}")
    return path.read_text(encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise PatchError(f"{label}: expected exactly one marker, found {count}")
    return text.replace(old, new, 1)


def patch_metrics(root: Path) -> None:
    path = root / "src/encoding/metrics.ts"
    text = read(path)
    if '"skill-category"' in text:
        return

    text = replace_once(
        text,
        'export type CategoricalMetricId = "folder" | "tag" | "cluster";',
        'export type CategoricalMetricId = "folder" | "tag" | "cluster" | "skill-category";',
        label="metrics categorical type",
    )
    text = replace_once(
        text,
        'export const CATEGORICAL_METRIC_IDS: readonly CategoricalMetricId[] = ["folder", "tag", "cluster"];',
        'export const CATEGORICAL_METRIC_IDS: readonly CategoricalMetricId[] = ["folder", "tag", "cluster", "skill-category"];',
        label="metrics categorical ids",
    )
    text = replace_once(
        text,
        '\t\tcase "tag": return facts.tags[0] ?? "";\n\t\tcase "cluster": return facts.cluster;',
        '\t\tcase "tag": return facts.tags[0] ?? "";\n'
        '\t\tcase "cluster": return facts.cluster;\n'
        '\t\tcase "skill-category": {\n'
        '\t\t\tconst prefix = "skill-category/";\n'
        '\t\t\tconst tag = facts.tags.find((value) => value.startsWith(prefix));\n'
        '\t\t\treturn tag ? tag.slice(prefix.length) : "";\n'
        '\t\t}',
        label="metrics compute switch",
    )
    text = replace_once(
        text,
        'return metric === "folder" || metric === "tag" || metric === "cluster";',
        'return metric === "folder" || metric === "tag" || metric === "cluster" || metric === "skill-category";',
        label="metrics categorical predicate",
    )
    write(path, text)


def patch_color_scales(root: Path) -> None:
    path = root / "src/encoding/colorScales.ts"
    text = read(path)
    if '"skillz-semantic"' in text:
        return

    text = replace_once(
        text,
        '\t/** Distinct hues for categorical color metrics. */\n\tcategories: number[];\n',
        '\t/** Distinct hues for categorical color metrics. */\n'
        '\tcategories: number[];\n'
        '\t/** Optional exact category → color mapping before hash fallback. */\n'
        '\tcategoryOverrides?: Record<string, number>;\n',
        label="scale preset interface",
    )

    override_lines = "\n".join(
        f'\t\t\t"{name}": {color},' for name, color in SKILLZ_COLORS.items()
    )
    preset = (
        '\t"skillz-semantic": {\n'
        '\t\t// Semantic palette for the generated Skillz Obsidian projection.\n'
        '\t\tstops: [0x56b4e9, 0x009e73, 0xf0e442, 0xe15759],\n'
        '\t\tcategories: CATEGORY_PALETTE,\n'
        '\t\tcategoryOverrides: {\n'
        f'{override_lines}\n'
        '\t\t},\n'
        '\t},\n'
    )
    text = replace_once(
        text,
        '\t},\n};\n\nexport const DEFAULT_PRESET_ID = "recency";',
        '\t},\n' + preset + '};\n\nexport const DEFAULT_PRESET_ID = "recency";',
        label="skillz semantic preset",
    )

    old_fn = (
        'export function categoryColor(category: string, palette: readonly number[] = CATEGORY_PALETTE): number {\n'
        '\tlet hash = 5381;'
    )
    new_fn = (
        'export function categoryColor(\n'
        '\tcategory: string,\n'
        '\tpalette: readonly number[] = CATEGORY_PALETTE,\n'
        '\toverrides?: Readonly<Record<string, number>>\n'
        '): number {\n'
        '\tconst override = overrides?.[category];\n'
        '\tif (override !== undefined) return override;\n'
        '\tlet hash = 5381;'
    )
    text = replace_once(text, old_fn, new_fn, label="categoryColor overrides")
    write(path, text)


def patch_encode(root: Path) -> None:
    path = root / "src/encoding/encode.ts"
    text = read(path)
    marker = 'categoryColor(categories[i], preset.categories, preset.categoryOverrides)'
    if marker in text:
        return
    text = replace_once(
        text,
        'categoryColor(categories[i], preset.categories)',
        marker,
        label="encoding semantic overrides",
    )
    write(path, text)


def patch_legend(root: Path) -> None:
    path = root / "src/ui/Legend.ts"
    text = read(path)
    if 'preset.categoryOverrides' in text:
        return
    text = replace_once(
        text,
        '\t\tconst palette = activePreset(presetId).categories;',
        '\t\tconst preset = activePreset(presetId);\n\t\tconst palette = preset.categories;',
        label="legend active preset",
    )
    text = replace_once(
        text,
        'categoryColor(category, palette)',
        'categoryColor(category, palette, preset.categoryOverrides)',
        label="legend semantic override",
    )
    write(path, text)


def patch_theme_contrast(root: Path) -> None:
    path = root / "src/encoding/themeContrast.ts"
    text = read(path)
    if 'categoryOverrides: preset.categoryOverrides' in text:
        return
    text = replace_once(
        text,
        '\t\tcategories: preset.categories.map((color) => adaptColorToTheme(color, true)),\n',
        '\t\tcategories: preset.categories.map((color) => adaptColorToTheme(color, true)),\n'
        '\t\tcategoryOverrides: preset.categoryOverrides\n'
        '\t\t\t? Object.fromEntries(\n'
        '\t\t\t\tObject.entries(preset.categoryOverrides).map(([key, color]) => [key, adaptColorToTheme(color, true)])\n'
        '\t\t\t)\n'
        '\t\t\t: undefined,\n',
        label="theme semantic overrides",
    )
    write(path, text)


def patch_locale(path: Path) -> None:
    text = read(path)
    changed = False

    if '"metric.skill-category"' not in text:
        match = re.search(r'^(\s*)"metric\.cluster":\s*"[^"]*",\s*$', text, flags=re.MULTILINE)
        if not match:
            raise PatchError(f"{path}: could not find metric.cluster")
        indent = match.group(1)
        label = "Skill-Kategorie" if path.name == "de.ts" else "Skill category"
        insertion = match.group(0) + f'\n{indent}"metric.skill-category": "{label}",'
        text = text[: match.start()] + insertion + text[match.end() :]
        changed = True

    if '"scale.skillz-semantic"' not in text:
        match = re.search(r'^(\s*)"scale\.pastel":\s*"[^"]*",\s*$', text, flags=re.MULTILINE)
        if not match:
            raise PatchError(f"{path}: could not find scale.pastel")
        indent = match.group(1)
        insertion = match.group(0) + f'\n{indent}"scale.skillz-semantic": "Skillz Semantic",'
        text = text[: match.start()] + insertion + text[match.end() :]
        changed = True

    if changed:
        write(path, text)


def patch_locales(root: Path) -> None:
    locale_root = root / "src/i18n/locales"
    for locale in LOCALES:
        patch_locale(locale_root / locale)


def add_tests(root: Path) -> None:
    path = root / "src/encoding/skillzSemantic.test.ts"
    if path.exists():
        return
    content = '''import { describe, expect, test } from "vitest";
import { resolvePreset, categoryColor } from "./colorScales";
import { buildEncoding } from "./encode";
import { computeMetric, type NodeFacts } from "./metrics";

function facts(tags: string[]): NodeFacts {
\treturn {
\t\tpath: "skills/example.md",
\t\tfolder: "skills",
\t\ttags,
\t\tinCount: 0,
\t\toutCount: 0,
\t\tunresolvedCount: 0,
\t\tctime: 0,
\t\tmtime: 0,
\t\tsize: 100,
\t\topensTotal: 0,
\t\tpagerank: 0,
\t\tcluster: "",
\t\topens7: 0,
\t\topens30: 0,
\t\topens90: 0,
\t};
}

describe("Skillz semantic coloring", () => {
\ttest("extracts generated skill-category tags", () => {
\t\texpect(
\t\t\tcomputeMetric("skill-category", facts(["skill", "skill-category/engineering"]), 0)
\t\t).toBe("engineering");
\t});

\ttest("returns an empty category for unrelated notes", () => {
\t\texpect(computeMetric("skill-category", facts(["skill-workflow"]), 0)).toBe("");
\t});

\ttest("uses exact semantic overrides before hash fallback", () => {
\t\tconst preset = resolvePreset("skillz-semantic");
\t\texpect(categoryColor("engineering", preset.categories, preset.categoryOverrides)).toBe(0x009e73);
\t\texpect(categoryColor("regulated-engineering", preset.categories, preset.categoryOverrides)).toBe(0xe15759);
\t\texpect(categoryColor("tax-specialist", preset.categories, preset.categoryOverrides)).toBe(0xf28e2b);
\t});

\ttest("buildEncoding applies semantic category colors", () => {
\t\tconst encoded = buildEncoding(
\t\t\t[facts(["skill", "skill-category/tax-specialist"])],
\t\t\t{ size: null, color: "skill-category", glow: null },
\t\t\t"skillz-semantic",
\t\t\t0
\t\t);
\t\texpect(encoded.categories).toEqual(["tax-specialist"]);
\t\texpect(encoded.tints[0]).toBe(0xf28e2b);
\t});
});
'''
    write(path, content)


def validate_root(root: Path) -> None:
    expected = (
        root / "package.json",
        root / "src/encoding/metrics.ts",
        root / "src/encoding/colorScales.ts",
        root / "src/encoding/encode.ts",
        root / "src/encoding/themeContrast.ts",
        root / "src/ui/Legend.ts",
    )
    missing = [str(path) for path in expected if not path.is_file()]
    if missing:
        raise PatchError(
            "Target does not look like n23eos/advanced_graph_view. Missing: " + ", ".join(missing)
        )


def apply(root: Path) -> None:
    validate_root(root)
    patch_metrics(root)
    patch_color_scales(root)
    patch_encode(root)
    patch_legend(root)
    patch_theme_contrast(root)
    patch_locales(root)
    add_tests(root)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply the Skillz semantic-category patch to an Advanced Graph View checkout."
    )
    parser.add_argument("repo", type=Path, help="Path to a clone/fork of n23eos/advanced_graph_view")
    args = parser.parse_args()
    root = args.repo.resolve()

    try:
        apply(root)
    except PatchError as exc:
        parser.error(str(exc))

    print("Applied Skillz Semantic patch.")
    print("Recommended verification: npm install && npm run verify && npm run build")
    print("Obsidian: Size=PageRank, Color=Skill category, Color scheme=Skillz Semantic, Glow=off")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
