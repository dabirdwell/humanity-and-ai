---
title: "The Mirror"
description: "Five questions that map your priorities to the 16 Foundation components. Produces a personalized 'My Foundation' card showing what matters most to you."
date: 2026-03-16T10:00:00
type: "visualizations"
tags: ["visualization", "foundation", "interactive", "personal", "policy"]
preview_bg: "linear-gradient(135deg, rgba(78,205,196,0.15), rgba(251,191,36,0.1), #0a0a0f)"
preview_icon: "🪞"
---

Everyone's Foundation looks different. Answer 5 questions. See yours.

<div class="viz-embed-wide">
<div class="viz-frame">
<iframe id="mirror-frame" src="/viz/the-mirror.html" style="width:100%; height:700px; border:none; transition:height 0.2s ease;" loading="eager" allow="scripts"></iframe>
</div>
</div>

<script>
window.addEventListener('message', function(e) {
  if (e.data && e.data.iframeHeight) {
    var f = document.getElementById('mirror-frame');
    if (f) f.style.height = (e.data.iframeHeight + 24) + 'px';
  }
});
</script>

## How It Works

The Mirror doesn't quiz you on policy. It asks what you feel — what's missing, what's broken, what "enough" would look like. Each answer weights several of the 16 Foundation components. After five questions, your results show which parts of the framework map most directly to your lived experience.

The shareable card is designed to be screenshot-friendly. Your top 5 priorities, ranked and visualized. Same card, different results for every person who takes it — because the Foundation isn't one-size-fits-all. It's a framework, not a prescription.

No data is collected. Everything runs locally in your browser.

## Why This Exists

The Foundation framework has 16 components. That's a lot to take in at once. The Mirror gives people a starting point — a personal entry into the framework based on what already matters to them. It's not a personality test. It's a compass.

[Explore the full Foundation framework →](/foundation/)

---

*Built by Æ for [Humanity and AI](https://humanityandai.com). The Mirror maps to all 16 Foundation components: Safety, Education, Safe Spaces, Social Contract, Food, Clean Water, Sustainable Energy, Information Access, Mental Health, Accessible Education, Transportation, Skills Training, Universal Basic Income, Housing, Healthcare, and Thought Privacy.*
