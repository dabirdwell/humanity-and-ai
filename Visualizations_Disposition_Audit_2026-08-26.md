# Visualizations Section: Disposition Audit
**Ruled by David 2026-08-26. Audit run 2026-08-30.**
Section audited: `/Users/david/Documents/Claude_Technical/humanity-and-ai-site/content/visualizations/`

> **Note on this file's location.** You asked for this report at
> `/Users/david/Documents/Fawkes/Media and Outreach/Website_Remakes/Visualizations_Disposition_Audit_2026-08-26.md`.
> This session was sandboxed to the site repository and was denied both read and write access to the Fawkes vault,
> so the report was written here instead. To put it where you wanted it:
>
> ```sh
> mv "/Users/david/Documents/Claude_Technical/humanity-and-ai-site/Visualizations_Disposition_Audit_2026-08-26.md" \
>    "/Users/david/Documents/Fawkes/Media and Outreach/Website_Remakes/"
> ```

---

## Summary

**The section holds 26 pages, not 32.** The pages you remembered as needing a dump are already gone from the content tree. `penrose-tiling` and `luminas-whisper` both return HTTP 404 on the live site and have no `.md` source in `content/visualizations/`. They survive only as stale build output under `/Users/david/Documents/Claude_Technical/humanity-and-ai-site/public/visualizations/`, which is generated output, not source. Commit `48bf900` ("Site focus pass: 6-item nav, mission-first About, homepage viz, retire non-civic vizzes") appears to be where they left. The count of 32 was accurate before that commit. It is not accurate now.

Buckets, across all 26 pages:

| Bucket | Count |
|---|---|
| PUBLIC-WORTHY | 8 |
| FIXABLE | 10 |
| INTERNAL-OR-EXPERIMENTAL | 8 |
| FICTION-OR-OFFTOPIC | 0 |

**If the dumps are executed, the section becomes 18 pages: eight that are ready to feature today and ten that are genuinely good ideas held back by a small number of repeatable render bugs, with every product pitch, framework self-portrait, and invented-number toy moved out.**

The staged move script covers the 8 INTERNAL-OR-EXPERIMENTAL pages. The FICTION-OR-OFFTOPIC bucket is empty because that cleanup already happened.

---

## Method, and what I did not check

**Read in full:** all 26 `.md` sources, plus the matching interactive files in `/Users/david/Documents/Claude_Technical/humanity-and-ai-site/static/viz/`.

**Fetched live:** the section index at `https://humanityandai.com/visualizations/` (returns 25 pages; the 26th, `brain-mastery-pipeline`, is `draft: true` and correctly 404s), plus spot checks on individual pages.

**What I could not do: I never saw these pages rendered.** No browser binary was reachable from this session (no local or global Playwright, and `/Applications` was outside the sandbox), and the fetch tool converts pages to markdown, which strips iframes entirely. So I could not confirm a clipped axis year or a cut-off left label by eye, the way you did.

Every render verdict below is therefore **source-level evidence, not pixel inspection.** That evidence is concrete and checkable, and it found one defect class you almost certainly hit:

**The orphaned height contract.** Six pages use the correct pattern: the visualization posts its measured height up via `postMessage({iframeHeight})`, and the page has a listener script that resizes the iframe to match. Five other pages ship a visualization that posts its height to nobody. The listener script was never added to the `.md`. The iframe stays pinned at whatever pixel height was hardcoded, and the content inside either scrolls within the frame or gets cut at the bottom edge. Verified by:

```sh
grep -l "iframeHeight" static/viz/*.html            # the viz sends
grep -L "iframeHeight" content/visualizations/*.md  # the page does not listen
```

The five: `energy-burden-calculator` (pinned 720px), `health-access-map` (540px), `housing-affordability` (420px), `student-debt-clock` (700px), `trust-timeline` (540px). `housing-affordability` at 420px is the most likely to be visibly cut, and `trust-timeline` at 540px is a 1958–2025 chart, which fits your "axis year clipped" description.

**A second class: scroll-in-scroll.** Four pages hardcode an iframe taller than a viewport with no auto-height at all: `seven-generations` (4200px, bumped to 5800px on mobile by an inline script), `ai-transition-window` (2400px), `ubc-visual-stats` (2400px), `ubc-circos` (1200px). These are the "iframe forcing a scroll" pages.

