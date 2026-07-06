#!/usr/bin/env python3
"""
Render a This Machine Press broadsheet from Hugo-built HTML to a print-ready
A4 PDF using Playwright (headless Chromium).

Same render path as render-inference.py: load the built HTML, wait for fonts,
strip everything that does not belong on a printed broadsheet, print to A4.

The stripped elements include the funnel footer, the provenance (SHA-256) line,
and the PDF download link. Stripping the provenance line is deliberate: the PDF
is the record, and its hash is printed on the web page, not inside the file it
describes. That keeps the hash stable and free of any chicken-and-egg loop.

Usage:
    python3 scripts/render-broadsheet.py public/thismachine/<slug>/index.html static/thismachine/pdfs/<name>.pdf

Requirements:
    pip install playwright
    playwright install chromium
"""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Everything that must not appear in the printed broadsheet.
HIDE_SELECTORS = ", ".join([
    "nav", ".site-header", ".site-footer", ".skip-link",
    ".welcome-overlay", ".newsletter-signup", ".edit-link",
    ".tmp-funnel", ".tmp-provenance", ".tmp-pdf", ".tmp-date-placeholder",
    "[data-for='artificial-minds']",
])

# Spare paper stationery: white sheet, dark serif, regardless of site theme.
PRINT_STYLE = f"""
    {HIDE_SELECTORS} {{ display: none !important; }}
    html, body {{ background: #ffffff !important; }}
    body, .post-single, .post-content, .post-content p, .post-content li {{
        color: #1a1a1a !important;
    }}
    h1, h2, h3, .post-meta, .tmp-subtitle, .tmp-byline,
    .tmp-date-placeholder, .post-content blockquote,
    .post-content strong {{ color: #111111 !important; }}
    .post-content .footnotes {{ color: #333333 !important; border-top-color: #cccccc !important; }}
    .post-content .footnotes::before {{ color: #111111 !important; }}
    .post-content a {{ color: #1a1a1a !important; text-decoration: none !important; }}
    main {{ padding-top: 0 !important; }}
"""


def render_pdf(html_path: str, pdf_path: str) -> None:
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"Error: HTML file not found: {html_file}", file=sys.stderr)
        sys.exit(1)

    pdf_file = Path(pdf_path).resolve()
    pdf_file.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Block every off-machine request (analytics, remote fonts, preconnect).
        # They otherwise hang the load event in a headless render and add nothing
        # a print broadsheet needs; the serif fallback stack carries the type.
        page.route(
            "**/*",
            lambda route: route.abort()
            if route.request.url.startswith(("http://", "https://"))
            else route.continue_(),
        )

        print(f"Loading {html_file.name} ...")
        page.goto(html_file.as_uri(), wait_until="load", timeout=60000)
        try:
            page.evaluate("() => document.fonts.ready")
        except Exception:
            pass
        page.wait_for_timeout(500)
        page.add_style_tag(content=PRINT_STYLE)

        print("Rendering PDF ...")
        page.pdf(
            path=str(pdf_file),
            format="A4",
            margin={"top": "0.9in", "right": "0.9in", "bottom": "0.9in", "left": "0.9in"},
            print_background=True,
        )
        browser.close()

    size_kb = pdf_file.stat().st_size / 1024
    print(f"Done: {pdf_file} ({size_kb:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description="Render a This Machine Press broadsheet HTML file to PDF via Playwright."
    )
    parser.add_argument("input", help="Path to the built HTML file")
    parser.add_argument("output", help="Path for the output PDF")
    args = parser.parse_args()
    render_pdf(args.input, args.output)


if __name__ == "__main__":
    main()
