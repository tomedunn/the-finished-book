---
title: "Effective HP and Damage"
excerpt: "How to represent creature defensive and offensive strengths in effective terms that don't require calculating chances to hit or save against an enemy creature."
date: 2022-1-17
last_modified_at: 2023-3-4
#tags:
#  - theory
#  - monsters
#  - classes
---

<div style="display:none">
\(
\newcommand{\RTW}{\mathit{RTW}}
\newcommand{\phit}{\rho_\mathrm{hit}}
\newcommand{\pcrit}{\rho_\mathrm{crit}}
\newcommand{\pmiss}{\rho_\mathrm{miss}}
\newcommand{\psave}{\rho_\mathrm{save}}
\newcommand{\pfail}{\rho_\mathrm{fail}}
\newcommand{\AC}{\mathit{AC}}
\newcommand{\eAC}{\mathit{eAC}}
\newcommand{\SB}{\mathit{SB}}
\newcommand{\SBave}{\SB_\mathrm{ave}}
\newcommand{\HP}{\mathit{HP}}
\newcommand{\eHP}{\mathit{eHP}}
\newcommand{\eHPatck}{\eHP_\mathrm{a}}
\newcommand{\eHPsave}{\eHP_\mathrm{s}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\DC}{\mathit{DC}}
\newcommand{\eD}{\mathit{eD}}
\newcommand{\eDatck}{\eD_\mathrm{a}}
\newcommand{\eDsave}{\eD_\mathrm{s}}
\newcommand{\eDPR}{\mathit{eDPR}}
\newcommand{\D}{\mathit{D}}
\newcommand{\Dave}{\D_\mathrm{ave}}
\newcommand{\Dhit}{\D_\mathrm{hit}} 
\newcommand{\Dcrit}{\D_\mathrm{crit}}
\newcommand{\Dsave}{\D_\mathrm{save}}
\newcommand{\Dfail}{\D_\mathrm{fail}}
\newcommand{\DPR}{\mathit{DPR}} 
\newcommand{\DPRhit}{\DPR_\mathrm{hit}} 
\newcommand{\DPRcrit}{\DPR_\mathrm{crit}}
\newcommand{\DPRsave}{\DPR_\mathrm{save}}
\newcommand{\DPRfail}{\DPR_\mathrm{fail}}
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
    \Dave &= \Dhit \cdot \phit + \Dcrit \cdot \pcrit \,,
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
    \Dave &= \Dhit \cdot 0.05 \left(22 + \AB - \AC\,\right) \nonumber \\\\ 
          &= \Dhit \cdot 0.05 \left(13 + \left(9 + \AB - \AC\,\right)\right)  \nonumber \\\\ 
          &= \Dhit \cdot 0.65 \, \left(1 + 0.077 \left(9 + \AB - \AC\,\right)\right)\,,
    \label{eq:attack-damage-average-full}
\end{align}

where $$0.077 \equiv 1/13$$. 

The form of Eqn. \eqref{eq:attack-damage-average-full} may seem odd at first glance, but it can be explained rather simply. 

As shown in Fig. <a href="#fig:attack-hit-probability-vs-level" class="fig-ref">1</a> (below), the average chance to hit with an attack against a level appropriate enemy is close to $$65\%$$ for both monsters and PCs. With this in mind, the therm $$0.077\,(9 + \AB - \AC\,)$$ in Eqn. \eqref{eq:attack-damage-average-full} measures how much the attack's average damage deviates from that baseline.

<figure id="fig:attack-hit-probability-vs-level">
    {% include_relative effective-hp-and-damage/fig-attack-hit-probability-vs-level-small.html %}
    {% include_relative effective-hp-and-damage/fig-attack-hit-probability-vs-level-large.html %}
    <figcaption>Figure 1: Shows the average chance to hit with an attack against a level appropriate target for monsters (blue) and PCs (orange). Monster \(\AB\) and \(AC\) values taken from chapter 9 of the DMG (p. 275). PCs were assumed to start with an attack modifier of +3 at 1st level that increases to +4 at 4th level and to +5 at 8th level, and \(\AC\) is averaged across all classes with minor armor improvements from purchasing better mundane gear, with no bonuses to their \(\AB\) or \(\AC\) from magic items.</figcaption>
</figure>

The value of putting Eqn. \eqref{eq:attack-damage-average-full} in this form is that it allows us to take advantage of the following approximation, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which turns Eqn. \eqref{eq:attack-damage-average-full} into

\begin{align}
    \Dave \approx \Dhit \cdot 0.65 \cdot 1.077^{\,9 + \AB - \AC}\,,
    \label{eq:attack-damage-average-exp}
\end{align}

where $$1.077 \equiv 14/13$$.

Putting Eqn. \eqref{eq:attack-damage-average-exp} back into our test equation, Eqn. \eqref{eq:uses-to-win}, gives

\begin{align}
    N_\mathrm{attacks} &= \frac{\HP}{\Dave(\AB, \AC\,)} \nonumber \\\\\\
      &\approx \frac{\HP}{\Dhit \cdot 0.65 \cdot 1.077^{\,9 + \AB - \AC}}\,,
    \label{eq:uses-to-win-attack}
\end{align}

and, since $$x^{a + b} = x^a\,x^b$$, we can finally move $$\AC$$ into the numerator,

\begin{align}
    N_\mathrm{attacks} &\approx \frac{\HP \cdot 1.077^{\AC - \AC_0}}{\Dhit \cdot 0.65 \cdot 1.077^{\AB + 1 - \AB_0}}\,.
\end{align}

Here, $$\AC_0$$ and $$\AB_0$$ are baseline values for a creature's armor class and attack bonus respectively, and the extra $$+1$$ in the exponent of the denominator (bottom) is there to separate out the extra damage dealt by critical hit. We have a lot of flexibility in what values we choose for these baselines, so long as they satisfy $$\AC_0 = 8 + \AB_0$$.

At this point our task is essentially done. We've successfully moved all the stats of the defending creature to the numerator, $$\HP$$ and $$\AC$$, and all the stats of the attacking creature in the denominator, $$\Dave$$ and $$\AB$$. The average number of attacks it takes the attacker to win can now be written in the form

\begin{align}
    N_\mathrm{attacks} \approx \frac{ \eHP \left(\HP,\AC\,\right)}{\eD \left(\Dhit, \AB\,\right)}\,,
\end{align}

where $$\eHP$$ is the defending creature's effective hit points and $$\eD$$ is the attacking creature's effective damage, which are given by

\begin{align}
    \eHPatck &= \frac{1}{\sqrt{0.65}} \cdot \HP \cdot 1.077^{\AC - 12}\,, \label{eq:effective-hit-points-attack} \\\\ 
    \eDatck  &= \sqrt{0.65} \cdot \Dhit \cdot 1.077^{\AB - 3}\,. \label{eq:effective-damage-attack}
\end{align}

Here, I've chosen $$\AB_0 = 4$$ and $$\AC_0 = 12$$, which satisfy our requirement that $$\AC_0 = 8 + \AB_0$$.

It's worth pointing out that while Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-damage-attack} do satisfied equation \eqref{eq:uses-to-win-attack}, they're not the only possible solutions. I chose $$\AC_0 = 12$$ because it's one less than the target $$\AC$$ of $$13$$ for a CR 1 monster from the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275), and $$\AB_0 = 4$$ to satisfy the requirement that
$$\AC_0 = 8 + \AB_0$$. These, along with the factors of $$\sqrt{0.65}$$ in front of each equation, are particularly useful for calculating calculating creature XP values, as I discuss [here]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}).

