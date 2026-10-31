# Content verification log (catalog_version 5, 2026-10-27)

Internal file, not part of the app bundle (lives outside DisclosureApp/).

Method: every source_url was requested with curl (browser User-Agent); HTTP status and final URL below (entries of catalog v2 on 2026-10-17, the four entries added in v3 on 2026-10-18). Quotes were checked against text extracted from the fetched document (pdftotext for PDFs, BeautifulSoup for HTML).
Before comparing, curly quotes, dashes and whitespace were normalized, and words split by a line-end hyphen were rejoined. A quote counts as verified only if it then appears verbatim as a substring of the source text.
Tooling: /workspace/research on the build box (fetch.py, build/verify.py; v3 additions in build/part5_v3.py, build/build_v3.py, build/vermd_v3.py). It is not shipped.

Catalog v3 also adds `title_de` (German title) to every entry. Titles are translations of our own English titles, not quotes; quoted document names inside them stay in the original English.

Catalog v5 (2026-10-27) adds four entries, checked on 2026-10-27 (Europe/Berlin). Tooling: /workspace/ufo-research/verify/v5 on the build box (fetch.sh with browser headers, results.tsv fetch log, saved source texts). war.gov answers 403 to plain curl and WebFetch but 200 to curl with full browser headers. sefaa.dgac.gob.cl does not answer curl from the build box (000); it was read with the WebFetch tool and the quoted text saved.
Original-language quotes (v5): when no official English text exists, the quote `text` holds the verbatim original followed by ` — English: "…" (unofficial translation)`. Only the part before ` — English:` is checked verbatim; the translation is ours.
v5 also refreshes two existing texts (no new quotes): pursue-release-06-2026 `timeline_context`/`_de` and pursue-nda-waiver-2026 influence `note`/`note_de`.

Totals: 58 entries, 159/159 quotes verified verbatim.

| entry id | source_url status | quotes verified | notes |
|---|---|---|---|
| roswell-1947 | 200 | 3/3 yes | source_url is the FBI Vault Roswell file (holds the July 8, 1947 teletype). Its PDF scan has no usable text layer, so the quotes come from the GAO report, which describes the teletype and press releases. |
| project-sign-1948 | 200 | 2/2 yes | Date from the CIA history (Project SIGN "began its work on 23 January 1948"). |
| project-grudge-1949 | 200 | 2/2 yes | Date from the CIA history ("On 27 December 1949, the Air Force announced the project's termination"). |
| hottel-memo-1950 | 200 | 3/3 yes |  |
| washington-radar-1952 | 200 | 3/3 yes | Date = first night of the radar sightings (19-20 July 1952) per the CIA history. |
| robertson-panel-1953 | 200 (JS bot challenge on document) | 2/2 yes | source_url is the CIA Reading Room record of the panel report. It loads (HTTP 200), but a JavaScript bot challenge blocks scripted reads of the document, so the panel text could not be read. All quotes are from the CIA's own history (Haines 1997) and are attributed to it. Date uses month precision (January 1953); the exact report date was not verified. |
| house-armed-services-1966 | 200 | 3/3 yes | govinfo details page; quotes are from the govinfo PDF (scanned, OCR). The first quote matched only after ignoring whitespace: the OCR text has "attached,I believe", rendered here with the normal space. |
| house-symposium-1968 | 200 | 2/2 yes | govinfo details page; quotes are from the govinfo PDF (scanned, OCR). |
| condon-report-1969 | 200 | 3/3 yes | Year precision: the CIA history says the report was released in April 1969, other accounts say January 1969. The DTIC copy (AD0680975) was under maintenance; NCAS hosts the full text. |
| project-blue-book-1969 | 200 | 3/3 yes |  |
| rendlesham-1980 | 200 | 3/3 yes | Month precision (December 1980, per The National Archives). The TNA catalogue record for DEFE 24/1948/1 returns a bot challenge (HTTP 202), so the TNA UFO-reports collection page, which describes the file, is used. The Halt memo itself was not fetched. |
| foia-mj12-1980s | 200 | 2/2 yes | Marked as a CLAIM with a low score. Date = September 15, 1988, when Air Force OSI contacted FBI Dallas (FBI file). The quote describing the document as "completely bogus" comes from the archived FBI FOIA reading-room index (2005, Wayback Machine). The current Vault page has no such summary text. |
| belgian-wave-1990 | 200 | 2/2 yes | No official Belgian source found online; this uses the UK National Archives description of MoD file DEFE 24/1958/1. Score reduced for the secondhand source. |
| gao-roswell-1995 | 200 | 2/2 yes | gao.gov product page loads; quotes are from the govinfo full text of the same report. |
| cia-ufo-history-1997 | 200 | 3/3 yes | Year precision (1997). Quotes were verified against the archived CIA HTML of the same article, because the cia.gov PDF text layer is column-scrambled. |
| roswell-case-closed-1997 | 200 | 3/3 yes | Year precision (1997); exact release day not verified. |
| phoenix-lights-1997 | 200 | 3/3 yes | Previously sourced to Wikipedia; now an AP report from 1997 (Las Vegas Sun). |
| nimitz-tic-tac-2004 | 200 | 3/3 yes | Previously navy.mil homepage. Date 14 Nov 2004 from the UAPTF slide ("'Tic Tac' Case 14 Nov 2004") in Shellenberger's 2024 submitted statement; Fravor's statement says "Nov 2004". |
| theodore-roosevelt-2015 | 200 | 3/3 yes | Month precision (January 2015, per the DoD video statement and Gallaudet). The Gallaudet email-deletion claim is uncorroborated. |
| nytimes-aatip-2017 | 403 (blocks bots; URL correct) | 3/3 yes | nytimes.com blocks scripted fetches (403); the URL is correct and the text was verified on a Wayback Machine capture from Dec 31, 2017. |
| foia-navy-uap-guidelines | 403 (blocks bots; URL correct) | 2/2 yes | id kept for compatibility. Category changed to Media Investigation; previously navy.mil homepage. politico.com returns 403; verified via Wayback Machine. |
| dod-navy-videos-2020 | 200 | 3/3 yes | defense.gov now redirects to war.gov; the war.gov URL is used. |
| ssci-uap-report-request-2020 | 200 | 2/2 yes | congress.gov PDF loads. The report text breaks words with hyphens at line ends (e.g. "phe- nomenon"); the quotes were matched after joining them. |
| uaptf-established-2020 | 200 | 2/2 yes |  |
| uaptf-preliminary-2021 | 200 | 4/4 yes | Previously linked via dni.gov; the archive.dni.gov URL (redirect target) is used. |
| aoimsg-established-2021 | 200 | 2/2 yes |  |
| ndaa-fy2022-uap-office | 200 | 2/2 yes |  |
| house-hearing-2022 | 200 | 4/4 yes | Previously congress.gov homepage; now the official transcript PDF on docs.house.gov. |
| nasa-study-announced-2022 | 200 | 2/2 yes |  |
| aaro-established-2022 | 200 | 2/2 yes |  |
| ndaa-fy2023-reporting | 200 | 2/2 yes |  |
| odni-annual-2022 | 200 | 3/3 yes | archive.dni.gov PDF (redirect target of dni.gov). |
| sasc-aaro-hearing-2023 | 200 | 2/2 yes | The armed-services.senate.gov hearing page blocks curl; the govinfo transcript is used as source_url. |
| debrief-grusch-2023 | 200 | 3/3 yes |  |
| magenta-1933 | 403 (blocks bots; URL correct) | 3/3 yes | Marked as a CLAIM with a low score. Previously Wikipedia, dated 1933-06-13 (unverifiable day). Now dated to the June 2023 NewsNation interview where the claim was made (2023-06-11, from the article byline "Updated: Jun 11, 2023"). newsnationnow.com returns 403; quotes verified via Wayback Machine. Since catalog v4 the entry also has `event_date` 1933-01-01 with `event_date_precision` "year" (the year the claim refers to): the timeline groups it under the 1930s and shows "1933", while `date` (feed, detail, newest-entry logic) stays the claim date. |
| uap-disclosure-act-2023 | 403 (blocks bots; URL correct) | 3/3 yes | democrats.senate.gov returns 403 to curl, but the URL is correct. The page was read with the WebFetch tool and the quoted paragraphs saved for verification. |
| grusch-whistleblower-2023 | 200 | 4/4 yes | Previously congress.gov homepage. Hearing page on oversight.house.gov; quotes from Grusch's written statement (docs.house.gov) and the govinfo transcript. |
| nasa-uap-report-2023 | 200 | 3/3 yes |  |
| odni-annual-2023 | 200 | 2/2 yes | Uses the aaro.mil copy because the dni.gov FY23 PDF is image-only. Month precision: the report cover says "October 2023"; exact release day not verified. |
| ndaa-fy2024-uap-records | 200 | 2/2 yes |  |
| aaro-historical-2024 | 200 | 3/3 yes | Previously aaro.mil homepage; now the report PDF. Date 2024-03-08 = public release (Pentagon statement of March 8, 2024). |
| house-hearing-2024 | 200 | 4/4 yes | Hearing page on oversight.house.gov; quotes from the written statements on docs.house.gov. |
| aaro-annual-2024 | 200 | 3/3 yes |  |
| sasc-aaro-hearing-2024 | 200 | 3/3 yes |  |
| house-task-force-hearing-2025 | 200 | 4/4 yes | Hearing page on oversight.house.gov; quotes from the govinfo transcript CHRG-119hhrg61718. The video Rep. Burlison showed is not authenticated in the record. |
| pursue-directive-2026 | 200 | 3/3 yes | Date from the "[02 19 26]" stamp on war.gov/UFO. |
| pursue-release-01-2026 | 200 | 3/3 yes |  |
| pursue-release-02-2026 | 200 | 3/3 yes | Added in catalog v3 (checked 2026-10-18). Date, file counts and contents: war.gov release + war.gov/UFO ("RELEASE 02: CLEARED FOR RELEASE - MAY 22, 2026"), CBS News (64 files: 6 PDFs, 7 audio, 51 videos). Officer quotes from the primary PDF ODNI-UAP-D001 (a May 26, 2026 correction note in the PDF fixes "map-of-the-earth" to "nap-of-the-earth"; not quoted). |
| pursue-release-03-2026 | 200 | 3/3 yes | Added in catalog v3 (checked 2026-10-18). File counts from CBS News (53 documents, 10 images, 6 videos, 3 audio = 72). AARO memo quotes from the primary PDF DOW-UAP-D077. The memo says six agents; CBS describes five narratives. The summary follows the memo. |
| pursue-release-04-2026 | 200 | 3/3 yes | Added in catalog v3 (checked 2026-10-18). File counts from CBS News (14 documents, 19 videos, 4 audio, 3 images = 40). The Pantex report is internally inconsistent on the day (cover: September 2, 2015; narrative: September 1, 2015), so the summary says September 2015. |
| aaro-annual-2025 | 200 | 3/3 yes | Date = "Date Added" on the aaro.mil Congressional/Press Products page (July 20, 2026); the report's information cut-off is May 30, 2025. |
| pursue-release-05-2026 | 200 | 3/3 yes | Added in catalog v3 (checked 2026-10-18). 41 files and agencies per CBS News. The two IIR quotes were matched against the CBS article, which quotes the report; the primary PDF DOW-UAP-D101 is a scan whose OCR text has the same sentences with OCR errors, so a verbatim match against it is impossible. The second quote ends without the period because CBS embeds it mid-sentence. Bahia 1963 cable content checked against DOS-UAP-D001 (scan, read manually; not quoted). |
| pursue-nda-waiver-2026 | 200 | 3/3 yes |  |
| pursue-release-06-2026 | 200 | 3/3 yes | The DIRD details come from CBS News; the war.gov release itself is a short statement. |
| pursue-release-07-2026 | 200 | 3/3 yes | Added in catalog v5 (checked 2026-10-27). war.gov release 4632058 (200 with browser headers). Quotes 2–3 from the primary PDF DOW-UAP-D176 (AARO MFR, 200). FBI FD-302 FBI-UAP-D043 (200) read for the summary, not quoted; its ~3-second duration differs from the AARO memo's longer phases. "28 PDF files", "national security site in the western U.S." and AARO's "further investigation" assessment are from CBS News (not in the D176 text). |
| sefaa-chile-cases-sep-2026 | WebFetch OK (curl 000) | 2/2 yes | Added in catalog v5 (checked 2026-10-27). Spanish originals with unofficial English translations. Quote 1 from the case page; quote 2 from case file PDF 2288 (first read 2026-10-27; a re-fetch at 06:42 returned HTTP 500, the re-check at about 06:47 returned the document again with the same text). The PDF of case 2289 wrongly says "Caso N°: 2288" in its header. |
| bundestag-uap-answer-2026 | 200 | 3/3 yes | Added in catalog v5 (checked 2026-10-27). German originals with unofficial English translations, from Drucksache 21/8662 (dated 16.10.2026). Question: Drucksache 21/8323 (02.10.2026, 200). |
| uk-mod-typhoon-airprox-2026 | WebFetch OK; Parliament API 200 | 2/2 yes | Added in catalog v5 (checked 2026-10-27). Quote 1 from the written answer (UIN 36199). Quote 2 from the UK Airprox Board April 2026 drone summary PDF (200), row 2026014; the same standard wording appears in other rows. event_date 2026-02-23 = date of the airprox. |

