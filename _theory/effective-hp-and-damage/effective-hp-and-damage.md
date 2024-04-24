---
title: "Effective HP and Damage"
excerpt: "How to represent creature defensive and offensive strengths in effective terms that don't require calculating chances to hit or save against an enemy creature."
permalink: /:collection/:name/
date: 2022-01-17
last_modified_at: 2024-04-24
tags:
  - theory
  - xp
---

{% include LaTex.html %}

<div style="display:none">
\(
% general
\newcommand{\ave}{\mathrm{ave}}

% probability
\newcommand{\phit}{\rho_{\hit}}
\newcommand{\pcrit}{\rho_{\crit}}
\newcommand{\pmiss}{\rho_{\miss}}
\newcommand{\psave}{\rho_{\save}}
\newcommand{\pfail}{\rho_{\fail}}

\newcommand{\SBave}{\SB_\mathrm{ave}}
\newcommand{\eHPatck}{\eHP_\mathrm{a}}
\newcommand{\eHPsave}{\eHP_\mathrm{s}}
\newcommand{\eD}{\mathit{eD}}
\newcommand{\eDatck}{\eD_\mathrm{a}}
\newcommand{\eDsave}{\eD_\mathrm{s}}

% damage
\newcommand{\D}{\mathit{D}}
\newcommand{\Dave}{\D_\mathrm{ave}}
\newcommand{\Dhit}{\D_{\hit}} 
\newcommand{\Dcrit}{\D_{\crit}}
\newcommand{\Dsave}{\D_{\save}}
\newcommand{\Dfail}{\D_{\fail}}
\newcommand{\DPR}{\mathit{DPR}}
\newcommand{\dpr}{\mathit{dpr}}
\newcommand{\dprvec}{\mathbf{dpr}}

% abilities
\newcommand{\str}{\mathrm{Str}}
\newcommand{\dex}{\mathrm{Dex}}
\newcommand{\con}{\mathrm{Con}}
\newcommand{\int}{\mathrm{Int}}
\newcommand{\wis}{\mathrm{Wis}}
\newcommand{\cha}{\mathrm{Cha}}
\newcommand{\arm}{\mathrm{armor}}
% stats
\newcommand{\stat}{\mathit{s}}
\newcommand{\stats}{\mathit{S}}

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

In this post, I show how such effective hit points and effective damage can be calculated for two simple cases: attacks that deal damage with no additional effects, and saving throw effects that deal damage with no additional effects. Clearly, there are more complicated abilities in the game than these, but solving these simple cases will help lay the ground-work for handing those more complicated abilities later on.


# Method

In order for any effective hit points or effective damage formula to be practically useful, they can't just be theoretical constructs, they also need to work for calculating real, measurable quantities. To ensure this, I'll be using the equation for one such measurable quantity as the basis of their derivation. Specifically, I'll be using the equation for calculating the average number of times a damaging ability needs to be used to defeat a given enemy creature, 
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


## Simple attacks

To start, we first need to establish how $$\Dave$$ is calculated for attacks. The average damage of an attack can be calculate as follows, 
\begin{align}
    \Dave &= \Dhit \, \phit + \Dcrit \, \pcrit \,,
    \label{eq:attack-damage-average-abstract}
\end{align}
where $$\Dhit$$ is the average damage of a hit, $$\Dcrit$$ is the average damage of a critical hit, $$\phit$$ is the probability of landing a hit, i.e., having the attack roll meet or exceed the target's $$\AC$$, 
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

If we plug Eqns. \eqref{eq:attack-hit-probability} and \eqref{eq:attack-crit-probability} into Eqn. \eqref{eq:attack-damage-average-abstract}, and if we assume a critical hit does twice the damage of a regular hit, $$\Dcrit = 2\,\Dhit$$, the average damage for an attack becomes
\begin{align}
    \Dave &= \Dhit \, 0.05 \left(22 + \AB - \AC\,\right) \nonumber \\\\ 
          &= \Dhit \, 0.05 \left(13 + \left(9 + \AB - \AC\,\right)\right)  \nonumber \\\\ 
          &= \Dhit \, 0.65 \, \left(1 + 0.077 \left(9 + \AB - \AC\,\right)\right)\,,
    \label{eq:attack-damage-average-full}
\end{align}
where $$0.077 \equiv 1/13$$. 

The form of Eqn. \eqref{eq:attack-damage-average-full} may seem odd at first glance, but it can be explained rather simply. 

As shown in Fig. <a href="#fig:attack-hit-probability-vs-level" class="fig-ref">1</a> (below), the average chance to hit with an attack against a level appropriate enemy is close to $$65\%$$ for both monsters and PCs. With this in mind, the term $$0.077\,(9 + \AB - \AC\,)$$ in Eqn. \eqref{eq:attack-damage-average-full} measures how much the attack's average damage deviates from that baseline.

<figure id="fig:attack-hit-probability-vs-level">
    {% include_relative fig-attack-hit-probability-vs-level-small.html %}
    {% include_relative fig-attack-hit-probability-vs-level-large.html %}
    <figcaption>Figure 1: Shows the average chance to hit with an attack against a level appropriate target for monsters (blue) and PCs (orange). Monster \(\AB\) and \(AC\) values taken from chapter 9 of the DMG (p. 275). PCs were assumed to start with an attack modifier of +3 at 1st level that increases to +4 at 4th level and to +5 at 8th level, and \(\AC\) is averaged across all classes with minor armor improvements from purchasing better mundane gear, with no bonuses to their \(\AB\) or \(\AC\) from magic items.</figcaption>
</figure>

The value of putting Eqn. \eqref{eq:attack-damage-average-full} in this form is that it allows us to take advantage of the following approximation, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which turns Eqn. \eqref{eq:attack-damage-average-full} into
\begin{align}
    \Dave \approx 0.65 \, \Dhit \, 1.077^{\,9 + \AB - \AC}\,,
    \label{eq:attack-damage-average-exp}
\end{align}
where $$1.077 \equiv 14/13$$.

Putting Eqn. \eqref{eq:attack-damage-average-exp} back into our test equation, Eqn. \eqref{eq:uses-to-win}, gives
\begin{align}
    N_\mathrm{attacks} &= \frac{\HP}{\Dave(\AB, \AC\,)} \nonumber \\\\\\
      &\approx \frac{\HP}{0.65 \, \Dhit \, 1.077^{\,9 + \AB - \AC}}\,,
    \label{eq:uses-to-win-attack}
\end{align}
and, since $$x^{a + b} = x^a\,x^b$$, we can finally move $$\AC$$ into the numerator,
\begin{align}
    N_\mathrm{attacks} &\approx \frac{\HP \, 1.077^{\AC - \AC_0}}{0.65 \, \Dhit \, 1.077^{\AB + 1 - \AB_0}}\,.
\end{align}
Here, $$\AC_0$$ and $$\AB_0$$ are baseline values for a creature's armor class and attack bonus respectively, and the extra $$+1$$ in the exponent of the denominator (bottom) is there to separate out the extra damage dealt by critical hit. We have a lot of flexibility in what values we choose for these baselines, so long as they satisfy $$\AC_0 = 8 + \AB_0$$.

At this point our task is essentially done. We've successfully moved all the stats of the defending creature to the numerator, $$\HP$$ and $$\AC$$, and all the stats of the attacking creature in the denominator, $$\Dave$$ and $$\AB$$. The average number of attacks it takes the attacker to win can now be written in the form
\begin{align}
    N_\mathrm{attacks} \approx \frac{ \eHP \left(\HP,\AC\,\right)}{\eD \left(\Dhit, \AB\,\right)}\,,
\end{align}
where $$\eHP$$ is the defending creature's effective hit points and $$\eD$$ is the attacking creature's effective damage, which are given by
\begin{align}
    \eHPatck &= \frac{1}{\sqrt{0.65}} \, \HP \, 1.077^{\AC - 12}\,, \label{eq:effective-hit-points-attack} \\\\ 
    \eDatck  &= \sqrt{0.65} \, \Dhit \, 1.077^{\AB - 3}\,. \label{eq:effective-damage-attack}
\end{align}
Here, I've chosen $$\AB_0 = 4$$ and $$\AC_0 = 12$$, which satisfy our requirement that $$\AC_0 = 8 + \AB_0$$.

It's worth pointing out that while Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-damage-attack} do satisfied equation \eqref{eq:uses-to-win-attack}, they're not the only possible solutions. I chose $$\AC_0 = 12$$ because it's one less than the target $$\AC$$ of $$13$$ for a CR 1 monster from the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275), and $$\AB_0 = 4$$ to satisfy the requirement that $$\AC_0 = 8 + \AB_0$$. These, along with the factors of $$\sqrt{0.65}$$ in front of each equation, are particularly useful for calculating calculating creature XP values, as I discuss [here]({{ site.data.page-links.xp-and-encounter-balancing.path }}).

## Simple saving throws

For damaging effects that require saving throws, the derivation of effective hit points and effective damage follows a similar path. To start, $$\Dave$$ can be calculated for saving throws as 
\begin{equation}
    \Dave = \Dfail \, \pfail + \Dsave \, \psave\,,
    \label{eq:save-damage-average-abstract}
\end{equation}
where $$\Dfail$$ is the damage from a failed save, $$\Dsave$$ is the damage from a successful save, $$\pfail$$ is the probability of the target failing the saving throw, 
\begin{equation}
    %\pfail = \left(\frac{\DC - \SB - 1}{20}\right)\,,
    \pfail = 0.05\left(\DC - \SB - 1\,\right)\,,
    \label{eq:save-hit-probability}
\end{equation}
and $$\psave = 1 - \pfail$$ is the probability of the target succeeding. In order to avoid negative probabilities, the results of Eqn. \eqref{eq:save-hit-probability} are also bound between $$0 \le \pfail \le 1$$.

Assuming the effect deals no damage on a successful save, $$\Dsave = 0$$, then \eqref{eq:save-damage-average-abstract} simplifies to
\begin{align}
    \Dave &= \Dfail \, 0.05 \left(\DC - \SB - 1\,\right) \nonumber \\\\ 
          &= \Dfail \, 0.05 \left(13 + \left(\DC - \SB - 14\,\right)\right) \nonumber \\\\ 
          &= \Dfail \, 0.65 \left(1 + 0.077 \left(\DC - \SB - 14\,\right)\right)\,,
    \label{eq:save-damage-average-none-full}
\end{align}
where $$0.077 \equiv 1/13$$.

Just as in the previous section for attacks, the form of Eqn. \eqref{eq:save-damage-average-none-full} was chosen to take advantage of the fact that the average chance for a level appropriate target to fail a saving throw is close to $$65\%$$, as shown in Fig. <a href="#fig:save-hit-probability-vs-level" class="fig-ref">2</a> (below).

<figure id="fig:save-hit-probability-vs-level">
    {% include_relative fig-save-hit-probability-vs-level-small.html %}
    {% include_relative fig-save-hit-probability-vs-level-large.html %}
    <figcaption>Figure 2: Shows the average chance to hit with a saving throw against a level appropriate target for monsters (blue) and PCs (orange). Monster \(\DC\) values taken from chapter 9 of the DMG (p. 275) and \(\SB\) were averaged from published monsters. PCs were assumed to start with a save modifier of +3 at 1st level that increases to +4 at 4th level and to +5 at 8th level, and \(\SB\) is averaged across all classes and monsters, with no bonuses to their \(\DC\) or \(\SB\) from magic items.</figcaption>
</figure>

And, since $$0.077 \ll 1$$ we can once again use the approximation $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, to arrive at the equation's final form,
\begin{align}
    \Dave &\approx 0.65 \, \Dfail \, 1.077^{\DC - \SB - 14}\,,
    \label{eq:save-damage-average-none-exp}
\end{align}
where $$1.077 \equiv 14/13$$.

Calculating the number of times a creature needs to use their saving throw effect in order to defeat another creature gives
\begin{align}
    N \approx \frac{\HP \, 1.077^{\SB - \SB_0}}{ 0.65 \, \Dfail \, 1.077^{\DC - \DC_0}}\,,
    \label{eq:saves-to-win-none}
\end{align}
where $$\SB_0$$ and $$\DC_0$$ are baseline values for a creature's saving throw bonus and ability difficulty class respectively, that must satisfy the relationship $$\DC_0 = \SB_0 + 14$$.

This can also be expressed in terms of $$\eHP$$ and $$\eD$$ using the following definitions,
\begin{align}
    \eHPsave &= \frac{1}{\sqrt{0.65}} \, \HP  \, {1.077}^{\SB + 2}\,, \label{eq:effective-hit-points-save} \\\\ 
    \eDsave  &= \sqrt{0.65} \, \Dfail \, {1.077}^{\DC - 12}\,. \label{eq:effective-damage-save}
\end{align}

Just like in the previous section with attacks, I chose $$\DC_0 = 12$$ because it's one less than the target $$\DC$$ for a CR 1 monster listed in the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275), and $$\SB_0 = -2$$ because it satisfies the requirement that $$\DC_0 = \SB_0 + 14$$. 

It's worth noting that the DMG doesn't actually list recommended values for $$\SB$$, which is an unfortunate oversight, but the suggested minimum value presented here of $$\SB_0 = -2$$ is significant, as I'll discuss later on in this post.

<!--
The form of the effective hit points in Eqn. \eqref{eq:effective-hit-points-save} poses another interesting problem because every creature has six different values for $$\SB$$, one for each ability score. If we think of each ability score's $$\SB$$ value as representing a creatures defense against one avenue of effect, then their overall defense against saving throw effects can be represented by averaging across all ability scores,
\begin{align}
    \SBave = \sum \SB_i / 6\,, \label{eq:average-save-bonus} 
\end{align}
where the sum is carried out over all six ability scores. This may be a bit too simplistic of an approach, though, as not all ability scores are targeted equally by saving throw effects. However, it will do for the time being.
-->

<!--
## scratch

The average damage of an attack or a save can be calculated from
\begin{align}
    \D_{ave}  &= 
    \begin{cases} 
        0.65 \, \D \left[1 + 0.077 \left((\AB - \,\,\, 4) - (\AC - 12)\right)\right] & \mathrm{for\ attacks}\,; \\\\ 
        0.65 \, \D \left[1 + 0.077 \left((\DC - 12) - (\SB \, + \,\,\, 2)\right)\right] & \mathrm{for\ saves}\,. 
    \end{cases}
    %\label{eq:save-damage-average-none-exp}
\end{align}
These can be generalized into the following equation,
\begin{align}
    \D_{ave}  &= 0.65 \, \D \left[1 + 0.077 \left( \ABp - \ACp \,\right)\right]\,.
    %\label{eq:save-damage-average-none-exp}
\end{align}
where
\begin{equation}
    \ABp = 
    \begin{cases} 
        \AB - \,\,\, 4 & \mathrm{for\ attacks}\,, \\\\ 
        \DC - 12 & \mathrm{for\ saves}\, 
    \end{cases}\,;\quad
    \ACp = 
    \begin{cases} 
        \AC - 12 & \mathrm{for\ attacks}\,, \\\\ 
        \SB \, + \,\,\, 2 & \mathrm{for\ saves}\, 
    \end{cases}\,.
\end{equation}
-->

## Mixed case

With simple cases out of the way, lets now look at a more realistic, and slightly more complex scenario where a mix of attacks and saves are used to deal damage to a target, such as when calculating a monster's average damage per round when determining their challenge rating.

To simplify things a bit, note that Eqns. \eqref{eq:attack-damage-average-exp} and \eqref{eq:save-damage-average-none-exp} can both be written in the same general form,
\begin{align}
    \D_{\ave}  &= 0.65 \, \D \left[1 + 0.077 \left( \ABp - \ACp \right)\right]\,.
    \label{eq:mixed-damage-average-basic}
\end{align}
Here, $$\D$$ represents the average damage dealt on a hit for an attack or on a failed saving throw for a save, $$\ABp$$ is the offensive stat used to determine whether damage is dealt or not,
\begin{equation}
    \ABp = 
    \begin{cases} 
        \AB - \,\,\, 4 & \mathrm{for\ attacks}\,, \\\\ 
        \DC - 12 & \mathrm{for\ saves}\,, 
    \end{cases}
\end{equation}
and $$\ACp$$ is the corresponding defensive stat that the damage targets,
\begin{equation}
    \ACp = 
    \begin{cases} 
        \AC - 12 & \mathrm{for\ attacks}\,, \\\\ 
        \SB \, + \,\,\, 2 & \mathrm{for\ saves}\,.
    \end{cases}
    \label{eq:generic-armor-class-relative}
\end{equation}

<!--where for attacks $$\D = \Dhit$$, $$o = \AB - \AB_0$$, and $$d = \AC - \AC_0$$, and for saving throw $$\D = \Dfail$$, $$o = \DC - \DC_0$$, and $$d = \SB - \SB_0$$.-->

When determining a creature's average damage per round $$(\DPR_{\ave})$$, we can use Eqn. \eqref{eq:mixed-damage-average-basic} to calculate the average damage per round for each of their abilities individually and then simply add them all together, 
\begin{align}
    \DPR_{\ave}  &= \sum_{i = 1}^{N} 0.65 \, \DPR_{i} \left[1 + 0.077 \left(\,\ABp_{i} - \ACp_{i}\right)\right]\,,
    \label{eq:mixed-damage-average-1}
\end{align}
Here, $$N$$ is the number of abilities used by the creature to deal damage during combat. For each ability, $$\DPR$$ is the average damage per round dealt when the ability deals damage, $$\ABp$$ is the offensive stat used to determine if the ability deals damage, and $$\ACp$$ is the corresponding defensive stat being targeted.

If we take the total damage per round, assuming all abilities successfully deal damage, $$\DPR_{\total} = \sum \DPR_{i}$$, and factor it out of the summation, Eqn. \eqref{eq:mixed-damage-average-1} becomes,
\begin{align}
    \DPR_{\ave} 
        &= 0.65 \, \DPR_{\total} \, \sum_{i = 1}^{N} dpr_{i} \, \left[1 + 0.077 \left( \,\ABp_{i} - \ACp_{i} \right)\right] \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \, \left[1 +  0.077 \, \sum_{i = 1}^{N} dpr_{i} \, \left( \,\ABp_{i} - \ACp_{i} \right) \right] \,,
    \label{eq:mixed-damage-average-2}
\end{align}
where $$\dpr = \DPR/\DPR_{\total}\,$$ is the fraction of $$\DPR_{\total}$$ dealt by an ability, and that $$\sum \dpr_{i} = 1$$.

The summation in Eqn. \eqref{eq:mixed-damage-average-2} can also be expressed through the following vector equation,
\begin{align}
    \sum_{i = 1}^{N} dpr_{i} \, \left(\,\ABp_{i} - \ACp_{i}\right)
        = \dprvec \cdot \left( \ABpvec - \ACpvec \right) \,,
    \label{eq:sum-as-dot-products}
\end{align}
which takes the [dot product](https://en.wikipedia.org/wiki/Dot_product) (scalar product) between the vector $$\dprvec$$ and the vectors $$\ABpvec$$ and $$\ACpvec$$, where
\begin{align}
    \dprvec &= \left[ \dpr_{1}, \dpr_{2}, \cdots, \dpr_{N}  \right] \,; \\\\ 
    \ABpvec &= \left[ \ABp_{1}, \ABp_{2}, \cdots, \ABp_{N}  \right] \,; \\\\ 
    \ACpvec &= \left[ \ACp_{1}, \ACp_{2}, \cdots, \ACp_{N}  \right] \,.
\end{align}

<!--
\begin{equation}
    \mathbf{dpr} = 
    \begin{bmatrix}
    \begin{array}{l}
        \dpr_{1} \\\\ 
        \dpr_{2} \\\\ 
        \,\,\, \vdots \\\\ 
        \dpr_{N}
    \end{array}
    \end{bmatrix};\,
    \ABpvec = 
    \begin{bmatrix}
    \begin{array}{l}
        \ABp_{1} \\\\ 
        \ABp_{2} \\\\ 
        \,\,\, \vdots \\\\ 
        \ABp_{N}
    \end{array}
    \end{bmatrix};\,
    \ACpvec = 
    \begin{bmatrix}
    \begin{array}{l}
        \ACp_{1} \\\\ 
        \ACp_{2} \\\\ 
        \,\,\, \vdots \\\\ 
        \ACp_{N}
    \end{array}
    \end{bmatrix}\,.
\end{equation}
-->

<!--
which takes the dot product (scalar product) between the vector $$\mathbf{dpr}$$ and the vectors $$\ABpvec$$ and $$\ACpvec$$, where
\begin{gather}
    \mathbf{dpr} = \sum_{i = 1}^{N} dpr_{i} \, \hat{\mathbf{u}}\_{i}\,; \\\\ 
    \ABpvec   = \sum_{i = 1}^{N} \ABp_{i}   \, \hat{\mathbf{u}}\_{i}\,; \\\\ 
    \ACpvec   = \sum_{i = 1}^{N} \ACp_{i}   \, \hat{\mathbf{u}}\_{i}\,.
\end{gather}
The unit vector $$\hat{\mathbf{u}}$$ in each of these equations is used to indicate which attack/save each elements is associated with. The exact form of these vectors isn't important, so long as they satisfy the following relationship,
\begin{equation}
    \hat{\mathbf{u}}\_{i} \cdot \hat{\mathbf{u}}\_{j} = 
    \begin{cases} 
        1 & i = j\,; \\\\ 
        0 & i \ne j\,.
    \end{cases}
\end{equation}
-->

<!--
However, if you're having a hard time consider the following example of a creature that deals damage each round against their target in the following ways. 

1. An attack that deals 15 damage on average on a hit with an attack bonus of $$+8$$ against an armor class of 14. 
2. A DC 13 Dexterity saving throw for 25 damage on a failed save against a saving throw modifier of $$+3$$.
3. An attack that deals 10 damage on average on a hit with an attack bonus of $$+7$$ against an armor class of 14.

For these damage sources $$\mathbf{dpr} = \left[ 0.3, 0.5, 0.2 \right]$$, $$\ABpvec = \left[ 4, 1, 3 \right]$$, and $$\ACpvec = \left[ 2, 5, 2 \right]$$.
-->

<!--
Adding up the damage from each source gives $$\DPR_{\total} = 15 + 25 + 10 = 50$$, and
\begin{align}
    \mathbf{dpr} &= \left[ 0.3, 0.5, 0.2 \right] \,; \nonumber \\\\ 
    \ABpvec      &= \left[ 4, 1, 3 \right] \,; \nonumber \\\\ 
    \ACpvec      &= \left[ 2, 5, 2 \right] \,. \nonumber
\end{align}
-->

<!--
The summation in Eqn. \eqref{eq:mixed-damage-average-2} can be further simplified by expressing the summation as a dot product between vectors as follows,
\begin{align}
    \DPR_{\ave} 
        &= 0.65 \, \DPR_{\total} \, \left[1 +  0.077 \, \left( \mathbf{dpr} \cdot \left( \ABpvec - \ACpvec \right) \right) \right] \,,
    \label{eq:mixed-damage-average-3}
\end{align}
where
\begin{gather}
    \mathbf{dpr} = \sum_{i = 1}^{N} dpr_{i} \, \hat{\mathbf{s}}\_{i}\,; \\\\ 
    \ABpvec   = \sum_{i = 1}^{N} o_{i}   \, \hat{\mathbf{s}}\_{i}\,; \quad
    \ACpvec   = \sum_{s \in S}   d_{s}   \, \hat{\mathbf{s}}\_{s}\,.
\end{gather}
Since the number of defensive stats is fixed, $$\ACpvec$$ is constructed by summing over $$\stats \equiv \left\{ \arm, \str, \dex, \con, \int, \wis, \cha \right\}$$.
-->

<!--
The unit vector $$\hat{\mathbf{s}}$$ in each of these equations is used to indicate which of the defender's seven defensive stat is being targeted,
\begin{align}
    \stat \in \stats \equiv \left\\{ \arm, \str, \dex, \con, \int, \wis, \cha \right\\}\.
\end{align}
The exact form of these vectors isn't important, so long as they have the following properties:
\begin{equation}
    \hat{\mathbf{s}}\_{i} \cdot \hat{\mathbf{s}}\_{j} = 
    \begin{cases} 
        1 & i = j\,; \\\\ 
        0 & i \ne j\,. \\\\ 
    \end{cases}
\end{equation}
-->

Substituting Eqn. \eqref{eq:sum-as-dot-products} into Eqn. \eqref{eq:mixed-damage-average-2}, and once again using the approximation $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, results in
\begin{equation}
    \DPR_{\ave} \approx 0.65 \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \left( \ABpvec - \ACpvec \right)}\,.
    \label{eq:mixed-damage-average-exp}
\end{equation}

<!--
\begin{equation}
    \DPR_{\ave} = 0.65 \, \DPR_{\total} \, \left[1 +  0.077 \, \left( \dprvec \cdot \left( \ABpvec - \ACpvec \right) \right) \right] \,.
    \label{eq:mixed-damage-average-3}
\end{equation}
From here we can once again use approximation $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, to approximate $$\DPR_{ave}$$ as
\begin{equation}
    \DPR_{\ave} \approx 0.65 \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \left( \ABpvec - \ACpvec \right)}\,.
    \label{eq:mixed-damage-average-exp}
