#!/usr/bin/env python3
"""
Render an Inference issue HTML file to PDF using Playwright.

Loads the HTML in a headless Chromium browser, waits for Google Fonts
to finish loading, then prints to A4 PDF with 0.75in margins.

Usage:
    python3 scripts/render-inference.py public/inference/issue-7/index.html output.pdf
    python3 scripts/render-inference.py path/to/file.html path/to/output.pdf

Requirements:
    pip install playwright
    playwright install chromium
"""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def render_pdf(html_path: str, pdf_path: str) -> None:
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"Error: HTML file not found: {html_file}", file=sys.stderr)
        sys.exit(1)

    pdf_file = Path(pdf_path).resolve()
    pdf_file.parent.mkdir(parents=True, exist_ok=True)

    file_url = html_file.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        print(f"Loading {html_file.name} ...")
        page.goto(file_url, wait_until="networkidle")

        # Wait for Google Fonts to finish loading
        page.evaluate("() => document.fonts.ready")

        # Hide nav, footer chrome, and external-link buttons that don't
        # belong in a printed PDF
        page.add_style_tag(content="""
            @media print {
                nav, .site-header, .site-footer, .inference-external-link,
                .inference-footer-links { display: none !important; }
            }
            /* Also hide in screen context for the PDF render */
            nav, .site-header, .site-footer, .inference-external-link,
            .inference-footer-links { display: none !important; }
        """)

        print(f"Rendering PDF ...")
        page.pdf(
            path=str(pdf_file),
            format="A4",
            margin={
                "top": "0.75in",
                "right": "0.75in",
                "bottom": "0.75in",
                "left": "0.75in",
            },
            print_background=True,
        )

        browser.close()

    size_kb = pdf_file.stat().st_size / 1024
    print(f"Done: {pdf_file} ({size_kb:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description="Render an Inference HTML file to PDF via Playwright."
    )
    parser.add_argument("input", help="Path to the HTML file")
    parser.add_argument("output", help="Path for the output PDF")
    args = parser.parse_args()

    render_pdf(args.input, args.output)


if __name__ == "__main__":
    main()