## Quote-level detail

### roswell-1947
- source_url: https://vault.fbi.gov/Roswell%20UFO
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/GAOREPORTS-NSIAD-95-187/html/GAOREPORTS-NSIAD-95-187.htm - govinfo full text of the GAO report
  > On July 8, 1947, the Roswell Army Air Field (RAAF) public information office in Roswell, New Mexico, reported the crash and recovery of a "flying disc."
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/GAOREPORTS-NSIAD-95-187/html/GAOREPORTS-NSIAD-95-187.htm - govinfo full text of the GAO report
  > The following day, the press reported that the Commanding General of the U.S. Eighth Air Force, Fort Worth, Texas, announced that RAAF personnel had recovered a crashed radar-tracking (weather) balloon, not a "flying disc."
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/GAOREPORTS-NSIAD-95-187/html/GAOREPORTS-NSIAD-95-187.htm - govinfo full text of the GAO report
  > The FBI message stated that the military had reported that an object resembling a high-altitude weather balloon with a radar reflector had been recovered near Roswell.

### project-sign-1948
- source_url: https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-40-no-5/the-cias-role-in-the-study-of-ufos-1947-90/
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > The Technical Intelligence Division of the Air Material Command (AMC) at Wright Field (later Wright-Patterson Air Force Base) in Dayton, Ohio, assumed control of Project SIGN and began its work on 23 January 1948.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > Although at first fearful that the objects might be Soviet secret weapons, the Air Force soon concluded that UFOs were real but easily explained and not extraordinary.

### project-grudge-1949
- source_url: https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-40-no-5/the-cias-role-in-the-study-of-ufos-1947-90/
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > GRUDGE officials found no evidence in UFO sightings of advanced foreign weapons design or development, and they concluded that UFOs did not threaten US security.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > They recommended that the project be reduced in scope because the very existence of Air Force official interest encouraged people to believe in UFOs and contributed to a "war hysteria" atmosphere.

