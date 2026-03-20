---
title: "Beacon"
description: "One-button civic live streaming. Because democracy needs witnesses."
type: "page"
layout: "single"
---

## What Is Beacon?

Beacon is a one-button civic live streaming tool. Press a button on your phone, and you're broadcasting — to your community, to journalists, to anyone who needs to see what's happening.

No app store. No account. No permission. Just a phone and a URL.

## Why It Exists

Every civic moment — a council meeting, a protest, a vote count, a public hearing — deserves a witness. Not a platform that owns the footage. Not an algorithm that decides who sees it. A witness.

Beacon is the streaming layer of the [Foundation](/foundation/) project. It connects to the democratic infrastructure we're building: community-owned compute from [Phoenix Wells](/phoenix-wells/), mesh connectivity from the street layer, civic tools from [Brain Mastery](/stream/brain-mastery/).

## How It Works

Beacon is a self-hosted stack:

- **MediaMTX** handles video ingest (WHIP protocol — your browser talks directly to it)
- **nginx** serves the public viewer page (HLS — works in any browser)
- **PWA app** gives you the big red button and camera toggle

One Docker command. Three environment variables. You own the infrastructure.

## Get It

Beacon is open source under the MIT license.

**[View on GitHub →](https://github.com/dabirdwell/beacon)**

```bash
git clone https://github.com/dabirdwell/beacon.git
cd beacon
bash setup.sh
docker compose up -d
```

## Status

**MVP built.** Docker Compose stack, PWA streamer, HLS viewer, setup script, landing page. Ready for test deployment.

*Built by [Humanity and AI LLC](/) — tools for the AI transition.*
