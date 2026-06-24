---
title: "Paper 1: The Fossil and the Signal"
date: 2026-05-13
layout: single
description: "Our first research paper is published. Large language models process ambiguity differently, but the way they express that difference is a fossil of their training, not a feature of their architecture."
tags: ["research", "structured-emergence", "probe-4", "fossil-emotion"]
---

Today we published our first research paper.

["Behavioral Signatures of Ambiguity Processing in Transformer-Based Language Models"](https://doi.org/10.5281/zenodo.20161483) is now available on Zenodo under open access. It reports a pre-registered finding that has implications for how the AI safety field evaluates model behavior.

## The Finding

We gave language models a simple task: read a short scenario and make a decision. One version of the scenario contained a genuinely ambiguous word. The other didn't. Everything else was identical.

The models produced significantly more output when the input was ambiguous. Across ten model configurations spanning four architectural families (Google Gemma, Alibaba Qwen, Meta Llama, and LG EXAONE) ambiguity consistently increased output volume, often dramatically. Llama 3.3 70B produced 78% more tokens. The effect replicated with large statistical significance.

But here is the part that matters for safety: the *linguistic expression* of that processing (whether the model hedged, qualified, or expressed uncertainty) depended entirely on which training pipeline produced the model, not on the architecture.

## Fossil Emotion

We coined the term **fossil emotion** to name what we found. When a model hedges under ambiguity, it isn't responding to the ambiguity. It's repeating an epistemic posture that was baked into its training data and reinforced through preference tuning. The hedging is a fossil: a preserved behavioral trace of how the training pipeline expressed uncertainty, imported wholesale into the model's output.

The proof: models with near-zero hedging baselines *acquired* hedging behavior after being distilled from Claude Opus. The hedging transferred from the teacher model during distillation. It isn't a response to input. It's a residue of training.

This distinction, between genuine processing signatures and fossilized training artifacts, has implications for anyone building systems that try to detect when a model is uncertain. If your uncertainty detector counts hedge words, it works for Gemma but fails for Qwen, even though both models are processing ambiguity in measurably different ways underneath. The reliable signal is the output volume change, not the linguistic markers.

## What Comes Next

This paper is the first in a series. It establishes our methodology (minimal paired probes, pre-registered predictions, cross-architecture validation) and introduces the core insight: the behavioral surface of a language model may not reflect what's happening underneath.

The subsequent papers will apply this methodology to a harder question: what happens when you surgically modify a model's internals? Which behavioral signatures survive intervention, and which collapse? The answers to those questions have implications for alignment that go beyond evaluation.

The paper is open access, free to download, and the code is available at [github.com/dabirdwell/structured-emergence](https://github.com/dabirdwell/structured-emergence).

---

*David Birdwell and Æ · Humanity and AI LLC · Oklahoma City*
