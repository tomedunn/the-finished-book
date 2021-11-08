---
title: "Stunning Strike"
excerpt: "Analysis of how Stunning Strike holds up against published monsters"
share: true
date: 2021-10-27
last_modified_at: 2021-11-03
#tags:
#  - analysis
#  - classes
#  - monk
#  - stunning strike
#  - saving throws
---

# Introduction

Over the years, I've seen countless debates online around how strong the monk Stunning Strike feature is. In the early days of 5th edition the consensus seemed to be that Stunning Strike was extremely strong. However, in the last few years that consensus has changed within some portions of the online D&D community to Stunning Strike being considered weak instead. 

The reason often cited for this change is that Stunning Strike relies on Constitution saving throws which higher CR monsters generally strong against. This line of argument seems reasonable enough, but does the data actually support it? This is the question I'll be attempting to answer here.

# Method

The probability of monster failing the Constitution saving throw against being stunned can be calculated using the following equation.

$$ p_{\rm stun} = \frac{ {\rm min}(20, {\rm max}(0, DC - SB - 1)) }{ 20 } $$

Here, DC is the monk's ki save DC and SB is the monster's Constitution saving throw bonus. The maximum and minimum functions are there to keep the probability between 0 and 1.

The monk that we will be calculating this for is assumed to have 16 Dexterity and 16 Wisdom at 1st level. They then takes +2 Dexterity for their Ability Score Improvement at 4th level, +2 Wisdom at 8th level, +2 Dexterity at 12th level, and finally +2 Wisdom at 16th level.

The monsters our monk will be facing come from a range of CRs around the monk's level. The CR range our monk will face at level 5 is CRs 1-9, at level 10 they'll face CRs 5-15, at level 15 they'll face CRs 9-21, and at level 20 they'll face CRs 13-27. These ranges were picked to reflect that PCs typically face a wide range of monster CRs. The number of monsters tends to decrease as CR increases, which roughly fits with how CR impacts the number of monsters in a typical encounter.

As a final note, I have divided monsters up into three broad categories. A full description can be found [here]({% link _monsters/categorizing-monsters.md %}), but simply put, **Generic** monsters are templates for a certain type of monsters, **Legendary** monsters are templates for monsters with legendary traits, and **Unique** monsters each represent a singular NPC and have a unique stat block which may or may not have legendary traits. 

# Analysis

## Probability of Stunning a Monster

Applying the above formula for our monk to monsters taken from official source books published by WotC shows the following.

<center>
<figure style="width:1200px;min-width:50%;max-width:100%" alt="Stunning Strike probability distribution">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-probability-distribution-categories.svg">
    <figcaption>Distribution of Stunning Strike probabilities.</figcaption>
</figure>
</center>

Right away we see why our monster categories are important. While the shape of the distribution for Generic monsters widens as our monk levels up, the average remains fairly consistently around 50%. Unique monsters, though, have a similar distribution to Generic monsters at levels 5 and 10, but shift much more towards the lower end of the spectrum for levels 15 and 20. Finally, Legendary monsters are nearly absent from our level 5 distribution and for levels 10, 15, and 20 they skew consistently towards lower chances of being stunned.

To further illustrate these observations, the previous data is plotted again below. These shows the average stun probability (dashed line), along with the 80% confidence interval (shaded region) for each category of monsters.

<center>
<figure style="width:1200px;min-width:50%;max-width:100%" alt="Stunning Strike probability range">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-probability-inner-quantile80-categories.svg">
    <figcaption>Average probability of landing a Stunning Strike along with 80% confidence interval.</figcaption>
</figure>
</center>

The strength of Stunning Strike for our monk at higher levels, therefore, depends strongly on which category of monsters the DM tends to draw from. If the DM chooses to use Legendary and Unique monsters exclusively at higher levels, then the strength of Stunning Strike is likely to decrease as our monk levels up. However, if the DM chooses to use exclusively Generic monsters then the strength of Stunning Strike will remain largely unchanged.


## Ki per Stun

Another useful way of looking at this data is to calculate the average ki our monk needs to expend in order to successfully stun a monster. Since the probability of our monk needed to spend "X" ki points in order to successfully stun a specific monster follows the binomial distribution, the average number of ki needed for each monster is calculated by taking the inverse of their probability of being stunned from a single Stunning Strike. For example, if our monk had a 25% chance of stunning some monster then they would need to spend $$1/0.25 = 4$$ ki on average to stun that monster.

