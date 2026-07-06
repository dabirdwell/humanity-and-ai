# Sprint Report: This Machine Press archive-of-record (Phase 1)

**Sprint:** tmp-phase1-site-jul5
**Repo:** humanity-and-ai-site (hai-site)
**Date:** 2026-07-05
**Section URL (on flip):** humanityandai.com/thismachine/
**Status:** Built, verified locally, committed (no push). Broadsheet I is **PENDING** (see gate below).

---

## GO/NO-GO gate result: Broadsheet I is PENDING

The gate required `GO_Broadsheets/Broadsheet_I_Pipeline_Report_2026-07-05.md` to exist and report zero em dashes with a resolved consultation before Broadsheet I could be imported.

**That report does not exist.** The Broadsheet I editorial pipeline sprint (`broadsheet-01-pipeline-jul5`) is still `queued`, and its results directory carries a `broadsheet-01-pipeline-jul5.VERIFY_FAILED` marker. Per the gate, I built **the section and the Broadsheet II page only**. Broadsheet I (The Gentle Robot) is not imported.

Note for David: the source `broadsheet_01_the_gentle_robot.md` currently shows 0 em dashes on disk, but the gate is the pipeline report plus a completed model consultation, neither of which is present. Do not import I until that pipeline clears and writes its report. The section is already shaped to accept it (drop in `content/thismachine/the-gentle-robot.md`, render its PDF the same way, and it appears in the series index automatically).

---

## Files created (all intended, git status clean of anything else)

Content (both `draft: true`):
- `content/thismachine/_index.md` — section index: imprint statement, the two bylines, the Guthrie machine lineage, the record posture, colophon.
- `content/thismachine/the-adversary-has-a-name.md` — Broadsheet II, full text, endnote intact.

Layouts (spare, reuse baseof/header/footer partials; scoped styles inline, main.css untouched):
- `layouts/thismachine/list.html` — section index + series list.
- `layouts/thismachine/single.html` — broadsheet page: meta, date placeholder, body, PDF download, provenance line, funnel footer.

Render path:
- `scripts/render-broadsheet.py` — Playwright/headless-Chromium A4 renderer (see below).

PDF + provenance:
- `static/thismachine/pdfs/broadsheet-02-the-adversary.pdf`

Report:
- `SPRINT_REPORT_tmp-phase1-site-jul5.md` (this file).

---

## Hashes

Broadsheet II print PDF, SHA-256 (printed on the page as its provenance line):

```
ff8c93677b3015928074d5cae7372e13c65b86888dce841b77835cc2a3b5b989  broadsheet-02-the-adversary.pdf
```

Broadsheet I: no PDF, no hash (pending).

Verified: the hash of the committed `static/...pdf` and the hash printed on the built page match, and the copy Hugo emits to `public/thismachine/pdfs/` is byte-identical.

---

## Render path used

Established path, not a new one. `RENDERING.md` documents the site's Playwright + headless-Chromium approach (`scripts/render-inference.py`); the requested `render_package.py` / `Rick_Moore_Package` stationery renderer does not exist in this repo. I added `scripts/render-broadsheet.py`, a sibling of the inference renderer using the same engine and A4 settings, differing only in what it strips and a spare paper stylesheet.

Behavior:
- Loads the Hugo-built page HTML, blocks all off-machine requests (analytics, remote fonts) so the render is deterministic and offline, prints to A4 with 0.9in margins, backgrounds on.
- Strips before render (the "draft scaffolding" and site chrome): nav, header, footer, newsletter signup, welcome overlay, skip link, the AI-minds beacon, the funnel footer, the PDF download button, **and the provenance/SHA line and the date placeholder.**
- Stripping the provenance line is deliberate and avoids a chicken-and-egg loop: the PDF is the record; its hash lives on the web page, never inside the file it describes. So the printed page can carry the hash while the PDF stays byte-stable. Re-rendering after the hash was written to the page produces the identical PDF (confirmed by the parity check above).

Reproduce:
```
hugo --buildDrafts
python3 scripts/render-broadsheet.py \
  public/thismachine/the-adversary-has-a-name/index.html \
  static/thismachine/pdfs/broadsheet-02-the-adversary.pdf
```

---

## Editorial-source note (Broadsheet II)

The vault source `broadsheet_02_the_adversary.md` still contains **12 em dashes**. The house rule is zero. The pipeline-cleared artifact for II is `substack_ready/broadsheet_02_SUBSTACK_REVISED.md` (0 em dashes), which is the same argument with the em dashes already resolved by sentence-level rephrasing. I used that cleared phrasing for the page body and restored the `[^1]` footnote so the endnote renders intact as a linked note (the Substack version had flattened it to inline numbering for Substack's renderer). Argument and citation are untouched. Result: the II page and its PDF contain **0 em dashes**.

---

## Date placeholders (what David sets at flip time)

Broadsheet II is first publication here; nothing is live on Substack, so no date is set. The placeholder is visible on the web page byline and reads:

> `[ publication date: David sets this at flip time, when draft:false ]`

To set it: add a `date:` field to the front matter of
`content/thismachine/the-adversary-has-a-name.md`
(the layout guards zero-dates, so the placeholder shows until a real `date` exists). The placeholder is stripped from the print PDF, so setting the date does **not** change the PDF or its hash.

---

## Verification performed

- `hugo --buildDrafts` builds clean (571 pages, no errors/warnings on the new templates).
- Section index renders; Broadsheet II page renders; footnotes render as a linked "Notes" block.
- PDF link resolves (`/thismachine/pdfs/broadsheet-02-the-adversary.pdf` present in `public/`).
- No new 404s: the funnel links point only to live targets (`/thismachine/`, the Substack home, `/foundation/`). No internal links to unbuilt Part 1 / Part 3 pages; the series prose mentions them without linking.
- Production build (`hugo`, no drafts) **omits** both section pages: the section is inert until David flips `draft:false`. (The static PDF is copied in any build, as static assets are; it is unlinked and unannounced until flip.)
- Zero em dashes across every authored file and inside the rendered PDF.
- Colophon honors the decision: the section text never explicitly names "Humanity and AI"; only the `@humanityandaiofficial` Substack handle and the domain carry the linkage.
- `git status` shows only the four intended paths.

---

## House rules honored

- Zero em dashes (authored files and PDF: confirmed 0).
- `draft: true` on every page.
- No subscribe machinery added (the single funnel CTA is a plain link to the existing Substack; no forms, no capture).
- No analytics added. (The site-wide Plausible tag in `baseof.html` is pre-existing and out of scope; I did not add or extend any counter, per decision point 4.)
- Local commit with specific paths only. **No push.**

---

## David's remaining step (five minutes, at flip time)

Point **thismachinepress.com** at the section: GoDaddy domain forwarding (301) to `https://humanityandai.com/thismachine/`. That is a David step in the GoDaddy console; nothing in this repo does it.

At flip: set `draft: false` on `_index.md` and the Broadsheet II page, add the `date:`, and (if desired) import Broadsheet I once its pipeline clears.