## Simple saving throws

For damaging effects that require saving throws, the derivation of effective hit points and effective damage follows a similar path. To start, $$\Dave$$ can be calculated for saving throws as 

\begin{equation}
    \Dave = \Dfail \cdot \pfail + \Dsave \cdot \psave\,,
    \label{eq:save-damage-average-abstract}
\end{equation}

where $$\Dfail$$ is the damage from a failed save, $$\Dsave$$ is the damage from a successful save, $$\pfail$$ is the probability of the target failing the saving throw, 

\begin{equation}
    %\pfail = \left(\frac{DC - SB - 1}{20}\right)\,,
    \pfail = 0.05\left(DC - SB - 1\,\right)\,,
    \label{eq:save-hit-probability}
\end{equation}

and $$\psave = 1 - \pfail$$ is the probability of the target succeeding. In order to avoid negative probabilities, the results of Eqn. \eqref{eq:save-hit-probability} are also bound between $$0 \le \pfail \le 1$$.

Assuming the effect deals no damage on a successful save, $$\Dsave = 0$$, then \eqref{eq:save-damage-average-abstract} simplifies to

\begin{align}
    \Dave &= \Dfail \cdot 0.05 \left(DC - SB - 1\,\right) \nonumber \\\\ 
          &= \Dfail \cdot 0.05 \left(13 + \left(DC - SB - 14\,\right)\right) \nonumber \\\\ 
          &= \Dfail \cdot 0.65 \left(1 + 0.077 \left(DC - SB - 14\,\right)\right)\,,
    \label{eq:save-damage-average-none-full}