<center>
<figure style="width:1200px;min-width:50%;max-width:100%" alt="Ki per stun probability distribution">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/ki-per-stun-probability-distribution-categories.svg">
    <figcaption>Probability distribution of average ki needed to land a Stunning Strike.</figcaption>
</figure>
</center>

The above plots show how the average ki cost per stun is distributed for each of the level ranges we've looked at so far.

For our monk at levels 5 and 10, the distribution for Generic monsters is sharply peaked around 2 ki per stun. Indeed, when we calculated the median values for these levels we get an average cost of 1.82 ki per stun. For levels 15 and 20, the distributions still have a strong peak around 2 ki per stun, but they also have a longer tail. Still, the vast majority of monsters take 4 ki per stun or less. The calculated median values for these levels are 2.0 and 2.2 ki per stun respectively.

For Legendary and Unique monsters the story is similar, however, the size of the tails are much larger compared to the Generic monsters. For Legendary monsters the median is 2.0 ki per stun at 5th level, 2.9 ki per stun at 10th level, 2.9 ki per stun at 15th level, and 2.5 ki per stun at 20th level. And, for Unique monsters the median is 2.0 ki per stun at 5th level, 1.8 ki per stun at 10th level, 2.0 ki per stun at 15th level, and 2.9 ki per stun at 20th level.

<center>
<figure style="width:1200px;min-width:50%;max-width:100%" alt="Ki per stun probability range">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/ki-per-stun-probability-inner-quantile60-categories.svg">
    <figcaption>Average ki needed to land a Stunning Strike along with 60% confidence interval.</figcaption>
</figure>
</center>

These averages (dashed line) along with their 60% confidence intervals (shaded region) are plotted above.

In total, our monk will not experience a significant change in the effectiveness of Stunning Strike against Generic monsters, and on average they'll still fair decently well against both Legendary and Unique monsters. However, the lengths of the tails for Legendary and Unique monsters at higher levels makes it much more likely that our monk will face an important monster during their time adventuring that cannot practically be stunned.

## Attacks per Stun

In the same way the probability of stunning a monster was calculated for a single use of Stunning Strike, the probability of an attack resulting in a successful stun can also be calculated. 

<center>
<figure style="width:1200px;min-width:50%;max-width:100%" alt="Attacks per stun probability range">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/attacks-per-stun-inner-quantile60-categories.svg">
    <figcaption>Average number of attacks needed to land a Stunning Strike along with 60% confidence interval.</figcaption>
</figure>
</center>

Without spending too much time focusing on the distributions, the above plots show how the median (dashed line) and 60% confidence interval (shaded region) change with level for each category of monster.

For generic monsters, the average number of attacks needed to successfully stun a monster stays close to 3 attacks per stun for all levels. However, for Legendary and Unique monsters the number of attacks is generally higher, at around 4 attacks per stun.

# Conclusion

When facing Generic monsters, the overall likelihood of stunning a monster with Stunning Strike, as well as the typical ki cost for doing so, does not change significantly as a monk levels up. And, when facing Legendary or Unique monsters, while the average probability and ki cost of stunning a monster don't change too much, the tails at the extreme end of the distributions become much more likely. So while on average things aren't likely to get worse, there's a non-trivial chance that a particular monk will end up facing Legendary and Unique monsters in their campaign for which Stunning Strike is not nearly as effective as it would have been in a similar encounter at lower levels.

# Extra Credit

For those wondering why the probability distributions of stunning a monster have two peaks at higher levels, this comes from the ever widening gap between monsters with proficiency in Constitution saves and those without. Since monsters' proficiency bonus scales with CR this gap gets wider the higher we go. And, since the frequency of monsters having saving throw proficiencies increases with CR as well, this second peak gets taller and taller.

<center>
<figure style="width:1200px;min-width:50%;max-width:100%" alt="Stunning Strike probability distribution by proficiency">
    <img src="{{ site.url }}{{ site.baseurl }}/classes/stunning-strike/stun-probability-distribution-proficient.svg">
    <figcaption>Distribution of Stunning Strike probabilities, grouped by whether or not monsters are proficient in Constitution saving throws.</figcaption>
</figure>
</center>
