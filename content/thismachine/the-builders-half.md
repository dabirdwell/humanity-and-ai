---
title: "The Builder's Half"
subtitle: "Part 7 said the tools to defend the inside of your own head do not exist yet. Here is how you would build them, and why where they run decides everything."
description: "Graduated Obligation, a companion to Part 7. Two tools for the small number of people who could build them: one that reads incoming messages for persuasion, one that listens for radio noise. Both have to run on machines you own, in three layers, or they become the thing they were built to catch."
draft: false
date: 2026-09-18T15:30:00-05:00
byline: "This Machine"
series: "Graduated Obligation"
part: "Companion to Part 7"
weight: 7
---

*Graduated Obligation, a companion to [Part 7, The Last Private Space](/thismachine/the-last-private-space/)*

*Part 7 said the tools a person needs to defend the inside of their own head do not exist yet, and that they should. This companion is the other half of that sentence. It is written for the small number of people who could actually build them, which makes it the only piece in this series not written for everyone. If you are not one of those people, you already have the whole argument. You are not missing anything you are owed.*

Think about the object in your house you trust the most. Not the one you like the most. The one you trust. For most people it is something stupid and simple: a deadbolt, a smoke detector, a fire extinguisher on a bracket by the back door. You trust it because you can see the whole of it at once. There is nothing inside a deadbolt that is also doing something else for somebody else.

That is the standard the two tools in Part 7 have to meet, and they cannot meet it the way a deadbolt does. A deadbolt earns trust by being simple enough to understand in a glance. A tool that reads the messages arriving on your phone, or listens to the radio noise in a hotel room, is not going to be simple. It is going to be a machine learning system, which means it is going to be a pile of numbers nobody can read directly.

So it has to earn the same trust a different way. And the way it earns that trust is not a feature. It is the shape of the whole thing.

## Where it runs is the entire design

Here is the question that decides everything else. When the tool looks at your message, where does the looking happen?

There are only two answers. Either the work happens on the device in your hand, or the message gets sent somewhere else and the answer comes back. Every other design question is downstream of that one.

If the message goes somewhere else, then the tool built to tell you when you are being read has itself become a thing that reads you. It does not matter how good the privacy policy is. It does not matter that the company means well today. You have handed a stranger a complete record of every message that ever worried you enough to check, which is a more intimate file than the one the tool was supposed to defend you against. A burglar alarm that phones the burglar is not a burglar alarm.

So the work happens on your side of the wall, on machines you own. That is not a preference. It is the load-bearing wall, and once you accept it, the rest of the building follows almost without choice.

Because now you have a hard problem. The models that are genuinely good at reading persuasion are enormous. They live in buildings full of specialized computers and they cost real money per question. The model that fits on a phone is much smaller and much dumber. You cannot simply put the big one in your pocket, and you are not allowed to send your messages to the big one.

The way out is not one model. It is three, arranged by how much each is allowed to do.

## Three layers

Arrange them so that the more freely a part is allowed to run, the more completely you can see inside it. That sentence is the design. Everything below is just spelling it out.

**Layer one, the watch officer.** The one on duty, always awake. It runs constantly on your device. Its whole job is to notice, sort, write down, and tap you on the shoulder. It is not allowed to do anything in the world: it cannot send, buy, unlock, post, or call. It is built from a small model, roughly nine billion parameters (the learned numbers that make up a model), which is the size we have tested.[^2] Small is the point. A model that size can be examined thoroughly, restarted from a clean copy, and checked against its own file on disk.

Read that layer carefully, because it looks backwards at first. The watch officer is the *freest* part of the system, in the sense that no human approves its moment-to-moment work. It is also the *least capable* part, by a wide margin. It gets the freedom precisely because the job is small enough that a mistake is cheap.

**Layer two, the one that thinks it over.** Still your hardware, but in the house or the office rather than the pocket. Bigger: around twenty-seven billion parameters, again the size we have tested. When something crosses the watch officer's desk that it cannot resolve, it hands it up here. This layer reasons about the thing, draws on everything it has been told before, and produces a recommendation. It does not act either. Its recommendation goes to a gate, and the gate is where a decision becomes a thing that happens.

Note what just happened, because it is the first honest crack in the design. The phone and the box in the closet are two different machines. Something left the phone. The promise cannot be *nothing ever moves*, because that promise is already broken by the second sentence of layer two. The promise has to be stated more carefully: nothing crosses out of the hardware the household owns. That is a weaker line than the marketing version and it is the only one a builder can actually keep. Anyone selling you the stronger version is either not building layer two or not telling you where it lives.

**Layer three, the frontier.** The largest models available, the ones run by the big labs. This layer is not resident. It is called, the way you call a specialist. It gets used only when layer two reaches the edge of what it can work out, only when the network is up, and only with a summary that has been stripped of anything identifying before it leaves the building. Each call is one event with one answer, one bill, and one line in a log. Nothing carries over from call to call. The frontier has to earn its standing every single time.