\end{align}

where $$0.077 \equiv 1/13$$.

Just as in the previous section for attacks, the form of Eqn. \eqref{eq:save-damage-average-none-full} was chosen to take advantage of the fact that the average chance for a level appropriate target to fail a saving throw is close to $$65\%$$, as shown in Fig. <a href="#fig:save-hit-probability-vs-level" class="fig-ref">2</a> (below).

<figure id="fig:save-hit-probability-vs-level">
    {% include_relative effective-hp-and-damage/fig-save-hit-probability-vs-level-small.html %}
    {% include_relative effective-hp-and-damage/fig-save-hit-probability-vs-level-large.html %}
    <figcaption>Figure 2: Shows the average chance to hit with a saving throw against a level appropriate target for monsters (blue) and PCs (orange). Monster \(\DC\) values taken from chapter 9 of the DMG (p. 275) and \(\SB\) were averaged from published monsters. PCs were assumed to start with a save modifier of +3 at 1st level that increases to +4 at 4th level and to +5 at 8th level, and \(\SB\) is averaged across all classes and monsters, with no bonuses to their \(\DC\) or \(\SB\) from magic items.</figcaption>
</figure>

And, since $$0.077 \ll 1$$ we can once again use the approximation $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, to arrive at the equation's final form,

\begin{align}
    \Dave &\approx \Dfail \cdot 0.65 \cdot 1.077^{DC - SB - 14}\,,
    \label{eq:save-damage-average-none-exp}
\end{align}

where $$1.077 \equiv 14/13$$.

Calculating the number of times a creature needs to use their saving throw effect in order to defeat another creature gives

\begin{align}
    N \approx \frac{\HP \cdot 1.077^{\SB - \SB_0}}{\Dfail \cdot 0.65 \cdot 1.077^{\DC - \DC_0}}\,,
    \label{eq:saves-to-win-none}
\end{align}

where $$\SB_0$$ and $$\DC_0$$ are baseline values for a creature's saving throw bonus and ability difficulty class respectively, that must satisfy the relationship $$\DC_0 = \SB_0 + 14$$.

This can also be expressed in terms of $$\eHP$$ and $$\eD$$ using the following definitions,

\begin{align}
    \eHPsave &= \frac{1}{\sqrt{0.65}} \cdot \HP  \cdot {1.077}^{\SB + 2}\,, \label{eq:effective-hit-points-save} \\\\ 
    \eDsave  &= \sqrt{0.65} \cdot \Dfail \cdot {1.077}^{\DC - 12}\,. \label{eq:effective-damage-save}
\end{align}

Just like in the previous section with attacks, I chose $$\DC_0 = 12$$ because it's one less than the target $$\DC$$ for a CR 1 monster listed in the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275), and $$\SB_0 = -2$$ because it satisfies the requirement that $$\DC_0 = \SB_0 + 14$$. 

It's worth noting that the DMG doesn't actually list recommended values for $$\SB$$, which is an unfortunate oversight, but the suggested minimum value presented here of $$\SB_0 = -2$$ is significant, as I'll discuss later on in this post.

