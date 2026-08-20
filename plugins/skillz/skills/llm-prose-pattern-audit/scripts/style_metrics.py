#!/usr/bin/env python3
"""Diagnostic style metrics for German/English prose. Not an AI detector."""
from __future__ import annotations
import argparse, json, re, statistics, sys
from collections import Counter

CONNECTORS = {
    "en": ["additionally", "moreover", "furthermore", "however", "therefore", "consequently", "overall", "in conclusion"],
    "de": ["darüber hinaus", "zudem", "weiterhin", "allerdings", "daher", "folglich", "insgesamt", "zusammenfassend"],
}
HEDGES = {
    "en": ["may", "might", "could", "appears", "suggests", "potentially", "possibly"],
    "de": ["könnte", "dürfte", "scheint", "möglicherweise", "potenziell", "eventuell"],
}
EVALUATIVE = {
    "en": ["key", "crucial", "pivotal", "significant", "important", "robust", "essential"],
    "de": ["entscheidend", "wesentlich", "relevant", "bedeutend", "wichtig", "zentral", "robust"],
}

def occurrences(text: str, terms: list[str]) -> int:
    low = text.lower()
    return sum(len(re.findall(r"(?<!\w)" + re.escape(t) + r"(?!\w)", low)) for t in terms)

def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ0-9])", text.strip()) if s.strip()]

def main() -> int:
    p = argparse.ArgumentParser(description="Emit diagnostic prose metrics as JSON; never an AI-authorship score.")
    p.add_argument("path", nargs="?", help="UTF-8 input file; omit to read stdin")
    p.add_argument("--language", choices=["de", "en"], required=True)
    args = p.parse_args()
    text = open(args.path, encoding="utf-8").read() if args.path else sys.stdin.read()
    words = re.findall(r"\b[\wÄÖÜäöüß'-]+\b", text, flags=re.UNICODE)
    sents = sentences(text)
    lengths = [len(re.findall(r"\b[\wÄÖÜäöüß'-]+\b", s, flags=re.UNICODE)) for s in sents]
    initial_connectors = 0
    for s in sents:
        low = s.lower()
        if any(low.startswith(c) for c in CONNECTORS[args.language]):
            initial_connectors += 1
    bullets = sum(1 for line in text.splitlines() if re.match(r"^\s*(?:[-*•]|\d+[.)])\s+", line))
    nominalizations = 0
    if args.language == "de":
        nominalizations = sum(1 for w in words if re.search(r"(?:ung|heit|keit|tion|tät|ismus|ierung)(?:en|e|s)?$", w.lower()))
    metrics = {
        "schemaVersion": 1,
        "language": args.language,
        "wordCount": len(words),
        "sentenceCount": len(sents),
        "sentenceLengthMean": round(statistics.mean(lengths), 2) if lengths else 0,
        "sentenceLengthStdev": round(statistics.pstdev(lengths), 2) if len(lengths) > 1 else 0,
        "semicolonCount": text.count(";"),
        "colonCount": text.count(":"),
        "emDashCount": text.count("—"),
        "bulletCount": bullets,
        "sentenceInitialConnectorCount": initial_connectors,
        "connectorCount": occurrences(text, CONNECTORS[args.language]),
        "hedgeCount": occurrences(text, HEDGES[args.language]),
        "evaluativeWordCount": occurrences(text, EVALUATIVE[args.language]),
        "negativeParallelismCount": len(re.findall(r"\bnot\s+(?:only\s+)?[^.!?]{1,80}\bbut\b", text, flags=re.I)) if args.language == "en" else len(re.findall(r"\bnicht\s+(?:nur\s+)?[^.!?]{1,80}\bsondern\b", text, flags=re.I)),
        "germanNominalizationHeuristicCount": nominalizations,
        "note": "Diagnostic indicators only; do not interpret as AI-authorship probability or fixed quality targets."
    }
    json.dump(metrics, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
