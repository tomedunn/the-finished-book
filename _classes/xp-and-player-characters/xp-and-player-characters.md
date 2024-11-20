---
title: "Player Character XP"
excerpt: "Calculates encounter and adventuring day XPs for each class and compares them with XP thresholds and budgets in the DMG."
#excerpt: "Have you ever wondered where the adventuring day XP budget values come from? In this post I discuss how XP values can be calculated for each of the classes in the PH, and show how those values stack up against the encounter difficulty XP thresholds and adventuring day XP budgets given in the DMG."
permalink: /:collection/:name/
date: 2022-09-03
last_modified_at: 2023-05-06
tags:
  - analysis
  - adventuring day
  - classes
  - encounter balancing
  - xp
---

{% include LaTex.html %}

# Introduction

In my previous post, [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}), I showed how PC XP thresholds and NPC XP values could be derived from fundamental equations for combat. And, while I did go into detail [here]({{ site.data.page-links.calculating-monster-xp.path }}) showing how monster XP values compared with those listed for published monsters, I never really addressed XP thresholds for PCs in a similar way.

In this post, I'd like to rectify this, by calculating XP values for each of the PC classes and showing how they relate to the different encounter difficulty XP thresholds, as well as the adventuring day XP budgets from [chapter 13](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters) of the _Basic Rules_.


# Calculating player character XP

As I covered in [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}), XP values can be calculated for player characters, similarly to how they're calculated for non-player characters, by taking the product of a PC's effective hit points $$(\eHP\,)$$ and average effective damage per round $$(\eDPR\,)$$, 

\begin{equation}
    \XP_{\PC} = \eHP \cdot \eDPR\,.
    \label{eq:XP-simple}
\end{equation}

The specifics of how $$\eHP$$ and $$\eDPR$$ are calculated are covered in [Effective HP and Damage]({{ site.data.page-links.effective-hp-and-damage.path }}), but for a simple approximation Eqn. \eqref{eq:XP-simple} can be written as,

\begin{equation}
    %\XP_{\PC} = \HP \cdot \DPRhit \left(1 + 0.077\left(\AC + \AB - 15\right)\right)\,, 
    \XP_{\PC} = \HP \cdot \DPRhit \left( \frac{\AC + \AB - 2}{13} \right)\,,
    \label{eq:XP-full}
\end{equation}

where $$\HP$$ is the PC's average hit points, $$\AC\,$$ is their effective armor class, $$\DPRhit$$ is their average damage per round assuming all attacks hit, and $$\AB\,$$ is their effective attack bonus.

Since, as I show [here]({{ site.data.page-links.encounter-multiplier-p1.path }}), the encounter multiplier already factors in the PC's ability to deal damage to multiple targets at once via area of effect abilities, $$\DPRhit$$ should only reflect a PC's single target damaging abilities in order to avoid double counting.
 
For NPCs, XP was calculated for a single three round encounter with the NPC fully rested at the start of it. This fit well with how NPCs typically experience combat, but the same can't be said for PCs. PCs often face several encounters before resting, and the number of rounds can vary significantly, depending on a variaty of factors.

Over the course of multiple encounters, the resources available to each PC for healing, damage, or other combat effects change. The values used to calculate Eqn. \eqref{eq:XP-full} also change as a result, which means a PCs encounter XP will vary from one encounter to the next. The consequences of this is that a PC's XP value can be defined in a number of ways: it can be defined for a single encounter, as an average across multiple encounters, and for a full adventuring day. In terms of how XP is used for balancing encounters, the second and third of these are generally the most important.


## Encounter XP

