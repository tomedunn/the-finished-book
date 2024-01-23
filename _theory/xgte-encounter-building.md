---
title: "Encounter Building in Xanathar's Guide to Everything"
excerpt: "A comparison of the encounter building rules in XGtE and the DMG."
date: 2023-4-18
last_modified_at: 2023-4-19
tags:
  - encounter balancing
  - encounter multiplier
  - theory
  - xp
---

{% include LaTex.html %}

# Introduction

In addition to providing player character (PC) options, such as spells and subclasses, _Xanathar's Guide to Everything_ (_XGtE_) also offers a wide range of rules and systems that DMs can use in their games. One of these is an alternative system for [building and balancing encounters](https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#EncounterBuilding). According to the book, these alternative rules are based on the same math the encounter building rules in the _[Basic Rules](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters)_ are based on,

> This approach uses the same math that underlies the rules presented in \[the _Basic Rules_\], but it makes a few adjustments to the way that math is presented to produce a more flexible system.

Since I've already covered, quite extensively, how the rules for [building combat encounters](https://tomedunn.github.io/the-finished-book/theory/xp-and-encounter-balancing/) in the _Basic Rules_ work, this alternative system presents a unique opportunity to further our understanding of that system.

In this post, I explore the math behind these alternative encounter building rules and compare them to those presented in the _Basic Rules_, first for solo monster encounters and then for encounters with multiple monsters. I've omitted a lot of the specifics from the _XGtE_ rules (though, I do link to them on D&D Beyond), but I cover the math needed to reproduce the tables used by them for anyone who would like to use them but doesn't have access to the book.

# Solo monsters