### hottel-memo-1950
- source_url: https://www.fbi.gov/news/stories/ufos-and-the-guy-hottel-memo
- quote verified: yes. Checked against https://www.fbi.gov/news/stories/ufos-and-the-guy-hottel-memo
  > A single-page March 22, 1950 memo by Guy Hottel, special agent in charge of the Washington Field Office, regarding UFOs is the most viewed document in the FBI Vault, our online repository of public records.
- quote verified: yes. Checked against https://www.fbi.gov/news/stories/ufos-and-the-guy-hottel-memo
  > Finally, the Hottel memo does not prove the existence of UFOs; it is simply a second- or third-hand claim that we never investigated.
- quote verified: yes. Checked against https://www.fbi.gov/news/stories/ufos-and-the-guy-hottel-memo
  > There is no reason to believe the two are connected.

### washington-radar-1952
- source_url: https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-40-no-5/the-cias-role-in-the-study-of-ufos-1947-90/
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > On 19 and 20 July, radar scopes at Washington National Airport and Andrews Air Force Base tracked mysterious blips. On 27 July, the blips reappeared. The Air Force scrambled interceptor aircraft to investigate, but they found nothing.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > since there is a remote possibility that they may be interplanetary aircraft, it is necessary to investigate each sighting.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > Project BLUE BOOK became the major Air Force effort to study the UFO phenomenon throughout the 1950s and 1960s.

### robertson-panel-1953
- source_url: https://www.cia.gov/readingroom/document/0005516124
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > The panel concluded unanimously that there was no evidence of a direct threat to national security in the UFO sightings. Nor could the panel find any evidence that the objects sighted might be extraterrestrials.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > It did find that continued emphasis on UFO reporting might threaten "the orderly functioning" of the government by clogging the channels of communication with irrelevant reports and by inducing "hysterical mass behavior" harmful to constituted authority.

### house-armed-services-1966
- source_url: https://www.govinfo.gov/app/details/CHRG-89hhrg50066O
- quote verified: yes (whitespace-insensitive match, OCR spacing). Checked against https://www.govinfo.gov/content/pkg/CHRG-89hhrg50066O/pdf/CHRG-89hhrg50066O.pdf - scanned hearing record, OCR text
  > Based upon 10,147 reported sightings from 1947 through 1965, a summary of which is attached, I believe it significant that the Air Force has succeeded in identifying 9,501 of these objects.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-89hhrg50066O/pdf/CHRG-89hhrg50066O.pdf - scanned hearing record, OCR text
  > We know of no phenomena or vehicles, intelligently guided, which have come from extraterrestrial sources.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-89hhrg50066O/pdf/CHRG-89hhrg50066O.pdf - scanned hearing record, OCR text
  > It is entirely conceivable that there might be unidentified aerial phenomena about us which have no connection with extraterrestrial visitation.

### house-symposium-1968
- source_url: https://www.govinfo.gov/app/details/CHRG-90hhrg97818
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-90hhrg97818/pdf/CHRG-90hhrg97818.pdf - scanned hearing record, OCR text
  > I have interviewed several hundred witnesses in selected cases, and I am astonished at what I have found.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-90hhrg97818/pdf/CHRG-90hhrg97818.pdf - scanned hearing record, OCR text
  > I do not think the evidence is at all persuasive, that UFO's are of intelligent extraterrestrial origin nor do I think the evidence is convincing that no UFO's are of intelligent extraterrestrial origin.

### condon-report-1969
- source_url: https://condon.ncas.org/text/sec-i.htm
- quote verified: yes. Checked against https://condon.ncas.org/text/sec-i.htm - NCAS full-text edition of the Condon Report; DTIC copy (AD0680975) was under maintenance
  > Our general conclusion is that nothing has come from the study of UFOs in the past 21 years that has added to scientific knowledge.
- quote verified: yes. Checked against https://condon.ncas.org/text/sec-i.htm - NCAS full-text edition of the Condon Report; DTIC copy (AD0680975) was under maintenance
  > Careful consideration of the record as it is available to us leads us to conclude that further extensive study of UFOs probably cannot be justified in the expectation that science will be advanced thereby.
- quote verified: yes. Checked against https://condon.ncas.org/text/sec-i.htm - NCAS full-text edition of the Condon Report; DTIC copy (AD0680975) was under maintenance
  > we believe that any scientist with adequate training and credentials who does come up with a clearly defined, specific proposal for study should be supported.

### project-blue-book-1969
- source_url: https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104590/unidentified-flying-objects-and-air-force-project-blue-book/
- quote verified: yes. Checked against https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104590/unidentified-flying-objects-and-air-force-project-blue-book/ - needs browser User-Agent (plain curl 403)
  > Of a total of 12,618 sightings reported to Project Blue Book, 701 remained "unidentified."
- quote verified: yes. Checked against https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104590/unidentified-flying-objects-and-air-force-project-blue-book/ - needs browser User-Agent (plain curl 403)
  > There was no evidence submitted to or discovered by the Air Force that sightings categorized as "unidentified" represented technological developments or principles beyond the range of modern scientific knowledge
- quote verified: yes. Checked against https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104590/unidentified-flying-objects-and-air-force-project-blue-book/ - needs browser User-Agent (plain curl 403)
  > There was no evidence indicating that sightings categorized as "unidentified" were extraterrestrial vehicles.

### rendlesham-1980
- source_url: https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/
- quote verified: yes. Checked against https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/ - catalogue record pages (discovery.nationalarchives.gov.uk) return a bot challenge (HTTP 202)
  > Perhaps Britain's most well-known UFO event happened in December 1980 at a Royal Air Force (RAF) base in Suffolk.
- quote verified: yes. Checked against https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/ - catalogue record pages (discovery.nationalarchives.gov.uk) return a bot challenge (HTTP 202)
  > A note in response to a Parliamentary Question confirmed that there was nothing of defence interest in the alleged sighting.
- quote verified: yes. Checked against https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/ - catalogue record pages (discovery.nationalarchives.gov.uk) return a bot challenge (HTTP 202)
  > A single sheet report is the only record of the event itself held by The National Archives, though we hold various files concerning it, which are mostly enquiries from the public and press.

### foia-mj12-1980s
- source_url: https://vault.fbi.gov/Majestic%2012
- quote verified: yes. Checked against https://web.archive.org/web/20050105095253/http://foia.fbi.gov/foiaindex/majestic.htm - Archived FBI FOIA reading-room description of the MJ-12 file
  > This investigation was closed after it was learned that the document was completely bogus.
- quote verified: yes. Checked against https://www.fbi.gov/video-repository/inside-the-fbi-ufos-102921.mp4/view - FBI "Inside the FBI" episode page with transcript
  > Of course, it doesn't look right, it doesn't really look like a lot of classified documents.

### belgian-wave-1990
- source_url: https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/
- quote verified: yes. Checked against https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/ - catalogue record pages (discovery.nationalarchives.gov.uk) return a bot challenge (HTTP 202)
  > A major event occurred in 1990 over Belgium. On 30-31 March, large, unknown triangular-shaped objects were reported.
- quote verified: yes. Checked against https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/postwar/ufo-reports/ - catalogue record pages (discovery.nationalarchives.gov.uk) return a bot challenge (HTTP 202)
  > Radar reportedly tracked an unknown object over central Belgium, and the Belgian Air Force scrambled two F-16s. The pilots reported no sightings, and the object was not identified.

### gao-roswell-1995
- source_url: https://www.gao.gov/products/nsiad-95-187
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/GAOREPORTS-NSIAD-95-187/html/GAOREPORTS-NSIAD-95-187.htm - govinfo full text of the GAO report
  > only two government records originating in 1947 have been recovered regarding the Roswell incident
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/GAOREPORTS-NSIAD-95-187/html/GAOREPORTS-NSIAD-95-187.htm - govinfo full text of the GAO report
  > although some of the records concerning Roswell activities had been destroyed, there was no information available regarding when or under what authority the records were destroyed

