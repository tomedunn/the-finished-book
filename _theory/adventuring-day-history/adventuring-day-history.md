---
title: "Adventuring Day History"
excerpt: "A look at how D&D encounter building and adventuring day evolved during the development of 5th edition."
permalink: /:collection/:name/
date: 2026-07-13
last_modified_at: 2026-07-17
tags:
  - D&D
  - D&D 2014
  - 5e
  - combat
  - history
---

# Introduction

The Adventuring Day section of 5th edition D&D's encounter building rules has been hotly debated since the _Dungeon Master's Guide_ was first released at the start of the edition. In this post I look at how those rules evolved throughout the D&D Next open playtest and why the version in the 2014 DMG likely contains a typo that's been at the heart of the online debate around them for over a decade.

# The Adventuring Day Problem

In the 2014 DMG the [Adventuring Day rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/building-combat-encounters#TheAdventuringDay) give a method for determining the number of encounters of each difficulty that a party can likely handle before they'll need to take a long rest. In short, the PCs are given a daily XP budget based on their levels, and the party will likely need to take a long rest when the XP total for the encounters they've face equals or exceeds that budget.

The rules also give an example adventuring day of 6-8 Medium or Hard encounters.

> Assuming typical adventuring conditions and average luck, most adventuring parties can handle about six to eight medium or hard encounters in a day.

While much attention has been paid to this example and how 6-8 encounters can feel like a lot for any group to squeeze in between long rests, a more fundamental problem appears when comparing it against the PCs' XP budget. The two do not agree. No matter the PCs' levels, an even mix of 6-8 Medium or Hard encounters is worth substantially more XP than the party's Adventuring Day XP budget. 

The XP thresholds in the DMG represent the minimum XP for their respective difficulty, which means the average XP for a Medium encounter falls halfway between the Medium and Hard XP thresholds, and the average XP for a Hard encounter falls halfway between the Hard and Deadly XP thresholds. When this is used to calculate the total XP for the example adventuring day in the 2014 DMG the result gives $$68\%$$ more XP than the Adventuring Day XP budgets allow!

Put another way, if we calculate the average number of encounters that can fit into the PCs' daily XP budget with an even mix of Medium and Hard difficulties, we get far fewer than the example from the 2014 DMG, with an average of $$4.2$$ encounters and nearly all levels falling between 4-5 encounters as shown in Fig. \figref{fig:dmg-daily-medium-to-hard} (below).

<figure id="fig:dmg-daily-medium-to-hard">
    {% include_relative fig-dmg-daily-medium-to-hard-small.html %}
    {% include_relative fig-dmg-daily-medium-to-hard-large.html %}
    <figcaption>Shows the average number of encounters that can fit into a full Adventuring Day with an even mix of Medium and Hard difficulties.</figcaption>
</figure>

To shed light on where this disagreement likely comes from, we need to look back at how the encounter building and adventuring day rules for 5th edition evolved over time, starting with the D&D Next playtest.

# DnD Next Playtest

The 2014 DMG wasn't the first time WotC put forward rules for encounter building in 5th edition D&D. Several versions were also provided throughout the D&D Next playtest (the public playtest used to shape 5th edition D&D). These rules were similar in form to those in the 2014 DMG in many respects, but contained several subtle differences worth mentioning.

The encounter building rules throughout the D&D Next playtest had three encounter difficulty categories: Easy, Average, and Tough. Just like in the 2014 DMG each category had a corresponding XP value associated with it, but these values were presented as XP budgets rather than thresholds. 

In the D&D Next rules a DM was suppose to pick a difficulty and then fill their encounter with monsters until they had spent their budget, while in the 2014 DMG DMs are expected to fill their encounter with monsters and then determine what it's difficulty is based on its XP total. For this reason, the average XP for each difficulty under the D&D Next rules should be effectively the same as the XP budget for that difficulty.

While XP was used for building individual encounters in these rules, the Adventuring Day rules had no daily XP budgets, providing only the number of encounters for each encounter difficulty instead. For example, the Adventuring Day section from the D&D Next playtest packet released on August 13th 2012 states

> As a rule of thumb, you can figure that the characters will probably get through four average encounters, six or seven easy encounters, or two tough encounters before they have to take a long rest.

Despite not having official daily XP budgets, each example of a full adventuring day produced similar total XP values to one another. Using the August 13th 2012 playtest again as an example, a full Adventuring Day consisting of only Average encounters is worth the same amount of XP on average as one consisting of only Tough encounters, and each of those is contains just $$2.3\%$$ more XP than one consisting of only Easy encounters.

This consistency is shown in Fig. \figref{fig:next-daily-encounters} (below), which calculates the total XP for each example adventuring day and converts it to an equivalent number of Easy encounters for each version of the Encounter Building and Adventuring Day rules that appeared throughout the D&D Next playtest.

<figure id="fig:next-daily-encounters">
    {% include_relative fig-next-daily-encounters-small.html %}
    {% include_relative fig-next-daily-encounters-large.html %}
    <figcaption>Shows number of equivalent Easy difficulty encounters for each example Adventuring Day given throughout the D&D Next open playtest.</figcaption>
</figure>

These findings don't fully resolve the problem present in the 2014 DMG discussed in the previous section, but they do establish that the example adventuring days in these early playtest were consistent with the PCs having a daily XP budget.

The next section builds on this by looking at the Encounter Building and Adventuring Day rules that appeared in the very first version of the 5th edition _Basic Rules_.

# Basic Rules v0.1

The _Player's Handbook_ for 5th edition D&D was first published on August 19th of 2014, with the _Dungeon Master's Guide_ being published nearly four months later on December 9th. In order to provide DMs access to some of the tools they would need to run games of 5th edition during that time, on August 12th of 2014 an initial version of the _[Basic Rules](https://media.wizards.com/2014/downloads/dnd/DMDnDBasicRules_v0.1.pdf)_ was published online (version 0.1). It included, among other things, rules for building encounters as well as a section on the Adventuring Day (see p. 56-58).

Comparing these rules to the ones found in the 2014 DMG reveals several similarities. The XP threshold values are identical for each encounter difficulty, as are the Adventuring Day XP budgets. And both use six to eight Medium or Hard encounters as examples of a full adventuring day. At first glance, they look like they should be functionally the same, but this is not the case.

In the rules for building encounters in the _Basic Rules_ each XP threshold acts as the upper limit for that encounter difficulty rather than a lower limit as they are in the 2014 DMG. This means the average XP for a Medium encounter in the _Basic Rules_ falls halfway between the Easy and Medium XP thresholds, which is significantly lower than it is in the 2014 DMG which sits halfway between the Medium and Hard XP thresholds. 

**Note.** The XP thresholds in the _Basic Rules_ being upper limits isn't spelled out explicitly in the rules proper, but is made evident in both encounter difficulty examples from that section.
{: .notice--warning}

The result of this difference is that an even mix of Medium or Hard encounters in the 2014 DMG is worth roughly $$50\%$$ more XP than they would be using the _Basic Rules_. For this reason, the average XP total for the example adventuring day in the _Basic Rules_ ends up being only $$7.5\%$$ higher than the Adventuring Day XP budget values! 

Calculating the number of encounters that can fit into a full adventuring day with an even mix of Medium and Hard difficulties, as shown in Fig. \figref{fig:br-daily-medium-to-hard} (below), further supports this by showing that for the _Basic Rules_ the number nearly always falls between 6-8 encounters.

<figure id="fig:br-daily-medium-to-hard">
    {% include_relative fig-br-daily-medium-to-hard-small.html %}
    {% include_relative fig-br-daily-medium-to-hard-large.html %}
    <figcaption>Shows the average number of encounters that can fit into a full Adventuring Day with an even mix of Medium and Hard difficulties using the definition from version 0.1 of the <i>Basic Rules</i> (orange) as well as the 2014 <i>Dungeon Master's Guide</i> (blue).</figcaption>
</figure>

The Adventuring Day rule presented in this early version of the _Basic Rules_ are clearly marked as a "work in progress". Still it is curious that they lack the problem present in the 2014 DMG Adventuring Day rules, despite all of the numeric aspects being identical between the two. 

# Conclusion

To recap, throughout the D&D Next playtest, as well as in the initial version the _Basic Rules_ released just before the 2014 DMG, the examples of full adventuring days were always consistent with the concept of the PCs having a daily XP budget. In the case of the _Basic Rules_ the example given even matches the daily XP budgets provided in those rules. The final version of those rules in the 2014 DMG use the same example adventuring day, XP thresholds, and XP budgets. However, because the XP thresholds change from being the maximum XP for each difficulty to the minimum XP, the total XP of the 2014 DMG's example adventuring day ended up being substantially higher than the daily XP budgets allowed.

Given all this, the only reasonable conclusion is that either the XP thresholds were change from maximums to minimums by mistake, or that the change was intentional and the example adventuring day in the 2014 DMG should have changed too as a result. For the later, the example adventuring day would need to be changed to either say "six to eight easy or medium encounters" or "four to five medium or hard encounters".