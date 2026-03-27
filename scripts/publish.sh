#!/bin/bash
# Publish Humanity and AI site to GitHub
# Usage: ./scripts/publish.sh

SITE_DIR="/Users/david/Documents/Claude_Technical/humanity-and-ai-site"
cd "$SITE_DIR" || exit 1

# Check for changes
if git diff --quiet && git diff --cached --quiet; then
    osascript -e 'display notification "No changes to publish" with title "Humanity & AI"'
    echo "No changes to publish."
    exit 0
fi

# Count changes
CHANGES=$(git status --porcelain | wc -l | tr -d ' ')

# Stage, commit, push
git add -A
git commit -m "Update: ${CHANGES} files changed — $(date '+%b %d, %Y %I:%M %p')"
git push origin main

if [ $? -eq 0 ]; then
    osascript -e "display notification \"${CHANGES} files pushed to GitHub\" with title \"Humanity & AI\" subtitle \"Published successfully\""
    echo "Published successfully: ${CHANGES} files."
else
    osascript -e 'display notification "Push failed — check terminal" with title "Humanity & AI" subtitle "Error"'
    echo "Push failed."
    exit 1
fi