### cia-ufo-history-1997
- source_url: https://www.cia.gov/resources/csi/static/cia-role-study-UFOs.pdf
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > What emerges from this examination is that, while Agency concern over UFOs was substantial until the early 1950s, CIA has since paid only limited and peripheral attention to the phenomena.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > over half of all UFO reports from the late 1950s through the 1960s were accounted for by manned reconnaissance flights (namely the U-2) over the United States.
- quote verified: yes. Checked against https://web.archive.org/web/20070509174747/https://www.cia.gov/csi/studies/97unclass/ufo.html - Archived CIA HTML of the Haines article (clean text). Same article as the cia.gov CSI page/PDF; the current PDF text layer is column-scrambled
  > This led the Air Force to make misleading and deceptive statements to the public in order to allay public fears and to protect an extraordinarily sensitive national security project.

### roswell-case-closed-1997
- source_url: https://www.af.mil/The-Roswell-Report/
- quote verified: yes. Checked against https://www.af.mil/The-Roswell-Report/
  > The 1994 Air Force report concluded that the predecessor to the U.S. Air Force, the U.S. Army Air Forces, recovered debris from an Army Air Forces balloon-borne research project code named MOGUL.
- quote verified: yes. Checked against https://www.af.mil/The-Roswell-Report/
  > "Aliens" observed in the New Mexico desert were actually anthropomorphic test dummies that were carried aloft by U.S. Air Force high altitude balloons for scientific research.
- quote verified: yes. Checked against https://www.af.mil/The-Roswell-Report/
  > Air Force activities which occurred over a period of many years have been consolidated and are now represented to have occurred in two or three days in July 1947.

### phoenix-lights-1997
- source_url: https://lasvegassun.com/news/1997/jul/25/military-now-says-flares-may-be-cause-of-mysteriou/
- quote verified: yes. Checked against https://lasvegassun.com/news/1997/jul/25/military-now-says-flares-may-be-cause-of-mysteriou/ - AP report in the Las Vegas Sun
  > That wouldn't appear to cover all the sightings reported that night, as many came from far north of Phoenix
- quote verified: yes. Checked against https://lasvegassun.com/news/1997/jul/25/military-now-says-flares-may-be-cause-of-mysteriou/ - AP report in the Las Vegas Sun
  > one hell of a light show
- quote verified: yes. Checked against https://lasvegassun.com/news/1997/jul/25/military-now-says-flares-may-be-cause-of-mysteriou/ - AP report in the Las Vegas Sun
  > If that is their explanation then they need to do a re-enactment so people can say that's what they saw or not what they saw

### nimitz-tic-tac-2004
- source_url: https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-FravorD-20230726.pdf
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-FravorD-20230726.pdf - written statement
  > As all 4 looked down we saw a small white Tic Tac shaped object
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-FravorD-20230726.pdf - written statement
  > There were no Rotors, No Rotor wash, or any visible flight control surfaces like wings.
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-FravorD-20230726.pdf - written statement
  > What is shocking is that the incident was never investigated, none of my crew were ever questioned, tapes were never taken

### theodore-roosevelt-2015
- source_url: https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-GallaudetPhDRearAdmiralUSNavyRetT-20241113.pdf
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-GallaudetPhDRearAdmiralUSNavyRetT-20241113.pdf - written statement
  > Attached to the email was what is now known as the "Go Fast" video
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-GallaudetPhDRearAdmiralUSNavyRetT-20241113.pdf - written statement
  > The very next day, the email disappeared from my account and those of the other recipients without explanation.
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-GravesR-20230726.pdf - written statement
  > In 2014, I was near Virginia Beach as part of VFA-11, a Navy Fighter/Attack Squadron made up of F/A-18F Super Hornets. Upon an upgrade to our radar system, we began to detect unknown objects in our airspace.

### nytimes-aatip-2017
- source_url: https://www.nytimes.com/2017/12/16/us/politics/pentagon-program-ufo-harry-reid.html
- quote verified: yes. Checked against https://web.archive.org/web/20171231163831/https://www.nytimes.com/2017/12/16/us/politics/pentagon-program-ufo-harry-reid.html - nytimes.com returns 403 to scripted fetches; verified via Wayback Machine
  > In the $600 billion annual Defense Department budgets, the $22 million spent on the Advanced Aerospace Threat Identification Program was almost impossible to find.
- quote verified: yes. Checked against https://web.archive.org/web/20171231163831/https://www.nytimes.com/2017/12/16/us/politics/pentagon-program-ufo-harry-reid.html - nytimes.com returns 403 to scripted fetches; verified via Wayback Machine
  > I'm not embarrassed or ashamed or sorry I got this thing going,
- quote verified: yes. Checked against https://web.archive.org/web/20171231163831/https://www.nytimes.com/2017/12/16/us/politics/pentagon-program-ufo-harry-reid.html - nytimes.com returns 403 to scripted fetches; verified via Wayback Machine
  > It was determined that there were other, higher priority issues that merited funding, and it was in the best interest of the DoD to make a change,

### foia-navy-uap-guidelines
- source_url: https://www.politico.com/story/2019/04/23/us-navy-guidelines-reporting-ufos-1375290
- quote verified: yes. Checked against https://web.archive.org/web/20220207202604/https://www.politico.com/story/2019/04/23/us-navy-guidelines-reporting-ufos-1375290 - politico.com returns 403 to scripted fetches; verified via Wayback Machine
  > There have been a number of reports of unauthorized and/or unidentified aircraft entering various military-controlled ranges and designated air space in recent years,
- quote verified: yes. Checked against https://web.archive.org/web/20220207202604/https://www.politico.com/story/2019/04/23/us-navy-guidelines-reporting-ufos-1375290 - politico.com returns 403 to scripted fetches; verified via Wayback Machine
  > the Navy is updating and formalizing the process by which reports of any such suspected incursions can be made to the cognizant authorities.

### dod-navy-videos-2020
- source_url: https://www.war.gov/News/Releases/Release/Article/2165713/statement-by-the-department-of-defense-on-the-release-of-historical-navy-videos/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2165713/statement-by-the-department-of-defense-on-the-release-of-historical-navy-videos/ - defense.gov URL redirects to war.gov
  > The Department of Defense has authorized the release of three unclassified Navy videos, one taken in November 2004 and the other two in January 2015, which have been circulating in the public domain after unauthorized releases in 2007 and 2017.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2165713/statement-by-the-department-of-defense-on-the-release-of-historical-navy-videos/ - defense.gov URL redirects to war.gov
  > DOD is releasing the videos in order to clear up any misconceptions by the public on whether or not the footage that has been circulating was real, or whether or not there is more to the videos.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2165713/statement-by-the-department-of-defense-on-the-release-of-historical-navy-videos/ - defense.gov URL redirects to war.gov
  > The aerial phenomena observed in the videos remain characterized as "unidentified."

### ssci-uap-report-request-2020
- source_url: https://www.congress.gov/116/crpt/srpt233/CRPT-116srpt233.pdf
- quote verified: yes. Checked against https://www.congress.gov/116/crpt/srpt233/CRPT-116srpt233.pdf - congress.gov PDFs load; congress.gov HTML pages are behind a bot challenge
  > The Committee supports the efforts of the Unidentified Aerial Phenomenon Task Force at the Office of Naval Intelligence to standardize collection and reporting on unidentified aerial phenomenon
- quote verified: yes. Checked against https://www.congress.gov/116/crpt/srpt233/CRPT-116srpt233.pdf - congress.gov PDFs load; congress.gov HTML pages are behind a bot challenge
  > the Committee finds that the information sharing and coordination across the Intelligence Community has been inconsistent, and this issue has lacked attention from senior leaders.

