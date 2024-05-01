---
title: "Effective HP and Damage"
excerpt: "How to represent creature defensive and offensive strengths in effective terms that don't require calculating chances to hit or save against an enemy creature."
permalink: /:collection/:name/
date: 2022-01-17
last_modified_at: 2024-04-30
tags:
  - theory
  - xp
---

{% include LaTex.html %}

<div style="display:none">
\(
% general
\newcommand{\ave}{\mathrm{a}}
\newcommand{\total}{\mathrm{t}}

% probability
\newcommand{\phit}{\rho_{\hit}}
\newcommand{\pcrit}{\rho_{\crit}}
\newcommand{\pmiss}{\rho_{\miss}}
\newcommand{\psave}{\rho_{\save}}
\newcommand{\pfail}{\rho_{\fail}}

\newcommand{\SBave}{\SB_{\ave}}
\newcommand{\eD}{\mathit{eD}}

% damage
\newcommand{\D}{\mathit{D}}
\newcommand{\Dave}{\D_{\ave}}
\newcommand{\DPR}{\mathit{DPR}}
\newcommand{\dpr}{\mathit{dpr}}
\newcommand{\dprvec}{\mathbf{dpr}}

% abilities
\newcommand{\arm}{\mathrm{armor}}
\newcommand{\str}{\mathrm{Str}}
\newcommand{\dex}{\mathrm{Dex}}
\newcommand{\con}{\mathrm{Con}}
\newcommand{\int}{\mathrm{Int}}
\newcommand{\wis}{\mathrm{Wis}}
\newcommand{\cha}{\mathrm{Cha}}

% attacks
\newcommand{\eAB}{\mathit{eAB}}
\newcommand{\ABp}{\mathit{AB}^{\,\prime}}
\newcommand{\ABpvec}{\mathbf{AB}^{\,\prime}}
\newcommand{\eAC}{\mathit{eAC}}
\newcommand{\ACp}{\mathit{AC}^{\,\prime}}
\newcommand{\ACpvec}{\mathbf{AC}^{\,\prime}}
\)
</div>

<!--
This is the first post in a series that will cover and expand upon what's in my paper "[Calculating XP and encounter difficulty in D&D 5e](https://drive.google.com/file/d/1VnvdnJYTIym1QNGvONWZkOFYgbFO66Bx/view?usp=sharing)".

I will be covering this material in a different order than how it was initially presented. This post covers the material found in the second section "Effective HP and DPR". 
-->

# Introduction

A common problem that pops up when trying to evaluate a creature’s defensive or offensive strength is that any calculations you make, outside of comparing pure hit points or damage, require a second creature to stand in as an opponent for comparison. 

For instance, if I want to calculate the average damage of an attack that has a +5 to hit and deals 10 damage, I also need to know the armor class of the creature being attacked. Once I have that armor class, the rest of the calculation is easy, but it would be great if there was a way calculating an effective damage for the attack using just the qualities of the attack.

In this post, I show how such effective hit points and effective damage can be calculated for two simple cases: attacks that deal damage with no additional effects, and saves that deal damage with no additional effects. Clearly, there are more complicated abilities in the game than these, but solving these simple cases will help lay the ground-work for handing those more complicated abilities later on.

# Derivation

In order for any effective hit points or effective damage formula to be practically useful they can't just be theoretical constructs, they also need to work for calculating real, measurable quantities. To ensure this, I'll be using the equation for one such measurable quantity as the basis of their derivation. Specifically, I'll be using the equation for calculating the average number of rounds it takes for an attacker to defeat a given enemy creature, 
\begin{align}
    N_{\rounds} &= \frac{\HP}{\DPR_{\ave}}\,.
    \label{eq:rounds-to-win}
\end{align}
where $$\HP$$ is the defending creature's hit points, and $$\DPR_{\ave}$$ is the attacker's average damage per round.

For attacks, $$\DPR_{\ave}$$ depends on both the targets armor class $$(\AC\,)$$ and the attacker's attack bonus $$(\AB\,)$$, and for saving throw effects it depends on the target's saving throw bonus $$(\SB\,)$$ and the attacker's save difficulty class $$(\DC\,)$$. In either case, the goal is to move all defensive terms to the numerator (top) and all offensive terms to the denominator (bottom). This means we want to rearrange things in the following way,
\begin{align}
    \frac{\HP}{\DPR_{\ave}(\AB, \AC, \DC, \SB\,)} \Rightarrow \frac{\eHP(\AC, \SB\,)}{\eDPR(\AB, \DC\,)}\,,
    \label{eq:separation-requirement}
\end{align}
where $$\eHP$$ is the target's effective hit points, and $$\eDPR$$ is the attackers effective damage per round.

I've broken up this derivation into three parts. The first two look at how the average damage is calculated for [simple attacks](#simple-attacks) and [simple saves](#simple-saves), and how these equations can be "re-centered" about the game's baseline chance to deal damage. The third then takes these re-centered average damage equations and uses them, along with Eqn. \eqref{eq:rounds-to-win}, to derive formulas for a creature's [effective hit points and damage per round](#effective-hit-points-and-damage-per-round).

<!--
# Method

In order for any effective hit points or effective damage formula to be practically useful they can't just be theoretical constructs, they also need to work for calculating real, measurable quantities. To ensure this, I'll be using the equation for one such measurable quantity as the basis of their derivation. Specifically, I'll be using the equation for calculating the average number of times a damaging ability needs to be used to defeat a given enemy creature, 
\begin{align}
    N &= \frac{\HP}{\Dave}\,.
    \label{eq:uses-to-win}
\end{align}
where $$\HP$$ is the defending creature's hit points, and $$\Dave$$ is the ability's average damage per use.

For attacks, $$\Dave$$ depends on both the targets armor class $$(\AC\,)$$ and the attacker's attack bonus $$(\AB\,)$$, and for saving throw effects it depends on the target's saving throw bonus $$(\SB\,)$$ and the attacker's save difficulty class $$(\DC\,)$$. In either case, the goal is to move all defensive terms to the numerator (top) and all offensive terms to the denominator (bottom). For attacks, this means we want to rearrange things in the following way,
\begin{align}
    N_\mathrm{attacks} = \frac{\HP}{\Dave(\AB, \AC\,)} \Rightarrow \frac{\eHP(\AC\,)}{\eD(\AB\,)}\,,
