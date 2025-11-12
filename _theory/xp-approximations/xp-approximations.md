---
title: "XP Approximations"
excerpt: "Approximations simplify XP calculations but that comes at the cost of accuracy. How much are we paying?"
permalink: /:collection/:name/
date: 2025-11-12
last_modified_at: 2025-11-12
tags:
  - encounter balancing
  - theory
  - xp
---

{% include LaTex.html %}

<div style="display:none">
\(
\newcommand{\total}{\mathrm{tot}}
\newcommand{\level}{\mathit{Level}}
\newcommand{\D}{\mathit{D}}
\newcommand{\d}{\mathit{d}}

% accuracy
\newcommand{\accuracy}{A}
\)
</div>

# Introduction

In my previous posts on [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}) I showed how XP values can be calculated for monsters and for player characters. The linear approximation to that equation showed excellent agreement with monster XP values in 5th edition D&D (5e) when using the baseline monster stats from chapter 9 of the 2014 _Dungeon Master's Guide_, but when using stats from [actual monsters]({{ site.data.page-links.calculating-monster-xp.path }}) it tended to produce lower than expected XP values at low CRs and higher than expected values at high CRs.

As it turns out, the reason for this discrepancy is that published monsters and the baseline monsters in the 2014 DMG follow different XP formula. Specifically, they have different sensitivities to armor class $$(\AC\,)$$ and attack bonus $$(\AB\,).$$ This can be seen clearly in Fig. \figref{fig:npc-accuracy-vs-acab} (below) which plots monster $$\XP$$ values, normalized to their average hit points $$(\HP\,)$$ and damage per round $$(\DPR\,),$$ against the sum $$\AC + \AB.$$ Since $$\XP \propto \HP \cdot \DPR$$ this allows us to isolate and view the dependence of $$\XP$$ on $$\AC$$ and $$\AB$$ directly.

<figure id="fig:npc-accuracy-vs-acab">
    {% include_relative fig-npc-accuracy-vs-acab-small.html %}
    {% include_relative fig-npc-accuracy-vs-acab-large.html %}
    <figcaption>Plots monster XP values, normalized to their adjusted total hit points and unmitigated damage per round, against the sum of their adjusted armor class and adjusted attack bonus.</figcaption>
</figure>

**Note.** For a summary of the monsters used in this analysis, see [Monster Dataset]({{ site.data.page-links.monster-dataset.path }}).
{: .notice--warning}

While the $$\XP$$ values for the baseline monsters described in the 2014 DMG are clearly linearly depended on $$\AC + \AB,$$ for published monsters the dependence is split. Published monsters above CR 20 show the same linear dependence on $$\AC + \AB$$ as the 2014 DMG baseline monsters, while the dependence for monsters CR 20 and below is essentially flat (i.e., their XP values have no $$\AC + \AB$$ dependence).

In terms of the $$\XP$$ equation derived in [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}), published monsters above CR 20 follow a 1st order (i.e., linear) approximation with respect to $$\AC + \AB,$$ while monsters CR 20 and blow follow a 0th order approximation with respect to $$\AC + \AB.$$

<!--
\begin{eqnarray}
    \XP_{\NPC}  \simeq \frac{1}{4}\HP \cdot \DPRhit
        \begin{cases} 
            \frac{ 30 }{ 13 }            &, & \CR \leq 20 \,, \\\\ 
            \frac{ \AC + \AB - 2 }{ 13 } &, & 20  \lt  \CR \,, 
        \end{cases}
\end{eqnarray}
-->

This flat dependence on $$\AC + \AB$$ can also be observed for PCs by applying a similar technique to the various encounter difficulty XP thresholds found in the [encounter building rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/building-combat-encounters#XPThresholdsbyCharacterLevel) from chapter 3 of the 2014 DMG, along with stats taken from my previous post [Baseline PC Stats]({{ site.data.page-links.baseline-player-character-stats.path }}).

<figure id="fig:pc-accuracy-vs-acab">
    {% include_relative fig-pc-accuracy-vs-acab-small.html %}
    {% include_relative fig-pc-accuracy-vs-acab-large.html %}
    <figcaption>Plots player character XP thresholds from chapter 3 of the 2014 DMG, normalized to their adjusted total hit points and unmitigated damage per round, against the sum of their adjusted armor class and adjusted attack bonus. Player character stats were taken from <a href="{{ site.data.page-links.baseline-player-character-stats.path }}">Baseline PC Stats</a>.</figcaption>
</figure>

In order to understand the impact these results have on the game, in this post I look at how different approximations to the $$\XP$$ equation affect the accuracy of D&D's encounter building rules.

# Measuring XP accuracy

In order to assess the accuracy different XP calculation we need a way of comparing their predicted difficulties against the corresponding actual difficulties produced from actual combat encounters. In [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}) the XP equation was derived from efforts to calculate how much total damage the enemy NPCs would deal to the PCs during a combat encounter on average $$(\D_{\NPCs}^{\,\total})$$ relative to the PCs' total hit points $$(\HP_{\PCs}^{\,\total}),$$
\begin{align}
    \d \equiv \frac{ \D_{\NPCs}^{\,\total} }{ \HP_{\PCs}^{\,\total} } \,. 
    \label{eq:difficulty-definition}
