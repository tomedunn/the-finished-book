---
title: "Monsters of the Multiverse"
excerpt: "How have the monsters in Mordenkainen Presents: Monsters of the Multiverse changed?"
date: 2023-06-21
last_modified_at: 2023-06-21
tags:
  - analysis
  - challenge rating
  - monsters
  - xp
---

{% include LaTex.html %}

# Introduction
In May of 2022, Wizards of the Coast released _Mordenkainen Presents: Monsters of the Multiverse_ (MotM) which included a large assortment of monsters that had been published previously in other source books, the overwhelming majority of which came from _Volo's Guide to Monsters_ (VGtM) and _Mordenkainen's Tome of Foes_ (MToF). While some of these republished monsters were unchanged, the majority include changes to their mechanics in one form or another.

These changes took several forms, including subtle formatting improvements. However, in this post I'll be focusing on the changes that impacted monster CRs, such as changes to their damage per round, hit points, attack bonuses, and armor class to name a few. 

Just as in my previous post looking at the CR accuracy of [early legendary monsters]({{ site.data.page-links.early-legendary-monsters.path }}), for this analysis I'll be using calculated XP values instead of CR when evaluating these changes. 


# Calculating XP
As I've covered previously (see [Calculating Monster XP]({{ site.data.page-links.calculating-monster-xp.path }}#calculating-xp)), a monster's XP value can be calculated directly from their offensive and defensive stats in the following way,
\begin{equation}
    \label{eq:XP-simple}
    \XP = \frac{1}{4} \eHP \cdot \eDPR\,,
\end{equation}
where $$\eHP\,$$ is the monster's effective hit points and $$\eDPR\,$$ is their effective damage per round. 

If you're interested in the details of how these are calculated, or where this all comes from, you can read more about it [here]({{ site.data.page-links.xp-and-encounter-balancing.path }}), but for our purposes you can simply think of $$\eHP\,$$ as how much defensive toughness a monster has, and $$\eDPR\,$$ as how much offensive power it has.

Looking at monsters in this way has several advantages. Not only does it allow for a more nuanced measure of how strong a monster is in combat, it also gives a much more direct measure of how changes to a monster's defensive and offensive stats impact their overall combat strength, and insights into how to rebalance monsters that aren't hitting their listed CR.


