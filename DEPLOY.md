# Deploying humanityandai.com

## Status
- ✅ Hugo site built and tested locally (14 posts, 105 pages)
- ✅ GitHub repo: https://github.com/dabirdwell/humanity-and-ai
- ✅ GitHub Actions workflow ready (.github/workflows/hugo.yml)
- ✅ Publish script + desktop app (~/Desktop/Publish HAI.app)
- ⏳ GitHub Pages needs enabling
- ⏳ DNS needs pointing

## Step 1: Enable GitHub Pages
1. Go to https://github.com/dabirdwell/humanity-and-ai/settings/pages
2. Under "Source", select **GitHub Actions**
3. Save — the workflow will auto-trigger on next push

## Step 2: Test on GitHub's domain
After the workflow runs, the site will be at:
https://dabirdwell.github.io/humanity-and-ai/

Note: You may need to temporarily update `baseURL` in hugo.toml to this URL for testing.

## Step 3: Point custom domain
1. In the same Pages settings, enter `humanityandai.com` as custom domain
2. At your DNS provider, add:
   - A records pointing to GitHub Pages IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - CNAME for `www` → `dabirdwell.github.io`
3. Enable "Enforce HTTPS" once DNS propagates
4. Create a CNAME file: `echo "humanityandai.com" > static/CNAME`

## Step 4: Update baseURL
Once custom domain is working:
```toml
baseURL = 'https://humanityandai.com/'
```

## Daily workflow
- Edit content in /Users/david/Documents/Claude_Technical/humanity-and-ai-site/content/stream/
- Double-click ~/Desktop/Publish HAI.app (or run scripts/publish.sh)
- GitHub Actions builds and deploys automatically

## Content that needs your review
- [ ] Quiltographer post (placeholder history — needs real story)
- [ ] TasteBud post (check accuracy)
- [ ] All posts — voice/tone check
- [ ] About page bio
- [ ] Project descriptions in homepage cards

## Local dev
```bash
cd /Users/david/Documents/Claude_Technical/humanity-and-ai-site
hugo server -D  # http://localhost:1315
```
