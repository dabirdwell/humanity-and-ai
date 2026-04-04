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
2. Waits for network idle and Google Fonts to load (`document.fonts.ready`)
3. Hides site navigation, footer links, and external-link buttons
4. Prints to A4 PDF with 0.75-inch margins and background colors preserved

## Output location

PDFs are written to `static/pdf/` so Hugo can serve them at `/pdf/inference-issue-N.pdf`.
