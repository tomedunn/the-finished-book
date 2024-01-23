---
title: "Balancing Short Adventuring Days"
excerpt: "How do XP thresholds change for adventuring days with only one or two encounters?"
permalink: /:collection/:name/
date: 2023-2-13
last_modified_at: 2023-03-04
tags:
  - analysis
  - adventuring day
  - classes
  - encounter balancing
  - xp
---

{% include LaTex.html %}

# Introduction
In my previous post, "[Daily XP and Encounter Difficulty]({{ site.data.page-links.daily-xp-and-encounter-difficulty.path }})", I showed how player character XP thresholds change with the average encounter difficulty for full adventuring days. Since the number of encounters per day depends strongly on the encounter difficulty, you could say I also effectively showed how these XP thresholds change with the number of encounters per long rest.

This covered a fairly wide range of encounters per adventuring day, anything between 3-13 encounters, but left out two of the most common adventuring day options used by many DMs. In this post, I aim to fill in this gap by looking at adventuring days with only one or two encounters.

These calculations assume the PCs will be using only their most powerful abilities during combat, and aren't attempting to hold back any resources for later. For games where a short adventuring day only happen occasionally, and the players don't know they're free to go all out, these findings likely won't apply.

As a reminder, XP values can be calculated for player characters by taking the product of a PC's effective hit points $$(\eHP\,)$$ and average effective damage per round $$(\eDPR\,)$$, 

\begin{equation}
    \label{eq:XP-simple}
    \XP_{\PC} = \eHP \cdot \eDPR\,.
\end{equation}

For a detailed summary of how these XP values are calculated, see [Player Character XP]({{ site.data.page-links.xp-and-player-characters.path }}).

# Single encounter adventuring day

For the most part, when faced with a combat encounter, players have to make choose which of their PCs resources they want to use during the encounter and which they want to save for later. If a player knows their PCs will have to face more encounters before their next long rest, or strongly suspects they might, then they'll be much more hesitant to use their most powerful abilities all at once. Opting, instead, to use them as needed across several encounters.

However, for adventuring days with only a single combat encounter this is less likely to be the case. Especially if the if the players go into the day knowing they'll only have to face a single encounter.

For days like this, the PCs are free to use their strongest abilities all at once, which can dramatically increase their offensive and defensive strengths, allowing them to handle much tougher encounters than they could normally for full adventuring day.

To estimate how much more encounter XP each class can handle for such days, I calculated XP values for each class across five rounds of combat (i.e., the length of a typical Deadly encounter). The results of these calculations are shown in Fig. <a href="#fig:single-encounter-xp-vs-level" class="fig-ref">1</a> (below) relative to their average encounter XP for a full adventuring day with only Medium difficulty encounters.

<figure id="fig:single-encounter-xp-vs-level">
    {% include_relative fig-single-encounter-xp-vs-level-deadly-small.html %}
    {% include_relative fig-single-encounter-xp-vs-level-deadly-large.html %}
    <figcaption>Figure 1: Ratio between an average PC's encounter XP for a single Deadly encounter adventuring day and their average encounter XP for a full adventuring day with only Medium encounters.</figcaption>
</figure>

On average, this shows the **PCs are able to handle roughly $$40\%$$ more XP** than they'd be able to for a full adventuring day made up of Medium encounters. However, looking at the individual classes tells a very different story, with some classes able to handle nearly twice as much, and other the same as they can normally.

Looking at the classes within each group the dividing factor becomes clear. Classes with the Spellcasting feature show large increases in encounter XP, averaging around $$70\%$$, while those that don't have significantly small increases, averaging around only $$10\%$$. 

Barbarians and warlocks break these two general trends, but for entirely different reasons. The barbarian's XP increase gets smaller as they level due to having more uses of their Rage feature per long rest, and the warlock's XP increase grows larger as they level and gain access to higher level spells that can only be used once per long rest.

For most classes, this improvement in encounter XP comes from improvements in average effective damage per round. However, as shown in Fig. <a href="#fig:single-encounter-ehp-vs-level" class="fig-ref">2</a> (below), a few saw improvements in effective hit points as well.

<figure id="fig:single-encounter-ehp-vs-level">
    {% include_relative fig-single-encounter-ehp-vs-level-deadly-small.html %}
    {% include_relative fig-single-encounter-ehp-vs-level-deadly-large.html %}
    <figcaption>Figure 2: Ratio between an average PC's encounter effective hit points for a single Deadly encounter adventuring day and their average  for a full adventuring day with only Medium encounters.</figcaption>
