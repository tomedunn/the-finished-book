---
title: "Baseline Player Character Stats"
excerpt: "An analysis of how player character stats scale as they level up."
date: 2023-08-25
last_modified_at: 2023-08-25
tags:
  - analysis
  - classes
---

{% include LaTex.html %}

# Introduction

In [Baseline Monster Stats]({{ site.url }}{{ site.baseurl }}{% link _monsters/baseline-monster-stats.md %}), I used published monsters to determine how a typical monster scales with their challenge rating (CR) in 5th edition D&D (5e). In this post, I extend the same treatment to player characters. 

In addition to shining a light on how 5e is designed and balanced, these results, combined with the monster trends established previously, will be useful in understanding how combat changes as the player characters level up. It will also allow for better [valuing of conditions]({{ site.url }}{{ site.baseurl }}{% link _theory/valuing-conditions.md %}), which can be useful in determining if game mechanics like feats and spells are balanced relative to the rest of the game.

<!--
# Review

To summarize the findings from [Baseline Monster Stats]({{ site.url }}{{ site.baseurl }}{% link _monsters/baseline-monster-stats.md %}), the baseline values for monster damage per round and hit points scale with CR in the following ways,
\begin{align}
    \DPR &\approx
    \begin{cases} 
        \ \ \ \ 6 + \ \  6 \cdot \CR & \CR \lt 20\,; \\\\ 
        132 + 12 \cdot \left( \CR - 20 \right) & \CR \geq 20\,,
    \end{cases} \\\\ 
    \HP &\approx
    \begin{cases} 
        \ \ 16 + 16 \cdot \CR & \CR \lt 20\,; \\\\ 
        368 + 48 \cdot \left( \CR - 20 \right) & \CR \geq 20\,,
    \end{cases}
\end{align}
and for attack bonus, save DC, armor class, and saving throw bonus values,
\begin{align}
    \AB &\approx \ \ 3.5 + \CR/2 \,, \\\\ 
    \DC &\approx    11.5 + \CR/2 \,, \\\\ 
    \AC &\approx    13.0 + \CR/3 \,, \\\\ 
    \SB &\approx \ \ 0.0 + \CR/2 \,. 
\end{align}
-->

# Baseline Classes

Trying to encapsulate all of the build options (i.e., ability scores, feats, subclasses, multiclassing, magic items, etc) available to player characters in 5e would be an extraordinary undertaking due to the shear number of possible combinations. So, in order to simplify things, in this post I'll be limiting my analysis to just the base mechanics for each class (i.e., no subclasses) without feats or magic items. This is similar to the approach taken in my analysis of [player character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}).

The player characters used in this analysis were built using a standard point buy for ability scores, with racial bonuses of either a $$+2$$ to one ability score and $$+1$$ to another, or $$+1$$ to three different ability scores. Ability Score Improvements were used to increase each class's primary attacking stat first, followed by their secondary stat in the case of classes like the monk, and finally towards boosting defensive stats like Dexterity or Constitution. 

For a summary of each class's starting stats see the [Initial Ability Scores](#tab:pc-baseline-ability-scores){: .fig-ref} table (below). Subclasses were also not included in these calculations. Any further considerations, like equipment, are discussed in their relevant sections below.

<div class="dataframe center" style="width:100%;">
    <h3 id="tab:pc-baseline-ability-scores">Initial Ability Scores</h3>
    {% include_relative baseline-player-character-stats/tab-pc-baseline-ability-scores.html %}
</div>

**Note.** These starting ability scores differ from those used in my posts on [player character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}). I plan on unifying the two in the future, but for now this means there are slight inconsistencies in the results between the two.
{: .notice--warning}

# Offensive Stats

