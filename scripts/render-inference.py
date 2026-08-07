#!/usr/bin/env python3
"""
Render an Inference issue HTML file to PDF using Playwright.

Loads the HTML in a headless Chromium browser, waits for Google Fonts
to finish loading, then prints to A4 PDF with 0.75in margins.

Usage:
    python3 scripts/render-inference.py public/inference/issue-7/index.html output.pdf
    python3 scripts/render-inference.py path/to/file.html path/to/output.pdf

    # Also drop a vault-only "## Related" wikilinks section from the render
    # (DOM-only; never touches the source markdown):
    python3 scripts/render-inference.py --strip-related in.html out.pdf

Requirements:
    pip install playwright
    playwright install chromium
"""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


# Runs before any page script on every navigation. Setting the
# "hai_welcomed" flag means the first-visit welcome overlay's own JS
# (in layouts/_default/baseof.html) short-circuits and never schedules
# the timer that adds the .visible class, so the overlay stays hidden.
# Wrapped in try/catch because file:// origins can restrict localStorage.
DISMISS_WELCOME_INIT = """
try { localStorage.setItem('hai_welcomed', '1'); } catch (e) {}
"""

# Belt-and-suspenders: even if the overlay is inserted or shown, force it
# (and the skip-to-content link) out of the print/screen layout. The
# welcome overlay lives in baseof.html as .welcome-overlay/#welcomeOverlay
# with a "Got it" dismiss; the skip link is <a class="skip-link"
# href="#main-content">. None of these belong in a printed PDF.
HIDE_CHROME_CSS = """
    @media print {
        nav, .site-header, .site-footer, .inference-external-link,
        .inference-footer-links, .welcome-overlay, #welcomeOverlay,
        .skip-link, a[href="#main-content"] { display: none !important; }
    }
    /* Also hide in screen context for the PDF render */
    nav, .site-header, .site-footer, .inference-external-link,
    .inference-footer-links, .welcome-overlay, #welcomeOverlay,
    .skip-link, a[href="#main-content"] { display: none !important; }
"""

# Removes a trailing "## Related" wikilinks section (a vault-only authoring
# convention) from the rendered DOM before printing. Returns the stripped
# heading text, or null if no Related section was present. This only edits
# the in-browser DOM -- the source markdown file is never modified.
STRIP_RELATED_JS = r"""
() => {
    const scope = document.querySelector('.inference-content') || document.body;
    const heads = Array.from(scope.querySelectorAll('h2'));
    for (const h of heads) {
        const isRelated = h.id === 'related'
            || h.textContent.trim().toLowerCase() === 'related';
        if (!isRelated) continue;
        let node = h.nextElementSibling;
        const toRemove = [];
        // Remove everything up to the next h1/h2 (or end of the section).
        while (node && !/^H[12]$/.test(node.tagName)) {
            toRemove.push(node);
            node = node.nextElementSibling;
        }
        toRemove.forEach(n => n.remove());
        h.remove();
        return 'Related';
    }
    return null;
}
"""


def render_pdf(html_path: str, pdf_path: str, strip_related: bool = False) -> None:
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

        # Suppress the first-visit welcome overlay before the page's own
        # scripts run.
        page.add_init_script(DISMISS_WELCOME_INIT)

        print(f"Loading {html_file.name} ...")
        page.goto(file_url, wait_until="networkidle")

        # Wait for Google Fonts to finish loading
        page.evaluate("() => document.fonts.ready")

        # Hide nav, footer chrome, welcome overlay, skip link, and
        # external-link buttons that don't belong in a printed PDF.
        page.add_style_tag(content=HIDE_CHROME_CSS)

        if strip_related:
            stripped = page.evaluate(STRIP_RELATED_JS)
            if stripped:
                print("Stripped vault-only '## Related' section from the render.")
            else:
                print("No '## Related' section found (nothing to strip).")

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
    parser.add_argument(
        "--strip-related",
        action="store_true",
        help="Drop a trailing vault-only '## Related' wikilinks section from "
        "the rendered PDF (DOM-only; the source markdown is never modified).",
    )
    args = parser.parse_args()

    render_pdf(args.input, args.output, strip_related=args.strip_related)


if __name__ == "__main__":
    main()
