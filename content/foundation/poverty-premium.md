---
title: "The Poverty Premium"
description: "An interactive calculator showing the hidden costs of being poor — the fees, markups, and time penalties that turn poverty into a tax on the people least able to pay it."
weight: 50
tags: ["foundation", "poverty", "economics", "interactive", "calculator"]
---

There's a tax in this country that doesn't appear in any legislation. It's not collected by the IRS. No one votes on it, debates it, or campaigns against it. But it's levied on roughly 37 million Americans every day, and it costs them thousands of dollars a year.

It's called the poverty premium — the measurable, documentable, infuriating extra cost of being poor.

If you don't have a bank account, you pay to cash your own paycheck. If you can't afford a washer, you pay more per load at the laundromat than someone who bought the machine. If you don't have a car, you pay in hours. If you don't live near a grocery store, you pay a markup for the same food. If you can't get a bank loan, you pay a payday lender 400% interest for the privilege of borrowing $500.

None of this is about bad decisions. It's about the cost structure of not having money — a structure that extracts wealth from the people who have the least of it and transfers it to the people who have the most.

The calculator below makes it visible.

## The Calculator

Adjust the income slider. Watch the numbers. Click any category to see the side-by-side comparison — what something costs when you're poor versus what it costs when you're not.

<div class="viz-embed" style="margin: 2rem 0;">
  <iframe id="poverty-frame" src="/viz/poverty-premium-calculator.html"
          title="Poverty Premium Calculator"
          style="width:100%;height:900px;border:none;border-radius:12px;transition:height .2s ease;"
          loading="lazy"></iframe>
</div>
<script>
window.addEventListener('message', function(e) {
  if (e.data && e.data.iframeHeight) {
    document.getElementById('poverty-frame').style.height = e.data.iframeHeight + 'px';
  }
});
</script>

## Why This Matters for Foundation

The poverty premium is what happens when society treats basic services as products instead of infrastructure. Every category in the calculator above maps to a [Foundation component](/foundation/):

- **Banking** → [Safety](/foundation/safety/) and economic security. Foundation proposes public banking infrastructure so no one pays a fee to access their own money.
- **Laundry & Housing** → [Housing](/foundation/housing/). When housing is stable and adequate, appliances come with it. The laundromat premium is a housing premium in disguise.
- **Transportation** → [Transportation](/foundation/transportation/). The time penalty is the cruelest part. Foundation's autonomous fleet model eliminates it.
- **Food** → [Food Security](/foundation/food/). Food deserts aren't accidents. They're market logic applied to neighborhoods that don't generate enough profit. Foundation treats food access as infrastructure.
- **Credit** → [Safety](/foundation/safety/) and financial infrastructure. Payday lending exists because banks don't serve poor neighborhoods. Public banking and emergency funds eliminate the trap entirely.

The poverty premium isn't one problem. It's the same problem — the cost of exclusion from basic infrastructure — showing up in five different line items. Foundation is designed to eliminate all of them. Not by giving people money to pay the premium. By removing the premium entirely.

## The Math Doesn't Lie

At federal poverty-line income (~$15,000/year for a single adult), the poverty premium calculated above represents roughly **40% of annual income**. That means for every dollar a person in poverty earns, forty cents goes to fees and markups that a wealthier person simply doesn't pay.

This isn't a market inefficiency. It's a wealth transfer — from the poorest Americans to check cashers, payday lenders, corner store owners, and transit systems that were never designed to work. The annual poverty premium across all affected Americans exceeds **$100 billion per year**. That's not a rounding error. That's an industry.

Foundation treats this as what it is: a systems failure with a systems solution. You don't fix the poverty premium by teaching financial literacy. You fix it by building the infrastructure that makes it unnecessary.