\end{align}
and for saving throw effects,
\begin{align}
    N_\mathrm{saves} = \frac{\HP}{\Dave(\DC, \SB\,)} \Rightarrow \frac{\eHP(\SB\,)}{\eD(\DC\,)}\,.
\end{align}
-->

## Simple attacks

<!--
To start, we first need to establish how $$\Dave$$ is calculated for attacks. 
-->

The average damage of an attack can be calculated as follows, 
\begin{align}
    \Dave &= \D_{\hit} \, \phit + \D_{\crit} \, \pcrit \,,
    \label{eq:attack-damage-average-abstract}
\end{align}
where $$\D_{\hit}$$ is the average damage of a hit, $$\D_{\crit}$$ is the average damage of a critical hit, $$\phit$$ is the probability of landing a hit, i.e., having the attack roll meet or exceed the target's $$\AC$$, 
\begin{equation}
    %\phit = \left(\frac{20 + \AB - \AC\,}{20}\right)\,,
    \phit = 0.05\left(20 + \AB - \AC\,\right)\,,
    \label{eq:attack-hit-probability}
\end{equation}
and $$\pcrit$$ is the probability of landing a critical hit, i.e., rolling a natural 20 on the attack roll,
\begin{equation}
    %\pcrit = \left(\frac{1}{20}\right)\,.
    \pcrit = 0.05\,.
    \label{eq:attack-crit-probability}
\end{equation}

Because rolling a natural 1 on an attack roll always results in a miss, and rolling a natural 20 always results in a critical hit, the results of Eqn. \eqref{eq:attack-hit-probability} are also bound between $$0.05 \le \phit \le 0.95$$.

If we plug Eqns. \eqref{eq:attack-hit-probability} and \eqref{eq:attack-crit-probability} into Eqn. \eqref{eq:attack-damage-average-abstract}, and if we assume a critical hit does the same damage as a regular hit, $$\D_{\crit} = \D_{\hit}$$, the average damage for an attack becomes
\begin{align}
    \Dave &= \D_{\hit} \, 0.05 \left(21 + \AB - \AC\,\right) \,.
    \label{eq:attack-damage-average-full}
\end{align}

To progress further, we'll need to rearrange Eqn. \eqref{eq:attack-damage-average-full} to take advantage of the fact that, as shown in Fig. <a href="#fig:attack-hit-probability-vs-level" class="fig-ref">1</a> (below), the average chance to deal damage with an attack against a level appropriate enemy is close to $$65\%$$ for both monsters and PCs.

<!--
\begin{align}
    \Dave &= \D_{\hit} \, 0.05 \left(22 + \AB - \AC\,\right) \nonumber \\\\ 
          &= \D_{\hit} \, 0.05 \left(13 + \left(9 + \AB - \AC\,\right)\right)  \nonumber \\\\ 
          &= \D_{\hit} \, 0.65 \, \left(1 + 0.077 \left(9 + \AB - \AC\,\right)\right)\,,
    \label{eq:attack-damage-average-full}
\end{align}
where $$0.077 \equiv 1/13$$. 

The form of Eqn. \eqref{eq:attack-damage-average-full} may seem odd at first glance, but it can be explained rather simply. 

As shown in Fig. <a href="#fig:attack-hit-probability-vs-level" class="fig-ref">1</a> (below), the average chance to hit with an attack against a level appropriate enemy is close to $$65\%$$ for both monsters and PCs. With this in mind, the term $$0.077\,(9 + \AB - \AC\,)$$ in Eqn. \eqref{eq:attack-damage-average-full} measures how much the attack's average damage deviates from that baseline.
-->

<figure id="fig:attack-hit-probability-vs-level">
    {% include_relative fig-attack-hit-probability-vs-level-small.html %}
    {% include_relative fig-attack-hit-probability-vs-level-large.html %}
    <figcaption>Figure 1: Shows the average chance to hit with an attack against a level appropriate target for monsters (blue) and PCs (orange). Monster \(\AB\) and \(AC\) values taken from chapter 9 of the DMG (p. 275). PCs were assumed to start with an attack modifier of +3 at 1st level that increases to +4 at 4th level and to +5 at 8th level, and \(\AC\) is averaged across all classes with minor armor improvements from purchasing better mundane gear, with no bonuses to their \(\AB\) or \(\AC\) from magic items.</figcaption>
</figure>

We can do so by rewriting Eqn. \eqref{eq:attack-damage-average-full} in the following way,
\begin{align}
    \Dave = \D_{\hit} \, 0.65 \left[1 + \left(\frac{ 8 + \AB - \AC\, }{ 13 }\right)\right]\,.
    \label{eq:attack-damage-average-centered}
\end{align}
This centers the equation around the observed $$65\%$$ average and uses the term $$(8 + \AB - \AC\,)/13$$ to measure how much this particular attack deviates away from that average. What makes this form useful is that these deviations are typically small relative to the average.

We'll come back to Eqn. \eqref{eq:attack-damage-average-centered} shortly, but before we progress any further, lets take a look at how the average damage for a save is calculated.

<!--
In this form, the term $$0.077\,(9 + \AB - \AC\,)$$ in Eqn. \eqref{eq:attack-damage-average-full} measures how much the attack's average damage deviates from that $$65\%$$ baseline chance for the attack to deal damage.
-->

<!--
The value of putting Eqn. \eqref{eq:attack-damage-average-full} in this form is that it allows us to take advantage of the following approximation, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which turns Eqn. \eqref{eq:attack-damage-average-full} into
\begin{align}
    \Dave \approx 0.65 \, \D_{\hit} \, 1.077^{\,9 + \AB - \AC}\,,
    \label{eq:attack-damage-average-exp}
\end{align}
where $$1.077 \equiv 14/13$$.

