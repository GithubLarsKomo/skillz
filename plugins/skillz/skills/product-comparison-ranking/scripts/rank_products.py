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

def _perturb_weights(criteria, target_id, shift):
    target=next((c for c in criteria if c["id"]==target_id),None)
    if target is None: raise KeyError(target_id)
    old=float(target["weight"])
    new=max(0.0,min(1.0,old+shift))
    if math.isclose(new,old,abs_tol=1e-12): return None
    others=1.0-old
    if others <= 1e-12: return None
    scale=(1.0-new)/others
    adjusted=[]
    for c in criteria:
        item=dict(c)
        item["weight"]=new if c["id"]==target_id else float(c["weight"])*scale
        adjusted.append(item)
    return adjusted

def _quality_pool(candidates):
    return [c for c in candidates if c["gate"]==PASS and c.get("evidenceCoverage") in {"high","medium"} and not c.get("materialReliabilityBlocker",False)]

def _quality_winner(candidates, criteria):
    scored=[]
    for c in _quality_pool(candidates):
        score=weighted(c.get("criterionScores",{}),criteria,False)
        if score is not None: scored.append((score,c))
    return max(scored,key=lambda x:x[0],default=(None,None))

def _price_performance_winner(candidates, criteria):
    scored=[]
    for c in candidates:
        if c["gate"]!=PASS: continue
        score=weighted(c.get("criterionScores",{}),criteria,True)
        if score is not None: scored.append((score,c))
    return max(scored,key=lambda x:x[0],default=(None,None))

def _margin(candidates, criteria, include_price):
    pool=[c for c in candidates if c["gate"]==PASS] if include_price else _quality_pool(candidates)
    scores=[]
    for c in pool:
        score=weighted(c.get("criterionScores",{}),criteria,include_price)
        if score is not None: scores.append(score)
    scores.sort(reverse=True)
    return None if len(scores)<2 else scores[0]-scores[1]

def sensitivity_analysis(candidates, criteria, delta=0.05, near_tie_threshold=1.0):
    if not 0 < delta < 1: raise ValueError("sensitivityDelta must be in (0,1)")
    if near_tie_threshold < 0: raise ValueError("nearTieThreshold must be >= 0")
    _,q=_quality_winner(candidates,criteria)
    _,pp=_price_performance_winner(candidates,criteria)
    baseline_q=q.get("candidateId") if q else None
    baseline_pp=pp.get("candidateId") if pp else None
    changes=[]; scenario_count=0
    for criterion in criteria:
        for direction in (-1,1):
            adjusted=_perturb_weights(criteria,criterion["id"],direction*delta)
            if adjusted is None: continue
            scenario_count+=1
            _,sq=_quality_winner(candidates,adjusted)
            _,spp=_price_performance_winner(candidates,adjusted)
            qid=sq.get("candidateId") if sq else None
            ppid=spp.get("candidateId") if spp else None
            if qid != baseline_q or ppid != baseline_pp:
                changes.append({
                    "criterionId":criterion["id"],
                    "direction":"decrease" if direction<0 else "increase",
                    "qualityWinner":qid,
                    "pricePerformanceWinner":ppid,
                    "weights":{c["id"]:round(c["weight"],10) for c in adjusted},
                })
    quality_margin=_margin(candidates,criteria,False)
    utility_margin=_margin(candidates,criteria,True)
    quality_stable=all(change["qualityWinner"]==baseline_q for change in changes)
    pp_stable=all(change["pricePerformanceWinner"]==baseline_pp for change in changes)
    return {
        "method":"one-at-a-time-weight-shift",
        "delta":delta,
        "nearTieThreshold":near_tie_threshold,
        "scenarioCount":scenario_count,
        "baseline":{"qualityWinner":baseline_q,"pricePerformanceWinner":baseline_pp},
        "margins":{"qualityUtility":quality_margin,"utilityScore":utility_margin},
        "nearTie":{
            "quality":quality_margin is not None and quality_margin <= near_tie_threshold,
            "pricePerformance":utility_margin is not None and utility_margin <= near_tie_threshold,
        },
        "qualityWinnerStable":quality_stable,
        "pricePerformanceWinnerStable":pp_stable,
        "winnerChanges":changes,
    }

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
    sensitivity=sensitivity_analysis(candidates,criteria,float(data.get("sensitivityDelta",0.05)),float(data.get("nearTieThreshold",1.0)))
    sensitivity_unstable=not sensitivity["qualityWinnerStable"] or not sensitivity["pricePerformanceWinnerStable"]
    near_tie=any(sensitivity["nearTie"].values())
    limitations=[]
    if sensitivity_unstable: limitations.append("winner changes under plausible one-at-a-time weight shifts")
    if near_tie: limitations.append("top candidates are within the configured near-tie threshold")
    if missing_material: limitations.append("shortlist contains conditional/unknown gates or incomplete utility scores")
    return {
        "schemaVersion":1,
        "rankingConfidence":"low" if missing_material or sensitivity_unstable or near_tie else "high",
        "winners":{"quality":q.get("candidateId") if q else None,"pricePerformance":pp.get("candidateId") if pp else None,"bargain":bargain.get("candidateId") if bargain else None},
        "rankedCandidates":shortlist,
        "excludedCandidates":[c["candidateId"] for c in candidates if c["gate"]==FAIL],
        "sensitivity":sensitivity,
        "limitations":limitations,
    }

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
