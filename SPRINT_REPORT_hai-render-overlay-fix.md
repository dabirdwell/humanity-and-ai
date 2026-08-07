# Sprint Report — Inference PDF render: welcome-overlay + skip-link + `## Related` fix

**Date:** 2026-07-17
**Repo:** `humanity-and-ai-site`
**Goal:** Stop the first-visit welcome overlay (and the skip-to-content link) from
printing onto page 1 of the Inference PDF, and handle the vault-only `## Related`
wikilinks section — ahead of tomorrow's Issue 21 ship.

---

## ⚠️ Blocker you must resolve first: local `main` is corrupt (pre-existing)

I could **not** make the requested local commit. The local `main` branch is
corrupted, and this predates my session — I did not cause it:

- `refs/heads/main` → `84f446025239620994820e05b0e62102f64984c2`, but **that commit
  object is missing from the object store** (`git cat-file -t` → "could not get
  object info"). So `git status`, `git log`, and `git commit` all fail with
  `fatal: bad object HEAD`. (The session-start "clean" status was git failing
  silently, not a genuinely clean tree.)
- These are **unpushed local commits** — `origin/main` is far behind at
  `3cb70238`, so `git fetch` will **not** recover the missing object.
- The missing commit is only the **tip**: `chore: issue-21 substack_url +
  distribution done (all 3 surfaces live Jul 17)`. Its parent
  `c22a8f667fa79e4794e236f6829405b0dff92391`
  (`publish: stream companion 'The Decree Carries a Gate Inside It'`) and all
  earlier commits are intact.
- `git fsck` did not complete within 2 minutes — the object store is unhealthy;
  run a full `fsck` when you have time.

I did **not** rewrite branch state (that drops a commit from history and is
hard to reverse) without your go-ahead. My two file changes are safe on disk,
staged for you to commit once `main` is repaired.

### Recommended recovery (safe — nothing on disk changes)

```bash
cd ~/Documents/Claude_Technical/humanity-and-ai-site
# Point main at the last surviving commit. --mixed keeps ALL working-tree files
# untouched; the lost tip's frontmatter edits reappear as uncommitted changes
# you can re-commit. The missing tip object is already unrecoverable, so this
# loses nothing that isn't already gone.
git reset --mixed c22a8f667fa79e4794e236f6829405b0dff92391
git status            # should work again
git fsck --full       # then verify object-store health
```

### Then commit this sprint's work (script + docs only)

```bash
git add scripts/render-inference.py RENDERING.md
git commit -m "render-inference: robustly suppress welcome overlay + add --strip-related

Set hai_welcomed via init script so the first-visit overlay never activates;
keep CSS hiding of overlay/#welcomeOverlay/.skip-link as a fallback. Add an
optional --strip-related flag to drop a trailing vault-only '## Related'
wikilinks section from the rendered DOM (source markdown untouched), and
document both in RENDERING.md.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
# NO push (push = deploy).
```

---

## 1. Overlay component + selectors found

**File:** `layouts/_default/baseof.html` (lines 103–121, rendered for every
section except `thismachine`).

| Element | Selector |
|---|---|
| Overlay container | `.welcome-overlay` / `#welcomeOverlay` |
| Card / heading | `.welcome-card` → `<h2>Welcome to Humanity &amp; AI</h2>` |
| Dismiss button | `.welcome-dismiss` / `#welcomeDismiss` ("Got it") |
| Skip link | `<a href="#main-content" class="skip-link">Skip to main content</a>` (line 100) |

**Mechanism (CSS `static/css/main.css` L2443–2462 + JS in baseof.html
L146–211):** `.welcome-overlay` is `display:none`; on first visit (no
`hai_welcomed` in `localStorage`) the JS adds `.visible` after a 1500 ms timer,
flipping it to `display:flex`. A fresh headless browser has no `hai_welcomed`
flag, so the overlay and the `.skip-link` printed onto page 1 of the PRELIM.

Note: the overlay+skip-link CSS hiding was **already** added in an earlier commit
today (`d8c791ca render-inference: hide welcome overlay + skip link in PDF
renders`), which is why the working-tree script already referenced them. This
sprint hardens that and adds the `## Related` handling.

## 2. What changed in `scripts/render-inference.py`

- **Primary fix — suppress before activation:** `page.add_init_script()` sets
  `localStorage['hai_welcomed'] = '1'` before any page script runs (wrapped in
  try/catch for `file://` origins), so the overlay's own JS short-circuits and
  never schedules the reveal timer.
- **Fallback — CSS hiding:** kept and extended `display:none !important` on
  `.welcome-overlay, #welcomeOverlay, .skip-link, a[href="#main-content"]`
  (plus the existing nav/footer chrome), in both `@media print` and screen.
- **New `--strip-related` flag:** removes a trailing `## Related` heading + its
  wikilink list from the rendered **DOM only** (finds `h2#related` / `h2` whose
  text is "Related", deletes siblings up to the next `h1`/`h2`). **Never edits
  markdown.** Prints whether it stripped anything.
- `RENDERING.md` documents the overlay suppression and both ways to handle
  `## Related` (preferred: strip it from the issue markdown before the final
  build; safety net: `--strip-related`).

## 3. Verification (rebuild → re-render → extract)

Staged the raw vault draft
(`Fawkes/Media and Outreach/Inference/Inference_21_DRAFT_jul17.md`, which still
contains the `## Related` block) into `content/inference/issue-21.md`, built with
`hugo -D -F -d /tmp/i21_build`, rendered to `/tmp/i21_render_test.pdf`, then
**restored the original `issue-21.md`** (see §4).

Confirmed both bugs were present in the built HTML before rendering:
`welcome-overlay` element present, `id="related"` heading present, literal
`[[Issue_21_News_Gather_2026-07-14]]` text present.

### Page-1 text — BEFORE (PRELIM `Inference_21_PRELIM_v3_jul16.pdf`, reported)
> **Welcome to Humanity & AI** … **Got it** … Skip to main content …

### Page-1 text — AFTER (`/tmp/i21_render_test.pdf`, this fix)
> The Inference   Issue #21   July 17, 2026
> The Ballot and the Docket
> On July 9, Oklahoma's Corporation Commission voted 3 to 0 to set the schedule …
> By David Alan Birdwell and Æ — Humanity and AI …

Grep assertions on page 1 of the AFTER render:
- `Welcome to Humanity` → **absent** ✓
- `Got it` → **absent** ✓
- `Skip to main content` → **absent** ✓

### `## Related` behavior
- Default render (`/tmp/i21_render_test.pdf`): `[[Issue_21_News_Gather_2026-07-14]]`
  still printed near the end (as expected — flag not used; demonstrates the
  page-9 literal-text bug).
- `--strip-related` render (`/tmp/i21_render_test_stripped.pdf`): overlay absent
  on page 1 **and** all wikilinks (`[[Issue_21…]]`, `[[Inference_20…]]`,
  `[[Publication_QC…]]`) **absent** ✓ — script logged
  "Stripped vault-only '## Related' section from the render."

## 4. Repo hygiene

- `content/inference/issue-21.md` **already existed** in the repo as clean,
  publishable content (the draft body with the vault `do_not_publish` frontmatter
  and `## Related` block already removed). The task assumed it did not exist and
  said to "stage then REMOVE" it — following that literally would have **deleted
  tomorrow's ship content I did not create**. So I backed it up
  (`/tmp/issue-21.orig.md`), staged the raw draft only for the test, and
  **restored** the original afterward. It is now byte-identical to the backup
  (verified with `diff -q`): 149 lines, `## Related` count 0, `do_not_publish`
  count 0.
- Temp build dir `/tmp/i21_build` removed. Evidence PDFs kept at
  `/tmp/i21_render_test.pdf` and `/tmp/i21_render_test_stripped.pdf`.
- Only intended working-tree changes: `scripts/render-inference.py`,
  `RENDERING.md` (this report is an output artifact, not committed).

## 5. Exact command for tomorrow's final render

The committed `content/inference/issue-21.md` is already clean (no `## Related`),
so `--strip-related` is a harmless no-op safety net there — keep it on. The issue
is `draft: true`, so build with `-D` (or flip `draft: false` first, per David).
Output path matches the frontmatter `pdf_url`
(`/inference/pdfs/Issue_21_The_Ballot_and_the_Docket.pdf`):

```bash
cd ~/Documents/Claude_Technical/humanity-and-ai-site
hugo -D -F                      # build the site (draft:true issue needs -D)
python3 scripts/render-inference.py --strip-related \
    public/inference/issue-21/index.html \
    static/inference/pdfs/Issue_21_The_Ballot_and_the_Docket.pdf

# Sanity-check page 1 has no overlay:
pdftotext -f 1 -l 1 static/inference/pdfs/Issue_21_The_Ballot_and_the_Docket.pdf - \
  | grep -i "Welcome to Humanity\|Got it\|Skip to main content" \
  || echo "page 1 clean ✓"
```