The form of the effective hit points in Eqn. \eqref{eq:effective-hit-points-save} poses another interesting problem because every creature has six different values for $$\SB$$, one for each ability score. If we think of each ability score's $$\SB$$ value as representing a creatures defense against one avenue of effect, then their overall defense against saving throw effects can be represented by averaging across all ability scores,

\begin{align}
    \SBave = \sum \SB_i / 6\,, \label{eq:average-save-bonus} \\\\ 
\end{align}

where the sum is carried out over all six ability scores. This may be a bit too simplistic of an approach, though, as not all ability scores are targeted equally by saving throw effects. However, it will do for the time being.


# Discussion

Now that we've derived equations for effective hit points and effective damage, I'd like to spend some time discussing what they mean and where to go from here.

## Saving throw bonus scaling

One important thing that these equations show is how saving throw bonuses should scale in comparison to $$\AC$$. The [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275) lists suggested values for monster's $$\HP$$, $$\AC$$, and $$\DC$$ but it doesn't list one for $$\SB$$. However, if we compared Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-hit-points-save} then it becomes clear that $$\SB$$ should scale as $$\AC - 14$$.

<figure id="fig:monster-save-modifier-trends">
    {% include_relative effective-hp-and-damage/fig-monster-save-modifier-vs-cr-small.html %}
    {% include_relative effective-hp-and-damage/fig-monster-save-modifier-vs-cr-large.html %}
    <figcaption>Figure 1: Shows average saving throw modifiers (proficiency bonus not included) and armor class for monsters from official source books. Monster \(\AC\) values taken from the "Monster Statistics by Challenge Rating" table in chapter 9 of the DMG (p. 275). </figcaption>
</figure>

Figure <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> (above) shows this relationship for published monsters (I've excluded saving throw proficiency bonuses here because the DMG has separate rules for how much they should be valued in terms of an adjusted $$\AC\,$$). The saving throw modifiers for monsters clearly show a similar trend to $$\AC - 14$$ for all abilities but Dexterity, which is reassuring, and the average across all saving throws matches the trend for $$\AC - 14$$ almost exactly!

It's been well established that certain saving throws for monsters are weaker than others (see my earlier post [Monster Saving Throws]({{ site.url }}{{ site.baseurl }}{% link _monsters/monster-saving-throws.md %})). However, what hasn't been clear until now is whether the strong saving throws are overpowered or the weak saving throws are underpowered. 

What Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> shows is that, for monsters, Strength and Constitution modifiers are generally stronger than baseline, Wisdom and Charisma are on target, and Intelligence is slightly below baseline. Finally, monster Dexterity modifiers are on target at very low CRs and increasingly underpowered at CR increases.

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

Another small adjustment that some may find useful is to multiply all four of the above equations by $$\sqrt{0.65}$$. This removes the prefactor from Eqns. \eqref{eq:effective-hit-points-attack-approx} and \eqref{eq:effective-hit-points-save-approx}, and also removes the square root from Eqns. \eqref{eq:effective-damage-attack-approx} and \eqref{eq:effective-damage-save-approx}. As I mentioned before, the choice to split the factor of $$0.65$$ between the two terms was a stylistic one that proves useful when discussing how XP is calculated, which you can read about [here]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}).

# Conclusion

In this post I've shown how effective hit points and effective damage can be derived for creatures using the math underpinning how attacks and saving throws work in D&D 5th edition. These allow a creature's defensive and offensive strength to be calculated in absolute terms, without the need of a second creature for comparison. For damage, this allows both attacks and saving throw effects to be added together and weighted equally. And for hit points, this allows an overall defensive strength to be calculated that combines armor class as well as saving throw bonuses. 

In the process, I've also shown how monster ability score modifiers can be expected to scale with CR in a way similar to how the DMG recommends scaling armor class. 

For anyone who stuck through all that to the end, congratulations! Compared to many of my previous posts, this one doesn't contain that much in terms of useful insights into the game. But it does lay the ground work needed for much more to come.