#!/usr/bin/env python3
"""Builds news.json (schema v1) from the approved sources. Run hourly by the GitHub Action (workflows/news-feed.yml).

- Sources: sources.json (`enabled` sources only; ADM approves the list; schema: validate_sources.py). Each source is
  an RSS 2.0 or Atom feed (an official API that serves RSS counts); nothing is scraped. A general newsroom or
  committee feed carries `match_title` (topic terms) so only UAP headlines are kept.
- Conditional requests per source (If-None-Match / If-Modified-Since from the state file); per-source timeout.
- A source that fails (network, HTTP error, unparsable feed) keeps its last good items from the previous news.json.
- Headline + link only: the feed's description / content is NEVER read into news.json. A summary comes only from
  summaries.json (our own one-liners, keyed by item id or url), else the item has none.
- news.json is rewritten only when the ITEMS change (generated_at alone never causes a write or a commit).
- The result is validated (validate_news.py) before it is written; an invalid result is not written (exit 1).

Usage: build_news.py --sources sources.json --state state/news-state.json --out news.json [--summaries summaries.json]
       (in disclosure-content: --sources feed/sources.json --state feed/state/news-state.json --out news.json)
"""
import argparse, hashlib, json, os, re, sys, tempfile
import urllib.error, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_news  # noqa: E402
import validate_sources  # noqa: E402

PER_SOURCE_TIMEOUT = 15
PER_SOURCE_ITEMS = 20
MAX_AGE_DAYS = 60
USER_AGENT = "disclosure-news-bot/1 (+https://github.com/DisclosureManager/disclosure-content)"
ATOM = "{http://www.w3.org/2005/Atom}"


# MARK: fetching

def http_fetch(url, headers, timeout):
    """→ (status, body bytes or None, response headers dict). Raises on network errors."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **headers})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read(), {k.lower(): v for k, v in response.headers.items()}
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return 304, None, {k.lower(): v for k, v in e.headers.items()}
        return e.code, None, {}


def conditional_headers(state):
    headers = {}
    if state.get("etag"):
        headers["If-None-Match"] = state["etag"]
    if state.get("last_modified"):
        headers["If-Modified-Since"] = state["last_modified"]
    return headers


# MARK: parsing (titles, links, dates only)

def _text(el):
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def _date(value):
    value = (value or "").strip()
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)          # RSS: RFC 822
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))   # Atom: RFC 3339
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def parse_feed(body):
    """RSS 2.0 or Atom → [(title, link, published datetime)]. Descriptions and content are ignored on purpose."""
    root = ET.fromstring(body)
    out = []
    if root.tag == f"{ATOM}feed":
        for entry in root.findall(f"{ATOM}entry"):
            link = ""
            for l in entry.findall(f"{ATOM}link"):
                if l.get("rel", "alternate") == "alternate" and l.get("href"):
                    link = l.get("href").strip()
                    break
            published = _date(_text(entry.find(f"{ATOM}published")) or _text(entry.find(f"{ATOM}updated")))
            out.append((_text(entry.find(f"{ATOM}title")), link, published))
    else:
        for item in root.iter("item"):
            out.append((_text(item.find("title")), _text(item.find("link")), _date(_text(item.find("pubDate")))))
    return out


def item_id(source_id, link):
    return f"{source_id}-{hashlib.sha1(link.encode()).hexdigest()[:12]}"


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def title_matcher(terms):
    """`match_title` terms → predicate on a title (None = keep every title). An all-caps term (UAP, AARO, PURSUE)
    matches case-sensitively, so the acronym PURSUE never matches the verb "pursue"; other terms
    ("unidentified anomalous") match case-insensitively. Whole words only."""
    if not terms:
        return None
    patterns = [re.compile(rf"(?<!\w){re.escape(t)}(?!\w)", 0 if t.isupper() else re.I) for t in terms]
    return lambda title: any(p.search(title) for p in patterns)


def upgrade_link(link, source):
    """`https_upgrade`: a feed that still prints http:// links (House Armed Services) gets https:// on the same host."""
    if source.get("https_upgrade") and link.startswith("http://"):
        return "https://" + link[len("http://"):]
    return link


