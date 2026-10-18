#!/usr/bin/env python3
"""sources.json schema v1 validator (the approved news sources that build_news.py reads).

Rules (ADM, 1.3.0 (9)):
- every source has: id (lower-case slug, unique), name, kind (official | press | advocacy), feed_url (https RSS / Atom,
  or an official API that serves RSS), site_url (https), why (one line, at most 160 characters: why it is
  trustworthy), lang, enabled (bool);
- feed_format is "rss" or "atom": a feed or an API, never a scraped page;
- at most 2 advocacy sources; official sources come first in the list;
- no paywalled sources: `paywall` must be false;
- optional: match_title (non-empty list of topic terms; required for general newsrooms and committees, see
  `topic`), https_upgrade (bool), topic ("uap" = the whole feed is about UAP, "general" = needs match_title),
  verified (the last manual check: on / http / items / latest_item).
Unknown keys are errors, so a typo never silently turns a rule off.

Usage: validate_sources.py FILE [FILE ...]   → exit 0 when every file is valid, 1 otherwise.
"""
import json, re, sys
from urllib.parse import urlsplit

KINDS = ("official", "press", "advocacy")
MAX_ADVOCACY = 2
MAX_WHY = 160
MAX_NAME = 80
REQUIRED = {"id", "name", "kind", "feed_url", "site_url", "feed_format", "why", "lang", "enabled", "paywall", "topic"}
OPTIONAL = {"match_title", "https_upgrade", "verified"}
VERIFIED_KEYS = {"on", "http", "items", "latest_item", "matching_items"}
_SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def _https(value):
    if not isinstance(value, str):
        return False
    parts = urlsplit(value.strip())
    return parts.scheme == "https" and "." in (parts.hostname or "")


def issues(doc):
    out = []
    if not isinstance(doc, dict) or not isinstance(doc.get("sources"), list):
        return ["top level must be an object with a `sources` list"]
    extra = set(doc) - {"sources", "_note", "_status", "schema_version"}
    if extra:
        out.append(f"unknown top-level keys: {sorted(extra)}")
    if doc.get("schema_version", 1) != 1:
        out.append("schema_version must be 1")
    seen, kinds = set(), []
    for n, s in enumerate(doc["sources"]):
        where = f"sources[{n}]" + (f" ({s.get('id')})" if isinstance(s, dict) and s.get("id") else "")
        if not isinstance(s, dict):
            out.append(f"{where}: must be an object"); continue
        missing, unknown = REQUIRED - set(s), set(s) - REQUIRED - OPTIONAL
        if missing:
            out.append(f"{where}: missing {sorted(missing)}")
        if unknown:
            out.append(f"{where}: unknown keys {sorted(unknown)}")
        sid = s.get("id")
        if not isinstance(sid, str) or not _SLUG.match(sid):
            out.append(f"{where}: id must be a lower-case slug")
        elif sid in seen:
            out.append(f"{where}: duplicate id")
        else:
            seen.add(sid)
        name = s.get("name")
        if not isinstance(name, str) or not name.strip() or len(name) > MAX_NAME:
            out.append(f"{where}: name must be 1–{MAX_NAME} characters")
        if s.get("kind") not in KINDS:
            out.append(f"{where}: kind must be one of {KINDS}")
        kinds.append(s.get("kind"))
        for key in ("feed_url", "site_url"):
            if key in s and not _https(s[key]):
                out.append(f"{where}: {key} must be an https URL with a real host")
        if s.get("feed_format") not in ("rss", "atom"):
            out.append(f"{where}: feed_format must be rss or atom (feeds and APIs only, no scraping)")
        why = s.get("why")
        if not isinstance(why, str) or not why.strip() or len(why) > MAX_WHY or "\n" in why:
            out.append(f"{where}: why must be one line of 1–{MAX_WHY} characters")
        if not isinstance(s.get("lang"), str) or not re.match(r"^[a-z]{2}$", s.get("lang", "")):
            out.append(f"{where}: lang must be a two-letter code")
        if not isinstance(s.get("enabled"), bool):
            out.append(f"{where}: enabled must be true or false")
        if s.get("paywall") is not False:
            out.append(f"{where}: paywalled sources are not allowed (paywall must be false)")
        topic = s.get("topic")
        if topic not in ("uap", "general"):
            out.append(f"{where}: topic must be uap or general")
        terms = s.get("match_title")
        if terms is not None and (not isinstance(terms, list) or not terms
                                  or not all(isinstance(t, str) and t.strip() for t in terms)):
            out.append(f"{where}: match_title must be a non-empty list of terms")
        if topic == "general" and not terms:
            out.append(f"{where}: a general feed needs match_title so only UAP headlines are kept")
        if "https_upgrade" in s and not isinstance(s["https_upgrade"], bool):
            out.append(f"{where}: https_upgrade must be true or false")
        v = s.get("verified")
        if v is not None and (not isinstance(v, dict) or set(v) - VERIFIED_KEYS):
            out.append(f"{where}: verified may only hold {sorted(VERIFIED_KEYS)}")
    if kinds.count("advocacy") > MAX_ADVOCACY:
        out.append(f"at most {MAX_ADVOCACY} advocacy sources (found {kinds.count('advocacy')})")
    order = [KINDS.index(k) for k in kinds if k in KINDS]
    if order and order[0] != 0 and "official" in kinds:
        out.append("official sources come first")
    if "official" in kinds and any(k != "official" for k in kinds[: kinds.count("official")]):
        out.append("official sources come first (all of them before press and advocacy)")
    return out


def main(argv):
    if not argv:
        print(__doc__); return 2
    bad = 0
    for path in argv:
        try:
            with open(path, encoding="utf-8") as f:
                problems = issues(json.load(f))
        except (OSError, ValueError) as e:
            problems = [f"unreadable: {e}"]
        if problems:
            bad += 1
            print(f"{path}: INVALID"); [print(f"  - {p}") for p in problems]
        else:
            print(f"{path}: valid")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
