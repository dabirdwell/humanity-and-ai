#!/usr/bin/env bash
#
# Staged visualization disposition — written 2026-08-30, NOT executed by the audit.
# Companion to: Visualizations_Disposition_Audit_2026-08-26.md
#
# WHAT THIS DOES
#   Moves the 8 pages graded INTERNAL-OR-EXPERIMENTAL out of the public content
#   tree and into content/_archive_visualizations/.
#
#   Every move is a `git mv`. Nothing is deleted. Nothing is overwritten.
#   Every move is echoed. The whole thing is reversible with `git checkout -- .`
#   before you commit, or `git mv` back afterward.
#
#   The FICTION-OR-OFFTOPIC bucket is empty: penrose-tiling, luminas-whisper and
#   the rest are already gone from content/ and already 404 on the live site.
#   They survive only as stale build output in public/, which a clean rebuild clears.
#
# WHAT THIS DOES NOT DO
#   No rm. No git commit. No git push. No edits to hugo.toml. No rebuild.
#
# RUN IT WITH
#   bash _staged_viz_disposition_2026-08-26.sh
#

set -euo pipefail

REPO="/Users/david/Documents/Claude_Technical/humanity-and-ai-site"
SRC="$REPO/content/visualizations"
DEST="$REPO/content/_archive_visualizations"

# The 8 INTERNAL-OR-EXPERIMENTAL pages, with the one-line reason from the audit.
PAGES=(
  "brain-mastery-pipeline|Five-product funnel with a Try Clarity CTA. A product page, not a visualization."
  "why-oklahoma|Org marketing: Rep. Dollens contact, Clarity and Guardian AI plugs, family narrative."
  "the-5-3-scale|Job scores are one person's informal ratings, labeled approximations, shown as data."
  "the-dominoes|Cascade animation of a claim with no sources at all in the footer."
  "foundation-ripple|Diagram of our own framework; cascade weights admitted to be directional estimates."
  "ubc-circos|Chord diagram of our own proposal; footer says data derived from the Foundation framework."
  "seven-generation-fork|Two invented 175-year futures drawn with the visual authority of data."
  "the-mirror|Clean build, teaches nothing about the world: feelings mapped to our taxonomy, share card out."
)

echo ""
echo "=============================================================="
echo " Visualizations disposition — staged moves"
echo " Repo: $REPO"
echo "=============================================================="
echo ""

cd "$REPO"

if [ ! -d "$REPO/.git" ]; then
  echo "ERROR: $REPO is not a git repository. Refusing to run." >&2
  exit 1
fi

if [ ! -d "$SRC" ]; then
  echo "ERROR: source directory not found: $SRC" >&2
  exit 1
fi

echo "Working tree status before moves:"
git status --short -- content/visualizations/ || true
echo ""

# ---- create the archive directory -------------------------------------------
if [ -d "$DEST" ]; then
  echo "  archive directory already exists: $DEST"
else
  mkdir -p "$DEST"
  echo "  CREATED  $DEST"
fi

# ---- suppress the archive from the build ------------------------------------
# Hugo does NOT ignore underscore-prefixed directories. That is a Jekyll
# convention. Without this, a rebuild would republish all 8 pages at
# /_archive_visualizations/<slug>/, which is the opposite of the point.
# hugo.toml has no ignoreFiles key, so this _index.md is the first line of
# defense. Adding the ignoreFiles line (printed at the end) is the real one.
if [ -f "$DEST/_index.md" ]; then
  echo "  archive _index.md already present, leaving it alone"
else
  cat > "$DEST/_index.md" <<'ARCHIVE_INDEX'
---
title: "Archived Visualizations"
description: "Internal experiments, product pages, and framework self-portraits moved out of the public visualizations section on 2026-08-26. Not published."
draft: true
headless: true
---

Not public. Moved here by `_staged_viz_disposition_2026-08-26.sh`.
Graded INTERNAL-OR-EXPERIMENTAL in `Visualizations_Disposition_Audit_2026-08-26.md`.

Nothing here was deleted. Every file is a `git mv` away from its old home.
ARCHIVE_INDEX
  echo "  CREATED  $DEST/_index.md  (draft: true, headless: true)"
fi

echo ""
echo "--------------------------------------------------------------"
echo " Moving 8 pages"
echo "--------------------------------------------------------------"
echo ""

moved=0
skipped=0

for entry in "${PAGES[@]}"; do
  slug="${entry%%|*}"
  reason="${entry#*|}"
  from="$SRC/$slug.md"
  to="$DEST/$slug.md"

  if [ ! -f "$from" ]; then
    echo "  SKIP     $slug.md  (not found at $from)"
    skipped=$((skipped + 1))
    continue
  fi

  if [ -e "$to" ]; then
    echo "  SKIP     $slug.md  (destination already exists: $to — refusing to overwrite)"
    skipped=$((skipped + 1))
    continue
  fi

  git mv "$from" "$to"
  echo "  MOVED    content/visualizations/$slug.md  ->  content/_archive_visualizations/$slug.md"
  echo "           reason: $reason"
  moved=$((moved + 1))
done

echo ""
echo "--------------------------------------------------------------"
echo " Result: $moved moved, $skipped skipped, 0 deleted"
echo "--------------------------------------------------------------"
echo ""

remaining=$(ls -1 "$SRC"/*.md 2>/dev/null | grep -v '/_index\.md$' | wc -l | tr -d ' ')
echo "  content/visualizations/ now holds $remaining pages (was 26)."
echo "  Expected after a clean run: 18."
echo ""
echo "  Of those 18: 8 are PUBLIC-WORTHY and ready to feature,"
echo "               10 are FIXABLE and need the repairs named in the audit."
echo ""

echo "Staged changes:"
git status --short -- content/visualizations/ content/_archive_visualizations/ || true
echo ""

cat <<'NEXT_STEPS'
==============================================================
 BEFORE YOU REBUILD — one config line is required
==============================================================

Hugo does not ignore underscore-prefixed directories inside content/.
Your hugo.toml currently has no ignoreFiles key, so a rebuild right now
would publish the archived pages at /_archive_visualizations/<slug>/.

Add this line to hugo.toml:

    ignoreFiles = ['content/_archive_visualizations/.*']

Or, if you would rather not touch config, move the archive out of content/
entirely:

    mv content/_archive_visualizations _archive_visualizations

==============================================================
 THEN: rebuild and review locally before committing
==============================================================

  1. Rebuild clean, so the stale public/ output and its iCloud " 2"
     duplicate directories go away too:

         rm -rf public && npx hugo

  2. Serve it and actually look at the section with your own eyes:

         npx hugo server -D
         open http://localhost:1313/visualizations/

  3. Confirm all three:
       - the section lists 18 pages, not 26
       - none of the 8 archived slugs resolve anywhere
       - the 10 FIXABLE pages still have the render bugs the audit named
         (they were not repaired by this script, only graded)

  4. Only then commit. Nothing here has been committed or pushed.

         git add -A content/
         git commit -m "Archive 8 internal/experimental visualization pages"

  To undo everything before committing:

         git checkout -- content/ && rm -rf content/_archive_visualizations

==============================================================
NEXT_STEPS