def to_items(source, parsed, summaries, now):
    """Feed entries → schema items: https links only, title capped, dated, recent, newest first, ≤ PER_SOURCE_ITEMS.
    A source with `match_title` keeps only titles that name the topic (general newsrooms and committees)."""
    cutoff = now - timedelta(days=MAX_AGE_DAYS)
    matches = title_matcher(source.get("match_title"))
    items = []
    for title, link, published in parsed:
        link = upgrade_link(link, source)
        if not title or not published or published < cutoff or not validate_news.is_source_link(link):
            continue
        if matches and not matches(title):
            continue
        if len(title) > validate_news.MAX_TITLE:
            title = title[: validate_news.MAX_TITLE - 1].rstrip() + "…"
        iid = item_id(source["id"], link)
        item = {"id": iid, "title": title, "url": link, "source": source["name"], "source_kind": source["kind"],
                "published_at": iso(min(published, now))}
        editorial = summaries.get(iid) or summaries.get(link) or {}
        for field in ("summary", "summary_de"):
            value = (editorial.get(field) or "").strip()
            if value and len(value) <= validate_news.MAX_SUMMARY and "\n" not in value:
                item[field] = value
        if source.get("lang"):
            item["lang"] = source["lang"]
        items.append(item)
    items.sort(key=lambda i: (i["published_at"], i["id"]), reverse=True)
    unique, seen = [], set()
    for i in items:
        if i["id"] not in seen:
            seen.add(i["id"]); unique.append(i)
    return unique[:PER_SOURCE_ITEMS]


# MARK: build

def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def write_json_atomic(path, value):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(os.path.abspath(path)), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, path)


def build(sources, state, previous, summaries, fetch=http_fetch, now=None, log=print):
    """→ (feed dict, new state, report lines). Pure apart from `fetch` (injectable for tests)."""
    now = now or datetime.now(timezone.utc).replace(microsecond=0)
    previous_items = previous.get("items", []) if isinstance(previous, dict) else []
    last_good = {}
    for i in previous_items:
        last_good.setdefault(i["id"].rsplit("-", 1)[0], []).append(i)
    new_state, items, report = {}, [], []
    for source in sources:
        if not source.get("enabled"):
            continue
        sid = source["id"]
        st = dict(state.get(sid, {}))
        kept = last_good.get(sid, [])
        try:
            status, body, headers = fetch(source["feed_url"], conditional_headers(st), PER_SOURCE_TIMEOUT)
            if status == 304:
                got, how = kept, "304 unchanged"
                if not kept:   # nothing to keep (news.json lost): forget the validators, fetch in full next run
                    st, how = {}, "304 but no last good items: state reset"
            elif status == 200 and body:
                got = to_items(source, parse_feed(body), summaries, now)
                st["etag"] = headers.get("etag") or None
                st["last_modified"] = headers.get("last-modified") or None
                how = f"200, {len(got)} items"
            else:
                got, how = kept, f"HTTP {status}: kept {len(kept)} last good items"
        except Exception as e:  # network error, timeout, bad XML: keep the last good items
            got, how = kept, f"failed ({type(e).__name__}): kept {len(kept)} last good items"
        st = {k: v for k, v in st.items() if v}
        new_state[sid] = st
        items.extend(got)
        report.append(f"{sid}: {how}")
    items.sort(key=lambda i: (i["published_at"], i["id"]), reverse=True)
    items = items[: validate_news.MAX_ITEMS]
    unchanged = isinstance(previous, dict) and previous.get("items") == items and previous.get("feed_version") == 1
    feed = previous if unchanged else {"feed_version": 1, "generated_at": iso(now), "items": items}
    return feed, new_state, report, not unchanged


def main(argv):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--sources", required=True)
    p.add_argument("--state", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--summaries")
    a = p.parse_args(argv)
    sources_doc = load_json(a.sources, None)
    source_problems = validate_sources.issues(sources_doc)
    if source_problems:   # a broken or unapproved-looking source list never reaches news.json
        print("sources.json invalid, nothing built:")
        for line in source_problems:
            print(f"  - {line}")
        return 1
    sources = sources_doc["sources"]
    summaries = load_json(a.summaries, {}) if a.summaries else {}
    feed, state, report, changed = build(sources, load_json(a.state, {}), load_json(a.out, {}), summaries)
    for line in report:
        print(line)
    problems = validate_news.issues(feed)
    if problems:
        print("news.json NOT written, validation failed:")
        for line in problems:
            print(f"  - {line}")
        return 1
    write_json_atomic(a.state, state)
    if changed:
        write_json_atomic(a.out, feed)
        print(f"news.json written: {len(feed['items'])} items, generated_at {feed['generated_at']}")
    else:
        print("news.json unchanged (same items)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
