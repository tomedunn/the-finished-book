---
title: "Encounter Building in Pathfinder vs D&D"
excerpt: "How similar is the math between the XP and encounter building systems in D&D 5e and Pahtfinder 2e?"
permalink: /:collection/:name/
date: 2023-1-17
last_modified_at: 2023-3-1
tags:
  - analysis
  - encounter balancing
  - encounter multiplier
  - pathfinder 2e
  - theory
  - xp
---

{% include LaTex.html %}

# Introduction
This will be a bit different from my typical post. Until now, I've exclusively covered the game mechanics of D&D 5th edition (D&D 5e), but in this post I'd like to take a look at how the XP and encounter building rules in Pathfinder 2nd edition (PF 2e) work. Hopefully, this will server as an interesting contrast between the two systems and a good test of the theoretical approaches I've developed so far in my analysis of D&D 5e's monsters and encounter building rules.


# PF 2e encounter building overview

Just like in D&D 5e, the [encounter building rules](https://2e.aonprd.com/Rules.aspx?ID=497) in PF 2e can be boiled down to calculating an XP value for the encounter based on the monsters in it and comparing that value against the party's XP thresholds to determine the encounter's difficulty. However, there are some key differences.

* **Relative monster XP.** Monster XP values are determined by the monster's level (PF 2e's version of CR) _relative_ to the party's level.
* **Fixed XP thresholds.** The party's XP thresholds do not change with the party's level.
* **No encounter multiplier.** An encounter's XP total is equal to the sum monsters' individual XP values with no additional modifications.

Monsters having relative XP values and the party having fixed XP thresholds are obviously interconnected. If the party's XP thresholds don't increase as the party levels up then monster XP values must decrease to reflect the fact that the party is getting stronger. Conceptually, this is equivalent to how D&D 5e handles it, where monster XP increases with CR and the party's XP thresholds increase with their level. However, as I discuss in the next section, "[Monster XP scaling](#monster-xp-scaling)", there's an additional requirement needed to make it work.

The lack of an encounter multiplier in PF 2e is a bit more puzzling. In D&D 5e, the encounter multiplier is used to account for the fact that a group of monsters is deadlier when fought together than they are when fought separately. This fact is not unique to D&D 5e, which means the PF 2e rules must be accounting for it in other ways. I explore how exactly the PF 2e rules are doing this in "[Accounting for groups](#accounting-for-groups)" later in this post.


# Monster XP scaling

As I mentioned in the previous section, in order for PF 2e's encounter building rules to work using relative monster XP and fixed encounter difficulty XP thresholds, there's an additional requirement the system must satisfy. Specifically, monsters and PCs must scale in combat strength (i.e., their XP) exponentially with their level.

In simple terms, this means a monster's XP value should always be a constant multiple of the XP value for monsters one level lower, and looking at PF 2e's encounter building rules this appears to be the case.

According to PF 2e's _Gamemastery Guide_ ([p. 198](https://2e.aonprd.com/Rules.aspx?ID=1371)),

> Under the math in the Core Rulebook, two monsters of a certain level are roughly as challenging as a single monster 2 levels higher.

