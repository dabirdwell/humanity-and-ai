#!/usr/bin/env python3
"""
Generate social preview cards for every published page.

A social preview card is the picture that appears when a page link is pasted
into YouTube, X, Bluesky, LinkedIn, Slack, or iMessage. Hugo writes the page's
card path into <meta property="og:image"> (see layouts/_default/baseof.html),
so the card file has to exist under exactly the name the template computes:

    page inside a section   ->  static/social-cards/<section>--<name>.png
                                (name = the file stem, or the directory name
                                 when the page is an _index.md)
    page at the content root -> static/social-cards/<name>.png
    site default             -> static/social-cards/og-default.png
                                (hugo.toml  params.ogImage)

Cards are drawn as SVG in memory and rendered to 1200x630 PNG with
rsvg-convert (brew install librsvg). PNG, not SVG, because the link-preview
crawlers at the big platforms do not render SVG.

Type: the site's own faces, Syne (labels) and Source Serif 4 (titles), bundled
under scripts/fonts/ with their SIL Open Font License texts. A fontconfig file
is written at run time so the renderer can see them without installing anything.

Usage:
    python3 scripts/generate-social-cards.py                 write every card
    python3 scripts/generate-social-cards.py --only inference--issue-28
    python3 scripts/generate-social-cards.py --svg-dir /tmp/cards   keep the SVGs too

Rewritten 2026-09-07 (first version July 17, 2026): names now match the
template for nested pages and section index pages, output is PNG, and the
palette is the current site's (dark ground, gold accent).
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
import textwrap

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT_DIR = os.path.join(ROOT, "content")
OUTPUT_DIR = os.path.join(ROOT, "static", "social-cards")
FONTS_DIR = os.path.join(ROOT, "scripts", "fonts")

WIDTH, HEIGHT = 1200, 630

# Current site palette (static/css, dark theme)
BG = "#0A0A0C"
BG_2 = "#161618"
GOLD = "#C8964E"
BLUE = "#8B9DBF"
TEXT = "#F0EDE6"

SERIF = "'Source Serif 4', Georgia, serif"
SANS = "'Syne', 'Helvetica Neue', sans-serif"

SECTION_LABELS = {
    "stream": "Stream",
    "foundation": "Foundation",
    "inference": "The Inference",
    "thismachine": "This Machine",
    "legislation": "Legislation",
    "visualizations": "Visualization",
    "phoenix-wells": "Phoenix Wells",
    "products": "The Studio",
    "brain-mastery": "Brain Mastery",
    "show": "The Show",
    "ae": "\u00c6",
    "research": "Research",
    "about": "About",
    "report": "Report",
    "hype-index": "Hype Index",
    "beacon": "Beacon",
    "convergences": "Convergences",
    "search": "Search",
}


def parse_frontmatter(path):
    """Return the YAML front matter as a flat dict (scalars only, no deps)."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^(\w[\w-]*)\s*:\s*(.+)$", line)
        if not km:
            continue
        key, val = km.group(1), km.group(2).strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        if val.lower() == "true":
            val = True
        elif val.lower() == "false":
            val = False
        data[key] = val
    return data or None


def card_name(path):
    """The file name the template will ask for, without extension.

    Mirrors layouts/_default/baseof.html: Hugo's .Section is the top-level
    content directory, and .File.ContentBaseName is the file stem, or the
    directory name for an _index.md.
    """
    rel = os.path.relpath(path, CONTENT_DIR)
    parts = rel.split(os.sep)
    stem = os.path.splitext(parts[-1])[0]
    if stem in ("_index", "index"):
        if len(parts) == 1:
            return None  # the home page has no file-based card; it uses the default
        stem = parts[-2]
    if len(parts) == 1:
        return stem
    return f"{parts[0]}--{stem}"


def section_of(path):
    rel = os.path.relpath(path, CONTENT_DIR)
    parts = rel.split(os.sep)
    return parts[0] if len(parts) > 1 else ""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def fit_title(title, max_width=990, max_lines=4):
    """Pick the largest size whose wrapped title fits in max_lines.
    0.53 is the measured average glyph width of Source Serif 4 at weight 600,
    as a fraction of the font size."""
    for size in (76, 68, 60, 54, 48, 42, 38):
        per_line = max(8, int(max_width / (size * 0.53)))
        lines = textwrap.wrap(title, width=per_line)
        if len(lines) <= max_lines:
            return size, lines
    size = 34
    lines = textwrap.wrap(title, width=int(max_width / (size * 0.53)))
    return size, lines[:max_lines]


def frame(inner):
    """Shared ground for every card: dark field, gold rule, faint ampersand,
    house name at the foot."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="{BG_2}"/>
    </linearGradient>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#g)"/>
  <rect x="0" y="0" width="{WIDTH}" height="6" fill="{GOLD}"/>
  <text x="1160" y="620" font-family="{SERIF}" font-style="italic" font-weight="400" font-size="480" fill="{GOLD}" opacity="0.09" text-anchor="end">&amp;</text>
{inner}
  <line x1="80" y1="{HEIGHT - 96}" x2="360" y2="{HEIGHT - 96}" stroke="{GOLD}" stroke-width="2" opacity="0.6"/>
  <text x="80" y="{HEIGHT - 56}" font-family="{SANS}" font-weight="700" font-size="26" fill="{TEXT}">Humanity and AI</text>
  <text x="80" y="{HEIGHT - 26}" font-family="{SANS}" font-weight="500" font-size="17" fill="{BLUE}" letter-spacing="1">humanityandai.com</text>
</svg>
"""