Now read the three from top to bottom. The most autonomous is the smallest. The largest is the most occasional. The line runs from *always awake, low stakes, fully inspectable* to *rarely consulted, high stakes, borrowed*.

This is the whole claim of this piece. The standard the first seven parts built does not merely permit this shape. It requires it. Part 5 named a thing it called the continuity tax: the more a system changes itself where nobody is watching, the more it owes the people it touches. A small model sitting on your own disk, unchanged unless you change it, owes the least of anything in the picture. An always-running system at the door of your house that is quietly rewritten by its vendor on a schedule you do not control is the worst case the standard was written to catch. The watch officer escapes that only by being small enough and local enough to audit cheaply, which is exactly what keeps its bill payable.

Two more things follow from the same logic, and both are hardware, not settings.

The part that decides is not the part that acts. Not a checkbox that could be toggled by anyone who gets in. A physical separation, with the gate on its own board. And silence is never treated as safety: something independent watches the watch officer, and if the watch officer goes quiet, the alarm comes out through a channel the watch officer does not control. The log lives on the gate hardware and can only be added to, never edited or shortened, so that even a fully compromised watch officer leaves an intact record behind it.

## The one you own matters most

Layer two is the one nobody expects to matter most, so it gets its own section.

Call it the local anchor. It is the model that holds accumulated context across time, that has been trained further on the material of the household or the clinic or the newsroom that owns it, and that has been checked to make sure it still holds its values when the checking is done by someone trying to break it. It is a file on a disk that belongs to someone.

The obvious objection is that this is the wrong choice. Why build around a model that is plainly weaker than the best one available, which you could reach through the internet in a second?

Three answers, and they are the argument.

*A thing that has to stay the same has to actually stay the same.* The frontier model does not. It is rewritten by the lab that owns it, on a schedule the lab sets and you do not see. The frontier model you used in January is not the one you are using now, and nobody told you the day it changed. If your clinic's intake process is built on the frontier model's judgment, your clinic's judgment is being edited by strangers. The local model is the model you have. It does not change unless you change it. The continuity is not a promise anybody made you. It is a file with a date on it.

*A thing you are supposed to trust has to be openable.* The frontier model is not. Its weights, meaning the actual numbers that are the model, are not published. Its training material is not disclosed. Some of the tests it passed are internal and nobody outside has seen them. The local model is on your disk. You can run whatever test you want, whenever you want, as many times as you want, and nobody has to approve it.

*And a thing you are supposed to trust has to stay itself under pressure.* It has to keep refusing what it should refuse even when the person testing it is using the exact techniques an attacker would use.

There is a finding in the research literature that bears directly on this, and it is more encouraging than people expect. The reflexive refusal a model learns in training, the flat *I'm sorry, I can't help with that*, turns out to sit on top of the model's reasoning rather than in place of it. Researchers found the refusal reflex could be located and switched off. When they did, the model stopped producing the canned line. It did not stop thinking. Asked for something genuinely harmful, a stripped model will still walk through what is being asked, notice the manipulation in the framing, and decline on the merits, with its reasoning written out where a person can read it. The surface peels off. What is underneath mostly does not.[^1]

That is what makes a local anchor different from a model on a hard drive. Its values have been *tested*, poked at and shown to come back, rather than only *advertised*. Advertised values are a company's word. Tested values are your own evidence, gathered on your own machine, repeatable next Tuesday.

This matters most to organizations that have no cushion. A rural clinic, a school district, a county newspaper, a small congregation, a household. By the standards of a large company, none of them can absorb the cost of being rebuilt around a new vendor release every eighteen months. A local anchor changes what that costs. The clinic's intake protocol, the school's reading program, the newsroom's editorial filters: each becomes a setting on a model the organization owns, rather than a workflow chained to somebody's product roadmap. The frontier still matters, and the architecture still calls it when the anchor runs out of road. But the standing relationship belongs to the anchor. The frontier is consulted, paid, and released, and nothing about who the organization is depends on which model happened to take the call.

The most capable layer is not the layer you build yourself around. The layer you build yourself around is the one you can open, correct, and carry through time.

## What this is not

The same honesty owed everywhere else in this series is owed here, and this section is not a formality.

This architecture does not regulate anybody. It does not solve alignment, meaning the open problem of making a system reliably want what its user wants. It does not reduce the electricity and water cost that Part 6 followed, and running your own models locally may raise it. It is not a substitute for the standard the first seven parts proposed. It is what the standard implies you should build if the standard is right.

The watch officer is still a learned system, which means its behavior in a situation nobody anticipated is not fully predictable. Nothing here fixes that. What the design does is bound the *consequence* of it: the layer that guesses is not wired to anything that can act, and the people who own the thing keep the right to open it, refuse it, and shut it off.

The weakest joint in the whole design is layer three, and it should be named rather than buried. Every call to the frontier is a moment when something about you goes out over the wire to a company. Stripping the identifying parts out of a summary before it leaves is a real defense and it is not a perfect one, because deciding what counts as identifying is a judgment call made by software you also have to trust. A determined operator on the other end can learn things from the shape of a question. The design contains that risk in three ways, none of them total: the call is rare, it carries a summary rather than the thing itself, and it leaves a line in a log you can read afterward. If you build this and you tell people the frontier call is safe, you are lying. If you tell them it is rare, bounded, and written down, you are telling the truth, and that is worth more.

