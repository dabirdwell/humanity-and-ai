#!/usr/bin/env python3
"""
Generate SVG social preview cards for all content pages.

Reads Hugo content frontmatter (title, type, section) and produces
an OG-sized SVG card per page in static/social-cards/<slug>.svg.

Usage:
    python3 scripts/generate-social-cards.py

Palette: navy (#0f172a), teal (#14b8a6), terracotta (#c2410c)
"""

import os
import re
import textwrap

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "social-cards")

# Card dimensions (standard OG image)
WIDTH = 1200
HEIGHT = 630

# Palette
NAVY = "#0f172a"
NAVY_MID = "#1e293b"
TEAL = "#14b8a6"
TERRACOTTA = "#c2410c"
WARM = "#f97316"
WHITE = "#f8fafc"
MUTED = "#94a3b8"

# Section-to-label mapping
SECTION_LABELS = {
    "stream": "Stream",
    "foundation": "Foundation",
    "inference": "The Inference",
    "products": "Products",
    "ae": "Essay",
    "show": "The Show",
    "visualizations": "Visualization",
    "legislation": "Legislation",
    "brain-mastery": "Brain Mastery",
    "hype-index": "Hype Index",
    "report": "Report",
}

# Type-to-accent color
TYPE_COLORS = {
    "policy": TERRACOTTA,
    "stream": TEAL,
    "insight": "#6366f1",   # indigo
    "tool": "#22c55e",      # green
    "futurism": WARM,
    "community": "#a855f7", # purple
    "report": TERRACOTTA,
}


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file (no external deps)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    data = {}
    for line in match.group(1).splitlines():
        # Simple key: value parsing — sufficient for Hugo scalar fields
        m = re.match(r'^(\w[\w-]*)\s*:\s*(.+)', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip().strip('"').strip("'")
            if val.lower() == "true":
                val = True
            elif val.lower() == "false":
                val = False
            data[key] = val
    return data if data else None


def slug_from_path(filepath):
    """Derive a slug from the file path relative to content/."""
    rel = os.path.relpath(filepath, CONTENT_DIR)
    # Remove .md extension
    slug = os.path.splitext(rel)[0]
    # Handle index.md inside leaf bundles
    if slug.endswith("/index"):
        slug = slug[:-6]
    # Flatten path separators into dashes for uniqueness
    slug = slug.replace(os.sep, "--")
    return slug


def section_from_path(filepath):
    """Get the top-level section from the file path."""
    rel = os.path.relpath(filepath, CONTENT_DIR)
    parts = rel.split(os.sep)
    if len(parts) > 1:
        return parts[0]
    return ""


def escape_xml(text):
    """Escape text for safe XML embedding."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def wrap_title(title, max_chars=32):
    """Wrap title into lines that fit the card."""
    lines = textwrap.wrap(title, width=max_chars)
    return lines[:4]  # max 4 lines


def generate_svg(title, section, content_type, slug):
    """Generate an SVG social card."""
    section_label = SECTION_LABELS.get(section, section.replace("-", " ").title())
    type_label = content_type.strip('"') if content_type else section_label
    accent = TYPE_COLORS.get(type_label.lower() if type_label else "", TEAL)

    lines = wrap_title(title)
    # Adjust font size based on title length
    if len(lines) <= 1:
        font_size = 56
    elif len(lines) == 2:
        font_size = 48
    elif len(lines) == 3:
        font_size = 42
    else:
        font_size = 36

    line_height = font_size * 1.25

    # Vertical centering: title block starts roughly centered
    title_block_height = len(lines) * line_height
    title_start_y = 200 + (240 - title_block_height) / 2

    title_lines_svg = ""
    for i, line in enumerate(lines):
        y = title_start_y + i * line_height
        title_lines_svg += (
            f'    <text x="80" y="{y:.0f}" '
            f'font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="{font_size}" font-weight="700" '
            f'fill="{WHITE}">{escape_xml(line)}</text>\n'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <linearGradient id="bg-{slug}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{NAVY}"/>
      <stop offset="100%" stop-color="{NAVY_MID}"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg-{slug})"/>

  <!-- Accent stripe -->
  <rect x="0" y="0" width="{WIDTH}" height="6" fill="{accent}"/>

  <!-- Decorative corner marks -->
  <line x1="60" y1="60" x2="60" y2="100" stroke="{accent}" stroke-width="2" opacity="0.5"/>
  <line x1="60" y1="60" x2="100" y2="60" stroke="{accent}" stroke-width="2" opacity="0.5"/>
  <line x1="{WIDTH - 60}" y1="{HEIGHT - 60}" x2="{WIDTH - 60}" y2="{HEIGHT - 100}" stroke="{accent}" stroke-width="2" opacity="0.5"/>
  <line x1="{WIDTH - 60}" y1="{HEIGHT - 60}" x2="{WIDTH - 100}" y2="{HEIGHT - 60}" stroke="{accent}" stroke-width="2" opacity="0.5"/>

  <!-- Section tag -->
  <rect x="80" y="120" width="{len(section_label) * 12 + 32}" height="36" rx="4" fill="{accent}" opacity="0.9"/>
  <text x="96" y="145" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" fill="{WHITE}" letter-spacing="0.5">{escape_xml(section_label.upper())}</text>

  <!-- Title -->
{title_lines_svg}
  <!-- Divider -->
  <line x1="80" y1="{HEIGHT - 120}" x2="400" y2="{HEIGHT - 120}" stroke="{accent}" stroke-width="2" opacity="0.4"/>

  <!-- Site name -->
  <text x="80" y="{HEIGHT - 75}" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="600" fill="{MUTED}">Humanity and AI</text>
  <text x="80" y="{HEIGHT - 48}" font-family="system-ui, -apple-system, sans-serif" font-size="15" fill="{MUTED}" opacity="0.7">humanityandai.com</text>

  <!-- Type badge (right side) -->
  <text x="{WIDTH - 80}" y="{HEIGHT - 60}" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="{accent}" text-anchor="end" letter-spacing="1.5" opacity="0.8">{escape_xml(type_label.upper())}</text>
</svg>"""
    return svg


def find_content_files():
    """Walk the content directory and yield markdown file paths."""
    for root, dirs, files in os.walk(CONTENT_DIR):
        # Skip _index.md files (section list pages)
        for fname in files:
            if fname.endswith(".md") and fname != "_index.md":
                yield os.path.join(root, fname)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generated = 0
    skipped = 0

    for filepath in sorted(find_content_files()):
        fm = parse_frontmatter(filepath)
        if fm is None:
            skipped += 1
            continue

        title = fm.get("title", "")
        if not title:
            skipped += 1
            continue

        # Skip drafts
        if fm.get("draft", False):
            skipped += 1
            continue

        content_type = fm.get("type", "")
        section = section_from_path(filepath)
        slug = slug_from_path(filepath)

        svg = generate_svg(title, section, content_type, slug)

        out_path = os.path.join(OUTPUT_DIR, f"{slug}.svg")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg)

        generated += 1

    print(f"Generated {generated} social cards in static/social-cards/")
    if skipped:
        print(f"Skipped {skipped} files (no title, draft, or missing frontmatter)")


if __name__ == "__main__":
    main()
