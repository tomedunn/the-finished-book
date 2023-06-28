---
title: "Calculating Monster CR"
excerpt: "Compares listed monster CRs with those calculated according to the rules in chapter 9 of the DMG."
date: 2021-10-30
last_modified_at: 2023-06-27
tags:
  - analysis
  - challenge rating
  - monsters
---

# Introduction

Chapter 9 of the _Dungeon Master's Guide_ (DMG) contains a section called "Creating a Monster" which outlines
how to calculate CRs for homebrew monsters. By the rules own admission, this calculated CR is intended
to act more as an initial estimate than a final value, with the final CR determined through playtesting.

Having CR ultimately determined through playtesting makes sense given the complexity of the task at hand. However, 
it also raises the question: how accurate are the CR calculations presented in the DMG?

In this post, I aim to answer this question by taking a detailed look at how CRs for monsters in official 5th 
edition products compare to those calculated using the method outlined in the DMG. You can find a summary of the 
monster dataset used for this analysis [here]({{ site.url }}{{ site.baseurl }}{% link _monsters/monster-dataset.md %}).

# Calculating CR

Without going into too much detail, here's a high level summary of how to calculate CR according to the DMG.
First, determine the monster's effective hit points (HP), armor class (AC), average damage per round (DPR), 
and attack bonus (AB) or saving throw difficulty class (DC). Second, compare those with values listed in the 
Monster Statistics by Challenge Rating table to determine the monster's defensive CR (D-CR) and offensive CR (O-CR).
And finally, average the monster's D-CR and O-CR together to get the monster's CR.

