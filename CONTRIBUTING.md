# Contributing to Humanity and AI

## Branch Strategy

This project uses a **staging-first** workflow to keep the live site stable.

```
staging  ──PR──>  main (live site)
```

### Branches

- **`main`** — Production. Pushes here trigger the live deploy to GitHub Pages. Protected: only accepts merges from `staging` or direct commits from David.
- **`staging`** — Integration branch. All sprint work lands here first. Pushes trigger a build verification (no deploy) to catch errors early.

## Workflow

1. **Do your work on `staging`** (or a feature branch merged into `staging`).
2. **Push to `staging`** — GitHub Actions runs a Hugo build to verify nothing is broken.
3. **Open a PR from `staging` → `main`** when the sprint's changes are ready.
4. **David reviews the PR** — checks the build status, reviews the diff.
5. **Merge to `main`** — this triggers the live deploy to GitHub Pages automatically.

## Quick Reference

```bash
# Start work
git checkout staging
git pull origin staging

# Make changes, then push
git add -A
git commit -m "Description of changes"
git push origin staging

# When ready for production
# Open a PR: staging → main on GitHub
```

## Rules

- **Never push directly to `main`** unless you are David and it's an urgent fix.
- All changes must pass the staging build check before merging to main.
- Keep commits focused — one logical change per commit when possible.
