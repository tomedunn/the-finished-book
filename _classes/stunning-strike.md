---
title: "Stunning Strike"
excerpt: "Analysis of how Stunning Strike holds up against published monsters"
share: true
date: 2021-10-27
last_modified_at: 2022-11-24
tags:
  - analysis
  - classes
  - monk
  - saving throws
  - stunning strike
---

<div style="display:none">
\(
\newcommand{\AC}{\mathit{AC}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\DC}{\mathit{DC}}
\newcommand{\SB}{\mathit{SB}}
\newcommand{\phit}{\rho_\mathrm{hit}}
\newcommand{\pstun}{\rho_\mathrm{stun}}
\)
</div>

# Introduction

Over the years, I've seen countless debates online around how strong the monk Stunning Strike feature is. In the early days of 5th edition the consensus seemed to be that Stunning Strike was extremely strong. However, in the last few years that consensus has changed within some portions of the online D&D community to Stunning Strike being considered weak instead. 

The reason often cited for why Stunning Strike is weak is that it relies on Constitution saving throws which monsters are generally strong against, especially at higher CRs. As I showed previously in my post on [Monster Saving Throws]({{ site.data.page-links.monster-saving-throws.path }}), there is some truth to this. However, the topic definitely warrants a more in-depth look.

In this post, I'll be taking a deep dive into how Stunning Strike holds up against published monsters from official source books.

# Method

In order to assess how often Stunning Strike can successfully stun a monster we need to be able to calculate the probability that monster fails the Constitution saving throw against the effect, as well as the probability that the monster is hit by an attack from a monk in the first place. 

We can express the probability of a monster failing the Constitution saving throw against being stunned as 

\begin{equation}
    \label{eq:prob-stun}
    \pstun = \frac{ {\rm min}(20, {\rm max}(0, \DC - \SB - 1)) }{ 20 }\ ,
\end{equation}

where $$\DC\,$$ is the monk's ki save difficulty class, and $$\SB\,$$ is the monster's Constitution saving throw bonus. The maximum and minimum functions are there to keep the probability between 0 and 1.

The probability of an attack hitting a monster can be calculated in a similar manner as

\begin{equation}
    \label{eq:prob-hit}
    \phit = \frac{ {\rm min}(19, {\rm max}(1, 21 + \AB - \AC)) }{ 20 }\ ,
\end{equation}

where $$\AB\,$$ is the monk's attack bonus, and $$\AC\,$$ is the monster's armor class. Here, the maximum and minimum functions keep the probability above 5%, to reflect the chance of rolling a critical hit on a natural 20, and below 95%, to reflect the chance of rolling a critical miss on a natural 1.

The monk that we will be calculating this for is assumed to have 16 Dexterity and 16 Wisdom at 1st level. They then takes +2 Dexterity for their Ability Score Improvement at 4th level, +2 Wisdom at 8th level, +2 Dexterity at 12th level, and finally +2 Wisdom at 16th level.

The monsters our monk will be facing come from a range of CRs around the monk's level. The CR range our monk will face at level 5 is CRs 1-9, at level 10 they'll face CRs 5-15, at level 15 they'll face CRs 9-21, and at level 20 they'll face CRs 13-27. These ranges were picked to reflect that PCs typically face a wide range of monster CRs. The number of monsters tends to decrease as CR increases, which roughly fits with how CR impacts the number of monsters in a typical encounter.

As a final note, I have divided monsters up into three broad categories. A full description can be found [here]({{ site.data.page-links.categorizing-monsters.path }}), but simply put, **Generic** monsters are non-specific templates for certain types of monsters, **Legendary** monsters similar but with legendary traits, and **Unique** monsters each represent a specific, named NPC and have a unique stat block which may or may not have legendary traits.

In most campaigns, the vast majority of monsters come from the Generic category with occasional Legendary and Unique monsters thrown in as bosses or plot important NPC.

# Analysis

## Probability of Stunning a Monster

Using Eqn. \eqref{eq:prob-stun}, the probability of our monk landing a Stunning Strike can be calculated for a wide array of monsters taken from official source books. To understand how likely it is for our monk to encounter a monster with a given probability of being stunned, Fig. <a href="#fig:stun-prob-dist-categories" class="fig-ref">1</a> below groups monsters by their Stunning Strike probability and plots the number of monsters in each category.

<figure alt="Stunning Strike probability distribution" id="fig:stun-prob-dist-categories">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-probability-distribution-categories.svg" style="width:100%">
    <figcaption>Figure 1: Distribution of Stunning Strike probabilities.</figcaption>
