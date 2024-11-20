---
title: "Magic Items and Encounter Balancing: part 2"
excerpt: "How much do magic items change encounter balancing?"
permalink: /:collection/:name/
date: 2024-01-30
last_modified_at: 2024-01-30
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

In [Magic Items and Encounter Balancing: part 1]({{ site.data.page-links.magic-items-and-encounter-balancing.path }}) I looked at how magic items impact the 5th edition D&D encounter building rules. In the conclusion of that post, I mentioned how the equation used to calculate player character XP thresholds tends to undervalue the impact of bonuses to a character's attack bonus, armor class, saving throw bonuses, and save difficulty class. In this post, I revisit this topic using the exponential form of that XP equation.

# Magic item bonuses
For this analysis, I'll once again be calculating XP values for PCs using the method outlined in [Player Character XP]({{ site.data.page-links.xp-and-player-characters.path }}). If you're curious about the details, I strongly suggest reading that post, but for the purposes of this analysis, the key concept is that a PC's XP thresholds and adventuring day XP can both be calculated using the following formula,
\begin{align}
    \XP  &= \HP \cdot \DPRhit \cdot 1.077^{\AC + \AB - 15} \,, 
    \label{eq:XP-full-attacks}
\end{align}
where $$\HP$$ is the PC's maximum hit points, $$\AC\,$$ is their effective armor class (includes adjustments from class features that make the PC harder to damage), $$\DPRhit$$ is their average damage per round assuming all attacks hit, and $$\AB\,$$ is their effective attack bonus (includes adjustments from class features that make it easier for the PC to deal damage).

