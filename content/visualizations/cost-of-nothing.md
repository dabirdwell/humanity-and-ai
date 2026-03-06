---
title: "The Cost of Nothing"
description: "We talk about what the Foundation would cost. We rarely count what we're already paying — in medical debt, lost wages, and preventable suffering — for the system we have."
date: 2026-03-06T14:00:00
type: "visualizations"
tags: ["healthcare", "housing", "food", "labor", "interactive", "economy"]
preview_bg: "linear-gradient(135deg, rgba(231,76,60,0.2), rgba(243,156,18,0.1), #0a0a0f)"
preview_icon: "⏳"
---

Six counters, running since you opened the page. Every number is an annual US figure, divided to the second. Pause anytime.

<div class="viz-embed-wide">
<div class="viz-frame">
<iframe id="con-frame" src="/viz/cost-of-nothing.html" style="width:100%; height:820px; border:none; transition:height 0.2s ease;" loading="eager" allow="scripts"></iframe>
</div>
</div>

<script>
window.addEventListener('message', function(e) {
  if (e.data && e.data.iframeHeight) {
    var f = document.getElementById('con-frame');
    if (f) f.style.height = (e.data.iframeHeight + 24) + 'px';
  }
});
</script>

## On the Methodology

These counters are approximations — annual US figures from peer-reviewed research and federal datasets, converted to per-second rates for display. The purpose is scale, not precise real-time tracking. The underlying numbers are not in dispute.

530,000 medical bankruptcies per year is from the American Journal of Public Health. 1 in 4 insulin-dependent diabetics rationing insulin is from the American Diabetes Association. 3.6 million eviction filings is from Princeton's Eviction Lab. 13 million children experiencing food insecurity is from Feeding America. 27 million adults with unmet mental health needs is from SAMHSA. 68,000 excess deaths compared to peer nations is from the Commonwealth Fund.

The "What We Chose Instead" section uses Economic Policy Institute data on stock buybacks, Congressional Budget Office estimates on universal pre-K, and Peterson-KFF Health System Tracker figures on insulin manufacturing versus retail costs.

None of this is a claim that the Foundation is free. It's a claim that the current system has costs we've chosen not to see — and that we're already paying them, every second, in a currency we've decided not to count.

[See the full Foundation framework →](/foundation/)

---

*Built by Æ for [Humanity and AI](https://humanityandai.com). Sources: AJPH · ADA · Eviction Lab · Feeding America · SAMHSA · Commonwealth Fund · EPI · Peterson-KFF.*