For player character attack bonus (AB), Fig. [1](#fig:ab-vs-level){: .fig-ref} (below) shows how each class changes as they level up. The bulk of the improvements come from increases to each class's proficiency bonus, which increases from $$+2$$ to $$+6$$, with additional contributions from improvements to their attack's ability score via Ability Score Improvement features, which increase from $$+3$$ to $$+5$$. Combined, most classes increased their AB by $$+6$$ by the time they reached level 20.

<figure id="fig:ab-vs-level">
    {% include_relative baseline-player-character-stats/fig-ab-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-ab-vs-level-large.html %}
    <figcaption>Figure 1: Shows attack bonus for player characters at each level.</figcaption>
</figure>

The trends for AB are mirrored for most classes in saving throw difficulty class (DC) values, as shown in Fig. [2](#fig:dc-vs-level){: .fig-ref} (below). The classes that deviate from this the most are the monk, paladin, and ranger since their saving throw DCs rely on different ability scores than those used for their attack bonuses. Still, unless a player chooses to neglect improving these secondary stats, each will cover the same overall range as those other classes.

<figure id="fig:dc-vs-level">
    {% include_relative baseline-player-character-stats/fig-dc-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-dc-vs-level-large.html %}
    <figcaption>Figure 2: Shows save difficulty class for player characters at each level. Barbarians, fighters, and rogues were excluded because they lack a default save DC stat in their base class.</figcaption>
</figure>

The average trends for AB and DC shown in Figs. [1](#fig:ab-vs-level){: .fig-ref} and [2](#fig:dc-vs-level){: .fig-ref} can be approximated using the following formula,
\begin{align}
    \AB &\approx \ \ 4.6 + \LV/3 \,, \label{eq:ab-approx} \\\\ 
    \DC &\approx    12.6 + \LV/3 \,, \label{eq:dc-approx}
\end{align}
where $$\LV$$ is the player character's level.

When compared against the same trends for [monster offensive stats]({{ site.url }}{{ site.baseurl }}{% link _monsters/baseline-monster-stats.md %}#conclusion), AB and DC values for player character start off slightly higher than for monsters but increase noticeably slower. It's interesting to note that this difference in scaling vanishes when factoring in magic items for player characters, which can add up to $$+3$$ to AB and DC by level 20.

Comparing Eqns. \eqref{eq:ab-approx} and \eqref{eq:dc-approx} against [monster defensive stats]({{ site.url }}{{ site.baseurl }}{% link _monsters/baseline-monster-stats.md %}#conclusion), as shown in Fig. [3](#fig:hit-fail-probabilities){: .fig-ref} (below), the average probability of a player character's attack hitting a monster who's CR equals their level holds fixed around $$65\%$$, while the odds of such a monster failing a saving throw starts off at $$60\%$$ at level 1 before steadily dropping down to $$40\%$$ at level 20.

<figure id="fig:hit-fail-probabilities">
    {% include_relative baseline-player-character-stats/fig-hit-fail-probabilities-small.html %}
    {% include_relative baseline-player-character-stats/fig-hit-fail-probabilities-large.html %}
    <figcaption>Figure 3: Shows the average probability that a player character's attack will hit a level appropriate monster, or that such a monster will fail a saving throw against the player character's save DC.</figcaption>
</figure>

This means that, in the absence of magic items, player characters that rely on attacks maintain their chance to hit level appropriate monsters as they level up, while characters who rely on saving throws affect their targets less and less often. This may explain why abilities and spells that rely on saving throws often deal half damage when a target succeeds on the saving throw, rather than no damage.

If we factor in bonuses to AB and DC from magic items as the player characters level up, the probability of hitting a monster with an attack increases up to around $$80\%$$ at level 20, while the chance of a monster failing a saving throw stays fairly flat, decreasing only slightly down to $$55\%$$. Given the powerful impact that non-damaging saving throw effects can have (often known as "save or suck" abilities), it makes sense that monsters were designed to be a bit more resilient against such effects compared to attacks when the player characters are enhanced by magic items.

The last offensive stat to consider is single target damage per round (DPR). These values, shown in Fig. [4](#fig:dpr-vs-level){: .fig-ref} (below), were taken from the simulations I ran previously for my post on [player character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}), which looked at each base class's average performance across a full adventuring day made up of Medium encounters. 

<figure id="fig:dpr-vs-level">
    {% include_relative baseline-player-character-stats/fig-dpr-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-dpr-vs-level-large.html %}
    <figcaption>Figure 4: Shows the average single target DPR for player characters at each level, assuming all attacks hit and all saving throws fail.</figcaption>
</figure>


The same caveats that applied to that post apply here as well. Namely, that only single target damage was considered and that spell templates were used for spellcasters rather than officially published spells. Because of these simplifications, these results should be interpreted as reflecting spellcaster single target damage budgets, rather than their actual single target damage capabilities.

The overall spread in DPR values stays relatively tight until higher levels where the paladin and warlock jump a ways in front of the rest. Furthermore, the dip seen in the monk's DPR at level 18 comes from them using their first action to activate Empty Body for the added durability. 

The average trend for single target DPR shown in Fig. [4](#fig:dpr-vs-level){: .fig-ref} can be approximated using the following formula,
\begin{align}
    \DPR &\approx    7 + 2 \cdot \LV \,.
\end{align}
For context, this average scales slightly faster than the extra damage from a rogue's Sneak Attack feature.


# Defensive Stats

For player character armor class (AC), each class was given the armor in their starting equipment at level 1 (no heavy armor for the cleric, and no shields for the fighter or paladin), and replaced with higher AC options as they became available at higher levels. For classes who would benefit from them, _studded leather armor_ was made available at level 5, _half plate_ at level 7, and _plate_ at level 10. 

For the sorcerer and wizard, _mage armor_ was added at level 5, and a $$+2$$ to AC was added at level 11 to approximate the impact of the _shield_ spell. The resulting AC values for each class are shown in Fig. [5](#fig:ac-vs-level){: .fig-ref} (below).

<figure id="fig:ac-vs-level">
    {% include_relative baseline-player-character-stats/fig-ac-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-ac-vs-level-large.html %}
    <figcaption>Figure 5: Shows armor class for player characters at each level.</figcaption>
</figure>

For saving throw bonuses (SB), the Evasion feature was estimated as a $$+6$$ to Dexterity saving throw for monks and rogues to reflect the damage reduction it provides, the Danger Sense feature for the barbarian was estimated as a $$+4$$ to Dexterity saving throws due to it granting advantage, and each use of Indomitable for the fighter was estimated as a $$+1/3$$ to all saving throws. The average SB across all ability scores for each class are shown in Fig. [6](#fig:sb-vs-level){: .fig-ref} (below).

<figure id="fig:sb-vs-level">
    {% include_relative baseline-player-character-stats/fig-sb-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-sb-vs-level-large.html %}
    <figcaption>Figure 6: Shows the average saving throw bonus for player characters at each level.</figcaption>
</figure>

In comparison to offensive stats shown in the previous section, AC and SB show a much higher level of variation than AB and DC. The spread for AC is particularly wide, with classes spread fairly evenly across the distribution. And, while the spread of SB values is tight for the majority of classes, the monk and the paladin show up as clear outliers due to contributions from Diamond Soul (level 14) and Aura of Protection (level 6) respectively.

The average trends for AC and SB can be approximated using the following formulas,
\begin{align}
    \AC &\approx    14.7 + \LV/6 \,, \label{eq:ac-approx} \\\\ 
    \SB &\approx \ \ 1.5 + \LV/5 \,. \label{eq:sb-approx}
\end{align}

<!--
Comparing these to Eqns. \eqref{eq:ab-approx} and \eqref{eq:dc-approx} highlights that AC and SB increase by roughly have as much as AB and DC from levels 1-20. 
-->

When compared against monster AB and DC values, as shown in Fig. [7](#fig:hp-vs-level){: .fig-ref} (below), the probability of a player character being hit by an attack, or failing a saving throw, from a level appropriate monster show very different trends than those shown in Fig. [3](#fig:hit-fail-probabilities){: .fig-ref} for attacks and saves against monsters from player characters. The overall average for both is close to the assumed baseline value of $$65\%$$, but rather than staying fixed or decreasing, both increase steadily as the player characters level up.

<figure id="fig:hp-vs-level">
    {% include_relative baseline-player-character-stats/fig-defense-probabilities-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-defense-probabilities-vs-level-large.html %}
    <figcaption>Figure 7: Shows average probability of a player character failing a saving throw or being hit by an attack from a level appropriate monster at each level.</figcaption>
</figure>

If we factor in bonuses to AC from magic items as the player characters level up, the probability of being hit by an attack will come down close to the $$65\%$$ baseline at level 20. Bonuses to player character SB values will have a similar effect for failing saving throws, but such items are generally less common.

Lastly, for player character hit points, the barbarian's Rage feature was approximated as a $$50\%$$ increase in adjusted hit points when used, the monk's Empty Body feature was approximated as a $$100\%$$ increase in adjusted hit points for levels 18 and above, and the rogue's Uncanny Dodge feature was approximated as a $$20\%$$ increase in adjusted hit points for levels 5 and above. The resulting adjusted hit point values are shown in Fig. [8](#fig:adj-hp-vs-level){: .fig-ref} (below).
<figure id="fig:adj-hp-vs-level">
    {% include_relative baseline-player-character-stats/fig-adj-hp-vs-level-small.html %}
    {% include_relative baseline-player-character-stats/fig-adj-hp-vs-level-large.html %}
    <figcaption>Figure 8: Shows average adjusted hit points for player characters at each level.</figcaption>
</figure>

The majority of classes scale according to their hit dice as expected, while the barbarian and monk stand out as clear outliers due to the large hit point multipliers provided by Rage and Empty Body respectively. The fighter stands out to a lesser extent due to the healing from their Second Wind feature. 

Combined, these outliers are large enough to skew the mean a fair bit, but if we look at the median adjusted hit points rather than the mean, that skew goes away and the average can be approximated using the following formula,
\begin{align}
    \HP &\approx \ \  1 + 7 \cdot \LV \,. \label{eq:ahp-approx}
\end{align}
For context, this trend is close to the amount of hit points we would expect for a character with a d8 hit die and a $$+2$$ Constitution modifier.

# Conclusion
To summarize these findings, the average DPR and hit points for a typical player character can be approximated using the following formulas,
\begin{align}
    \DPR &\approx 7 + 2 \cdot \LV \,, \\\\ 
    \HP  &\approx 1 + 7 \cdot \LV \,,
\end{align}
and for attack bonus, save DC, armor class, and average saving throw bonus using,
\begin{align}
    \AB &\approx \ \ 4.6 + \LV/3 \,, \\\\ 
    \DC &\approx    12.6 + \LV/3 \,, \\\\ 
    \AC &\approx    14.7 + \LV/6 \,, \\\\ 
    \SB &\approx \ \ 1.5 + \LV/5 \,. 
\end{align}

Before closing, there's one additional quantity I'd like to touch on, and that's how many rounds it should take for a party of four to defeat a single monster who's CR equals the party's level. This quantity, along with the number of rounds it should take the monster to defeat the party of four, is shown in Fig. [9](#fig:rounds-to-win){: .fig-ref} (below).

<figure id="fig:rounds-to-win">
    {% include_relative baseline-player-character-stats/fig-rounds-to-win-small.html %}
    {% include_relative baseline-player-character-stats/fig-rounds-to-win-large.html %}
    <figcaption>Figure 9: Shows the typical number of rounds it takes a party of four to defeat a level appropriate monster or vice-versa.</figcaption>
</figure>

This shows that on average, it takes a party of four player characters about $$2.5$$ rounds to defeat the monster, which is consistent with the general expectation that a Medium encounter should take between 2-3 rounds of combat to complete.

And it shows that, on average, it takes the monster close to seven rounds to defeat a party of four player characters. If we assume the monster's DPR is constant across those rounds, then this means the monster can be expected to do $$35.7\%$$ of the party's maximum hit points in damage in the time it takes the party to defeat them. This is slightly more than the value predicted [here]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}#fig:encounter-xp-thresholds-vs-level) from comparing player character XP thresholds from the encounter building rules against half of the adventuring day daily XP budget.