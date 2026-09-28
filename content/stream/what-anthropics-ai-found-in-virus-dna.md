---
title: "What Anthropic's AI Found in Virus DNA, and What Nobody Knows Yet"
date: 2026-09-27
draft: false
description: "On September 23, Anthropic said its AI, Claude, spotted a row of evenly spaced repeats in the DNA of viruses that infect bacteria, beside an enzyme scientists already knew about. Here is what was found, in plain words, why a row of repeats can matter, and what is still unknown."
tags:
  - "science"
  - "biology"
  - "anthropic"
  - "ai-agents"
  - "transparency"
categories:
  - "analysis"
---

On Wednesday, September 23, Anthropic, the company that makes the AI system Claude, said Claude had spotted, in the DNA of viruses, something no one appears to have described before. DNA is the chemical code of instructions inside living things, spelled in four letters, A, C, G and T. What Claude spotted was a row of short, evenly spaced repeats in that code.

That may sound small. The most famous time scientists looked hard at a row of repeats in the DNA of bacteria, the trail led to CRISPR, a defense system bacteria use against viruses, which scientists later turned into one of the most important tools in biology. Nobody knows yet whether this new row will matter at all.

## What Claude was looking for

A cell keeps its instructions in DNA and makes a working copy, called RNA, when it needs to use one. In everyday terms, DNA is the cookbook on the shelf and RNA is the photocopied recipe you carry into the kitchen.

Anthropic's scientists told Claude to search a huge database of DNA for new reverse transcriptases, enzymes (proteins that each do one job in a cell) that run that process backward, turning RNA back into DNA. Put plainly, they turn the photocopy back into a page for the book.

The search was run by agents, copies of Claude that each work on their own, with other copies checking the work. Think of a crew of research assistants taking jobs off a shared list. Anthropic ran about 950 of them, and they worked for about 21 hours with no person stepping in. They gathered more than 200,000 of these enzymes, picked out about 3,500 candidates, and narrowed those to about twenty written reports.

## The row of repeats one agent found

The DNA came from bacteriophages, or phages for short, viruses that infect bacteria instead of people. Put simply, germs that make germs sick.

One agent was reading the raw letters beside an odd-looking enzyme when it found a repeat array: the same short stretch of DNA repeated again and again at even spacing, with different DNA in each gap. Picture a fence, with identical posts at regular intervals and a different board between each pair. At one site there were 14 copies of a 16-letter repeat.

The agent wrote, as Anthropic quotes it: "[The DNA next to the RT] is spectacular: I can see by eye a tandem repeat array … that's a CRISPR-like … repeat array?!" RT is shorthand for reverse transcriptase, and tandem means one after another.

The enzyme itself was not new. Earlier studies had described it in a jumbo phage, one that carries an unusually large amount of DNA. What Claude appears to have noticed first is its neighborhood: the row of repeats on one side, and on the other a partner gene, a stretch of DNA holding the recipe for a second protein whose job nobody knows. Anthropic named the three-part system ART, for array-associated reverse transcriptases.

## Why a row of repeats can matter

CRISPR was first noticed as an odd row of repeats in bacterial DNA. It turned out to be a memory. Between the repeats, bacteria store snippets of DNA from viruses that attacked them before, and use copies of those snippets to recognize a returning virus. In everyday terms, it is a wall of wanted posters: each face different, each in the same frame. Scientists learned to slip in a poster of their own choosing, which is how CRISPR became a tool that can be aimed at a chosen spot in DNA.

Anthropic notes that ART's mix of features has turned up together in only a handful of other systems, all of which scientists can program to cut, copy, or paste DNA. That explains the interest. It is not evidence that ART can do the same.

The differences are real. CRISPR's snippets are short and change as bacteria meet new viruses, because they are a record of new attacks. ART's are several times longer, and related viruses carry the same ones in the same order. They do not change the way a record of attacks would, which is one more reason not to assume ART does CRISPR's job. And ART is not the only enzyme found beside such a row, the team's paper notes.

## What the lab has shown so far

The first lab result is suggestive. The team's scientists put one ART system into ordinary lab bacteria, and the row of repeats was read out as a set of separate short RNA pieces. Data from other scientists, who watched one of these viruses infect bacteria, showed similar pieces, among the most plentiful RNA the virus makes.

In CRISPR, short RNA pieces are what point the system at its target. Nobody has shown that ART's pieces do anything like that.

The lab works only at biosafety levels 1 and 2, the two lowest of four safety ratings for biology labs. In everyday terms, level 1 is the kind of lab a college biology class uses. Anthropic says the lab handles no germs that can infect people, and human scientists do all the lab work.

## Would the search find it again?

The team ran the same search ten more times. Most of those runs came across ART enzymes, and in two an agent looked closer. None read the stretch of DNA where the repeats sit, so none found the row.

That is not a scandal. It is how searching a haystack works: two people comb the same field, and only the one who lifts the right clump finds the needle. The company published the ten misses in its own paper, the same day it announced the find.

The team then tested the AI directly. Handed the right piece of DNA to read, the most capable versions of Claude described the row in at least 90 percent of tries. Given the same DNA in files, with tools to open them, the rate fell as low as 32 percent, often because Claude never opened enough of the file to see more than one repeat. The find depended on an AI actually reading the letters.

The DNA of one of these viruses had already been published by the scientists who first studied it. The row of repeats was in it the whole time, waiting for a reader who would look at the letters themselves.

## What no one knows yet

Nobody has shown that the ART enzyme is active, that it works on those RNA pieces, that it and its partner work together, or what the system does for the virus. Anthropic says plainly that the function is unknown and experiments are underway. The work so far is in a preprint, a scientific paper posted publicly before other scientists have formally reviewed it. In plain terms, the team is showing its work before the check a journal does.

Scientists outside the team have been interested and careful. Dimitri Perrin, of Queensland University of Technology, wrote in The Conversation, a site where academics write for the public, that ART is "CRISPR-like in its architecture, but there is no evidence that it is CRISPR-like in its function." Similar layout, no proof of a similar job. Kevin Blake, a microbiologist at Washington University School of Medicine in St. Louis, told Al Jazeera: "There's nothing to indicate this is a rival to CRISPR-the-technology, or could be developed into any kind of therapeutic or practical application." Feng Zhang of MIT and the Broad Institute, one of the scientists who made CRISPR into a tool, said in a statement in Anthropic's own announcement that finding the repeat arrays "is genuinely intriguing and merits further investigation."

Nothing here changes anyone's DNA. No medicine is on the table. What exists is a new pattern, a first lab result, and an open question. We will come back to this when the team, or anyone else, shows what ART does, even if the answer turns out to be ordinary.

*The Inference, our weekly newsletter, looks at this and Anthropic's other biology moves in Issue 31. This post was written with substantial help from Claude, made by Anthropic, the company whose AI made the finding described here. The publisher applied for a research fellowship with Anthropic this summer, an application now on hold until a future round.*
