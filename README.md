# disclosure-content

Content catalog for the iOS app **Disclosure** (bundle id `de.formaventus.disclosure`).
The app reads these files from the raw URL below.

[English](#english) · [Deutsch](#deutsch)

---

## English

### What this repo is

Static JSON for the app's archive of declassified UAP/UFO-related records. Every entry has:

- a plain-English summary and a German summary;
- a source link;
- verbatim key quotes;
- a 1–10 influence score with a five-area breakdown.

There is no backend. The app fetches the files, validates them, caches them, and falls back to the copy bundled in the app.

**The repo must stay public.** raw.githubusercontent.com serves nothing from a private repo without a token, and the app sends none.

App setting (`Config/Signing.xcconfig`):

```
CONTENT_BASE_URL = https:/$()/raw.githubusercontent.com/DisclosureManager/disclosure-content/main/
```

### Layout

| File | Purpose |
|---|---|
| `manifest.json` | `catalog_version`, `updated`, and the file names of `entries` and `glossary`. The app reads it first and skips the download when the version is not newer than the one it already has. |
| `entries.json` | `{"catalog_version": 5, "updated": "YYYY-MM-DD", "entries": [...]}`. The feed shows `updated` as "Updated <date>" / "Stand: <date>". |
| `glossary.json` | `{"version": 2, "terms": [...]}` (acronym, expansion, definition, definition_de) |
| `VERIFICATION.md` | One row per quote: the verbatim check against the primary source (or the named secondary source). |
| `scripts/validate.py` | Pre-push check. It applies the same rules as the app. |
| `pins.json` | Globe pins (app 1.4.0 (16)+): `{"schema_version": 1, "pins_version": 1, "updated": "YYYY-MM-DD", "pins": [...]}`. Listed in `manifest.json` as `pins` + `pins_version`. See [ADDING-PINS.md](ADDING-PINS.md). |
| `tools/validate_pins.py` | Pre-push check for `pins.json` (same rules as the app, but any skipped row is an error). |

### Entry fields

**Required:** `id`, `title`, `date` (YYYY-MM-DD), `source`, `source_url` (http/https), `category`, `summary`, `quotes`, `relevance_score` (1–10), `relevance_breakdown`, `timeline_context`, `tags`.

- `category` is one of: Congressional Hearing, Agency Report, FOIA Release, Whistleblower Testimony, Media Investigation, Other.
- `quotes` holds at least one `{speaker, text}`, quoted verbatim.
- `relevance_breakdown` has five areas, each scored 0–3 with a note, plus `explanation`. Kept from catalog v4 on so that app 1.2.0 can still decode the catalog; it no longer drives the score.
- **Catalog v4 and later:** `influence_breakdown` is required. It holds `official_acknowledgement`, `oversight_action`, `public_record`, `lasting_impact` and `evidence_substance` (integers 0–3), plus `note` and `note_de`. `relevance_score` must equal 1 + W × 0.3 rounded half up, where W = 2·official_acknowledgement + 2·oversight_action + 2·public_record + 3·lasting_impact + 1·evidence_substance (0–30). There is no other adjustment. `scripts/validate.py` checks this.

**Optional:**

- `title_de`, `summary_de`, `timeline_context_de`, `relevance_breakdown.explanation_de`
- `date_precision`: `year` or `month`
- `event_date` (YYYY-MM-DD) and `event_date_precision` (`year` or `month`): the date of the claimed event when it differs from `date` (for example magenta-1933: claim made 2023-06-11, claimed event 1933). The timeline groups and sorts by `event_date` when present; the feed keeps using `date`. Apps before 1.3.0 ignore these keys.
- `thumbnail_url`

Quotes and sources always stay in the English original. Original-language quotes are allowed only when no official English text exists; the quote `text` then holds the verbatim original followed by ` — English: "…" (unofficial translation)`. Only the part before the dash is checked verbatim (see VERIFICATION.md). There is no separate translation field.

### How the app uses it

1. **Fetch.** It fetches `manifest.json` (optional), then `entries.json` and `glossary.json`.
2. **Validate.** It checks:
   - the payload is a JSON object;
   - `catalog_version` is an integer and is not lower than the version bundled in the app;
   - `entries` is non-empty and every id is unique;
   - the required fields are present;
   - dates and URLs are valid;
   - every score is in range;
   - the glossary is non-empty.
3. **Apply.** A valid catalog is used and cached only when its `catalog_version` is higher than the last one the app saw. Bad data never overwrites a good cache.
4. **Fall back.** On any failure the app silently keeps its cached or bundled copy. That covers being offline, a 404, a 5xx, invalid JSON, a wrong schema and an older version.

### Publishing a new catalog

1. Edit `entries.json`. Add a row to `VERIFICATION.md` for every new quote. **Never invent quotes, dates or facts.**
2. Bump `catalog_version` by 1 in **both** `entries.json` and `manifest.json`. Set `updated` to today in both.
3. Run `python3 scripts/validate.py` and fix any errors.
4. Commit and push to `main`. Apps pick up the change on the next launch or pull-to-refresh. GitHub's raw cache can delay this by about 5 minutes.
5. Users with Premium get a "new release" notification for the newest entry.

### Current catalog

- `catalog_version` 5, updated 2026-10-27
- 58 entries, 159 quotes, all verified (see VERIFICATION.md)
- 23 glossary terms
- New in v5:
  - PURSUE Release 07 (Department of War, October 23, 2026)
  - Chile SEFAA September 2026 case files (October 8, 2026)
  - German government answer to Bundestag question on UAP (Drucksache 21/8662, October 16, 2026)
  - UK Ministry of Defence written answer on an RAF Typhoon near-miss with an unknown object (UIN 36199, October 26, 2026)
  - first original-language quotes (Spanish, German), each with an unofficial English translation
  - refreshed: pursue-release-06-2026 timeline line, pursue-nda-waiver-2026 note ("as of October 2026")
- New in v4: `influence_breakdown` and influence-based scores; `event_date` for magenta-1933
- New in v3:
  - PURSUE Releases 02–05 (Department of War, May–August 2026)
  - German titles (`title_de`) for every entry

---

## Deutsch

### Was dieses Repo ist

Statisches JSON für das Archiv der iOS-App **Disclosure**: freigegebene Dokumente rund um UAP/UFOs. Jeder Eintrag hat:

- eine Zusammenfassung auf Englisch und auf Deutsch;
- einen Quellenlink;
- wörtliche Kernzitate;
- einen Einflusswert von 1–10 mit einer Aufschlüsselung nach fünf Bereichen.

Es gibt kein Backend. Die App lädt die Dateien, prüft sie, speichert sie zwischen und fällt sonst auf die Kopie zurück, die in der App steckt.

**Das Repo muss öffentlich bleiben.** raw.githubusercontent.com liefert aus privaten Repos nichts ohne Token, und die App schickt keinen.

App-Einstellung (`Config/Signing.xcconfig`):

```
CONTENT_BASE_URL = https:/$()/raw.githubusercontent.com/DisclosureManager/disclosure-content/main/
```

### Aufbau

| Datei | Zweck |
|---|---|
| `manifest.json` | `catalog_version`, `updated` und die Dateinamen von `entries` und `glossary`. Die App liest sie zuerst und lädt nichts herunter, wenn die Version nicht neuer ist als die, die sie schon hat. |
| `entries.json` | `{"catalog_version": 5, "updated": "JJJJ-MM-TT", "entries": [...]}`. Der Feed zeigt `updated` als „Stand: <Datum>“ an. |
| `glossary.json` | `{"version": 2, "terms": [...]}` |
| `VERIFICATION.md` | Eine Zeile pro Zitat: der Wortlaut-Abgleich mit der Primärquelle (oder der genannten Sekundärquelle). |
| `scripts/validate.py` | Prüfung vor jedem Push. Sie wendet dieselben Regeln an wie die App. |
| `pins.json` | Globus-Pins (ab App 1.4.0 (16)): `{"schema_version": 1, "pins_version": 1, "updated": "JJJJ-MM-TT", "pins": [...]}`. In `manifest.json` als `pins` + `pins_version` eingetragen. Siehe [ADDING-PINS.md](ADDING-PINS.md). |
| `tools/validate_pins.py` | Prüfung von `pins.json` vor jedem Push (dieselben Regeln wie die App; jede Zeile, die die App überspringen würde, ist hier ein Fehler). |

### Felder

**Pflichtfelder:** `id`, `title`, `date` (JJJJ-MM-TT), `source`, `source_url` (http/https), `category`, `summary`, `quotes`, `relevance_score` (1–10), `relevance_breakdown`, `timeline_context`, `tags`.

- `quotes` enthält mindestens ein `{speaker, text}`, wörtlich zitiert.

- `relevance_breakdown` bleibt ab Katalog v4 erhalten, damit App 1.2.0 den Katalog weiter lesen kann; der Wert hängt nicht mehr davon ab.
- **Ab Katalog v4:** `influence_breakdown` ist Pflicht: `official_acknowledgement`, `oversight_action`, `public_record`, `lasting_impact` und `evidence_substance` (ganze Zahlen 0–3) sowie `note` und `note_de`. `relevance_score` muss 1 + W × 0,3 ergeben (kaufmännisch gerundet), mit W = 2·official_acknowledgement + 2·oversight_action + 2·public_record + 3·lasting_impact + 1·evidence_substance (0–30). Weitere Anpassungen gibt es nicht. `scripts/validate.py` prüft das.

**Optional:** `title_de`, `summary_de`, `timeline_context_de`, `relevance_breakdown.explanation_de`, `date_precision`, `event_date` und `event_date_precision` (Datum des behaupteten Ereignisses, wenn es von `date` abweicht; die Zeitleiste ordnet danach, der Feed nach `date`), `thumbnail_url`.

Zitate und Quellen bleiben immer im englischen Original. Zitate in der Originalsprache sind nur erlaubt, wenn es keinen offiziellen englischen Text gibt; dann enthält `text` das wörtliche Original, gefolgt von ` — English: "…" (unofficial translation)`. Wörtlich geprüft wird nur der Teil vor dem Gedankenstrich (siehe VERIFICATION.md). Ein eigenes Übersetzungsfeld gibt es nicht.

### So nutzt die App die Daten

1. **Laden.** Sie lädt `manifest.json` (optional), dann `entries.json` und `glossary.json`.
2. **Prüfen.** Sie kontrolliert:
   - die Daten sind ein JSON-Objekt;
   - `catalog_version` ist eine ganze Zahl und nicht niedriger als die Version in der App;
   - `entries` ist nicht leer und jede ID ist eindeutig;
   - die Pflichtfelder sind vorhanden;
   - Datumsangaben und URLs sind gültig;
   - jeder Wert liegt im erlaubten Bereich;
   - das Glossar ist nicht leer.
3. **Übernehmen.** Ein gültiger Katalog wird nur verwendet und zwischengespeichert, wenn seine `catalog_version` höher ist als die zuletzt gesehene. Fehlerhafte Daten überschreiben nie einen guten Zwischenspeicher.
4. **Zurückfallen.** Bei jedem Fehler behält die App still ihre zwischengespeicherte oder mitgelieferte Kopie. Das gilt für fehlendes Netz, 404, 5xx, ungültiges JSON, ein falsches Schema und eine ältere Version.

### Neuen Katalog veröffentlichen

1. `entries.json` bearbeiten. Für jedes neue Zitat eine Zeile in `VERIFICATION.md` ergänzen. **Niemals Zitate, Daten oder Fakten erfinden.**
2. `catalog_version` um 1 erhöhen, und zwar in **beiden** Dateien, `entries.json` und `manifest.json`. `updated` in beiden auf das heutige Datum setzen.
3. `python3 scripts/validate.py` ausführen und alle Fehler beheben.
4. Committen und nach `main` pushen. Die Apps übernehmen die Änderung beim nächsten Start oder Pull-to-Refresh. Der Raw-Cache von GitHub kann das um etwa 5 Minuten verzögern.
5. Nutzer mit Premium bekommen eine Mitteilung „neue Freigabe“ für den neuesten Eintrag.

### Aktueller Katalog

- `catalog_version` 5, Stand 27.10.2026
- 58 Einträge, 159 Zitate, alle geprüft (siehe VERIFICATION.md)
- 23 Glossarbegriffe
- Neu in v5:
  - PURSUE-Freigabe 07 (Department of War, 23. Oktober 2026)
  - Chile: SEFAA-Fallakten vom September 2026 (8. Oktober 2026)
  - Antwort der Bundesregierung auf eine Kleine Anfrage zu UAP (Drucksache 21/8662, 16. Oktober 2026)
  - Großbritannien: schriftliche Antwort des Verteidigungsministeriums zu einer Beinahe-Kollision eines RAF-Typhoon mit einem unbekannten Objekt (UIN 36199, 26. Oktober 2026)
  - erste Zitate in Originalsprache (Spanisch, Deutsch), jeweils mit inoffizieller englischer Übersetzung
  - aktualisiert: Zeitleisten-Zeile von pursue-release-06-2026, Hinweis bei pursue-nda-waiver-2026 („Stand Oktober 2026“)
- Neu in v4: `influence_breakdown` und Einflusswerte; `event_date` für magenta-1933
- Neu in v3:
  - PURSUE-Freigaben 02–05 (Department of War, Mai–August 2026)
  - deutsche Titel (`title_de`) für jeden Eintrag
