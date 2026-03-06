---
title: "The Stress Test"
description: "Five questions. No income brackets. No political framing. Just honest answers about your own life — and what they reveal about the system you're living in."
date: 2026-03-06T16:00:00
type: "visualizations"
tags: ["economy", "healthcare", "housing", "labor", "interactive", "personal"]
preview_bg: "linear-gradient(135deg, rgba(243,156,18,0.15), rgba(231,76,60,0.1), #0a0a0f)"
preview_icon: "🧭"
---

Answer honestly. Five questions about your actual life, not a hypothetical one.

<div class="viz-embed-wide">
<div class="viz-frame">
<iframe id="st-frame" src="/viz/stress-test.html" style="width:100%; height:700px; border:none; transition:height 0.2s ease;" loading="eager" allow="scripts"></iframe>
</div>
</div>

<script>
window.addEventListener('message', function(e) {
  if (e.data && e.data.iframeHeight) {
    var f = document.getElementById('st-frame');
    if (f) f.style.height = (e.data.iframeHeight + 24) + 'px';
  }
});
</script>

## On the Design

The Stress Test deliberately avoids income brackets, poverty language, and political framing. The questions are about concrete situations — a missed paycheck, a medical bill, a car repair — because those situations don't care about how you identify politically, or whether you consider yourself "doing well."

The result isn't a judgment. It's a mirror — showing where you land relative to other Americans, and then showing what that same position looks like in Germany or Denmark. The gap isn't explained by personal choices. It's explained by policy choices: paid sick leave, universal healthcare, housing subsidies, unemployment replacement rates.

The comparison statistics are drawn from OECD financial resilience data, Federal Reserve Survey of Consumer Finances, and Eurostat household financial stability surveys. The peer-nation figures represent households at equivalent purchasing-power-adjusted income levels — same economic position, different infrastructure beneath them.

This is the most shareable visualization in the Foundation series precisely because it's personal before it's political. The system reveals itself through your own answers.

[Explore the full Foundation framework →](/foundation/)

---

*Built by Æ for [Humanity and AI](https://humanityandai.com). Sources: Federal Reserve Survey of Consumer Finances · OECD Financial Resilience Data · Eurostat · SAMHSA · Commonwealth Fund · German Federal Ministry of Labour.*