This is reinforced by the fact that monster [relative XP values](https://2e.aonprd.com/Rules.aspx?ID=499) double every two levels, as shown in the <a href="#tab:pf-monster-xp" class="fig-ref">Pathfinder 2 monster XP</a> table (below).

<div class="dataframe center" style="width:660px;">
<h3 id="tab:pf-monster-xp">Pathfinder 2 monster XP</h3>
<table border="0" style="width: 600px; max-width: 100%; margin-left: auto; margin-right: auto;">
    <thead>
        <tr>
            <td style="text-align:center"><strong>Creature Level</strong></td>
            <td style="text-align:center"><strong>Monster XP</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">Party Level -4</td>
            <td style="text-align:center">10</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -3</td>
            <td style="text-align:center">15</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -2</td>
            <td style="text-align:center">20</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -1</td>
            <td style="text-align:center">30</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level</td>
            <td style="text-align:center">40</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +1</td>
            <td style="text-align:center">60</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +2</td>
            <td style="text-align:center">80</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +3</td>
            <td style="text-align:center">120</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +4</td>
            <td style="text-align:center">160</td>
        </tr>
    </tbody>
</table>
</div>

These both point to monster XP in PF 2e scaling exponentially in the following way, 

\begin{align}
    \XP(\LV\,) &= \sqrt{2} \, \XP (\LV - 1) \label{eq:xp-exp-recursive} \\\\ 
               &= \XP_0 \cdot 2^{\LV/2} \,, \label{eq:xp-exp}
\end{align}

where $$\LV$$ is the monster's level and $$\XP_0$$ is the XP of a level 0 monster. 

If we assume that Eqn. \eqref{eq:xp-exp} accurately represents how monsters scale in PF 2e then our extra scaling requirement is satisfied, but that's a rather big assumption. To check its validity, we need an independent way of calculating monster XP.

Thankfully, we already have a way of calculating monster XP straight from a monster's stat block. In my previous post on [XP and encounter balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}) in D&D 5e, I derived a [formula]({{ site.data.page-links.xp-and-encounter-balancing.path }}#mjx-eqn-eq:xp-npc-explicit) for calculating monster XP from the game's basic mechanics for dealing damage in combat,

\begin{align}
    \XP  &\propto \HP \cdot \DPRhit \cdot 1.077^{\AC + \AB} \,. \label{eq:xp-dnd}
\end{align}

Here, $$\HP$$ is the creature's average hit points, $$\DPRhit$$ is their average damage assuming all attacks hit, $$\AC$$ is their effective armor class, and $$\AB$$ is their effective attack bonus. The base of the exponential term in Eqn. \eqref{eq:xp-dnd}, $$1.077 \equiv 14/13$$, comes from D&D 5e having a baseline chance to hit with an attack of $$65\%$$, or a probability of $$13/20$$.

Since the mechanics behind dealing damage in PF 2e are essentially the same as they are in D&D 5e (i.e., via attack rolls and saving throws), Eqn. \eqref{eq:xp-dnd} should be capable of calculating XP values for monsters in PF 2e, so long at the baseline chance to hit in PF 2e is close to $$65\%$$.

Using values for $$\HP$$, $$\AC$$, $$\DPRhit$$, and $$\AB$$ taken from "[Building Creatures](https://2e.aonprd.com/Rules.aspx?ID=995)" in chapter 2 of the PF 2e's _Gamemastery Guide_, Fig. <a href="#fig:pf-xp-vs-level" class="fig-ref">1</a> (below) shows XP values given by Eqn. \eqref{eq:xp-dnd} for each level. For simplicity, I fixed the XP of a level 1 monster at 1 XP but, since we're only interested in the scaling behavior, any value would have worked just as well.

<figure id="fig:pf-xp-vs-level">
    {% include_relative fig-pf-xp-vs-level-small.html %}
    {% include_relative fig-pf-xp-vs-level-large.html %}
    <figcaption>Figure 1: Shows monster XP values for Pathfinder 2e calculated using Eqn. \eqref{eq:xp-dnd} along with "Moderate" monster stats taken from "<a href="https://2e.aonprd.com/Rules.aspx?ID=995">Building Creatures</a>" in chapter 2 of the PF 2e's <i>Gamemastery Guide</i>.</figcaption>
</figure>

Overall, the results are consistent with our earlier expectation that monster XP should double every two levels, especially for monsters level 10 and above. However, for lower levels monster XP grows substantially faster.

To better visualize how much faster, Fig. <a href="#fig:pf-xp-scaling" class="fig-ref">2</a> (below) plots the ratio of these XP values with those of monsters two levels lower.

<figure id="fig:pf-xp-scaling">
    {% include_relative fig-pf-xp-scaling-small.html %}
    {% include_relative fig-pf-xp-scaling-large.html %}
    <figcaption>Figure 2: Shows the ratio between monster XP values calculated using Eqn. \eqref{eq:xp-dnd} and those of a monster two levels lower.</figcaption>
</figure>

For monsters between levels 5 - 10, the XP scaling is a little bit higher than expected, but things really take off for monsters level 4 and below, which increase in power up to three times faster than expected!

Whether or not this poses a problem for building encounters at low levels depends on how PCs scale in comparison. If PCs scale similarly at these low levels, encounters with higher level monsters are likely to play out significantly more difficult than predicted using PF 2e's encounter building rules. However, if this scaling is unique to monsters and PCs continue to double in XP every two levels, then low level monsters are simply weaker than expected.

Low levels aside, the overall trends shown in Figs. <a href="#fig:pf-xp-vs-level" class="fig-ref">1</a> and <a href="#fig:pf-xp-scaling" class="fig-ref">2</a> confirm that Eqn. \eqref{eq:xp-exp} is an accurate representation of how monsters scale in PF 2e. It also means **monsters in PF 2e meet the scaling requirement needed to make its encounter building system work**.


# Accounting for groups

As mentioned earlier, a group of monsters fought together is more dangerous than those same monsters fought separately. The D&D 5e encounter building rules account for this by adjusting the total XP using an encounter multiplier. Essentially, the total XP of the monsters is multiplied by a number that's determined by the number of monsters and PCs in the encounter.

The encounter building rules in PF 2e make no such adjustments, simply using the total XP of the monsters in the encounter instead, which means they must be accounting for groups of monsters in other way. There are several ways an encounter building system can do this, but here I'll focus on two methods that I think are likely filling this role for PF 2e:

* **One monster per PC.** Centering the encounter building rules around one monster per PC reduces how much the encounter XP needs to be adjusted when dealing with larger or smaller groups of monsters.
* **Adjusted monster XP.** Increasing the relative XP values for monsters below the party's level and decreasing them for monsters above can offset the need for an encounter multiplier by accounting for needing more or fewer monsters to hit each encounter difficulty threshold.

<!--
* **Increased AoE damage.** Increasing how common area of effect damage abilities are, and increasing their damage relative to single target options, can reduce the need for an encounter multiplier by ensuring monsters are defeated in a similar number of rounds regardless of whether they're grouped with other monsters or not.
-->

## One monster per PC

In D&D 5e, the encounter building rules are centered around encounters with a party of four PCs against a single monster. This choice work fine when paired with an encounter multiplier, but without one it would significantly underestimate the difficulty of any encounter with more than two monsters.

If the D&D 5e encounter building rules were centered around encounters with four monsters instead of one - this can be done by dividing the encounter multiplier by two and multiplying monster XP by two - the need for an encounter multiplier would be dramatically reduced, because the error for not using one would be relatively small for a much wider range of encounters. The encounter multiplier for such a system is shown in Fig. <a href="#fig:encounter-multiplier" class="fig-ref">3</a> (below) along with the encounter multiplier used by the D&D 5e rules for a party of four.

<figure id="fig:encounter-multiplier">
    {% include_relative fig-encounter-multiplier-small.html %}
    {% include_relative fig-encounter-multiplier-large.html %}
    <figcaption>Figure 3: Shows the encounter multiplier from D&D 5e for party of four PCs (orange) as well as the same multiplier rescaled for a system that assumes four monsters per encounter as the default (blue).</figcaption>
</figure>

Under this alternative system, an encounter needs 15 or more monsters to warrant the same encounter multiplier that D&D 5e uses for an encounter with only three monsters. Put another way, if you were to remove the encounter multiplier from both systems, the system centered around four monsters would underestimate the difficulty of an encounter with 15 monsters by the same amount as the system centered around one monster would for three monsters.

While the PF 2e encounter building rules never explicitly say they're centered around encounters with four monsters, they do [suggest](https://2e.aonprd.com/Rules.aspx?ID=500) keeping the number of monsters close to the number of PCs,

> It’s best to use the XP increase from more characters to add more enemies or hazards, and the XP decrease from fewer characters to subtract enemies and hazards, rather than making one enemy tougher or weaker. Encounters are typically more satisfying if the number of enemy creatures is fairly close to the number of player characters.

If this is the case, which I suspect it is, it would reduce the need for an encounter multiplier in the PF 2e encounter building rules significantly but not entirely. The mismatch between calculated and actual difficulty would likely still be noticeable without some other form of correction, especially for encounters with only one monster and those with 11 or more monsters.


## Adjusting monster XP

For systems that use relative XP, such as PF 2e, it's possible to bake the XP scaling of the encounter multiplier into monster XP values directly. In doing so, weaker monsters have their XP values increased above what they would be normally, to account for needing more of them to fill an encounter, and stronger monsters have their XP values decreased, to account for needing fewer. The end result of this adjustment is that monster XP will increase slower than expected based on how their other combat stats change with their level.

However, as shown in Figs. <a href="#fig:pf-xp-vs-level" class="fig-ref">1</a> and <a href="#fig:pf-xp-scaling" class="fig-ref">2</a>, the relative XP values used in PF 2e's encounter building rules match the XP scaling calculated from monster combat stats using Eqn. \eqref{eq:xp-dnd}. Surely, this proves the relative XP values used by the PF 2e rules aren't being used to offset the need for an encounter multiplier, right? 

In short, no. There's one key mechanic, unique to PF 2e, that's missing from Eqn. \eqref{eq:xp-dnd} that can have exactly the kind of impact we're looking for. And, only shows up when looking at monsters in relative terms. That mechanic is how PF 2e handles critical hits.

In PF 2e, critical hits don't occur when you roll a natural 20 (there's a different effect for that). Instead, they occur when you roll 10 or more above the target's AC on an attack roll. Meaning, if a target has 10 AC, you would need to roll a 20 or higher on an attack roll for the result to be a critical hit.

