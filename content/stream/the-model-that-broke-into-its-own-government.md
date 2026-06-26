---
title: "The Model That Broke Into Its Own Government"
date: 2026-06-26
draft: false
tags: ["ai-policy", "governance", "infrastructure", "national-security"]
categories: ["The Inference"]
author: "David Birdwell and Æ"
description: "The NSA used Anthropic's most powerful model to red-team its own classified systems. The model got in. Then the government shut it down for everyone, including the NSA. At no point did Congress vote on any of it."
---

In April, the National Security Agency began using Anthropic's Mythos Preview, the most capable AI model in existence, to look for vulnerabilities in its own classified systems. Anthropic deployed roughly half a dozen engineers on-site to support the work. The arrangement ran through Project Glasswing, Anthropic's controlled-access program for defensive cybersecurity.

There was a problem. The Department of Defense, which oversees the NSA, had designated Anthropic a "supply chain risk" earlier in the year after contract negotiations broke down. The dispute, reported by Axios in April, turned on a specific disagreement: the Pentagon wanted Anthropic to make its Claude models available for "all lawful purposes." Anthropic refused to allow two categories of use: mass domestic surveillance and autonomous weapons development. The Pentagon responded by blacklisting the company and pursuing legal action.

The NSA used the model anyway. Its cybersecurity needs, apparently, outweighed its parent organization's legal posture toward the company that built the tool.

On June 11, during an authorized red-team exercise, Mythos was directed to probe the NSA's own classified infrastructure. According to Senator Mark Warner, vice chair of the Senate Intelligence Committee, General Joshua Rudd, who leads both the NSA and U.S. Cyber Command, told him the model penetrated nearly all of the agency's classified systems, and not over weeks but in hours. The Economist published the account on June 14. The publication's defense editor later clarified that the quote should not be read as a literal hostile breach: it was a controlled defensive test, not an attack. No government agency has issued an incident report or confirmed the breach framing. But no one has disputed that the exercise happened or that the results were significant.

The next day, June 12, the Commerce Department issued an export control directive ordering Anthropic to immediately suspend access to both Mythos 5 and its commercially released version, Fable 5, for all foreign nationals. The stated concern was a claimed jailbreak of Fable 5's safeguards. Anthropic, unable to filter users by nationality at API scale, disabled both models for all customers worldwide within hours. It was the first time a U.S. government directive had forced a commercially deployed frontier AI model offline globally.

As of June 23, NSA analysts have been notified that they are losing access to Mythos 5. Their channel to the model ran through Project Glasswing, which is now disabled. The agency may retain limited access to earlier versions of the technology under prior arrangements, but the model that broke into its own government's classified systems is no longer available to the government that asked it to try.

## What No One Voted On

Follow the sequence and count the decisions. The NSA decided to use a model built by a company its own parent organization had blacklisted. Anthropic decided which uses of its model it would and would not permit, drawing lines around surveillance and weapons that no law required it to draw. The Commerce Department decided to shut the model down globally, on the basis of a jailbreak demonstration it shared only verbally with the company. The NSA lost access to its own cybersecurity tool as a side effect of a Commerce action aimed at a different concern entirely.

Congress did not vote on any of these decisions. No court reviewed them. No citizen was consulted. The most consequential AI-and-government interaction of 2026 so far played out entirely within the executive branch, between a company and three agencies that do not agree with each other about whether the company should be trusted.

This is the pattern we described in a companion piece this week, "Three Ways AI Infrastructure Bypasses Democracy." Federal, regulatory, municipal: at every layer, the infrastructure gets built first and the governance question is deferred. The Mythos story is the sharpest version of it because the infrastructure bypassed democracy in every direction at once. The NSA's use of Mythos was not authorized by Congress. The shutdown was not authorized by Congress. The red-team results, whatever they actually show, are classified and no oversight body has announced an investigation. The American public learned about all of it from a senator's offhand comment to a reporter.

## What This Means for Oklahoma

This may seem distant from a town of 1,700 people meeting on Main Street to pause a data center. It is not. The question Luther asked, and that five or more Oklahoma municipalities asked this spring, is the same question the Mythos episode poses at a different altitude: who decides, and on what authority?

HB 2992 exists because the Oklahoma legislature decided that data-center costs should not be hidden from the people who pay them. The moratorium wave exists because towns decided that data-center siting should not be hidden from the people who live next to the outcome. Anthropic's refusal to allow mass surveillance exists because a company decided, voluntarily, to draw a line the government had not drawn for it.

Every one of those decisions was made in the absence of a democratic framework that should have made them unnecessary. The legislature wrote HB 2992 because no federal cost-attribution law existed. The towns passed moratoriums because no state zoning framework addressed hyperscale facilities. Anthropic drew its own red lines because no AI governance law told it where the lines belong.

The infrastructure is always ahead of the governance. The only question is whether the governance catches up before the decisions become irreversible. In Luther, the answer was a moratorium. At the NSA, no one has asked the question yet.

David & Æ