\end{equation}
-->

This is essentially the same form as Eqn. \eqref{eq:attack-damage-average-exp}, our approximation for the average damage from a simple attack. 

If we use Eqn. \eqref{eq:mixed-damage-average-exp} to calculate the average number of rounds it will take an attacker to defeat a target with $$\HP$$ hit points we get
\begin{align}
    N_{\mathrm{rounds}} 
        &= \frac{ \HP }{ \DPR_{\ave} } \nonumber \\\\ 
        &\approx \frac{\HP \cdot 1.077^{\,\dprvec \cdot \ACpvec}}{0.65 \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \ABpvec}}\,.
\end{align}
This can then be used to construct effective hit points and effective damage per round once following the same steps in the two previous sections,
\begin{align}
    \eHP  &= \frac{1}{\sqrt{0.65}} \, \HP \, 1.077^{\,\dprvec \cdot \ACpvec} \,, \label{eq:effective-hit-points-mix} \\\\ 
    \eDPR &= \sqrt{0.65} \, \DPR_{\total} \, 1.077^{\,\dprvec \cdot \ABpvec} \,. \label{eq:effective-damage-mix}
\end{align}

We can put Eqn. \eqref{eq:effective-damage-mix} into the same form as Eqn. \eqref{eq:effective-hit-points-attack} for simple attacks by defining an effective attack bonus $$(\eAB\,)$$ as
\begin{align}
    \eAB &= \dprvec \cdot \ABpvec + \AB_{0}\,,
