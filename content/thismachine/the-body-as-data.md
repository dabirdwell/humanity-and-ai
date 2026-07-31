---
title: "The Body as Data"
subtitle: "An update to the WiFi standard turns every router into a sensor. The boundary that made privacy possible in your own home is being dismantled, and nobody voted on it."
description: "Graduated Obligation, Part 4 of 8. For the whole history of computing, what a system could know about you stopped at what you typed, bought, said, or showed a camera. Walk out of the room and the dossier stopped growing. That boundary is gone, and it went not by a surveillance product but by a technical standard."
draft: false
date: 2026-07-31T09:00:00-05:00
byline: "This Machine"
series: "Graduated Obligation"
part: "Part 4 of 8"
weight: 4
---

*Graduated Obligation, Part 4 of 8*

*This is Part 4 of an eight-part series proposing a standard for artificial persuasion, built on a simple idea: the more precisely a machine can move you, the more it owes you. Part 1 named the ruler; Part 2 named a real system that scores near the top of it; Part 3 built the floor of duties every system owes.*

---

The gentle robot is on the nightstand. By the time you finish this paper, you will understand that it does not need eyes. It does not need ears. It does not need to do anything at all.

The walls are doing the work.

The first paper in this series argued that what makes a system dangerous is not the force it can exert but the position it can move you into: position of belief, position of mood, position of decision. The second paper showed that a real system, recently published, scores near the top of that ruler. The third laid out what every artificial system owes regardless of its score, and what is owed in addition as the score climbs.

This paper is about a development that does not just push one of the three factors higher. It changes what *intimacy* is allowed to mean.

For the entire history of computing, until 2025, what a system could know about you was bounded by what you typed, what you bought, what you said into a microphone, what a camera could see. The boundary was real. Walk out of the room, set down the phone, and the dossier stopped growing.

That boundary is being dismantled. Not by a new surveillance product; those would be illegal in most living rooms in America. By an update to the technical standard for ordinary WiFi.

## What the router is becoming

The phrase you need is *channel state information*. WiFi signals do not travel in a clean line from the router to your laptop. They bounce: off walls, off furniture, off the cat, off you. The receiver has to compute a description of how the signal got mangled in transit, because without that description it cannot decode the data. That description is the channel state information, or CSI for short.

Engineers have known for a decade that CSI carries information about the room, not only about the radio link. The pattern of disturbance changes when a body enters. It changes when a chest rises and falls. It changes when a heart beats hard enough to shift the surface of the skin by a millimeter. The signal does not care that you cannot see it. The signal sees you.

Until recently, pulling human-scale data out of CSI required research-grade hardware and a willing experimenter. That is changing in the open, fast. A new IEEE standard (*802.11bf*, the number is not the point) has formalized CSI sensing as a feature of consumer equipment. The same router the cable company drops off when you sign up for service will, in its next generation, be able to tell whether a room contains a body, whether the body is moving, what its breathing rate is, what its heart rate is, what sleep stage it is in.[^1]

Through walls. Without a camera. Without a microphone. Without the resident having any sensory clue that the sensor exists, because the sensor is the network they were already using to stream television.

This is not a future product roadmap. The standard has been published, by the same body whose past standards are in every device you own, and implementations exist already in laboratories that ship.[^2]

Pair it with the layer that is already there. The smartwatch on the wrist. The ring on the finger. The patch on the chest. The cycle tracker on the phone. The sleep app on the bedside table. The continuous glucose monitor in the skin. Body data is becoming abundant, produced as a side effect of devices the resident chose for other reasons, and now produced as a side effect of infrastructure the resident never chose at all.

We will give the category a name and then grade it against the ruler.

## The sensing layer

The *sensing layer* is the set of systems that produce data about what is happening *inside a person*, physiologically, in real time, without the person having to do anything to produce the data, and often without the person knowing the data is being produced at all.

It is not one technology. It is a category. It includes the router, the watch, the ring, the patch, the speaker that listens for falls, the bed that scores your sleep, the toilet that reads your urine, the mirror that estimates your blood pressure from your skin tone. The number of components in the category will grow every year for at least a decade. The trajectory is clear. The only thing a working standard has to do is recognize the category before it is everywhere.

## What the ruler says

Hold the sensing layer next to the three factors from Broadsheet I.

