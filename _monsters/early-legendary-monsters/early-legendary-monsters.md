---
title: "Early Legendary Monsters"
excerpt: "Legendary monsters in the first several books were overpowered but their balance has improved since then."
permalink: /:collection/:name/
date: 2021-12-27
last_modified_at: 2025-01-26
tags:
  - analysis
  - challenge rating
  - legendary monsters
  - monsters
  - xp
---

# Introduction

I've calculated CR values for a lot of monsters from official source books; nearly all of them to be precise. In the process of doing so, one thing that's stood out to me is that WotC has been getting more precise with their monster design over time, specifically when it comes to legendary monsters. What I mean by this is that legendary monsters published in more recent books are, on paper, more likely to be close to their listed CR than monsters from earlier book.

As I'll show in the sections that follow, legendary monsters from early books were overpowered. In most cases, this resulted in the listed CR being 1-2 levels lower than it ought to be based on the monsters' stat blocks. This sort of difference isn't likely to make a huge difference in actual play, unless a DM is intending to push their PCs to their absolute limits, so it's not surprising that they snuck through and have gone largely unnoticed until now.

I've broken up this post into two sections. The first looks at legendary monsters from adventures modules and how they've changed
over the years. The second looks at legendary monster from source books. Specifically, it looks at how legendary monsters from the _Monster Manual_ compares with those published in subsequent source books.

# Adventure Modules

Every adventure module WotC has published so far has legendary monsters in it that can't be found in any other books. To get a sense of how strong these monsters are for their respective CR values, I've calculated their XP values following the method I discussed in my previous post [Calculating Monster XP]({{ site.data.page-links.calculating-monster-xp.path }}). 

This approach gives better resolution than comparing listed CRs with CR values calculated using chapter 9 of the DMG. And, since the difference between CRs is not uniformly defined, it also gives a much more consistent measure of how much stronger/weaker a monster is than expected across a wide range of CRs.

Figure \figref{fig:exp-ratio-vs-time-adventure-modules} (below) shows how these calculated XP values compare to the target XP value for both normal and legendary monsters from adventure modules. 

<figure id="fig:exp-ratio-vs-time-adventure-modules">
    {% include_relative fig-exp-ratio-mean-vs-time-adventure-modules-small.html %}
    {% include_relative fig-exp-ratio-mean-vs-time-adventure-modules-large.html %}
    <figcaption>Calculated XP mean (points) normalized to target XP values for monsters published in official adventure modules as a function of the adventure modules' publication dates.</figcaption>
</figure>


For normal monsters, while the averages tends to be a bit on the weaker side of the spectrum, there is little change in the average over time. However, for legendary monsters there is a clear trend, where monsters from adventure modules published before 2018 were considerably stronger than expected compared to those published after.

It makes sense that WotC would get better at accurately assigning CR values as the system gets older and they gain more experience designing for it. However, it is puzzling that this trend only shows up for legendary monsters and not normal monsters as well.

To understand this better, Table 1 lists all of the legendary monsters from these adventure modules published prior to 2018.

#### Table 1
{% include_relative early-adventure-legendary-monsters.html %}

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

<figure id="fig:exp-ratio-vs-encounter-type">
    {% include_relative fig-exp-ratio-vs-encounter-type-small.html %}
    {% include_relative fig-exp-ratio-vs-encounter-type-large.html %}
    <figcaption>Calculated XP mean (points) normalized to target XP values for the monsters listed in Table 1.</figcaption>
</figure>

As shown in Fig. \figref{fig:exp-ratio-vs-encounter-type} (above), when split into monsters who are fought directly by the PCs and those who aren't, the legendary monsters who are driving this trend are clearly the later. 

This result isn't too surprising. The legendary monsters who are fought directly in these adventure modules are much more likely to have been encountered by playtesters and given feedback on than those who were intended to be avoided. And, for those legendary monsters encountered with support from allies or in weakened state, the playtest feedback would naturally be focused more on how the encounter felt as a whole, than how each monster felt individually.

Another interesting point to note about these monsters is that nearly all of the legendary monsters from _Out of the Abyss_ (the demon lords) were republished in _Mordenkainen's Tome of Foes_ with adjustments made to their stat blocks, and again in _Mordendainen Present: Monsters of the Multiverse_. A comparison between the XP ratios from each of these books for each demon lord is shown in Fig. \figref{fig:exp-ratio-vs-monster-oota-mtof} (below).

<figure id="fig:exp-ratio-vs-monster-oota-mtof">
    {% include_relative fig-exp-ratio-vs-monster-demon-lords-small.html %}
    {% include_relative fig-exp-ratio-vs-monster-demon-lords-large.html %}
    <figcaption>Calculated XP normalized to target XP values for the demon lords published in <i>Out of the Abyss</i> (OotA), then republished in <i>Mordenkainen's Tome of Foes</i> (MtoF), and again in <i>Mordenkainen's Presents: Monsters of the Multiverse</i> (MPMotM).</figcaption>
</figure>

