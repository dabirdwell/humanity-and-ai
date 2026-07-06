# Sprint Report: Broadsheet I (The Gentle Robot) added to This Machine Press

**Repo:** humanity-and-ai-site (hai-site)
**Date:** 2026-07-05
**Builds on:** commit d6a0813 (Phase 1 section + Broadsheet II)
**Status:** Built, verified locally, committed. **No push.**

---

## Gate: GO (confirmed)

`Fawkes/Foundation/Themes/AI_and_Governance/GO_Broadsheets/Broadsheet_I_Pipeline_Report_2026-07-05.md`
reports **CLEARED for site import / Gate: GO**. Opus 4.8 consultation completed
2026-07-05 22:02, no blockers, FTC 6(b) citation verified, em dashes zero,
endnote integrity confirmed. The Phase 1 sprint had held I as PENDING because this
report did not yet exist; it now exists and says GO. Imported.

## Files (commit a3d91b2, exactly these two paths)

- `content/thismachine/the-gentle-robot.md` (new) — Broadsheet I page, `draft: true`,
  full text, `[^1]` FTC endnote intact, This Machine byline, date placeholder.
- `static/thismachine/pdfs/broadsheet-01-the-gentle-robot.pdf` (new) — print A4 PDF.

Nothing else staged. `public/` is gitignored (not part of the commit). No push
(branch is local, ahead of origin/main).

## Hash

Broadsheet I print PDF, SHA-256 (printed on the page as its provenance line):

```
b859fcc93e71a2d0d846e95a63627c9605883e4697968a392dededd4f490e878  broadsheet-01-the-gentle-robot.pdf
```

Verified: the hash of the committed `static/...pdf`, the copy Hugo emits to
`public/thismachine/pdfs/`, and the string printed on the built page all match.

## How it was built (same path as II)

- Source: `GO_Broadsheets/broadsheet_01_the_gentle_robot.md` (post-consultation
  revision, 0 em dashes on disk, verified). Body reproduced in full, including the
  consultation-applied Asymmetry sentence ("...but you can model them back. With the
  system, the modeling runs only one way.") and the FTC dossier endnote verbatim.
- Render: `hugo --buildDrafts`, then
  `python3 scripts/render-broadsheet.py public/thismachine/the-gentle-robot/index.html static/thismachine/pdfs/broadsheet-01-the-gentle-robot.pdf`
  (Playwright/headless-Chromium A4, off-machine requests blocked, site chrome +
  provenance line + date placeholder stripped). Identical renderer, settings, and
  strip list as Broadsheet II.

## Structure parity with Broadsheet II (matched exactly)

- Same front-matter field set and same `single.html` / `list.html` layouts.
- Series index (`/thismachine/`) auto-lists broadsheets via
  `range where .Pages "Type" "thismachine"`; `_index.md` does not enumerate them,
  so it needed no edit. I added `weight: 1` to Broadsheet I so it orders **before**
  II (weight-1 sorts ahead of unweighted II). Confirmed order in the built index:
  "Part 1 of 8 — The Gentle Robot", then "Part 2 of 8 — The Adversary Has a Name."
  Broadsheet II's file was **not** modified.
- Provenance treatment identical: hash lives on the web page, stripped from the PDF.

### Two deliberate normalizations vs the source (flagging for your review)

Broadsheet II's page normalized the same boilerplate lines, so I matched II, not the
raw source. The argument and endnote are untouched; only these house-format lines differ:

1. Top locator: source reads "*Graduated Obligation, Broadsheet I*"; page reads
   "*Graduated Obligation, Part 1 of 8*" to match II's eyebrow/locator format and
   keep the series index consistent. Front-matter `part: "Part 1 of 8"`.
2. Closing colophon: source reads "*This is Broadsheet I of the Graduated Obligation
   series...*"; page reads "*Broadsheet I of the Graduated Obligation series...*"
   (drops "This is"), exactly as II's colophon does.

If you'd rather the page carry the source's own "Broadsheet I" wording verbatim
instead of the "Part 1 of 8" series format, that is a one-line change in three spots;
say the word.

Not carried over (correctly, matching II): the source's Obsidian `## Related`
wikilink block and the redundant `## Notes` heading (Hugo auto-collects the footnote
and the layout CSS labels it "Notes").

## Verification performed

- `hugo --buildDrafts` clean: 572 pages (was 571), no template errors/warnings.
- Both single pages render; footnote renders as a linked "Notes" block on the I page.
- Both PDF links resolve in `public/thismachine/pdfs/`.
- Clean production build (`hugo`, no drafts, `public/` wiped first) **omits** both
  broadsheet pages and the section index; static PDFs are copied regardless (inert,
  unlinked until flip). Section stays dark until you set `draft: false`.
- Zero em dashes and zero en dashes in the content file; zero em dashes in the
  extracted PDF text (`pdftotext`, 8230 chars).
- Chromium PDF output is not bit-reproducible run-to-run (a fresh re-render yields a
  different hash; **Broadsheet II behaves identically** — this is Chromium embedding a
  per-run document id/timestamp, not a content difference). The record invariant that
  matters holds: the committed PDF's hash equals the hash printed on the page.

## For David

- **Nothing blocking.** Section still `draft: true` throughout; inert until flip.
- **Review call:** the two boilerplate normalizations above (Part 1 of 8 vs Broadsheet
  I). Easy to revert if you want source-verbatim wording.
- **At flip** (unchanged from the Phase 1 plan): set `draft: false` on `_index.md`,
  the Broadsheet I page, and the Broadsheet II page; add `date:` to each broadsheet
  (the layout guards zero-dates, so the placeholder shows until then; setting the date
  does not change the PDF or its hash); point thismachinepress.com at
  `/thismachine/` via GoDaddy 301 forwarding.
- **This report is uncommitted** (untracked at repo root), per the "commit specific
  paths only" rule. The Phase 1 report still describes I as PENDING; this report is
  the record that the gate cleared and I is now in.
