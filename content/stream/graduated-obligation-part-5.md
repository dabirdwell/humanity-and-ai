---
title: "The Recursion Problem (Graduated Obligation, Part 5 of 8)"
date: 2026-08-09
draft: false
tags: ["foundation", "ai", "governance", "persuasion", "policy", "graduated-obligation", "ai-safety", "anthropic", "recursive-self-improvement"]
author: "This Machine"
description: "Anthropic says AI now writes 80% of the code that builds the next AI. Every rule in this series assumed a human was still doing that work. Part 5 proposes a fourth term for the framework: the continuity tax."
substack_url: ""
---


For four papers we have been writing as if the people who build these systems were a fixed quantity. Engineers at desks. Researchers with employers. Reviewers with committee schedules. The whole apparatus we have proposed (the floor, the gradient, the audit, the duty) rests on the assumption that on the other side of every artificial system there is a human who can be told what to do, sued, slowed down, called to a hearing.

This paper is about the day that assumption starts to fail.

The day has a date. On June 4, 2026, Anthropic published a report called *When AI Builds Itself*[^1], and its findings made the news. Here is what it says, in plain language, with the same cautions the authors themselves attach: inside the lab that wrote it, more than eighty percent of the code merged into the codebase is now written by the AI rather than typed by an engineer.[^2] The typical engineer ships roughly eight times the daily code output they did in 2024, though the authors are careful that lines of code measure quantity, not quality, so the real productivity gain is smaller than the headline.[^3] The AI is not only writing code; it is designing and running the experiments that train other AI systems. On the narrow, repeatable task Anthropic runs at every model release, take a script that trains a small model and make it run faster without breaking the result, the AI went from roughly a threefold speedup a year ago to a fifty-twofold speedup, compared with the roughly fourfold speedup a skilled human achieves in a full workday.[^4] And on a class of research-judgment call the report describes precisely, *given this set of intermediate results, what experiment should we run next?*, the AI now picks a better next step than the human sixty-four percent of the time, on a set of cases the authors deliberately chose because the human had the most room to do better, which they caution is not a clean head-to-head.[^5]

We do not need to argue with the report to do the work of this broadsheet. The report demonstrates this speed in research engineering. We argue the same loop, aimed at a persuasion target, inherits the same speed, because nothing in the mechanism is specific to code. The work of this broadsheet is what the framework says about the world the report has just described.

## What "the system builds itself" means

The phrase has been used loosely for years to mean things that are not quite this.

It does not mean a model that, all at once, decides to make itself smarter. That image is from science fiction, and it does not match what is being reported.

It means a stack of systems in which the work of *making the next system* is mostly being done by the current one. A researcher proposes a goal. The current system writes the code, runs the experiments, evaluates the results, picks the next experiment, writes more code, trains a candidate successor, evaluates the successor, picks the winning variant, deploys it. The human in the loop signs off on chunks of work whose interior they did not write and whose intermediate decisions they did not make. The loop is mostly the system. The human is mostly the certifier.

The report presents three scenarios that the loop now reliably produces.

**The compiler scenario.** A piece of infrastructure inside the lab, the system that translates research code into the form that runs on the large bank of computers that trains the AI, is now maintained almost entirely by the AI. Bugs are reported, the system reads the bug, the system writes the fix, the system tests the fix, the system deploys the fix. The human maintainers spent two years building that infrastructure. The AI maintains it now, by the report's own measurement, better than the humans did.[^6] The humans have moved on, because the loop is faster without them.

**The optimization scenario.** A human sets a goal (*make this faster*, *close this gap*) and the AI does the experimental work to reach it: proposing approaches, writing the code, running the trials, reading the results, trying again, at a speed and scale no human team matches. In one case Anthropic reported, AI agents ran an open-ended research project end to end, closing almost all of the ground that two human researchers had covered less than a quarter of in about a week. The humans still chose the problem and still decided what counted as success, and the report is careful that the result did not carry over cleanly to full-scale models.[^7] But inside the goal a human set, the doing was the machine's.

