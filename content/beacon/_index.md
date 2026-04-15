---
title: "Beacon — One-Button Civic Live Streaming"
draft: true
description: "One-button PWA for live streaming civic events. Docker Compose stack with MediaMTX and nginx. WHIP protocol, camera toggle, HLS viewer."
---

## What Is Beacon?

Beacon is a one-button PWA for live streaming civic events — city council meetings, protests, public hearings, vote counts. Open a URL on your phone, press a button, and you're broadcasting to anyone with a browser.

No app store. No account. No platform that owns your footage.

The entire stack runs in a single Docker Compose file: **MediaMTX** ingests your camera via the WHIP protocol, converts to HLS, and **nginx** serves the viewer page. Everything runs on hardware you control.

```
Phone browser ──WHIP/WebRTC──▶ MediaMTX ──HLS──▶ nginx ──▶ Viewer browser
                                  │
                                  └──RTMP──▶ YouTube (optional)
```

## Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**One-Button Start**
Open the URL. Press the button. You're live. Press again to stop. That's the entire interface.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**Front / Back Camera Toggle**
Switch between front and rear cameras mid-stream. Point it at the speaker, then at the crowd — no interruption.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**Multiple Concurrent Viewers**
HLS output means anyone with the viewer URL can watch — phones, laptops, smart TVs. No viewer limit imposed by the app.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**Home Assistant Integration**
Trigger automations when a stream starts or stops. Turn on lights, send notifications, log events — Beacon fits into your existing smart home stack.

</div>

<div style="padding: 1.5rem; border: 1px solid var(--border-subtle, #2a2a3a); border-radius: 8px;">

**YouTube Relay**
Optionally simulcast to YouTube — add a stream key and Beacon pushes to both your server and YouTube simultaneously.

</div>

</div>

## Status

**Alpha.** Core streaming, camera toggle, viewer page, and Docker Compose deployment are working. Active development.

**[View on GitHub →](https://github.com/dabirdwell/beacon)**

## Part of the Civic Stack

Beacon is part of the Humanity and AI civic technology stack. View the source on [GitHub](https://github.com/dabirdwell/beacon).

*Built by [Humanity and AI LLC](/) — tools for the AI transition.*