</figure>

Right away we see why our monster categories are important for this analysis. While the shape of the distribution for Generic monsters widens as our monk levels up, the average remains fairly consistently around 50%. Unique monsters, though, have a similar distribution to Generic monsters at levels 5 and 10, but shift much more towards the lower end of the spectrum for levels 15 and 20. Finally, Legendary monsters are nearly absent from our level 5 distribution and for levels 10, 15, and 20 they skew consistently towards lower chances of being stunned.

To further illustrate these observations, the previous data is plotted again in Fig. <a href="#fig:stun-prob-conf80-categories" class="fig-ref">2</a> below. It shows the average stun probability (dashed line), along with the 80% confidence interval (shaded region) for each category of monsters.

<figure alt="Stunning Strike probability range" id="fig:stun-prob-conf80-categories">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-probability-confidence80-categories.svg" style="width:100%">
    <figcaption>Figure 2: Average probability of landing a Stunning Strike along with 80% confidence interval.</figcaption>
</figure>

The strength of Stunning Strike for our monk at higher levels, therefore, depends strongly on which category of monsters the DM tends to draw from. If the DM chooses to use Legendary and Unique monsters exclusively at higher levels, then the strength of Stunning Strike is likely to decrease as our monk levels up. However, if the DM chooses to use exclusively Generic monsters then the strength of Stunning Strike will remain largely unchanged.


## Ki per Stun

Another useful way of looking at this data is to calculate the average ki our monk needs to expend in order to successfully stun a monster. Since the probability our monk needs to spend "X" ki points in order to successfully stun a specific monster follows the binomial distribution, the average number of ki needed for each monster is calculated by taking the inverse of their probability of being stunned from a single Stunning Strike. For example, if our monk had a 25% chance of stunning a particular monster then they would need to spend 1 / 0.25 = 4 ki on average to do so.

<figure alt="Ki per stun probability distribution" id="fig:ki-per-stun-prob-dist-categories">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/ki-per-stun-probability-distribution-categories.svg" style="width:100%">
    <figcaption>Figure 3: Probability distribution of the average ki needed to land a Stunning Strike.</figcaption>
</figure>

Figure <a href="#fig:ki-per-stun-prob-dist-categories" class="fig-ref">3</a> show how the average ki cost per stun is distributed for each of the level ranges we've looked at so far.

For our monk at levels 5 and 10, the distribution for Generic monsters is sharply peaked around 2 ki per stun. Indeed, when we calculated the median values for these levels we get an average cost of 1.82 ki per stun. For levels 15 and 20, the distributions still have a strong peak around 2 ki per stun, but they also have a longer tail. Still, the vast majority of monsters take 4 ki per stun or less. The calculated median values for these levels are 2.0 and 2.2 ki per stun respectively.

For Legendary and Unique monsters the story is similar, however, the size of the tails are much larger compared to Generic monsters. For Legendary monsters the median is 2.4 ki per stun at 5th level, 2.5 ki per stun at 10th level, 2.5 ki per stun at 15th level, and 2.5 ki per stun at 20th level. And, for Unique monsters the median is 2.0 ki per stun at 5th level, 1.8 ki per stun at 10th level, 2.2 ki per stun at 15th level, and 3.3 ki per stun at 20th level.

<figure alt="Ki per stun probability range" id="fig:ki-per-stun-prob-dist-conf60-categories">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/ki-per-stun-probability-confidence60-categories.svg" style="width:100%">
    <figcaption>Figure 4: Average ki needed to land a Stunning Strike along with 60% confidence interval.</figcaption>
</figure>

These averages (dashed line) along with their 60% confidence intervals (shaded region) are plotted above, in Fig. <a href="#fig:ki-per-stun-prob-dist-conf60-categories" class="fig-ref">4</a>.

In total, our monk will not experience a significant change in the effectiveness of Stunning Strike against Generic monsters, and on average they'll still fair decently well against both Legendary and Unique monsters. However, the lengths of the tails of the distributions for Legendary and Unique monsters at higher levels makes it much more likely that our monk will face an important monster during a campaign that cannot practically be stunned.

## Attacks per Stun

In the same way the number of ki needed to stun a monster was calculated, the number of attacks needed to stun a monster can be calculated as well using Eqns. \eqref{eq:prob-stun} and \eqref{eq:prob-hit}. 

<figure alt="Attacks per stun probability range" id="fig:attacks-per-stun-conf60-categories">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/attacks-per-stun-confidence60-categories.svg" style="width:100%">
    <figcaption>Figure 5: Average number of attacks needed to land a Stunning Strike along with 60% confidence interval.</figcaption>