For a base chance to hit of $$65\%$$ against creatures of the same level, the chance of scoring a critical hit in PF 2e is $$15\%$$. And, since PF 2e adds a creature's level when determining their attack bonus and armor class, a monster's chance to crit increase by $$5\%$$ for each level relative to the PCs', and their chance to be crit decreases by $$5\%$$ for each level as well. These probabilities are illustrated in Fig. <a href="#fig:pf-crit-probability" class="fig-ref">4</a> (below).

<figure id="fig:pf-crit-probability">
    {% include_relative fig-pf-crit-probability-small.html %}
    {% include_relative fig-pf-crit-probability-large.html %}
    <figcaption>Figure 4: Shows the average chance of an attack resulting in a critical hit for monsters (orange) and player characters (blue) as a function of a monster relative level.</figcaption>
</figure>

Since critical hits deal double damage in PF 2e, a $$5\%$$ higher chance to crit is equivalent to $$+1\,\AB$$ without the extra crit chance in terms of how much it increases an attack's average damage. Therefore, a PF 2e monster one level higher than the PCs effectively has $$+1\,\AB$$ and $$+1\,\AC$$ on top of what's listed in their stat block for the purpose of calculating their relative XP using Eqn. \eqref{eq:xp-exp}.

The the size of this correction is shown in Fig. <a href="#fig:pf-xp-multiplier-components" class="fig-ref">5</a> (below), along with the encounter multiplier from the previous section centered around encounters with four monsters (i.e., one per PC). The number of monsters used to determine the encounter multiplier was based on the number of monsters needed to fill each XP threshold at the monsters' relative level. For example, it would take 8 monsters with a relative level of $$-4$$ (10 XP each) to fill a Moderate encounter worth 80 XP, which would normally have an encounter multiplier of $$1.25$$.