### uaptf-established-2020
- source_url: https://www.war.gov/News/Releases/Release/Article/2314065/establishment-of-unidentified-aerial-phenomena-task-force/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2314065/establishment-of-unidentified-aerial-phenomena-task-force/ - defense.gov URL redirects to war.gov
  > The Department of Defense established the UAPTF to improve its understanding of, and gain insight into, the nature and origins of UAPs.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2314065/establishment-of-unidentified-aerial-phenomena-task-force/ - defense.gov URL redirects to war.gov
  > The mission of the task force is to detect, analyze and catalog UAPs that could potentially pose a threat to U.S. national security.

### uaptf-preliminary-2021
- source_url: https://archive.dni.gov/files/ODNI/documents/assessments/Prelimary-Assessment-UAP-20210625.pdf
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Prelimary-Assessment-UAP-20210625.pdf - dni.gov URL redirects to archive.dni.gov
  > The limited amount of high-quality reporting on unidentified aerial phenomena (UAP) hampers our ability to draw firm conclusions about the nature or intent of UAP.
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Prelimary-Assessment-UAP-20210625.pdf - dni.gov URL redirects to archive.dni.gov
  > We were able to identify one reported UAP with high confidence. In that case, we identified the object as a large, deflating balloon. The others remain unexplained.
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Prelimary-Assessment-UAP-20210625.pdf - dni.gov URL redirects to archive.dni.gov
  > In 18 incidents, described in 21 reports, observers reported unusual UAP movement patterns or flight characteristics.
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Prelimary-Assessment-UAP-20210625.pdf - dni.gov URL redirects to archive.dni.gov
  > The UAPTF has 11 reports of documented instances in which pilots reported near misses with a UAP.

### aoimsg-established-2021
- source_url: https://www.war.gov/News/Releases/Release/Article/2853121/dod-announces-the-establishment-of-the-airborne-object-identification-and-manag/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2853121/dod-announces-the-establishment-of-the-airborne-object-identification-and-manag/ - defense.gov URL redirects to war.gov
  > Today, Deputy Secretary of Defense Kathleen Hicks, in close collaboration with the Director of National Intelligence, directed the Under Secretary of Defense for Intelligence & Security to establish within the Office of the USD(I&S) the Airborne Object Identification and Management Synchronization Group (AOIMSG) as the successor to the U.S. Navy's Unidentified Aerial Phenomena Task Force.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/2853121/dod-announces-the-establishment-of-the-airborne-object-identification-and-manag/ - defense.gov URL redirects to war.gov
  > Incursions by any airborne object into our SUA pose safety of flight and operations security concerns, and may pose national security challenges.

### ndaa-fy2022-uap-office
- source_url: https://www.govinfo.gov/content/pkg/PLAW-117publ81/html/PLAW-117publ81.htm
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/PLAW-117publ81/html/PLAW-117publ81.htm
  > Developing procedures to synchronize and standardize the collection, reporting, and analysis of incidents, including adverse physiological effects, regarding unidentified aerial phenomena across the Department of Defense and the intelligence community
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/PLAW-117publ81/html/PLAW-117publ81.htm
  > Evaluating the threat that such incidents present to the United States.

### house-hearing-2022
- source_url: https://docs.house.gov/meetings/IG/IG05/20220517/114761/HHRG-117-IG05-Transcript-20220517.pdf
- quote verified: yes. Checked against https://docs.house.gov/meetings/IG/IG05/20220517/114761/HHRG-117-IG05-Transcript-20220517.pdf - official transcript
  > Unidentified aerial phenomena are a potential national security threat, and they need to be treated that way.
- quote verified: yes. Checked against https://docs.house.gov/meetings/IG/IG05/20220517/114761/HHRG-117-IG05-Transcript-20220517.pdf - official transcript
  > For too long the stigma associated with UAPs has gotten in the way of good intelligence analysis.
- quote verified: yes. Checked against https://docs.house.gov/meetings/IG/IG05/20220517/114761/HHRG-117-IG05-Transcript-20220517.pdf - official transcript
  > Since the release of that preliminary report, UAP database has now grown to contain approximately 400 reports. The stigma has been reduced.
- quote verified: yes. Checked against https://docs.house.gov/meetings/IG/IG05/20220517/114761/HHRG-117-IG05-Transcript-20220517.pdf - official transcript
  > So we are open to all hypotheses. We are open to any conclusions that we may encounter.

### nasa-study-announced-2022
- source_url: https://science.nasa.gov/uap/
- quote verified: yes. Checked against https://science.nasa.gov/uap/
  > On June 9, 2022, NASA announced that the agency is commissioning a study team to examine unidentified anomalous phenomena (UAPs)
- quote verified: yes. Checked against https://science.nasa.gov/uap/
  > The study will focus on identifying available data, how best to collect future data, and how NASA can use that data to move the scientific understanding of UAPs forward.

### aaro-established-2022
- source_url: https://www.war.gov/News/Releases/Release/Article/3100053/dod-announces-the-establishment-of-the-all-domain-anomaly-resolution-office/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/3100053/dod-announces-the-establishment-of-the-all-domain-anomaly-resolution-office/
  > The mission of the AARO will be to synchronize efforts across the Department of Defense, and with other U.S. federal departments and agencies, to detect, identify and attribute objects of interest in, on or near military installations, operating areas, training areas, special use airspace and other areas of interest
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/3100053/dod-announces-the-establishment-of-the-all-domain-anomaly-resolution-office/
  > This includes anomalous, unidentified space, airborne, submerged and transmedium objects.

### ndaa-fy2023-reporting
- source_url: https://www.govinfo.gov/content/pkg/PLAW-117publ263/html/PLAW-117publ263.htm
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/PLAW-117publ263/html/PLAW-117publ263.htm
  > any activity or program by a department or agency of the Federal Government or a contractor of such a department or agency relating to unidentified anomalous phenomena, including with respect to material retrieval, material analysis, reverse engineering, research and development, detection and tracking, developmental or operational testing, and security protections and enforcement.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/PLAW-117publ263/html/PLAW-117publ263.htm
  > regardless of the classification of information contained in the disclosure or any nondisclosure agreements

### odni-annual-2022
- source_url: https://archive.dni.gov/files/ODNI/documents/assessments/Unclassified-2022-Annual-Report-UAP.pdf
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Unclassified-2022-Annual-Report-UAP.pdf - dni.gov URL redirects to archive.dni.gov
  > This totals 510 UAP reports as of 30 August 2022.
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Unclassified-2022-Annual-Report-UAP.pdf - dni.gov URL redirects to archive.dni.gov
  > Some of these uncharacterized UAP appear to have demonstrated unusual flight characteristics or performance capabilities, and require further analysis.
- quote verified: yes. Checked against https://archive.dni.gov/files/ODNI/documents/assessments/Unclassified-2022-Annual-Report-UAP.pdf - dni.gov URL redirects to archive.dni.gov
  > partially due to reduced stigma surrounding UAP reporting

### sasc-aaro-hearing-2023
- source_url: https://www.govinfo.gov/content/pkg/CHRG-118shrg60390/html/CHRG-118shrg60390.htm
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-118shrg60390/html/CHRG-118shrg60390.htm - official hearing transcript (govinfo)
  > I want to underscore today that only a very small percentage of UAP reports display signatures that could reasonably be described as anomalous.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-118shrg60390/html/CHRG-118shrg60390.htm - official hearing transcript (govinfo)
  > in our research AARO, has found no credible evidence thus far of extraterrestrial activity, off-world technology, or objects that defy the known laws of physics.

### debrief-grusch-2023
- source_url: https://thedebrief.org/intelligence-officials-say-u-s-has-retrieved-non-human-craft/
- quote verified: yes. Checked against https://thedebrief.org/intelligence-officials-say-u-s-has-retrieved-non-human-craft/
  > A former intelligence official turned whistleblower has given Congress and the Intelligence Community Inspector General extensive classified information about deeply covert programs that he says possess retrieved intact and partially intact craft of non-human origin.
