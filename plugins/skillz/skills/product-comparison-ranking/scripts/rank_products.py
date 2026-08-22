#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, sys

PASS="PASS"; CONDITIONAL="CONDITIONAL"; FAIL="FAIL"; UNKNOWN="UNKNOWN"

def candidate_gate(states):
    states=list(states or [])
    if any(s==FAIL for s in states): return FAIL
    if any(s in {CONDITIONAL,UNKNOWN} for s in states): return CONDITIONAL
    if states and all(s==PASS for s in states): return PASS
    return UNKNOWN

def weighted(scores, criteria, include_price=True):
    total=0.0
    for c in criteria:
        if not include_price and c.get("kind") in {"price","tco"}: continue
        cid=c["id"]
        if cid not in scores or scores[cid] is None: return None
        value=scores[cid]
        if not isinstance(value,(int,float)) or not 0 <= value <= 100: raise ValueError(f"score {cid} must be 0..100")
        total += c["weight"]*value
    if include_price: return total
    quality_weight=sum(c["weight"] for c in criteria if c.get("kind") not in {"price","tco"})
    return None if quality_weight<=0 else total/quality_weight

def rank(data):
    criteria=data.get("criteria",[])
    if not criteria or any("weight" not in c for c in criteria): raise ValueError("complete confirmed criteria weights required")
    if not math.isclose(sum(c["weight"] for c in criteria),1.0,abs_tol=1e-9): raise ValueError("criterion weights must sum to 1.0")
    floor=float(data.get("bargainQualityFloor",0.80))
    if not 0 < floor <= 1: raise ValueError("bargainQualityFloor must be in (0,1]")
    candidates=[]
    for raw in data.get("candidates",[]):
        c=dict(raw); c["gate"]=candidate_gate(c.get("mustHaveStates",[])); c["utilityScore"]=weighted(c.get("criterionScores",{}),criteria,True); c["qualityUtility"]=weighted(c.get("criterionScores",{}),criteria,False); c["labels"]=[]; candidates.append(c)
    eligible=[c for c in candidates if c["gate"]==PASS]
    quality_pool=[c for c in eligible if c.get("qualityUtility") is not None and c.get("evidenceCoverage") in {"high","medium"} and not c.get("materialReliabilityBlocker",False)]
    q=max(quality_pool,key=lambda x:x["qualityUtility"],default=None)
    if q: q["labels"].append("quality-winner")
    pp_pool=[c for c in eligible if c.get("utilityScore") is not None]
    pp=max(pp_pool,key=lambda x:x["utilityScore"],default=None)
    if pp: pp["labels"].append("price-performance-winner")
    bargain=None
    if q and isinstance(q.get("effectivePrice"),(int,float)):
        priced=[c for c in eligible if isinstance(c.get("effectivePrice"),(int,float)) and c.get("qualityUtility") is not None and c["qualityUtility"] >= floor*q["qualityUtility"] and c["effectivePrice"] < q["effectivePrice"] and c.get("evidenceCoverage") in {"high","medium"} and not c.get("materialReliabilityBlocker",False)]
        bargain=min(priced,key=lambda x:x["effectivePrice"],default=None)
        if bargain: bargain["labels"].append("bargain")
    candidates.sort(key=lambda c:(c["gate"]!=PASS, -(c["utilityScore"] if c["utilityScore"] is not None else -1)))
    shortlist=candidates[:10]
    missing_material=any(c["gate"] in {CONDITIONAL,UNKNOWN} or c.get("utilityScore") is None for c in shortlist)
    return {"schemaVersion":1,"rankingConfidence":"low" if missing_material else "high","winners":{"quality":q.get("candidateId") if q else None,"pricePerformance":pp.get("candidateId") if pp else None,"bargain":bargain.get("candidateId") if bargain else None},"rankedCandidates":shortlist,"excludedCandidates":[c["candidateId"] for c in candidates if c["gate"]==FAIL],"limitations":[]}

def main():
    p=argparse.ArgumentParser(description="Deterministically rank product candidates from structured JSON."); p.add_argument("input"); p.add_argument("-o","--output"); a=p.parse_args()
    try:
        with open(a.input,encoding="utf-8") as handle: data=json.load(handle)
        result=rank(data); text=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
        if a.output:
            with open(a.output,"w",encoding="utf-8") as handle: handle.write(text)
        else: sys.stdout.write(text)
        return 0
    except (OSError,json.JSONDecodeError,ValueError,KeyError,TypeError) as exc:
        print(f"ERROR: {exc}",file=sys.stderr); return 2

if __name__=="__main__": raise SystemExit(main())
