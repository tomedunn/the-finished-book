---
title: "Early Legendary Monsters"
excerpt: "Legendary monsters were overpowered, but not anymore."
date: 2021-12-27
last_modified_at: 2021-12-27
#tags:
#  - analysis
#  - monsters
#  - monster categories
---

# Introduction

I've calculated CR values for a lot of monsters from official source books; nearly all of them to be precise. In the process of doing so, one of the things that's stood out to me is that WotC has been getting more precise with their monster design over time, specifically when it comes to legendary monsters. What I mean by this is that legendary monsters published in more recent books are, on paper, more likely to be close to be close to their listed CR than monsters from earlier book.

As I'll show in the sections that follow, legendary monsters from early books were overpowered. In most cases, this resulted in the listed CR being 1-2 levels lower than it aught to be based on the monsters' stat blocks. This sort of difference isn't likely to make a huge difference in actual play, unless a DM is intending to push their PCs to their absolute limits, so it's not surprising that they snuck through and have gone largely unnoticed until now.

I've broken up this post into two sections: the first looks at legendary monsters from adventures modules, while the second looks at legendary monster from the source books.

# Adventure Modules

Every adventure module WotC has published so far has in it legendary monsters that can't be found in any other books. To get a sense of how strong these monsters are for their respective CR values, I've calculated their effective XP value (eXP) following the method outlined in my paper "[Calculating XP and encounter difficulty in D&D 5e](https://drive.google.com/file/d/1VnvdnJYTIym1QNGvONWZkOFYgbFO66Bx/view?usp=sharing)", which I discussed in my previous post [Calculating Monster XP]({{ site.url }}{{ site.baseurl }}{% link _monsters/calculating-monster-xp.md %}). 

This approach gives better resolution than comparing listed CRs with CR values calculated using chapter 9 of the DMG. And, since the difference between CRs is not uniformly defined, it also gives a much more consistent measure of how much stronger/weaker a monster is than expected across a wide range of CRs.

Figure 1 shows how these calculated XP values for adventure module monsters compare to their target XP value, for both normal and legendary monsters. 


<figure>
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-mean-vs-time-adventure-modules-legendary.svg"  style="width:800px;min-width:50%;max-width:100%">
    <figcaption>Figure 1: Calculated XP mean (points) normalized to target XP values for monsters published in official adventure modules as a function of the adventure modules' publication dates.</figcaption>
</figure>


For normal monsters, while the averages tends to be a bit on the weaker side of the spectrum, there is little change in the average over time. However, for legendary monsters there is a clear trend, where monsters from adventure modules published before 2018 were considerably stronger than expected compared to those published after.

It makes sense that WotC would get better at accurately assigning CR values as the system gets older and they gain more experience designing for it. However, it is puzzling that this trend only shows up for legendary monsters and not normal monsters.

To understand this better, Table 1 lists all of the legendary monsters from these adventure modules published prior to 2018.

#### Table 1
{% include_relative early-legendary-monsters/early-adventure-legendary-monsters.html %}

For those who have run or read through these modules, you may immediately recognize part of the issue here. Most of these monsters are not fought directly in their respective adventures. They are fought indirectly, either in a weakened state, with allies, or intended to be avoided by the PCs entirely.

In fact, by my count only four of the legendary monsters listed above are suppose to be fought directly by the PCs under normal circumstances. These include Rezmir from _Hoard of the Dragon Queen_, Yestabrod from _Out of the Abyss_, Tarul Var from _Tales from the Yawning Portal_, and the atropal from _Tomb of Annihilation_.

<!--
In _Rise of Tiamat_, Severin doesn't need to be fought in order for the PCs to prevent Tiamat from being summoned. And, even if Severin succeeds in summoning Tiamat, he is quickly devoured by her upon her release. If Tiamat is summoned, she takes several rounds of combat to fully emerge through her portal, followed by several rounds spent devouring other enemy NPCs. During this time the PCs can damage her while her damage output is significantly reduced. Furthermore, Tiamat can be weakened considerably through the players' actions prior to her arrival.

In _Princes of the Apocalypse_, each of the princes of elemental evil - Imix, Ogremoch, Olhydra, and Yan-C-Bin - can be banished back to their respective planes without the PCs having to defeat them directly through combat.

In _Out of the Abyss_, only two of the nine demon lords are intended to be fought by the PCs, Juiblex and Demogorgon, and both of them are encountered in a weakened state. Juiblex and Yeenoghu can be encountered earlier in the adventure at full strength but the book makes it clear that the PCs are not intended to stand a chance against them.

In _Curse of Strahd_, the PCs aren't expected to face Strahd von Zarovich until after they obtain the _sunsword_, a magic weapon that negates Strahd's regeneration feature, and a powerful ally to aid them in the encounter.

In _Storm King's Thunder_, Maegera the Dawn Titan is not intended to be fought by the PCs and operates more as a plot device, Klauth is intended to aid or scare the PCs, and the encounter with Slarkrethel is best avoided or escaped while Slarkrethel focuses on destroying a ship.

Finally, in _Tomb of Annihilation_, Acererak is intended to be encountered with significant aid fron several if the trickster gods.