Putting Eqn. \eqref{eq:attack-damage-average-exp} back into our test equation, Eqn. \eqref{eq:uses-to-win}, gives
\begin{align}
    N_\mathrm{attacks} &= \frac{\HP}{\Dave(\AB, \AC\,)} \nonumber \\\\\\
      &\approx \frac{\HP}{0.65 \, \D_{\hit} \, 1.077^{\,9 + \AB - \AC}}\,,
    \label{eq:uses-to-win-attack}
\end{align}
and, since $$x^{a + b} = x^a\,x^b$$, we can finally move $$\AC$$ into the numerator,
\begin{align}
    N_\mathrm{attacks} &\approx \frac{\HP \, 1.077^{\AC - \AC_0}}{0.65 \, \D_{\hit} \, 1.077^{\AB + 1 - \AB_0}}\,.
\end{align}
Here, $$\AC_0$$ and $$\AB_0$$ are baseline values for a creature's armor class and attack bonus respectively, and the extra $$+1$$ in the exponent of the denominator (bottom) is there to separate out the extra damage dealt by critical hit. We have a lot of flexibility in what values we choose for these baselines, so long as they satisfy $$\AC_0 = 8 + \AB_0$$.

At this point our task is essentially done. We've successfully moved all the stats of the defending creature to the numerator, $$\HP$$ and $$\AC$$, and all the stats of the attacking creature in the denominator, $$\Dave$$ and $$\AB$$. The average number of attacks it takes the attacker to win can now be written in the form
\begin{align}
    N_\mathrm{attacks} \approx \frac{ \eHP \left(\HP,\AC\,\right)}{\eD \left(\D_{\hit}, \AB\,\right)}\,,
\end{align}
where $$\eHP$$ is the defending creature's effective hit points and $$\eD$$ is the attacking creature's effective damage, which are given by
\begin{align}
    \eHP_\mathrm{a} &= \frac{1}{\sqrt{0.65}} \, \HP \, 1.077^{\AC - 12}\,, \label{eq:effective-hit-points-attack} \\\\ 
    \eD_\mathrm{a}  &= \sqrt{0.65} \, \D_{\hit} \, 1.077^{\AB - 3}\,. \label{eq:effective-damage-attack}
\end{align}
Here, I've chosen $$\AB_0 = 4$$ and $$\AC_0 = 12$$, which satisfy our requirement that $$\AC_0 = 8 + \AB_0$$.

It's worth pointing out that while Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-damage-attack} do satisfied equation \eqref{eq:uses-to-win-attack}, they're not the only possible solutions. I chose $$\AC_0 = 12$$ because it's one less than the target $$\AC$$ of $$13$$ for a CR 1 monster from the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275), and $$\AB_0 = 4$$ to satisfy the requirement that $$\AC_0 = 8 + \AB_0$$. These, along with the factors of $$\sqrt{0.65}$$ in front of each equation, are particularly useful for calculating calculating creature XP values, as I discuss [here]({{ site.data.page-links.xp-and-encounter-balancing.path }}).
-->

## Simple saves

The average damage for a save can be calculated using the following formula,
\begin{equation}
    \Dave = \D_{\fail} \, \pfail + \D_{\save} \, \psave\,,
    \label{eq:save-damage-average-abstract}
\end{equation}
where $$\D_{\fail}$$ is the average damage from a failed saving throw, $$\D_{\save}$$ is the average damage from a successful saving throw, $$\pfail$$ is the probability of the target failing the saving throw, 
\begin{equation}
    \pfail = 0.05 \left(\DC - \SB - 1\,\right)\,,
    \label{eq:save-hit-probability}
\end{equation}
and $$\psave = 1 - \pfail$$ is the probability of the target succeeding. In order to avoid negative probabilities, the results of Eqn. \eqref{eq:save-hit-probability} are also bound between $$0 \le \pfail \le 1$$.

Assuming the save deals no damage on a successful saving throw, $$\D_{\save} = 0$$, Eqn. \eqref{eq:save-damage-average-abstract} becomes
\begin{align}
    \Dave &= \D_{\fail} \, 0.05 \left(\DC - \SB - 1\,\right)\,.
    \label{eq:save-damage-average-none-full}
\end{align}

Just as in the previous section for attacks, in order to progress further we'll need to rearrange Eqn. \eqref{eq:save-damage-average-none-full} to take advantage of the fact that, as shown in Fig. <a href="#fig:save-hit-probability-vs-level" class="fig-ref">2</a> (below), the average chance of a level appropriate target failing a saving throw is close to $$65\%$$ for both monsters and PCs.

<!--
Assuming the effect deals no damage on a successful save, $$\D_{\save} = 0$$, then \eqref{eq:save-damage-average-abstract} simplifies to
\begin{align}
    \Dave &= \D_{\fail} \, 0.05 \left(\DC - \SB - 1\,\right) \nonumber \\\\ 
          &= \D_{\fail} \, 0.05 \left(13 + \left(\DC - \SB - 14\,\right)\right) \nonumber \\\\ 
          &= \D_{\fail} \, 0.65 \left(1 + 0.077 \left(\DC - \SB - 14\,\right)\right)\,,
    \label{eq:save-damage-average-none-full}
\end{align}
where $$0.077 \equiv 1/13$$.

Just as in the previous section for attacks, the form of Eqn. \eqref{eq:save-damage-average-none-full} was chosen to take advantage of the fact that the average chance for a level appropriate target to fail a saving throw is close to $$65\%$$, as shown in Fig. <a href="#fig:save-hit-probability-vs-level" class="fig-ref">2</a> (below).
-->

<figure id="fig:save-hit-probability-vs-level">
    {% include_relative fig-save-hit-probability-vs-level-small.html %}
    {% include_relative fig-save-hit-probability-vs-level-large.html %}
    <figcaption>Figure 2: Shows the average chance to hit with a saving throw against a level appropriate target for monsters (blue) and PCs (orange). Monster \(\DC\) values taken from chapter 9 of the DMG (p. 275) and \(\SB\) were averaged from published monsters. PCs were assumed to start with a save modifier of +3 at 1st level that increases to +4 at 4th level and to +5 at 8th level, and \(\SB\) is averaged across all classes and monsters, with no bonuses to their \(\DC\) or \(\SB\) from magic items.</figcaption>
</figure>