Equation \eqref{eq:XP-full-attacks} can also be expressed in terms of a PC's effective saving throw bonuses $$(\SB\,)$$ and effective save difficulty class $$(\DC\,)$$. However, since a PC's $$\DC\,$$ is generally equal to $$\AB + 8$$, and $$\SB\,$$ can generally be treated as $$\AC - 14$$ (see [effective HP and Damage]({{ site.data.page-links.effective-hp-and-damage.path }}#saving-throw-bonus-scaling)), their effects will produce identical outcomes to $$\AC\,$$ and $$\AB\,$$.

These inputs are averaged across multiple encounters to get the PC's encounter XP, which is then multiplied by the ratios given in the [XP Thresholds](#tab:xp-threshold-ratios){: .fig-ref} table (below) to get their XP thresholds for each encounter difficulty.

<div class="dataframe center" style="width:500px;">
    <h3 id="tab:xp-threshold-ratios">XP Thresholds</h3>
    {% include_relative tab-xp-threshold-ratios.html %}
</div>

Calculating a PC's adventuring day XP budget follows the same process as their encounter XP but $$\HP\,$$ also includes any out of combat healing available to the PC. Since most PCs can recover close to their maximum hit points by expending hit dice during short rest, their adventuring day XP budget is roughly twice their encounter XP.

If a magic item increases any of the variables in Eqn. \eqref{eq:XP-full-attacks}, then they'll also increase a PC's encounter XP and adventuring day XP, as will their encounter difficulty XP thresholds. So, if a magic item increases a PC's $$\DPRhit$$ by $$10\%$$, their XP thresholds and adventuring day XP budget will increase by $$10\%$$ as well.

### Bonuses to hit and armor class

If a PC has a magic item that grants them a bonus to their attack rolls of $$+\Delta\AB\,$$, the resulting $$\XP$$ given by Eqn. \eqref{eq:XP-full-attacks} will be
\begin{align}
    %\XP \left(+\Delta\AB\, \right) 
    \XP^{\,\prime} 
        &= \HP \cdot \DPRhit \cdot 1.077^{\AC + \AB + \Delta\AB - 15} \nonumber \\\\ 
        &= \XP_0 \cdot 1.077^{\Delta\AB} \,,
    \label{eq:xp-bonus-ab-full}
\end{align}
where $$\XP_0$$ is their baseline XP with no magic items. 

This assumes the $$+\Delta\AB$$ bonus applies to all of the PC's attacks equally, but that's not always the case. For example, a monk wielding a magic weapon that grants $$+1\,\AB$$ wouldn't gain any benefit while making unarmed strikes as part of their bonus action.

For the case where only a fraction of the PC's total damage $$(d_{\AB})$$ benefits from this magic items, Eqn. \eqref{eq:xp-bonus-ab-full} becomes
\begin{align}
    %\XP \left(+\Delta\AB\, \right)
    \XP^{\,\prime} = \XP_0 \cdot 1.077^{\,d_{\AB} \cdot \Delta\AB} \,,
    \label{eq:xp-bonus-ab}
\end{align}
In the limit where $$d_{\AB}= 0$$ the PC would gain no benefit, and when $$d_{\AB} = 1$$ they would gain the full benefit, just as they do in Eqn. \eqref{eq:xp-bonus-ab-full}.

This effect is illustrated in Fig. \figref{fig:encounter-xp-ab-bonus} (below), which shows the XP benefits of a weapon that grants $$+1$$ to hit for both a fighter wielding a greatsword and a monk wielding a quarterstaff. Since all of the fighter's damage comes from weapon attacks, their encounter XP increases by the full $$7.7\%$$. And, since roughly half of the monk's damage comes from weapon attacks, their encounter XP increases by only half as much.

<figure id="fig:encounter-xp-ab-bonus">
    {% include_relative fig-encounter-xp-ab-bonus-small.html %}
    {% include_relative fig-encounter-xp-ab-bonus-large.html %}
    <figcaption>Shows the increase in encounter XP from a magic weapon that grants +1 to hit for a fighter wielding a greatsword and a monk wielding a quarterstaff for a full adventuring day made up of Medium difficulty encounters.</figcaption>
</figure>

In general, most PCs who rely on attacks for dealing damage gain the full benefit of a +1 to hit. So to good approximation a magic item that grants a +1 to hit can be treated as increasing a PC's XP thresholds and adventuring day XP by $$7.7\%$$.

This can be applied to magic items that grant a $$+\Delta\AC\,$$ bonus to $$\AC\,$$ in exactly the same way,
\begin{align}
    %\XP \left(+\Delta\AC\, \right) 
    \XP^{\,\prime} = \XP_0 \cdot 1.077^{h_{\AC} \cdot \Delta\AC} \,.
    \label{eq:xp-bonus-ac}
\end{align}
where $$h_{\AC}$$ represents the typical fraction of a PC's $$\HP\,$$ loss expected to come from attacks.

Combining the results of Eqns. \eqref{eq:xp-bonus-ab} and \eqref{eq:xp-bonus-ac} yields
\begin{align}
    \XP^{\,\prime} = \XP_0 \cdot 1.077^{\,d_{\AB} \cdot \Delta\AB + h_{\AC} \cdot \Delta\AC}\,,
    %\label{eq:xp-bonus-ab-ac-approx}
\end{align}
which, if we subtract off $$\XP_0$$ and expand the exponent to first order in $$\Delta\AB$$ and $$\Delta\AC$$, can be used to express the percent change in a PC's XP thresholds as
\begin{align}
    \Delta \XP \simeq \left( {\,d_{\AB} \cdot \Delta\AB + h_{\AC} \cdot \Delta\AC} \right) \cdot 7.7\%\,.
    \label{eq:xp-bonus-ab-ac-approx}
\end{align}

### Bonus save DC and saving throws

The results of the previous section can easily be extended to magic items that grant bonuses to $$\DC\,$$ or $$\SB\,$$ by recognizing that $$\DC = \AB + 8$$ for most PCs and that, as a result of this, $$\SB = \AC - 14$$ in order to maintain the same chance of hit with both saving throws and attack rolls.

The general equation for a PC's encounter XP when using a magic item that grants a $$+\Delta\DC\,$$ bonus to $$\DC\,$$ and a $$+\Delta\SB$$ bonus to $$\SB\,$$ is therefore,
\begin{align}
    \XP^{\,\prime} = \XP_0 \cdot 1.077^{\,d_{\DC} \cdot \Delta\DC + h_{\SB} \cdot \Delta\SB}\,,
\end{align}
where $$d_{\DC}$$ is the fraction of the PC's total damage that comes from saving throws against their save DC, and $$h_{\SB}$$ represents the typical fraction of a PC's $$\HP\,$$ loss that comes from saving throws.

And, just like in the previous section, we can subtract off $$\XP_0$$ and expand the exponent to first order in $$\Delta\DC$$ and $$\Delta\SB$$ to approximate the percent change in a PC's XP thresholds from such magic items,
\begin{align}
    \Delta \XP \simeq \left( {\,d_{\DC} \cdot \Delta\DC + h_{\SB} \cdot \Delta\SB} \right) \cdot 7.7\%\,.
    \label{eq:xp-bonus-dc-sb-approx}
\end{align}

### Bonus damage
For magic weapons that deal an additional $$+\Delta D$$ damage on a hit, the increase to a PC's $$\DPRhit$$ will be 
\begin{align}
    \Delta \DPRhit = \Nattacks \cdot \Delta D \,,
    \label{eq:dpr-bonus-damage}
\end{align}
where $$\Nattacks$$ is the number of attacks per round the PCs makes with the weapon. 

This increase in $$\DPRhit$$ will, in turn, increase their encounter XP and daily XP by 
\begin{align}
    %\XP \left(+\Delta D \right) 
    \XP^{\,\prime}
        &= \HP \cdot \left( \DPRhit + \Nattacks \cdot \Delta D \right) \cdot 1.077^{\AC + \AB - 15} \nonumber \\\\ 
        &= \XP_0 \left( 1 + \frac{\Nattacks \cdot \Delta D}{ \DPR } \right) \,.
    \label{eq:xp-bonus-damage}
\end{align}

PCs that get most of their damage directly from their weapons, like fighters, will benefit more than those that get most of their damage from spells or class features, like rogues or paladins. This relationship is illustrated in Fig. \figref{fig:encounter-xp-damage-bonus} (below) for the martial classes, calculated for a full adventuring day made up of Medium difficulty encounters.

<figure id="fig:encounter-xp-damage-bonus">
    {% include_relative fig-encounter-xp-damage-bonus-small.html %}
    {% include_relative fig-encounter-xp-damage-bonus-large.html %}
    <figcaption>Shows the increase in encounter XP for PCs with a +1 magic weapon relative to their baseline XP with no magic items for a full adventuring day made up of Medium difficulty encounters.</figcaption>
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
    <h3 id="tab:magic-item-bonus">Magic Item Bonus</h3>
    {% include_relative tab-bonus-summary.html %}
</div>

Using the encounter XP ratios for each of the encounter difficulties listed in the [XP Thresholds](#tab:xp-threshold-ratios){: .fig-ref} table earlier in this post, the Medium XP threshold is $$100\%$$ higher than the Easy XP threshold, the Hard XP threshold is $$50\%$$ higher than the Medium XP threshold, and the Deadly XP threshold is $$55\%$$ higher than the Hard XP threshold. 

In order for magic items to cause the encounter building rules in the DMG to underestimate encounter difficulties by a full category, they would have to increase the party's encounter XP by at least $$50\%$$. Given the XP bonuses listed in the [Magic Item XP Bonus](#tab:magic-item-bonus){: .fig-ref} table, this would be difficult to accomplish using only +1 magic items, but quite possible with a full array of +2 magic items or better.

<figure id="fig:encounter-xp-high-magic">
    {% include_relative fig-encounter-xp-high-magic-small.html %}
    {% include_relative fig-encounter-xp-high-magic-large.html %}
    <figcaption>Shows the percent increase in encounter XP for a PC following a high magic item progression over baseline, as described in the <a href="#tab:high-magic-progression" class="fig-ref">High Magic Progression</a> table for full adventuring days made up of Medium difficulty encounters.</figcaption>
</figure>


This result is illustrated in Fig. \figref{fig:encounter-xp-high-magic} (above), which shows the encounter XP increase for a PC who gain magic items with the bonuses described in the [High Magic Progression](#tab:high-magic-progression){: .fig-ref} table (below) as they level up.

<div class="dataframe center" style="width:750px;">
    <h3 id="tab:high-magic-progression">High Magic Progression</h3>
    {% include_relative tab-high-magic-progression.html %}
</div>

By tier 3, the increase in encounter XP for such a party is $$45\%$$, which means their Medium XP threshold will be nearly equal to the Hard XP threshold listed in the DMG, and their Hard XP threshold will nearly equal the Deadly threshold in the DMG!

Put another way, by tier 3, their magic items are strong enough to make every encounter play out one difficulty level lower than the encounter building rules in the DMG predict!

# Conclusion

Magic items are powerful tools in the hands of the PCs, and, if not accounted for, can have a serious impact on a DM's ability to properly build and balance combat encounters. This is especially true at higher levels, where the bonuses from magic items are generally much larger than they are at low levels, and where the boost they provide to the PCs can be enough to shift encounter difficulties down one full category over what's listed in the DMG.

While there are many more magic items than the ones covered here, these results should form a strong basis that DMs can use to improve encounter balancing in their campaigns as their PCs level up and acquire new and powerful magic items.