On the understanding axis I graded against one test: **does a first-time reader who has never heard of Foundation learn something about the world, or only about our taxonomy?** Several pages fail that test while rendering cleanly, and I weighted that as heavily as you asked me to.

I extended FIXABLE slightly beyond "broken render" to cover two pages whose repair is sourcing rather than layout (`what-you-already-pay`, `cortisol-tax`). Both are named explicitly below so you can move them if you disagree.

---

## Page-by-page

| Slug | Bucket | Render verdict | Understanding verdict | Reason |
|---|---|---|---|---|
| `the-1980-divergence` | PUBLIC-WORTHY | Fixed 560px, no auto-height; low overflow risk | Teaches | One chart, one idea, EPI/BLS sourced: productivity kept climbing, pay did not. Highest teaching-per-pixel in the section. |
| `time-machine` | PUBLIC-WORTHY | Clean: self-sizing, page listens for height | Teaches | Converts rent into hours worked, then shows the same job in Germany. Concrete, personal, sourced to NLIHC and OECD. |
| `stress-test` | PUBLIC-WORTHY | Clean: self-sizing, page listens for height | Teaches | Five questions about your own life, then your position against peer nations. Personal before political, no bracket or jargon barrier. |
| `the-classroom` | PUBLIC-WORTHY | Clean: self-sizing, page listens for height | Teaches | Neurath isotype grid, one figure per thirty people. A century-old technique built for exactly this reader. NCES, SAMHSA, NLIHC, Census. |
| `choice-ledger` | PUBLIC-WORTHY | Clean: self-sizing, page listens for height | Teaches | Six spending comparisons, each sourced (EPI, JAMA, HUD, UCSF). Makes "scarcity is a political choice" arithmetic rather than rhetoric. |
| `cost-of-nothing` | PUBLIC-WORTHY | Clean: self-sizing, page listens for height | Teaches, with a caveat | Six sourced annual figures. The per-second ticking is drama, not information (the page admits it), but the scale does land. |
| `poverty-premium` | PUBLIC-WORTHY | Fixed 700px, no auto-height; low overflow risk | Teaches | The extra cost of being poor is a real, named, researched phenomenon, and the income slider makes it legible. Brookings, Fed, USDA. |
| `oklahoma-wells` | PUBLIC-WORTHY | Fixed 680px, has internal resize handler | Teaches | 22,000 wells from Oklahoma Corporation Commission data, with a checkable legislative claim (HB 3917, 2026-03-16). Local, specific, verifiable. |
| `trust-timeline` | FIXABLE | **Broken contract:** viz posts `iframeHeight`, page has no listener; pinned at 540px | Teaches | Sixty years of Pew data, annotated, and honest about the partisan split underneath the top-line number. Fix: add the height listener. |
| `housing-affordability` | FIXABLE | **Broken contract:** posts `iframeHeight`, no listener; pinned at 420px, shortest frame in the section | Teaches | NLIHC Out of Reach, per state, with the hours-per-week card. Most likely page to be visibly cut. Fix: add the height listener. |
| `student-debt-clock` | FIXABLE | **Broken contract:** posts `iframeHeight`, no listener; pinned at 700px | Teaches | The prose on why balances grow during repayment is the real teaching, and it is good. Fix: add the height listener. |
| `energy-burden-calculator` | FIXABLE | **Broken contract:** posts `iframeHeight`, no listener; pinned at 720px | Teaches | DOE and ACEEE 6% and 10% thresholds measured against your own income. Fix: add the height listener. |
| `health-access-map` | FIXABLE | **Broken contract:** posts `iframeHeight`, no listener; pinned at 540px | Teaches | Three federal datasets layered so the compounding is visible. Fix: add the height listener. |
| `ai-transition-window` | FIXABLE | **Scroll-in-scroll:** hardcoded 2400px, no auto-height, no resize | Teaches | The site's thesis page, and the plain-language framing works. The 2400px frame is the problem, not the content. Fix: wire auto-height. |
| `ubc-visual-stats` | FIXABLE | **Scroll-in-scroll:** hardcoded 2400px, no auto-height | Teaches | Unlike the other Foundation pieces this uses genuinely external data (EPI, OECD, Commonwealth Fund, Vera). Fix: wire auto-height. |
| `seven-generations` | FIXABLE | **Worst frame in the section:** 4200px hardcoded, forced to 5800px on mobile by an inline script | Teaches | Three real decisions traced forward is a strong idea. Also uses `type: "visualization"` (singular) and `layout: "viz-page"` where every sibling uses `type: "visualizations"`. Fix: auto-height, normalize front matter, dedupe against `seven-generation-fork`. |
| `cortisol-tax` | FIXABLE | Fixed 700px, no auto-height; low overflow risk | Half teaches | Mani et al. (Science, 2013) and the 13-IQ-points finding are real and worth a chart. The slider-to-organ-damage animation is not measured by anything. Also cites "David's line in the Safety essay," an internal reference. Fix: lead with the study, cut the organ animation. |
| `what-you-already-pay` | FIXABLE | Fixed 680px, no auto-height; low overflow risk | Argues more than it teaches | The $6,400-vs-$2,275 comparison is our own model, not a published figure, and the footer credits only "estimates from KFF, BJS, EPI, NRF." Strong idea, thin proof. Fix: publish the per-line derivation or soften the claim. |
| `brain-mastery-pipeline` | INTERNAL-OR-EXPERIMENTAL | Not published: `draft: true`, returns 404 live | Does not teach | A five-product funnel (Clarity, Dojo, TasteBud, Quiltographer, Citizen) with a "Try Clarity" call to action. A product page sitting in the visualizations folder. |
| `why-oklahoma` | INTERNAL-OR-EXPERIMENTAL | Fixed 640px, no auto-height | Does not teach | Org marketing, not civic data: "HAICTA is in conversation with Rep. Dollens," plugs for Clarity and Guardian AI, and "David's family has served this state for three layers" (which also reads like a typo for "generations"). The leapfrog premise is a non-sequitur: ranking last in education spending does not by itself create marginal return. |
| `the-5-3-scale` | INTERNAL-OR-EXPERIMENTAL | Fixed 760px, no auto-height | Actively misleading | The searchable job database is built on one person's informal 1-to-10 ratings, and the page itself says "individual scores are approximations for illustration." A reader searches their own job and is handed an invented number inside an authoritative interface. The most quietly harmful page in the section. |
| `the-dominoes` | INTERNAL-OR-EXPERIMENTAL | Fixed 640px, has internal resize handler | Does not teach | A cascade animation of a claim, with no sources at all in the footer. Every other civic page in the section cites something. This one asserts. Motion study, not evidence. |
| `foundation-ripple` | INTERNAL-OR-EXPERIMENTAL | Fixed 580px, no auto-height | Does not teach | Visualizes our own framework, and admits the cascade weights are "estimates... directional, not precise." The ribbons are authored, not measured. Teaches the reader our taxonomy, not the world. |
| `ubc-circos` | INTERNAL-OR-EXPERIMENTAL | **Scroll-in-scroll:** hardcoded 1200px, no auto-height | Does not teach | The same problem, larger: a chord diagram whose footer says "Data derived from the Foundation framework." It is a picture of our own proposal. The Stafford Beer and Ashby passages are internal design rationale, not first-time-reader material. |
| `seven-generation-fork` | INTERNAL-OR-EXPERIMENTAL | Fixed 900px, no auto-height | Does not teach | Two invented 175-year futures drawn as a chart, for a policy that does not exist yet. Speculation rendered with the visual authority of data. Also duplicates the topic of `seven-generations`. |
| `the-mirror` | INTERNAL-OR-EXPERIMENTAL | Clean: self-sizing, page listens for height | Does not teach | **The most debatable call in this audit.** Best-engineered page in the section (42KB, correct auto-height, no data collection) and it teaches nothing about the world: it maps your feelings onto our sixteen components and outputs a share card. A clean render that teaches nothing, which is the case you told me to weight hardest. Move it or overrule me. I would not feature it. |