This can be done in a similar fashion to what we did for attacks by rewriting Eqn. \eqref{eq:save-damage-average-none-full} to be centered around that baseline chance of $$65\%$$ in the following way,
\begin{align}
    \Dave &= \D_{\fail} \, 0.65 \left[1 + \left(\frac{ \DC - \SB - 14 }{ 13 }\right)\right] ,
    \label{eq:save-damage-average-none-centered}
\end{align}
where now the term $$\left(\DC - \SB - 14\right)/13$$ represents a small deviation away from that average.

With both of our average damage equations written in this way, we're ready to move on to the general case and deriving our equations for $$\eHP$$ and $$\eDPR$$.

<!--
And, since $$0.077 \ll 1$$ we can once again use the approximation $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, to arrive at the equation's final form,
\begin{align}
    \Dave &\approx 0.65 \, \D_{\fail} \, 1.077^{\DC - \SB - 14}\,,
    \label{eq:save-damage-average-none-exp}
\end{align}
where $$1.077 \equiv 14/13$$.

Calculating the number of times a creature needs to use their saving throw effect in order to defeat another creature gives
\begin{align}
    N \approx \frac{\HP \, 1.077^{\SB - \SB_0}}{ 0.65 \, \D_{\fail} \, 1.077^{\DC - \DC_0}}\,,
    \label{eq:saves-to-win-none}
\end{align}
where $$\SB_0$$ and $$\DC_0$$ are baseline values for a creature's saving throw bonus and ability difficulty class respectively, that must satisfy the relationship $$\DC_0 = \SB_0 + 14$$.

This can also be expressed in terms of $$\eHP$$ and $$\eD$$ using the following definitions,
\begin{align}
    \eHP_\mathrm{s} &= \frac{1}{\sqrt{0.65}} \, \HP  \, {1.077}^{\SB + 2}\,, \label{eq:effective-hit-points-save} \\\\ 
    \eD_\mathrm{s}  &= \sqrt{0.65} \, \D_{\fail} \, {1.077}^{\DC - 12}\,. \label{eq:effective-damage-save}
\end{align}

Just like in the previous section with attacks, I chose $$\DC_0 = 12$$ because it's one less than the target $$\DC$$ for a CR 1 monster listed in the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275), and $$\SB_0 = -2$$ because it satisfies the requirement that $$\DC_0 = \SB_0 + 14$$. 

It's worth noting that the DMG doesn't actually list recommended values for $$\SB$$, which is an unfortunate oversight, but the suggested minimum value presented here of $$\SB_0 = -2$$ is significant, as I'll discuss later on in this post.
-->

## Effective hit points and damage per round

With the results of the previous two sections under our belts, lets move on to the task at hand of calculating $$\DPR_{\ave}$$ for our attacker.

<!--
\begin{align}
    \DPR_{\ave} =& 
        \sum_{i=1}^{N_{\attack}} \D_{\ave} \left( \D_{i}, \AB_{i}, \AC_{i} \right)  \nonumber \\\\ 
        &+ \sum_{i=1}^{N_{\save}} \D_{\ave} \left( \D_{i}, \DC_{i}, \SB_{i} \right) 
\end{align}

With simple cases out of the way, lets now look at a more realistic, and slightly more complex scenario where a mix of attacks and saves are used to deal damage to a target, such as when calculating a monster's average damage per round when determining their challenge rating.
-->

To make this task a bit simpler, note that our average damage equations, Eqns. \eqref{eq:attack-damage-average-centered} and \eqref{eq:save-damage-average-none-centered}, have the same general form and can be written in the following way,
\begin{align}
    \D_{\ave}  &= 0.65 \, \D \left[1 + \left( \frac{ \ABp - \ACp }{ 13 } \right)\right] .
    \label{eq:mixed-damage-average-basic}
\end{align}
Here, $$\D$$ represents the average damage dealt on a hit for an attack or on a failed saving throw for a save. The variable $$\ABp$$ is the normalized offensive stat used to determine whether damage is dealt or not,
\begin{equation}
    \ABp = 
    \begin{cases} 
        \AB - \AB_{0} & \mathrm{for\ attacks}\,, \\\\ 
        \DC - \DC_{0} & \mathrm{for\ saves}\,, 
    \end{cases}
\end{equation}
where $$\AB_{0} = 4$$ and $$\DC_{0} = 12$$ represent common baseline values for attack bonus and save difficulty class. And the variable $$\ACp$$ is the corresponding normalized defensive stat that the damage targets,
\begin{equation}
    \ACp = 
    \begin{cases} 
        \AC - \AC_{0} & \mathrm{for\ attacks}\,, \\\\ 
        \SB \, - \SB_{0} & \mathrm{for\ saves}\,,
    \end{cases}
    \label{eq:generic-armor-class-relative}
\end{equation}
where $$\AC_{0} = 12$$ and $$\SB_{0} = -2$$ represent common baseline values for armor class and saving throw bonus.

