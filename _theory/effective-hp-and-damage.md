---
title: "Effective HP and Damage"
excerpt: "How to represent creature defensive and offensive strengths in effective terms that don't require calculating chances to hit or save against an enemy creature."
date: 2022-1-17
last_modified_at: 2022-1-20
#tags:
#  - theory
#  - monsters
#  - classes
---


\\(
\newcommand{\RTW}{\mathit{RTW}}
\newcommand{\phit}{\rho\_\mathrm{hit}}
\newcommand{\pcrit}{\rho\_\mathrm{crit}}
\newcommand{\pmiss}{\rho\_\mathrm{miss}}
\newcommand{\psave}{\rho\_\mathrm{save}}
\newcommand{\pfail}{\rho\_\mathrm{fail}}
\newcommand{\AC}{\mathit{AC}}
\newcommand{\SB}{\mathit{SB}}
\newcommand{\SBave}{\mathit{SB}\_\mathrm{ave}}
\newcommand{\HP}{\mathit{HP}}
\newcommand{\eHP}{\mathit{eHP}}
\newcommand{\eHPatck}{\mathit{eHP}\_\mathrm{a}}
\newcommand{\eHPsave}{\mathit{eHP}\_\mathrm{s}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\DC}{\mathit{DC}}
\newcommand{\eD}{\mathit{eD}}
\newcommand{\eDatck}{\mathit{eD}\_\mathrm{a}}
\newcommand{\eDsave}{\mathit{eD}\_\mathrm{s}}
\newcommand{\eDPR}{\mathit{eDPR}}
\newcommand{\D}{\mathit{D}}
\newcommand{\Dave}{\mathit{D}\_\mathrm{ave}}
\newcommand{\Dhit}{\mathit{D}\_\mathrm{hit}} 
\newcommand{\Dcrit}{\mathit{D}\_\mathrm{crit}}
\newcommand{\Dsave}{\mathit{D}\_\mathrm{save}}
\newcommand{\Dfail}{\mathit{D}\_\mathrm{fail}}
\newcommand{\DPR}{\mathit{DPR}} 
\newcommand{\DPRhit}{\mathit{DPR}\_\mathrm{hit}} 
\newcommand{\DPRcrit}{\mathit{DPR}\_\mathrm{crit}}
\newcommand{\DPRsave}{\mathit{DPR}\_\mathrm{save}}
\newcommand{\DPRfail}{\mathit{DPR}\_\mathrm{fail}}
\\)

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

<!--
Lets say I have two creatures who are engaged in combat and I want to calculate the number of attacks it will take for one to defeat the other. The calculation for this is fairly straight forward, just divide the defending creature's hit points by the average damage of attacking creature's attack, which depends on the attacker's attack bonus and the defender's armor class.

simple task of determining the average number of attacks it takes a creature to defeat another in combat. This is easily calculated by dividing the defending creature's hit points by the average damage of the attacking creature's attacks, 

\begin{align}
    N &= \frac{\HP}{\Dave(\Dhit, \AB, \AC\,)}
\end{align}
-->

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

If we plug Eqns. \eqref{eq:attack-hit-probability} and \eqref{eq:attack-crit-probability} into Eqn. \eqref{eq:attack-damage-average-abstract}, and if we assume a critical hit does twice the damage of a hit, $$\Dcrit \approx 2\,\Dhit$$, the average damage for an attack becomes

\begin{align}
    %\Dave &\approx \Dhit \left(\frac{22 + \AB - \AC\,}{20}\right) \nonumber \\\\ 
    \Dave &\approx \Dhit \cdot 0.05 \left(22 + \AB - \AC\,\right) \nonumber \\\\ 
          &= \Dhit \left(0.6 + 0.05 \left(10 + \AB - \AC\,\right)\right)  \nonumber \\\\ 
          &= 0.6 \cdot \Dhit \, \left(1 + 0.083 \left(10 + \AB - \AC\,\right)\right)\,.
    \label{eq:attack-damage-average-full}
\end{align}

The form of Eqn. \eqref{eq:attack-damage-average-full} may seem like an odd choice, but it allows us to take advantage of the following approximation, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which turns Eqn. \eqref{eq:attack-damage-average-full} into

\begin{align}
    \Dave \approx 0.6 \cdot \Dhit \cdot 1.083^{10 + \AB - \AC}\,.
    \label{eq:attack-damage-average-exp}
\end{align}

At this point we're ready to go back to our test equation. Putting Eqn. \eqref{eq:attack-damage-average-exp} into Eqn. \eqref{eq:uses-to-win} gives

