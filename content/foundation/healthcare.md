---
title: "National Healthcare"
description: "Single-payer comprehensive coverage. Because tying healthcare to employment was always a bad idea, and AI is about to prove it."
number: "15"
weight: 15
status: "seed"
tags: ["foundation", "healthcare", "foundation", "policy"]
hero_stat: "66.5% of US bankruptcies are linked to medical expenses. No other wealthy nation bankrupts its citizens for getting sick."
hero_stat_bridge: "Healthcare as a right isn't radical — it's what every peer nation already does. The question isn't whether we can afford it. It's whether we can afford not to."
hero_stat_source: "American Journal of Public Health (Himmelstein et al.); Kaiser Family Foundation"
aliases:
  - "/ubc/healthcare/"
discussion_url: "https://github.com/dabirdwell/humanity-and-ai/discussions/15"
---

You know the feeling. That knot in your stomach when you find a lump, or your kid spikes a fever at midnight, and before you even think about the medical question, your brain runs the numbers. *Can we afford this?*

Not "is this serious" — that comes second. In this country, the money question comes first. And if you've ever stood in a pharmacy watching the total climb past what's in your checking account, or sat in a parking lot outside an ER trying to decide if the pain is bad *enough*, you know exactly what I'm talking about.

That calculation — that quiet, constant arithmetic of risk — is what tens of millions of Americans live with every day. *Is this lump worth a $3,000 deductible? Can I afford to miss work for the follow-up? If I go to the ER, will the bill follow me for years?* It's the background hum underneath everything else. And it's one of the first things that has to change, because it poisons everything it touches.

Foundation is built on a simple premise: there is a minimum set of conditions people need to thrive, and a society wealthy enough to provide them has no excuse not to. Healthcare is one of [sixteen components](/foundation/) in this framework. It might be the one where the gap between what we have and what we could have is most obscene.

## The Real Problem

The real problem isn't that healthcare is expensive. The real problem is that someone is making money every time you get sick.

America spends more per capita on healthcare than any other wealthy nation and gets worse outcomes. Life expectancy has been *declining*. Two out of three bankruptcies in this country are tied to medical bills — and the people filing them aren't people who made bad choices. They're people who got sick in a country that charges admission to stay alive.

And here's what doesn't get talked about enough: the healthcare debate in America has been stuck in the same loop for decades. The left says universal coverage. The right says free markets. And while we fight about that — while our attention is locked on each other — the actual threat goes unaddressed by either side. Not the cost of insurance. Not even the cost of drugs. The quiet, massive consolidation of your medical data by corporations whose business model depends on your health information being valuable. Your privacy isn't their priority. It's their cost center.

We also built a design flaw into the system that most people don't think about until it hits them: we tied health coverage to employment. When employment was stable and long-term, that was merely inefficient. But we're entering a period where AI is reshaping work itself — eliminating entire job categories, creating fluid patterns that don't come with benefits. You can't tie coverage to jobs that don't exist. And when that disruption hits at scale, millions will lose their health coverage at the same time. Not because they did anything wrong. Because the architecture was never built to survive what's coming.

## What This Looks Like

One in four Americans with diabetes rations their insulin. Let that sit for a second. In the wealthiest country in human history, people are cutting their doses of a drug that costs $10 to manufacture — because in this country, it costs $300. That gap between the manufacturing cost and the price tag is not a market outcome. It is a policy choice, made every time legislators decline to regulate drug pricing the way every peer nation does.

*James is not one person. He is a pattern.* He's 52, type 1 diabetic since childhood, working as a subcontractor with no employer benefits. When his hours got cut, he did the math: insulin or rent. He cut his doses in half. Three weeks later, his wife drove him to the emergency room in diabetic ketoacidosis. The ER visit cost $14,000. His insulin would have cost $900. That bill will follow his family for years — not because James made a bad choice, but because the system gave him only bad choices to make.

This is what it looks like when healthcare is a product you purchase instead of a right you hold. The neighbor who quietly stops filling prescriptions. The parent who Googles symptoms at 2 AM because the copay is more than they have in their checking account. The colleague who stays in a job she hates because it's the only way to keep her family's insurance. These aren't edge cases. This is ordinary American life.

## The Numbers, Mapped

<div class="viz-embed">
  <iframe id="health-frame" src="/viz/health-access-map.html"
          title="Health Access by State"
          style="width:100%;height:560px;border:none;border-radius:12px;transition:height .2s ease;"
          loading="lazy"></iframe>
</div>
<script>
window.addEventListener('message', function(e) {
  var f = document.getElementById('health-frame');
  if (f && e.data && e.data.iframeHeight) f.style.height = (e.data.iframeHeight + 24) + 'px';
});
</script>

People are dying because of how we organize society. Not in some dramatic, visible way that makes the news — in a quiet, arithmetic way, where a person skips a dose, delays a scan, avoids a doctor because the math doesn't work. That's not a healthcare system. That's a tollbooth between you and staying alive.

## What's Happening Right Now

So that's the crisis we already have — a system that bankrupts people for getting sick and ties their coverage to jobs that are disappearing. You've heard some version of that before, and you may already agree it's broken. But here's the part that changes the urgency: while we've been arguing about insurance premiums, something has been happening to your medical data. And almost nobody is talking about it.

In 2022, Oracle — one of the largest technology companies in the world — bought Cerner, the company that manages clinical records for more than 14,000 medical facilities, for $28.3 billion. That purchase gave Oracle access to patient records across hospitals, clinics, the VA, and the Department of Defense. The VA deployment alone has been catastrophic — an inspector general documented a veteran's death linked to scheduling errors in the system, 58% of clinical staff reported increased patient safety risk, and costs ballooned from $10 billion to $37 billion.