For encounters with only a single monster, the [Solo Monster Challenge Rating](https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#SoloMonsterChallengeRating) table from _XGtE_ shows what challenge rating (CR) a monster should be to act as a "satisfying but difficult battle" for a group of 4-6 PCs of a given level. 

Building encounters with a single monster against a group of four or more PCs is well within the capabilities of the encounter building rules in the _Basic Rules_. So this section is less an alternative way of building encounters, and more a collection of pre-calculated encounters. What isn't entirely clear, though, is what the _XGtE_ rules mean by a "satisfying but difficult battle".

We can shed some light on this by using the _Basic Rules_ encounter building rules to calculate the difficulty of the solo monster encounters provided in _XGtE_. The results of these calculations is shown in Fig. <a href="#fig:solo-monster-xp-ratios" class="fig-ref">1</a> (below), which puts the calculated XP values for these encounters right around the Hard XP threshold.

<figure id="fig:solo-monster-xp-ratios">
    {% include_relative xgte-encounter-building/fig-solo-monster-xp-ratios-small.html %}
    {% include_relative xgte-encounter-building/fig-solo-monster-xp-ratios-large.html %}
    <figcaption>Figure 1: Plots XP values, relative to half the PC's daily XP budget, for encounters given by the <a href="https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#SoloMonsterChallengeRating">Solo Monster Challenge Rating</a> table in <em>XGtE</em>.</figcaption>
</figure>

For a more challenging encounter, the rules suggest increasing the monster's CR by 1-2. Figure <a href="#fig:solo-monster-xp-ratios-harder" class="fig-ref">2</a> (below) shows the calculated XP value for the case where each monster's CR is 2 higher. For level 3 parties and above, this puts the encounter difficulties close to the Deadly XP threshold, while for levels 1-2 parties, this puts the difficulty well above a Deadly encounter.

<figure id="fig:solo-monster-xp-ratios-harder">
    {% include_relative xgte-encounter-building/fig-solo-monster-xp-ratios-harder-small.html %}
    {% include_relative xgte-encounter-building/fig-solo-monster-xp-ratios-harder-large.html %}
    <figcaption>Figure 2: Plots XP values, relative to half the PC's daily XP budget, for encounters given by the <a href="https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#SoloMonsterChallengeRating">Solo Monster Challenge Rating</a> table in <em>XGtE</em> where the CR for each monster is 2 higher than its listed value.</figcaption>
</figure>

For easier encounters, the rules suggest decreasing the monster's CR by 3 or more. Figure <a href="#fig:solo-monster-xp-ratios-easier" class="fig-ref">3</a> (below) shows the calculated XP value for the case where each monster's CR is 3 lower than the listed value. For levels 6-20, the calculated XP closely follows the Medium difficulty XP threshold. While for parties level 1-5 this will give encounters close to the Easy XP threshold or below.

<figure id="fig:solo-monster-xp-ratios-easier">
    {% include_relative xgte-encounter-building/fig-solo-monster-xp-ratios-easier-small.html %}
    {% include_relative xgte-encounter-building/fig-solo-monster-xp-ratios-easier-large.html %}
    <figcaption>Figure 3: Plots XP values, relative to half the PC's daily XP budget, for encounters given by the <a href="https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#SoloMonsterChallengeRating">Solo Monster Challenge Rating</a> table in <em>XGtE</em> where the CR for each monster is 3 lower than its listed value.</figcaption>
</figure>

These rules should work well for building solo monster encounters that fall into the Medium, Hard, or Deadly difficulty categories. Though, they appear to work best when the PCs are level 6 or higher. Of course, it's worth pointing out that these rules were designed to work with legendary monsters, and there aren't that many at low CRs, making it hard to build solo monster encounters below 6th level without building your own monsters. 

In principle, a legendary monster and a non-legendary one of the same CR are equally dangerous. So these rules can be extended to non-legendary monsters. However, legendary monsters often have their damage spread out over a larger number of attacks, which makes them more predictable, and less likely to unexpectedly kill a PC in a single hit.

# Multiple monsters

Much like the rules for solo monsters, the multiple monster rules also rely on tables for building encounters. However, rather than presenting pre-made encounters, like the solo monster rules do, these [tables](https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#MultipleMonsters1st5thLevel) show how many monsters of a certain CR are needed to balance out one PC at a specific level. Setting aside the ambiguity of what it means to "balance out" a PC, these rules allow a DM to construct encounters by converting each of their PCs into a group of monsters.

Naively, we might try to convert a PC into an equivalent group of monsters by dividing one of the PC's difficulty XP thresholds $$(\XP_{\thresh})$$ by the XP value of the monsters being used $$(\XP_{\NPC})$$,
\begin{equation}
    N_{\NPC} = \frac{\XP_{\thresh}}{\XP_{\NPC}} \,,
    \label{eq:n-npcs-wrong}
\end{equation}
but this won't give the correct result, and won't match the conversions given in _XGtE_. This is because of how monster XP values and the encounter multiplier were defined for the encounter building rules in the _Basic Rules_.

In order for the encounter multiplier $$(\EM\,)$$ to have a value of 1 for encounters with a single monster against a party of four PCs, monster XP values had to be reduced by a factor of 4. This is why the equation for monster XP derived in [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}),
\begin{equation}
    \label{eq:XP-simple}
    \XP_{\NPC} = \frac{1}{4} \eHP \cdot \eDPR\,,
\end{equation}
includes a factor of $$1/4$$ in it, while the XP equation for PCs does not. This choice effectively centers math for building encounters used by the _Basic Rules_ around "monsters per group", rather than "monsters per PC".

We can re-center the _Basic Rules_ encounter building math around "monsters per PC" by adjusting the $$\EM\,$$ such that it gives a value of 1 when there is one monster per PC, rather than one monster per group of four PCs. Since $$\EM = 2$$ for a group of four monsters against a party of four PCs, this can be accomplished using the following substitutions: 
\begin{gather}
    \XP_{\NPC} \rightarrow 2\,\XP_{\NPC} \,; \\\\ 
    \EM \rightarrow \frac{1}{2}\,\EM \,.
\end{gather}

Applying these substitutions, the equation for converting a PC into a group of equivalent monsters becomes,
\begin{equation}
    N_{\NPC} = \frac{\XP_{\thresh}}{2\,\XP_{\NPC}} \,.
    \label{eq:n-npcs}
\end{equation}
While the rules don't explicitly say what difficulty they are built around (i.e., what value of $$\XP_{\thresh}$$ to use), given the results of the previous section, the Hard XP threshold $$(\XP_{\mathrm{Hard}})$$ seems like a natural choice.

To test this, Fig. <a href="#fig:multi-monster-ratios" class="fig-ref">4</a> (below) compares the monster conversion ratios calculated from Eqn. \eqref{eq:n-npcs}, where $$\XP_{\thresh} = \XP_{\mathrm{Hard}}$$, with the values given in _XGtE_. The results follow the expected trend, and rounding to the nearest whole number ratio reproduces the tables in _XGtE_ almost exactly. This confirms that that multiple monster encounter building rules in _XGtE_ are also built around creating Hard encounters.

<figure id="fig:multi-monster-ratios">
    {% include_relative xgte-encounter-building/fig-multi-monster-ratios-small.html %}
    {% include_relative xgte-encounter-building/fig-multi-monster-ratios-large.html %}
    <figcaption>Figure 4: Plots monster conversion ratios given by Eqn. \eqref{eq:n-npcs} with \(\XP_{\thresh} = \XP_{\mathrm{Hard}}\) against values given in the <a href="https://www.dndbeyond.com/sources/xgte/dungeon-masters-tools#MultipleMonsters1st5thLevel">Multiple Monsters</a> tables in <em>XGtE</em>. A ratio of 1:5 indicates 1 PC is balanced by 5 monsters, and a ratio of 2:1 indicates 2 PCs are balanced by 1 monster.</figcaption>
</figure>

The multiple monster encounter building rules also include guidelines for building encounters that are easier or harder than this default Hard difficulty. For easier encounters, they recommend treating the party as $$1/3$$ smaller, and for harder encounters treating the party as $$50\%$$ larger. This are fitting adjustments because, as Fig. <a href="#fig:xp-threshold-ratios" class="fig-ref">5</a> shows (below) the Medium XP threshold is generally $$1/3$$ smaller than the Hard XP threshold, and the Deadly XP threshold is generally $$50\%$$ higher than the Hard XP threshold. Meaning, these adjustments are designed to create Medium and Deadly encounters respectively.

<figure id="fig:xp-threshold-ratios">
    {% include_relative xgte-encounter-building/fig-xp-threshold-ratios-small.html %}
    {% include_relative xgte-encounter-building/fig-xp-threshold-ratios-large.html %}
    <figcaption>Figure 5: Plots PC XP thresholds, relative to the Hard XP threshold, as a function of PC level.</figcaption>
</figure>

# Encounter multiplier

Before closing, I think it's worth discussing how the _XGtE_ encounter building rules are able to function without using an $$\EM\,$$. The rules for solo monsters clearly don't need it, but the rules for encounter with multiple monsters still should, since they, by definition, involve encounters with more than one monster.

From a theoretical perspective, they could have factored it into the conversion ratios listed in the various multiple monster tables, but as the results in Fig. <a href="#fig:multi-monster-ratios" class="fig-ref">4</a> show, this is clearly not the case. So, why isn't it there?

To understand how the multiple monster rules in _XGtE_ get away with not including an $$\EM\,$$, lets look at how our re-centered $$\EM\,$$ compares to the one from the _Basic Rules_. As shown in Fig. <a href="fig:encounter-multiplier" class="fig-ref">6</a> (below), rescaling the $$\EM\,$$ to be centered around one monster per PC also flattens it's overall value across a wide range of encounter sizes.

<figure id="fig:encounter-multiplier">
    {% include_relative xgte-encounter-building/fig-encounter-multiplier-small.html %}
    {% include_relative xgte-encounter-building/fig-encounter-multiplier-large.html %}
    <figcaption>Figure 6: Plots the encounter multiplier as a function of the number of monsters in an encounter for systems centered around "monsters per group" and "monsters per PC".</figcaption>
</figure>

For encounters with 2-10 monsters, the maximum error in encounter $$\XP$$ incurred by ommiting the new $$\EM\,$$ is only $$25\%$$, which is considerably smaller than the maximum error of $$60\%$$ incurred for ignoring the $$\EM$$ when building encounters in the _Basic Rules_. 

To put these values in perspective, recall from Fig. <a href="#fig:xp-threshold-ratios" class="fig-ref">5</a> that the Deadly XP threshold is typically  $$50\%$$ higher than the Hard XP threshold. So, while ignoring the $$\EM\,$$ in the _Basic Rules_ encounter building rules can potentially misjudge an encounter's difficulty by a full category, this is unlikely to be the case using the rules in _XGtE_.

# Conclusion

To conclude, the alternative encounter building rules presented in _XGtE_ are indeed based on the same math used in the _Basic Rules_. The tables for building solo monster encounters and multiple monster encounters are both aimed at producing encounters right at the Hard XP threshold, and the guidance for creating easier or more challenging encounters are aimed at the Medium and Deadly encounter XP thresholds respectively. 

The ability for these rules to operate without an encounter multiplier rests in how they re-center the math around one monster per PC, rather than one monster per party of four, which reduces the overall impact of the encounter multiplier over a wide range of encounter sizes. Removing the encounter multiplier also remove the potential for DMs, as well as online encounter calculators, to apply it incorrect; an extremely common problem in my experience.

Given that both are based on the same underlying math, these two systems for building encounters should give very similar results. Which means, whether or not the _XGtE_ rules work better than those in the _Basic Rules_ will mostly depend on what system you prefer to work with. 