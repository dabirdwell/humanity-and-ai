# SE to H&AI Migration Sprint (H&AI side): Finding 4

**Date:** July 5, 2026
**Authorized by:** David (full move, staged)
**Ground truth:** `/Users/david/Documents/Fawkes/Media and Outreach/SE_Migration_Triage_2026-07-05.md`
**Scope:** import the 9 MOVE posts into the H&AI Stream, replace the H&AI research page with a pointer, build and verify.
**Rules honored:** committed locally with specific paths, NO PUSH. Zero em dashes in everything authored here (frontmatter, provenance lines, research page, this report). Imported post bodies were preserved byte for byte and were not edited.

Note on paths: the triage doc was not at the `Claude_Technical/Fawkes` path named in the brief. It lives at `/Users/david/Documents/Fawkes/Media and Outreach/`. There are two Fawkes trees; the audit one is the top level `Documents/Fawkes`.

---

## 1. Imported posts (9) with new URLs

All imported to `content/stream/`, destination filename is the SE filename minus the leading number prefix. Bodies preserved verbatim; a single provenance line was appended to each. Original title and date preserved.

| SE source file | Old SE URL | New H&AI URL | Original date | type |
|---|---|---|---|---|
| 33-the-guardian-precedent.md | https://structuredemergence.com/posts/33-the-guardian-precedent/ | https://humanityandai.com/stream/the-guardian-precedent/ | 2026-03-20 | policy |
| 35-sixteen-components-one-thesis.md | https://structuredemergence.com/posts/35-sixteen-components-one-thesis/ | https://humanityandai.com/stream/sixteen-components-one-thesis/ | 2026-03-20 | policy |
| 80-the-carbon-credit-problem.md | https://structuredemergence.com/posts/80-the-carbon-credit-problem/ | https://humanityandai.com/stream/the-carbon-credit-problem/ | 2026-03-25 | insight |
| 87-the-250-degree-question.md | https://structuredemergence.com/posts/87-the-250-degree-question/ | https://humanityandai.com/stream/the-250-degree-question/ | 2026-03-27 | policy |
| 90-the-revolving-door-as-architecture.md | https://structuredemergence.com/posts/90-the-revolving-door-as-architecture/ | https://humanityandai.com/stream/the-revolving-door-as-architecture/ | 2026-03-27 | policy |
| 93-sixteen-components-one-portal.md | https://structuredemergence.com/posts/93-sixteen-components-one-portal/ | https://humanityandai.com/stream/sixteen-components-one-portal/ | 2026-03-29 | insight |
| 98-invest-dont-subsidize.md | https://structuredemergence.com/posts/98-invest-dont-subsidize/ | https://humanityandai.com/stream/invest-dont-subsidize/ | 2026-03-30 | policy |
| 118-who-controls-the-thinking-machines.md | https://structuredemergence.com/posts/118-who-controls-the-thinking-machines/ | https://humanityandai.com/stream/who-controls-the-thinking-machines/ | 2026-05-05 | policy |
| 119-three-ways-ai-infrastructure-bypasses-democracy.md | https://structuredemergence.com/posts/119-three-ways-ai-infrastructure-bypasses-democracy/ | https://humanityandai.com/stream/three-ways-ai-infrastructure-bypasses-democracy/ | 2026-06-26 | policy |

The provenance line appended to each body reads, for example:

> *Originally published at [Structured Emergence](https://structuredemergence.com/posts/119-three-ways-ai-infrastructure-bypasses-democracy/), June 26, 2026.*

The SE stub sprint will place a redirect at each old SE URL pointing back to the new H&AI URL, so the provenance link resolves to the SE URL which then redirects to the H&AI page. That loop is intentional and harmless per the brief.

### 90 / 105 dedupe choice

The triage lists `90/105-the-revolving-door-as-architecture` as a duplicate pair, import one. The SE side dedupe sprint (`sprints/intake/se-migration-jul5.json`) is still `status: queued`, so no SE dedupe report exists yet. Per the fallback rule I imported the lower number, **90**. I confirmed the two source bodies are byte identical, so the choice does not affect content. The survivor slug (`the-revolving-door-as-architecture`) is what the SE stub for both 90 and 105 should ultimately point at.

---

## 2. Frontmatter decisions

I inspected three existing Stream posts (`inference-6-oklahoma-ai-session`, `ferc-chose-the-regions`, `graduated-obligation`) and surveyed the whole section. Fields kept: `title`, `date`, `draft`, `type`, `tags`, `description`, and `author` where the source carried one.

- **draft normalization (notable).** Only 4 of the 9 were `draft: false` on SE (33, 35, 90, 119). Five were `draft: true` on SE: **80, 87, 93, 98, 118**. Hugo excludes `draft: true` from the build, so leaving them as drafts would have failed the step 3 requirement that all 9 render. I set `draft: false` on all 9. Because the move is staged (local commit, no push), nothing publishes until David pushes, so this is safe to review. Flag for David: the prescribed provenance wording says "Originally published," which is slightly generous for the five that were unpublished SE drafts. If that matters, the wording is a one line change per file before ship.
- **type.** Assigned from the Stream vocabulary (values in use: insight, report, community, futurism, policy, stream, tool). Seven civic and governance pieces got `type: "policy"`; the two building in public reflections (80 carbon credit, 93 one portal) got `type: "insight"`.
- **tags.** Preserved the source topical tags, with one change: dropped the `structured-emergence` self tag where present (33, 35, 80). On H&AI that tag names the other site, not a topic, and provenance is already carried by the appended line. Hyphenated a few multiword tags to match Stream tag style (for example `phoenix wells` became `phoenix-wells`). All other tags are verbatim.
- **description.** Where the source had a usable `description` or `summary` (80, 98, 118, 119), I carried it over. Where the source description was empty or absent (33, 35, 87, 90, 93), I wrote a one or two sentence factual description drawn from the post's own thesis. This is frontmatter metadata only; no body prose was touched. All descriptions are em dash free.
- **author.** Preserved where the source had one (33, 35, 80, 90 as "Humanity and AI"; 118, 119 as "David Birdwell and Æ"). Not invented where absent (87, 93, 98).
- **date.** Preserved verbatim, including 90's full timestamp form `2026-03-27T22:30:00-05:00`.
- **dropped source-only fields.** SE `cover:` blocks, `categories`, `summary`, and the `<!--more-->` marker in the body were handled as follows: `cover`/`categories`/`summary` are SE frontmatter conventions and were not carried into the Stream frontmatter; the `<!--more-->` marker inside 98's body was left in place because it is part of the verbatim body and Hugo treats it as a harmless summary divider.

Verification: a script confirmed each imported body is byte identical to its SE source (frontmatter stripped, provenance excluded), and that no em dash (U+2014) appears in any frontmatter or provenance line I authored.

---

## 3. Research page

`content/research/_index.md` replaced with a thin pointer. Page title (`Research & Publications`), `layout: "single"`, and the frontmatter field set were preserved; the `description` was updated to match the new pointer purpose. Diff: 2 insertions, 22 deletions.

New body (one paragraph, one link):

> The Humanity and AI research program, including our peer-reviewed and pre-print work on language model behavior, alignment, and the structured emergence of intelligence, now lives at [structuredemergence.com](https://structuredemergence.com). Papers, code, and data are published there, open access.

**Flag for David:** the previous version carried a full listing of **Paper 1** (Behavioral Signatures of Ambiguity Processing) with its Zenodo DOI `10.5281/zenodo.20161483`, the GitHub code link, and a companion essay link to `/stream/paper1-fossil-emotion/`. The thin pointer removes that listing. The companion essay itself still exists at `content/stream/paper1-fossil-emotion.md` and is untouched. If the intent is for H&AI to keep citing the paper's DOI directly rather than deferring entirely to SE, the pointer should be widened to retain the DOI line. The full removed content is preserved in git history and in this report's diff for easy restoration.

---

## 4. Build and verification

Built with `/opt/homebrew/bin/hugo --gc`. Result: 444 pages, **0 errors, 0 warnings**.

- All 9 posts render at `/stream/<slug>/` (confirmed 9 of 9 `index.html` present).
- Each renders its original date (spot checked the-guardian-precedent shows 2026-03-20 / March 20, 2026) and its provenance anchor to the correct numbered SE URL.
- The `/stream/` index lists all 9 with their original dates.
- The research pointer renders; the old Paper 1 / Zenodo block is gone from the built page (0 matches).

### Homepage "Latest" date behavior (noted, not hacked)

The homepage Latest block (`layouts/index.html`) shows `first 4` of stream posts by `.ByDate.Reverse`. After import, the Latest top 4 are:

1. **three-ways-ai-infrastructure-bypasses-democracy (imported, 2026-06-26)**
2. the-model-that-broke-into-its-own-government (2026-06-26)
3. ferc-chose-the-regions (2026-06-26)
4. washington-recalled-a-frontier-ai (2026-06-15)

Only **one** of the 9 imports (119) surfaces in Latest, and it does so at its genuine original date of June 26, not as if freshly written today. It lands at slot 1 because three published posts share that June 26 date and Hugo's reverse-date tie break ordered it first. The other 8 imports (March through May dates) sort well below the fold, as intended.

Context that matters here: the site's newest looking post, `who-decided` (2026-06-27), is `draft: true` and gitignored (David's unpublished draft), so it is not in the build. That is why June 26 is the effective newest published date and why a June 26 import can reach slot 1.

Per the brief I did not hack the dates or add weights to suppress this. If David wants 119 to not lead the homepage, the clean options are: give the genuinely newest intended post a later date, add a `weight` based ordering to the Latest query, or set 119 slightly earlier. No change was made pending David's call.

---

## 5. Commit

Single local commit, specific paths, **no push**:

- `content/research/_index.md` (pointer)
- `content/stream/` the 9 imported posts
- `SE_Migration_Sprint_HAI_2026-07-05.md` (this report)

`public/` is gitignored and not committed. `git status` showed only the intended files. Push order at ship time is H&AI first, then SE, so no SE stub ever points at a page that does not exist yet.