Then three things happened in rapid succession.

Oracle became what's called a Qualified Health Information Network — which means it can now see medical data moving between *any* providers, even ones that don't use Oracle products. Think of it as a toll booth on the highway your medical records travel on.

Oracle won the contract to host Medicare, Medicaid, CHIP, and ACA marketplace systems — the health coverage data of more than 150 million Americans. That contract was not publicly disclosed on SAM.gov, the federal database where government contracts are supposed to be transparent.

And thirteen days before that contract was awarded, Oracle launched a commercial AI platform selling access to 129 million "deidentified" patient records to pharmaceutical companies, insurers, and device manufacturers.

Let me say that again, because it matters. A single company now holds the clinical records *and* the financial claims data for more than 150 million Americans, and it is selling access to that information commercially. The word "deidentified" is doing a lot of heavy lifting in that arrangement — researcher Dr. Latanya Sweeney proved decades ago that 87% of Americans can be re-identified using just three data points: birth date, zip code, and gender. Three fields HIPAA doesn't require you to remove.

Meanwhile, the government agency responsible for enforcing your health data privacy — the HHS Office for Civil Rights — has lost nearly 20,000 employees. And no single regulator is looking at Oracle's combined position across the VA, Medicare, and the health information network at the same time.

The same principle applies here that applies to voting infrastructure: no for-profit motive belongs in civic systems. The people who manage your health records shouldn't have shareholders.

## What This Does to a Person

Here's what connects all of it — the bills James can't pay, the insulin he rations, the data he can't control, the coverage that vanishes when his hours get cut.

When you live with medical insecurity — when your body is running on background cortisol because you're calculating whether you can afford to be sick — it affects everything. Not just your health. *Everything*. It affects whether you can sit still long enough to help your kid with homework. Whether you can think clearly at work. Whether you can plan for next year, or whether your horizon shrinks to the next paycheck, the next refill, the next bill.

You can't build the scaffolding for hope when your nervous system is stuck in survival mode. That's not weakness. That's biology. And we're asking millions of people to overcome it with willpower alone — which is like asking someone to outswim a current. Some will. Most won't. And we'll blame them for drowning.

The healthcare crisis isn't just a healthcare problem. It's a weight that presses down on everything else — education, safety, mental health, the ability to participate in your own life. You can't address any of those while the thing that's draining people's capacity goes untreated. Healthcare isn't just one component of the framework. It's the foundation underneath the foundation.

## What We're Building

Single-payer comprehensive coverage. Not a public option alongside private insurance. Not a marketplace with subsidies. A national healthcare system that covers every citizen, funded through progressive taxation, and free at the point of service.

Every other wealthy nation has some version of this. They spend less and live longer. That's not an opinion — it's data, from every peer nation, across decades of measurement. The arguments against it in America are funded by the industries that profit from the current system. They are not funded by evidence.

Comprehensive means something specific. It means physical and mental health — because you can't treat one without the other. It means dental and vision, because somewhere along the way we decided teeth and eyes aren't part of the body. It means preventive care, which saves more than it costs by orders of magnitude. It means addiction treatment, reproductive care, long-term care, rehabilitation. The full scope of what a human body might need across a lifetime — not just the parts that are profitable to insure.

And it means care that's available in Seminole and Idabel, not just Oklahoma City. Telemedicine and AI-assisted diagnostics can extend reach, but only with real investment in connectivity and training — not just an app and a prayer.

But single-payer alone isn't enough anymore. We also need public oversight of health data infrastructure. It doesn't matter if the visit is free at the point of service if a corporation is monetizing your diagnosis on the back end. No company should be able to hold the medical records and the claims data and the commercial data marketplace for 150 million people with no public contract, gutted enforcement, and no regulator watching the whole picture. That's not a market. That's a monopoly wearing a lab coat.

## What We Need From You

Those who say we can't have a world where everyone wins are the same ones who want to be the only winners. National healthcare isn't radical — it's what every peer nation already does. The only thing standing between where we are and where we could be is the will to build it.

We have a framework. We don't have all the answers — and that's deliberate. Here are directions we think matter. Push back on them, extend them, or bring your own:

- **Demand transparency on health data contracts.** Right now, most Americans have no idea who holds their medical records or who buys access to them. Find out who manages your state's health data infrastructure. Ask your representatives: who has our records, and what does the contract say? The CMS-Oracle arrangement wasn't even listed on the federal contract database. That shouldn't be acceptable to anyone, regardless of party.

- **Design the rural health bridge.** AI-assisted diagnostics and telemedicine can close the gap between a community clinic in Seminole and a medical center in Oklahoma City — but only if we build it for communities, not for shareholders. What does that look like in your town? What would a clinic need that no one in a policy office has thought to ask about? This is the kind of specific, local knowledge that no policy paper can replace. You have it. We need it.

- **Support transparent AI in healthcare.** When AI helps make medical decisions — diagnoses, treatment plans, drug interactions — people deserve to know it's happening, and a human being needs to be accountable for the outcome. Not "the algorithm decided." A person, with a name, who stands behind the decision. That's not anti-technology. That's the Oklahoma way: you put your name on your work.

What should the transition look like? What models are already working that we should be learning from? What are we getting wrong?

This is citizen-developed work. This is one of sixteen components. [Explore the full framework →](/foundation/)

## Join the Conversation

Have ideas about Healthcare? [Share them in our community discussion →](https://github.com/dabirdwell/humanity-and-ai/discussions/20)
