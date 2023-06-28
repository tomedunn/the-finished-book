---
title: "Magic Items and Encounter Balancing"
excerpt: "How much do magic items change encounter balancing?"
date: 2023-04-30
last_modified_at: 2023-04-30
tags:
  - analysis
  - adventuring day
  - classes
  - encounter balancing
  - magic items
  - xp
---

{% include LaTex.html %}

# Introduction
So far, I've written about how player character (PC) XP thresholds and adventuring day XP budget are impacted for full adventuring days by the [average encounter difficulty]({{ site.url }}{{ site.baseurl }}{% link _classes/daily-xp-and-encounter-difficulty.md %}), as well as by [short adventuring days]({{ site.url }}{{ site.baseurl }}{% link _classes/short-adventuring-days.md %}) with only one or two encounters. In this post, I'd like to add to this by looking at how magic items affect these elements of encounter balancing.

Because magic items come in such a wide range of flavors and powers, covering this topic completely would be a monumental task. So instead, in this post I'll be focusing on a few basic types of magic items: ones that give a bonus to attack rolls, armor class, damage, save difficulty class, and saving throw bonuses. These results will help form a coherent basis that can be applied to a wide range of magic items beyond the simple examples shown here.

# Magic item bonuses
For this analysis, I'll once again be calculating XP values for PCs using the method outlined in [Player Character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}). If you're curious about the details, I strongly suggest reading that post, but for the purposes of this analysis, the key concept is that a PC's XP thresholds and adventuring day XP can both be calculated using the following formula,
\begin{align}
    \XP  &= \HP \cdot \DPRhit \cdot \left( 1 + 0.077\left(\AC + \AB - 15\right) \right) \nonumber \\\\ 
         &= \HP \cdot \DPRhit \cdot \left(\frac{\AC + \AB - 2}{13}\right) \,, 
    \label{eq:XP-full-attacks}
\end{align}
where $$\HP$$ is the PC's maximum hit points, $$\AC\,$$ is their effective armor class (includes adjustments from class features that make the PC harder to damage), $$\DPRhit$$ is their average damage per round assuming all attacks hit, and $$\AB\,$$ is their effective attack bonus (includes adjustments from class features that make it easier for the PC to deal damaage).

