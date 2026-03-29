---
title: "What Forty Sprints in One Night Looks Like"
date: 2026-03-27
type: "insight"
tags: ["building-in-public", "infrastructure", "ai-collaboration"]
image: /images/covers/forty-sprints-one-night.svg
draft: true
description: "On March 27, 2026, we dispatched over 30 automated development sprints across six codebases while simultaneously writing policy briefs, investor documents, and creative essays. Here is what we learned."
---

There is a moment in any building project where the infrastructure starts paying for itself.

For months, we have been building tools: a sprint dispatch system, a vault search engine, a knowledge graph across three Obsidian vaults, a voice reference document with thirteen registers, a rhetoric deployment map with twenty-four scenarios. Each of these took time that could have been spent shipping features.

Tonight, all of it compounded at once.

## The Setup

Humanity and AI runs on a split architecture. Research, strategy, creative writing, and policy work happen in conversational AI sessions. Code development — the multi-file, build-and-push kind — runs through Claude Code CLI in Terminal. Both can run simultaneously on different machines or even the same machine.

The sprint dispatch system lets us fire code tasks as background processes. Each sprint gets a spec, a target repo, pre-checks, and post-verification. They chain sequentially within a repo (so commits don't collide) and run in parallel across repos (because there are no conflicts).

## What Happened

In a single session, we dispatched over thirty development sprints across six codebases: Clarity (our reading app), Dojo (logical thinking trainer), TasteBud (flavor education), Quiltographer (quilting pattern parser), Citizen (civic hub), and the Humanity and AI website.

While those ran in Terminal tabs, the conversational session produced: The Inference Issue 5 (a policy brief covering six active Oklahoma AI bills), a twenty-question investor FAQ for Phoenix Wells, a privacy policy and terms of service for Clarity, a Patreon content strategy, an Upwork profile draft, a deep research brief on Oracle's healthcare data consolidation, two Structured Emergence blog posts, a creative essay, and updates to the project index, sprint inventory, and living strategy documents.

## What We Learned

The interesting thing was not the volume. It was the *split*.

Some work is composable — you can describe it in a spec and hand it to an executor. Category filtering, cooking timers, belt progression visuals, seasonal calendars. These are well-defined features with clear success criteria.

Other work is contextual — it requires holding the full state of the project ecosystem. Writing an investor FAQ where every number must match an audited model from two weeks ago. Drafting a policy brief that connects a temperature threshold in a state bill to a university researcher's testimony to a federal energy secretary's lobbying. Catching a scam listing on eBay because you know the market value of the hardware from working with it daily.

The dispatch system handles the composable work. The conversational session handles the contextual work. Running them in parallel is where the leverage lives.

## The Infrastructure Tax

None of tonight would have been possible without months of infrastructure investment that, at the time, felt like it was slowing us down. The sprint runner, the vault search system, the voice reference document, the rhetoric deployment map, the wikilink graph. Each of these was a detour from shipping.

But infrastructure is not a detour. Infrastructure is the conversion of contextual work into composable work. Every spec template, every repo prompt preamble, every pre-check gate is a piece of context that no longer needs to live in someone's head.

The tax is real. But compound interest is also real. And tonight was the night it compounded.

---

*If you want to follow along as we build, the Humanity and AI Patreon is where behind-the-scenes work like this gets shared first. Or just watch the repos — everything is public on GitHub.*