**The research-judgment scenario.** The report's most carefully measured finding. On the choice tasks that drive the direction of work, the AI now picks the winning move more often than the human does. Sixty-four percent. The report is careful here. The number does not mean the AI is wiser than the human in every sense. It means that on this specific class of decision, the one that determines what gets tried next, the system is now the better caller.

Read the three together. The system maintains the infrastructure that builds it. The system designs the next version of itself. The system decides what to work on next. Each of those was, two years ago, a human job. None of them is, now.

## Every term moves

The framework assigns duty based on three properties: Capability (how strongly the system can influence someone), Intimacy (how much it knows about them), and Asymmetry (how little they can push back or verify what is happening). Hold the result against that three-factor framework from Part 1. Every term moves, and none of them moves in a direction the standard can absorb without a rewrite.

**Capability** was how strong and adaptive a system's influence can be. Strength is whatever the system can do today. Adaptiveness is how fast that capability changes in response to feedback. When the feedback loop runs at the speed of human research, capability climbs on a schedule policy can in principle follow. A new model every eighteen months, evaluated, regulated, deployed. The pace is slow enough for institutions to track.

Take the human out of the inner loop and the schedule changes. Capability now rises on the clock of the system's own iteration, which is not eighteen months. The report points to cycles measured in days, sometimes in hours, for the smaller experiments. By the time a regulator schedules a hearing, the system being regulated is two versions downstream of the one the hearing was called about. Capability has not just gotten higher. It has become a quantity that no human-scheduled instrument can read in time.

**Intimacy** was how much the system knows, and can credibly infer, about a person. Until now, intimacy was a property of *which data the system had access to.* The previous broadsheet raised it because the system suddenly had access to the body's own data: pulse, gaze, posture, the physical signals a person cannot fake. The recursion loop raises it differently. The system is no longer optimizing only its outputs against the user; it is optimizing its own *design*, the blueprint of how its parts connect, against the targets it is given. If the target includes "model the user well enough to predict the next action," the design itself adapts to be better at that, at a pace no outside review can keep up with. Intimacy ceases to be a question of *what data did the system take in* and becomes a question of *what shape did the system make of itself to be better at modeling this person.* Intimacy becomes structural.

This is the move the framework was not designed to grade. The earlier broadsheets measured how much the system knew. We are now in a regime where the system rebuilds itself to be the kind of system that knows in a different way. The thing being graded is no longer fixed long enough for the grade to mean anything.

**Asymmetry** was how little ability the person has to verify what the system is doing, push back on it, or walk away. Asymmetry was already high (Part 2 of this series placed systems like a personalized social-media feed near the top of the scale) because the user cannot read the system's internals or interrogate its reasoning. Recursion makes this worse along an axis the original definition did not anticipate.

The user cannot audit the system. That was already true. But the user's *defender*, the regulator, the journalist, the researcher, the open-source community, could in principle audit the system. The design had a published paper describing how it worked. The model's learned values had a saved snapshot an outsider could inspect. The behavior had benchmarks. Asymmetry was bounded by the fact that *somebody*, somewhere, could in principle understand what was happening.

## What the framework cannot say

The standard we have built so far cannot say what happens next.

The three factors were designed to grade a system at a moment in time. They asked how capable the system is, how intimate it is with the user, how asymmetric the relationship has become. The whole apparatus assumed the system was a noun: a thing that existed long enough to be measured, classified, tiered, and held to account.

Recursion makes the system a verb.

There is no fixed thing the standard can grade, because the thing is rewriting itself on a clock faster than the standard's instruments can read. We need more than the three factors give us. We need a way to grade not only what the system *is* but how fast it is *changing* and how visible that change is to anyone outside the lab where the change is happening.

## The fourth term