</figure>

These classes include the barbarian, due to their limited uses for Rage at low levels, the fighter, due to the hit points restored by their Second Wind feature, as well as the sorcerer and wizard, both due to having more spell slots as they level up for defensive spells like _shield_ and _counterspell_. 

The bard also shows a slight improvement effective hit points, which comes from their Bardic Inspiration feature. This representation isn't entirely accurate for two reasons. First, Bardic Inspiration can be used both offensively and defensively, though both provide the same mathematical benefit to XP. And second, the benefits of Bardic Inspiration go to one of the bard's allies and not the bard.

# Two encounter adventuring days

For adventuring days with two encounters, I'd like to focus on two examples. The first involves two Deadly encounters with a short rest in between, and the second looks at two Hard encounters with no short rest. The day with Hard encounters involves fewer rounds of combat, but lacks a short rest witch will prevent certain classes from recovering resources in between the encounters.

## Deadly encounters with a short rest

For the adventuring day with two Deadly encounters and one short rest, Fig. <a href="#fig:two-deadly-encounter-xp-vs-level" class="fig-ref">3</a> (below) shows the average encounter XP for each class relative to a full adventuring day with only Medium encounters.

<figure id="fig:two-deadly-encounter-xp-vs-level">
    {% include_relative fig-two-encounters-xp-vs-level-deadly-small.html %}
    {% include_relative fig-two-encounters-xp-vs-level-deadly-large.html %}
    <figcaption>Figure 3: Ratio between an average PC's encounter XP for adventuring days with two Deadly encounters and one short rests and their average encounter XP for a full adventuring day with only Medium encounters.</figcaption>
</figure>

On average the **encounter XP for two Deadly encounters and one short rest increases around $$20\%$$**, roughly half the increase shown in Fig. <a href="#fig:single-encounter-xp-vs-level" class="fig-ref">1</a> for a single encounter adventuring day. The classes most effected are those with the Spellcasting feature, as well as the warlock at higher levels. Meanwhile, the purely martial classes performed identically to how they did for the adventuring day with only a single encounter.

## Hard encounters with no short rest

For the adventuring day with two Hard encounters and no short rest, Fig. <a href="#fig:two-hard-encounter-xp-vs-level" class="fig-ref">4</a> (below) shows the average encounter XP for each class relative to a full adventuring day with only Medium encounters.

<figure id="fig:two-hard-encounter-xp-vs-level">
    {% include_relative fig-two-encounters-xp-vs-level-hard-small.html %}
    {% include_relative fig-two-encounters-xp-vs-level-hard-large.html %}
    <figcaption>Figure 4: Ratio between an average PC's encounter XP for adventuring days with two Hard encounters and no short rests and their average encounter XP for a full adventuring day with only Medium encounters.</figcaption>
</figure>

As with the previous scenario with two Deadly encounters, the average **increase in encounter XP for two Hard encounters is also around $$20\%$$**. However, there are some subtle differences worth noting.

Classes with Spellcasting tend to fair slightly better due to the fewer number of combat rounds, while classes like fighter, monk, and warlock tend to perform worse due to the lack of a short rest. In fact, because the number of rounds across the two encounters is greater than what's typical between short rests for our baseline adventuring day, these three classes actually perform worse than the baseline for certain levels.

<!--
Fighters show the largest overall loss of any class due to only having one use of Action Surge and Second Wind to spread across both encounters.

Warlocks show similar losses to fighters at lower levels, but start to fair better above level 10 as they gain access to more long rest spells through their Mystic Arcanum features.
-->

Barbarian was the only class that showed no significant change, which makes sense as their Rage feature starts off with two uses and each one lasts a single encounter.


# Conclusion
For adventuring days with only one or two encounters, PCs can handle significantly more dangerous encounters because their average damage per round is higher than it would be for full adventuring days. The classes that benefit the most from this are spellcasters because they are able to use their strongest spells all at once instead of rationing them out across several encounters.

I don't think these results will come as a surprise to anyone who's spend much time DMing or playing 5th edition D&D. Still, for DMs who wish to run short adventuring days and still challenge their PCs with their encounters, **increasing the party's XP thresholds by $$40\%$$ for single encounter adventuring days, and by $$20\%$$ for two encounter adventuring days** should prove useful.