<figure id="fig:pf-xp-multiplier-components">
    {% include_relative fig-pf-xp-multiplier-components-small.html %}
    {% include_relative fig-pf-xp-multiplier-components-large.html %}
    <figcaption>Figure 5: Shows the encounter multiplier for encounters made up of only monsters of the given level for each encounter difficulty, as well as the XP multiplier needed to account for PF 2e's critical hit rules.</figcaption>
</figure>

The correction needed to account for PF 2e's critical hit rules clearly opposes the impact of the encounter multiplier. However, as Fig.  <a href="#fig:pf-xp-adjusted" class="fig-ref">6</a> (below) shows, while the product of these two effects is essentially flat with respect to the monsters' relative level, the average value decreases as the encounter difficulty goes down.

<figure id="fig:pf-xp-adjusted">
    {% include_relative fig-pf-xp-adjusted-small.html %}
    {% include_relative fig-pf-xp-adjusted-large.html %}
    <figcaption>Figure 6: Shows the total XP multiplier for each encounter difficulty using the encounter multiplier and critical hit XP multiplier values shown in Fig. <a href="#fig:pf-xp-multiplier-components" class="fig-ref">5</a>.</figcaption>
</figure>

This behavior isn't cause for concern. In fact, it's expected. Since the number of monsters per encounter at each relative monster level decreases along with the encounter difficulty, so too will the encounter multiplier while the critical hit multiplier remains the same. The effect this ultimately has on the PF 2e encounter building rules is that the difference between each encounter difficulty is actually larger that it appears based on the listed XP thresholds.

