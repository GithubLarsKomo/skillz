#!/usr/bin/env python3
"""Conservative token-level fidelity checks for prose rewrites."""
from __future__ import annotations
import argparse, json, re
from collections import Counter

PATTERNS = {
    "numbers": r"(?<!\w)[+-]?\d+(?:[.,]\d+)?(?:\s?%|\s?(?:mg|g|kg|µg|ug|ng|mL|ml|L|µL|uL|mm|cm|m|h|min|s|Hz|kDa))?(?!\w)",
    "doi": r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b",
    "pmid": r"\bPMID\s*:?\s*\d+\b",
    "urls": r"https?://[^\s)\]>]+",
    "numberedReferences": r"\[(?:\d+(?:\s*[-,]\s*\d+)*)\]",
}

def extract(text: str, pattern: str) -> Counter:
    return Counter(m.group(0) for m in re.finditer(pattern, text, flags=re.I))

def delta(a: Counter, b: Counter):
    return {"missing": list((a-b).elements()), "added": list((b-a).elements())}

def main() -> int:
    p = argparse.ArgumentParser(description="Compare conservative fidelity tokens between source and rewrite.")
    p.add_argument("source")
    p.add_argument("target")
    p.add_argument("--term-file", help="Optional UTF-8 file with one protected technical term per line")
    args = p.parse_args()
    src = open(args.source, encoding="utf-8").read()
    tgt = open(args.target, encoding="utf-8").read()
    out = {"schemaVersion": 1, "checks": {}}
    hard = []
    for name, pat in PATTERNS.items():
        d = delta(extract(src, pat), extract(tgt, pat))
        out["checks"][name] = d
        if d["missing"] or d["added"]:
            hard.append(name)
    if args.term_file:
        terms = [x.strip() for x in open(args.term_file, encoding="utf-8") if x.strip() and not x.lstrip().startswith("#")]
        src_terms = Counter({t: len(re.findall(re.escape(t), src, flags=re.I)) for t in terms})
        tgt_terms = Counter({t: len(re.findall(re.escape(t), tgt, flags=re.I)) for t in terms})
        out["checks"]["protectedTerms"] = delta(src_terms, tgt_terms)
    out["status"] = "review" if hard else "pass"
    out["reviewDimensions"] = hard
    out["note"] = "Token equality is not semantic proof; semantic claim, negation, modality and causality review remains required."
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