\end{align}

If we follow through on this calculation for an encounter with a single monster and four identical PCs without invoking XP this becomes
\begin{align}
    \d &= 
        \frac{ 1 }{ 16 } \frac{ \HP_{\NPCs} \, \DPR_{\NPCs} }{ \HP_{\PCs} \, \DPR_{\PCs} }
        \frac{ P \left( \AB_{\NPCs}, \AC_{\PCs} \right) }{ P \left( \AB_{\PCs}, \AC_{\NPCs} \right) } \,,
    \label{eq:difficulty-actual}
\end{align}
where  
\begin{align}
    P &= \frac{ \max \left( 1, \min \left(19,  21 + \AC_{j} - \AB_{i} \right) \right) }{ 20 }
    \label{eq:hit-crit-probability}
\end{align}
is the probability of an attack from character $$i$$ with attack bonus $$\AB_{i}$$ dealing damage to character $$j$$ with armor class $$\AC_{j}.$$

**Note.** For simplicity, this formulation assumes critical hits deal the same damage as hits and that none of the PCs die early.
{: .notice--warning}

In terms of $$\XP$$, Eqn. \eqref{eq:difficulty-definition} takes the form
\begin{align}
    \d_{\XP} = \frac{ \XP_{\NPCs} }{ 4 \XP_{\PCs} }\,. 
    \label{eq:difficulty-xp}
\end{align}
Normally this would also include the encounter XP multiplier $$\EM$$ in the numerator, but for encounters with a single monster and a party of four identical PCs $$\EM = 1.$$

Expanding out $$\XP_{\NPCs}$$ and $$\XP_{\PCs}$$, Eqn. \eqref{eq:difficulty-xp} becomes
\begin{align}
    \d_{\XP} &= 
        \frac{ 1 }{ 16 } \frac{ \HP_{\NPCs} \, \DPR_{\NPCs} }{ \HP_{\PCs} \, \DPR_{\PCs} }
        \frac{ F \left( \AB_{\NPCs}, \AC_{\NPCs} \right) }{ F \left( \AB_{\PCs}, \AC_{\PCs} \right) } \,,
    \label{eq:difficulty-xp-full}
\end{align}
where $$F$$ encapsulates the sensitivity of the $$\XP$$ equation to a character's $$\AC$$ and $$\AB.$$ Note that $$F$$ uses the stats from only one creature, while $$P$$ in Eqn. \eqref{eq:difficulty-actual} takes $$\AC$$ and $$\AB$$ from different characters.

If we think of Eqn. \eqref{eq:difficulty-actual} as the actual average damage the PCs will take during an encounter,s and Eqn. \eqref{eq:difficulty-xp-full} as the predicted average damage, then the ratio between the two,
\begin{align}
    \accuracy \equiv \frac{ \d_{\XP} }{ \d }\,, 
    \label{eq:accuracy-xp}
\end{align}
serves as a natural measure of how accurate our $$\XP$$ calculation is as a tool for building encounters. Under this definition when $$\accuracy > 1$$ the $$\XP$$ equation overestimate the damage the PCs will take, and when $$\accuracy < 1$$ it underestimates it.

Plugging Eqns. \eqref{eq:difficulty-actual} and \eqref{eq:difficulty-xp-full} into Eqn. \eqref{eq:accuracy-xp} the $$\HP$$ and $$\DPR$$ terms cancel out and we're left with 
\begin{align}
    \accuracy \equiv 
        \left[ \frac{ F \left( \AB_{\NPCs}, \AC_{\NPCs} \right) }{ F \left( \AB_{\PCs}, \AC_{\PCs} \right) } \right] / 
        \left[ \frac{ P \left( \AB_{\NPCs}, \AC_{\PCs} \right) }{ P \left( \AB_{\PCs}, \AC_{\NPCs} \right) } \right] \,. 
    \label{eq:accuracy-xp-full}
\end{align}

<!--

\begin{align}
    F_{e} &= 1.077^{\AC + \AB - 15} \\\\ 
    F_{0} &= 1 \\\\ 
    F_{1} &= \left( \frac{\AC + \AB - 2}{13} \right)