</figure>

Without spending too much time focusing on the distributions, Fig. <a href="#fig:attacks-per-stun-conf60-categories" class="fig-ref">5</a> shows how the median number of attacks needed to land a Stunning Strike (dashed line) and 60% confidence interval (shaded region) change with our monk's level for each category of monster.

For generic monsters, the average number of attacks needed to successfully stun a monster stays close to 3 attacks per stun for all levels. However, for Legendary and Unique monsters the number of attacks is generally higher, ranging between 3 and 4 attacks per stun.

## Spellcaster Comparison

To put all of this into context, lets look at how Stunning Strike holds up against similar abilities for spellcasters. Specifically, lets look at the effectiveness of spells that rely on Wisdom saving throws, which is the most common save for spells that produce effects similar to Stunning Strike. 

For the purpose of this comparison, I'll be using an example spellcaster that starts off with a spellcasting ability score of 16 at 1st level, increases it by +2 using their Ability Score Improvement at 4th level, and another +2 at 8th level.

Figure <a href="#fig:stun-spell-prob-conf80-categories" class="fig-ref">6</a>, shown below, compares the average stun probability (red dashed line), along with the 80% confidence interval (red shaded region), with the average probability of landing a spell with a Wisdom saving throw (blue dashed line), along with the 80% confidence interval (blue shaded region), for each category of monsters.

<figure alt="Stunning Strike and Wisdom spell save probability range" id="fig:stun-spell-prob-conf80-categories">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-spell-probability-confidence80-categories.svg" style="width:100%">
    <figcaption>Figure 6: Average probability of landing a Stunning Strike and 80% confidence interval (red) along with probability of landing a spell with a Wisdom saving throw and 80% confidence interval (blue).</figcaption>
</figure>

For level 10 and below, Stunning Strike has about a 10% lower chance to land on average compared to our spellcaster's Wisdom saving throw spells against Generic and Unique monsters. However, at level 15 this average gap drops to below 5% and at level 20 Stunning Strike is actually more likely to land on average. Meanwhile, against Legendary monsters Stunning Strike and spells with Wisdom saves are very similar at all levels, with Stunning Strike coming out a touch lower (less than 5%) for levels 10 and above.

In addition to this, the width of the distribution is generally narrower for Stunning Strike. Meaning, Stunning Strike will produce more consistent results than spells that use Wisdom saving throws. The reason for this difference in consistency comes almost entirely from the Magic Resistance monster trait that grants monsters advantage on saving throws against spells and magical effect. 

For Stunning Strike, the probability distribution is influence by the distribution in monster Constitution modifiers as well as whether each monster is proficient in Constitution saving throws. Spells with Wisdom saving throws are influence by both of these things for Wisdom, as well as whether or not the monster has the Magic Resistance trait, which is increasingly common as monster CR increases.

# Conclusion

In total, these results paint a very different picture than what is often discussed when comparing Stunning Strike to spells that produce similar effects. The gap between Stunning Strike and Wisdom saving throw spells is actually largest at lower level. At higher levels, Stunning Strike produces more consistent results against Generic monsters, is comparable with Wisdom spell saves against Legendary monsters, and is actually better than Wisdom spell saves against Unique monsters.

When facing Generic monsters, the overall likelihood of stunning a monster with Stunning Strike, as well as the typical ki cost for doing so, does not change significantly as a monk levels up. And, when facing Legendary or Unique monsters, while the average probability and ki cost of stunning a monster don't change too much, the tails at the extreme end of the distributions become much more likely. So while on average things aren't likely to get worse, there's a non-trivial chance that a particular monk will end up facing Legendary and Unique monsters in their campaign for which Stunning Strike is not nearly as effective as it would have been in a similar encounter at lower levels.

# Extra Credit

For those wondering why the probability distributions of stunning a monster have two peaks at higher levels, as shown in Fig. <a href="#fig:stun-prob-dist-prof" class="fig-ref">7</a>, this comes from the ever widening gap between monsters with proficiency in Constitution saves and those without. Since monsters' proficiency bonus scales with CR this gap gets wider the higher we go. And, since the frequency of monsters having saving throw proficiencies increases with CR as well, this second peak gets taller and taller.

<figure alt="Stunning Strike probability distribution by proficiency" id="fig:stun-prob-dist-prof">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-probability-distribution-proficient.svg" style="width:100%">
    <figcaption>Figure 7: Distribution of Stunning Strike probabilities, grouped by whether or not monsters are proficient in Constitution saving throws.</figcaption>
</figure>