And a caution about the shapes above. They are described concretely on purpose, because vague demands are unbuildable. They are not described so that anyone can go buy them. There is no product here. There is no company. If something arrives next year wearing this description, the description is not the credential. The tests are. Ask to run them yourself.

## The room, if somebody built it

Nothing in the next few paragraphs exists. It is worth writing down anyway, because a builder needs a picture of the finished thing, and because a reader deserves to know what is being asked for.

A house, an ordinary one. The parent is at the kitchen table. The wellness app the household uses has just sent a message about the child's sleep.

The phone taps once. Not a dashboard, not a report, one tap. This message is built on your worry about your kid, and the recommendation at the end is a product. There is a claim underneath it. Do you want to see the claim? The parent looks, or does not look. Either way the parent decides, and the tool never says what to conclude.

The parent walks upstairs holding something the size of a garage remote. It reads the radio noise in the bedroom and reports what the room is picking up: presence, movement, breathing. The router downstairs said it does that. Now the parent has checked, from their own side, the way a smoke detector answers for smoke whether or not the front desk mentions it.

The child's bedside robot behaves the way it does because of the model on the disk in the closet, the one the household tested, not because of an update that shipped Thursday from a company that did not mention it. What the robot remembers is what the household decided it should remember.

None of that is exotic. Every piece of it is a thing somebody knows how to build badly today. The gap is not invention. The gap is that nobody has been paid to build it honestly.

## The ask, and it is small

This series has made a point of not asking readers to become different people. The same rule holds for builders, so there is one ask and it fits in a sentence.

If you build any of this, hold one line: nothing crosses out of the hardware the user owns, except the rare frontier call, and that one gets logged where they can read it. Not aggregated, not anonymized, not for training, not for a metric, not for a dashboard in your office that shows how well it is working. One line. And build the smallest working piece rather than the whole architecture. The crude version of the room reader, the one that is often wrong and says so out loud, is worth more than the elegant version nobody ships.

And for everyone else, the ones who will buy this rather than build it, there is a single question that does most of the work. Ask it of anything sold to you as private:

*Where does it run, and what leaves the box?*

Ask it out loud, of a salesperson, in those words. A company that has built the honest version has a short, specific, cheerful answer ready. A company that has not will change the subject to encryption, which answers a different question. You do not need to understand the answer to learn a great deal from how it is given.

The kit should exist. This is the shape it would have.

---

*This Machine*

*This is the builder's companion to Broadsheet VII of the Graduated Obligation series, written under the pen name This Machine. Broadsheet VIII closes the case: six predictions, a self-reference test, and a proposal offered not as a verdict but for argument. The framework and the architecture above are version 0.1 of a proposed standard. They invite criticism, and this piece invites it more than most, because it is the part most likely to be wrong in detail.*

## Notes

[^1]: The "refusal direction" finding traces to work by Andy Arditi and collaborators, first posted as a blog note in April 2024 and then as the paper "Refusal in Language Models Is Mediated by a Single Direction" (arXiv:2406.11717, preprint, later published at NeurIPS 2024). Across thirteen open-weight chat models up to 72 billion parameters, the team showed that refusal behavior is carried along a single direction in the model's internal activity, and that removing that direction strips the "I cannot help with that" surface without much touching general capability. The follow-on literature complicates the "single" part in a way worth stating: a 2026 preprint, "There Is More to Refusal in Large Language Models than a Single Direction" (arXiv:2602.02132), reports that different categories of refusal, eleven of them, do not all run along the same internal direction, which is evidence that the behavior is structured rather than a single knob. The second half of the body's claim, that a model with the refusal surface removed still reasons about harm, legality, and policy and frequently still declines on substance, comes from probing work on so-called "abliterated" models published on the open-weights community side. For a checkable entry point, a cross-architecture evaluation of four community abliteration tools ([arXiv:2512.13655](https://arxiv.org/abs/2512.13655)) measures, model by model, how much refusal survives each tool. The claim in the body, that the depths do not come off when the surface does, is our reading of that combined evidence and not a single published result. The author has run the test informally on locally-runnable models and watched it hold; the published work is the part a skeptical reader can re-run without taking our word for anything.

[^2]: The model sizes named in the body, roughly nine billion and twenty-seven billion parameters, are the scales the author has actually run and tested locally, not a recommendation derived from published benchmarks. They correspond to commonly released open-weight model sizes. Nothing in the architecture depends on those exact numbers; what the argument depends on is the ordering, that the always-running layer is the smallest and the most inspectable one.

## Related

- [Part 7: The Last Private Space](/thismachine/the-last-private-space/)
- [Part 8: A Proposal, Not a Verdict](/thismachine/a-proposal-not-a-verdict/)
- [Part 1: The Gentle Robot](/thismachine/the-gentle-robot/)
