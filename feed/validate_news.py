#!/usr/bin/env python3
"""news.json schema v1 validator (twin of NewsValidation in DisclosureApp/Logic/NewsLogic.swift; keep in sync).

Rules (ADM, 1.3.0 (9)):
- every item links to its ORIGINAL source: `url` is required and must be https with a real host;
- `summary` / `summary_de` are optional, our OWN one-liners, at most 160 characters, one line;
- there is no body / content field: any item key outside ALLOWED_ITEM_KEYS is an error (article-text keys
  such as body, content, html, text, description are named as such);
- feed_version is the integer 1, generated_at and published_at are ISO 8601 date-times with a zone;
- ids are unique; source_kind is official, press or advocacy; at most 200 items. Zero items is valid.

Usage: validate_news.py FILE [FILE ...]   → exit 0 when every file is valid, 1 otherwise.
       validate_news.py --expect-invalid FILE ...  → exit 0 only when every file is INVALID (fixture check).
"""
import json, re, sys
from datetime import datetime
from urllib.parse import urlsplit

SUPPORTED_VERSION = 1
MAX_ITEMS = 200
MAX_TITLE = 200
MAX_SUMMARY = 160
MAX_SOURCE = 80
KINDS = {"official", "press", "advocacy"}
ALLOWED_ITEM_KEYS = {"id", "title", "url", "source", "source_kind", "published_at", "summary", "summary_de", "lang"}
ARTICLE_TEXT_KEYS = {"body", "content", "content_html", "html", "text", "full_text", "article", "description", "excerpt"}
_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$")


def is_iso_instant(value):
    if not isinstance(value, str) or not _ISO.match(value.strip()):
        return False
    try:
        datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def is_source_link(value):
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    parts = urlsplit(value)
    host = parts.hostname or ""
    return parts.scheme.lower() == "https" and "." in host and not host.startswith(".") and not host.endswith(".")


def issues(feed):
    """List of human-readable problems ([] = valid). `feed` is the parsed JSON value."""
    out = []
    if not isinstance(feed, dict):
        return ["feed is not a JSON object"]
    version = feed.get("feed_version")
    if not isinstance(version, int) or isinstance(version, bool):
        out.append("feed_version missing or not an integer")
    elif version != SUPPORTED_VERSION:
        out.append(f"feed_version {version} is not supported (expected {SUPPORTED_VERSION})")
    if not is_iso_instant(feed.get("generated_at")):
        out.append(f"generated_at {feed.get('generated_at')!r} is not an ISO 8601 date-time with a zone")
    items = feed.get("items")
    if not isinstance(items, list):
        return out + ["items missing or not an array"]
    if len(items) > MAX_ITEMS:
        out.append(f"{len(items)} items (max {MAX_ITEMS})")
    seen = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            out.append(f"item {index} is not an object")
            continue
        raw_id = item.get("id").strip() if isinstance(item.get("id"), str) else ""
        iid = raw_id or f"item {index}"
        for key in sorted(item):
            if key not in ALLOWED_ITEM_KEYS:
                if key.lower() in ARTICLE_TEXT_KEYS:
                    out.append(f"{iid}: field {key!r} not allowed (no article text: headline, link and our own summary only)")
                else:
                    out.append(f"{iid}: unknown field {key!r}")
        if not raw_id:
            out.append(f"{iid}: missing id")
        elif raw_id in seen:
            out.append(f"duplicate id {raw_id}")
        else:
            seen.add(raw_id)
        for field, limit in (("title", MAX_TITLE), ("source", MAX_SOURCE)):
            value = item.get(field).strip() if isinstance(item.get(field), str) else ""
            if not value:
                out.append(f"{iid}: missing {field}")
                continue
            if len(value) > limit:
                out.append(f"{iid}: {field} is {len(value)} characters (max {limit})")
            if "\n" in value or "\r" in value:
                out.append(f"{iid}: {field} must be one line")
        url = item.get("url")
        if not url:
            out.append(f"{iid}: missing url (every item links to its original source)")
        elif not is_source_link(url):
            out.append(f"{iid}: url {url!r} is not an https link to the original source")
        if item.get("source_kind") not in KINDS:
            out.append(f"{iid}: source_kind {item.get('source_kind')!r} (official, press or advocacy)")
        if not is_iso_instant(item.get("published_at")):
            out.append(f"{iid}: published_at {item.get('published_at')!r} is not an ISO 8601 date-time with a zone")
        for field in ("summary", "summary_de"):
            if field not in item:
                continue
            value = item[field]
            if not isinstance(value, str):
                out.append(f"{iid}: {field} must be a string")
                continue
            if len(value) > MAX_SUMMARY:
                out.append(f"{iid}: {field} is {len(value)} characters (max {MAX_SUMMARY})")
            if "\n" in value or "\r" in value:
                out.append(f"{iid}: {field} must be one line")
        if "lang" in item:
            lang = item["lang"]
            if not (isinstance(lang, str) and len(lang) == 2 and lang.isascii() and lang.islower() and lang.isalpha()):
                out.append(f"{iid}: lang {lang!r} (two-letter code)")
    return out


def validate_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        return [f"cannot read JSON: {e}"]
    return issues(data)


def main(argv):
    expect_invalid = "--expect-invalid" in argv
    paths = [a for a in argv if a != "--expect-invalid"]
    if not paths:
        print(__doc__)
        return 2
    ok = True
    for path in paths:
        found = validate_file(path)
        if expect_invalid:
            if found:
                print(f"OK (invalid as expected) {path}: {found[0]}")
            else:
                print(f"FAIL {path}: expected to be invalid, but it passed")
                ok = False
        elif found:
            ok = False
            print(f"FAIL {path}")
            for line in found:
                print(f"  - {line}")
        else:
            with open(path, encoding="utf-8") as f:
                n = len(json.load(f)["items"])
            print(f"OK {path} ({n} items)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