For all of the monsters except Juiblex, who was the most on target of the original set, the updated stat blocks are changed to bring them more in line with the expected strength of their CR. In total, the average XP ratio for these monsters dropped from around 1.40 in _Out of the Abyss_, with a standard deviation of 0.31, to 1.04 in _Mordenkainen's Tome of Foes_, with a standard deviation of 0.19. For their third publication in _Mordenkainen's Presents: Monsters of the Multiverse_, these both improved further to an average ratio of 1.03 and a standard deviation of 0.15.


# Source Books

For source books, the story is a bit more subtle. As Fig. \figref{fig:exp-ratio-vs-time-source-books} (below) shows, the average XP ratio for the published source books stays fairly consistent for both normal and legendary monsters.

<figure id="fig:exp-ratio-vs-time-source-books">
    {% include_relative fig-exp-ratio-mean-vs-time-source-books-small.html %}
    {% include_relative fig-exp-ratio-mean-vs-time-source-books-large.html %}
    <figcaption>Calculated XP mean normalized to target XP values for source books as a function of the source books' publication dates.</figcaption>
</figure>

The _Monster Manual_ (MM) has a slightly higher average ratio, but the difference is small compared to what the trend showed for adventure modules.

However, when comparing the distribution of XP ratio values, as shown in Fig. \figref{fig:exp-ratio-cdf-mm-vs-source-books} (below), the MM stands out as a clear outlier from the rest of the source books, with a higher than normal portion of its monsters having a XP ratio between 1.3 and 1.7.

<figure id="fig:exp-ratio-cdf-mm-vs-source-books">
    {% include_relative fig-exp-ratio-cdf-mm-vs-source-books-small.html %}
    {% include_relative fig-exp-ratio-cdf-mm-vs-source-books-large.html %}
    <figcaption>Cumulative probability distribution of XP normalized to target XP values for monsters from official source books. For source books outside of the <i>Monster Manual</i> (non-MM, orange), the thin lines represent each individual book while the thick line represents the average of the group as a whole.</figcaption>
</figure>

After looking through the legendary monsters from the MM in this range, this deviation was clearly the result of dragons. This is clearly illustrated in Fig. \figref{fig:exp-ratio-cdf-mm-vs-source-books-no-dragons} (below), which shows how the distribution of XP ratio values changes for the MM when dragons are removed from it.

<figure id="fig:exp-ratio-cdf-mm-vs-source-books-no-dragons">
    {% include_relative fig-exp-ratio-cdf-mm-vs-source-books-no-dragons-small.html %}
    {% include_relative fig-exp-ratio-cdf-mm-vs-source-books-no-dragons-large.html %}
    <figcaption>Cumulative probability distribution of XP normalized to target XP values for monsters from official source books.</figcaption>
</figure>

Indeed, the legendary dragons in the MM have an average XP ratio of around 1.7 while legendary non-dragon monsters have an average XP ratio of around 1.2. In other words, the legendary dragons in the MM are around 40% tougher, on average, than the rest of the legendary monsters in the MM. This relationship is illustrated again in Fig. \figref{fig:exp-ratio-vs-cr-mm-type-dragon}, which shows XP ratios for individual monsters along with their target CR.

<figure id="fig:exp-ratio-vs-cr-mm-type-dragon">
    {% include_relative fig-exp-ratio-vs-cr-mm-type-dragon-small.html %}
    {% include_relative fig-exp-ratio-vs-cr-mm-type-dragon-large.html %}
    <figcaption>Calculated XP normalized to target XP values for legendary monsters from the <i>Monster Manual</i>.</figcaption>
</figure>

I first came across this observation around the start of 2020, and my initial theory was that this was probably intentional on the part of WotC. After all, dragons are suppose to be iconic creatures in Dungeons & Dragons. They're in the name of the game! However, WotC recently released a source book dedicated specifically to dragons, _Fizban's Treasury of Dragons_ (FToD), which was included in the collection of non-MM source books shown in Fig. \figref{fig:exp-ratio-cdf-mm-vs-source-books} and it does not show this same behavior.

<figure id="fig:exp-ratio-vs-cr-mm-ftod-type-dragon">
    {% include_relative fig-exp-ratio-vs-cr-mm-ftod-type-dragon-small.html %}
    {% include_relative fig-exp-ratio-vs-cr-mm-ftod-type-dragon-large.html %}
    <figcaption>Calculated XP normalized to target XP values for legendary monsters from the <i>Monster Manual</i> and <i>Fizban's Treasury of Dragons</i>.</figcaption>
</figure>

When compared with the legendary dragons from the MM, as Fig. \figref{fig:exp-ratio-vs-cr-mm-ftod-type-dragon}, shows, the dragons published in FToD are consistently weaker, and more in line with their target values. In terms of a numeric average, the legendary dragons from the MM, again, have an average XP ratio of around 1.7 while the legendary dragons from FToD have an average XP ratio of 1.2.

# Conclusion

So, there you have it. The legendary monsters put out by WotC have gotten more in line with their listed CRs for both adventure modules and source books. I think this is generally a good thing, it shows that WotC has gotten better at working within their own system since the release of 5e. And, given their "next evolution" of D&D is suppose to work with monster stat blocks from 5e that means we will likely continue to get well balanced monsters going forward.