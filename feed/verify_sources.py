#!/usr/bin/env python3
"""Fetches every source in sources.json once, the way build_news.py does (same User-Agent, same parser, same
title filter), and prints a verification table: HTTP status, item count, latest item date, matching items.
`--write` stores the result in each source's `verified` block. A source that fails is reported, never dropped
here: dropping is an edit ADM approves.

Usage: verify_sources.py sources.json [--write] [--markdown]
"""
import json, sys, os
from datetime import datetime, timezone
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_news as B, validate_sources as V  # noqa: E402


def check(source, fetch=B.http_fetch):
    row = {"on": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "http": None, "items": 0, "latest_item": None,
           "matching_items": 0}
    try:
        status, body, _ = fetch(source["feed_url"], {}, B.PER_SOURCE_TIMEOUT)
        row["http"] = status
        if status == 200 and body:
            parsed = B.parse_feed(body)
            dates = [d for _, _, d in parsed if d]
            row["items"] = len(parsed)
            row["latest_item"] = B.iso(max(dates)) if dates else None
            match = B.title_matcher(source.get("match_title"))
            row["matching_items"] = sum(1 for t, _, _ in parsed if t and (match is None or match(t)))
    except Exception as e:  # noqa: BLE001 - reported, not raised
        row["error"] = f"{type(e).__name__}: {e}"[:120]
    return row


def main(argv):
    if not argv:
        print(__doc__); return 2
    path = argv[0]
    doc = json.load(open(path, encoding="utf-8"))
    problems = V.issues(doc)
    if problems:
        print("sources.json invalid:", *problems, sep="\n  - "); return 1
    rows, bad = [], 0
    for s in doc["sources"]:
        r = check(s)
        ok = r["http"] == 200 and r["items"] > 0
        bad += not ok
        rows.append((s, r, ok))
        if "--write" in argv:
            s["verified"] = {k: v for k, v in r.items() if k != "error"}
    if "--markdown" in argv:
        print("| # | Source | Type | HTTP | Items | Latest item (UTC) | UAP items now | Works |")
        print("|---|---|---|---|---|---|---|---|")
        for n, (s, r, ok) in enumerate(rows, 1):
            print(f"| {n} | {s['name']} | {s['kind']} | {r['http']} | {r['items']} | {r['latest_item'] or '—'} | "
                  f"{r['matching_items']}{' (all)' if s['topic'] == 'uap' else ''} | {'yes' if ok else 'NO ' + r.get('error', '')} |")
    else:
        for s, r, ok in rows:
            print(f"{'OK ' if ok else 'BAD'} {s['id']:<22} http={r['http']} items={r['items']} latest={r['latest_item']} "
                  f"matching={r['matching_items']} {r.get('error', '')}")
    if "--write" in argv:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2); f.write("\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
