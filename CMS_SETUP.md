# Sveltia CMS — Setup, Operations, and Editor Manual

This is the one-stop doc for running the H&AI Sveltia CMS install.

## TL;DR — What you can do once OAuth works

- Visit **<https://humanityandai.com/admin/>**, click **Login with GitHub**.
- Browse, filter, edit, and publish all 100+ stream posts, 16 Foundation essays, plus Visualizations, Show episodes, Æ Creative, Products, Inference, Report, and section landings.
- Set `Draft = true` or `false` on any entry. Drafts render at **<https://humanityandai.com/preview/>**, never on the live site.
- Every content page on the live site shows an **"✎ Edit this page"** link in the footer that deep-links to that exact entry's editor.

---

## The one manual step David has to do (2 clicks)

The Cloudflare Worker at `sveltia-cms-auth.davidbirdwell.workers.dev` is the OAuth proxy that brokers logins between Sveltia and GitHub. It needs **two secrets** set on the Worker side. These cannot be set from this repo — they must be set in the Cloudflare dashboard.

### Required Worker secrets

| Secret name | Value | Where to find it |
|---|---|---|
| `GITHUB_CLIENT_ID` | `Ov23lis4oErYLzX5a7uj` | GitHub OAuth App we already created. |
| `GITHUB_CLIENT_SECRET` | (generate fresh) | GitHub OAuth App → **Generate a new client secret**. Copy immediately — GitHub only shows it once. |

### Steps

1. **Get the client secret.** Open <https://github.com/settings/developers> → click the H&AI OAuth App (`Ov23lis4oErYLzX5a7uj`) → "Generate a new client secret". Copy it.
2. **Open the Worker.** Cloudflare dashboard → Workers & Pages → `sveltia-cms-auth` → **Settings** tab → **Variables and Secrets**.
3. **Add the two secrets.** Click "Add" twice — once for `GITHUB_CLIENT_ID`, once for `GITHUB_CLIENT_SECRET`. Set type to **Secret**, not Text. Save / Deploy.

### How to verify the Worker is configured

```bash
# Anonymous health check — the Worker should respond, not 404.
curl -I https://sveltia-cms-auth.davidbirdwell.workers.dev/

# This redirect endpoint requires the client_id to be set on the Worker side.
# A correctly configured Worker redirects (302) to github.com/login/oauth/authorize.
# A misconfigured Worker returns 500 or an error body.
curl -sI "https://sveltia-cms-auth.davidbirdwell.workers.dev/auth?provider=github&site_id=humanityandai.com&scope=repo" | head -5
```

If `curl` shows `HTTP/2 302` with a `location:` header pointing at `github.com`, the secrets are wired correctly. If you see 500 or a JSON error body mentioning `client_id`/`client_secret`, the secrets aren't set.

The real end-to-end test: go to <https://humanityandai.com/admin/>, click **Login with GitHub**. If a GitHub authorization page appears and (after authorizing) you land back on `/admin/` with the collection list visible, you're done.

### GitHub OAuth App callback URL

Make sure the OAuth App at <https://github.com/settings/developers> has its **Authorization callback URL** set to:

```
https://sveltia-cms-auth.davidbirdwell.workers.dev/callback
```

If it's set to anything else (e.g. an old Netlify URL), the login will fail with a redirect-mismatch error.

---

## Architecture

```
┌──────────────────────┐      ┌───────────────────────────┐      ┌─────────────────┐
│ humanityandai.com    │      │ sveltia-cms-auth          │      │ GitHub          │
│   /admin/            │ ───▶ │   .workers.dev            │ ───▶ │ OAuth + Repo    │
│ (Sveltia CMS JS)     │      │ (Cloudflare Worker proxy) │      │ (commits)       │
└──────────────────────┘      └───────────────────────────┘      └─────────────────┘
            │                                                            │
            │                  commit on save                            │
            └────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │ GitHub Actions       │
                            │ → build live (main)  │
                            │ → build drafts to    │
                            │   /preview/ subpath  │
                            └──────────────────────┘
```

Costs: $0/mo. GitHub Pages is free; Cloudflare Workers free tier (100k req/day) is more than enough for an OAuth proxy you hit a few times a session.

---

## What the CMS gives you

### Collections

- **Pages** — top-level pages (About, Sanctuary, TasteBud, Subscribe, Pattern).
- **Section Landing Pages** — every `_index.md` (Stream, Foundation, Inference, Legislation, Visualizations, Show, Beacon, Brain Mastery, Hype Index, Phoenix Wells, Products, Report, Research, Æ).
- **Stream Posts** — folder collection. Create / edit / delete. Filtered by Draft/Published and post Type.
- **Foundation Essays** — 16 essays, locked (no create/delete). Filtered by Status and Draft.
- **The Inference** — newsletter issue archive.
- **LegislAItive Report** — older newsletter archive.
- **Visualizations** — interactive pages.
- **Show Episodes** — episodes + format pages.
- **Æ Creative** — Æ-attributed pieces.
- **Products** — Beacon, Citizen, Clarity, Dojo, Gifio, Grove, Inference, Quiltographer, TasteBud.