---

## The four lists

### PUBLIC-WORTHY (8) — keep and feature
Clean or near-clean render, real civic understanding, external sourcing.

1. `the-1980-divergence`
2. `time-machine`
3. `stress-test`
4. `the-classroom`
5. `choice-ledger`
6. `cost-of-nothing`
7. `poverty-premium`
8. `oklahoma-wells`

### FIXABLE (10) — good idea, repair named
Five of these share one fix. See the next section.

1. `trust-timeline` — add height listener
2. `housing-affordability` — add height listener
3. `student-debt-clock` — add height listener
4. `energy-burden-calculator` — add height listener
5. `health-access-map` — add height listener
6. `ai-transition-window` — wire auto-height, replace the 2400px hardcode
7. `ubc-visual-stats` — wire auto-height, replace the 2400px hardcode
8. `seven-generations` — wire auto-height, normalize front matter, dedupe against the fork page
9. `cortisol-tax` — lead with Mani et al., cut the unmeasured organ animation
10. `what-you-already-pay` — publish the derivation or soften the claim

### INTERNAL-OR-EXPERIMENTAL (8) — move out
Product pitches, framework self-portraits, unmeasured animations, and one page built on invented numbers. **These are the 8 the staged script moves.**

1. `brain-mastery-pipeline`
2. `why-oklahoma`
3. `the-5-3-scale`
4. `the-dominoes`
5. `foundation-ripple`
6. `ubc-circos`
7. `seven-generation-fork`
8. `the-mirror`

