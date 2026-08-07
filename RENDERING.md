# Inference PDF Rendering

Automated pipeline to render Inference issues from Hugo-built HTML to print-ready A4 PDFs using Playwright (headless Chromium).

## Prerequisites

```bash
pip install playwright
playwright install chromium
```

## Quick start

Render the latest issue:

```bash
hugo                              # build the site first
./scripts/render-inference.sh     # renders highest-numbered issue
```

Render a specific issue:

```bash
./scripts/render-inference.sh 5   # renders Issue #5
```

Output goes to `static/pdf/inference-issue-N.pdf`.

## Direct usage

The Python script accepts any HTML file:

```bash
python3 scripts/render-inference.py public/inference/issue-3/index.html output.pdf
```

## What it does

1. Opens the HTML in headless Chromium
2. Suppresses the first-visit welcome overlay before the page's scripts run
   (sets the `hai_welcomed` localStorage flag via an init script) and hides
   site navigation, footer links, external-link buttons, the welcome overlay,
   and the "Skip to main content" link via CSS
3. Waits for network idle and Google Fonts to load (`document.fonts.ready`)
4. Prints to A4 PDF with 0.75-inch margins and background colors preserved

### Welcome overlay (first-visit onboarding)

The site shows a one-time "Welcome to Humanity & AI … Got it" overlay on a
visitor's first load (defined in `layouts/_default/baseof.html` as
`.welcome-overlay` / `#welcomeOverlay`, shown ~1.5s after load by adding the
`.visible` class). A fresh headless browser has no `hai_welcomed` flag set, so
without intervention the overlay — and the `.skip-link` "Skip to main content"
anchor — print onto page 1. The renderer suppresses both automatically; no
flag is needed.

## Removing the vault-only `## Related` section

Issue markdown drafted in the Obsidian vault often ends with a `## Related`
section of `[[wikilinks]]`:

```markdown
## Related
- [[Issue_21_News_Gather_2026-07-14]]
- [[Inference_20_DRAFT_jul10]]
```

Hugo does **not** resolve `[[wikilinks]]`, so this section renders as literal
`[[...]]` text at the end of the PDF. It is an authoring aid, not publishable
content, and must not appear in a final render.

Two ways to handle it:

1. **Preferred — remove it from the issue markdown before the final build.**
   When staging vault draft content into `content/inference/issue-N.md`, delete
   the trailing `## Related` block. (The committed `content/inference/*.md`
   issues are already clean; this only matters when copying fresh vault drafts.)
   The renderer never edits markdown, so this is the source-of-truth fix.

2. **Safety net — `--strip-related`.** If a `## Related` section slips through,
   pass the flag to drop it from the rendered DOM at print time (the source
   markdown is left untouched):

   ```bash
   python3 scripts/render-inference.py --strip-related \
       public/inference/issue-21/index.html output.pdf
   ```

   The script prints whether it found and stripped a section.

## Output location

PDFs are written to `static/pdf/` so Hugo can serve them at `/pdf/inference-issue-N.pdf`.
