---
title: "Calculating Monster XP"
excerpt: "Compares listed monster XP values with those calculated from their offensive and defensive abilities."
date: 2021-11-24
last_modified_at: 2023-3-4
#tags:
#  - analysis
#  - CR
#  - monsters
---

{% include LaTex.html %}


# Introduction

When it comes to monsters, challenge rating (CR) is the metric most often used to describe a monster's overall combat strength. However, rather than relying on CR, the rules for [encounter building](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters) in the _Basic Rules_ opt for using monster experience points (XP) instead. This suggests that XP is a more direct measure of a monster's true combat strength than CR, and that the XP values assigned to each CR were not arbitrarily chosen.

If XP values are not arbitrary and are, in fact, proportional to a monster's total combat strength then that means we should be able to calculate a monster's XP value from their offensive and defensive stat, similarly to how the DMG uses those stats to calculate a monster's CR. Being able to calculate the XP for each monster individually would also provide us with a continuum of XP values to pull from when designing encounters, rather than the fixed XP values assigned to each CR.

In this post, I review one such method for calculating monster XP (the only method I've come across, to be fair). I show how it compares to listed XP values for published monsters, and how it can be used to improve our understanding of modifying monsters and balancing encounters.

# Calculating XP

The math behind this one is a bit complicated. For those interested in a full derivation, check out my post [XP and Encounter Balancing]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}). For the purposes of this analysis, though, I'll be skipping the derivation and focusing on the conclusions for calculating monster XP instead.

With that out of the way, XP in 5th edition is proportional to the product of a monster's effective hit points $$(\eHP\,)$$ and effective damage per round $$(\eDPR\,)$$, 
\begin{equation}
    \label{eq:XP-simple}
    \XP_{\NPC} = \frac{1}{4} \eHP \cdot \eDPR\,,
\end{equation}
which can be approximated as, 
\begin{equation}
    %\XP_{\NPC} = \frac{1}{4} \HP \cdot \DPRhit \left(1 + 0.077\left(\AC + \AB - 15\right)\right)\,,
    \XP_{\NPC}  = \frac{1}{4}\HP \cdot \DPRhit \left( \frac{ \AC + \AB - 2 }{13} \right)\,,
    \label{eq:XP-full}
\end{equation}
where $$\HP$$ is the monster's average hit points, $$\AC$$ is their effective armor class, $$\DPRhit$$ is their average damage per round assuming all attacks hit, and $$\AB$$ is their effective attack bonus.

When calculating a monster's XP using Eqn. \eqref{eq:XP-full}, I'll be following the same guidance given in "[Creating a Monster](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#CreatingaMonster)" from chapter 9 of the DMG for calculating monster CR values. The key components of which are outlined below.

* _**Three Round Encounters.**_ Combat is assumed to last three rounds. Contributions to $$\AC$$, $$\AB$$, and $$\DPRhit$$ are averaged over over these rounds, while contributions to $$\HP$$ are added together.