For simple monsters, like a **[brown bear](https://www.dndbeyond.com/monsters/brown-bear)**, that have no special 
abilities, resistances, immunities, and such, this is a straight forward process. However, for more complicated 
monsters adjustments need to be made to the monster's HP, AC, DPR, and AB in order to make the calculations work.
I'll talk a bit more about these adjustments later on.

<!---
At a high level, the method for calculating CR in the DMG involves calculating a monsters defensive CR (D-CR)
and offensive CR (O-CR) and averaging the two together. A monster's D-CR is determined primarily from 
their hit points (HP), with some minor adjustments from their armor class (AC). And their O-CR is determined
primarily from their average damage per round (DPR), with some minor adjustments from their attack bonus (AB)
or saving throw difficulty class (DC).

For simple monsters, like a **[brown bear](https://www.dndbeyond.com/monsters/brown-bear)**, that have no special 
abilities, resistances, immunities, and such, this is a straight forward process. For more complicated monsters,
though, adjustments need to be made to the monster's HP, AC, DPR, and AB in order to make the calculations work.

As a consiquence of this, when comparing published monsters to what's described in the DMG for a typical monster 
of the same CR, these adjusted HP, AC, DPR, and AB should be used instead of the unadjusted values.

Thankfully, the DMG does provide guidance for making these adjustments for a wide range of monster traits, 
including damage resistances, immunities, legendary resistances, multiple saving throw proficiencies, and an array 
of monster features listed in the Monster Features table, also found in chapter 9. Of course, not every monster 
feature or ability is covered, especially for monsters published in later source books and modules, and for these
creatures assumptions need to be made in order to properly calculate a CR.
--->

## Defensive CR

Defensive CR (D-CR) is calculated from a monster's effective HP and AC. The most common adjustments to a monster's HP 
comes from resistances and immunities to multiple damage types, health regeneration, healing, and legendary resistances. 
HP is by far the stat that gets the most adjustments, and this is especially true for higher CR monsters. 

For AC, the most common adjustments are abilities that give attackers disadvantage on attacks, reactions that temporarily 
raise AC, and proficiencies in multiple saving throws. Like adjustments to HP, these adjustments play a larger role at 
higher CRs than they do at lower CRs. 

<figure class="half" id="fig:hp-and-ac-vs-cr">
    {% include_relative calculating-monster-cr/fig-hp-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-hp-vs-cr-large.html %}
    {% include_relative calculating-monster-cr/fig-ac-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-ac-vs-cr-large.html %}
    <figcaption>Figure 1: Hit points and armor class vs CR (adjusted and unadjusted).</figcaption>
</figure>

Figure <a href="#fig:hp-and-ac-vs-cr" class="fig-ref">1</a> shows how published creatures compare, on average, against the HP and AC targets listed in the DMG.

For HP, while average effective HP closely matches the DMG target, the average HP consistently falls short. For AC, 
though, the average AC generally match the DMG target, while the average effective AC comes out consistently higher than 
expected with the biggest difference coming from monsters CR 17 and above. 

The differences in effective AC might seem like a large discrepancy, but AC only acts as a minor adjustment to a monster's 
overall D-CR so the overall impact is relatively small. This impact is reflected in the calculated D-CR, which is shown in 
the Fig. <a href="#fig:d-cr-vs-cr" class="fig-ref">2</a> below.

<figure id="fig:d-cr-vs-cr">
    {% include_relative calculating-monster-cr/fig-d-cr-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-d-cr-vs-cr-large.html %}
    <figcaption>Figure 2: Calculated defensive CR mean and 60% confidence interval vs CR.</figcaption>
</figure>

Overall, D-CR appears to be on target, with the average D-CR for published monsters coming within +/- 1 of target. It's 
worth noting that the biggest differences come from the extreme ends of the CR spectrum, with very low CR monsters showing 
consistently lower D-CR than expected due to low effective HP, and very high CR monsters showing consistently higher D-CR 
than expected due to high effective AC.

## Offensive CR

Offensive CR (O-CR) is calculated from a monster's effective DPR and AB. DPR does have adjustments which typically take the 
form of damage that relies on specific conditions being true, such as the **Assassin's** Assassinate feature which allows 
them to score a critical hit against surprised creatures. However, I did not differentiate these sources of damage when 
calculating DPR for each monster and so, for the time being, they are not split apart from the effective DPR. The most common 
adjustments to AB are abilities that give advantage on attack rolls.

<figure class="half" id="fig:dpr-and-ab-vs-cr">
    {% include_relative calculating-monster-cr/fig-dpr-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-dpr-vs-cr-large.html %}
    {% include_relative calculating-monster-cr/fig-ab-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-ab-vs-cr-large.html %}
    <figcaption>Figure 3: Damage per round and attack bonus vs CR (adjusted and unadjusted).</figcaption>
</figure>

Figure <a href="#fig:dpr-and-ab-vs-cr" class="fig-ref">3</a> shows how published creatures compare, on average, against the DPR and AB targets listed in the DMG. 

Effective DPR closely matches the expected DPR values from the DMG for all but the highest CRs which tend to be a bit lower 
than expected. The DPR values shown here only include effective DPR. As mentioned earlier, there are adjustments made to DPR 
but these tend to be rare and relatively minor and its unlikely the unadjusted DPR differs significantly from the effective 
DPR values. 

Effective AB shows a similar story to effective AC. It is generally higher than the expected value and that difference is 
largest at higher CRs. However, unlike AC, there is little to no difference between effective AB and unadjusted values.

The combined impact of effective DPR and AB is shown in Fig. <a href="#fig:o-cr-vs-cr" class="fig-ref">4</a> below which shows how the average O-CR compares with the
expected values in the DMG.

<figure id="fig:o-cr-vs-cr">
    {% include_relative calculating-monster-cr/fig-o-cr-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-o-cr-vs-cr-large.html %}
    <figcaption>Figure 4: Calculated offensive CR mean and  60% confidence interval vs CR.</figcaption>
</figure>

On average, the calculated O-CR closely matches the expected target and is rarely more than +/- 1 away across the full 
range of CRs. The width of the distribution is also generally narrower than what was observed for D-CR, except for CRs 
between 12 and 20 where the distribution is generally wider. This widening of the distribution is due to the increased 
frequency of legendary monsters which tend to deal a bit more damage than non-legendary creatures within this CR range.

## CR

With D-CR and O-CR both calculated, the CR for each monster is calculated by taking the average of the two. The results of 
this are shown in Fig. <a href="#fig:dmg-cr-vs-cr" class="fig-ref">5</a> below.

<figure id="fig:dmg-cr-vs-cr">
    {% include_relative calculating-monster-cr/fig-dmg-cr-vs-cr-small.html %}
    {% include_relative calculating-monster-cr/fig-dmg-cr-vs-cr-large.html %}
    <figcaption>Figure 5: Calculated CR mean and 60% confidence interval vs CR.</figcaption>
</figure>

As with D-CR and O-CR, the calculated CR for published monsters closely matches the listed values on average. It's 
interesting to note that the calculated CR is more accurate than either of the component D-CR and O-CR.

# Conclusion
In conclusion, the methods for calculating CR in the DMG are generally pretty accurate at predicting a monster's final
CR. Effective AC and AB were generally about +2-4 higher than expected, but not enough to seriously overpower typical 
monsters. 

The large difference between effective HP and actual HP values for monsters poses an interesting problem 
that I'm sure many DMs grapple with regularly. It indicates that a significant portion of most monster's effective health
is dependent on the PCs strengths and weaknesses as well as how the PCs choose to engage the monster. However, that's
a discussion for another time.