\begin{align}
    N_\mathrm{attacks} &= \frac{\HP}{\Dave(\AB, \AC\,)} \nonumber \\\\\\
      &\approx \frac{\HP}{0.6 \cdot \Dhit \cdot 1.083^{10 + \AB - \AC}}\,.
    \label{eq:uses-to-win-attack}
\end{align}

Since $$x^{a + b} = x^a\,x^b$$, Eqn. \eqref{eq:uses-to-win-attack} can also be written as

\begin{align}
    N_\mathrm{attacks} &\approx \frac{\HP \cdot 1.083^{\AC - 13}}{0.6 \cdot \Dhit \cdot 1.083^{\AB - 3}}\,.
\end{align}

At this point our task is essentially done. We've successfully moved all the stats of the defending creature to the numerator, $$\HP$$ and $$\AC$$, and all the stats of the attacking creature in the denominator, $$\Dave$$ and $$\AB$$. The average number of attacks it takes the attacker to win can now be written in the form

\begin{align}
    N_\mathrm{attacks} \approx \frac{ \eHP \left(\HP,\AC\,\right)}{\eD \left(\Dhit, \AB\,\right)}\,,
\end{align}

where $$\eHP$$ is the defending creature's effective hit points and $$\eD$$ is the attacking creature's effective damage, which are given by

\begin{align}
    \eHPatck &= \frac{1}{\sqrt{0.6}} \cdot \HP \cdot 1.083^{\AC - 13}\,, \label{eq:effective-hit-points-attack} \\\\ 
    \eDatck  &= \sqrt{0.6} \cdot \Dhit \cdot 1.083^{\AB - 3}\,. \label{eq:effective-damage-attack}
\end{align}

It's worth pointing out that while Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-damage-attack} do satisfied equation \eqref{eq:uses-to-win-attack}, they are not the only solutions to our problem. I've chosen these particular forms for our effective hit points and effective damage for two reasons. First, the factors of $$-13$$ ($$-3$$) in the exponents were chosen to match the minimum $$\AC$$ $$(\AB\,)$$ values listed in the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275). And second, the factors of $$\sqrt{0.6}$$ in front mean that $$\eHPatck(\HP, 13)\cdot\eDatck(\Dhit, 3) = \HP\cdot\Dhit$$. Neither of these are strict requirements, but they will prove useful later on when calculating a creature's XP which I will cover in a future post.

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
    %\Dave &= \Dfail \left(\frac{DC - SB - 1}{20}\right) \nonumber \\\\ 
    \Dave &= \Dfail \cdot 0.05 \left(DC - SB - 1\,\right) \nonumber \\\\ 
          &= \Dfail \left(0.6 + 0.05 \left(DC - SB - 13\,\right)\right) \nonumber \\\\ 
          &= 0.6 \cdot \Dfail \left(1 + 0.083 \left(DC - SB - 13\,\right)\right) \nonumber \\\\ 
          &\approx 0.6 \cdot \Dfail \cdot 1.083^{DC - SB - 13}\,.
    %\Dave = \Dfail \left(\frac{DC - SB - 1}{20}\right) \approx \Dfail 1.05^{DC - SB - 21}\,.
    \label{eq:save-damage-average-none-exp}
\end{align}

Here, I've used the same approximation I used for attacks, $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, to arrive at the equation's final form.

Calculating the number of times a creature needs to use their saving throw effect in order to defeat another creature gives

\begin{align}
    N \approx \frac{\HP \cdot 1.083^{\SB}}{0.6 \cdot \Dfail \cdot 1.083^{\DC - 13}}\,,
    \label{eq:saves-to-win-none}
\end{align}

which can be expressed in terms of $$\eHP$$ and $$\eD$$ using the following definitions,

\begin{align}
    \eHPsave &= \frac{1}{\sqrt{0.6}} \cdot \HP  \cdot {1.083}^{\SB}\,, \label{eq:effective-hit-points-save} \\\\ 
    \eDsave  &= \sqrt{0.6} \cdot \Dfail \cdot {1.083}^{\DC - 13}\,. \label{eq:effective-damage-save}
\end{align}

Just like in the previous section with attacks, I chosen the factor of $$-13$$ in the exponent of Eqn. \eqref{eq:effective-damage-save} to match the minimum $$\DC$$ value listed in the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275). It's worth noting that the DMG doesn't actually list recommended values for $$\SB$$, which is an unfortunate oversight, but the suggested minimum value presented here of $$+0$$ is significant, as I'll discuss later on in this post.

The form of the effective hit points in Eqn. \eqref{eq:effective-hit-points-save} poses another interesting problem because every creature has six different $$\SB$$ values, one for each ability score. If we think of each ability score's $$\SB$$ value as representing a creatures defense against one avenue of effect, then their overall defense against saving throw effects can be represented by averaging across all ability scores,