**Note.** The values use here for $$\AB_{0}$$, $$\AC_{0}$$, $$\DC_{0}$$, and $$\SB_{0}$$ are not the only options I could have chosen. Equations \eqref{eq:attack-damage-average-centered} and \eqref{eq:save-damage-average-none-centered} only require $$\AB_{0} + 8 = \AC_{0}$$ and $$\SB_{0} + 14 = \DC_{0}$$. To get these specific values, I also used the fact that $$\AB + 8 = \DC$$ for spellcasters, and that $$\AB \approx 4$$ on average for [CR 1 monsters]({{ site.data.page-links.baseline-monster-stats.path }}/#fig:ab-vs-cr). 
{: .notice--warning}

<!--
**Note.** The values use here for $$\AB_{0}$$, $$\AC_{0}$$, $$\DC_{0}$$, and $$\SB_{0}$$ are not the only options I could have chosen. Equations \eqref{eq:attack-damage-average-centered} and \eqref{eq:save-damage-average-none-centered} only require $$\AB_{0} + 8 = \AC_{0}$$ and $$\SB_{0} + 14 = \DC_{0}$$. To get these specific values, I also used the fact that $$\AB + 8 = \DC$$ for spellcasters, and that $$\AB \approx 4$$ on average for [CR 1 monsters]({{ site.data.page-links.baseline-monster-stats.path }}/#fig:ab-vs-cr). This effectively puts each normalized offensive and defensive stat on the same scale. Meaning $$\ABp = 5$$ is equally good for the attacker as $$\ACp = 5$$ is for the defender relative to the baseline chance to deal damage of $$65\%$$.
{: .notice--warning}
-->

With this generalized average damage equation in hand, determining $$\DPR_{\ave}$$ for any attacker is simply a matter of calculating the average damage per round for each of their attacks or saves individually using Eqn. \eqref{eq:mixed-damage-average-basic}, and then adding them all together,
\begin{align}
    \DPR_{\ave}  &= \sum_{i = 1}^{N} 0.65 \, \DPR_{i} \left[1 + \left( \frac{ \ABp_{i} - \ACp_{i} }{ 13 }\right)\right] .
    \label{eq:mixed-damage-average-1}
\end{align}
Here, $$N$$ is the number of abilities used by the creature to deal damage during combat. For each ability, $$\DPR$$ is the average damage per round dealt when the ability deals damage, $$\ABp$$ is the offensive stat used to determine if the ability deals damage, and $$\ACp$$ is the corresponding defensive stat being targeted.

If we take the total damage per round, assuming all abilities successfully deal damage, $$\DPR_{\total} = \sum \DPR_{i}$$, and factor it out of the summation, Eqn. \eqref{eq:mixed-damage-average-1} becomes,
\begin{align}
    \DPR_{\ave} 
        &= 0.65 \, \DPR_{\total} \sum_{i = 1}^{N} dpr_{i} \left[1 + \left( \frac{ \ABp_{i} - \ACp_{i} }{ 13 } \right)\right] \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \left[1 +  \sum_{i = 1}^{N} dpr_{i} \left( \frac{ \ABp_{i} - \ACp_{i} }{ 13 } \right) \right] \,,
    \label{eq:mixed-damage-average-2}
\end{align}
where $$\dpr = \DPR/\DPR_{\total}\,$$ is the fraction of $$\DPR_{\total}$$ dealt by an ability, and that $$\sum \dpr_{i} = 1$$.

The summation in Eqn. \eqref{eq:mixed-damage-average-2} can also be expressed in a slightly more condensed way through the following vector equation,
\begin{align}
    \sum_{i = 1}^{N} dpr_{i} \left(\ABp_{i} - \ACp_{i}\right)
        = \dprvec \cdot \left( \ABpvec - \ACpvec \right) \,,
    \label{eq:sum-as-dot-products}
\end{align}
which takes the [dot product](https://en.wikipedia.org/wiki/Dot_product) (scalar product) between the vector $$\dprvec$$ and the vectors $$\ABpvec$$ and $$\ACpvec$$, 
\begin{align}
    \dprvec &= \left[ \dpr_{1},\, \dpr_{2},\, \cdots,\, \dpr_{N}  \right] \,; \\\\ 
    \ABpvec &= \left[ \ABp_{1},\, \ABp_{2},\, \cdots,\, \ABp_{N}  \right] \,; \\\\ 
    \ACpvec &= \left[ \ACp_{1},\, \ACp_{2},\, \cdots,\, \ACp_{N}  \right] \,.
\end{align}
Each of these vectors has $$N$$ elements, one for each of of the attacker's damage dealing abilities.

Substituting Eqn. \eqref{eq:sum-as-dot-products} into Eqn. \eqref{eq:mixed-damage-average-2} gives, 
\begin{align}
    \DPR_{\ave} = 0.65 \, \DPR_{\total} \left[1 +  \frac{ \dprvec \cdot \left( \ABpvec - \ACpvec \right) }{ 13 } \right].
    \hspace{-.8em}
    \label{eq:mixed-damage-average-3}
\end{align}

From here, we can take advantage of the fact that $$1/13 \approx 0.077 \ll 1$$ to apply the following approximation to Eqn. \eqref{eq:mixed-damage-average-3}, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which results in
\begin{equation}
    \DPR_{\ave} \approx 0.65 \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \left( \ABpvec - \ACpvec \right)} ,
    %\DPR_{\ave} \approx 0.65 \, \DPR_{\total} \left(\frac{14}{13}\right)^{\,\dprvec \cdot \left( \ABpvec - \ACpvec \right)} ,
    \label{eq:mixed-damage-average-exp}
\end{equation}
where $$1.077 \approx 1 + 1/13$$. 

In this form, we're finally ready to construct our test equation, Eqn. \eqref{eq:rounds-to-win}, and separate out the offensive and defensive terms. Substituting Eqn. \eqref{eq:mixed-damage-average-exp} for $$\DPR_{\ave}$$ in Eqn. \eqref{eq:rounds-to-win} gives
\begin{align}
    N_{\rounds} \approx \frac{\HP }{0.65 \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \left( \ABpvec - \ACpvec \right)}} ,
\end{align}
where $$\HP$$ is the defender's hit points. Since $$x^{a + b} = x^a\,x^b$$, we can move $$\ACpvec$$ into the numerator, yielding
\begin{align}
    N_{\rounds} \approx \frac{\HP \cdot 1.077^{\,\dprvec \cdot \ACpvec}}{0.65 \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \ABpvec}} .
\end{align}

This successfully separates puts our equation for $$N_{\rounds}$$ into the form described by Eqn. \eqref{eq:separation-requirement}, allowing us to construct $$\eHP$$ and $$\eDPR$$ as follows,
\begin{align}
    \eHP  &= \frac{1}{\sqrt{0.65}} \, \HP \, 1.077^{\,\eAC - \AC_{0}} \,, \label{eq:effective-hit-points-mix} \\\\ 
    \eDPR &= \sqrt{0.65} \, \DPR_{\total} \, 1.077^{\,\eAB - \AB_{0}} \,. \label{eq:effective-damage-mix}
\end{align}
Here, $$\eAC$$ is the creature's effective armor class,
\begin{align}
    \eAC &= \dprvec \cdot \ACpvec + \AC_{0} ,
    \label{eq:effective-armor-class}