Each post-type collection has:
- **Filters** — Drafts, Published, plus a few status-specific ones.
- **Groups** — group entries by Status, Draft, or (Stream) Year.
- **Sortable fields** — date, title, weight, status, draft.
- **Live preview links** — open in `/preview/` so you see drafts rendered.

### Draft control

Every content type that should have draft control has a `draft` boolean field. Hugo's default behavior:
- `draft: true` → never rendered on the live site (`humanityandai.com`).
- `draft: false` or no `draft` field → rendered on the live site.
- The preview build at `/preview/` shows **both** drafts and live.

So: setting `Draft = true` in Sveltia immediately hides a page from live. The next push deploys it. You can preview the draft at `humanityandai.com/preview/<section>/<slug>/`.

### Preview deployment

The GitHub Actions workflow at `.github/workflows/hugo.yml` does two builds per deploy:

1. **Live build** → `public/` at `https://humanityandai.com/` (no drafts, no future-dated posts).
2. **Preview build** → `public/preview/` at `https://humanityandai.com/preview/` (drafts + future + expired included).

Both are uploaded as one Pages artifact. `/preview/` is blocked in `static/robots.txt` and gets its own `Disallow: /` robots inside `/preview/`, so search engines should ignore it. (It is still publicly reachable to anyone with the URL — treat it as obscurity, not security.)

### Edit-this-page links

Every Hugo page that maps to a CMS entry now renders a small **"✎ Edit this page"** link in the footer. Clicking it opens Sveltia at exactly that entry. The mapping lives in `layouts/partials/edit-link.html`. If you ever add a new section, add it to the two dicts in that partial.

---

## Editor workflow — daily ops

### Reviewing what's live vs draft

1. Open the CMS, pick a collection (e.g. **Stream Posts**).
2. Click the filter row → **Drafts** to see in-progress posts.
3. Click an entry, eyeball it, flip **Draft → false**, hit **Save**. Done — site rebuilds in ~2 min.

### Quick edit from the live site

1. Browsing humanityandai.com, see a typo.
2. Scroll to the bottom of the page → click **✎ Edit this page**.
3. Sveltia opens that exact entry. Fix. Save.

### Bulk demote — pull a bunch of posts back to draft

There's no native bulk action in Sveltia (yet). For mass demotions, fastest path is:

```bash
# Example: mark all stream posts as draft. Adjust the glob.
for f in content/stream/*.md; do
  if ! grep -q '^draft:' "$f"; then
    # insert draft: true after the title line
    sed -i '' '/^title:/a\
draft: true\
' "$f"
  else
    sed -i '' 's/^draft: false/draft: true/' "$f"
  fi
done
git diff --stat
git add content/stream
git commit -m "Demote all stream posts to draft for editorial review"
git push
```

Then go to the CMS and individually re-publish reviewed ones.

### Adding a new section

If you add a new content folder (e.g. `content/podcast/`):

1. Add a new collection block to `static/admin/config.yml` (copy the Stream Posts block and adapt).
2. Add the section to both dicts in `layouts/partials/edit-link.html` so the edit-this-page link works.
3. If it has an `_index.md`, add a Section Landing entry to the `section_landings` files list.

---

## Troubleshooting

### "Login with GitHub" pops a window, then nothing happens
- The Worker likely isn't responding. Run the `curl` health check above. If it returns 500, the secrets are missing — follow the manual step.

### "Repository not found" / 404 after login
- The signed-in user must have **push** access to `dabirdwell/humanity-and-ai`. Sveltia uses your GitHub permissions directly.

### Sveltia loads but the editor is blank / no collections
- Open browser devtools → Console. If you see a YAML parse error, recheck `static/admin/config.yml`. Run `python3 -c "import yaml; yaml.safe_load(open('static/admin/config.yml'))"` locally to validate before committing.

### Preview at `/preview/<x>/` is 404
- The page isn't a draft, or doesn't exist yet, or the latest deploy hasn't finished. Check the **Deploy Hugo site to GitHub Pages** Actions run.

### I broke the workflow and now the site is gone
- The previous Pages deployment stays live until the next successful one. Revert the workflow file, push, and the next deploy fixes it.

---

## File map — what changed in this sprint

| File | Why |
|---|---|
| `static/admin/config.yml` | Modernized — added `site_url`, `display_url`, `media_libraries`, `show_preview_links`, `preview_path` per collection, view filters/groups across all post types, draft fields on Æ and Visualizations, commit message templates, plus missing section landings (Beacon, Brain Mastery, Phoenix Wells, Research). |
| `static/admin/index.html` | Pinned `@sveltia/cms` to the 0.x major to avoid surprise breaking releases. Added `noindex,nofollow` and a favicon. |
| `.github/workflows/hugo.yml` | Added the `/preview/` subpath build with `--buildDrafts --buildFuture`. Both builds ship in one deploy. |
| `static/robots.txt` | `Disallow: /preview/` and `Disallow: /admin/`. |
| `layouts/partials/edit-link.html` | New. Renders "✎ Edit this page" deep-linked to the right Sveltia entry. |
| `layouts/_default/baseof.html` | Includes the edit-link partial in the global `<main>` so every page gets it for free. |
| `CMS_SETUP.md` | This file. |

`static/admin/config.yml.bak` is the original starter config from when only Stream was wired up. Kept for reference; safe to delete.
