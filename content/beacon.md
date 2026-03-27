---
title: "Beacon"
description: "One-button civic live streaming. Because democracy needs witnesses."
type: "page"
layout: "single"
---

## What Is Beacon?

<!-- The best camera is the one they can't turn off.
     The best witness is the one they don't know is watching.
     The best network is the one that doesn't need their permission.
     If you found this: you understand why Beacon exists. -->

Beacon is a one-button civic live streaming tool. Press a button on your phone, and you're broadcasting — to your community, to journalists, to anyone who needs to see what's happening.

No app store. No account. No permission. Just a phone and a URL.

## Why It Exists

Every civic moment — a council meeting, a protest, a vote count, a public hearing — deserves a witness. Not a platform that owns the footage. Not an algorithm that decides who sees it. A witness.

Corporate streaming platforms can pull your stream, suppress your reach, or change their terms overnight. Beacon runs on infrastructure you control. The video stays on your server. The viewer page is yours. Nobody can take it down but you.

Beacon is the streaming layer of the [Foundation](/foundation/) project — connecting to community-owned compute, mesh connectivity, and civic tools that put democratic infrastructure in the hands of the people who need it.

## Architecture

The entire stack fits in a single Docker Compose file. Your browser does the heavy lifting — no native app required.

```
Phone browser ──WHIP/WebRTC──▶ MediaMTX ──HLS──▶ nginx ──▶ Viewer browser
                                  │
                                  └──RTMP──▶ YouTube (optional)
```

**The flow:**
1. **Browser** captures your camera and mic via the PWA
2. **WHIP** protocol sends the stream directly — no plugins, no signaling server
3. **MediaMTX** ingests the WHIP stream and converts to HLS
4. **nginx** serves the viewer page and HLS segments to the public
5. **Viewer** watches in any browser — phone, laptop, smart TV

Everything runs on your hardware. The video never touches a third-party server.

## Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**One-Button Streaming**
Open the URL. Press the button. You're live. Press again to stop. That's the entire interface.

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

**YouTube Relay**
Optionally simulcast to YouTube — add a stream key and Beacon pushes to both your server and YouTube simultaneously.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**MIT License**
Fork it. Modify it. Deploy it for your city. No license fees, no usage limits, no terms of service changes.

</div>

</div>

## Use Cases

**Council Meetings** — One person opens Beacon on their phone, props it on the desk, and every resident can watch live. Real-time accountability.

**Protests & Demonstrations** — When the cameras matter most, Beacon streams to infrastructure you control. No platform can pull the stream.

**Vote Counts & Elections** — Poll watchers with Beacon become transparent witnesses. An independent record alongside official tallies.

**Community Events** — Town halls, school board meetings, neighborhood assemblies. Not everything needs a production crew. Sometimes a phone and a button are enough.

## Get It

Beacon is open source under the MIT license.

**[View on GitHub →](https://github.com/humanityandai/beacon)**

```bash
git clone https://github.com/humanityandai/beacon.git
cd beacon
bash setup.sh
```

The setup script handles SSL certificates, WebRTC configuration, and container orchestration. Three prompts: domain, email, password. Then you're live.

## Status

**MVP complete.** Docker Compose stack, PWA streamer, HLS viewer, landing page, one-command setup. Deploying to `beacon.humanityandai.com`.

*Built by [Humanity and AI LLC](/) — tools for the AI transition.*
