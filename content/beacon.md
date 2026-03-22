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

## Architecture

The entire stack fits in a single Docker Compose file. Your browser does the heavy lifting — no native app required.

<div style="text-align: center; margin: 2rem 0;">
<img src="/images/beacon-architecture.svg" alt="Beacon architecture: Browser sends video via WHIP to MediaMTX, which converts to HLS served by nginx to viewers" style="max-width: 100%; height: auto;" />
</div>

**The flow:**
1. **Browser** captures your camera and mic via the PWA
2. **WHIP** protocol sends the stream directly — no plugins, no Flash, no WebRTC signaling server
3. **MediaMTX** ingests the WHIP stream and transcodes to HLS
4. **HLS** segments go to disk, ready for any standard player
5. **nginx** serves the viewer page and HLS segments to the public
6. **Viewer** watches in any browser — phone, laptop, smart TV

Everything runs on your hardware. The video never touches a third-party server.

## Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**One-Button Streaming**
Open the URL. Press the red button. You're live. Press again to stop. That's the entire interface.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**Camera Toggle**
Switch between front and rear cameras mid-stream. Point it at the speaker, then at the crowd — no interruption.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**No App Store**
Beacon is a PWA. Share a link, and the streamer has the app. No download, no approval process, no gatekeepers.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**Self-Hosted**
One `docker compose up` command. You own the server, the video, and the viewer page. No cloud dependency.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**MIT License**
Fork it. Modify it. Deploy it for your city. No license fees, no usage limits, no terms of service changes.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**Three Environment Variables**
`DOMAIN`, `EMAIL`, `STREAM_KEY`. That's the entire configuration. The setup script handles the rest.

</div>

</div>

## The PWA Interface

<div style="display: flex; flex-wrap: wrap; gap: 2rem; justify-content: center; margin: 2rem 0;">

<div style="text-align: center;">
<img src="/images/beacon-pwa-idle.svg" alt="Beacon PWA idle state — large red GO LIVE button with camera toggle" style="max-width: 280px; height: auto;" />
<p style="color: var(--text-muted, #68687a); font-size: 0.85rem; margin-top: 0.5rem;">Idle — ready to stream</p>
</div>

<div style="text-align: center;">
<img src="/images/beacon-pwa-live.svg" alt="Beacon PWA live state — pulsing red indicator with STOP button" style="max-width: 280px; height: auto;" />
<p style="color: var(--text-muted, #68687a); font-size: 0.85rem; margin-top: 0.5rem;">Live — broadcasting</p>
</div>

</div>

## Use Cases

**Council Meetings**
Your city council meets Tuesday night. One person opens Beacon on their phone, props it on the desk, and every resident can watch live. No FOIA request. No waiting for minutes. Real-time accountability.

**Protests & Demonstrations**
When the situation is tense and the cameras matter most, Beacon streams to infrastructure you control. No platform can pull the stream. No algorithm can suppress it. The footage exists on your server.

**Vote Counts & Elections**
Poll watchers with Beacon become transparent witnesses. The public stream creates an independent record alongside official tallies. Trust through visibility.

**Community Events**
Town halls, school board meetings, neighborhood assemblies, mutual aid distributions. Not everything needs a production crew. Sometimes a phone and a red button are enough.

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