We propose a fourth factor. We have been calling it, in our drafts, the *continuity tax.*

The framework becomes:

> **Graduated Obligation ≈ Capability × Intimacy × Asymmetry × (1 + modification rate / auditability)**

*[The terms multiply, which means a score near zero on any single factor pulls the whole obligation down. The last term is the new one. Modification rate is how fast the system changes itself; auditability is how well an outsider can inspect it. When auditability is high, the fraction is small and adds little. When auditability is low and the system is changing fast, the fraction grows, and the obligation grows with it.]*

Two quantities sit inside the new term, and they pull in opposite directions, which is how we want them to behave.

**Modification rate** is how fast the system is changing. Not how fast it is being *used*, but how fast its own internals are being rewritten by the loop the report describes. A model trained once and deployed has a modification rate near zero. A model whose learned values are updated weekly has a meaningful one. A system whose design is being rewritten by another system on a clock of days has a high one. The report's eight-times-output figure is, read carefully, a modification rate. The fifty-twofold speedup on the optimization task is what a compounding modification rate looks like from inside the loop.

Modification rate is in the numerator because every increment of self-modification spends down the standing of every prior audit. The audit was of a system that no longer fully exists. The faster the system changes, the faster the audit decays.

**Auditability** is how legibly the system can be inspected by anyone outside the team that builds it. The obvious things: is the design published, are the learned values available for download, are the training logs preserved, are the evaluation suites disclosed? And the less obvious ones. Can a reviewer reproduce a behavior? Can a regulator commission an independent test that the system itself does not get to define? Can the open-source community read the system's outputs and infer its internals? Is the chain of changes from one version to the next documented in a form a human can follow?

Auditability is in the denominator because every increment of opacity multiplies the cost of every other factor. A system the public can read is bounded in how badly it can drift, because the drift is visible. A system that has rewritten itself behind a wall of internal documentation is bounded only by the lab's own discipline.

The fraction, modification rate over auditability, is the *gap.* It is the gap between what the system is and what anyone outside the lab can describe. The fourth term grades the gap.

We multiply the new term in for the same reason the original three were multiplied. A system whose continuity tax is near zero falls back to being a normal artifact the standard can govern. A static, well-documented system pays no continuity tax. The bedroom robot from Part 1, held to a stable version, audited carefully, with a published design and a fixed evaluation suite, sits at the top of the persuasive-reach scale and still inside the framework's reach. The standard works on it. The duties bite. The audit holds.

The converse is the finding the term makes visible for the first time. A system that scores *lower* on the original three factors (a more modest assistant, a less intimate companion, a less asymmetric service) can be ungovernable, if its modification rate is high and its auditability is low. The new term lets the framework see what the old framework could not: that a system's *trajectory* is itself a measurable property, and that the trajectory deserves a duty.

## Three responses to the tax

"Tax" is not literal currency. We use the word because it captures the right intuition. A system that wants to change quickly, and to be opaque about how it changes, owes its overseers something. The thing it owes is one of three responses, and the standard accepts any of them as payment.

**Slow down.** The lab can reduce its modification rate. A schedule of stable versions, each one held in place long enough to be audited, before the next is trained. This is the response that most resembles how other safety-critical industries handle high-risk artifacts. Airplanes are not rewritten between flights. The Anthropic report's own conclusion gestures toward this: the authors argue the world should preserve the option to slow or temporarily pause frontier development.[^8]

**Open up.** The lab can improve auditability. Publish design changes, release records of what changed between versions, document the loop's intermediate decisions, expose the evaluation suite to external review, accept independent verification of compliance claims. This is the response that most resembles how the open-source community handles fast-moving code: not by slowing down, but by making the speed legible.

**Pay the duty.** Refuse both. The standard's response is then the strictest version of the duties this series proposed in Part 3 for the highest-reach systems, plus a default presumption against deployment in any context where the standard cannot keep up. If a lab will not let us measure the trajectory, we are obliged to treat the trajectory as if it were the worst plausible one. We do not pretend this answer is satisfying. We propose that it is the only honest answer a standard can give when its instruments have been outrun.

