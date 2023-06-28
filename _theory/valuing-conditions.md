---
title: "Valuing Conditions"
excerpt: "How strong are conditions in 5th edition D&D?"
date: 2022-12-14
last_modified_at: 2022-12-14
tags:
  - conditions
  - mechanics
  - theory
  - xp
---

<div style="display:none">
\(
\newcommand{\adv}{\mathrm{adv}}
\newcommand{\dis}{\mathrm{dis}}

\newcommand{\crit}{\mathrm{c}}
\newcommand{\hit}{\mathrm{h}}
\newcommand{\miss}{\mathrm{m}}
\newcommand{\save}{\mathrm{s}}
\newcommand{\fail}{\mathrm{f}}

\newcommand{\p}{\rho}

\newcommand{\AC}{\mathit{AC}}
\newcommand{\eAC}{\mathit{eAC}}
\newcommand{\SB}{\mathit{SB}}
\newcommand{\SBave}{\SB_\mathrm{ave}}

\newcommand{\DPR}{\mathit{DPR}}
\newcommand{\eDPR}{\mathit{eDPR}}
\newcommand{\eHP}{\mathit{eHP}}

\newcommand{\HP}{\mathit{HP}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\DC}{\mathit{DC}}
\newcommand{\d}{\mathit{d}}
\newcommand{\D}{\mathit{D}}
\newcommand{\Dave}{\D}
\newcommand{\DDave}{\Delta \D}
\newcommand{\DDaveadv}{\D_{\,\adv}}
\)
</div>

<style>
td {
  text-align: center
}
</style>

# Introduction <!-- omit in toc -->

Balancing abilities, monsters, and spells is an important part of the design process for D&D, whether for homebrew use or official publication. There is guidance in chapter 9 of the DMG for how to do this, but it's mostly described in terms of damage and healing with little information on how to handle other mechanics. This gap in knowledge make balancing more complicated creations much more difficult.

In this post, I aim to add a bit more clarity to this task by showing how conditions in 5th edition can be evaluated in terms of damage and healing.

This post is broken up into two sections. The first breaks down each condition into one of several components, each of which is then evaluated in terms of its impact on damage and healing. And the second uses the values of these components to construct the overall value of each condition.

# Condition components <!-- omit in toc -->

Reading through 5th edition D&D's list of conditions (see [Appendix A](https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions) of the _Basic Rules_) reveals a number common components that are shared between them. I've summarized these components in Table <a href="#tab:condition-components" class="fig-ref">1</a> (below), but as a simple example, "attack rolls against the creature have advantage" is a component common to several conditions, such as the [blinded](https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Blinded) and [restrained](https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Restrained) conditions.

<div class="dataframe center">
<h3 id="tab:condition-components">Table 1</h3>
<table border="0">
    <thead>
        <tr>
            <td style="text-align:left"><strong>Condition</strong></td>
            <td><strong>Actions</strong></td>
            <td><strong>Attacks Against</strong></td>
            <td><strong>Attacks From</strong></td>
            <td><strong>Saves Against</strong></td>
            <td><strong>Speed</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Blinded</td>
            <td>-</td>
            <td>adv</td>
            <td>dis</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Charmed</td>
            <td>-</td>
            <td>-</td>
            <td>no charmer</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Deafened</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Frightened</td>
            <td>-</td>
            <td>-</td>
            <td>dis</td>
            <td>-</td>
            <td>zero*</td>
        </tr>
        <tr>
            <td style="text-align:left">Grappled</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>zero</td>
        </tr>
        <tr>
            <td style="text-align:left">Incapacitated</td>
            <td>none</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Invisible</td>
            <td>-</td>
            <td>dis</td>
            <td>adv</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Paralyzed</td>
            <td>none</td>
            <td>adv, crit</td>
            <td>-</td>
            <td>fail (Str, Dex)</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Petrified</td>
            <td>none</td>
            <td>adv</td>
            <td>-</td>
            <td>fail (Str, Dex)</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Poisoned</td>
            <td>-</td>
            <td>-</td>
            <td>dis</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Prone</td>
            <td>-</td>
            <td>adv/dis*</td>
            <td>dis</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Restrained</td>
            <td>-</td>
            <td>adv</td>
            <td>dis</td>
            <td>dis (Dex)</td>
            <td>zero</td>
        </tr>
        <tr>
            <td style="text-align:left">Stunned</td>
            <td>none</td>
            <td>adv</td>
            <td>-</td>
            <td>fail (Str, Dex)</td>
            <td>zero</td>
        </tr>
        <tr>
            <td style="text-align:left">Unconscious</td>
            <td>none</td>
            <td>adv, crit</td>
            <td>dis</td>
            <td>fail (Str, Dex)</td>
            <td>-</td>
        </tr>
    </tbody>
