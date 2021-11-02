---
title: "Monster CR and XP"
excerpt: "How to calculate CR and XP and how published monsters compare to expectation."
---

# Introduction

Chapter 9 of the _Dungeon Master's Guide_ (DMG) contains a section called "Creating a Monster" which outlines
how to calculate CRs for homebrew monsters. By the rules own admission, this calculated CR is intended
to act more as an initial estimate than a final value, with the final CR determined, instead, through 
playtesting.

Having CR ultimately rely on playtesting makes sense given how the rules calculate CR. However, a natural
question emerges from this process: how accurate are the calculations presented in the DMG?

In this post, I take a detailed look at how the listed CRs for monsters in official 5th edition products 
compare to those calculated using the method outlined in the DMG.

# Calculating CR

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

## Defensive CR

Defensive CR (D-CR) is calculated from a monster's adjusted HP and adjusted AC. The most common 
adjustments to a monster's HP comes from resistances and immunities to multiple damage types, health regeneration, 
healing, and legendary resistances. For AC, the most common adjustments are abilities that give attackers disadvantage 
on attacks, reactions that temporarily raise AC, and proficiencies in multiple saving throws.

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/monster-cr-and-xp/hp-vs-cr.png">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/monster-cr-and-xp/ac-vs-cr.png">
    <figcaption>Hit points and armor class vs CR (adjusted and unadjusted).</figcaption>
</figure>

The above figure shows how published creatures compare, on average, against the HP and AC targets listed in the DMG.

For HP, while adjusted HP closely matches the expected target on average, unadjusted HP consistently falls short. For
AC, though, the unadjusted AC generally match the expected target on average, while the adjusted AC comes out consistently 
higher than expected with the biggest difference coming from monsters CR 17 and above. The differences in adjusted AC 
might seem like a large discrepancy, but recall that AC acts only as a minor adjustment to a monster's overall D-CR.

<center>
<figure style="width: 500px">
    <img src="/monsters/monster-cr-and-xp/d-cr-vs-cr.png">
    <figcaption>Calculated defensive CR mean and inner 60% quantile vs CR.</figcaption>
</figure>
</center>

The above figure shows how the average calculated D-CR compares with the expected value. 
Overall, D-CR appears to be on target with the average D-CR for published monsters, coming within +/- 1 of target on
average. It's worth noting that the biggest differences come from the extreme ends of the CR spectrum, with very low CR 
monsters showing consistently lower D-CR than expected and very high CR monsters showing consistently higher D-CR than 
expected.

## Offensive CR

Offensive CR (O-CR) is calculated from a monster's DPR and adjusted AB. The most common adjustments to AB are abilities
that give advantage on attack rolls.

<figure class="half">
    <img src="/monsters/monster-cr-and-xp/dpr-vs-cr.png">
    <img src="/monsters/monster-cr-and-xp/ab-vs-cr.png">
    <figcaption>Damage per round and attack bonus vs CR (adjusted and unadjusted).</figcaption>
</figure>

The above figure shows how published creatures compare, on average, against the DPR and AB targets listed in the DMG.
AB shows little to no difference between adjusted and non-adjusted values.

<center>
<figure style="width: 500px">
    <img src="/monsters/monster-cr-and-xp/o-cr-vs-cr.png">
    <figcaption>Calculated offensive CR mean and inner 60% quantile vs CR.</figcaption>
</figure>
</center>

The above figure shows how the average calculated O-CR compares with the expected value. 
On average, the calculated O-CR closely matches the expected target and is rarely more than +/- 1 away across the full 
range of CRs. The width of the distribution is also generally narrower than what was observed for D-CR, except for CRs 
between 12 and 20 where the distribution is generally wider.

# Combined CR

The CR for each monster is calculated by taking the average of the D-CR and O-CR values calculated previously. The
results of this are shown in the figure below.

<center>
<figure style="width: 500px">
    <img src="/monsters/monster-cr-and-xp/dmg-cr-vs-cr.png">
    <figcaption>Calculated CR mean and inner 60% quantile vs CR.</figcaption>
</figure>
</center>

As with D-CR and O-CR, the calculated CR for published monsters closely matches the listed values on average. It is 
interesting to note that the calculated CR is more accurate than either of the component D-CR and O-CR.

<!---
# Calculating XP
A monster's XP can be calculated using the following equation



$$XP_{\rm NPC} = \frac{1}{4} HP \cdot DPR \cdot 1.05^{AB + AC - 14}$$

$$XP_{\rm NPC} = \frac{1}{4} eHP \cdot eDPR$$

where 

$$eDPR = DPR \cdot 1.05^{AB - 2}$$

$$eHP = HP \cdot 1.05^{AC - 12}$$

![Calculated XP vs target XP](calculated-xp-vs-target-xp.png)

![Calculated CR vs target CR](calculated-cr-vs-cr.png)
--->

