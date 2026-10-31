#!/usr/bin/env python3
"""Validate pins.json before every push. Mirrors the app's PinValidation (DisclosureApp/Logic/PinSync.swift, app 1.4.0 (16)).

The app checks pins ROW BY ROW and silently skips a bad row (it never crashes; an empty or unusable file falls back to
the last good cache, then to the pins bundled in the app). This script is stricter: ANY row the app would skip is an
error here, so a published file always shows every pin.

Usage:  python3 tools/validate_pins.py [path/to/pins.json]      (default: pins.json next to manifest.json)
Exit 0 = OK, 1 = problems (listed one per line).
"""
import datetime, json, pathlib, re, sys
from urllib.parse import urlparse

SUPPORTED_SCHEMA = 1
STRENGTHS = {"strong", "medium", "weak"}
root = pathlib.Path(__file__).resolve().parent.parent
path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "pins.json"
errors = []

def is_int(v): return isinstance(v, int) and not isinstance(v, bool)
def is_num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)

def day_ok(s):
    m = re.fullmatch(r"(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?", s)
    if not m: return False
    y, mo, d = m.group(1), m.group(2), m.group(3)
    if mo and not 1 <= int(mo) <= 12: return False
    if d:
        try: datetime.date(int(y), int(mo), int(d))
        except ValueError: return False
    return True

def date_ok(s): return isinstance(s, str) and 1 <= len(s.split("/")) <= 2 and all(day_ok(p) for p in s.split("/"))

def https_ok(u):
    p = urlparse(u if isinstance(u, str) else "")
    return p.scheme == "https" and "." in (p.hostname or "")

try:
    raw = path.read_text(encoding="utf-8")
    doc = json.loads(raw)
except Exception as e:
    print(f"{path.name}: not valid JSON ({e})"); sys.exit(1)

if "thumbnail_url" in raw: errors.append("thumbnail_url is not allowed anywhere in pins.json")
if not isinstance(doc, dict): errors.append("top level must be an object"); doc = {}
sv, pv = doc.get("schema_version"), doc.get("pins_version")
if not is_int(sv): errors.append("schema_version missing or not an integer")
elif sv > SUPPORTED_SCHEMA: errors.append(f"schema_version {sv} is newer than the app understands ({SUPPORTED_SCHEMA}): the app would ignore the whole file")
if not is_int(pv) or pv < 1: errors.append("pins_version must be an integer >= 1 (raise it with every change)")
if "updated" in doc and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(doc["updated"])): errors.append("updated must be YYYY-MM-DD")
pins = doc.get("pins")
if not isinstance(pins, list) or not pins: errors.append("pins must be a non-empty array"); pins = []

entry_ids = set()
try:
    ej = json.loads((root / "entries.json").read_text(encoding="utf-8"))
    entry_ids = {e.get("id") for e in (ej.get("entries", []) if isinstance(ej, dict) else ej)}
except Exception:
    pass

seen = set()
for i, p in enumerate(pins):
    pid = p.get("id") if isinstance(p, dict) else None
    tag = f"row {i} ({pid or '?'})"
    if not isinstance(p, dict): errors.append(f"{tag}: not an object"); continue
    if not isinstance(pid, str) or not pid.strip(): errors.append(f"{tag}: id missing or empty")
    elif pid in seen: errors.append(f"{tag}: duplicate id")
    seen.add(pid)
    for field in ("title", "location", "summary"):
        t = p.get(field)
        for lang in ("en", "de"):
            if not isinstance(t, dict) or not isinstance(t.get(lang), str) or not t[lang].strip():
                errors.append(f"{tag}: {field}.{lang} missing or empty")
    if not date_ok(p.get("date")): errors.append(f"{tag}: date must be YYYY, YYYY-MM, YYYY-MM-DD or start/end of those")
    lat, lon = p.get("lat"), p.get("lon")
    if not is_num(lat) or not -90 <= lat <= 90: errors.append(f"{tag}: lat must be a number in -90..90")
    if not is_num(lon) or not -180 <= lon <= 180: errors.append(f"{tag}: lon must be a number in -180..180")
    if p.get("strength") not in STRENGTHS: errors.append(f"{tag}: strength must be one of {sorted(STRENGTHS)}")
    srcs = p.get("sources")
    if not isinstance(srcs, list) or not srcs: errors.append(f"{tag}: sources must be a non-empty array")
    else:
        for s in srcs:
            if not isinstance(s, dict) or not str(s.get("title", "")).strip(): errors.append(f"{tag}: every source needs a title")
            if not isinstance(s, dict) or not https_ok(s.get("url")): errors.append(f"{tag}: source URL must be https: {s.get('url') if isinstance(s, dict) else s!r}")
    eid = p.get("entry_id")
    if eid is not None:
        if not isinstance(eid, str) or not eid.strip(): errors.append(f"{tag}: entry_id must be a non-empty string when present")
        elif entry_ids and eid not in entry_ids: errors.append(f"{tag}: entry_id {eid!r} is not in entries.json (the app would just hide 'Open case file')")
    allowed = {"id", "title", "date", "location", "lat", "lon", "summary", "strength", "sources", "entry_id"}
    extra = set(p) - allowed
    if extra: errors.append(f"{tag}: unknown field(s) {sorted(extra)} (the app ignores them)")

# The manifest must list the file and carry the same pins_version, or the app never downloads the change.
if path.resolve() == (root / "pins.json").resolve():
    try:
        m = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        if m.get("pins") != "pins.json": errors.append('manifest.json must list "pins": "pins.json"')
        if m.get("pins_version") != pv: errors.append(f"manifest.json pins_version ({m.get('pins_version')}) must equal pins.json pins_version ({pv})")
    except Exception as e:
        errors.append(f"manifest.json: not readable ({e})")

if errors:
    for e in errors: print("ERROR", e)
    print(f"FAILED: {len(errors)} problem(s) in {path.name}")
    sys.exit(1)
n_src = sum(len(p["sources"]) for p in pins)
linked = sum(1 for p in pins if p.get("entry_id"))
print(f"OK: schema_version {sv}, pins_version {pv}, {len(pins)} pins, {n_src} sources (all https), {linked} linked to archive entries")