\end{align}
which is just the average of the equivalent attack bonuses for each ability weighted by the amount of damage each does.

Looking at Eqn. \eqref{eq:effective-hit-points-mix}, one might be tempted to define an effective armor class $$(\eAC\,)$$ in a similar way, but there is a subtle problem with this approach. The $$\eHP$$ described by Eqn. \eqref{eq:effective-hit-points-mix} is calculated from $$\dprvec$$, which comes from the attacker, and is therefore not solely dependent on the defending monster stats.

To get around this, we can define a universal attack vector, $$\dprvec_{\mathrm{u}}$$ and use it when determining a creature's effective armor class,
\begin{align}
    \eAC &= \dprvec_{\mathrm{u}} \cdot \ACpvec + \AC_{0}\,.
    \label{eq:effective-armor-class}
\end{align}
I won't get into the exact form of $$\dprvec_{\mathrm{u}}$$ at this time (though, I hope to at some point in the near future), but, for now, think of it as the average attack vector the defender is likely see across a wide range of attackers. In the mean time, we can simply use the effective armor class defined in chapter 9 of the DMG as a proxy for calculating $$\eAC$$ using Eqn. \eqref{eq:effective-armor-class}.

<!--
And, since the number of defensive stats is fixed at seven for each creature (i.e., their armor class and six saving throw bonuses), $$\dprvec_{\mathrm{u}}$$ and $$\ACpvec$$ can both be written as vectors with seven elements, 
\begin{align}
    \dprvec = 
    \begin{bmatrix}
        \dpr_{\arm} \\\\ 
        \dpr_{\str} \\\\ 
        \vdots \\\\ 
        \dpr_{\cha}
    \end{bmatrix} \,; \,
    \ACpvec = 
    \begin{bmatrix}
        \AC - \AC_{0} \\\\ 
        \SB_{\str} - \SB_{0} \\\\ 
        \vdots \\\\ 
        \SB_{\cha} - \SB_{0}
    \end{bmatrix}\,,