- quote verified: yes. Checked against https://thedebrief.org/intelligence-officials-say-u-s-has-retrieved-non-human-craft/
  > We are not talking about prosaic origins or identities,
- quote verified: yes. Checked against https://thedebrief.org/intelligence-officials-say-u-s-has-retrieved-non-human-craft/
  > The material includes intact and partially intact vehicles.

### magenta-1933
- source_url: https://www.newsnationnow.com/space/ufo/we-are-not-alone-the-ufo-whistleblower-speaks/
- quote verified: yes. Checked against https://web.archive.org/web/20240103070635/https://www.newsnationnow.com/space/ufo/we-are-not-alone-the-ufo-whistleblower-speaks/ - newsnationnow.com returns 403 to scripted fetches; verified via Wayback Machine
  > In 1933 was the first recovery in Europe and in Magenta, Italy,
- quote verified: yes. Checked against https://web.archive.org/web/20240103070635/https://www.newsnationnow.com/space/ufo/we-are-not-alone-the-ufo-whistleblower-speaks/ - newsnationnow.com returns 403 to scripted fetches; verified via Wayback Machine
  > They recovered a partially intact vehicle.
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/AARO_Historical_Record_Report_Vol_1_2024.pdf - PDF text via pdftotext
  > AARO found no empirical evidence for claims that the USG and private companies have been reverse-engineering extraterrestrial technology.

### uap-disclosure-act-2023
- source_url: https://www.democrats.senate.gov/newsroom/press-releases/leader-schumer-senator-rounds-introduce-new-legislation-to-declassify-government-records-related-to-unidentified-anomalous-phenomena-and-ufos_modeled-after-jfk-assassination-records-collection-act--part-of-ndaa
- quote verified: yes. Checked against https://www.democrats.senate.gov/newsroom/press-releases/leader-schumer-senator-rounds-introduce-new-legislation-to-declassify-government-records-related-to-unidentified-anomalous-phenomena-and-ufos_modeled-after-jfk-assassination-records-collection-act--part-of-ndaa - returns 403 to curl; text read with the WebFetch tool on 2026-10-17
  > The American public has a right to learn about technologies of unknown origins, non-human intelligence, and unexplainable phenomena.
- quote verified: yes. Checked against https://www.democrats.senate.gov/newsroom/press-releases/leader-schumer-senator-rounds-introduce-new-legislation-to-declassify-government-records-related-to-unidentified-anomalous-phenomena-and-ufos_modeled-after-jfk-assassination-records-collection-act--part-of-ndaa - returns 403 to curl; text read with the WebFetch tool on 2026-10-17
  > Relevant documents related to this issue should be preserved.
- quote verified: yes. Checked against https://www.democrats.senate.gov/newsroom/press-releases/leader-schumer-senator-rounds-introduce-new-legislation-to-declassify-government-records-related-to-unidentified-anomalous-phenomena-and-ufos_modeled-after-jfk-assassination-records-collection-act--part-of-ndaa - returns 403 to curl; text read with the WebFetch tool on 2026-10-17
  > the federal government shall have eminent domain over any and all recovered technologies of unknown origin (TUO) and biological evidence of non-human intelligence (NHI) that may be controlled by private persons or entities in the interests of the public good.

### grusch-whistleblower-2023
- source_url: https://oversight.house.gov/hearing/unidentified-anomalous-phenomena-implications-on-national-security-public-safety-and-government-transparency/
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-GruschD-20230726.pdf - written statement
  > I was informed, in the course of my official duties, of a multi-decade UAP crash retrieval and reverse engineering program to which I was denied access to those additional read-on's.
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO06/20230726/116282/HHRG-118-GO06-Wstate-GruschD-20230726.pdf - written statement
  > But as I stand here under oath now, I am speaking to the facts as I have been told them.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-118hhrg53022/pdf/CHRG-118hhrg53022.pdf - official hearing transcript (govinfo)
  > I have to be careful to describe what I have seen firsthand and not in this environment.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-118hhrg53022/pdf/CHRG-118hhrg53022.pdf - official hearing transcript (govinfo)
  > That is something I have not witnessed myself.

### nasa-uap-report-2023
- source_url: https://www.nasa.gov/wp-content/uploads/2023/09/uap-independent-study-team-final-report-0.pdf
- quote verified: yes. Checked against https://www.nasa.gov/wp-content/uploads/2023/09/uap-independent-study-team-final-report-0.pdf - PDF text via pdftotext
  > At this point there is no reason to conclude that existing UAP reports have an extraterrestrial source.
- quote verified: yes. Checked against https://www.nasa.gov/wp-content/uploads/2023/09/uap-independent-study-team-final-report-0.pdf - PDF text via pdftotext
  > the absence of consistent, detailed, and curated observations means we do not presently have the body of data needed to make definitive, scientific conclusions about UAP.
- quote verified: yes. Checked against https://www.nasa.gov/news-release/update-nasa-shares-uap-independent-study-report-names-director/ - NASA news release
  > At NASA, it's in our DNA to explore - and to ask why things are the way they are.

### odni-annual-2023
- source_url: https://www.aaro.mil/Portals/136/PDFs/UNCLASSIFIED-FY23_Consolidated_Annual_Report_on_UAP-Oct_25_2023_1236.pdf
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/UNCLASSIFIED-FY23_Consolidated_Annual_Report_on_UAP-Oct_25_2023_1236.pdf - aaro.mil copy; the dni.gov FY23 PDF is image-only (no text layer)
  > The All-domain Anomaly Resolution Office (AARO) received a total of 291 UAP reports during this period, consisting of 274 that occurred during this period and another 17 that occurred during previous reporting periods from 2019-2022
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/UNCLASSIFIED-FY23_Consolidated_Annual_Report_on_UAP-Oct_25_2023_1236.pdf - aaro.mil copy; the dni.gov FY23 PDF is image-only (no text layer)
  > the unidentified and purported anomalous nature of most UAP will likely resolve to ordinary phenomena

### ndaa-fy2024-uap-records
- source_url: https://www.govinfo.gov/content/pkg/PLAW-118publ31/html/PLAW-118publ31.htm
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/PLAW-118publ31/html/PLAW-118publ31.htm - quote begins after a [[Page]] marker
  > Government-funded records relating to unidentified anomalous phenomena, technologies of unknown origin, and non-human intelligence
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/PLAW-118publ31/html/PLAW-118publ31.htm - quote begins after a [[Page]] marker
  > None of the funds authorized to be appropriated or otherwise made available by this division may be obligated or expended in support of any activity involving unidentified anomalous phenomena

### aaro-historical-2024
- source_url: https://www.aaro.mil/Portals/136/PDFs/AARO_Historical_Record_Report_Vol_1_2024.pdf
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/AARO_Historical_Record_Report_Vol_1_2024.pdf - PDF text via pdftotext
  > AARO found no evidence that any USG investigation, academic-sponsored research, or official review panel has confirmed that any sighting of a UAP represented extraterrestrial technology.
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/AARO_Historical_Record_Report_Vol_1_2024.pdf - PDF text via pdftotext
  > AARO found no empirical evidence for claims that the USG and private companies have been reverse-engineering extraterrestrial technology.
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/AARO_Historical_Record_Report_Vol_1_2024.pdf - PDF text via pdftotext
  > AARO determined, based on all information provided to date, that claims involving specific people, known locations, technological tests, and documents allegedly involved in or related to the reverse-engineering of extraterrestrial technology, are inaccurate.

