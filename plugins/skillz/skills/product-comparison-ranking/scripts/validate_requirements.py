#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, sys

VALID_MODES={"private","professional-standard","professional-complex-technology"}

def validate(data):
    errors=[]
    if not isinstance(data,dict): return ["root must be an object"]
    if data.get("decisionType")!="purchase": errors.append("decisionType must be purchase")
    if data.get("mode") not in VALID_MODES: errors.append("invalid mode")
    ids=set()
    for field in ("mustHaves","preferences","criteria"):
        value=data.get(field,[])
        if not isinstance(value,list): errors.append(f"{field} must be a list"); continue
        for i,item in enumerate(value):
            if not isinstance(item,dict): errors.append(f"{field}[{i}] must be an object"); continue
            rid=item.get("id")
            if rid:
                if rid in ids: errors.append(f"duplicate id {rid}")
                ids.add(rid)
    criteria=data.get("criteria",[])
    weights=[c.get("weight") for c in criteria if isinstance(c,dict) and c.get("weight") is not None]
    if weights:
        if len(weights)!=len(criteria): errors.append("weights must be all confirmed or all omitted")
        elif not all(isinstance(x,(int,float)) and x>=0 for x in weights): errors.append("criterion weights must be non-negative numbers")
        elif not math.isclose(sum(weights),1.0,rel_tol=0,abs_tol=1e-9): errors.append("criterion weights must sum to 1.0")
    budget=data.get("budget")
    if budget is not None:
        if not isinstance(budget,dict): errors.append("budget must be an object")
        else:
            if budget.get("type") not in {"hard","soft",None}: errors.append("budget.type must be hard or soft")
            for key in ("target","maximum"):
                v=budget.get(key)
                if v is not None and (not isinstance(v,(int,float)) or v<0): errors.append(f"budget.{key} must be non-negative")
    return errors

def main():
    p=argparse.ArgumentParser(description="Validate purchase requirements JSON"); p.add_argument("path"); a=p.parse_args()
    try:
        with open(a.path,encoding="utf-8") as handle: data=json.load(handle)
    except (OSError,json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}",file=sys.stderr); return 2
    errors=validate(data)
    if errors:
        for e in errors: print(f"ERROR: {e}",file=sys.stderr)
        return 1
    print("OK"); return 0

if __name__=="__main__": raise SystemExit(main())