\end{align}
where each $$\dpr$$ represents how much of the total damage targets each of the creature's defenses.
-->

As a final step, we can take advantage of the fact that the number of defensive stats is fixed at seven for each creature (i.e., their armor class and six saving throw bonuses), and rewrite $$\dprvec_{\mathrm{u}}$$ and $$\ACpvec$$ in terms of these seven stats rather than for an arbitrary number of damage sources, 
\begin{align}
    \dprvec &= \left[ \dpr_{\arm}, \dpr_{\str}, \cdots, \dpr_{\cha}  \right] \,; \\\\ 
    \ACpvec &= \left[ \ACp_{\arm}, \ACp_{\str}, \cdots, \ACp_{\cha} \right] \,.
\end{align}
Now each $$\dpr$$ represents the relative damage targeting each defensive stat, instead of the relative damage of each ability, and $$\ACp$$ is defined by Eqn. \eqref{eq:generic-armor-class-relative}.

<!--
where
\begin{align}
    \Delta \mathbf{eHP} 
        &= \sum_{\stat \in \stats} 1.077^{\,\ACp_{\stat} - \left( eAC - \AC_{0} \right) } \hat{\mathbf{s}}\_{s}
\end{align}
-->



<!--
\begin{align}
    \mathbf{dpr}\_{\mathrm{u}} = 
    \begin{bmatrix}
        \dpr_{\arm} \\\\ 
        \dpr_{\str} \\\\ 
        \dpr_{\dex} \\\\ 
        \dpr_{\con} \\\\ 
        \dpr_{\int} \\\\ 
        \dpr_{\wis} \\\\ 
        \dpr_{\cha} 
    \end{bmatrix} =
    \begin{bmatrix}
        1/2 \\\\ 
        1/12 \\\\ 
        1/12 \\\\ 
        1/12 \\\\ 
        1/12 \\\\ 
        1/12 \\\\ 
        1/12 
    \end{bmatrix}
    \,.
