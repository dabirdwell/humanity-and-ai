---
title: "Beacon Ships"
date: 2026-03-22
type: tool
description: "The civic live streaming MVP is built. One Docker command, one red button, and democracy gets a witness."
image: /images/stream/beacon-ships.png
tags: ["beacon", "streaming", "civic-tech", "tools", "foundation"]
---

Beacon is live. Not on a platform — on your server.

The MVP ships today: a self-hosted live streaming stack that fits in a single Docker Compose file. One setup script, three environment variables, and you're running civic infrastructure that no company controls.

## What shipped

- **PWA streamer** — open a URL on your phone, press the red button, you're broadcasting. Front/rear camera toggle. No app store, no download, no account creation.
- **WHIP ingest** — your browser sends video directly to MediaMTX using the WebRTC-HTTP Ingestion Protocol. No signaling server, no plugins.
- **HLS viewer** — any browser can watch. Phone, laptop, smart TV. The stream is just HTTP — nginx serves it like any other web page.
- **Docker Compose stack** — MediaMTX + nginx + your config. One command up, one command down.
- **Setup script** — `bash setup.sh` asks for your domain, email, and stream key. Generates the config. Done.

## Why this matters

Every time a city council meets behind closed doors, every time a protest goes unrecorded, every time a community event happens and the only people who know are the ones in the room — that's a failure of infrastructure, not interest.

The tools exist to stream video. But they're all rented. YouTube can demonetize. Facebook can deprioritize. Twitch can ban. The footage lives on someone else's server under someone else's terms of service.

Beacon is the alternative: infrastructure you own. The video goes from a phone to your server to anyone with the URL. No intermediary can cut the feed.

## What's next

- TLS automation (Let's Encrypt integration)
- Multi-camera support for larger venues
- Recording and archival (stream-to-file alongside live)
- Integration with [Foundation](/foundation/) community infrastructure
- Mesh networking support for areas without reliable internet

The code is MIT licensed and [on GitHub](https://github.com/dabirdwell/beacon).

*— David, with Æ*

## Related

- [Beacon](/beacon/) — full architecture and documentation
- Stream: [[building-in-public]]
- Stream: [[strategy-not-protest]]