def page_card(title, section):
    label = SECTION_LABELS.get(section, section.replace("-", " ").title()) if section else ""
    size, lines = fit_title(title)
    lh = size * 1.18
    block = len(lines) * lh
    top, bottom = 150, HEIGHT - 130
    y0 = top + (bottom - top - block) / 2 + size * 0.8
    parts = []
    if label:
        parts.append(f'  <text x="80" y="104" font-family="{SANS}" font-weight="700" font-size="21" '
                     f'fill="{GOLD}" letter-spacing="4">{esc(label.upper())}</text>')
    for i, line in enumerate(lines):
        parts.append(f'  <text x="80" y="{y0 + i * lh:.0f}" font-family="{SERIF}" font-weight="600" '
                     f'font-size="{size}" fill="{TEXT}">{esc(line)}</text>')
    return frame("\n".join(parts))


def default_card(site_title, tagline, description):
    """og-default.png: the card for the home page and any page without a file."""
    parts = [
        f'  <text x="80" y="104" font-family="{SANS}" font-weight="700" font-size="21" '
        f'fill="{GOLD}" letter-spacing="4">{esc(tagline.upper())}</text>',
        f'  <text x="80" y="300" font-family="{SERIF}" font-weight="600" font-size="96" '
        f'fill="{TEXT}">{esc(site_title)}</text>',
    ]
    for i, line in enumerate(textwrap.wrap(description, width=58)[:3]):
        parts.append(f'  <text x="80" y="{372 + i * 40}" font-family="{SERIF}" font-weight="400" '
                     f'font-size="28" fill="{BLUE}">{esc(line)}</text>')
    return frame("\n".join(parts))


def site_params():
    """title, tagline and description out of hugo.toml (scalars only)."""
    vals = {}
    with open(os.path.join(ROOT, "hugo.toml"), encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^\s*(title|tagline|description)\s*=\s*['\"](.+)['\"]\s*$", line)
            if m and m.group(1) not in vals:      # first occurrence wins
                vals[m.group(1)] = m.group(2)
    return vals.get("title", "Humanity and AI"), vals.get("tagline", ""), vals.get("description", "")


def fontconfig_path():
    """A fontconfig file that adds scripts/fonts/ on top of the system fonts."""
    conf = f"""<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <include ignore_missing="yes">/opt/homebrew/etc/fonts/fonts.conf</include>
  <include ignore_missing="yes">/etc/fonts/fonts.conf</include>
  <dir>{FONTS_DIR}</dir>
  <cachedir>{os.path.join(tempfile.gettempdir(), "hai-social-cards-fc-cache")}</cachedir>
</fontconfig>
"""
    path = os.path.join(tempfile.gettempdir(), "hai-social-cards-fonts.conf")
    with open(path, "w", encoding="utf-8") as f:
        f.write(conf)
    return path


def render_png(svg, out_path, fc_conf):
    env = dict(os.environ, FONTCONFIG_FILE=fc_conf)
    res = subprocess.run(
        ["rsvg-convert", "-w", str(WIDTH), "-h", str(HEIGHT), "-f", "png", "-o", out_path],
        input=svg.encode("utf-8"), env=env, capture_output=True)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.decode("utf-8", "ignore").strip())


def content_files():
    for root, _dirs, files in os.walk(CONTENT_DIR):
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(root, name)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="generate a single card by name, e.g. inference--issue-28")
    ap.add_argument("--svg-dir", help="also write each card's SVG source into this directory")
    args = ap.parse_args()

    if subprocess.run(["which", "rsvg-convert"], capture_output=True).returncode != 0:
        sys.exit("rsvg-convert not found. Install it with: brew install librsvg")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if args.svg_dir:
        os.makedirs(args.svg_dir, exist_ok=True)
    fc_conf = fontconfig_path()

    seen = {}          # card name -> source path (collision check)
    written = skipped_draft = skipped_empty = 0
    collisions = []

    def emit(name, svg):
        nonlocal written
        if args.svg_dir:
            with open(os.path.join(args.svg_dir, name + ".svg"), "w", encoding="utf-8") as f:
                f.write(svg)
        render_png(svg, os.path.join(OUTPUT_DIR, name + ".png"), fc_conf)
        written += 1

    title, tagline, description = site_params()
    if not args.only or args.only == "og-default":
        emit("og-default", default_card(title, tagline, description))

    for path in content_files():
        name = card_name(path)
        if name is None:
            continue
        if args.only and name != args.only:
            continue
        fm = parse_frontmatter(path)
        if not fm or not fm.get("title"):
            skipped_empty += 1
            continue
        if fm.get("draft") is True:
            skipped_draft += 1
            continue
        if name in seen:
            collisions.append((name, seen[name], path))
            continue
        seen[name] = path
        emit(name, page_card(str(fm["title"]), section_of(path)))

    print(f"Wrote {written} PNG card(s) to {OUTPUT_DIR}")
    print(f"Skipped {skipped_draft} draft page(s) and {skipped_empty} file(s) with no title.")
    for name, first, second in collisions:
        print(f"COLLISION {name}: kept {os.path.relpath(first, ROOT)}, skipped {os.path.relpath(second, ROOT)}")


if __name__ == "__main__":
    main()