</table>
</div>

Here, "adv" stands for advantage, "dis" stands for disadvantage, "crit" stands for scoring an automatic critical on a hit, and "fail" stands for automatically failing the listed saving throws. Missing from the list is that the [petrified](https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Petrified) condition also grants resistance to all damage, which will be factored in later.

In total, across all 14 conditions, there are seven common components that carry mechanical weight,

- [Advantage on attack rolls](#advantage-on-attack-rolls)
- [Disadvantage on attack rolls](#disadvantage-on-attack-rolls)
- [Automatically crit when attacks hit](#automatically-crit-when-attacks-hit)
- [Disadvantage on saving throws](#disadvantage-on-saving-throws)
- [Automatically fail saving throws](#automatically-fail-saving-throws)
- [Inability to take actions](#inability-to-take-actions)
- [Inability to move](#inability-to-move)

By understanding the impact each of these components has on combat, we can derive a total value for each condition. The links above will take you to the relevant section for each component, but if the math doesn't interest you, you can also skip straight to the summary [here](#component-summary-).

## Advantage on attack rolls

Assuming an attack deals no damage on a miss, the average damage for an attack can be calculated generically as
\begin{align}
    \Dave &= \D_\hit \, \p_\hit + \D_\crit \, \p_\crit \,,
    \label{eq:attack-damage}
\end{align}
where $$\D_\hit$$ is the average damage of a hit, $$\p_\hit$$ is the probability of hit, $$\D_\crit$$ is the average damage of a critical hit, and $$\p_\crit$$ is the probability of a critical hit. 

When attacking with advantage, two attack rolls are made and the highest roll is used to determine whether or not the attack hits. This increases the probability of the attack resulting in a hit or a critical hit,

\begin{align}
    \p_\hit^\adv  &= \p_\hit \left( 2 - \p_\hit - 2 \p_\crit \right) \,, \label{eq:adv-hit-prob} \\\\ 
    \p_\crit^\adv &= \p_\crit \left( 2 - \p_\crit \right) \,, \label{eq:adv-crit-prob}
\end{align}

which leads to an increase in the average damage of the attack as a result,

\begin{align}
    \Dave_\adv &= \D_\hit \, \p_\hit \left( 2 - \p_\hit - 2 \p_\crit \right) + \D_\crit \, \p_\crit \left( 2 - \p_\crit \right) \,.
    \label{eq:attack-damage-adv}
\end{align}

Since this doesn't increase the damage of either a hit or a critical hit, it's useful to think of advantage as increasing the attack's effective attack bonus $$(\AB\,)$$.

For regular attacks, an attack bonus increase of $$\Delta \AB$$ increases the average damage of the attack by $$\Delta \D = \D_\hit \, \Delta \AB / 20$$. Using the difference in damage between Eqns. \eqref{eq:attack-damage-adv} and \eqref{eq:attack-damage} to determine $$\Delta \D$$, the effective attack bonus increase for attacking with advantage is, 

\begin{align}
    \Delta \AB_\adv &= 20 \left( \p_\hit \left( 1 - \p_\hit - 2 \p_\crit \right) + \d_\crit \, \p_\crit \left( 1 - \p_\crit \right) \right) \,,
    \label{eq:attack-delta-ab-adv} 
\end{align}

where $$\d_\crit = \D_\crit / \D_\hit$$.

<figure id="fig:delta-ab-advantage">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/valuing-conditions/fig-delta-ab-advantage.svg">
    <figcaption>Figure 1: Effective attack bonus increase from advantage as a function of the attacks normal chance to hit or crit for an attack that deals no extra damage on a critical hit.</figcaption>
</figure>

Figure <a href="#fig:delta-ab-advantage" class="fig-ref">1</a> (above) plots Eqn. \eqref{eq:attack-delta-ab-adv} for the case where $$\d_\crit = 1.5$$, which produces a maximum attack bonus increase of $$\Delta \AB_\adv = +5.5$$ for $$\p_\hit + \p_\crit = 0.5$$.

For a baseline chance to hit or crit of $$\p_\hit + \p_\crit = 0.65$$, and $$\d_\crit = 1.5$$, the effective attack bonus increase from advantage is $$\Delta \AB_\adv = +5.0$$. This is slightly higher than the value of $$+4$$ used in the [Monster Features](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterFeatures) table from chapter 9 of the DMG (see the entries for Blood Frenzy, Nimble Escape, and Shadow Stealth). The lower value in the DMG could be because WotC assumes a lower value of $$\d_\crit$$, or it could be lower to account for the monsters not always benefiting from these features.

For higher values of $$\d_\crit$$, the effective attack bonus from advantage increase to $$+5.5$$ for $$\d_\crit = 2.0$$ and $$+6.0$$ for $$\d_\crit = 2.5$$. This is especially relevant for the Barbarian class, which has easy access to advantage from Reckless Attack, and increased critical hit damage from Brutal Critical.

The value of having advantage can also be expressed as a percent change in damage using Eqns. \eqref{eq:attack-damage} and \eqref{eq:attack-damage-adv},

\begin{align}
    \Delta \d_{\,\adv} &= \frac{ \D_\adv - \Dave }{ \Dave } \nonumber \\\\ 
                       &= \frac{ \p_\hit \left( 1 - \p_\hit - 2 \p_\crit \right) + \d_\crit \, \p_\crit \left( 1 - \p_\crit \right) }{ \p_\hit + \d_\crit \, \p_\crit } \,.
    \label{eq:attack-delta-pct-adv} 
\end{align}

For $$\p_\hit + \p_\crit = 0.65$$ and $$\d_\crit = 1.5$$, Eqn. \eqref{eq:attack-delta-pct-adv} yields an increase in damage of $$37.2\%$$.

## Disadvantage on attack rolls

When attacking with disadvantage, two attack rolls are made, however, the lowest roll is used to determine whether or not the attack hits instead of the highest. Following through the same steps we covered for attacks with advantage, the probabilities of a hit or a critical hit with disadvantage are

\begin{align}
    \p_\hit^\dis  &= \p_\hit \left( \p_\hit + 2 \p_\crit \right) \,, \label{eq:dis-hit-prob} \\\\ 
    \p_\crit^\dis &= \p_\crit^2 \,, \label{eq:dis-crit-prob}
\end{align}

which lead to an effective attack bonus decrease of

\begin{align}
    \Delta \AB_\dis &= - 20 \left( \p_\hit \left( 1 - \p_\hit - 2 \p_\crit \right) + \d_\crit \, \p_\crit \left( 1 - \p_\crit \right) \right) \nonumber \\\\ 
                    &= - \Delta \AB_\adv \,.
    \label{eq:attack-delta-ab-dis} 
\end{align}

This means that for a baseline chance to hit or crit of $$\p_\hit + \p_\crit = 0.65$$, the effective change in attack bonus from disadvantage is $$\Delta \AB_\dis = -5.0$$. For creatures with abilities that force their attackers to attack with disadvantage, this can also be though of as an equivalent increase to the creature's armor class, $$\Delta \AC_\dis = +5.0$$. This is, again, slightly larger than the value of $$+4$$ used in the [Monster Features](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterFeatures) table from chapter 9 of the DMG (see the entries for Nimble Escape).

In terms of a percent change in damage, $$\d_{\,\dis} = - \d_{\,\adv}$$, which means for $$\p_\hit + \p_\crit = 0.65$$ and $$\d_\crit = 1.5$$ a change in damage of $$-37.2\%$$.

## Automatically crit when attacks hit

Automatically scoring a critical hit when landing a normal hit can be valued in much the same way as advantage/disadvantage on attack rolls. The average damage of an attack that deals critical hit damage on any hit is

\begin{align}
    \Dave &= \D_\crit \left( \p_\hit + \p_\crit \right)\,,
    \label{eq:attack-damage-auto-crit}
\end{align}

where, again, $$\D_\crit$$ is the average damage of a critical hit, $$\p_\hit$$ is the probability of a hit and $$\p_\crit$$ is the probability of a critical hit under normal circumstances.

Just as with advantage/disadvantage, this can be converted to an effective increase in attack bonus by comparing the damage from Eqn. \eqref{eq:attack-damage-auto-crit} with the damage from Eqn. \eqref{eq:attack-damage}. Doing so yields

\begin{align}
    \Delta \AB_\mathrm{ac} &= 20 \p_\hit \left( \d_\crit - 1 \right) \,.
    \label{eq:attack-delta-ab-auto-crit} 
\end{align}

For a baseline chance to hit of $$\p_\hit = 0.60$$ and $$\d_\crit = 1.5$$, automatically scoring a critical hit when hitting with an attack is worth $$\Delta \AB_\mathrm{ac} = +6.0$$.

Expressed as a percent change in damage,

\begin{align}
    \Delta \d_{\,\mathrm{ac}} &= \frac{ \p_\hit \left( \d_\crit - 1 \right) }{ \p_\hit + \d_\crit \, \p_\crit } \,,
    \label{eq:attack-delta-pct-auto-crit} 
\end{align}

which translates into a 44.4% increase in damage for the baseline values of $$\p_\hit = 0.60$$, $$\p_\crit = 0.05$$, and $$\d_\crit = 1.5$$.

## Disadvantage on saving throws

For effects that deal damage following a saving throws, the average damage can be expressed generically as
\begin{align}
    \Dave &= \D_\fail \, \p_\fail + \D_\save \, \p_\save \,,
    \label{eq:save-damage-generic}
\end{align}

where $$\D_\fail$$ is the average damage for failing the save, $$\p_\fail$$ is the probability of failing the save, $$\D_\save$$ is the average damage for succeeding on the save, and $$\p_\save$$ is the probability of succeeding. Since $$1 = \p_\fail + \p_\save$$, this can also be written as
\begin{align}
    \Dave &= \left( \D_\fail - \D_\save \right) \p_\fail + \D_\save \nonumber \\\\ 
          &=  \D_\fail \left( \left( 1 - \d_\save \right) \p_\fail + \d_\save \right)  \,,
    \label{eq:save-damage}
\end{align}
where $$\d_\save = \D_\save / \D_\fail$$.

When attempting a saving throw with disadvantage, the average damage of each outcome remains the same, but the probabilities change as follows, 
\begin{align}
    \p_\fail^\dis &= \p_\fail \left( 2 - \p_\fail \right) \,, \label{eq:dis-fail-prob} \\\\ 
    \p_\save^\dis &= \p_\save^2 = \left( 1 - \p_\fail \right)^2 \,. \label{eq:dis-save-prob}
\end{align}

The average damage taken increases as a result, and can be calculated as follows,
\begin{align}
    \Dave_\dis &= \D_\fail \left( \left( 1 - \d_\save \right) \p_\fail \left( 2 - \p_\fail \right) + \d_\save \right) \,.
    \label{eq:save-damage-dis}
\end{align}

When a saving throw is made normally for effects that deal no damage on a successful save, $$\d_\save = 0$$, a change in the save DC of $$\Delta \DC$$ changes the average damage taken by $$\Delta \D = \D_\fail \cdot \Delta \DC / 20$$. Using this, along with Eqns. \eqref{eq:save-damage} and \eqref{eq:save-damage-dis}, the effective change in DC from having disadvantage on a saving throw is,
\begin{align}
    %\Dave_\dis &= \D_\fail \left( 1 - \d_\save \right) \p_\fail \left( 1 - \p_\fail \right) \,.
    \Delta \DC_\dis &= 20 \, \left( 1 - \d_\save \right) \p_\fail \left( 1 - \p_\fail \right) \,.
    %\Delta \DC_\dis &= 20 \, \p_\fail \left( 1 - \p_\fail \right) \,.
    \label{eq:save-delta-dc-dis}
\end{align}

Figure <a href="#fig:delta-dc-disadvantage" class="fig-ref">2</a> (below) plots Eqn. \eqref{eq:save-delta-dc-dis} for the case where $$\d_\save = 0$$ as well as for $$\d_\save = 0.5$$. For both, the maximum save DC bonus comes when $$\p_\fail = 0.5$$. The effective increase in save DC is larger for saving throws where $$\d_\save = 0$$ due to the starting damage being lower relative to the maximum damage.

<figure id="fig:delta-dc-disadvantage">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/valuing-conditions/fig-delta-dc-disadvantage.svg">
    <figcaption>Figure 2: Effective save DC increase from disadvantage on saving throws as a function of the saves normal chance to fail.</figcaption>
</figure>

For the baseline probability of failing saving throws of $$\p_\fail = 0.65$$, having disadvantage gives an effective DC increase of $$\Delta \DC = +4.5$$ when $$\d_\save = 0$$, and $$\Delta \DC = +2.3$$ when $$\d_\save = 0.5$$. 

This increase in damage can also be expressed as a percent increase over the saving throw's normal damage,
\begin{align}
    \Delta \d_{\,\dis} &= \frac{ \D_\dis - \Dave }{ \Dave } \nonumber \\\\ 
                       &= \frac{ \left( 1 - \d_\save \right) \p_\fail \left( 1 - \p_\fail \right) }{ \left( 1 - \d_\save \right) \p_\fail + \d_\save } \,.
    \label{eq:save-delta-pct-dis} 
\end{align}

For $$\p_\fail = 0.65$$ and $$\d_\save = 0$$, Eqn. \eqref{eq:save-delta-pct-dis} gives a damage increase of $$35.0\%$$, and for $$\p_\fail = 0.65$$ and $$\d_\save = 0.5$$ it gives $$13.8\%$$. 

When compared to the change in effective save DC, the percent increase in damage for $$\d_\save = 0.5$$ appears low at first glance. However, it's worth noting that the base damage for $$\d_\save = 0.5$$ is $$27\%$$ higher than when $$\d_\save = 0$$, which wasn't used for when calculating $$\Delta \DC_\dis$$. This difference in average base damage is precisely why the rules for [creating spells](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#CreatingaSpell) in the DMG recommend increasing the damage of spells that deal no damage on a successful save by $$25\%$$.


## Automatically fail saving throws

For conditions that cause a target to automatically fail a saving throw, Eqn. \eqref{eq:save-damage-generic} simplifies to
\begin{align}
    \Dave_\mathrm{af} &= \D_\fail \,.
    \label{eq:save-damage-auto-fail}
\end{align}

The increase in damage from this is therefore
\begin{align}
    \Delta \Dave_\mathrm{af} &= \D_\fail \left( 1 - \d_\save \right) \left( 1 - \p_\fail \right) \,,
    \label{eq:save-delta-damage-auto-fail}
\end{align}

which translates into an effective change in DC of
\begin{align}
    \Delta \DC_\mathrm{af} &= 20 \left( 1 - \d_\save \right) \left( 1 - \p_\fail \right) \,.
    \label{eq:save-delta-DC-auto-fail}
\end{align}

For the baseline probability of failing saving throws of $$\p_\fail = 0.65$$, automatically failing a saving throw acts like an effective increase in save DC of $$\Delta \DC_\mathrm{af} = +7.0$$ when $$\d_\save = 0$$, and $$\Delta \DC_\mathrm{af} = +3.5$$ when $$\d_\save = 0.5$$.

Putting this in terms of a percent increase in damage yields,

\begin{align}
    \Delta \d_\mathrm{af} &= \frac{ \left( 1 - \d_\save \right) \left( 1 - \p_\fail \right) }{ \left( 1 - \d_\save \right) \p_\fail + \d_\save } \,,
    \label{eq:save-delta-pct-auto-fail} 
\end{align}

which gives a $$53.8\%$$ increase in damage when $$\d_\save = 0.0$$, and a $$21.2\%$$ increase in damage when $$\d_\save = 0.5$$.

## Inability to take actions

In simplest terms, when a creature is unable to take actions during a round, their damage output for that round drops to zero. For a baseline attack with $$\p_\hit = 0.60$$, $$\p_\crit=0.05$$, and $$\d_\crit = 1.5$$, this is equivalent to a $$\Delta \AB_\mathrm{na} = -13.5$$. For baseline saving throws with $$\p_\fail = 0.65$$, when $$\d_\save = 0$$ this is the same as $$\Delta \DC_\mathrm{na} = -13.0$$, and when $$\d_\save = 0.5$$ it's equivalent to $$\Delta \DC_\mathrm{na} = -16.5$$.

This description is a bit misleading, though, since the change in attack bonus and the change in DC for saves that deal half damage on a success aren't actually achievable in game. A better description is that the target experiences a change in damage of $$-100.0\%$$ (i.e., their damage goes to zero). When applied to a hostile creature, this benefit can be thought of as providing effective healing equal to $$100\%$$ of the damage the target would do while unable to take actions.

## Inability to move

Trying to assign a value to being unable to move is tricky. Unlike the other components, which each had a clear mechanical effect, this can only be evaluated by assuming how important movement is in combat. If being unable to move prevents a creature from attacking any targets, then it can be treated similarly to the inability to take actions from the previous section. However, how likely this is to occur isn't at all clear, and likely depends on the specific monster. For now, I won't be assigning any value to this condition component, but I will update this post if I come up with anything concrete.

As an interesting side note, the [Monster Features](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterFeatures) table from chapter 9 of the DMG gives the [orc's](https://www.dndbeyond.com/monsters/16972-orc) Aggressive feature, which allows them to double their speed as a bonus action, a value of +2 DPR, which translates into a $$21\%$$ increase in their DPR.

## Component summary <!-- omit in toc -->

Table <a href="#tab:condition-component-values" class="fig-ref">2</a> (below) provides a summary of the effects these components have on an affected target. I've presented each in terms of their offensive effect, but they can easily be swapped to defensive stats using $$\Delta \AB = - \Delta \AC$$, as well as $$\Delta \DC = - \Delta \SB$$.

<div class="dataframe center">
<h3 id="tab:condition-component-values">Table 2</h3>
<table border="0">
    <thead>
        <tr>
            <td style="text-align:left"><strong>Component</strong></td>
            <td style="width:33%"><strong>Effect on Target</strong></td>
            <td style="width:33%"><strong>Change in Damage</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Advantage on attack rolls</td>
            <td>+5 AB</td>
            <td>+37.2% dealt</td>
        </tr>
        <tr>
            <td style="text-align:left">Disadvantage on attack rolls</td>
            <td>-5 AB</td>
            <td>-37.2% dealt</td>
        </tr>
        <tr>
            <td style="text-align:left">Automatic crit on hit</td>
            <td>+6 AB</td>
            <td>+44.4% dealt</td>
        </tr>
        <tr>
            <td style="text-align:left">Disadvantage on saving throws</td>
            <td>-(2.3&#8211;4.5) SB</td>
            <td>+(13.8&#8211;35.0)% taken</td>
        </tr>
        <tr>
            <td style="text-align:left">Automatically fail saving throws</td>
            <td>-(3.5&#8211;7.0) SB</td>
            <td>+(21.2&#8211;53.8)% taken</td>
        </tr>
        <tr>
            <td style="text-align:left">Inability to take actions</td>
            <td>0 DPR</td>
            <td>-100% dealt</td>
        </tr>
        <tr>
            <td style="text-align:left">Inability to move</td>
            <td>-</td>
            <td>-</td>
        </tr>
    </tbody>
</table>
</div>

As a reminder, the range in the saving throw bonuses for having disadvantage on saving throws, and automatically failing saving throws, represents the difference between effects that deal half damage on successful saves and ones that deal no damage on successful saves.

# Conditions <!-- omit in toc -->

With values established for each of component, the value of each condition can be calculated by inserting the results of Table <a href="#tab:condition-component-values" class="fig-ref">2</a> into Table <a href="#tab:condition-components" class="fig-ref">1</a>. The results of this are summarized in Table <a href="#tab:condition-values" class="fig-ref">3</a> (below). As an example of how to read the table, the [stunned](https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Stunned) condition reduces the target's DPR to zero, grants an effective bonus of $$+5$$ to hit on attack rolls against the target, and an effective bonus of $$+3.5$$ to $$+7.0$$  to the save DC of any effects used against the target that require a Strength or Dexterity saving throw.

<div class="dataframe center" style="width:90%">
<h3 id="tab:condition-values">Table 3</h3>
<table border="0">
    <thead>
        <tr>
            <td style="border-bottom:0px"></td>
            <td style="border-bottom:0px" colspan="2"><strong>&#8211; From Target &#8211;</strong></td>
            <td style="border-bottom:0px" colspan="2"><strong>&#8211; Against Target &#8211;</strong></td>
        </tr>
        <tr>
            <td style="text-align:left"><strong>Condition</strong></td>
            <td><strong>Attacks</strong></td>
            <td><strong>Saves</strong></td>
            <td style="width:25%"><strong>Attacks</strong></td>
            <td style="width:25%"><strong>Saves</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Blinded</td>
            <td>-5 AB</td>
            <td>-</td>
            <td>+5 AB</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Charmed</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Deafened</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Frightened</td>
            <td>-5 AB</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Grappled</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Incapacitated</td>
            <td>0 DPR</td>
            <td>0 DPR</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Invisible</td>
            <td>+5 AB</td>
            <td>-</td>
            <td>-5 AB</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Paralyzed</td>
            <td>0 DPR</td>
            <td>0 DPR</td>
            <td>+11 AB</td>
            <td>+(3.5 &#8211; 7.0) DC (Str, Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Petrified</td>
            <td>0 DPR</td>
            <td>0 DPR</td>
            <td>-4.2 AB</td>
            <td>-(4.2 &#8211; 7.1) DC (Str, Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Poisoned</td>
            <td>-5 AB</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Prone</td>
            <td>-5 AB</td>
            <td>-</td>
            <td>+/-5 AB</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Restrained</td>
            <td>-5 AB</td>
            <td>-</td>
            <td>+5 AB</td>
            <td>+(2.3 &#8211; 4.5) DC (Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Stunned</td>
            <td>0 DPR</td>
            <td>0 DPR</td>
            <td>+5 AB</td>
            <td>+(3.5 &#8211; 7.0) DC (Str, Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Unconscious</td>
            <td>0 DPR</td>
            <td>0 DPR</td>
            <td>+11 AB</td>
            <td>+(3.5 &#8211; 7.0) DC (Str, Dex)</td>
        </tr>
    </tbody>
</table>
</div>

For the [petrified](https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Petrified) condition, the values in the Attacks Against Target and Saves Against Target columns were calculated by applying damage resistance to Eqns. \eqref{eq:attack-damage-adv} and \eqref{eq:save-delta-damage-auto-fail} and then using them to calculate $$\Delta \AB$$ and $$\Delta \DC$$ respectively.

The results in Table <a href="#tab:condition-values" class="fig-ref">3</a> are perhaps the most natural way of understanding the mechanical impact of each condition, but we're ultimately interested in how those translate into damage and healing. Table <a href="#tab:condition-values-edpr" class="fig-ref">4</a> (below) presents the data from Table <a href="#tab:condition-values" class="fig-ref">3</a> in terms of the percent change in damage the condition causes for both the target and anyone attempting to damage it.

<div class="dataframe center" style="width:90%">
<h3 id="tab:condition-values-edpr">Table 4</h3>
<table border="0">
    <thead>
        <tr>
            <td style="border-bottom:0px"></td>
            <td style="border-bottom:0px" colspan="2"><strong>&#8211; Damage From Target &#8211;</strong></td>
            <td style="border-bottom:0px" colspan="2"><strong>&#8211; Damage Against Target &#8211;</strong></td>
        </tr>
        <tr>
            <td style="text-align:left"><strong>Condition</strong></td>
            <td style="width:18%"><strong>Attacks</strong></td>
            <td style="width:18%"><strong>Saves</strong></td>
            <td style="width:20%"><strong>Attacks</strong></td>
            <td style="width:20%"><strong>Saves</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Blinded</td>
            <td>-37%</td>
            <td>-</td>
            <td>-37%</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Charmed</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Deafened</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Frightened</td>
            <td>-37%</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Grappled</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Incapacitated</td>
            <td>-100%</td>
            <td>-100%</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Invisible</td>
            <td>+37%</td>
            <td>-</td>
            <td>-37%</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Paralyzed</td>
            <td>-100%</td>
            <td>-100%</td>
            <td>+98%</td>
            <td>+(21&#8211;54)% (Str, Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Petrified</td>
            <td>-100%</td>
            <td>-100%</td>
            <td>-35%</td>
            <td>-(27&#8211;55)% (Str, Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Poisoned</td>
            <td>-37%</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Prone</td>
            <td>-37%</td>
            <td>-</td>
            <td>+37%</td>
            <td>-</td>
        </tr>
        <tr>
            <td style="text-align:left">Restrained</td>
            <td>-37%</td>
            <td>-</td>
            <td>+37%</td>
            <td>+(14&#8211;35)% (Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Stunned</td>
            <td>-100%</td>
            <td>-100%</td>
            <td>+37%</td>
            <td>+(21&#8211;54)% (Str, Dex)</td>
        </tr>
        <tr>
            <td style="text-align:left">Unconscious</td>
            <td>-100%</td>
            <td>-100%</td>
            <td>+98%</td>
            <td>+(21&#8211;54)% (Str, Dex)</td>
        </tr>
    </tbody>
</table>
</div>

When presented in this way, there are two big takeaways. First, the value of each condition depends on the damage the creatures involved are capable of. Since the average damage output of PCs (monsters) depends on their level (CR), the average strength of each condition must also depend on them. And second, since PCs and monsters deal different amounts of damage, even when their levels and CRs are matched, the value of each condition when used by monsters against PCs will be different than its value when used by PCs against monsters.

Both of these points are illustrated in Fig. <a href="#fig:dpr-stunned-illustrative" class="fig-ref">3</a> (below), which shows the average damage per round for PCs (monsters) across levels (CRs) 1 - 20, along with the estimated value of the stunned condition. The value of the stunned condition is determined by adding together the extra effective healing from the target, and extra damage against the target, for an encounter with a single monsters and four PCs. For illustrative purposes, I assumed an average damage increase of $$29\% = (37\% + 21\%)/2$$ against the stunned target, which comes from averaging the damage increase for attacks against the target and saves against the target that do half damage on a successful save.

<figure id="fig:dpr-stunned-illustrative">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/valuing-conditions/fig-dpr-stunned-illustrative.svg">
    <figcaption>Figure 3: Average DPR for monsters (PCs) as a function of CR (level), as well as average value in DPR of the stunned condition when used by monsters against a PC, and by a group of four PCs against a monster.</figcaption>
</figure>

In this example, it's clear that the strength of the stunned condition is significantly stronger when used by PCs against a single monster that it is when used by a monster against a single PC (at least when their levels and CR are matched). It's also worth noting that, for a PC, the stunned condition is worth significantly more than the average damage per round of a typical PC. This is a bit of an overestimation, though, since the average DPR factors in the PCs chance to hit their target, while the stunned condition doesn't factor in the chance of the target getting stunned. However, even after applying a baseline chance to land a saving throw of $$65\%$$, the value of the stunned condition in this example will still be significantly higher.


# Conclusion

When I first set out to look into this, I was hoping to arrive at harder number for each condition. However, given that the values of each condition depends on the levels and CR of the creatures involved, doing so isn't a simple task. While this post establishes a firm understanding of how each condition can be valued in terms of damage and/or healing, there is still more work that needs to be done to make it of practical use for balancing abilities, spells, and monsters.