\end{align}
-->

<!--
let $$\D_{\total} = \sum \D_{i}$$ then
\begin{align}
    \Dave 
        &\approx 0.65 \, \D_{\total} \, \sum_{i = 1}^{N} dpr_{i} \, 1.077^{\,o_{i} - d_{i}} \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \, \sum_{i = 1}^{N} dpr_{i} \, \left(1 + 0.077 \, \left(o_{i} - d_{i}\right)\right) \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \, \left(1 + 0.077 \, \sum_{i = 1}^{N} dpr_{i} \, \left(o_{i} - d_{i}\right) \right) \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \, 1.077^{ \sum_{i = 1}^{N} dpr_{i} \, \left(o_{i} - d_{i}\right) } \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \, 1.077^{ \mathbf{dpr} \cdot \left( \ABpvec - \ACpvec \right) }
    \,,
    %\label{eq:save-damage-average-none-exp}
\end{align}
where $$d_{i} = \D_{i}/\D_{\total}$$.

This can also be written in the form
\begin{align}
    \Dave &\approx \mathbf{eD} \cdot \mathbf{eM} \,,
    %\label{eq:save-damage-average-none-exp}
\end{align}

\begin{align}
    \mathbf{eD} = \sqrt{0.65} \sum_{i = 1}^{N} \D_{i} \, 1.077^{\,o_{i}} \hat{\mathbf{s}}_{i}\,,
    %\label{eq:save-damage-average-none-exp}