\begin{align}
    \SBave = \sum \SB_i / 6\,, \label{eq:average-save-bonus} \\\\ 
\end{align}

where the sum is carried out over all six ability scores. This may be a bit too simplistic of an approach, though, as not all ability scores are targeted equally by saving throw effects. However, it will do for the time being.


# Discussion

Now that we've derived equations for effective hit points and effective damage, I'd like to spend some time discussing what they mean and where to go from here.

## Saving throw bonus scaling

One important thing that these equations show is how saving throw bonuses should scale in comparison to $$\AC$$. The [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop\#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG (p. 275) lists suggested values for monster's $$\HP$$, $$\AC$$, and $$\DC$$ but it doesn't list one for $$\SB$$. However, if we compared Eqns. \eqref{eq:effective-hit-points-attack} and \eqref{eq:effective-hit-points-save} then it becomes clear that $$\SB$$ should scale as $$\AC - 13$$.

<figure id="fig:monster-save-modifier-trends">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/effective-hp-and-damage/monster-save-modifier-trends.svg">
    <figcaption>Figure 1: Average saving throw modifiers (proficiency bonus not included) and armor class for monsters from official source books.</figcaption>
</figure>

Figure <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a>, above, shows this relationship for published monsters (I've excluded saving throw proficiency bonuses here because the DMG has separate rules for how much they should be valued in terms of an adjusted $$\AC\,$$). The saving throw modifiers for monsters clearly show a similar trend to $$\AC - 13$$ for all abilities but Dexterity, which is reassuring.

It's been well established that certain saving throws for monsters are weaker than others (see my earlier post [Monster Saving Throws]({{ site.url }}{{ site.baseurl }}{% link _monsters/monster-saving-throws.md %})). However, what hasn't been clear until now is whether the strong saving throws are overpowered or the weak saving throws are underpowered. What Fig. <a href="#fig:monster-save-modifier-trends" class="fig-ref">1</a> shows is that, for monsters, Strength and Constitution modifiers are generally on target at middle CRs and slightly overpowered at very high and very low CR, while Intelligence, Wisdom, and Charisma saving throws are all on target at very high and very low CRs and slightly underpowered in the middle. Finally, monster Dexterity modifiers are on target at very low CRs and increasingly underpowered at CR increases.

## Putting it all together

As it stands now, we have two ways of calculating effective hit points and two ways of calculating effective damage. 

For damage, this doesn't pose any potential conflict. We can simply pick whichever equation best fits how are creature is dealing damage. If we wanted to calculate the effective damage per round $$(\eDPR)$$ for a creature that deals damage using one attack and one saving throw effect, we can simply add the effective damage of the two together. Put more generally,

\begin{align}
    \eDPR = \sum \eDatck \left(\Dhit, \AB\,\right)  + \sum \eDsave \left(\Dfail, \DC\,\right)\,,
    \label{eq:effective-dpr-general}
\end{align}

where the first summation includes all of the attacks the creature is likely to use during the round, and the second summation includes all of the saving throw effects.

For hit points, however, this raises a difficult question. Which formulation, Eqn. \eqref{eq:effective-hit-points-attack} or \eqref{eq:effective-hit-points-save}, should we use to reflect a creature true defensive strength? The simple answer, of course, is to just average between the two, as was done previously to account for each ability score having its own saving throw bonus,

\begin{align}
    \eHP = \frac{1}{\sqrt{0.6}} \cdot \HP  \cdot {1.083}^{\frac{1}{2}\left(\AC - 13\right) + \frac{1}{2} \left(\SBave\right)}\,.
\end{align}

This assumes that a creature is just as likely to be subjected to a damaging attack as they are a damaging saving throw effect, and that the saving throw effects target each of the creature's ability scores equally. Again, this may not be the best assumption, but how all this is weighted can easily be adjusted to account for differences discovered later on.

# Conclusion

In this post I've shown how effective hit points and effective damage can be derived for creatures using the underpinning math of how attacks and saving throws work in D&D 5th edition. These allow a creatures defensive and offensive strength to be calculated in absolute terms, without the need of a second creature for comparison. For damage, this allows both attacks and saving throw effects to be added together and weighted equally. And for hit points, this allows an overall defensive strenth to be calculated that combines armor class as well as saving throw bonuses. 

In the process, I've also shown how monster ability score modifiers can be expected to scale with CR in a way similar to how the DMG recommends scaling armor class. 

For anyone who stuck through all that to the end, congratulations! Compared to many of my previous posts, this one doesn't contain that much in terms of useful insights into the game. But it does lay the ground work needed for much more to come.