### house-hearing-2024
- source_url: https://oversight.house.gov/hearing/unidentified-anomalous-phenomena-exposing-the-truth/
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-ElizondoL-20241113.pdf - written statement
  > Let me be clear: UAP are real. Advanced technologies not made by our Government - or any other government - are monitoring sensitive military installations around the globe.
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-ElizondoL-20241113.pdf - written statement
  > Furthermore, the U.S. is in possession of UAP technologies, as are some of our adversaries.
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-ShellenbergerM-20241113.pdf - submitted statement
  > The whistleblower alleges that the DOD created the USAP, called "Immaculate Constellation," in 2017 after the New York Times published an article describing an informal Pentagon UAP program called "Advanced Aerospace Threat Identification Program," or AATIP.
- quote verified: yes. Checked against https://docs.house.gov/meetings/GO/GO12/20241113/117721/HHRG-118-GO12-Wstate-GoldM-20241113.pdf - written statement
  > Unfortunately, for decades this topic has been suffering from a stigma that has prevented much needed study and public discourse.

### aaro-annual-2024
- source_url: https://media.defense.gov/2024/Nov/14/2003583603/-1/-1/0/FY24-CONSOLIDATED-ANNUAL-REPORT-ON-UAP-508.PDF
- quote verified: yes. Checked against https://media.defense.gov/2024/Nov/14/2003583603/-1/-1/0/FY24-CONSOLIDATED-ANNUAL-REPORT-ON-UAP-508.PDF - PDF text via pdftotext
  > The All-domain Anomaly Resolution Office (AARO) received 757 UAP reports during this period; 485 of these reports featured UAP incidents that occurred during the reporting period.
- quote verified: yes. Checked against https://media.defense.gov/2024/Nov/14/2003583603/-1/-1/0/FY24-CONSOLIDATED-ANNUAL-REPORT-ON-UAP-508.PDF - PDF text via pdftotext
  > AARO determined 21 cases merit further analysis by its IC and science and technology (S&T) partners.
- quote verified: yes. Checked against https://media.defense.gov/2024/Nov/14/2003583603/-1/-1/0/FY24-CONSOLIDATED-ANNUAL-REPORT-ON-UAP-508.PDF - PDF text via pdftotext
  > It is important to underscore that, to date, AARO has discovered no evidence of extraterrestrial beings, activity, or technology.

### sasc-aaro-hearing-2024
- source_url: https://www.aaro.mil/Portals/136/PDFs/Dr_Jon_Kosloski_Statement_for_the_Record_SASC_Open_Hearing_Nov2024.pdf
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/Dr_Jon_Kosloski_Statement_for_the_Record_SASC_Open_Hearing_Nov2024.pdf - statement for the record
  > Only a very small percentage of reports AARO receives are potentially anomalous
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/Dr_Jon_Kosloski_Statement_for_the_Record_SASC_Open_Hearing_Nov2024.pdf - statement for the record
  > It is important to underscore that, to date, AARO has discovered no verifiable evidence of extraterrestrial beings, activity, or technology.
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/Dr_Jon_Kosloski_Statement_for_the_Record_SASC_Open_Hearing_Nov2024.pdf - statement for the record
  > there should be zero stigma associated with UAP reporting.

### house-task-force-hearing-2025
- source_url: https://oversight.house.gov/hearing/restoring-public-trust-through-uap-transparency-and-whistleblower-protection/
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-119hhrg61718/html/CHRG-119hhrg61718.htm - official hearing transcript (govinfo)
  > For too long, the issue of unidentified anomalous phenomena, commonly known as UAPs, has been shrouded in secrecy, stigma, and in some cases outright dismissal.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-119hhrg61718/html/CHRG-119hhrg61718.htm - official hearing transcript (govinfo)
  > Between 2003 and 2005, five UAP incidents occurred at Vandenberg Air Force Base
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-119hhrg61718/html/CHRG-119hhrg61718.htm - official hearing transcript (govinfo)
  > What I observed and what our crew recorded was not consistent with conventional aircraft or drones as they appeared on our system.
- quote verified: yes. Checked against https://www.govinfo.gov/content/pkg/CHRG-119hhrg61718/html/CHRG-119hhrg61718.htm - official hearing transcript (govinfo)
  > This video is of an MQ-9 drone tracking an orb, or this object, off the coast of Yemen.

### pursue-directive-2026
- source_url: https://www.war.gov/UFO/
- quote verified: yes. Checked against https://www.war.gov/UFO/
  > I will be directing the Secretary of War, and other relevant Departments and Agencies, to begin the process of identifying and releasing Government files related to alien and extraterrestrial life, unidentified aerial phenomena (UAP), and unidentified flying objects (UFOs)
- quote verified: yes. Checked against https://www.war.gov/UFO/
  > The materials archived here are unresolved cases, meaning the government is unable to make a definitive determination on the nature of the observed phenomena.
- quote verified: yes. Checked against https://www.war.gov/UFO/
  > This is an unprecedented, historic undertaking that requires coordination between dozens of agencies and the review of tens of millions of records, many existing only on paper, spanning many decades.

### pursue-release-01-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/
  > While all of the files have been reviewed for security purposes, many of the materials have not yet been analyzed for resolution of any anomalies.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/
  > These files, hidden behind classifications, have long fueled justified speculation - and it's time the American people see it for themselves.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/
  > We will remain candid about what we know to be true, what we have yet to understand, and all that remains to be discovered.

### pursue-release-02-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/
  > Today, the Department of War is publishing the second release of declassified and historical Unidentified Anomalous Phenomena (UAP) files as part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE).
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/052226/release_02/documents/ODNI-UAP-D001_USPER_Narrative_Senior_USIC.pdf - Release 02 document ODNI-UAP-D001 on war.gov, PDF text via pdftotext
  > What followed was a series of close UAP encounters lasting over an hour.
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/052226/release_02/documents/ODNI-UAP-D001_USPER_Narrative_Senior_USIC.pdf - Release 02 document ODNI-UAP-D001 on war.gov, PDF text via pdftotext
  > In the distance, we saw countless orange orbs swarming in all directions against the backdrop of the mountain.

### pursue-release-03-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4515408/department-of-war-publishes-third-release-of-unidentified-anomalous-phenomena-f/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4515408/department-of-war-publishes-third-release-of-unidentified-anomalous-phenomena-f/
  > Today, the Department of War is publishing the third release of declassified and historical Unidentified Anomalous Phenomena (UAP) files as part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE).
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/061226/release_03/documents/DOW-UAP-D077_Unresolved-Case-Analysis-Update_Western-United-States-Event.pdf - Release 03 document DOW-UAP-D077 on war.gov, PDF text via pdftotext
  > The reporting agents did not collect video footage, photographic imagery, or other technical data during the incident.
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/061226/release_03/documents/DOW-UAP-D077_Unresolved-Case-Analysis-Update_Western-United-States-Event.pdf - Release 03 document DOW-UAP-D077 on war.gov, PDF text via pdftotext
  > As of June 2026, the case remains unresolved.

### pursue-release-04-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4539898/department-of-war-publishes-fourth-release-of-unidentified-anomalous-phenomena/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4539898/department-of-war-publishes-fourth-release-of-unidentified-anomalous-phenomena/
  > Today, the Department of War is publishing the fourth release of declassified and historical Unidentified Anomalous Phenomena (UAP) files as part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE).
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/071026/release_04/documents/DOE-UAP-D005_Pantex-Unidentified-Object-Incident-Report_2015.pdf - Release 04 document DOE-UAP-D005 on war.gov, PDF text via pdftotext (scan with OCR layer)
  > Once outside, they noted that the object did not make any sound.
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/071026/release_04/documents/DOE-UAP-D005_Pantex-Unidentified-Object-Incident-Report_2015.pdf - Release 04 document DOE-UAP-D005 on war.gov, PDF text via pdftotext (scan with OCR layer)
  > It should be noted that at no time did the object appear to be threatening in nature nor did it come to close proximity to any sensitive assets.

