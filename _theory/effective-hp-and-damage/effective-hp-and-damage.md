---
title: "Effective HP and Damage"
excerpt: "How to represent creature defensive and offensive strengths in effective terms that don't require calculating chances to hit or save against an enemy creature."
permalink: /:collection/:name/
date: 2022-01-17
last_modified_at: 2024-05-01
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

In this post, I show how such effective hit points and effective damage can be calculated for any combination of attacks and saves that deal damage with no additional effects. Clearly, there are more complicated abilities in the game than these, but solving these simple cases will help lay the ground-work for handing those more complicated abilities later on.

# Derivation

In order for any effective hit points or effective damage formula to be practically useful they can't just be theoretical constructs, they also need to be grounded in reality. They need to work for calculating real, measurable quantities. To ensure this, I'll be using the equation for one such measurable quantity as the basis of this derivation. Specifically, I'll be using the equation for calculating the average number of rounds $$(N_{\rounds})$$ it takes for an attacker to defeat a given enemy creature, 
\begin{align}
    N_{\rounds} &= \frac{\HP}{\DPR_{\ave}}\,.
    \label{eq:rounds-to-win}
\end{align}
where $$\HP$$ is the defending creature's hit points, and $$\DPR_{\ave}$$ is the attacker's average damage per round.

For attacks, $$\DPR_{\ave}$$ depends on both the defender's armor class $$(\AC\,)$$ and the attacker's attack bonus $$(\AB\,)$$, and for saves it depends on the defender's saving throw bonus $$(\SB\,)$$ and the attacker's save difficulty class $$(\DC\,)$$. In either case, the goal is to move all defensive terms to the numerator (top), where they can be grouped with the defender's $$\HP$$, and all offensive terms to the denominator (bottom). This means we want to rearrange things in the following way,
\begin{align}
    \frac{\HP}{\DPR_{\ave}(\AB, \AC, \DC, \SB\,)} \Rightarrow \frac{\eHP(\AC, \SB\,)}{\eDPR(\AB, \DC\,)}\,,
    \label{eq:separation-requirement}
\end{align}
where $$\eHP$$ is the target's effective hit points, and $$\eDPR$$ is the attackers effective damage per round.

I've broken up this derivation into three parts. The first two look at how the average damage is calculated for [simple attacks](#simple-attacks) and [simple saves](#simple-saves), and how these equations can be "re-centered" about the game's baseline chance to deal damage. The third then takes these re-centered average damage equations, generalizes them, and uses them, along with Eqn. \eqref{eq:rounds-to-win}, to derive formulas for a creature's [effective hit points and damage per round](#effective-hit-points-and-damage-per-round).


## Simple attacks

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
This centers the equation around the observed $$65\%$$ average and uses the term $$(8 + \AB - \AC\,)/13$$ to measure how much this particular attack deviates away from that average. What makes this form useful is that these deviations are typically small relative to the average. A quality we'll need to take advantage of later on.

We'll come back to Eqn. \eqref{eq:attack-damage-average-centered} shortly, but before we progress any further, lets take a look at how the average damage for a save is calculated.


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
where now the term $$\left(\DC - \SB - 14\right)/13$$ represents a small deviation away from that average. We'll take advantage of this property in the section that follows.

With both of our average damage equations written in this way, we're ready to move on to the general case and deriving our equations for $$\eHP$$ and $$\eDPR$$.


## Effective hit points and damage per round

With the results of the previous two sections under our belts, lets move on to the task at hand of calculating $$\DPR_{\ave}$$ for our attacker.

To make this task a bit simpler, note that our average damage equations, Eqns. \eqref{eq:attack-damage-average-centered} and \eqref{eq:save-damage-average-none-centered}, have the same general form, and both can be written in the following way,
\begin{align}
    \D_{\ave}  &= 0.65 \, \D \left[1 + \left( \frac{ \ABp - \ACp }{ 13 } \right)\right] .
    \label{eq:mixed-damage-average-basic}
\end{align}
Here, $$\D$$ represents the average damage dealt on a hit for an attack or on a failed saving throw for a save. The variable $$\ABp$$ is the normalized offensive stat used to determine whether damage is dealt or not (either attack bonus or save difficulty class),
\begin{equation}
    \ABp = 
    \begin{cases} 
        \AB - \AB_{0} & \mathrm{for\ attacks}\,, \\\\ 
        \DC - \DC_{0} & \mathrm{for\ saves}\,, 
    \end{cases}
\end{equation}
where $$\AB_{0} = 4$$ and $$\DC_{0} = 12$$ represent common baseline values for attack bonus and save difficulty class. And the variable $$\ACp$$ is the corresponding normalized defensive stat that the damage targets (either armor class or saving throw bonus),
\begin{equation}
    \ACp = 
    \begin{cases} 
        \AC - \AC_{0} & \mathrm{for\ attacks}\,, \\\\ 
        \SB \, - \SB_{0} & \mathrm{for\ saves}\,,
    \end{cases}
    \label{eq:generic-armor-class-relative}
\end{equation}
where $$\AC_{0} = 12$$ and $$\SB_{0} = -2$$ represent common baseline values for armor class and saving throw bonus.