\end{align}
-->




# Analysis

With the math out of the way, lets look at how different XP approximations perform. To start, Fig. \figref{fig:xp-accuracy-vs-cr-matched} (below) shows the accuracy, calculated using Eqn. \eqref{eq:accuracy-xp-full}, of three different XP approximations when a single monster is pitted against a party of four PCs with levels equal to the monster's CR, or, in the case of monsters with $$\CR > 20,$$ against a party of four level 20 PCs.

<figure id="fig:xp-accuracy-vs-cr-matched">
    {% include_relative fig-xp-accuracy-vs-cr-matched-small.html %}
    {% include_relative fig-xp-accuracy-vs-cr-matched-large.html %}
    <figcaption>Plots the accuracy ratio for encounters with a party of four PCs against a single monster. The party's level equals the monster's CR for CRs less than 20, and the party's level equals 20 for monster CRs 20 and above.</figcaption>
</figure>

Of the three $$\XP$$ approximations, the exponential form of the XP equation, for which
\begin{align}
    F_{e} = 1.077^{\AC + \AB - 15}\,, \label{eq:f-exponential}
\end{align}
is clearly the most accurate, with $$\accuracy \simeq 1$$  across the full range of CRs. 

For the remaining two the overall accuracy is lower and similar to one another, with the linear $$\XP$$ approximation,
\begin{align}
    F_{1} &= \left( \frac{\AC + \AB - 2}{13} \right) \,, \label{eq:f-linear}
\end{align}
being only slightly more accurate than the values for published monsters, which has no explicit formula but whose sensitivity can be see in Fig. \figref{fig:npc-accuracy-vs-acab}. In addition to having $$\accuracy$$ slightly below $$1$$ for monster CR 15 and lower, both also tend to underestimate monster difficulties by similar amounts at higher CRs. 

The similar accuracies between these two at lower CRs can be explained by monsters and PCs have relatively fixed chances to hit each other at around $$65\%$$ for $$CR \lt 20$$. And at higher CRs both follow the same linear dependence on $$\AC + \AB$$ as shown earlier in Fig. \figref{fig:npc-accuracy-vs-acab}.

The reason both shift towards underestimating encounter difficulties has to do with how the linear approximation to $$\XP$$ tends to undervalue differences in $$\AC$$ and $$\AB$$ as the total value of $$\AC + \AB$$ increases. Increasing either $$\AB$$ or $$\AC$$ by $$+1$$ in Eqn. \eqref{eq:f-linear} produces a smaller relative change in $$F_{1}$$ when $$\AC + \AB$$ is large than when $$\AC + \AB$$ is small. 

For example, when $$\AC + \AB = 15$$ a $$+1$$ to either stat increases $$F_{1}$$ from $$1$$ to $$1.077$$ for a $$7.7\%$$ increase, while a $$+1$$ increase when $$\AC + \AB = 28$$ increases $$F_{1}$$ from $$2$$ to $$2.077$$ for only a $$3.3\%$$ increase. Since $$\AC + \AB$$ tends to increase as monster CR and PC level increase, this causes difference in $$\AC$$ and $$\AB$$ to show up as less significant at higher levels of play.

Moving on to the more general case, Fig. \figref{fig:xp-accuracy-vs-relative-cr} (below) shows $$\accuracy$$ for every combination of monster CR and party level, using the same $$\XP$$ approximations shown previously in Fig. \figref{fig:xp-accuracy-vs-cr-matched}. Presenting the data in this way works, in large part, because $$\AC$$ and $$\AB$$ generally increase linearly with monster CR and PC level.

<figure id="fig:xp-accuracy-vs-relative-cr">
    {% include_relative fig-xp-accuracy-vs-relative-cr-small.html %}
    {% include_relative fig-xp-accuracy-vs-relative-cr-large.html %}
    <figcaption>Plots the accuracy ratio for encounters with a party of four PCs against a single monster as a function the monster's relative challenge rating.</figcaption>
</figure>

Once again, the exponential $$\XP$$ equation performs the best out of the three, with the average $$\accuracy$$ keeping within $$10\%$$ of target for CR within $$\pm 15$$ of the party's level. Even if we look beyond the average, at the individual points, this range only shrinks to CR with the range $$[-13,8]$$ of the party's level, which is still quite large.

The difference in $$\accuracy$$ between the linear $$\XP$$ approximation and official 5e XP values is also much more apparent in Fig. \figref{fig:xp-accuracy-vs-relative-cr}. For the later, the average $$\accuracy$$ stays within $$10\%$$ of target for only a narrow range of CR within $$[-2, 1]$$ of the party's level, with the former doing only a bit better with a range of $$[-4,2].$$ For official 5e XP values the $$\accuracy$$ is especially poor at low relative CR, i.e., when the monsters have CRs that are significantly below the party's level.