When calculating XP for a single encounter using Eqn. \eqref{eq:XP-full}, effects that modify a PC's $$\AC\,$$ and $$\AB\,$$, such as the barbarian's [Reckless Attack](https://www.dndbeyond.com/classes/barbarian#RecklessAttack-53) feature, need to be averaged across the number of rounds, as does the PC's $$\DPRhit$$. However, effects that contribute to a PC's hit points, such as the fighter's [Second Wind](https://www.dndbeyond.com/classes/fighter#SecondWind-192) feature, need to be added together instead.

In mathematical terms, these can be expressed using the following equations,

\begin{align}
    \AC &= \AC_{\,\mathrm{base}} + \frac{1}{N_\mathrm{rounds}}\sum_{i = 1}^{N_\mathrm{rounds}} \Delta \AC_{\,i} \,; \label{eq:AC-encounter} \\\\ 
    \AB &= \AB_{\,\mathrm{base}} + \frac{1}{N_\mathrm{rounds}}\sum_{i = 1}^{N_\mathrm{rounds}} \Delta \AB_{\,i} \,; \label{eq:AB-encounter} \\\\ 
    \DPRhit &= \frac{1}{N_\mathrm{rounds}}\sum_{i = 1}^{N_\mathrm{rounds}} \DPRhit^{\,i} \,; \label{eq:DPR-encounter} \\\\ 
    \HP &= \HP_{\mathrm{max}} + \sum_{i = 1}^{N_\mathrm{rounds}} \Delta \HP_{\,i} \,. \label{eq:HP-encounter}
\end{align}

Here, $$\AC_{\,\mathrm{base}}$$ is the PC's base armor class and $$\Delta \AC\,$$ is the bonus applied to the PC's armor class during a round of combat, $$\AB_{\,\mathrm{base}}$$ is their base attack bonus and $$\Delta \AB\,$$ is the bonus applied to their attack bonus during a round of combat, $$\HP_{\mathrm{max}}$$ is their hit points at full health and $$\Delta \HP$$ is the healing or temporary hit points they receive during a round of combat, and $$N_\mathrm{rounds}$$ is the number of rounds in the encounter.

The number of rounds in an encounter can vary quite a bit for PCs, but we can simplify this a bit by focusing on the typical number of rounds for each encounter difficulty. This approach is also convenient when calculating PC XP values for full adventuring days, since the number of encounters also depends on the average encounter difficulty. I cover how to calculate the number of rounds per encounter, as well as the number of rounds per full adventuring day, for each encounter difficulty [here]({{ site.data.page-links.rounds-per-day.path }}).


## Adventuring day XP

Across a full adventuring day Eqns. \eqref{eq:AC-encounter} - \eqref{eq:DPR-encounter} can also be used to calculate $$\AC\,$$, $$\AB\,$$, and $$\DPRhit$$, but with $$N_\mathrm{rounds}$$ being the number of rounds in the adventuring day, rather than a single encounter. For calculating $$\HP$$, Eqn. \eqref{eq:HP-encounter} must be modified to also include any healing done outside of combat, such as hit points recovered from hit dice during a short rest. This can be expressed mathematically as

\begin{equation}
    \HP = \HP_{\mathrm{max}} + \LV \left( \HD + \CON\right) + \sum_{i = 1}^{N_\mathrm{rounds}} \Delta \HP_{\,i} \,, 
    \label{eq:HP-daily}
\end{equation}

where $$\LV$$ is the PC's level, $$\HD$$ is the average value for their hit die, and $$\CON$$ is their Constitution modifier.

For most PCs, their maximum hit points and the hit points restored by their hit dice during short rests account for nearly all of the RHS of Eqn. \eqref{eq:HP-daily}. These two contributions are also roughly equal to each other, which means we should expect a PC's average encounter XP for a full adventuring day to be roughly half of their daily XP budget under the same conditions.

Right away, this has some interesting implications for what the various encounter difficulty thresholds are and how they are calculated. In [XP and Encounter Balancing](https://tomedunn.github.io/the-finished-book/theory/xp-and-encounter-balancing/#fig:pc-xp-thresholds-vs-level) I plotted these XP thresholds as ratios of the Easy encounter difficulty threshold, but as Fig. \figref{fig:encounter-xp-thresholds-vs-level} shows (below), they also show up as set percentages of a PC's encounter XP budget (i.e., half their adventuring day budget).

<figure id="fig:encounter-xp-thresholds-vs-level">
    {% include_relative fig-encounter-xp-thresholds-vs-level-large.html %}
    {% include_relative fig-encounter-xp-thresholds-vs-level-small.html %}
    <figcaption>PC encounter XP thresholds normalized to half their adventuring day XP budget (solid lines) and average normalized values (dashed lines).</figcaption>
</figure>

When measured in this way the Easy encounter XP threshold is roughly 15% of a PC's encounter XP budget, the Medium threshold is roughly 30%, the Hard threshold is roughly 45%, and the Deadly threshold is roughly 70%.


# Results

With the mathematical descriptions out of the way, let's see how the calculated values compare to the XP values for PCs given in the encounter balancing rules from chapter 13 of the _Basic Rules_. 

Before doing so, though, there are a few additional nuances to the calculation that I need to cover which I used to simplify the calculations and make them more manageable. For anyone wanting to jump straight to the results, the following links will take you to the results for the [average XP](#average-calculated-xp) and the [class breakdown](#calculated-xp-by-class).

## Simplifications

For NPCs, the strategies that produce a creature's optimal encounter XP are relatively easy to determine because of their limited number of abilities, as well as only having to look at three rounds of combat in total. For PCs the picture is quite a bit more complex.

Rather than looking for optimal strategies by hand, I built a solver that goes through the different ability combinations for each round in an encounter to find it form me. This works well for martial characters, who typically only have a limited number of options to pick from. However, for spellcaster the sheer number of options available each round makes the task practically impossible in a reasonable amount of time. This is especially true when dealing with longer encounters.

In order to reduce the number of options available to spellcasters, I chose to replace specific spell lists with spell damage templates instead. These spell damage templates were built from the values listed in the [Spell Damage](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#SpellDamageTable) table from chapter 9 of the DMG. Each was assumed to damage only a single target via an attack roll, and have a casting time of one action. For paladins and rangers, bonus action spell templates were also used, and for sorcerers and wizards, reaction spells that increased AC were included as well.

This makes the calculation manageable, but also it washes away important differences between each class's spell list, as well as differences in the strengths of individual spells at a given spell level. So, rather than measuring how much single target damage each spellcaster is capable of, this approach can be though of as measuring how the game _budgets_ single target damage for each spellcaster instead.

The choice of subclasses and feats posed similar problems. I hope to tackle subclasses more directly in future posts, and possibly through updates to this one, but for now I've chosen to ignore them and focus only on base classes when calculating each class's XP values. Similarly, I've chosen to ignored feats when calculating each class's XP values, focusing on ability score improvements as each class levels up instead.

While the loss of feats _should_ be neutral in terms of how the game budgets each class, the same can't be said of excluding subclasses. This means the results presented here underestimates how much XP each class is worth. How much it underestimates it won't be clear until I add subclasses back in, but I think a safe estimate would be around 10%. 

The last simplification I'd like to mention here is that, whenever possible, I chose to avoid assigning values to conditions when damage or healing alternative were present. The only class especially affected by this was the monk, which could no longer use Stunning Strike. I'm currently working on a method for assigning values to each condition, and will update this once that work is done, but for now you can think of the monk's calculated XP values as further underestimation compared to the rest.


## Average calculated XP

The average calculated encounter XP across all classes for a full adventuring day consisting of Medium encounters in shown in Fig. \figref{fig:encounter-xp-vs-level-medium-adventuring-days} (below). As expected, the average encounter XP is close to half of the adventuring day XP budget from the DMG, and is generally a decent margin above the Deadly encounter XP threshold.

<figure id="fig:encounter-xp-vs-level-medium-adventuring-days">
    {% include_relative fig-half-daily-xp-vs-level-medium-adventuring-days-large.html %}
    {% include_relative fig-half-daily-xp-vs-level-medium-adventuring-days-small.html %}
    <figcaption>Average PC encounter XP (red, circles) calculated using Eqn. \eqref{eq:XP-full} for a full adventuring days filled with Medium encounters and two short rests.</figcaption>
</figure>

For levels 1 - 10, the calculated XP values are slightly lower than expected, while for levels 11 - 20 they're slightly higher. The biggest difference comes at level 3, which is the only level where the average XP dips below the Deadly encounter XP threshold. This is likely due to subclasses being excluded from the calculations, which typically come online around level 3. I have plans to include subclasses in the future and will revise this post to reflect those results once they're done.

The corresponding daily XP values are shown in Fig. \figref{fig:daily-xp-vs-level-medium-adventuring-days} (below). As predicted, these values closely follow the adventuring day XP budgets from the DMG, and are nearly twice the average calculated encounter XP values.

<figure id="fig:daily-xp-vs-level-medium-adventuring-days">
    {% include_relative fig-full-daily-xp-vs-level-medium-adventuring-days-large.html %}
    {% include_relative fig-full-daily-xp-vs-level-medium-adventuring-days-small.html %}
    <figcaption>Average PC daily XP (red, circles) calculated using Eqn. \eqref{eq:XP-full} for a full adventuring days filled with Medium encounters and two short rests.</figcaption>
</figure>

These results, along with my previous results from [Calculating Monster XP]({{ site.data.page-links.calculating-monster-xp.path }}) for NPCs, provide strong evidence that this approach accurately replicates how the encounter balancing rules are designed to work in 5th edition D&D.

## Calculated XP by class

Breaking up the average encounter XP from the previous section by class, as shown in Fig. \figref{fig:encounter-xp-thresholds-vs-level} (below), shows some unexpected and interesting results. While the average was indeed close to the expected value of half the adventuring day budget, only a few of the classes come close on their own.

<figure id="fig:pcs-encounter-xp-vs-level-Medium-adventuring-days">
    {% include_relative fig-pcs-encounter-xp-vs-level-medium-adventuring-days-large.html %}
    {% include_relative fig-pcs-encounter-xp-vs-level-medium-adventuring-days-small.html %}
    <figcaption>Average encounter XP for each class for a full adventuring day consisting of Medium encounters and two short rests.</figcaption>
</figure>

Of the twelve classes, only the ranger and rogue classes stay close to target across the full range of levels. The monk remains close all the way up until level 17, but jumps up well above it at level 18 after gaining access to Empty Body. The remaining classes have encounter XP values either well above, or well below target.

The classes with encounter XP values significantly below target are the full spellcaster classes (i.e., the bard, cleric, druid, sorcerer, warlock, and wizard), while those significantly above are the remaining martial classes (i.e., the barbarian, fighter, and paladin). This result may seem surprising at first glance (I wasn't expecting it), but we can make sense of it by looking at the effective hit points and effective damage per round used to calculate it.

According to Eqn. \eqref{eq:XP-simple}, a PC's XP value comes from the product of their average effective hit points and average effective damage per round. Martial character tend to have larger hit dice as well as higher AC values from their armor than spellcasters. They also tend to have more features that can help them mitigate damage or, in the case of the fighter and the paladin, features that heal them without diminishing their ability to deal damage. The result of this is that martial character tend to have significantly higher effective hit points than spellcasters. 

This difference is made clear in Fig. \figref{fig:pcs-encounter-ehp-vs-level-medium-adventuring-days} (below), which plots each class's average effective hit points used to calculate their encounter XP. Expect for a few exceptions, the ranking here matches those observed for XP in Fig. \figref{fig:encounter-xp-thresholds-vs-level}.

<figure id="fig:pcs-encounter-ehp-vs-level-medium-adventuring-days">
    {% include_relative fig-pcs-encounter-ehp-vs-level-medium-adventuring-days-large.html %}
    {% include_relative fig-pcs-encounter-ehp-vs-level-medium-adventuring-days-small.html %}
    <figcaption>Average encounter effective hit points for each class for a full adventuring day consisting of Medium encounters and two short rests.</figcaption>
</figure>

It's also interesting to note that while most of the classes show a linear growth in effective hit points (mostly due to their maximum hit points increasing linearly as they level), the barbarian and monk show non-linear growth in later levels. 

For the barbarian, this growth comes from gaining additional uses of their Rage feature as they level up, which increases their damage mitigation, as well as from their Primal Champion feature at level 20, which increases their Constitution score by four. 

For the monk, there is a small boost from Diamond Soul at level 14, which grants them proficiency in all saving throws (approximately a +4 to their effective AC), as well as a massive boost from Empty Body at level 18, which grants them resistance to nearly all damage but at the cost of dealing less damage.

<figure id="fig:pcs-encounter-edpr-vs-level-medium-adventuring-days">
    {% include_relative fig-pcs-encounter-edpr-vs-level-medium-adventuring-days-large.html %}
    {% include_relative fig-pcs-encounter-edpr-vs-level-medium-adventuring-days-small.html %}
    <figcaption>Average encounter effective damage per round for each class for a full adventuring day consisting of Medium encounters and two short rests.</figcaption>
</figure>

On the damage side of the equation, as Fig. \figref{fig:pcs-encounter-edpr-vs-level-medium-adventuring-days} (above) shows, most classes have very similar effective damage per round. Recall that these values represent the single target damage per round each class is capable of, and that for spellcasters template spells were used rather than each class's actual spell list. So, while a bard may be budgeted as dealing comparable effective damage per round as a wizard, the wizard will almost certainly deal significantly more in actual play due to the bard's limited number of damaging spells known.

Combining the results shown in Fig. \figref{fig:pcs-encounter-ehp-vs-level-medium-adventuring-days} and Fig. \figref{fig:pcs-encounter-edpr-vs-level-medium-adventuring-days}, it's clear why spellcasters had lower than average calculated XP values, and why barbarians, fighters, and paladins were higher than average. Their damage per rounds were similar while having dramatically different effective hit points.

# Conclusion

The average daily XP values for PCs calculated here show good agreement with the adventuring day XP budgets given in [chapter 13](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters) of the _Basic Rules_. And the calculated encounter XP values fit in well with the different encounter difficulty XP thresholds from it as well. Combined with my previous results calculating monster XP values, I think it's safe to say this approach closely matches how the encounter balancing rules in 5th edition D&D are designed to work.

For further readings on this topic, see my posts on how [encounter difficulties]({{ site.data.page-links.daily-xp-and-encounter-difficulty.path }}), [short adventuring days]({{ site.data.page-links.short-adventuring-days.path }}), and [magic items]({{ site.data.page-links.magic-items-and-encounter-balancing.path }}) impact PC XP values.