This means that of the monsters listed from these adventures only Rezmir from _Hoard of the Dragon Queen_, Yestabrod from _Out of the Abyss_, Tarul Var from _Tales from the Yawning Portal_, and the atropal from _Tomb of Annihilation_ are intended to be fought directly and under normal circumstances.
-->

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-vs-encounter-type.svg">
    <figcaption>Figure 2: Calculated XP mean (points) normalized to target XP values for the monsters listed in Table 1.</figcaption>
</figure>

As shown in Fig. 2, when split into monsters who are fought directly by the PCs and those who aren't, the legendary monsters who are driving this trend are clearly the later. 

This result isn't too surprising, since the legendary monsters who are fought directly in these adventure modules are much more likely to have been encountered by playtesters and given feedback on than those who were intended to be avoided. And, for those legendary monsters encountered with support from allies or in weakened state, the playtest feedback would naturally be focused more on how the encounter felt as a whole, than how each monster felt individually.

Another interesting point to note about these monsters is that nearly all of the legendary monsters from _Out of the Abyss_ (the demon lords) were republished in _Mordenkainen's Tome of Foes_ with adjustments made to their stat blocks. A comparison between eXP values for each of these demon lords is shown in Fig. 3.  

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-vs-monster-oota-mtof.svg">
    <figcaption>Figure 3: Calculated XP mean normalized to target XP values for the demon lords published in <i>Out of the Abyss</i> (OotA) and then republished in <i>Mordenkainen's Tome of Foes</i> (MtoF).</figcaption>
</figure>

For all of the monsters except Juiblex, who was the most on target of the original set, all of the updated stat blocks are changed to bring them more in line with the expected strength of their CR. In total, the average XP ratio for these monsters dropped from around 1.7 to 1.3. This still puts them on the over-powered side of the spectrum, but not nearly as much as they were in their first publication.


# Source Books

For source books the story is a bit more subtle. As Fig. 4 shows, the average XP ratio for the published source books show a very consistent trend with normal monsters and a fairly consistent trend with legendary monsters.

<figure>
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-mean-vs-time-source-books-legendary.svg" style="width:800px;min-width:50%;max-width:100%">
    <figcaption>Figure 4: Calculated XP mean normalized to target XP values for source books as a function of the source books' publication dates.</figcaption>
</figure>

Out of the published source books, the _Monster Manual_ (MM) stands out as having a slightly higher average ratio but the difference is small compared to what the trend showed for adventure modules.

However, when comparing the distribution of XP ratio values, as shown in Fig. 5, the MM stands out as a clear outlier from the rest of the source books. Clearly, the MM has a higher than normal number of monsters with XP ratio between 1.3 and 1.7.

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-cdf-mm-vs-source-books.svg">
    <figcaption>Figure 5: Cumulative probability distribution of XP normalized to target XP values for monsters from official source books. For source books outside of the <i>Monster Manual</i> (non-MM, orange), the thin lines represent each individual book while the thick line represents the average of the group as a whole.</figcaption>
</figure>

As Fig. 6 clearly illustrates, the source of this deviation in the MM is, in fact, dragons.

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-cdf-mm-vs-source-books-no-dragons.svg">
    <figcaption>Figure 6: Cumulative probability distribution of XP normalized to target XP values for monsters from official source books.</figcaption>
</figure>

Indeed, the legendary dragons in the MM have an average XP ratio of around 1.70 while legendary non-dragon monsters have an average XP ratio of around 1.23. In other words, the legendary dragons in the MM are around 40% tougher, on average, than the rest of the legendary monsters in the MM. This relationship is illustrated in Fig. 7.

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-vs-cr-mm-type-dragon.svg">
    <figcaption>Figure 7: Calculated XP mean normalized to target XP values for legendary monsters from the <i>Monster Manual</i>.</figcaption>
</figure>

Now, one could probably write this off as intentional on the part of WotC. After all, dragons are suppose to be iconic creatures in Dungeons & Dragons. They're even mentioned in the name of the game! However, WotC recently released a source book dedicated specifically to dragons, _Fizban's Treasury of Dragons_ (FToD), which was included in the collection of non-MM source books shown in Fig. 5 and it did not show this same behavior.

<figure class="half">
    <img src="{{ site.url }}{{ site.baseurl }}/monsters/early-legendary-monsters/exp-ratio-vs-cr-mm-ftod-type-dragon.svg">
    <figcaption>Figure 8: Calculated XP mean normalized to target XP values for legendary monsters from the <i>Monster Manual</i> and <i>Fizban's Treasury of Dragons</i>.</figcaption>
</figure>

As Fig. 8 shows, the dragons published in FToD are consistently weaker, and more in line with their target values, than those dragons published in the MM. In terms of a numeric average, the legendary dragons from the MM, again, have an average XP ratio of around 1.70 while the legendary dragons from FToD have an average XP ratio of 1.20.

# Conclusion

So, there you have it. The legendary monsters put out by WotC have gotten more in line with their listed CRs for both adventure modules and source books. I think this is generally a good thing, it shows that WotC has gotten better at working within their own system since the release of 5e. And, given their "next evolution" of D&D is suppose to work with monster stat blocks from 5e that means we will likely continue to get well balanced monsters going forward.