**Note.** The values use here for $$\AB_{0}$$, $$\AC_{0}$$, $$\DC_{0}$$, and $$\SB_{0}$$ are not the only options we could have chosen. Equations \eqref{eq:attack-damage-average-centered} and \eqref{eq:save-damage-average-none-centered} only require $$\AB_{0} + 8 = \AC_{0}$$ and $$\SB_{0} + 14 = \DC_{0}$$. To get these specific values, I also used the fact that $$\AB + 8 = \DC$$ for spellcasters, and that $$\AB \approx 4$$ on average for [CR 1 monsters]({{ site.data.page-links.baseline-monster-stats.path }}/#fig:ab-vs-cr). 
{: .notice--warning}


Defining $$\ABp$$ and $$\ACp$$ in this way puts our offensive and defensive stats on equal scales. Meaning, $$\ABp = 5$$ is equally good at dealing damage as $$\ACp = 5$$ is as avoiding it relative to our $$65\%$$ baseline for both attacks and saves.

With this generalized average damage equation in hand, determining $$\DPR_{\ave}$$ for any attacker is simply a matter of calculating the average damage per round for each of their attacks and saves individually using Eqn. \eqref{eq:mixed-damage-average-basic} and then adding them all together,
\begin{align}
    \DPR_{\ave}  &= \sum_{i = 1}^{N} 0.65 \, \DPR_{i} \left[1 + \left( \frac{ \ABp_{i} - \ACp_{i} }{ 13 }\right)\right] .
    \label{eq:mixed-damage-average-1}
\end{align}
Here, $$N$$ is the number of attacks and saves used by the creature to deal damage during combat. For each ability, $$\DPR$$ is the average damage per round dealt when the ability deals damage, $$\ABp$$ is the offensive stat used to determine if the ability deals damage, and $$\ACp$$ is the corresponding defensive stat being targeted.

If we take the total damage per round, assuming all abilities successfully deal damage, $$\DPR_{\total} = \sum \DPR_{i}$$, and factor it out of the summation, Eqn. \eqref{eq:mixed-damage-average-1} becomes,
\begin{align}
    \DPR_{\ave} 
        &= 0.65 \, \DPR_{\total} \sum_{i = 1}^{N} dpr_{i} \left[1 + \left( \frac{ \ABp_{i} - \ACp_{i} }{ 13 } \right)\right] \nonumber \\\\ 
        &= 0.65 \, \DPR_{\total} \left[1 +  \sum_{i = 1}^{N} dpr_{i} \left( \frac{ \ABp_{i} - \ACp_{i} }{ 13 } \right) \right] \,,
    \label{eq:mixed-damage-average-2}
\end{align}
where $$\dpr = \DPR/\DPR_{\total}\,$$ is the fraction of $$\DPR_{\total}$$ dealt by an attack or save, and that $$\sum \dpr_{i} = 1$$.

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
Each of these vectors has $$N$$ elements, one for each of of the attacker's attacks and saves.

Substituting Eqn. \eqref{eq:sum-as-dot-products} into Eqn. \eqref{eq:mixed-damage-average-2} gives, 
\begin{align}
    \DPR_{\ave} = 0.65 \, \DPR_{\total} \left[1 +  \frac{ \dprvec \cdot \left( \ABpvec - \ACpvec \right) }{ 13 } \right].
    \hspace{-.8em}
    \label{eq:mixed-damage-average-3}
\end{align}

From here, we can take advantage of the fact that $$1/13$$ is small, $$1/13 \approx 0.077 \ll 1$$, to apply the following approximation to Eqn. \eqref{eq:mixed-damage-average-3}, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which results in
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
which is just the weighted average of the attacker's normalized offensive stats, expressed in terms of an equivalent attack bonus value.

**Note.** The choice to split the factor of $$0.65$$ between $$\eHP$$ and $$\eDPR$$ was a stylistic one that proves useful when discussing how [XP is calculated]({{ site.data.page-links.xp-and-encounter-balancing.path }}).
{: .notice--warning}

Before concluding this derivation, it's worth noting that, while we were able to successfully split $$\AB$$ and $$\DC$$ from $$\AC$$ and $$\SB$$, our formula for $$\eAC$$, Eqn. \eqref{eq:effective-armor-class}, still contains $$\dprvec$$ which comes from the attacker. To get around this, instead of using a specific attacker's $$\dprvec$$ when calculating $$\eAC$$, we can define a "universal" attack vector $$\dprvec_{\mathrm{u}}$$ that represents the average of what the defender might see across a broad range of attackers, and use that for calculating $$\eAC$$.

At this time, it's unclear what the exact form of $$\dprvec_{\mathrm{u}}$$ should be. The "[Creating a Monster](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop/#CreatingaMonster)" section from chapter 9 of the DMG covers how to adjust a creature's $$\AC$$ to account for their saving throw proficiencies and any saving throw related traits they might have. This _could_ work as a stand in for an $$\eAC$$ calculated using $$\dprvec_{\mathrm{u}}$$, but since the DMG's method for adjusting $$\AC$$ is almost certainly an approximation this isn't an ideal solution.

For further discussion around the impact $$\dprvec_{\mathrm{u}}$$ has on monster effective hit points, see "[Encounter specific effective hit points](#encounter-specific-effective-hit-points)" in the section that follows.


# Discussion

Now that we've derived equations for effective hit points and effective damage, I'd like to spend some time discussing what they mean and where to go from here.

## Linear approximation

For some, the form of Eqns. \eqref{eq:effective-hit-points-mix} and \eqref{eq:effective-damage-mix} can be a bit intimidating due to their exponential nature. For those wanting more linear equations for effective hit points and effective health, the same approximation used previously can be used in reverse, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, resulting in the following,
\begin{align}
    \eHP  &\approx \frac{1}{\sqrt{0.65}} \, \HP \left[ 1 +  \left( \frac{ \eAC - \AC_{0} }{ 13 } \right) \right] , \label{eq:effective-hit-points-mix-approx} \\\\ 
    \eDPR &\approx \sqrt{0.65} \, \DPR_{\total} \left[ 1 + \left( \frac{ \eAB - \AB_{0} }{ 13 } \right) \right] . \label{eq:effective-damage-mix-approx}
\end{align}

It should be noted, however, that while this works well for low CR creatures, at higher CRs this approach will introduce errors, due to the exclusion of higher order terms in the approximation, that lead to $$\eAB$$ and $$\eAC$$ being undervalued for higher CR monsters.

Another small adjustment that some may find useful is to multiply both of the above equations by $$\sqrt{0.65}$$. This removes the prefactor from Eqn. \eqref{eq:effective-hit-points-mix-approx} and also removes the square root from Eqn. \eqref{eq:effective-damage-mix-approx}. As I mentioned before, the choice to split the factor of $$0.65$$ between the two terms was a stylistic one that proves useful when discussing how [XP is calculated]({{ site.data.page-links.xp-and-encounter-balancing.path }}).

## Saving throw bonus scaling

One important thing that these equations show is how saving throw bonuses should scale in comparison to $$\AC$$. The [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275) lists suggested values for monster's $$\HP$$, $$\AC$$, and $$\DC$$ but it doesn't list one for $$\SB$$.

However, if we compared equal values of $$\ACp$$ for attacks and saves, it becomes clear that $$\SB$$ should scale as $$\AC - 14$$. Comparing saving throw modifiers for published monsters against the baseline $$\AC$$ values from the "Monster Statistics by Challenge Rating" table in chapter 9 of the DMG, as shown in Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">3</a> (below), this is indeed the case. 

<figure id="fig:monster-save-modifier-trends">
    {% include_relative fig-monster-save-modifier-vs-cr-small.html %}
    {% include_relative fig-monster-save-modifier-vs-cr-large.html %}
    <figcaption>Figure 3: Shows average saving throw modifiers (proficiency bonus not included) and armor class for monsters from official source books. Monster \(\AC\) values taken from the "Monster Statistics by Challenge Rating" table in chapter 9 of the DMG (p. 275). </figcaption>
</figure>

For all abilities but Dexterity, monster saving throw modifiers follow similar trends to $$\AC - 14$$, and the average across all saving throws matches the trend for $$\AC - 14$$ almost exactly!

It's been well established that certain saving throws for monsters are weaker than others (see my post on [Monster Saving Throws]({{ site.data.page-links.monster-saving-throws.path }})). However, what hasn't been clear until now is whether the strong saving throws are overpowered or the weak saving throws are underpowered.

What Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> shows is that, for monsters, Strength and Constitution modifiers are generally stronger than baseline, Wisdom and Charisma are on target, Intelligence is slightly below baseline, and Dexterity starts out stronger than baseline at low CRs but becomes relatively weaker and weaker as CR increases.


## Encounter specific effective hit points

The introduction of $$\dprvec_{\mathrm{u}}$$ in Eqn. \eqref{eq:effective-armor-class} effectively removes any information about the attacker from our $$eHP$$ calculation. As a result, it also means $$\eHP$$ won't always reflect a creature's true toughness in combat, because that depends on their opponents' specific attack vector.

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

Following the rules in chapter 9 of the DMG, the hezrou has an adjusted AC of 21, which translates into $$\eAC^{\,\prime} = 9$$. Adding a $$+4$$ bonus to each of the hezrou's saving throws to account for the Magic Resistance trait and a $$+2$$ bonus to the hezrou's AC to account for its Stench trait, gives the hezrou the following relative toughness vector,
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

The effective hit points and effective damage per round derived in this post are useful tools for comparing creatures' offensive and defensive strengths in more absolute terms, without the need of a second creature for comparison. The general equations for effective attack bonus and effective armor class are also useful towards that end, and also give us greater insight into the relative strength of each defensive stat.

Most importantly, these results lay the groundwork needed for future work analyzing D&D 5th edition, and potentially other TTRPGs. For further reading on how these tools can be used to further understand combat in D&D 5th edition, see [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}) and [The Value of Legendary Resistances]({{ site.data.page-links.legendary-resistance.path }})