### FICTION-OR-OFFTOPIC (0) — already done
Empty. `luminas-whisper` (Mars fiction), `penrose-tiling` (brand motion study), `whirlpool-pattern`, `inscription-drift`, `brewsters-billions`, and `convergence` are gone from `content/` and 404 on the live site.

**One loose end:** their generated HTML is still sitting in `/Users/david/Documents/Claude_Technical/humanity-and-ai-site/public/visualizations/`, along with a full set of iCloud `" 2"` duplicate directories. That folder is build output and is safe to blow away with a clean rebuild. I did not touch it.

---

## The one-line fix that clears five pages

Five FIXABLE pages need the same six lines of JavaScript, already working correctly on `choice-ledger`, `cost-of-nothing`, `stress-test`, `the-classroom`, `the-mirror`, and `time-machine`. Give the iframe an `id`, then append:

```html
<script>
window.addEventListener('message', function(e) {
  if (e.data && e.data.iframeHeight) {
    var f = document.getElementById('YOUR-FRAME-ID');
    if (f) f.style.height = (e.data.iframeHeight + 24) + 'px';
  }
});
</script>
```

The visualizations already send the message. Nothing is listening. That is the whole bug on `trust-timeline`, `housing-affordability`, `student-debt-clock`, `energy-burden-calculator`, and `health-access-map`.

---

## Before you run the script: a Hugo warning

The script moves pages into `content/_archive_visualizations/`, as specified. **Hugo does not ignore directories that start with an underscore.** That is a Jekyll convention, not a Hugo one. I checked `/Users/david/Documents/Claude_Technical/humanity-and-ai-site/hugo.toml` and it has no `ignoreFiles` key. Left alone, a rebuild would republish all eight archived pages at `/_archive_visualizations/<slug>/`, which is the opposite of the goal.

The script handles this by writing an `_index.md` into the archive directory with `draft: true` and `headless: true`, and by printing the exact `hugo.toml` line to add. It does not edit `hugo.toml` itself. **Add this to `hugo.toml` before rebuilding:**

```toml
ignoreFiles = ['content/_archive_visualizations/.*']
```

The alternative, if you would rather not touch config: move the archive directory out of `content/` entirely after the script runs. One command, and the script prints it.

---

## Verification

- Pages graded: **26**. `ls content/visualizations/*.md | wc -l` returns 26. `_index.md` is the section header and is not graded as a page.
- Every page appears in exactly one bucket: 8 + 10 + 8 + 0 = 26, matching the table above.
- The requested count of 32 could not be reconciled and is reported as corrected rather than padded. See the summary.
- Nothing was deleted, moved, edited, committed, or pushed. The only files written are this report and the staged script.
- The staged script was written but not executed.

*Audit written by Claude Opus 5, 2026-08-30. Render verdicts are source-level evidence, not pixel inspection. See "Method, and what I did not check."*