# Discussion

Before concluding, I think it's worth discussing these results within a broader context. Because the poor accuracy produced by the official 5e XP values isn't likely as bad as it might appear at first glance. The key takeaway from the previous section is that the official 5e XP values underestimate the difficulty of individual monsters with CR above the party's level and overestimate it when they have CR below the party's level. If we think about this in the context of encounter building, an interesting connection appears.

When building an encounter monsters are added until their adjusted XP total falls within a certain range, as defined by the encounter's intended difficulty. We get this adjusted XP total by multiplying the total XP of the monsters by the encounter multiplier, $$\EM,$$ which depends on the number of monsters. Encounters with more monsters have higher $$\EM$$ values than those with fewer.

Since an encounter with lower CR monsters can contain more monsters than one made up of higher CR monsters, groups of lower CR monsters end up getting treated being more dangerous than their individual stats would suggest. In other words, it produces a qualitatively similar shift in the predicted difficulty to what was observed in the previous section for official 5e XP values.

We can compare the sizes of these two effects quantitatively by constructing an effective multiplier created by the official 5e XP values and comparing it against the $$\EM$$ in the 2014 DMG. To do this, we can construct combat encounters in the typical way using just the monster XP values (i.e., no multiplier) to determine the number of monsters for a given $$\CR$$ and difficulty, and then use the $$\accuracy$$ for those monsters, calculated from Eqn. \eqref{eq:accuracy-xp}, for the effective $$\EM.$$ The results of this process are shown in Fig. \figref{fig:effective-xp-multiplier} (below) for several difficulty thresholds.

<figure id="fig:effective-xp-multiplier">
    {% include_relative fig-effective-xp-multiplier-small.html %}
    {% include_relative fig-effective-xp-multiplier-large.html %}
    <figcaption>Plots the effective encounter XP multiplier from official 5e XP values for Easy (blue), Medium (orange), Hard (green), and Deadly (red) encounter difficulty XP thresholds. Also shows the encounter XP multiplier from chapter 3 of the DMG (black).</figcaption>
</figure>

While the effect isn't as strong as the $$\EM$$ in chapter 3 of the DMG, it's not negligible. In fact, if the $$\EM$$ in the 2014 DMG were an overestimate for how much the difficulty of an encounter increases with the number of monsters then this effect could potentially be strong enough to offset the need for the $$\EM$$ altogether.

Of course, this wouldn't be a perfect solution. As Fig. \figref{fig:effective-xp-multiplier} shows, the size of this effective $$\EM$$ gets smaller as the encounter difficulty increases. This is caused by two effects: a general increase in the number of monsters per encounter due to larger $$\XP$$ thresholds, shifting the curve to the right, and encounters with lower numbers of monsters tending to have higher CRs monsters for which this effect is weaker, shifting the curve down. If this effect were enough to remove the need for the $$\EM$$ at lower encounter difficulties, the encounter building rules would still tend to underestimate the actual difficulty for higher encounter difficulty targets.

# Conclusion

To summarize, the results presented here help answer two key questions that have lingered on my mind for some time now regarding the encounter building rules in 5e and my research on them.

First, why did my XP formula worked so well for the baseline monsters in the 2014 DMG while consistently giving low values for low CR published monsters? I had always assumed the answer had to do with designers having a bias towards weaker monsters at low CR, but this analysis shows that hasn't been the case. Instead, its because the XP formula used for published monsters is simply different from the one used when generating the baseline monsters in the 2014 DMG. And that difference happens to be most pronounced for low CR monsters, and leads to them having high XP values than they would based on the monster creation rules in the 2014 DMG.

Second, why did the 2024 encounter building rules do away with the encounter XP multiplier? There are still a few angle left to consider in regard to how PCs have change in power under the 2024 rules update for 5e, so I wouldn't consider this point closed completely. But these results are compelling, and strongly suggest that the 2024 encounter building rules are able to go without the encounter XP multiplier because one was already baked into the game's XP values, knowingly or unknowingly.

My analysis of the [Pathfinder 2]({{ site.data.page-links.xp-dnd-vs-pathfinder.path }}) encounter building rules showed something similar. However, for those rules the offset appeared to a fixed percent scaling difference, which would produce a more uniform and predictable shift at each level of play. Applied to 5e, this would be like using the exponential XP formula but with a smaller exponential base (e.g., instead of $$1.077$$ a smaller value like $$1.06$$ could be used instead).