\end{align}

\begin{align}
    \mathbf{eM} = \sqrt{0.65} \sum_{s \in S} 1.077^{- d_{s}} \hat{\mathbf{s}}\,,
    %\label{eq:save-damage-average-none-exp}
\end{align}

We can also write $$\mathbf{eD} = eD \, \ACpvec$$ where
\begin{align}
    eD = \sqrt{0.65} \sum_{i = 1}^{N} \D_{i} \, 1.077^{\,o_{i}} \,,
    %\label{eq:save-damage-average-none-exp}
\end{align}

\begin{align}
    \Dave &\approx eD \left(\ACpvec \cdot \mathbf{eM} \right) \,,
    %\label{eq:save-damage-average-none-exp}
\end{align}

Putting this into our test measurement

\begin{align}
    N \approx \frac{\HP}{eD \left(\ACpvec \cdot \mathbf{eM} \right)}\,,
    %\label{eq:rounds-to-win-none}
\end{align}

this leads to 
\begin{align}
    \eHP^{\,\prime} 
        &= \frac{ \HP }{ \ACpvec \cdot \mathbf{eM} } \nonumber \\\\ 
        &= \HP \left( \sqrt{0.65}\, \sum_{i = 1}^{N} d_{i} \, 1.077^{ - d_{i}}  \right)^{-1}  \nonumber \\\\ 
        &= \frac{1}{\sqrt{0.65}} \HP \, 1.077^{eAC} \left( \sum_{i = 1}^{N} d_{i} \, 1.077^{eAC - d_{i}}  \right)^{-1}  \nonumber \\\\ 
        &= \eHP \left( \sum_{i = 1}^{N} d_{i} \, 1.077^{eAC - d_{i}}  \right)^{-1}  \nonumber \\\\ 
        &= \eHP \left( \ACpvec \cdot \Delta \mathbf{eM} \right)^{-1}  \nonumber \\\\ 
