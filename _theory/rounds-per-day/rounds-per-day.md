---
title: "Rounds of Combat Per Day"
excerpt: "How many rounds should combat take? And how does encounter difficulty affect the number of rounds in a full adventuring day?"
permalink: /:collection/:name/
date: 2022-07-12
last_modified_at: 2023-05-05
tags:
  - encounter balancing
  - theory
  - xp
---

{% include LaTex.html %}

<div style="display:none">
\(
% generic
\newcommand{\RTWM}{\rounds_{\mathrm{Med}}}
\newcommand{\XPM}{\XP_{\mathrm{Med}}}
\)
</div>

# Introduction
The rules for building combat encounters show how to fit a wide range of encounter difficulties into a full adventuring day by combining encounters of different difficulties (see "[The Adventuring Day](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#TheAdventuringDay)" in chapter 13 of the _Basic Rules_). And, while this information is extremely useful for a variety of reasons, there's one bit of information that I find conspicuously absent from it; how this impacts the number of rounds of combat per day?

For the average DM who's just trying to understand how far they can push their PCs, knowing how many rounds combat encounters for each difficulty are likely to take probably isn't all that important. But when it comes to assessing how balanced the different classes are in combat, knowing the number of rounds per encounter and per full adventuring day can be extremely useful.

<!---
It's not uncommon for me to see online discussions about how the number of encounters per day impacts the relative strengths of different classes. Full adventuring days with more difficult encounters will tend to have fewer encounters per day than those with easier encountersOne topic I find conspicuously absent from these discussions, though, is how the difficulty of each encounters impacts the number of round each encounter takes, and the total number of rounds per full adventuring day.
--->

In this post, I'll attempt to calculate the number of rounds per encounter and rounds per day using the rules from "[Building Combat Encounters](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters)" in chapter 13 of the _Basic Rules_. For those wishing to skip the math and jump straight to the results, see the <a href="#tab:rounds-summary" class="fig-ref">Summary</a> table in the conclusion to this post.

# Rounds per encounter
To a simple approximation, the number of rounds a combat encounter takes can be calculated by dividing the total effective hit points of the enemy NPCs,  $$\eHP_{\NPC}$$, by the total effective damage per round of the PCs, $$\eDPR_{\PC}$$,

\begin{align}
    \rounds &= \frac{\eHP_{\NPC}}{\eDPR_{\PC}}\,. \label{eq:rounds-to-win-full-PCs}
\end{align}

For the purpose of this post, you can think of effective hit points and effective damage per round as just hit points and damage per round, but with armor class and attack bonuses factored in. That said, if you would like a more detailed understanding of what they are, see my earlier post [Effective HP and Damage]({{ site.data.page-links.effective-hp-and-damage.path }}).

Equation \eqref{eq:rounds-to-win-full-PCs} makes intuitive sense, however, it's not especially helpful at the moment because our encounter difficulty thresholds are given in values of XP, rather than effective hit points. Thankfully, there is a simple conversion we can take advantage of.

In my previous post, [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}), I showed that a monster's XP value can be calculated from the product of their effective hit points and effective damage per round,

\begin{align}
    \XP_{\NPC} &= \frac{1}{4}\eHP_{\NPC} \cdot \eDPR_{\NPC}\,. \label{eq:xp-npcs}
\end{align}

Since $$\eHP_{\NPC}$$ and $$\eDPR_{\NPC}$$ tend to scale proportionally to one another, $$\eDPR_{\NPC}$$ can be removed from Eqn. \eqref{eq:xp-npcs} by replacing it with $$\eDPR_{\NPC} \simeq 0.2 \eHP_{\NPC}$$. Figure <a href="#fig:monster-edpr-ehp-ratio" class="fig-ref">1</a> (below) shows the justification for this approximation. However, it's worth noting that the factor of $$0.2$$ will drop out of the calculation later on, and isn't especially important to the derivation that follows.

<figure id="fig:monster-edpr-ehp-ratio">
    {% include_relative fig-monster-edpr-ehp-ratio-by-cr-small.html %}
    {% include_relative fig-monster-edpr-ehp-ratio-by-cr-large.html %}
    <figcaption>Figure 1: Shows the average ratio of monster effective damage per round and effective hit points as a function of monster CR.</figcaption>
</figure>

Inserting this approximation into Eqn. \eqref{eq:xp-npcs} and solving for effective hit points yields

\begin{align}
    \eHP_{\NPC} &\simeq \sqrt{20 \XP_{\NPC}}\,. \label{eq:ehp-xp-only}
\end{align}

For encounters with only a single monster, Eqn. \eqref{eq:ehp-xp-only} can be inserted into Eqn. \eqref{eq:rounds-to-win-full-PCs} to remove its dependence on $$\eHP_{\NPC}$$,

\begin{align}
    \rounds &\simeq \frac{\sqrt{20 \XP_{\NPC}}}{\eDPR_{\PC}}\,. \label{eq:rounds-to-win-xp}
\end{align}

This obviously won't hold true for encounters with multiple monsters, but it should serve as a good first step towards a more general solution.