\end{align}
which represents the weighted average of the defender's normalized defensive stats, expressed in terms of an equivalent armor class value.
And $$\eAB$$ is the creature's effective attack bonus,
\begin{align}
    \eAB &= \dprvec \cdot \ABpvec + \AB_{0} ,
    \label{eq:effective-attack-bonus}
\end{align}
which is just the weighted average of the attacker's offensive stats, expressed in terms of an equivalent attack bonus value.

**Note.** The choice to split the factor of $$0.65$$ between $$\eHP$$ and $$\eDPR$$ was a stylistic one that proves useful when discussing how [XP is calculated]({{ site.data.page-links.xp-and-encounter-balancing.path }}).
{: .notice--warning}

Before concluding this derivation, it's worth noting that, while we were able to successfully split $$\AB$$ and $$\DC$$ from $$\AC$$ and $$\SB$$, our formula for $$\eAC$$, Eqn. \eqref{eq:effective-armor-class}, still contains $$\dprvec$$ which comes from the attacker. To get around this, instead of using a specific attacker's $$\dprvec$$ when calculating $$\eAC$$, we can define a "universal" attack vector $$\dprvec_{\mathrm{u}}$$ that represents the average of what the defender might see across a broad range of attackers, and use that for calculating $$\eAC$$.

At this time, it's unclear what the exact form of $$\dprvec_{\mathrm{u}}$$ should to be. The "[Creating a Monster](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop/#CreatingaMonster)" section from chapter 9 of the DMG covers how to adjust a creature's $$\AC$$ to account for their saving throw proficiencies and any traits saving throw related traits they might have. This _could_ work as a stand in for an $$\eAC$$ calculated using $$\dprvec_{\mathrm{u}}$$, but since the DMG's method for adjusting $$\AC$$ is almost certainly an approximation this isn't an ideal solution.



<!--
Need a better way of making this transition...
Should this be in the discussion section?

Lets integrate these directly into the eHP and eDPR equations and define them right afterwards. Will still need a bit explaining the problem with eAC as it's currently defined.
-->

<!--
The exponent in Eqn. \eqref{eq:effective-damage-mix}, $$\dprvec \cdot \ABpvec,$$ is just the weighted average of the normalized attack bonuses for each ability in our $$\DPR_{\ave}$$ calculation. As such, it can be though of as an effective attack bonus $$(\eAB\,)$$, where
\begin{align}
    \eAB &= \dprvec \cdot \ABpvec + \AB_{0} .
    \label{eq:effective-attack-bonus}
\end{align}

Similarly, the exponent in Eqn. \eqref{eq:effective-hit-points-mix}, $$\dprvec \cdot \ACpvec,$$ is just the weighted average of our defender's normalized defensive stats, allowing us to define an effective armor class as
\begin{align}
    \eAC &= \dprvec_{\mathrm{u}} \cdot \ACpvec + \AC_{0}\,.
    \label{eq:effective-armor-class}
\end{align}
-->

<!--
Looking at Eqn. \eqref{eq:effective-hit-points-mix}, one might be tempted to define an effective armor class $$(\eAC\,)$$ in a similar way, but there is a subtle problem with this approach. The $$\eHP$$ described by Eqn. \eqref{eq:effective-hit-points-mix} is calculated from $$\dprvec$$, which comes from the attacker, and is therefore not solely dependent on the defending monster stats.

To get around this, we can define a universal attack vector, $$\dprvec_{\mathrm{u}}$$ and use it when determining a creature's effective armor class,
\begin{align}
    \eAC &= \dprvec_{\mathrm{u}} \cdot \ACpvec + \AC_{0}\,.
    \label{eq:effective-armor-class}
\end{align}
I won't get into the exact form of $$\dprvec_{\mathrm{u}}$$ at this time (though, I hope to at some point in the near future), but, for now, think of it as the average attack vector the defender is likely see across a wide range of attackers. In the mean time, we can simply use the effective armor class defined in chapter 9 of the DMG as a proxy for calculating $$\eAC$$ using Eqn. \eqref{eq:effective-armor-class}.


As a final step, we can take advantage of the fact that the number of defensive stats is fixed at seven for each creature (i.e., their armor class and six saving throw bonuses), and rewrite $$\dprvec_{\mathrm{u}}$$ and $$\ACpvec$$ in terms of these seven stats rather than for an arbitrary number of damage sources, 
\begin{align}
    \dprvec &= \left[ \dpr_{\arm}, \dpr_{\str}, \cdots, \dpr_{\cha}  \right] \,; \\\\ 
    \ACpvec &= \left[ \ACp_{\arm}, \ACp_{\str}, \cdots, \ACp_{\cha} \right] \,.
\end{align}
Now each $$\dpr$$ represents the relative damage targeting each defensive stat, instead of the relative damage of each ability, and $$\ACp$$ is defined by Eqn. \eqref{eq:generic-armor-class-relative}.
-->

# Discussion

Now that we've derived equations for effective hit points and effective damage, I'd like to spend some time discussing what they mean and where to go from here.

## Linear approximation

For some, the form of Eqns. \eqref{eq:effective-hit-points-mix} and \eqref{eq:effective-damage-mix} can be a bit intimidating due to their exponential nature. For those wanting more linear equations for effective hit points and effective health, the same approximation used previously can be used in reverse, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, resulting in the following,
\begin{align}
    \eHP  &\approx \frac{1}{\sqrt{0.65}} \, \HP \left[ 1 +  \left( \frac{ \eAC - \AC_{0} }{ 13 } \right) \right] , \label{eq:effective-hit-points-mix-approx} \\\\ 
    \eDPR &\approx \sqrt{0.65} \, \DPR_{\total} \left[ 1 + \left( \frac{ \eAB - \AB_{0} }{ 13 } \right) \right] . \label{eq:effective-damage-mix-approx}
\end{align}

It should be noted, however, that while this works well for low CR creatures, at higher CRs this approach will introduce minor errors due to the exclusion of higher order terms in the approximation.

Another small adjustment that some may find useful is to multiply both of the above equations by $$\sqrt{0.65}$$. This removes the prefactor from Eqn. \eqref{eq:effective-hit-points-mix-approx} and also removes the square root from Eqn. \eqref{eq:effective-damage-mix-approx}. As I mentioned before, the choice to split the factor of $$0.65$$ between the two terms was a stylistic one that proves useful when discussing how [XP is calculated]({{ site.data.page-links.xp-and-encounter-balancing.path }}).

