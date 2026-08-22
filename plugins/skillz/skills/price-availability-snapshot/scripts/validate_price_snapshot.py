#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from datetime import datetime

ALLOWED_PRICE_STATUS={"available","unavailable","quote-required","uncertain"}
ALLOWED_CONDITION={"new","refurbished","used"}
ALLOWED_SELLER={"manufacturer-direct","authorized-dealer","specialist-retailer","large-retailer","marketplace-seller","refurbished-specialist","used-marketplace","unknown"}

def parse_time(value):
    if not isinstance(value,str) or not value:
        raise ValueError("capturedAt must be a non-empty ISO datetime")
    datetime.fromisoformat(value.replace("Z","+00:00"))

def validate(data):
    if not isinstance(data,dict) or data.get("schemaVersion") != 1:
        raise ValueError("schemaVersion must be 1")
    offers=data.get("offers")
    if not isinstance(offers,list):
        raise ValueError("offers must be a list")
    seen=set(); errors=[]
    for i,o in enumerate(offers):
        p=f"offers[{i}]"
        if not isinstance(o,dict): errors.append(f"{p}: must be object"); continue
        oid=o.get("offerId")
        if not isinstance(oid,str) or not oid: errors.append(f"{p}: offerId required")
        elif oid in seen: errors.append(f"{p}: duplicate offerId {oid}")
        seen.add(oid)
        if not o.get("candidateId") or not o.get("seller"): errors.append(f"{p}: candidateId and seller required")
        if o.get("condition") not in ALLOWED_CONDITION: errors.append(f"{p}: invalid condition")
        if o.get("sellerType","unknown") not in ALLOWED_SELLER: errors.append(f"{p}: invalid sellerType")
        status=o.get("priceStatus","available")
        if status not in ALLOWED_PRICE_STATUS: errors.append(f"{p}: invalid priceStatus")
        if status=="available":
            price=o.get("price")
            if not isinstance(price,dict) or not isinstance(price.get("amount"),(int,float)) or price["amount"] < 0 or not price.get("currency"): errors.append(f"{p}: available price requires non-negative amount and currency")
            try: parse_time(o.get("capturedAt"))
            except Exception as exc: errors.append(f"{p}: {exc}")
        ep=o.get("effectivePrice")
        if ep is not None and (not isinstance(ep,(int,float)) or ep < 0): errors.append(f"{p}: effectivePrice must be non-negative")
    return errors

def main():
    p=argparse.ArgumentParser(description="Validate price-snapshot.json"); p.add_argument("path"); a=p.parse_args()
    try:
        with open(a.path,encoding="utf-8") as handle: data=json.load(handle)
        errors=validate(data)
    except (OSError,json.JSONDecodeError,ValueError) as exc:
        print(f"ERROR: {exc}",file=sys.stderr); return 2
    if errors:
        for e in errors: print(f"ERROR: {e}",file=sys.stderr)
        return 1
    print("OK"); return 0

if __name__=="__main__": raise SystemExit(main())
