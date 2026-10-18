# News feed (`news.json` schema v1) — tools, ready to move

1.3.0 (10). The Feed tab's **News** side reads one file, `news.json`, from `ContentConfig.newsURL` =
`https://raw.githubusercontent.com/DisclosureManager/disclosure-content/main/news.json`: the ONE public content repo
(Johan / ADM), next to the catalog (`manifest.json`, `entries.json`, `glossary.json`). This folder is the master copy;
nothing is pushed from the app repo, and GitHub does not run `workflows/` here.

## Rules (enforced by `validate_news.py` and the app's `NewsValidation`)
- Every item links to its **original source**: `url` is required, https, real host.
- `summary` / `summary_de`: optional, **our own** one-liners, max **160** characters, one line. Never copied article text.
- **No body / content field.** Item keys are limited to `id, title, url, source, source_kind, published_at, summary, summary_de, lang`;
  `body`, `content`, `html`, `text`, `description`, `excerpt`, … are rejected by name.
- `source_kind`: `official` | `press` | `advocacy` (advocacy keeps its own chip in the app).
- `feed_version` is the integer `1`; `generated_at` and `published_at` are ISO 8601 date-times with a zone. Max 200 items; zero is valid.

```json
{ "feed_version": 1, "generated_at": "2026-10-18T19:17:00Z",
  "items": [ { "id": "example-agency-1a2b3c4d5e6f", "title": "…", "url": "https://…", "source": "Example Agency",
               "source_kind": "official", "published_at": "2026-10-18T14:02:00Z", "summary": "optional", "lang": "en" } ] }
```

The app shows `generated_at` as "Updated <date, time>" plus "Updated hourly" / "Stündlich aktualisiert" (no fetch time; the cadence is always "hourly").

## Sources
- Headlines only from feeds or official APIs that serve RSS/Atom; nothing is scraped and no paywalled site is listed.
- General feeds (the Department of War releases, the committees, GAO, The Debrief, The Black Vault) keep only titles that match
  `match_title`. An all-caps term (UAP, AARO, PURSUE) matches case-sensitively and whole-word, so PURSUE never matches "pursue".
- `https_upgrade`: House Armed Services still prints http:// links; the builder rewrites them to https:// (same host).
- No usable feed (checked 18 Oct 2026): AARO (aaro.mil answers automated clients with 403 and no AARO RSS feed was found; its releases
  appear on the Department of War release feed), Senate Armed Services (no RSS), ODNI (403 to feed requests), the Federal Register
  API (works, but 0 UAP documents), war.gov/UFO (a page, no feed).

## Files
| File | Role |
|---|---|
| `validate_news.py` | Validator (CLI: `validate_news.py news.json`; `--expect-invalid` for the bad fixtures). |
| `build_news.py` | Hourly builder: approved RSS/Atom sources → `news.json`. Conditional requests (ETag / Last-Modified in the state file), 15 s per source, a failing source keeps its last good items, titles + links only (descriptions are never read), summaries only from `summaries.json`, writes only when the items change, validates before writing. |
| `sources.json` | Source list, **APPROVED** by ADM on 18 Oct 2026 (12 sources: 6 official, 4 press, 2 advocacy). Each: id, name, kind, feed_url, site_url, feed_format, topic, why, lang, enabled, paywall (+ match_title for general feeds, https_upgrade, verified). |
| `validate_sources.py` | sources.json schema: required fields, https feed/site URLs, rss/atom only (no scraping), `paywall: false`, at most 2 advocacy, official first, `match_title` required when `topic` is general, unknown keys rejected. Run by the builder (exit 1 on an invalid list) and by the workflow. |
| `verify_sources.py` | Fetches each source like the builder (same User-Agent, parser, title filter): HTTP status, items, latest item, UAP items. `--markdown` prints the table, `--write` stores it in `verified`. |
| `summaries.json` | Our own optional one-liners keyed by item id or url. |
| `workflows/news-feed.yml` | GitHub Action: cron `17 * * * *` + manual, concurrency `news-feed` (cancel in progress), built-in `GITHUB_TOKEN` with `contents: write` (no secrets), commit only when `news.json` changed (pull --rebase before the push). Inactive here (not under `.github/workflows`). |
| `fixtures/` | `news-sample.json` (= the app's DEBUG `-uitest-news-fixture sample`), `news-empty.json`, `invalid-*.json`. |
| `news_items_changed.py` | Workflow commit gate: exit 0 (commit) only when the `items` of `news.json` differ from `HEAD:news.json` or there is none yet; `generated_at` or `feed/state/` alone never commit. |
| `tests/` | `python3 -m unittest discover -s feed/tests` (recorded RSS + Atom, fake server). App repo only, not copied to `disclosure-content`. |

## In `disclosure-content`
`workflows/news-feed.yml` → `.github/workflows/`; the tools (incl. `news_items_changed.py`), `sources.json`, `summaries.json`, `fixtures/` →
`feed/` (`tests/` stay in the app repo); ETag state → `feed/state/news-state.json`; output `news.json` at the repo root. Run the workflow once by hand
(Actions › news-feed › Run workflow), then check that the raw URL above serves `news.json`.