<!--
eq:effective-hit-points-attack-approx: legendary resistances
-->
<!--
resulting in the following for attacks,
\begin{align}
    \eHP_\mathrm{a} &\approx \frac{1}{\sqrt{0.65}} \cdot \HP \left( 1 + 0.077 \left(\AC - 12\right)\right)\,, \label{eq:effective-hit-points-attack-approx} \\\\ 
    \eD_\mathrm{a}  &\approx \sqrt{0.65} \cdot \D_{\hit} \left( 1 + 0.077 \left(\AB - 3\right)\right)\,, \label{eq:effective-damage-attack-approx}
\end{align}
and for saving throws,
\begin{align}
    \eHP_\mathrm{s} &\approx \frac{1}{\sqrt{0.65}} \cdot \HP  \left(1 + 0.077 \left(\SB + 2\right)\right)\,, \label{eq:effective-hit-points-save-approx} \\\\ 
    \eD_\mathrm{s}  &\approx \sqrt{0.65} \cdot \D_{\fail} \left(1 + 0.077\left(\DC - 12\right)\right)\,. \label{eq:effective-hit-points-save-approx}
\end{align}

It should be noted, however, that while this works well for low CR creatures, at higher CRs this approach will introduce minor errors due to the exclusion of higher order terms in the approximation.

Another small adjustment that some may find useful is to multiply all four of the above equations by $$\sqrt{0.65}$$. This removes the prefactor from Eqns. \eqref{eq:effective-hit-points-attack-approx} and \eqref{eq:effective-hit-points-save-approx}, and also removes the square root from Eqns. \eqref{eq:effective-damage-attack-approx} and \eqref{eq:effective-damage-save-approx}. As I mentioned before, the choice to split the factor of $$0.65$$ between the two terms was a stylistic one that proves useful when discussing how XP is calculated, which you can read about [here]({{ site.data.page-links.xp-and-encounter-balancing.path }}).
-->

## Saving throw bonus scaling

One important thing that these equations show is how saving throw bonuses should scale in comparison to $$\AC$$. The [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275) lists suggested values for monster's $$\HP$$, $$\AC$$, and $$\DC$$ but it doesn't list one for $$\SB$$.

However, if we compared equal values of $$\ACp$$ for attacks and saves, it becomes clear that $$\SB$$ should scale as $$\AC - 14$$. Comparing saving throw modifiers for published monsters against the baseline $$\AC$$ values from the "Monster Statistics by Challenge Rating" table in chapter 9 of the DMG, as shown in Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">3</a> (below), this is indeed the case. 

<figure id="fig:monster-save-modifier-trends">
    {% include_relative fig-monster-save-modifier-vs-cr-small.html %}
    {% include_relative fig-monster-save-modifier-vs-cr-large.html %}
    <figcaption>Figure 3: Shows average saving throw modifiers (proficiency bonus not included) and armor class for monsters from official source books. Monster \(\AC\) values taken from the "Monster Statistics by Challenge Rating" table in chapter 9 of the DMG (p. 275). </figcaption>
</figure>

For all abilities but Dexterity, monster saving throw modifiers follow similar trends to $$\AC - 14$$, and the average across all saving throws matches the trend for $$\AC - 14$$ almost exactly!