Equation \eqref{eq:XP-full-attacks} can also be expressed in terms of a PC's effective saving throw bonuses $$(\SB\,)$$ and effective save difficulty class $$(\DC\,)$$. However, since a PC's $$\DC\,$$ is generally equal to $$\AB + 8$$, and $$\SB\,$$ can generally be treated as $$\AC - 14$$ (see [effective HP and Damage]({{ site.url }}{{ site.baseurl }}{% link _theory/effective-hp-and-damage.md %}#saving-throw-bonus-scaling)), their effects will produce identical outcomes to $$\AC\,$$ and $$\AB\,$$.

These inputs are averaged across multiple encounters to get the PC's encounter XP, which is then multiplied by the ratios given in the [XP Thresholds](#tab:xp-threshold-ratios){: .fig-ref} table (below) to get their XP thresholds for each encounter difficulty.

<div class="dataframe center" style="width:500px;">
    <h3 id="tab:xp-threshold-ratios">XP Thresholds</h3>
    {% include_relative magic-items-and-encounter-balancing/tab-xp-threshold-ratios.html %}
</div>

Calculating a PC's adventuring day XP budget follows the same process as their encounter XP but $$\HP\,$$ also includes any out of combat healing available to the PC. Since most PCs can recover close to their maximum hit points by expending hit dice during short rest, their adventuring day XP budget is roughly twice their encounter XP.

If a magic item increases any of the variables in Eqn. \eqref{eq:XP-full-attacks}, then they'll also increase a PC's encounter XP and adventuring day XP, as will their encounter difficulty XP thresholds. So, if a magic item increases a PC's $$\DPRhit$$ by $$10\%$$, their XP thresholds and adventuring day XP budget will increase by $$10\%$$ as well.

### Bonuses to hit and armor class

If a PC has a magic item that grants them a bonus to their attack rolls of $$+\Delta\AB\,$$, the resulting $$\XP$$ given by Eqn. \eqref{eq:XP-full-attacks} will be
\begin{align}
    %\XP \left(+\Delta\AB\, \right) 
    \XP^{\,\prime}
        &= \HP \cdot \DPRhit \cdot \left(\frac{\AC + \AB + \Delta\AB - 2}{13}\right) \nonumber \\\\ 
        &= \XP_0 \cdot \left(1 + \frac{\Delta\AB}{\AC + \AB - 2} \right)\,
    \label{eq:xp-bonus-ab-full}
\end{align}
where $$\XP_0$$ is their baseline XP with no magic items. 

This assumes the $$+\Delta\AB$$ bonus applies to all of the PC's attacks equally, but that's not always the case. For example, a monk wielding a magic weapon that grants $$+1\,\AB$$ wouldn't gain any benefit while making unarmed strikes as part of their bonus action.

For the case where only a fraction of the PC's total damage $$(d_{\AB})$$ benefits from this magic items, Eqn. \eqref{eq:xp-bonus-ab-full} becomes
\begin{align}
    %\XP \left(+\Delta\AB\, \right) 
    \XP^{\,\prime}
        = \XP_0 \cdot \left(1 + \frac{d_{\AB} \cdot \Delta\AB}{\AC + \AB - 2} \right)\,.
    \label{eq:xp-bonus-ab}
\end{align}
In the limit where $$d_{\AB}= 0$$ the PC would gain no benefit, and when $$d_{\AB} = 1$$ they would gain the full benefit, just as they do in Eqn. \eqref{eq:xp-bonus-ab-full}.

This can be applied to magic items that grant a $$+\Delta\AC\,$$ bonus to $$\AC\,$$ in exactly the same way,
\begin{align}
    %\XP \left(+\Delta\AC\, \right) 
    \XP^{\,\prime}
        = \XP_0 \cdot \left(1 + \frac{h_{\AC} \cdot \Delta\AC}{\AC + \AB - 2} \right)\,,
    \label{eq:xp-bonus-ac}
\end{align}
where $$h_{\AC}$$ represents the typical fraction of a PC's $$\HP\,$$ loss expected to come from attacks.

For both of these types of magic item bonuses, the increase to a PC's encounter XP depends on their baseline value of $$(\AC + \AB - 2)^{-1}$$ at each level. This acts as an upper bounds to the increase in encounter XP for a typical PC due to a magic item that grants a $$+1$$ bonus to either $$\AB\,$$ or $$\AC\,$$.

To get a sense of how large the XP increase can be from these bonuses, Fig. [1](#fig:encounter-xp-generic-bonus){: .fig-ref} (below) plots this value for each class, as well as the average across all classes, from levels 1-20 using data from my previous post [Player Character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}) for a full adventuring day made up of Medium difficulty encounters. 

<figure id="fig:encounter-xp-generic-bonus">
    {% include_relative magic-items-and-encounter-balancing/fig-encounter-xp-generic-bonus-small.html %}
    {% include_relative magic-items-and-encounter-balancing/fig-encounter-xp-generic-bonus-large.html %}
    <figcaption>Figure 1: Shows the typical values of \((\AC + \AB - 2)^{-1}\) as a percent increase in encounter XP for PCs across a full adventuring day of Medium difficulty encounters.</figcaption>
</figure>

While the increase in encounter XP drops slightly as the PCs level up, the average remains close to $$4\%$$. Since Eqns. \eqref{eq:xp-bonus-ab} and \eqref{eq:xp-bonus-ac} are both linear in terms of the size of the magic item bonus, as well as on $$d_{\AB}$$ and $$h_{\AC}$$, we can approximate the increase in encounter XP from both as
\begin{align}
    \Delta\XP \simeq \left(
        d_{\AB} \cdot \Delta\AB\, + h_{\AC} \cdot \Delta\AC\, 
    \right) \cdot 4\% \,.
    \label{eq:xp-bonus-ab-ac-approx}
\end{align}


### Bonus save DC and saving throws

The results of the previous section can easily be extended to magic items that grant bonuses to $$\DC\,$$ or $$\SB\,$$ by recognizing that $$\DC = \AB + 8$$ for most PCs and that, as a result of this, $$\SB = \AC - 14$$ in order to maintain the same chance of hit with both saving throws and attack rolls.

The general equation for a PC's encounter XP when using a magic item that grants a $$+\Delta\DC\,$$ bonus to $$\DC\,$$ is therefore,
\begin{align}
    %\XP \left(+\Delta\DC\, \right) 
    \XP^{\,\prime}
        = \XP_0 \cdot \left(1 + \frac{d_{\DC} \cdot \Delta\DC}{\AC + \AB - 2} \right)\,,
    \label{eq:xp-bonus-dc}
\end{align}
where $$d_{\DC}$$ is the fraction of the PC's total damage that comes from saving throws.

Similarly, magic items that grant a $$+\SB\,$$ bonus to a PC's saving throws result in an encounter XP of
\begin{align}
    %\XP \left(+\Delta\SB\, \right) 
    \XP^{\,\prime}
        = \XP_0 \cdot \left(1 + \frac{h_{\SB} \cdot \Delta\SB}{\AC + \AB - 2} \right)\,,
    \label{eq:xp-bonus-sb}
\end{align}
where $$h_{\SB}$$ represents the typical fraction of a PC's $$\HP\,$$ loss that comes from saving throws.

And since the form of Eqns. \eqref{eq:xp-bonus-dc} and \eqref{eq:xp-bonus-sb} matches that of Eqns. \eqref{eq:xp-bonus-ab} and \eqref{eq:xp-bonus-ac}, they can also be combined and approximated using the results for $$(\AC + \AB - 2)^{-1}$$ shown in Fig. [1](#fig:encounter-xp-generic-bonus){: .fig-ref},
\begin{align}
    \Delta\XP \simeq \left(
        d_{\DC} \cdot \Delta\DC\, + h_{\SB} \cdot \Delta\SB\, 
    \right) \cdot 4\% \,.
    \label{eq:xp-bonus-dc-sb-approx}
\end{align}

### Bonus damage
For magic weapons that deal an additional $$+\Delta D$$ damage on a hit, the increase to a PC's $$\DPRhit$$ will be 
\begin{align}
    \Delta \DPRhit = \Nattacks \cdot \Delta D \,,
    \label{eq:dpr-bonus-damage}
\end{align}
where $$\Nattacks$$ is the number of attacks per round the PCs makes with the weapon. 

This increase in $$\DPRhit$$ will, in turn, increase their encounter XP and daily XP in the following way, 
\begin{align}
    %\XP \left(+\Delta D \right) 
    \XP^{\,\prime}
        &= \HP \cdot \left( \DPRhit + \Nattacks \cdot \Delta D \right) \cdot \left(\frac{\AC + \AB - 2}{13}\right) \nonumber \\\\ 
        &= \XP_0 \left( 1 + \frac{\Nattacks \cdot \Delta D}{ \DPRhit } \right) \,.
    \label{eq:xp-bonus-damage}
\end{align}

PCs that get most of their damage directly from their weapons, like fighters, will benefit more than those that get most of their damage from spells or class features, like rogues or paladins. This relationship is illustrated in Fig. [2](#fig:encounter-xp-damage-bonus){: .fig-ref} (below) for the martial classes, calculated for a full adventuring day made up of Medium difficulty encounters.

<figure id="fig:encounter-xp-damage-bonus">
    {% include_relative magic-items-and-encounter-balancing/fig-encounter-xp-damage-bonus-small.html %}
    {% include_relative magic-items-and-encounter-balancing/fig-encounter-xp-damage-bonus-large.html %}
    <figcaption>Figure 2: Shows the increase in encounter XP for PCs with a +1 magic weapon relative to their baseline XP with no magic items for a full adventuring day made up of Medium difficulty encounters.</figcaption>
</figure>

While the average benefit tends to decrease as a PC levels up, due to more of their damage coming from sources other than their weapon's damage, a magic item that has $$+1$$ damage increases a PC's XP thresholds and adventuring day XP by $$6.8\%$$ on average.

Just as with the previous sections, we can use this average to approximate the increase to a PC's encounter XP due to a magic weapon that grants $$+\Delta D$$ as 
\begin{align}
    \Delta\XP \simeq \Delta D \cdot 6.8\% \,.
    \label{eq:xp-bonus-damage-approx}
\end{align}

# Discussion

With most of the math out of the way, it's worth noting that not all of these bonuses are additive. While there are circumstances where a PC might deal damage in a way that involves both an attack roll and a saving throw, generally, the two are mutually exclusive. In other words, $$d_{\AB} + d_{\DC} \leq 1$$. Similarly, the damage a PC takes will nearly always target either their $$\AC\,$$ or their $$\SB\,$$. Thus, $$h_{\AC} + h_{\SB} \leq 1$$.

With this in mind, the [Magic Item XP Bonus](#tab:magic-item-bonus){: .fig-ref} table (below) provides a summary of the average encounter XP increases from each type of magic item bonus covered in the previous section.

<div class="dataframe center" style="width:660px;">
    <h3 id="tab:magic-item-bonus">Magic Item XP Bonus</h3>
    {% include_relative magic-items-and-encounter-balancing/tab-bonus-summary.html %}
</div>

Using the encounter XP ratios for each of the encounter difficulties listed in the [XP Thresholds](#tab:xp-threshold-ratios){: .fig-ref} table earlier in this post, the Medium XP threshold is $$100\%$$ higher than the Easy XP threshold, the Hard XP threshold is $$50\%$$ higher than the Medium XP threshold, and the Deadly XP threshold is $$55\%$$ higher than the Hard XP threshold. 

In order for magic items to cause the encounter building rules in the DMG to underestimate encounter difficulties by a full category, they would have to increase the party's encounter XP by at least $$50\%$$. Given the XP bonuses listed in the [Magic Item XP Bonus](#tab:magic-item-bonus){: .fig-ref} table, this would be difficult to accomplish using only these standard magic items.

<figure id="fig:encounter-xp-high-magic">
    {% include_relative magic-items-and-encounter-balancing/fig-encounter-xp-high-magic-small.html %}
    {% include_relative magic-items-and-encounter-balancing/fig-encounter-xp-high-magic-large.html %}
    <figcaption>Figure 3: Shows the percent increase in encounter XP for a PC following a high magic item progression over baseline, as described in the <a href="#tab:high-magic-progression" class="fig-ref">High Magic Progression</a> table for full adventuring days made up of Medium difficulty encounters.</figcaption>
</figure>


This is illustrated in Fig. [3](#fig:encounter-xp-high-magic){: .fig-ref} (above), which shows the encounter XP increase for PCs who gain magic items with the bonuses described in the [High Magic Progression](#tab:high-magic-progression){: .fig-ref} table (below) as they level up.

<div class="dataframe center" style="width:750px;">
    <h3 id="tab:high-magic-progression">High Magic Progression</h3>
    {% include_relative magic-items-and-encounter-balancing/tab-high-magic-progression.html %}
</div>

While the fighter comes close to the $$50\%$$ encounter XP increase needed to misjudge encounter difficulties by a full category, the average is still quite a ways below it at around $$32\%$$. Of course, that doesn't mean these XP increases aren't worth accounting for.

As mentioned [earlier](#magic-item-bonuses), a DM can account for this increase in power by increasing the party's encounter difficulty XP thresholds, as well as their adventuring day XP budget, by the percents listed in "XP Increase" column of the [High Magic Progression](#tab:high-magic-progression){: .fig-ref} table (or by whatever percent they calculate for their party's magic items), or by keeping the party's XP thresholds the same and simply running more encounters.

If we approximate a PC's adventuring day XP budget as twice their encounter XP budget, then a party following the magic item progression described in the [High Magic Progression](#tab:high-magic-progression){: .fig-ref} table would be able to handle an additional Medium encounter in tier 2, an additional Hard encounter in tier 3, and an additional Deadly encounter in tier 4.

# Conclusion

Magic items are powerful tools in the hands of the PCs, and, if not accounted for, can have a serious impact on a DM's ability to properly build and balance combat encounters. This is especially true at higher levels, where the bonuses from magic items are generally much larger than they are at low levels.

While there are many more magic items than the ones covered here, these results should form a strong basis that DMs can use to improve encounter balancing in their campaigns as their PCs level up and acquire new and powerful magic items.

As a final comment on these findings, the fact that the XP increase from a $$+1$$ to hit, armor class, save DC, or saving throw bonus gets smaller as a PC's level increases is not a true reflection of how these changes impact combat at later levels. Because the game's combat math is centered around the PCs having a baseline chance to hit or be hit of $$65\%$$ at all levels, a $$+1$$ to any of these should always increase a PC's XP values by the same percentage, regardless of their level.

The fact that these XP increases get smaller at higher levels is the result of the specific XP formula used in this post. As I show [here]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}), while this formulation matches XP values used by the D&D core rules quite well, it's based on a linear approximation to the more general XP formula derived from the game's combat mechanics. The result of this approximation is that XP values for monsters and PCs underestimate the impact of a creature having $$\AB\,$$, $$\AC\,$$, $$\DC\,$$, or $$\SB\,$$ values that are higher/lower than baseline relative to differences $$\HP\,$$ and $$\DPR\,$$.

That's all I'll say on the topic for now, but I will be covering this in more detail in a future post.