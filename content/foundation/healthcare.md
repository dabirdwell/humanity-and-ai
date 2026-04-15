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
discussion_url: "https://github.com/dabirdwell/humanity-and-ai/discussions/37"
---

You know the feeling. That knot in your stomach when you find a lump, or your kid spikes a fever at midnight, and before you even think about the medical question, your brain runs the numbers. *Can we afford this?*

Not "is this serious" — that comes second. In this country, the money question comes first. And if you've ever stood in a pharmacy watching the total climb past what's in your checking account, or sat in a parking lot outside an ER trying to decide if the pain is bad *enough*, you know exactly what I'm talking about.

That calculation — that quiet, constant arithmetic of risk — is what tens of millions of Americans live with every day. *Is this lump worth a $3,000 deductible? Can I afford to miss work for the follow-up? If I go to the ER, will the bill follow me for years?* It's the background hum underneath everything else. And it's one of the first things that has to change, because it poisons everything it touches.

Foundation is built on a simple premise: there is a minimum set of conditions people need to thrive, and a society wealthy enough to provide them has no excuse not to. Healthcare is one of [sixteen components](/foundation/) in this framework. It might be the one where the gap between what we have and what we could have is most obscene.

## The Real Problem

The real problem isn't that healthcare is expensive. The real problem is that someone is making money every time you get sick.

America spends more per person on healthcare than any other wealthy nation and gets worse outcomes. Life expectancy has been *declining*. Two out of three bankruptcies in this country are tied to medical bills — and the people filing them aren't people who made bad choices. They're people who got sick in a country that charges admission to stay alive.

And here's what doesn't get talked about enough: the healthcare debate in America has been stuck in the same loop for decades. The left says universal coverage. The right says free markets. And while we fight about that — while our attention is locked on each other — the actual threat goes unaddressed by either side. Not the cost of insurance. Not even the cost of drugs. The quiet, massive gathering of your medical data by corporations whose business model depends on your health information being valuable. Your privacy isn't something they're protecting. It's something that gets in the way of what they're selling.

We also built a design flaw into the system that most people don't think about until it hits them: we tied health coverage to employment. When employment was stable and long-term, that was merely inefficient. But we're entering a period where AI is reshaping work itself — eliminating entire job categories, creating fluid patterns that don't come with benefits. You can't tie coverage to jobs that don't exist. And when that disruption hits at scale, millions will lose their health coverage at the same time. Not because they did anything wrong. Because the architecture was never built to survive what's coming.

## What This Looks Like

One in four Americans with diabetes rations their insulin. Let that sit for a second. In the wealthiest country in human history, people are cutting their doses of a drug that costs $10 to manufacture — because in this country, it costs $300. That gap between the manufacturing cost and the price tag is not a market outcome. It is a policy choice, made every time legislators decline to regulate drug pricing the way every peer nation does.

*James is not one person. He is a pattern.* He's 52, type 1 diabetic since childhood, working as a subcontractor with no employer benefits. When his hours got cut, he did the math: insulin or rent. He cut his doses in half. Three weeks later, his wife drove him to the emergency room in diabetic ketoacidosis — his body shutting down from the insulin he couldn't afford to take. The ER visit cost $14,000. His insulin would have cost $900. That bill will follow his family for years — not because James made a bad choice, but because the system gave him only bad choices to make.

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

*This next part gets into some technical territory — data systems, government contracts, corporate mergers. Stay with me. You don't need to understand every detail. The important thing is the pattern: one company is quietly gaining control over your health information from multiple directions at once, and the people who are supposed to be watching aren't.*

In 2022, Oracle — one of the largest technology companies in the world — bought Cerner, the company that manages clinical records for more than 14,000 medical facilities, for $28.3 billion. That purchase gave Oracle access to patient records across hospitals, clinics, the VA, and the Department of Defense. The VA deployment alone has been catastrophic — an inspector general documented a veteran's death linked to scheduling errors in the system, 58% of clinical staff reported increased patient safety risk, and costs ballooned from $10 billion to $37 billion.

