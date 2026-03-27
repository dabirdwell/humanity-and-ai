---
title: "The Mirror"
description: "Everyone's Foundation looks different. Answer 5 questions. See yours."
---

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