* _**Limited Area of Effect Targets.**_ Abilities capable of targeting an area of effect (AoE) are assumed to only hit a modest number of target. This number is typically two for standard sized AoE abilities, like the _[fireball](https://www.dndbeyond.com/spells/fireball)_ spell.

<!--
With that out of the way, XP in 5th edition is proportional to the product of a monster's effective hit points $$(\eHP)$$ and effective damage per round $$(\eDPR)$$, 

\begin{equation}
    \label{eq:XP-simple}
    \XP_{\NPC} = \frac{1}{4} \eHP \cdot \eDPR\,.
\end{equation}

A monster's _eHP_ can be calculated using the same adjusted hit points (HP) and adjusted armor class (AC) used when calculating CR, following the rules in "Creating a Monster" from chapter 9 of the DMG, along with the following equation, 

\begin{equation}
    \label{eq:eHP}
    eHP_{\rm NPC} = HP \cdot 1.05^{AC - 8}\ .
\end{equation}

Similarly, a monster's _eDPR_ can be calculated using the adjusted damage per round (DPR) and adjusted attack bonus (AB) used when calculating CR, following the same rules, according to the following equation,

\begin{equation}
    \label{eq:eDPR}
    eDPR_{\rm NPC} = DPR \cdot 1.05^{AB - 6}\ .
\end{equation}

Combining these two equations together, a monster's XP can be calculated as follows,

\begin{equation}
    \label{eq:XP-full}
    \XP_{\NPC} = \frac{1}{4} HP \cdot DPR \cdot 1.05^{AC + AB - 14}\, .
\end{equation}
-->

## Example: Air Elemental

With the basic equations defined, lets look at an example monster to better understand how they work. For this example, I'll be using the **air elemental** published in the _Basic Rules_, the stat block of which is shown below.

<center>
{% include_relative calculating-monster-xp/air-elemental.html %}
</center>

For defensive stats, the air elemental has 90 (12d10 + 24) HP and an AC of 15. Because the air elemental has resistances to multiple damage types - including bludgeoning, piercing, and slashing from nonmagical attacks - the DMG recommends multiplying its HP by 1.5 for an adjusted total of 135 HP. <!--Using these values, the DMG estimates a **defensive CR of 5** and Eqn. \eqref{eq:eHP} gives it **190.0 _eHP_**.-->

On the offensive side of the equation, the air elemental can use its Multiattack or Whirlwind action during its turn. The Multiattack action allows the air elemental to make two Slam attacks for a total of 28 (4d8 + 10) bludgeoning damage with an AB of +8.

The Whirlwind action requires a DC 13 Strength saving throw, which is roughly equivalent to a +5 attack bonus, and deals 15.5 (3d8 + 2) bludgeoning damage to creatures who fail their save, with an additional 3.5 (1d6) bludgeoning damage if the creature is thrown into an object. Assuming the extra damage is always applied and that two targets are affected, the action deals 38 bludgeoning damage in total.

<!--Assuming the air elemental is able to use Whirlwind once and Slam twice during a three round encounter, the DMG estimates an **offensive CR of 5** and Eqn. \eqref{eq:eDPR} gives it **29.7 _eDPR_**.-->
Assuming the air elemental is able to use Whirlwind once and Multiattack twice during a three round encounter, their average $$\DPRhit$$ would be 31 and their effective attack bonus would be around +7.

<!--Feeding these values into Eqn. \eqref{eq:XP-full} gives **1,410.75 XP** which, while only 78% of the creature's listed value of 1,800 XP, is just high enough to still qualify it as a CR 5 monster. This tells us that the air elemental is likely on the weaker side of of CR 5. And, given how much its HP was adjusted to account for its multiple resistances, when facing PCs with access to magical weapons its combat strength will be more on the lower side of CR 4, and possibly even on the upper side of CR 3 depending on how its played.-->

Feeding these values into Eqn. \eqref{eq:XP-full} gives 1,610 XP, while only 89% of the creature's listed value of 1,800 XP, is still high enough to qualify it as a CR 5 monster. This tells us that the air elemental is likely on the weaker side of of CR 5. And, given how much its HP was adjusted to account for its multiple resistances, when facing PCs with access to magical weapons its combat strength will be more on the lower side of CR 4, and possibly even on the upper side of CR 3 depending on how its played.

Not only does this method for calculating a monster's XP give us additional insights into how tough the monster might be for our PCs, it also gives us an easy method for adjusting monster's to fit our needs. When facing PCs with magical weapons, we can increase the air elemental's hit points by 50% to compensate for their resistances being less valuable. Alternatively, if we it to be a more offensively oriented monster, we could increase the damage of each of the air elemental's actions by 50% instead.

## Full Comparison

To check the accuracy of this approach, I applied Eqn. \eqref{eq:XP-full} to monsters with CRs of 1 or more, taken from official 5th edition source books. I used the same adjusted HP, AC, DPR, and AB values I used previously in [Calculating Monster CR]({{ site.url }}{{ site.baseurl }}{% link _monsters/calculating-monster-cr.md %}). A comparison of the calculated XP values and listed XP values is shown in Fig. <a href="#fig:calc-xp-vs-xp-log-log" class="fig-ref">1</a> below.

<figure id="fig:calc-xp-vs-xp-log-log">
    {% include_relative calculating-monster-xp/fig-calc-xp-vs-xp-log-log-small.html %}
    {% include_relative calculating-monster-xp/fig-calc-xp-vs-xp-log-log-large.html %}
    <figcaption>Figure 1: Calculated XP mean (line) and 60% confidence interval (shaded region) vs listed XP.</figcaption>
</figure>

The general trend shows a strong correlation between the two, however, there are some small differences. Namely, that this method tends to underestimate monster XP at low CRs and slightly overestimates it at high CRs.

<figure id="fig:xp-cr-vs-cr">
    {% include_relative calculating-monster-xp/fig-xp-cr-vs-cr-small.html %}
    {% include_relative calculating-monster-xp/fig-xp-cr-vs-cr-large.html %}
    <figcaption>Figure 2: Calculated CR mean and 60% confidence interval vs listed CR.</figcaption>
</figure>

Next, I converted the calculated XP values to their equivalent CR for each monster. As Fig. <a href="#fig:xp-cr-vs-cr" class="fig-ref">2</a> illustrates, the CRs calculated using this method are generally in good agreement with the CRs listed in the monsters' stat blocks, with the vast majority of monsters having a calculated CR within +/- 1 of their listed value. 

<figure id="fig:ecr-dmg-cr-delta-vs-cr">
    {% include_relative calculating-monster-xp/fig-ecr-dmg-cr-delta-vs-cr-small.html %}
    {% include_relative calculating-monster-xp/fig-ecr-dmg-cr-delta-vs-cr-large.html %}
    <figcaption>Figure 3: Shows the difference between the calculated CR and the listed CR as a function of CR for both calculated XP and CR calculated using the method given in the DMG.</figcaption>
</figure>

When compared with the method for calculating CR in the DMG, as shown in Fig. <a href="#fig:ecr-dmg-cr-delta-vs-cr" class="fig-ref">3</a>, the results are also quite close. Both tend to underestimate monster CRs at the lower end of the CR spectrum, and both tend to overestimate it as well at the higher end. 

<!---
Where the two differ the most is between CR 12 and 23. The reason for this difference comes from how each method handles monsters with better/worse than average AC or AB. 

The DMG accounts for AC and AB is by adjusting the monster's defensive or offensive CR by +/-1 for ever two points either is above/below the recommended value in the DMG for the monster's HP or DPR. This sort of adjustment makes sense, so long as the new CR's effective HP or DPR is sufficiently larger than the initial one's.

In comparison, the method used for calculating XP assumes each +2 to AC (AB) is worth roughly 10% more HP (DPR). If the HP (DPR) of the new CR is less than 10% more than the previous CR's then the DMG's method will end up underestimating a monster's strength relative to what we get when calculating XP.

<figure class="half" id="fig:hp-dpr-ratio-and-dmg-cr-delta-vs-cr">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/calculating-monster-xp/hp-dpr-ratio-vs-cr.svg">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/calculating-monster-xp/dmg-cr-delta-vs-cr.svg">
    <figcaption>Figure 4: Shows (left) the ratio between the target HP and DPR at the given CR and the CR below it, and (right) the difference between CR values calculated from XP and those calculated using the DMG.</figcaption>
</figure>

As Fig. <a href="#fig:hp-dpr-ratio-and-dmg-cr-delta-vs-cr" class="fig-ref">4</a> shows, when the HP and DPR of the next CR are less than 10% higher than the previous one, the DMG reports a CR below that of the XP calculation. 

Assuming a base chance to hit with an attack of 70% for both PCs and NPCs when facing tier appropriate enemies, each +2 to AC is worth roughly 14% more HP and each +2 to AB is worth roughly 14% more DPR. This means that while the XP calculation slightly underestimates the impact of AC and AB on CR across the full CR range, the method presented in the DMG varies from significantly overestimating it for CRs less than 5, to significantly underestimates it for CRs between 15 - 19, as well as CRs 25 and above.
--->

# Conclusion

In conclusion, I have demonstrated how XP can be calculated directly from monster stat blocks with good accuracy for the majority of published monsters, and that those XP values can be used to accurately estimate a monster's CR.

This understanding of XP highlights new and intuitive ways we can adjust monsters to better match any one particular group. There is a lot more I could dive into here regarding XP calculations for published monsters but I think those are topics best left for a later post. 