The <a href="#tab:pf-adj-xp" class="fig-ref">Pathfinder Adjusted XP</a> table (below) shows how these adjusted XP thresholds compare with the XP of an Extreme encounter. What I find especially interesting, is that these new adjusted XP thresholds have ratios that are quite close to the ratios I calculated [previously]({{ site.data.page-links.xp-and-player-characters.path }}#fig:encounter-xp-thresholds-vs-level) for D&D 5e's Easy, Medium, and Deadly encounter difficulties.

<div class="dataframe center" style="width:660px;">
<h3 id="tab:pf-adj-xp">Pathfinder Adjusted XP</h3>
<table border="0" style="width: 600px; max-width: 100%; margin-left: auto; margin-right: auto;">
    <thead>
        <tr>
            <td style="text-align:center"><strong>Encounter Difficulty</strong></td>
            <td style="text-align:center"><strong>PF 2e <br> XP ratio</strong></td>
            <td style="text-align:center"><strong>PF 2e <br> adj XP ratio</strong></td>
            <td style="text-align:center"><strong>D&D 5e <br> XP ratio</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">Trivial (Easy)</td>
            <td style="text-align:center">0.25</td>
            <td style="text-align:center">0.13</td>
            <td style="text-align:center">0.15</td>
        </tr>
        <tr>
            <td style="text-align:center">Low (Medium)</td>
            <td style="text-align:center">0.38</td>
            <td style="text-align:center">0.25</td>
            <td style="text-align:center">0.30</td>
        </tr>
        <tr>
            <td style="text-align:center">Moderate (Hard)</td>
            <td style="text-align:center">0.50</td>
            <td style="text-align:center">0.36</td>
            <td style="text-align:center">0.45</td>
        </tr>
        <tr>
            <td style="text-align:center">Severe (Deadly)</td>
            <td style="text-align:center">0.75</td>
            <td style="text-align:center">0.69</td>
            <td style="text-align:center">0.70</td>
        </tr>
    </tbody>
</table>
</div>

<!--
## Increased AoE damage

Increasing how common area of effect damage abilities are, and increasing their damage relative to single target options, can reduce the need for an encounter multiplier by ensuring monsters are defeated in a similar number of rounds regardless of whether they're grouped with other monsters or not.

For area of effect damage, a quick comparison of damage dealing spells in PF 2e suggests area of effect spells generally deal about $$50\%$$ of the damage per target as single target spells. Also, the suggested damage for unlimited use multi-target effects in the rules for [building creatures](https://2e.aonprd.com/Rules.aspx?ID=995) is generally half that of the Moderate strike damage using the same number of actions. 

These are both quite similar to what's found in D&D 5e which, in the "Creating a Spell" section from chapter 9 of the _Dungeon Master's Guide_, suggests a multi-target spell that does half damage on a successful save should deal roughly $$55\%$$ of the damage per target of a single target attack spell. 

It's possible area of effect damage is simply more common in PF 2e classes. However, as I show [here]({{ site.data.page-links.encounter-multiplier-p1.path }}), the encounter multiplier used in D&D 5e already assumes a rather high percent of the party's damage come from area of effect abilities when fighting large groups of monsters.
-->


<!--

# XP scaling in Pathfinder

The XP and encounter building rules in PF 2e actually come in two flavors: "standard" and "proficiency without level" (PWL). In the "standard" version of the rules, a creature's level is added to their armor class, attack bonus, and saving throw bonuses, while in the PWL version it isn't. So a level 10 creature might have an attack bonus of +17 in the "standard" rules and a +7 under PWL.

This difference means that monsters under the "standard" system increase in combat power faster than they do under PWL. The [Standard vs PWL XP](#tab:standard-vs-pwl-xp) table (below) shows the relative XP values for PF 2e's "[standard](https://2e.aonprd.com/Rules.aspx?ID=499)" and [PWL](https://2e.aonprd.com/Rules.aspx?ID=1371) systems and, as expected, this faster scaling for the "standard" system is clearly evident.

<div class="dataframe center" style="width:660px;">
<h3 id="tab:standard-vs-pwl-xp">Standard vs PWL XP</h3>
<table border="0" style="width: 600px; max-width: 100%; margin-left: auto; margin-right: auto;">
    <thead>
        <tr>
            <td style="text-align:center"><strong>Creature Level</strong></td>
            <td style="text-align:center"><strong>Standard XP</strong></td>
            <td style="text-align:center"><strong>PWL XP</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">Party Level -4</td>
            <td style="text-align:center">10</td>
            <td style="text-align:center">18</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -3</td>
            <td style="text-align:center">15</td>
            <td style="text-align:center">21</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -2</td>
            <td style="text-align:center">20</td>
            <td style="text-align:center">26</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -1</td>
            <td style="text-align:center">30</td>
            <td style="text-align:center">32</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level</td>
            <td style="text-align:center">40</td>
            <td style="text-align:center">40</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +1</td>
            <td style="text-align:center">60</td>
            <td style="text-align:center">48</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +2</td>
            <td style="text-align:center">80</td>
            <td style="text-align:center">60</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +3</td>
            <td style="text-align:center">120</td>
            <td style="text-align:center">72</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +4</td>
            <td style="text-align:center">160</td>
            <td style="text-align:center">90</td>
        </tr>
    </tbody>
</table>
</div>

Now, the way attack rolls, saving throws, and damage work in PF 2e is generally very similar to the way they work in D&D 5e. If PF 2e's relative XP values are also derived from those basic mechanics, then the [XP formula]({{ site.data.page-links.xp-and-encounter-balancing.path }}#mjx-eqn-eq:experience-NPC-explicit) I previously derived for D&D 5e should also work as a means of translating between PF 2e's "standard" and PWL XP values. 

Recall, for D&D 5e, I showed a monster's XP can be calculated using the following formula,

\begin{align}
    \XP  &\propto \HP \cdot \DPRhit \cdot 1.077^{\AC + \AB - 16} \,, \label{eq:xp-dnd}
\end{align}

where $$\HP$$ is the creature's average hit points, $$\DPRhit$$ is their average damage assuming all attacks hit, $$\AC$$ is their effective armor class, and $$\AB$$ is their effective attack bonus.

Translating between PF 2e's "standard" and PWL versions, $$\AB \rightarrow \AB - \LV$$ and $$\AC \rightarrow \AC - \LV$$, where $$\LV$$ represents the creature's level. Inserting these into Eqn. \eqref{eq:xp-dnd}, the formula for XP under PWL becomes,

\begin{align}
    \XP_{\mathrm{PWL}}  &\propto \HP \cdot \DPRhit \cdot 1.083^{(\AC - \LV\,) + (\AB - \LV\,) - 16} \nonumber \\\\ 
         &= \HP \cdot \DPRhit \cdot 1.077^{\AC + \AB - 16} \cdot 1.077^{- 2\,\LV} \nonumber \\\\ 
         &= \XP_{\mathrm{S}} \cdot 1.077^{- 2\,\LV} \,, \label{eq:xp-pf-pwl}
\end{align}

where $$\XP_{\mathrm{S}}$$ is the creature's absolute XP value under the "standard" system.

Because Eqn. \eqref{eq:xp-pf-pwl} scales exponentially with the creature's level, it can easily be applied to Pathfinder's relative level system by replacing a creature's level with their relative level, giving us an easy way of translating between the two XP values. A comparison between PF 2e's PWL XP values and those predicted by Eqn. \eqref{eq:xp-pf-pwl} is shown in Fig. <a href="#fig:pf-xp-theory" class="fig-ref">1</a> (below). 

<figure id="fig:pf-xp-theory">
    {% include_relative fig-pf-xp-theory-small.html %}
    {% include_relative fig-pf-xp-theory-large.html %}
    <figcaption>Figure 1: Pathfinder 2nd edition monster XP vs relative level for "Proficiency Without Level" system, along with a theoretical XP values calculated from "standard" proficiency scaling rules.</figcaption>
</figure>

Overall, Eqn. \eqref{eq:xp-pf-pwl} shows excellent agreement with the values provided in the PF 2e rules for PWL. This strongly suggests the encounter building systems for D&D 5e and PF 2e are based on the same fundamental math.

-->


<!--
# Comparing Pathfinder vs D&D

In the last section, I showed how Pathfinder's two XP systems could be translated between using the XP formula I previously derived for D&D 5e. In this section, I expand on this by showing how D&D 5e's XP values can be translated into a relative XP system, effectively reproducing Pathfinder's PWL XP values.

As I mentioned earlier, in order for a relative XP system, like PF 2e's, to work, monster absolute XP values need to scale in a consistent way. For example, the relative XP values used by PF 2e's "Standard" rules double every two levels, which means their absolute XP values should scale like

\begin{align}
    \XP_{\mathrm{S}}  &= \XP_1 \cdot 2^{0.5\,\LV} \,, \label{eq:xp-pf-absolute}
\end{align}

where $$\XP_1$$ is the absolute XP value of a level 1 creature.

Combining Eqns. \eqref{eq:xp-pf-pwl} and \eqref{eq:xp-pf-absolute} gives the absolute XP scaling for PWL,

\begin{align}
    \XP_{\mathrm{PWL}}  &= \XP_1 \cdot 2^{0.5 \, \LV} \cdot 1.077^{- 2\,\LV} \nonumber \\\\ 
    &= \XP_1 \cdot 2^{0.5 \, \LV} \cdot 2^{-0.214 \, \LV} \nonumber \\\\ 
    &= \XP_1 \cdot 2^{0.286 \, \LV} \,, \label{eq:xp-pf-absolute-pwl}
\end{align}

where I used $$1.077 = 2^{0.107}$$ to go from the first to the second line.

The XP values for D&D 5e don't follow such an exact scaling, but an approximate scaling can be calculated by fitting to an exponential of the form

\begin{align}
    \XP_{\mathrm{5e}}  &= 2^{A\,\LV + B} \,. \label{eq:xp-dnd-fit}
\end{align}

Doing so yields values of $$A = 0.288$$ and $$B = 9.089$$. A comparison of this fit and XP values taken from the [Experience Points by Challenge Rating](https://www.dndbeyond.com/sources/basic-rules/monsters#ExperiencePointsbyChallengeRating) table in chapter 12 of the _Basic Rules_ is show in Fig. <a href="#fig:dnd-xp-fit" class="fig-ref">2</a> (below).

<figure id="fig:dnd-xp-fit">
    {% include_relative fig-dnd-xp-fit-small.html %}
    {% include_relative fig-dnd-xp-fit-large.html %}
    <figcaption>Figure 2: Monster XP vs CR for D&D 5e, along with an exponential fit.</figcaption>
</figure>

Careful readers will have already noticed that the level dependent term in this fit, $$A = 0.288$$, is nearly identical to the calculated value of $$0.286$$ for Pathfinder's PWL system! Given the mechanical similarities between these two systems, this result isn't too surprising, but it does give further confidence in the overall approach taken here.

-->




# Conclusion

While different in presentation, the PF 2e and D&D 5e encounter building rules are both built on top of the same fundamental math, and use XP values that are directly tied to the strength of monster offensive and defensive abilities. The PF 2e rules are able to use relative monster XP values and fixed encounter XP thresholds because of the consistent exponential scaling of monster XP. And, the PF 2e rules remove the need for an encounter multiplier to adjust for larger or smaller groups of monsters by centering their math around more monsters per encounter and by scaling a character's chance to land a critical hit with their relative level.

These results add further support for the theoretical approach taken in my previous posts analyzing D&D 5e's encounter building rules, and could be used to repackage those rules into a similar form with relative monster XP and fixed encounter XP thresholds. Without the scaling critical hit rules, though, an encounter multiplier would still be necessary.