\end{align}

\begin{align}
    \mathbf{dpr} \cdot \mathbf{eM}
        &= \sqrt{0.65}\, \sum_{i = 1}^{N} dpr_{i} \, 1.077^{ - d_{i}} \nonumber \\\\ 
        &\approx \sqrt{0.65}\, \sum_{i = 1}^{N} dpr_{i} \, \left(1 - 0.077\, d_{i}\right) \nonumber \\\\ 
        &= \sqrt{0.65}\, \left( 1 - 0.077 \, \sum_{i = 1}^{N} dpr_{i} \, d_{i} \right) \nonumber \\\\ 
        &= \sqrt{0.65}\, 1.077^{ - \sum_{i = 1}^{N} dpr_{i} \, d_{i} } \nonumber \\\\ 
        &= \sqrt{0.65}\, 1.077^{ - \mathbf{dpr} \cdot \ACpvec }
\end{align}

so
\begin{align}
    \eHP^{\,\prime} 
        &= \eHP \left( \ACpvec \cdot \Delta \mathbf{eM} \right)^{-1}  \nonumber \\\\ 
        &= \eHP \, 1.077^{ \mathbf{dpr} \cdot \ACpvec }  \nonumber \\\\ 
\end{align}
-->

# Discussion

Now that we've derived equations for effective hit points and effective damage, I'd like to spend some time discussing what they mean and where to go from here.

## Saving throw bonus scaling

One important thing that these equations show is how saving throw bonuses should scale in comparison to $$\AC$$. The [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275) lists suggested values for monster's $$\HP$$, $$\AC$$, and $$\DC$$ but it doesn't list one for $$\SB$$. However, if we compared Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-hit-points-save} then it becomes clear that $$\SB$$ should scale as $$\AC - 14$$.

<figure id="fig:monster-save-modifier-trends">
    {% include_relative fig-monster-save-modifier-vs-cr-small.html %}
    {% include_relative fig-monster-save-modifier-vs-cr-large.html %}
    <figcaption>Figure 1: Shows average saving throw modifiers (proficiency bonus not included) and armor class for monsters from official source books. Monster \(\AC\) values taken from the "Monster Statistics by Challenge Rating" table in chapter 9 of the DMG (p. 275). </figcaption>