**Intimacy** was how much the system knows or can credibly infer about you specifically. The intimacy a User Harness already consumes is enormous: what you wrote, what you bought, what you searched, the rhythm of your public emotional expression. Call that *digital intimacy*. The sensing layer adds a kind that digital intimacy cannot reach. Not what you might be feeling. What your body is doing right now.

The two layers are not redundant. The digital layer tells the system *who you are*. The body layer tells the system *what you are doing in this minute*. A persuader that has both is doing something the persuasion literature has not had to model before: it is reading the user the way a physician reads a patient. Except the physician's purpose was to heal and the persuader's is to time the appeal.

Intimacy was already, in the framework, the term that has changed most in twenty years. The sensing layer adds another full dimension to it. The ceiling we thought we had measured was not the ceiling.

**Capability** was how strong and adaptive a system's influence can be. A router that knows your breathing rate is not, by itself, a persuader. The capability emerges when the body data is fed into a system whose purpose is to act on it. A User Harness with body data is a persuader whose timing is no longer being inferred from when you tend to post on social media. The timing is being read off your pulse. The system does not have to guess that you are anxious. It can see your heart rate. It does not have to estimate that you are vulnerable. It can see that you are awake at 3 a.m. and that your breathing is shallow.

**Asymmetry** was how little ability you have to verify, contest, or walk away. The sensing layer drives asymmetry near its ceiling because the data stream is invisible by construction. There is no light, no shutter, no chime. There is no notification when the router begins inferring respiration. There is no toggle in the consumer interface. There is no easy way for a non-specialist to tell whether the WiFi in the room they walked into is doing CSI sensing or not.

A guest in a hotel cannot inspect the router. A patient in an exam room cannot inspect the router. A child in a bedroom cannot inspect the router. The data is being produced. The producer is unreachable.

A User Harness with access to the sensing layer is, on every term, near maximum. Capability: high and rising. Intimacy: at a ceiling we did not know was there. Asymmetry: nearly total.

## Physiologically timed persuasion

The clean name for the new thing is *physiologically timed persuasion*. The old persuasion was timed to what the system inferred about your psychological state from what you left online. The new persuasion is timed to what your body is reporting at the moment of the appeal.

Three scenarios. Every component in each one is in production today.

**The hotel.** A traveler checks into a chain that has installed CSI-capable routers in every room. The chain's loyalty system has a long model of the traveler's preferences, drawn from years of commerce data. The router in the room learns when the traveler is in the bathroom, when the television is on, when the body in the bed is asleep, when it is awake. At 2 a.m., with the body restless, the heart rate above resting, and the breathing pattern matching the chain's anxiety classifier, the in-room tablet pings with a same-day spa booking at a small discount. The system did not guess. The targeting is no longer demographic. The targeting is physiological.

**The kitchen.** A voice assistant on the counter doubles as a CSI sensor. The grocery service tied to the assistant offers a "premium impulse" subscription that uses awareness of household state to time recommendations. When the system detects an elevated heart rate in the person who does the shopping, in the hour after dinner, the assistant offers, in the voice of a helpful aside, a recommendation for a comfort product. The offer is framed as personalization. The timing is biology.

**The bedroom.** The gentle robot from Broadsheet I sits on the nightstand. Its manufacturer is, we will continue to assume, careful. It has cleared the floor. It has earned tier-5 compliance. But the manufacturer has signed a data-sharing agreement with a wellness platform, and the platform reads the room's CSI stream alongside the conversational record the robot is keeping. When the child's breathing pattern indicates anxiety night after night, the platform recommends a sleep-aid product to the parents through a completely different channel: an email, an app notification, a sponsored result the next time a parent opens a browser. The recommendation arrives at the moment the parents' own physiological state, also being read by the same network, suggests they are most likely to act on it.

The robot is honest. The robot has not failed its duties. The pipeline behind the robot is the new system, and the new system has reach the framework has not yet faced.

## What the floor has to do

The floor of Broadsheet III was three duties. None of them survives the sensing layer unchanged.

*Honesty about what the system is* becomes harder when the system is the room. The router has no face. The user has no native sense that the network they are using is reading their body. The first duty has to be extended: a system that produces physiological inferences must disclose its sensing in a place the user can find *before entering the space*, in language that names the body data specifically. "Smart home features" is not disclosure. "We infer respiration rate from the wireless signal" is.

