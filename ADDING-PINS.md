# Adding or changing globe pins (pins.json)

The globe in Disclosure Decoded (app 1.4.0 (16) and later) shows the pins from `pins.json`. The app downloads it from
this repo (same host as `entries.json`, no new server), caches it, and falls back to the copy bundled in the app.
Changing pins needs **no app update**.

## How the app reads the file

1. It reads `manifest.json`. If `pins_version` there is higher than the last one it loaded (or it has no cached pins
   yet), it downloads the file named in `pins`.
2. It checks every row on its own. A bad row is **skipped** (the rest stay visible); the app never crashes on it.
3. If no row is usable, the file is empty, not JSON, or has a `schema_version` the app does not know, the app keeps
   its last good cached pins, or else the pins bundled in the app.
4. Only the validated rows are cached. Unknown fields are dropped.

## File layout

```json
{
  "schema_version": 1,
  "pins_version": 2,
  "updated": "YYYY-MM-DD",
  "pins": [ { ... }, { ... } ]
}
```

| Field | Required | Rule |
|---|---|---|
| `schema_version` | yes | `1`. Only raise it with a matching app release: an app that does not know the number ignores the whole file. |
| `pins_version` | yes | Integer. **Raise it by 1 with every change**, in `pins.json` and in `manifest.json` (`pins_version`). |
| `updated` | no | `YYYY-MM-DD`. |
| `pins` | yes | Non-empty array of pins. |

### Pin fields

| Field | Required | Rule |
|---|---|---|
| `id` | yes | Unique, lowercase, e.g. `rendlesham-1980`. Never reuse an id for a different case. |
| `title.en`, `title.de` | yes | Non-empty. |
| `date` | yes | `YYYY-MM-DD`, `YYYY-MM` or `YYYY`; a range is `start/end`, e.g. `1980-12-26/1980-12-28`. |
| `location.en`, `location.de` | yes | Non-empty place text. |
| `lat` | yes | Number, -90 to 90 (decimal degrees, north positive). |
| `lon` | yes | Number, -180 to 180 (decimal degrees, east positive). |
| `summary.en`, `summary.de` | yes | Non-empty, neutral, sourced. |
| `strength` | yes | `strong` (case-specific official source), `medium` (official archive/index plus reputable coverage) or `weak` (press/secondary only). |
| `sources` | yes | Non-empty array of `{"title": "...", "url": "https://..."}`. **https only**: one http link skips the whole pin. |
| `entry_id` | no | Id of an archive entry in `entries.json`. The pin detail then shows "Open case file" / "Fallakte öffnen". An unknown id is ignored by the app. |

There is **no** `thumbnail_url` (or any image field). Do not add one; the validator rejects it.

## Full example (one pin)

```json
{
  "id": "rendlesham-1980",
  "title": {
    "en": "Rendlesham Forest Incident",
    "de": "Vorfall im Rendlesham Forest"
  },
  "date": "1980-12-26/1980-12-28",
  "location": {
    "en": "Rendlesham Forest, Suffolk, England, UK",
    "de": "Rendlesham Forest, Suffolk, England, Großbritannien"
  },
  "lat": 52.0897,
  "lon": 1.4366,
  "summary": {
    "en": "US Air Force personnel at RAF Woodbridge reported lights and a possible craft in the forest on two nights, and deputy base commander Charles Halt sent a memo to the UK Ministry of Defence. The MoD concluded the reports had no defence significance. Common explanations include the Orford Ness lighthouse, bright stars and a fireball; the file is open at The National Archives.",
    "de": "Angehörige der US-Luftwaffe auf RAF Woodbridge meldeten in zwei Nächten Lichter und ein mögliches Fluggerät im Wald; der stellvertretende Kommandant Charles Halt schickte ein Memo an das britische Verteidigungsministerium. Das Ministerium sah darin keine Bedeutung für die Verteidigung. Gängige Erklärungen sind der Leuchtturm von Orford Ness, helle Sterne und ein Feuerball; die Akte ist in den National Archives einsehbar."
  },
  "strength": "strong",
  "sources": [
    {
      "title": "The National Archives (UK): Rendlesham Forest file",
      "url": "https://discovery.nationalarchives.gov.uk/details/r/C11483093"
    },
    {
      "title": "The National Archives (UK): UFO reports",
      "url": "https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/"
    }
  ],
  "entry_id": "rendlesham-1980"
}
```

## Steps

1. Edit `pins.json` (add, change or remove pins).
2. Raise `pins_version` by 1 in `pins.json` **and** `manifest.json`.
3. Validate:

   ```sh
   python3 tools/validate_pins.py          # must print OK
   python3 scripts/validate.py             # catalog + manifest still OK
   jq -e '.schema_version == 1 and (.pins | length) > 0 and all(.pins[]; (.lat | fabs) <= 90 and (.lon | fabs) <= 180 and all(.sources[]; .url | startswith("https://")))' pins.json
   ```

4. Commit and publish as usual. Apps pick the change up at the next start or archive refresh.

