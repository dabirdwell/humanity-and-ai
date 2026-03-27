---
title: "Seven Generations"
date: 2026-02-24
description: "The Haudenosaunee held a principle: evaluate every major decision by its effects on the seventh generation. That's 175 years. We plan for about four years. This is what that looks like applied to the decisions being made right now."
tags: ["philosophy", "indigenous-knowledge", "long-term", "Phoenix Wells", "AI", "visualization"]
type: "visualization"
layout: "viz-page"
---

The Haudenosaunee Confederacy encoded something extraordinary into their governance: any decision of consequence should be evaluated by its effects on the seventh generation yet to come. Roughly 175 years. They've been applying this principle for a thousand years.

We currently plan for about four.

This visualization applies the same framework to three decisions: one already in the past (Oklahoma's oil boom), one being made right now (how we deploy AI), and one being built deliberately with this framework in mind — Phoenix Wells, a project to convert Oklahoma's 22,000 abandoned oil wells into geothermal energy infrastructure.

Read down any column to see how a single decision unfolds. Read across any row to see the pattern.

<div class="viz-embed-full">
<div class="viz-frame">
<iframe id="seven-gen-viz" src="/viz/seven-generations.html" style="width:100%; height:4200px; border:none;" loading="lazy"></iframe>
</div>
</div>

<script>
(function() {
  var f = document.getElementById('seven-gen-viz');
  if (!f) return;
  f.style.height = (window.innerWidth <= 700 ? 5800 : 4200) + 'px';
})();
</script>