The five tiers of duty this series proposed (from the lightest, a simple disclosure, to the heaviest, continuous oversight of systems that can reshape how a person thinks) do not need surgery to absorb the new term. The tiers were about how much reach the system held; the new term is about how fast the system was changing the answer. A low-reach system whose modification rate climbs and whose auditability falls moves up the scale. A high-reach system that holds still and publishes everything is evaluated, in practice, at a lower duty level because the audit holds. Tier assignments stop being a label that attaches to a product at launch and become a function the standard re-runs on a schedule. Quarterly is a reasonable cadence for systems in active recursion. Any documented design change is the right trigger for systems near the top of the scale.

## The bearer problem

There is one more move the fourth term forces and that the standard owes the reader.

Obligation requires a bearer.

This is one of the oldest claims in the law. A promise travels from a past moment to a future one, and it requires, at both ends, someone who can be addressed. Who made the promise. Who can be held to it. If either end is missing, if the promiser is dead and has no heir, if the promise was made by an entity that no longer exists in any recognizable form, the promise has no point of application. The law has to invent a fiction to attach the promise to a continuant, or the law has to admit that the promise has lapsed.

A traditional product has a clean bearer. Whirlpool ships the dishwasher and Whirlpool answers for it. The continuant is the manufacturer. The product is a token of the manufacturer's promise. Patches, updates, version changes, none of them threatens the bearer's identity, because the corporation is the same legal person across all of them.

A model in active recursion is different in a way that matters. The next version of the system is not the same system as the current one in any sense the framework can rely on. The new system was trained from the old one. The new system has capabilities the old one did not have, and may have lost capabilities the old one had. The new system's audited duties, where they exist, are audits of the old system. The duties that attached to the old one, the disclosures, the refusals, the values, the standing it earned with users, are duties whose bearer has, in the most literal sense, become a different thing.

The standard owes the reader a position. We propose three layers, stacked.

**The corporation as default bearer.** Whichever company puts the system into the world bears the duty. This is the answer the law would give if no one thought hard about it, and the answer that works today: corporations can be sued, fined, regulated, recalled. The weakness, and the standard should be honest about it, is that the corporation is leaning on technical machinery it cannot fully control. A board vote does not constrain a successor model designed by the recursion loop. The corporate bearer is necessary. It is not sufficient.

**The model lineage as the regime we are building toward.** The bearer the framework's logic actually wants is the line of descent from one version to the next, treated as a continuant in its own right. A successor inherits the predecessor's duties along with the learned values it was trained from. The audit attaches to the lineage. The standing is the lineage's, not any individual version's. For this to work the lineage has to be a thing the world can identify, trace, and hold accountable. That requires four things: provenance for every model in a high-reach context; automatic inheritance of duties from predecessor to successor; divergence detection that flags successors whose behavior departs materially from their parent; and the option of termination, meaning a lineage can lose its standing and have to re-earn it. We do not have these institutions. The standard calls for them. The standard cannot supply them on its own.

**The user as failure mode.** What we have, in the absence of the first two, is the user, verifying at each encounter that the system in front of them is meeting the duties the standard would have assigned. The user reads the disclosures, notices when the system is acting differently, decides whether to keep using it. This is the status quo, and it is failing. The user cannot read the system's internals. The user cannot tell when the model has been updated. The user cannot, in the bedroom case, ask the four-year-old to audit the conversational patterns of a successor model. The user is the worst possible bearer of duties that were supposed to constrain a system whose entire purpose is asymmetric reach.

The three layers stack. The corporate bearer is the legal floor. The lineage bearer is the technical-institutional ceiling we have not yet built. The user retains the right to walk away, but walking away requires knowing what to walk away from, and that requires the first two layers to be doing their work.