### aaro-annual-2025
- source_url: https://www.aaro.mil/Portals/136/PDFs/FY25%20UAP%20Annual%20Report/AARO_FY2025_Consolidated_Annual_Report_on_UAP.pdf
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/FY25%20UAP%20Annual%20Report/AARO_FY2025_Consolidated_Annual_Report_on_UAP.pdf - PDF text via pdftotext
  > AARO resolved 114 of the 319 UAP reports.
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/FY25%20UAP%20Annual%20Report/AARO_FY2025_Consolidated_Annual_Report_on_UAP.pdf - PDF text via pdftotext
  > AARO assesses that all resolved cases are attributable to prosaic objects such as balloons, satellites, birds, aircraft, and unmanned aerial systems (UAS).
- quote verified: yes. Checked against https://www.aaro.mil/Portals/136/PDFs/FY25%20UAP%20Annual%20Report/AARO_FY2025_Consolidated_Annual_Report_on_UAP.pdf - PDF text via pdftotext
  > During the reporting period, AARO onboarded a new capability that enabled analysts to resolve 238 reported UAP as satellite flaring.

### pursue-release-05-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4565994/department-of-war-publishes-fifth-release-of-unidentified-anomalous-phenomena-f/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4565994/department-of-war-publishes-fifth-release-of-unidentified-anomalous-phenomena-f/
  > Today, the Department of War is publishing the fifth release of declassified and historical Unidentified Anomalous Phenomena (UAP) files as part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE).
- quote verified: yes. Checked against https://www.cbsnews.com/news/ufo-files-pentagon-5th-release-documents-videos/ - CBS News article (Aug 7, 2026) quoting the IIR; the war.gov PDF of DOW-UAP-D101 is a scan whose OCR layer contains the same sentences with OCR errors (e.g. "coJcl orbs", "airer.aft"), so it cannot be matched verbatim
  > The UAPs were observed as cold orbs flying at lower altitudes between 250 to 1300 MPH in different formations as well as maneuvering aggressively.
- quote verified: yes. Checked against https://www.cbsnews.com/news/ufo-files-pentagon-5th-release-documents-videos/ - CBS News article (Aug 7, 2026) quoting the IIR; the war.gov PDF of DOW-UAP-D101 is a scan whose OCR layer contains the same sentences with OCR errors (e.g. "coJcl orbs", "airer.aft"), so it cannot be matched verbatim
  > UAPs also appeared to react to the aircraft firing its main cannon

### pursue-nda-waiver-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4600020/department-of-war-issues-legal-waiver-to-authorize-unidentified-anomalous-pheno/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4600020/department-of-war-issues-legal-waiver-to-authorize-unidentified-anomalous-pheno/
  > This waiver establishes an authorized, legally protected disclosure mechanism for current and former personnel to provide UAP-related National Defense Information (NDI) to designated representatives of the PURSUE effort.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4600020/department-of-war-issues-legal-waiver-to-authorize-unidentified-anomalous-pheno/
  > The waiver supersedes civil and administrative enforcement provisions contained within Non-Disclosure Agreements (NDAs) and Special Access Program Indoctrination Agreements (SAPIAs) previously executed within the United States, strictly for communications directed to the PURSUE team.
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4600020/department-of-war-issues-legal-waiver-to-authorize-unidentified-anomalous-pheno/
  > Historically, individuals with direct knowledge of UAP-related programs cited concerns regarding potential legal liability, loss of clearances, or administrative prosecution stemming from standard NDAs and SAP indoctrination terms.

### pursue-release-06-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4604795/department-of-war-publishes-sixth-release-of-unidentified-anomalous-phenomena-f/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4604795/department-of-war-publishes-sixth-release-of-unidentified-anomalous-phenomena-f/
  > Today, the Department of War is publishing the sixth release of declassified and historical Unidentified Anomalous Phenomena (UAP) files as part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE).
- quote verified: yes. Checked against https://www.cbsnews.com/news/ufo-files-uap-pentagon-6th-release/ - CBS News article (Sept 18, 2026); used for Pentagon DIRD notes
  > best understood as reference and synthesis products rather than as original research
- quote verified: yes. Checked against https://www.cbsnews.com/news/ufo-files-uap-pentagon-6th-release/ - CBS News article (Sept 18, 2026); used for Pentagon DIRD notes
  > should not be read as implying current validation of the concepts discussed.

### pursue-release-07-2026
- source_url: https://www.war.gov/News/Releases/Release/Article/4632058/department-of-war-publishes-seventh-release-of-unidentified-anomalous-phenomena/
- quote verified: yes. Checked against https://www.war.gov/News/Releases/Release/Article/4632058/department-of-war-publishes-seventh-release-of-unidentified-anomalous-phenomena/
  > Today, the Department of War is publishing the seventh release of declassified and historical Unidentified Anomalous Phenomena (UAP) files as part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE).
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/release-07/documents/DOW-UAP-D176-Triangular_UAP_AARO_MFR_2026.pdf - AARO memorandum for the record (PURSUE D176)
  > This report reflects the reporter's interpretation at the time of the event.
- quote verified: yes. Checked against https://www.war.gov/medialink/ufo/release-07/documents/DOW-UAP-D176-Triangular_UAP_AARO_MFR_2026.pdf - AARO memorandum for the record (PURSUE D176)
  > matte black triangular shape of extremely low aspect ratio

### sefaa-chile-cases-sep-2026
- source_url: https://sefaa.dgac.gob.cl/2026/10/08/casos-septiembre-2026/
- quote verified: yes. Checked against https://sefaa.dgac.gob.cl/2026/10/08/casos-septiembre-2026/ (verbatim check covers the original-language part only; the English rendering is an unofficial translation)
  > Nuestras investigaciones se fundamentan en el método científico, por lo que dependen fuertemente de la disponibilidad de registros audiovisuales (audios, fotografías, videos).
- quote verified: yes. Checked against https://sefaa.dgac.gob.cl/wp-content/uploads/2026/10/CASO-N%C2%B02288-19092026.pdf - SEFAA case file 2288 (verbatim check covers the original-language part only; the English rendering is an unofficial translation)
  > Todo lo anterior llevó a la hipótesis de estar frente a una aeronave muy pequeña, de forma similar a un RPA/dron.

### bundestag-uap-answer-2026
- source_url: https://dserver.bundestag.de/btd/21/086/2108662.pdf
- quote verified: yes. Checked against https://dserver.bundestag.de/btd/21/086/2108662.pdf (verbatim check covers the original-language part only; the English rendering is an unofficial translation)
  > Über UAP liegen keine Erkenntnisse vor.
- quote verified: yes. Checked against https://dserver.bundestag.de/btd/21/086/2108662.pdf (verbatim check covers the original-language part only; the English rendering is an unofficial translation)
  > Für Meldungen zu UAP existieren keine gesonderten Meldewege.
- quote verified: yes. Checked against https://dserver.bundestag.de/btd/21/086/2108662.pdf (verbatim check covers the original-language part only; the English rendering is an unofficial translation)
  > Derzeit ist eine Überarbeitung bestehender Verfahren nicht geplant.

### uk-mod-typhoon-airprox-2026
- source_url: https://questions-statements.parliament.uk/written-questions/detail/2026-10-19/36199
- quote verified: yes. Checked against https://questions-statements.parliament.uk/written-questions/detail/2026-10-19/36199
  > DASORs are not intended to provide assessments of intent, ownership, attribution, or threat.
- quote verified: yes. Checked against https://www.airproxboard.org.uk/media/3ikpobnb/april-drone-summary-sheet.pdf - UK Airprox Board summary, row 2026014
  > In the Board's opinion the reported altitude and/or description of the object were such that they were unable to determine the nature of the unknown object.