<!--
Figure <a href="#fig:monster-save-modifier-trends" class="fig-ref">3</a> (above) shows this relationship for published monsters (I've excluded saving throw proficiency bonuses here because the DMG has separate rules for how much they should be valued in terms of an adjusted $$\AC\,$$). The saving throw modifiers for monsters clearly show a similar trend to $$\AC - 14$$ for all abilities but Dexterity, which is reassuring, and the average across all saving throws matches the trend for $$\AC - 14$$ almost exactly!
-->

It's been well established that certain saving throws for monsters are weaker than others (see my post on [Monster Saving Throws]({{ site.data.page-links.monster-saving-throws.path }})). However, what hasn't been clear until now is whether the strong saving throws are overpowered or the weak saving throws are underpowered.

What Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> shows is that, for monsters, Strength and Constitution modifiers are generally stronger than baseline, Wisdom and Charisma are on target, Intelligence is slightly below baseline, and Dexterity starts out stronger than baseline at low CRs but becomes relatively weaker and weaker as CR increases.


<!--
## Putting it all together

As it stands now, we have two ways of calculating effective hit points and two ways of calculating effective damage. 

For damage, this doesn't pose any potential conflict. We can simply pick whichever equation best fits how are creature is dealing damage. If we wanted to calculate the effective damage per round $$(\eDPR)$$ for a creature that deals damage using one attack and one saving throw effect, we can simply add the effective damage of the two together. Put more generally,
\begin{align}
    \eDPR = \sum \eD_\mathrm{a} \left(\D_{\hit}, \AB\,\right)  + \sum \eD_\mathrm{s} \left(\D_{\fail}, \DC\,\right)\,,
    %\eDPR = \sqrt{0.65} \cdot \left( \sum \D_{\hit} \cdot 1.077^{\AB - 3}  + \sum \cdot \D_{\fail} \cdot {1.077}^{\DC - 12}\right)\,,
    \label{eq:effective-dpr-general}
\end{align}
where the first summation includes all of the attacks the creature is likely to use during the round, and the second summation includes all of the saving throw effects.

For hit points, however, this raises a difficult question. Which formulation, Eqn. \eqref{eq:effective-hit-points-attack} or \eqref{eq:effective-hit-points-save}, should we use to reflect a creature true defensive strength? The simple answer, of course, is to just average between the two, as was done previously to account for each ability score having its own saving throw bonus,
\begin{align}
    \eHP = \frac{1}{\sqrt{0.65}} \cdot \HP  \cdot {1.077}^{\frac{1}{2}\left(\AC - 12\right) + \frac{1}{2} \left(\SBave + 2\right)}\,.
    \label{eq:effective-hit-points-general}
\end{align}
This assumes that a creature is just as likely to be subjected to a damaging attack as they are a damaging saving throw effect, and that the saving throw effects target each of the creature's ability scores equally. Again, this may not be the best assumption, but how all this is weighted can easily be adjusted to account for differences discovered later on.

The exponent in Eqn. \eqref{eq:effective-hit-points-general} can also be used to define an effective armor class,
\begin{align}
    %\eAC = \frac{1}{2}\left(\AC + \SBave + 14\right)\,.
    \eAC = \frac{\AC + \SBave + 14}{2}\,.
\end{align}
-->

## Encounter specific effective hit points

The introduction of $$\dprvec_{\mathrm{u}}$$ in Eqn. \eqref{eq:effective-armor-class} effectively removes any information about the attacker from our $$eHP$$ calculation, but it also means $$\eHP$$ won't always reflect a creature's true toughness in combat, because that depends on their opponents' specific attack vector.

We can determine error this approach introduces for a specific monster by taking the ratio between their encounter specific effective hit points and their universal effective hit points,
\begin{align}
    \frac{ \eHP \left( \dprvec \right) }{ \eHP \left( \dprvec_{\mathrm{u}} \right) }  
        &= \frac{1.077^{\,\dprvec \cdot \ACpvec} }{ 1.077^{\, \eAC^{\,\prime}} } \nonumber \\\\ 
        &= 1.077^{\, \dprvec \cdot \left[ \ACpvec - \eAC^{\,\prime} \right] } \nonumber \\\\ 
        &\approx \dprvec \cdot \Delta \mathbf{eHP}
\end{align}
where $$\eAC^{\,\prime} = \eAC - \AC_{0}$$ and 
\begin{align}
    \Delta \mathbf{eHP}  =
    \begin{bmatrix}
        1.077^{\ACp_{\arm} - \eAC^{\,\prime}} \\\\ 
        1.077^{\ACp_{\str} - \eAC^{\,\prime}} \\\\ 
        \vdots \\\\ 
        1.077^{\ACp_{\cha} - \eAC^{\,\prime}}
    \end{bmatrix} 
    \,.
    \label{eq:relative-toughness-vector}
\end{align}

When the scalar product $$\dprvec \cdot \Delta \mathbf{eHP} > 1$$ the creature will be tougher than normal, and when $$\dprvec \cdot \Delta \mathbf{eHP} < 1$$ it will be weaker. 

The relative toughness vector $$\Delta \mathbf{eHP}$$ given by Eqn. \eqref{eq:relative-toughness-vector} can also be useful in assessing a creature's strengths and weaknesses. When any of the individual $$\ACp < 0$$ the corresponding $$\Delta \mathbf{eHP}$$ values will be less than 1, indicating the creature is weaker to damage that targets these defensive stats, and when $$\ACp > 0$$ they'll be greater than 1, indicating the creature is more resilient to damage targeting these stats.

### Example: Hezrou

As an example, let's look at how this plays out for a specific monster, the **[hezrou](https://www.dndbeyond.com/monsters/16922-hezrou)** shown in the stat block below.

<center>
{% include_relative hezrou.html %}
</center>

Following the rules in chapter 9 of the DMG, the hezrou has an effective AC of 21, which translates into $$\eAC^{\,\prime} = 9$$. Adding a $$+4$$ bonus to each of the hezrou's saving throws to account for the Magic Resistance trait and a $$+2$$ bonus to the hezrou's AC to account for its Stench trait, gives the hezrou the following relative toughness vector,
\begin{equation}
    \Delta \mathbf{eHP} = 
    \begin{bmatrix}
        \Delta \eHP_{\arm} \\\\ 
        \Delta \eHP_{\str} \\\\ 
        \Delta \eHP_{\dex} \\\\ 
        \Delta \eHP_{\con} \\\\ 
        \Delta \eHP_{\int} \\\\ 
        \Delta \eHP_{\wis} \\\\ 
        \Delta \eHP_{\cha}
    \end{bmatrix}
    =
    \begin{bmatrix}
        0.80 \\\\ 
        1.35 \\\\ 
        1.00 \\\\ 
        1.45 \\\\ 
        0.64 \\\\ 
        1.08 \\\\ 
        0.86
    \end{bmatrix} 
    \,.
\end{equation}

From this we can surmise that the hezrou is most resilient against Constitution saves, and that if a party were to exclusively target these saves the hezrou would be roughly $$45\%$$ tougher. Similarly, the hezrou is most vulnerable to saves that target Intelligence, and if a party were able to exclusively target that save the hezrou would be roughly $$36\%$$ easier.

<!--
For a party consisting of two martial characters and two spellcasters with an estimated $$\dprvec = [0.5, 0, 0.3, 0, 0.1, 0.1, 0]$$, the hezrou's XP would be $$87\%$$ of its normal value. If we use the listed XP value for a CR 8 monster this would drop the hezrou from $$3,900$$ XP to $$3,400$$ XP which is roughly halfway between a CR 7 and CR 8.
-->

# Conclusion
In this post I've shown how effective hit points and effective damage per round can be derived for creatures using the math underpinning how attacks and saves work in D&D 5th edition. These allow a creature's defensive and offensive strength to be calculated in absolute terms, without the need of a second creature for comparison. 

This process has also given rise to general equations for a creature's effective attack bonus and effective armor class. And it's given us greater insight into how strong monster saving throw bonuses are relative to their armor class, as well as how those saving throw bonuses should scale with monster challenge rating.

For further reading on how these tools can be used to further understand combat in D&D 5th edition, see [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}).

<!--
In this post I've shown how effective hit points and effective damage can be derived for creatures using the math underpinning how attacks and saving throws work in D&D 5th edition. These allow a creature's defensive and offensive strength to be calculated in absolute terms, without the need of a second creature for comparison. For damage, this allows both attacks and saving throw effects to be added together and weighted equally. And for hit points, this allows an overall defensive strength to be calculated that combines armor class as well as saving throw bonuses. 

In the process, I've also shown how monster ability score modifiers can be expected to scale with CR in a way similar to how the DMG recommends scaling armor class. 

For anyone who stuck through all that to the end, congratulations! Compared to many of my previous posts, this one doesn't contain that much in terms of useful insights into the game. But it does lay the ground work needed for much more to come.
-->