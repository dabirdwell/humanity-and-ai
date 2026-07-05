# Sprint Report: Finding 6, Legislation Toolkit

**Date:** July 5, 2026
**Scope:** Turn /legislation from a scoreboard into a toolkit a staffer can act on today (Site Concept Audit, Finding 6, full toolkit option, authorized by David July 5).
**Status:** Complete. All new content pages ship `draft: true`. Committed locally only. Not pushed.

## What shipped

Five new content pages under `content/legislation/`, all `draft: true`, plus a Toolkit section added to the section layout.

1. **Model framework:** `content/legislation/haicta.md`
2. **Bill briefs (one per enacted bill):**
   - `content/legislation/brief-hb2992.md` (Data Center Consumer Ratepayer Protection Act)
   - `content/legislation/brief-sb259.md` (Data Center Groundwater Protection Act)
   - `content/legislation/brief-sb1734.md` (Responsible Technology in Schools Act)
   - `content/legislation/brief-sb1521.md` (Minor Protection from AI)
3. **Layout:** `layouts/legislation/list.html`, Toolkit section (model legislation, briefs, contact path).

## Sourcing and honesty calls

**HAICTA is presented as a framework, not statutory language.** The authorized sources (Dollens pitch, meeting prep, Deliverables one-pager) contain the concept and the one-pager, not drafted statute. The meeting-prep document is explicit that HAICTA is "a concept, not a draft bill." Per the sprint rules, the page publishes the one-pager framework and states plainly that full statutory drafting is available to any member office that wants it. No statutory language was written. The page also states clearly that HAICTA is not enacted law and was not one of the four bills that passed.

**Bill briefs are sourced only from the verified tracker and the Inference issues.**
- HB 2992 and SB 259 draw on `data/ok_bills_2026.json` plus their dedicated Inference coverage (Issue #17 and #19 for HB 2992; Issue #15 for SB 259).
- SB 1734 and SB 1521 draw on the tracker JSON only. Their mapped Inference issues (#3, #2) do not actually cover them: issue-3 is the Oracle healthcare brief and issue-2 is a "coming soon" stub. Rather than cite issues that do not discuss the bill, those two briefs rest on the verified tracker. No claim was imported that is not in the tracker JSON or a real Inference issue.

**Effective dates are stated as known, never invented.** HB 2992: July 1, 2026. SB 1734: approved May 12, 2026 with emergency clause, with the district-policy deadline before the 2027-28 school year. SB 259: signed May 20, 2026. SB 1521: passed the Senate March 23, 2026 and enacted before sine die. Where the tracker gives no distinct operative date, the brief states the signing or enactment date rather than guessing.

**Contact path reused, not invented.** `david@humanityandai.com`, the established public email on `/about` and throughout the Inference issues. Used verbatim in every page and in the layout contact block.

## Layout behavior

The Toolkit section iterates `.RegularPages` filtered on a custom `toolkit_kind` param and is wrapped in `{{ with $toolkit }}`, so it renders nothing when there are no published toolkit pages. Because all five pages are drafts, the section is inert on the live site until David flips `draft: false`.

Note: the pages use a custom `toolkit_kind` param rather than Hugo's `type` field. `type` is configured as a taxonomy in `hugo.toml` (`type = "types"`), so using it would spawn unwanted `/types/model-framework/` and `/types/bill-brief/` term pages once the drafts are published. `toolkit_kind` avoids that side effect.

## Verification (local hugo, /opt/homebrew/bin/hugo v0.156.0)

- **Drafts excluded (live behavior):** `/legislation/index.html` is byte-identical to the pre-change build. Toolkit markup count on the live legislation page: 0. No `/legislation/haicta/` or brief pages render. No `/types/` term pages for the toolkit. Confirmed inert.
- **Drafts included (what David gets when he flips):** all five pages render, the Toolkit section renders with the model framework, four briefs sorted by title, and the contact block. No stray taxonomy term pages.
- **Em dashes:** zero across all five content pages and the layout (Foundation Editorial Style Guide Rule 10).

## Pre-existing issue flagged (not fixed here, out of scope)

While verifying "renders unchanged," two build-to-build instabilities surfaced that are independent of this commit:

1. **Duplicate content at `/about/`:** both `content/about.md` and `content/about/_index.md` exist and resolve to the same URL. Hugo picks one nondeterministically; the choice flips based on page-map ordering, which any content addition perturbs. Removing this sprint's files does not restore a single stable resolution, confirming the flip is pre-existing, not caused by these pages.
2. **Taxonomy term title-casing:** unrelated terms render as `UBC` vs `Ubc` and `AI Governance` vs `Ai-Governance` across builds, a known Hugo ordering effect.

Neither was touched. Recommend resolving the `/about/` duplicate (keep one of the two files) in a separate, authorized pass, since it makes the about page and site aggregates nondeterministic on every deploy.

## Commit

Single commit of the specific paths: the five new content pages, the modified layout, and this report. No push.