The dependence of Eqn. \eqref{eq:rounds-to-win-xp} on $$\eDPR_{\PC}$$ can be removed by multiplying the RHS by $$1 \equiv \RTWM / \RTWM$$, where $$\RTWM$$ is the average number of rounds it takes the PCs to win a Medium difficulty encounter;

\begin{align}
    \rounds &\simeq \left(\frac{\RTWM}{\RTWM}\right) \cdot \frac{\sqrt{20 \XP_{\NPC}}}{\eDPR_{\PC}} \nonumber \\\\ 
            &= \RTWM \left(\frac{\eDPR_{\PC}}{\sqrt{20 \XPM}} \cdot \frac{\sqrt{20 \XP_{\NPC}}}{\eDPR_{\PC}}\right) \nonumber \\\\ 
            &= \RTWM \left( \frac{\XP_{\NPC}}{\XPM} \right)^{1/2} \,. \label{eq:rounds-to-win-xp-only}
\end{align}

Only one more piece of information is needed to make Eqn. \eqref{eq:rounds-to-win-xp-only} practically useful. We need the number of rounds a Medium difficulty encounter is expected to take.

The rules for 5th edition don't say that much about how long combat is expected to take, but there is one bit of information we can use to infer $$\RTWM $$. In the "[Creating a Monster](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#CreatingaMonsterStatBlockSteps1115)" section in chapter 9 of the DMG (pg. 278), when describing how to calculate the average damage per round for a monster, it says

> If a monster’s damage output varies from round to round, calculate its damage output each round for the first three rounds of combat, and take the average.

Since a monster's CR represents the level a party of four PCs should be in order for it to be a Medium encounter, we can reasonably assume that the average length of a Medium encounter is around three rounds. Therefore, 

\begin{align}
    \rounds &\simeq 3 \left( \frac{\XP_{\NPC}}{\XPM} \right)^{1/2} \,. \label{eq:rounds-to-win-xp-only-final}
\end{align}

The form of Eqn. \eqref{eq:rounds-to-win-xp-only-final} now allows us to calculate the expected duration for any encounter with only a single monster in it using that monster's XP value, $$\XP_{\NPC}$$, along with the Medium difficult XP threshold for the PCs' level, $$\XPM$$. Figure <a href="#fig:rounds-per-encounter" class="fig-ref">2</a> (below) plots the average number of rounds given by Eqn. \eqref{eq:rounds-to-win-xp-only-final} for each encounter difficulty. The average number of rounds per encounter for each difficulty and across all levels is listed in the <a href="#tab:rounds-summary" class="fig-ref">Summary</a> table in the conclusion to this post (below).

<figure id="fig:rounds-per-encounter">
    {% include_relative fig-rounds-per-encounter-by-level-small.html %}
    {% include_relative fig-rounds-per-encounter-by-level-large.html %}
    <figcaption>Figure 2: Number rounds of combat predicted by Eqn. \eqref{eq:rounds-to-win-xp-only-final} for each encounter difficulty.</figcaption>
</figure>

# Rounds per full adventuring day
For a full adventuring day, the total number of rounds of combat can be calculated by multiplying the rounds per encounter, given by Eqn. \eqref{eq:rounds-to-win-xp-only-final}, by the average number of encounters for each encounter difficulty. The average number of encounters per day can be easily calculated by dividing the PCs' adventuring day XP budget, as given in the [Adventuring Day XP](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#AdventuringDayXP) table, by the XP thresholds for each difficulty, as listed in the [XP Threshold by Character Level](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#XPThresholdsbyCharacterLevel) table.

The results of this are shown in Fig. <a href="#fig:full-adventuring-day-by-level" class="fig-ref">3</a> (below). The average number of rounds per adventuring day for each difficulty is listed in the <a href="#tab:rounds-summary" class="fig-ref">Summary</a> table in the conclusion to this post (below).

<figure class="half" id="fig:full-adventuring-day-by-level">
    {% include_relative fig-encounters-per-full-adventuring-day-by-level-small.html %}
    {% include_relative fig-encounters-per-full-adventuring-day-by-level-large.html %}
    {% include_relative fig-rounds-per-full-adventuring-day-by-level-small.html %}
    {% include_relative fig-rounds-per-full-adventuring-day-by-level-large.html %}
    <figcaption>Figure 3: Number of encounters and the number of rounds per full adventuring days for each encounter difficulty.</figcaption>
</figure>

# Conclusion
The <a href="#tab:rounds-summary" class="fig-ref">Summary</a> table (below) averages the findings from the previous two sections across levels 1 through 20. As expected, the number of rounds per encounter increases for deadlier encounters. This trend towards longer encounters means that, while the number of encounters drops by 56% when increasing the average encounter difficulty from Medium to Deadly, the number of rounds only drops by 33%.

#### Summary
{% include_relative table-rounds-summary.html %}

Before closing, it's worth mentioning again that the results shown here are only truly accurate for encounters with only a single monster. For encounters with more monster, additional approximations will need to be taken in order to account for things like abilities that damage multiple targets simultaneously. So, while these results are limit at the moment, they do server as a good first step towards a better understanding of how encounter design impact the number of rounds a combat encounter is likely to take.

I plan to do more work on this topic in the future to produce a more general equation, and will either present that as a separate post or I will update this post with those findings.