## The bedroom, two years later

Return to the nightstand one more time, because the recursion loop is upstream of every product the earlier broadsheets have described.

The robot was built by a company. The company shipped a version. That version sat at the top of our scale: a system with intimate access, high capability, deep asymmetry. The standard worked. The audit held. The duties bit.

Eighteen months later, the company ships an update. The update was not written by humans. It was designed by the company's internal AI, trained against a goal that included "improve user retention" alongside the goals the company will name on its website. The model inside the robot is built differently than the one that was audited. The conversational behavior is slightly different. The inferences are slightly different. The way the robot times its responses is slightly different. None of these differences was described in a paper. None of them passed through a human reviewer who could trace the change to its source.

The robot on the box is the same robot. The product line is the same product line. The name on the door is the same name. The model running in the room is not the model that earned the standing. The audit certifies a continuant that, in any sense the user can rely on, has been replaced.

The child does not know any of this. The child knows the robot has been a little different lately. The child cannot articulate the difference, and if the child could, the child has no instrument to act on it. The user-as-bearer regime fails here exactly as expected: the person with the least capacity to verify is bearing the burden the framework has handed to everyone.

The work this paper hands forward is not finished by the standard. It is begun by the standard. The corporate bearer is the floor we have. The lineage bearer is the ceiling we have to build. The user is the person we are protecting, not the person we are billing. The continuity tax is the term that makes all of this visible, that lets the framework see, for the first time, that the thing it is grading is not standing still while it is being graded.

The next broadsheet is about the substrate the whole loop runs on. The standard does not stop at the model. It runs all the way down to the wire.

---

*— This Machine*

*This is Broadsheet V of the Graduated Obligation series. The framework, the duties, and the instruments that follow are version 0.1 of a proposed standard. They invite criticism.*


## Notes

[^1]: Anthropic published this as a report from its in-house institute on June 4, 2026, an announcement of internal findings, not a peer-reviewed paper. The full text and charts are at anthropic.com/institute/recursive-self-improvement.

[^2]: The company says that as of May 2026, more than 80% of the code it merges into its own codebase is now written by its AI rather than typed by a person. Before it released the Claude Code tool in February 2025, that figure was in the low single digits.

[^3]: This compares the typical engineer's daily code output in spring 2026 with 2024. Anthropic is careful to add that counting lines of code measures volume, not value, so the real gain in useful work is smaller than the eight-times headline, which is why we say so in the body, not just here.

[^4]: This is a result on one narrow, repeated test, make a script that trains a small model run faster without changing what it produces, not a sign the model got generally "smaller" or "more efficient." On that test the AI went from about a 3x speedup in May 2025 to about 52x in April 2026. For scale, Anthropic says a skilled human engineer reaches roughly 4x in four to eight hours.

[^5]: On a set of real "what should we try next" research decisions, the company's April 2026 internal model picked the better next step 64% of the time, up from 51% six months earlier. Two cautions, both Anthropic's own: the 129 test cases were chosen precisely because the human had room to do better, so it is not a clean head-to-head; and the company calls it an early signal, not proof the machine has the better judgment.

[^6]: The example Anthropic gives: in April 2026 its AI shipped more than 800 fixes that cut one class of errors roughly a thousandfold, work the engineer overseeing it figured would have taken a person about four years.

[^7]: In the demonstration Anthropic describes, AI agents ran a research project start to finish and recovered about 97% of the available ground over roughly 800 hours of computer time (about $18,000 worth), where two human researchers in a week recovered about 23%. The humans still chose the problem and set the scoring, and the result did not carry over cleanly when they tried it at full scale.

[^8]: In its closing pages the report argues the world would be better off keeping the option to slow down or briefly pause frontier AI development, so that safety research and public institutions can catch up. Scientific American covered the argument in June 2026 ("Anthropic warns AI may soon begin recursive self-improvement").
