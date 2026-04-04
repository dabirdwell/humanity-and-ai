#!/usr/bin/env bash
#
# Render the latest Inference issue to PDF.
#
# Finds the highest-numbered issue HTML in public/inference/,
# renders it to static/pdf/inference-issue-N.pdf.
#
# Usage:
#   ./scripts/render-inference.sh            # latest issue
#   ./scripts/render-inference.sh 5          # specific issue number
#

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PUBLIC_DIR="$REPO_ROOT/public/inference"
OUTPUT_DIR="$REPO_ROOT/static/pdf"

if [ "${1:-}" != "" ]; then
    ISSUE_NUM="$1"
else
    # Find the highest-numbered issue directory
    ISSUE_NUM=$(ls -d "$PUBLIC_DIR"/issue-* 2>/dev/null \
        | sed 's/.*issue-//' \
        | sort -n \
        | tail -1)

    if [ -z "$ISSUE_NUM" ]; then
        echo "Error: No issue directories found in $PUBLIC_DIR" >&2
        echo "Run 'hugo' first to build the site." >&2
        exit 1
    fi
fi

HTML_FILE="$PUBLIC_DIR/issue-${ISSUE_NUM}/index.html"
PDF_FILE="$OUTPUT_DIR/inference-issue-${ISSUE_NUM}.pdf"

if [ ! -f "$HTML_FILE" ]; then
    echo "Error: $HTML_FILE not found" >&2
    echo "Run 'hugo' first to build the site, or check the issue number." >&2
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo "Rendering Issue #${ISSUE_NUM} → ${PDF_FILE}"
python3 "$REPO_ROOT/scripts/render-inference.py" "$HTML_FILE" "$PDF_FILE"