# Analysis
Before jumping into monster XP calculations, lets look at how the inputs to those calculations changed for the republished monsters. As shown in Fig. [1](#fig:stat-changes){: .fig-ref} (below), the most common type of change was to monster damage per round (DPR), with 55% of monsters (138 our of 252) having a different DPR in their republished form compared to its original. 

<figure alt="How monsters changed in MotM" id="fig:stat-changes">
    {% include_relative monsters-of-the-multiverse/fig-stat-changes-small.html %}
    {% include_relative monsters-of-the-multiverse/fig-stat-changes-large.html %}
    <figcaption>Figure 1: Shows the percent of monsters republished in <em>Mordenkainen Presents: Monsters of the Multiverse</em> that changed in each of the listed categories relative to how they appeared in earlier publications.</figcaption>
</figure>

Hit points (HP) comprised the second most common change, with 33% of monsters (82 out of 252) showing a difference. And changes to armor class (AC) and attack bonus (AB) were the least likely of the four, with 15% (38 out of 252) and 8% (21 out of 252) of monsters affected respectively.

For HP, DPR, and AB the majority of the changes were to the raw, or unadjusted stat, while for AC most were to the adjusted stat. This means that republished monsters were more likely to see a change to their defensive features, like the Magic Resistance trait, than to the AC value listed in their stat blocks.

In total, 63% (159 out of 252) of all monster republished in MotM saw some kind of change impacting their overall combat strength, i.e., their calculated XP and possibly their CR. And, when broken down by CR, as shown in Fig. [2](#fig:change-distribution){: .fig-ref} (below), we see that a significantly higher portion of these changes were directed at high CR monsters than at low CR monsters.

<figure alt="How monsters changed in MotM" id="fig:change-distribution">
    {% include_relative monsters-of-the-multiverse/fig-change-distribution-small.html %}
    {% include_relative monsters-of-the-multiverse/fig-change-distribution-large.html %}
    <figcaption>Figure 2: Shows the number of monsters republished in <em>Mordenkainen Presents: Monsters of the Multiverse</em> that changed for each CR.</figcaption>
</figure>

The overall impact that these changes had on the calculated XP values for monsters republished in MotM can be seen in Fig. [3](#fig:xp-ratio-vs-cr){: .fig-ref}, which shows the average ratio between monster XP values calculated using Eqn. \eqref{eq:XP-simple} and the XP value associated with their CR $$(\XP_{\CR})$$, as well as an $$80\%$$ confidence interval (i.e., $$80\%$$ of the monster fall within that range at each CR).

<figure alt="Monster XP vs CR" id="fig:xp-ratio-vs-cr">
    {% include_relative monsters-of-the-multiverse/fig-xp-ratio-vs-cr-small.html %}
    {% include_relative monsters-of-the-multiverse/fig-xp-ratio-vs-cr-large.html %}
    <figcaption>Figure 3: Shows average and \(80\%\) confidence interval for calculated monster XP values relative to listed XP values for monsters originally published in <em>Volo's Guide to Monsters</em> and <em>Mordenkainen's Tome of Foes</em>, and then republished in <em>Mordenkainen Presents: Monsters of the Multiverse</em>.</figcaption>
</figure>

The average XP for monsters republished in MotM shifts slightly closer to target for monsters CR 15 and above. But, the biggest change comes in the width of the distribution, with the $$80\%$$ confidence interval for MotM being significantly narrower than that of the original publications. 

This "tightening" of the distribution can also be seen in Fig. [4](#fig:xp-delta-vs-xp-ratio){: .fig-ref}, which plots the ratio between each republished monster's calculated XP value $$(\XP^{\,\prime}\,)$$ and original calculated XP value $$(\XP\,)$$ against the ratio of their original calculated XP value and the XP value listed for their CR. For example, the **[spring eladrin](https://www.dndbeyond.com/monsters/96548-spring-eladrin)** had an XP ratio of $$0.49 = \XP / \XP_{\CR}$$ when it was initially published in MToF, while its [republished](https://www.dndbeyond.com/monsters/2560921-spring-eladrin) XP increased by a factor of $$2.16 = \XP^{\,\prime} / \XP$$ for a final XP ratio of $$1.05 = \XP^{\,\prime} / \XP_{\CR}$$.

<figure alt="Monster XP vs CR" id="fig:xp-delta-vs-xp-ratio">
    {% include_relative monsters-of-the-multiverse/fig-xp-delta-vs-xp-ratio-small.html %}
    {% include_relative monsters-of-the-multiverse/fig-xp-delta-vs-xp-ratio-large.html %}
    <figcaption>Figure 4: Shows the ratio between calculated XP values for republished monsters and that of their original publication, as a function of their original calculated XP ralative to the target XP listed by their CR. The dashed line shows the correction needed to hit the XP target for the republished monsters.</figcaption>
</figure>

For monsters CR 6 and above, the change in XP for republished monsters closely follows the dashed line, which represents the theoretical correction needed to bring their XP in line with their CR's XP target, $$\XP_{\CR}$$,
\begin{equation}
    \label{eq:XP-correction}
    \frac{\XP^{\,\prime}}{\XP} = \frac{\XP_{\CR}}{\XP}\,.
\end{equation}

For monsters CR 5 and below, while some follow this trend, the majority fall a ways below it. Given my previous findings, that low CR monsters tend to be [weaker than expected]({{ site.data.page-links.calculating-monster-xp.path }}), it is likely that this trend reflects a similar correction but to a lower XP target than what's associated with their CR.


# Conclusion
To conclude, the republished monsters in MotM hit closer to to their CR than their original counterparts, improving the overall consistency of monster combat power at each CR compared to VGtM and MToF. This comes on top of the other changes to monster formatting and design that WotC has discussed, which should make these monsters easier to play at or near their intended CR as well.

The changes target high CR monsters more so than low CR monsters. While the changes to low CR monsters do tend to move their average XP closer to target, the republished monsters still hit well below that target. This further supports the idea that Wizards of the Coast is either intentionally erroring on the side of weaker monsters at low CR, or that their internal targets are slightly lower than those listed in chapter 9 of the _Dungeon Master's Guide_.


# Extra Credit
Before Wrapping this up, I'd like to touch on one other significant change seen in the republished monsters, as well as highlight a tool I've been working on over the past few months when I've had free time.

When I run this kind of analysis, I do the DPR calculations for each monster by hand, looking for the combination of abilities that maximize each creature's calculated XP. This process can be slow and a bit tedious, especially for source books with lots of monsters. It also leaves important bits of information out, like what types of damage each monster is doing, and how "non-optimal" DPR compares to "optimal".

To help automate this process, I've be developing a monster feature parser that's capable of doing these calculations for me. The parser isn't finished yet - it gives the correct answer for the vast majority of monster actions, including the Multiattack action - but it still needs to be expanded to cover spells, legendary actions, and mythic actions.

That said, it's now at the point where it's starting to give useful and reliable data for the things it does cover. So, as a preview, here's some preliminary data on how the types of damage dealt by monster attacks changed for the monsters republished in MotM.

<figure alt="Monster damage by type" id="fig:damage-by-type">
    {% include_relative monsters-of-the-multiverse/fig-damage-by-type-small.html %}
    {% include_relative monsters-of-the-multiverse/fig-damage-by-type-large.html %}
    <figcaption>Figure 5: Shows the amount of damage dealt of each type dealt by monsters from <em>Volo's Guide to Monsters</em> and <em>Mordenkainen's Tome of Foes</em>, as well as from <em>Mordenkainen Presents: Monsters of the Multiverse</em>. Data includes damage from monster actions, but not legendary actions, mythic actions, or spells.</figcaption>
</figure>

As Fig. [5](#fig:damage-by-type){: .fig-ref} shows (above), the republished monsters deal significantly more force damage, and significantly less physical damage (bludgeoning, piercing, and slashing) than their original counterparts on average. This shift is most dramatic at higher CRs, and is accompanied by a complete removal of the Magic Weapons trait found in some monsters, which asserted that a monster's weapon attacks be considered magical for the purposes of overcoming resistances and immunities to non-magical damage.


<!--

# Stats
There is no significant difference in the average trends for monster stats, including effective hit points, effective AC, effective DPR, and effective AB.

# Condition Immunities
Only four monsters had any change in condition immunities.

Corpse Flower: +Poisoned
Molydeus: +Blinded, +Deafened, -Exhaustion, 
Red Abishai: +Frightened
Yuan-ti Broodguard: +Charmed, +Paralyzed

# Damage Mitigation
A few monsters had their damage mitigations changed.

Alhoon: -Nonmagical Attacks immunity
Annis Hag: -Nonmagical Attacks resistance
Barghest: -Fire resistance
Bodak: -Lightning immunity, -Necrotic resistance, +Necrotic immunity
Boneclaw: -Nonmagical Attacks resistance
Clockwork Bronze Scout: -Nonmagical Attacks immunity
Clockwork Oaken Bolter: -Nonmagical Attacks immunity
Clockwork Stone Defender: -Nonmagical Attacks immunity
Eladrin, Autumn: -Nonmagical Attacks resistance, +Psychic resistance
Eladrin, Spring: -Nonmagical Attacks resistance, +Psychic resistance
Eladrin, Summer: -Nonmagical Attacks resistance, +Fire resistance
Eladrin, Winter: -Nonmagical Attacks resistance
Juiblex: +Acid immunity
Molydeus: -Necrotic resistance
Morkoth: -Nonmagical Attacks resistance
Nabassu: -Necrotic resistance, +Lightning resistance
Nupperibo: -Nonmagical Attacks resistance
Shoosuva: -Nonmagical Attacks resistance
Skulk: +Radiant immunity
Slithering Tracker: +Nonmagical Attacks resistance
Swarm of Rot Grubs: +Fire vulnerability
Troll, Spirit: -Lightning resistance, -Thunder resistance, -Nonmagical Attacks immunity, +Nonmagical Attacks resistance
Warlock of the Fiend: -Nonmagical Attacks resistance, +Fire resistance
Zaratan: -Thunder vulnerability


# CR
Three creatures changed CRs.

Juiblex: increased from CR 23 to CR 24.
Shadow Mastiff Alpha: increased from CR 2 to CR 3.
Yeenoghu: increased from CR 24 to CR 25.

-->