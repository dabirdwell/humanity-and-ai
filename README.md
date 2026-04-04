# Humanity and AI

[![Hugo Build CI](https://github.com/dabirdwell/humanity-and-ai/actions/workflows/deploy.yml/badge.svg)](https://github.com/dabirdwell/humanity-and-ai/actions/workflows/deploy.yml)

**Research. Tools. Ideas. Futures we direct.**

A living notebook from the intersection of humanity and artificial intelligence. Built with [Hugo](https://gohugo.io/).

This is the hub site for [Humanity and AI, LLC](https://humanityandai.com) — the parent organization encompassing:

- **[Structured Emergence](https://structuredemergence.com)** — Consciousness research
- **Foundation** — Political movement for human-AI partnership
- **Universal Basic Citizenship** — Policy framework
- **Phoenix Wells** — Infrastructure (abandoned wells → geothermal AI)
- **Software tools** — Quiltographer, TasteBud, and more
- **Creative work** — The Interpolated Mind, Lumina's Whisper, and Æ's writing

## Local Development

```bash
hugo server -D
```

## Social Cards (OG Images)

Auto-generated SVG social preview cards live in `static/social-cards/`. After adding or renaming content, regenerate them:

```bash
python3 scripts/generate-social-cards.py
```

Cards use the site's navy/teal/terracotta palette and display the post title, section tag, and site name. The `baseof.html` template automatically sets `og:image` to the matching card.

## Deploy

```bash
./scripts/publish.sh
```

## License

Content © David Alan Birdwell / Humanity and AI, LLC. All rights reserved.