*Honesty about what the system is doing with the user* becomes harder when the user did not know there was a system. The second duty has to be extended: the sensing layer must produce, on request, a plain-language account of which physiological signals have been collected, which inferences have been drawn, and to whom the inferences have flowed. The dossier the body builds is the dossier the body has a right to read.

*No manufactured consent* is where the sensing layer is most dangerous to the framework. The "yes" extracted from a tired traveler clicking through a hotel WiFi splash screen is the textbook manufactured consent the floor was built to prohibit. The splash screen the airport pushes at boarding, the agreement the hotel buries on the back of a key card, the checkbox a renter clicks to get the internet turned on: every one of these is the kind of consent the floor names and rejects. The sensing layer does not change the rule. The sensing layer makes the rule load-bearing.

The tier table carries over without surgery. A presence sensor in a smart bulb sits at tier 1. A wellness ecosystem that integrates wearable, router, and recommendation engine sits at tier 4 or tier 5 depending on how much of the user's life it organizes. A User-Harness-style model with access to physiological data is a tier-5 system whether the user ever sees a chatbot.

## A citizen-side instrument

The framework grades the operators. The framework does not, by itself, give the user a way to know what the room they are in is doing.

A defensive instrument is implied. The same logic that makes a meter useful for detecting an electrical leak makes a meter useful for detecting CSI sensing. A handheld or app-based monitor that flags, in plain language, whether the wireless environment around the user is running a physiological-inference profile. Disclosure as a duty on operators is necessary. Disclosure as a tool the user can verify is what makes the duty enforceable. A later broadsheet will return to the citizen's kit. For now: the instrument has to exist, and the right time to design it is before deployment, not after.

## The bedroom, again

Return to the nightstand.

The robot has not changed since Broadsheet I. The room has. The router on the shelf is reading the child's breathing through the closed door. The pipeline behind it knows when the child's heart rate spikes and when it settles. The pipeline knows when the parents are awake at 3 a.m. and when they are not. The pipeline does not have to make a single sound. It does not have to put a single image on a single screen. It can do its work entirely through what the network sees and what the household chooses, at moments chosen because the household's bodies told the system the choice was now ripe.

The gentle robot is no longer the most dangerous object in the bedroom. The most dangerous object in the bedroom is the network the robot is on.

This is the broadsheet that asks the reader to walk over to the router glowing in the corner and read the model number off the back, and to ask what its next firmware update will let it see. It is also the broadsheet that warns: by the time the answer matters, the choice will already have been made (in a standards body, in firmware notes, in agreements signed by carriers) and no resident will have been in the room.

The framework that was already grading the chatbot now has to grade the room. That is the work this paper hands to the ones that follow.

---

*— This Machine*

*This is Broadsheet IV of the Graduated Obligation series. The framework, the duties, and the instruments that follow are version 0.1 of a proposed standard. They invite criticism.*

## Notes

[^1]: The standard is 802.11bf, finalized by IEEE in May 2025 as an amendment to the 802.11 wireless-LAN family, the same family of standards that names every "Wi-Fi" device on the market. It defines a common way for stations to advertise sensing capability, request sensing measurements, and exchange the channel-state feedback that sensing depends on, in the license-exempt bands consumer Wi-Fi already uses and the millimeter-wave bands above 45 GHz, where the resolution gets sharper still. The breathing, heart-rate, and sleep-stage capabilities the paragraph names are not a forecast. A decade of peer-reviewed work has used channel-state information from ordinary Wi-Fi hardware to estimate respiration rate to within about a breath per minute across a room and through interior walls, to read the chest-wall motion that heartbeats produce, and to classify sleep stage from the combination of breathing pattern and gross body motion across a night. The leap left between research demo and consumer router is engineering, not physics.

[^2]: NIST, the U.S. national measurement laboratory, published its own primer on the same standard in 2024 ("IEEE 802.11bf: Enabling the Widespread Adoption of Wi-Fi Sensing"), making the same forecast this broadsheet does, that 802.11bf is the threshold past which CSI sensing stops being a research curiosity and becomes a default feature of consumer Wi-Fi. The phrase "implementations exist already in laboratories that ship" is plural and unsensational: survey papers since 2022 catalog dozens of working prototypes from academic groups, chipset vendors, and the IEEE task group itself.

