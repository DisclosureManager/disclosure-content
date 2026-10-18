# disclosure-content

The public content for the **Disclosure Decoded** iOS app (DisclosureManager). The app reads these files directly over
GitHub raw from `https://raw.githubusercontent.com/DisclosureManager/disclosure-content/main/`. There is no server,
no account and no tracking.

| File | What it is | Updated |
|---|---|---|
| `manifest.json` | Catalog manifest (`catalog_version` 4, `updated` 2026-10-18) | with each catalog release |
| `entries.json` | Archive catalog v4: 54 entries (EN/DE), byte-identical to the bundle in app 1.3.0 | with each catalog release |
| `glossary.json` | Glossary (EN/DE) | with each catalog release |
| `news.json` | News feed, schema v1: headlines and links to the original sources only, no article text | about hourly, by the workflow |

The app keeps its bundled catalog, accepts a remote catalog only when it validates and is newer, and validates
`news.json` before caching it.

## News
- `.github/workflows/news-feed.yml` runs hourly (cron `17 * * * *`) and on demand (Actions › news-feed › Run workflow).
  It checks `feed/sources.json`, fetches the listed RSS/Atom feeds (conditional requests; a failing feed keeps its last
  good items), validates the result and commits `news.json` only when the items changed. It uses the built-in
  `GITHUB_TOKEN` with `contents: write` and no secrets.
- Tools and rules: `feed/README.md`. Check the feeds by hand with `python3 feed/verify_sources.py feed/sources.json --markdown`.
- Sources: `feed/sources.json`. Changes to the list need ADM's approval.

## Rules
Every news item links to its original source. Summaries are optional, our own and at most 160 characters. Advocacy
sources are labelled as advocacy. Catalog changes go through the app team's validator before they are committed here.
