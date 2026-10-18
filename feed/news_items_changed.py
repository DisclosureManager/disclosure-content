#!/usr/bin/env python3
"""Exit 0 when the ITEMS of news.json differ from the committed HEAD:news.json (or there is no committed copy yet:
first run), exit 1 when the items are equal. Only `items` is compared, so a new `generated_at` alone and changes to
feed/state/news-state.json never cause a commit. Used by .github/workflows/news-feed.yml.

Usage: news_items_changed.py [news.json]
"""
import json, subprocess, sys

path = sys.argv[1] if len(sys.argv) > 1 else "news.json"
with open(path, encoding="utf-8") as f:
    new_items = json.load(f).get("items")
shown = subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True)
if shown.returncode != 0:
    print(f"{path}: no committed copy (first run): commit")
    sys.exit(0)
try:
    old_items = json.loads(shown.stdout).get("items")
except ValueError:
    print(f"HEAD:{path} unreadable: commit")
    sys.exit(0)
if old_items == new_items:
    print(f"{path}: items unchanged ({len(new_items or [])}): no commit")
    sys.exit(1)
print(f"{path}: items changed ({len(old_items or [])} → {len(new_items or [])}): commit")
sys.exit(0)