</figure>

Figure <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> (above) shows this relationship for published monsters (I've excluded saving throw proficiency bonuses here because the DMG has separate rules for how much they should be valued in terms of an adjusted $$\AC\,$$). The saving throw modifiers for monsters clearly show a similar trend to $$\AC - 14$$ for all abilities but Dexterity, which is reassuring, and the average across all saving throws matches the trend for $$\AC - 14$$ almost exactly!

It's been well established that certain saving throws for monsters are weaker than others (see my earlier post [Monster Saving Throws]({{ site.data.page-links.monster-saving-throws.path }})). However, what hasn't been clear until now is whether the strong saving throws are overpowered or the weak saving throws are underpowered. 

What Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> shows is that, for monsters, Strength and Constitution modifiers are generally stronger than baseline, Wisdom and Charisma are on target, and Intelligence is slightly below baseline. Finally, monster Dexterity modifiers are on target at very low CRs and increasingly underpowered at CR increases.

<!--
## Putting it all together

As it stands now, we have two ways of calculating effective hit points and two ways of calculating effective damage. 

For damage, this doesn't pose any potential conflict. We can simply pick whichever equation best fits how are creature is dealing damage. If we wanted to calculate the effective damage per round $$(\eDPR)$$ for a creature that deals damage using one attack and one saving throw effect, we can simply add the effective damage of the two together. Put more generally,
\begin{align}
    \eDPR = \sum \eDatck \left(\Dhit, \AB\,\right)  + \sum \eDsave \left(\Dfail, \DC\,\right)\,,
    %\eDPR = \sqrt{0.65} \cdot \left( \sum \Dhit \cdot 1.077^{\AB - 3}  + \sum \cdot \Dfail \cdot {1.077}^{\DC - 12}\right)\,,
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

## Linear approximation

For some, the form of Eqns. \eqref{eq:effective-hit-points-attack} - \eqref{eq:effective-damage-attack} and Eqns. \eqref{eq:effective-hit-points-save} - \eqref{eq:effective-damage-save} can be a bit intimidating due to their exponential nature. For those wanting more linear equations for effective hit points and effective health, the same approximation used previously can be used in reverse, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, resulting in the following for attacks,
\begin{align}
    \eHPatck &\approx \frac{1}{\sqrt{0.65}} \cdot \HP \left( 1 + 0.077 \left(\AC - 12\right)\right)\,, \label{eq:effective-hit-points-attack-approx} \\\\ 
    \eDatck  &\approx \sqrt{0.65} \cdot \Dhit \left( 1 + 0.077 \left(\AB - 3\right)\right)\,, \label{eq:effective-damage-attack-approx}
\end{align}
and for saving throws,
\begin{align}
    \eHPsave &\approx \frac{1}{\sqrt{0.65}} \cdot \HP  \left(1 + 0.077 \left(\SB + 2\right)\right)\,, \label{eq:effective-hit-points-save-approx} \\\\ 
    \eDsave  &\approx \sqrt{0.65} \cdot \Dfail \left(1 + 0.077\left(\DC - 12\right)\right)\,. \label{eq:effective-damage-save-approx}
\end{align}

It should be noted, however, that while this works well for low CR creatures, at higher CRs this approach will introduce minor errors due to the exclusion of higher order terms in the approximation.

Another small adjustment that some may find useful is to multiply all four of the above equations by $$\sqrt{0.65}$$. This removes the prefactor from Eqns. \eqref{eq:effective-hit-points-attack-approx} and \eqref{eq:effective-hit-points-save-approx}, and also removes the square root from Eqns. \eqref{eq:effective-damage-attack-approx} and \eqref{eq:effective-damage-save-approx}. As I mentioned before, the choice to split the factor of $$0.65$$ between the two terms was a stylistic one that proves useful when discussing how XP is calculated, which you can read about [here]({{ site.data.page-links.xp-and-encounter-balancing.path }}).

## Encounter specific effective hit points

The introduction of $$\dprvec_{\mathrm{u}}$$ in Eqn. \eqref{eq:effective-armor-class} effectively removes any information about the attacker from our $$eHP$$ calculation, but it also means $$eHP$$ won't always reflect a creature's true toughness in combat. In other words, it masks the fact that each creature's overall toughness in combat does, in fact, depend on which of their defensive stats their opponents target.

We can determine how much this causes $$\eHP$$ to underestimate or overestimate a creature's toughness in a particular encounter by taking the ratio between their encounter specific effective hit points and their general effective hit points,
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

In this post I've shown how effective hit points and effective damage can be derived for creatures using the math underpinning how attacks and saving throws work in D&D 5th edition. These allow a creature's defensive and offensive strength to be calculated in absolute terms, without the need of a second creature for comparison. For damage, this allows both attacks and saving throw effects to be added together and weighted equally. And for hit points, this allows an overall defensive strength to be calculated that combines armor class as well as saving throw bonuses. 

In the process, I've also shown how monster ability score modifiers can be expected to scale with CR in a way similar to how the DMG recommends scaling armor class. 

For anyone who stuck through all that to the end, congratulations! Compared to many of my previous posts, this one doesn't contain that much in terms of useful insights into the game. But it does lay the ground work needed for much more to come.