Then three things happened in rapid succession.

Oracle became what's called a Qualified Health Information Network. Here's what that means in plain English: Oracle can now see your medical data as it moves between *any* doctors, hospitals, or clinics — even ones that don't use Oracle products. Think of it as a toll booth on the highway your medical records travel on.

Oracle won the contract to host Medicare, Medicaid, CHIP (the Children's Health Insurance Program), and the ACA marketplace — the health insurance exchange created under the Affordable Care Act. That's the health coverage data of more than 150 million Americans. That contract was not publicly disclosed on SAM.gov, the federal database where government contracts are supposed to be listed for the public to see.

And thirteen days before that contract was awarded, Oracle launched a commercial AI platform selling access to 129 million "deidentified" patient records to pharmaceutical companies, insurers, and device manufacturers.

Let me say that again, because it matters. A single company now holds the clinical records *and* the financial claims data for more than 150 million Americans, and it is selling access to that information commercially. The word "deidentified" is doing a lot of heavy lifting in that arrangement. "Deidentified" means they've supposedly stripped out the information that could identify you personally — your name, your Social Security number, and so on. But researcher Dr. Latanya Sweeney proved decades ago that 87% of Americans can be re-identified using just three pieces of information: birth date, zip code, and gender. HIPAA — the federal law that's supposed to protect your health data — doesn't even require those three fields to be removed.

Meanwhile, the government office that's supposed to enforce your health data privacy — the HHS Office for Civil Rights, the people who are literally paid to make sure nobody misuses your medical records — has lost nearly 20,000 employees. The cops are gone. And no single regulator is looking at everything Oracle now controls — the VA, Medicare, the health information network — at the same time. Nobody has the full picture.

The same principle applies here that applies to voting infrastructure: no for-profit motive belongs in civic systems. The people who manage your health records shouldn't have shareholders.

## What This Does to a Person

Here's what connects all of it — the bills James can't pay, the insulin he rations, the data he can't control, the coverage that vanishes when his hours get cut.

When you live with medical insecurity — when your body is running on stress hormones because you're calculating whether you can afford to be sick — it affects everything. Not just your health. *Everything*. It affects whether you can sit still long enough to help your kid with homework. Whether you can think clearly at work. Whether you can plan for next year, or whether your horizon shrinks to the next paycheck, the next refill, the next bill.

You can't build the scaffolding for hope when your nervous system is stuck in survival mode. That's not weakness. That's biology. And we're asking millions of people to overcome it with willpower alone — which is like asking someone to outswim a current. Some will. Most won't. And we'll blame them for drowning.

The healthcare crisis isn't just a healthcare problem. It's a weight that presses down on everything else — education, safety, mental health, the ability to participate in your own life. You can't address any of those while the thing that's draining people's capacity goes untreated. Healthcare isn't just one component of the framework. It's the foundation underneath the foundation.

## What We're Building

Single-payer comprehensive coverage. That means one system, funded by taxes, that covers everyone. Not a public option alongside private insurance. Not a marketplace with subsidies. A national healthcare system that covers every citizen, funded through taxes where those who earn more pay more, and free when you walk through the door.

Every other wealthy nation has some version of this. They spend less and live longer. That's not an opinion — it's data, from every peer nation, across decades of measurement. The arguments against it in America are funded by the industries that profit from the current system. They are not funded by evidence.

Comprehensive means something specific. It means physical and mental health — because you can't treat one without the other. It means dental and vision, because somewhere along the way we decided teeth and eyes aren't part of the body. It means preventive care — catching problems early — which saves far more than it costs. It means addiction treatment, reproductive care, long-term care, rehabilitation. The full scope of what a human body might need across a lifetime — not just the parts that are profitable to insure.

And it means care that's available in Seminole and Idabel, not just Oklahoma City. Telemedicine and AI-assisted diagnostics can extend reach, but only with real investment in connectivity and training — not just an app and a prayer.

But single-payer alone isn't enough anymore. We also need public oversight of health data infrastructure. It doesn't matter if the visit is free when you walk through the door if a corporation is monetizing your diagnosis on the back end. No company should be able to hold the medical records and the claims data and the commercial data marketplace for 150 million people with no public contract, gutted enforcement, and no regulator watching the whole picture. That's not a market. That's a monopoly wearing a lab coat.

## How We Get There

So here's the question that hangs over every conversation about single-payer — one system, funded by all of us, covering all of us: if this is so obviously the right answer, why don't we have it yet? And what changes between now and the day we do?

The honest answer is that people need to *feel* the alternative before they'll fight for it. You can show someone charts comparing American outcomes to Canadian or British outcomes. You can cite the bankruptcies, the rationing, the deaths. And their eyes glaze over — not because they don't care, but because they've never experienced healthcare that works differently. The broken system is the only system they know. It's like trying to explain color to someone who's only seen gray.

There's a model that already exists, right now, that lets people taste what healthcare feels like without the insurance layer. It's called Direct Primary Care.

Here's how it works: you pay your doctor a flat monthly fee — usually $50 to $150. That's it. No insurance billing. No "prior authorizations" — that's when your insurance company makes your doctor ask permission before they can treat you. No denied claims. No co-pays for primary care visits. Your doctor gives you their cell number. You get seen the same day or the next. Appointments are 30 to 60 minutes, not the seven-minute shuffle that insurance billing demands. Your doctor knows your name, your history, your family, your situation — because the relationship is the product, not the claim.

DPC is legal right now. In Oklahoma and everywhere else. No legislation required. No ballot initiative. No permission needed. You can walk into a DPC practice tomorrow and experience healthcare that works the way you always thought it should.

And here's what DPC quietly removes from the equation: your health data doesn't flow through the insurance pipeline. No insurance system deciding whether to pay your doctor's bill. No middleman company tracking which prescriptions you fill. No data broker selling your diagnosis codes to advertisers. No Oracle AI training on your medical history. Your doctor keeps records for one reason — to take care of you. Not to feed a billing machine that has grown into something that watches you.

That matters. Because if the problem with American healthcare is both the money being taken out *and* the data being gathered up — and it is — then DPC addresses both at once. It removes the profit layer and it keeps your data in the relationship where it belongs.

### The Stepping Stone, Not the Destination

I want to be precise about this, because it matters: DPC is not the answer. Single-payer is the answer. DPC is primary care only — it doesn't cover hospitalization, surgery, specialists, or catastrophic events. If you break your leg, DPC doesn't pay for the ER.

That limitation is actually the point.

Here's why. Every person who joins a DPC practice and experiences healthcare without the insurance layer becomes someone who *knows in their body* that the alternative works. That's not a theoretical voter for single-payer. That's someone who has tasted it. And when they hit the wall — when they love their DPC doctor but can't afford the surgery their DPC doctor referred them to — the argument for universal coverage completes itself. They don't need a policy paper. They need the rest of the system to work the way their doctor's office already does.

DPC builds the support base. Its own limitations build the demand. And single-payer is the only thing that resolves both.

### The Honest Objection

Now — there's a real objection to this approach, and it comes from allies, not opponents. Some people who want single-payer worry that DPC is a pressure valve. That it solves the problem just enough for the people with the most political power — the professional class, small business owners, the organized working class — and they get their relief and stop fighting. The poorest people get left behind. The coalition that could have pushed for real change falls apart because everyone else already got theirs.

This is exactly the argument that cannabis legalization advocates made against medical cannabis in Oklahoma. Half-measures, they said, would release the pressure without achieving the real goal. They wanted full legalization or nothing.

Here's what actually happened. Oklahoma's State Question 788 — a ballot initiative — passed in 2018 as medical-only. And Oklahoma didn't stagnate — it built one of the most permissive medical cannabis systems in the country. The infrastructure grew. The business ecosystem grew. The cultural normalization compounded. Full recreational narrowly failed at the ballot, but the practical reality on the ground moved further than most states that went straight to full legalization. Medical wasn't a ceiling. It was a floor.

The key is what the cannabis movement didn't have: a map. The incremental step wasn't declared as phase one of a larger strategy. It was positioned as an end in itself. Nobody published a framework that said "this is step one — here's the destination, and here are steps two through four."

That's what Foundation is. DPC within Foundation isn't a standalone healthcare reform. It's step one of a larger plan that names universal single-payer as the destination — and [fifteen other components](/foundation/) that work alongside it. Every DPC patient encounters the full vision — not just their own relief. The pressure valve can't release because the framework keeps pointing at the destination. The stepping stone is marked on the map.

### Who This Builds

The coalitions DPC creates are the coalitions that make single-payer politically possible — and they cross every line that usually divides us.

Small business owners in Oklahoma already can't afford group health insurance. A DPC membership for their employees costs a fraction of what premiums run — and the employees actually use it. That's not a progressive coalition or a conservative coalition. That's a balance-sheet coalition.

Rural communities that lost their hospital can't sustain the economics of building a new one. But a DPC clinic needs a doctor, a building, and patients. A town that can't support a hospital *can* support a DPC practice — especially one anchored to community-owned infrastructure like the geothermal energy projects we're building through [Phoenix Wells](/phoenix-wells/).

Veterans. Oklahoma has one of the highest veteran populations per person in the country. The VA's Oracle deployment has failed them. DPC gives veterans reliable primary care while they retain VA benefits for specialty and hospital coverage. Supporting the troops means supporting their access to a doctor who picks up the phone.

And people struggling with addiction. Oklahoma's opioid crisis demands relationship-based care — the kind where your doctor knows you, has time for you, and doesn't need your insurance company's permission to help you. When insurance runs addiction treatment, it chops the care into separate visits with separate approvals, and the relationship between you and the person trying to help you gets lost in the paperwork. DPC keeps the relationship whole.

## What We Need From You

Those who say we can't have a world where everyone wins are the same ones who want to be the only winners. National healthcare isn't radical — it's what every peer nation already does. The only thing standing between where we are and where we could be is the will to build it.

We have a framework. We don't have all the answers — and that's deliberate. Here are directions we think matter. Push back on them, extend them, or bring your own:

- **Demand transparency on health data contracts.** Right now, most Americans have no idea who holds their medical records or who buys access to them. Find out who manages your state's health data infrastructure. Ask your representatives: who has our records, and what does the contract say? The Oracle contract for Medicare and Medicaid systems wasn't even listed on the federal contract database. That shouldn't be acceptable to anyone, regardless of party.

- **Design the rural health bridge.** AI-assisted diagnostics and telemedicine can close the gap between a community clinic in Seminole and a medical center in Oklahoma City — but only if we build it for communities, not for shareholders. What does that look like in your town? What would a clinic need that no one in a policy office has thought to ask about? This is the kind of specific, local knowledge that no policy paper can replace. You have it. We need it.

- **Explore Direct Primary Care.** DPC is the flat-fee, no-insurance doctor model described above. If you're uninsured, underinsured, or just tired of fighting your insurance company, look into DPC practices in your area — you can search "direct primary care near me" and you might be surprised what's already out there. If you're an employer, look at DPC memberships as an employee benefit — it's cheaper than group insurance and your people will actually use it. If you're a physician burning out on billing codes, this model exists and it's growing. Every person who experiences DPC becomes part of the movement that makes universal coverage inevitable.

- **Support transparent AI in healthcare.** When AI helps make medical decisions — diagnoses, treatment plans, drug interactions — people deserve to know it's happening, and a human being needs to be accountable for the outcome. Not "the algorithm decided." A person, with a name, who stands behind the decision. That's not anti-technology. That's the Oklahoma way: you put your name on your work.

What should the transition look like? What models are already working that we should be learning from? What are we getting wrong?

This is citizen-developed work. This is one of sixteen components. [Explore the full framework →](/foundation/)

## Join the Conversation

Have ideas about Healthcare? [Share them in our community discussion →](https://github.com/dabirdwell/humanity-and-ai/discussions/37)
