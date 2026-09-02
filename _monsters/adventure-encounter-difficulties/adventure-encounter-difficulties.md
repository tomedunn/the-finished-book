---
title: "Adventure Encounter Difficulties"
excerpt: "An analysis of encounter difficulties from official 5e adventures."
permalink: /:collection/:name/
date: 2026-09-02
last_modified_at: 2026-09-02
tags:
  - analysis
  - adventures
  - combat
  - encounters
  - xp
---

# Introduction

Both the 2014 _Dungeon Master's Guide_ and 2024 _Dungeon Master's Guide_ contain rules for building encounters and estimating their difficulty. I've explored the mathematical underpinnings of these rules in previous posts but I've yet to look at these rules in practice over the course of an adventure or campaign.

In this post I look at combat encounters from official D&D 5e adventures published by Wizards of the Coast. Specifically, the difficulties of those encounters based on the 2014 rules. In order to calculate these difficulties, each encounter was assigned a party level based on the advancement guidelines in its respected book. And, since virtually all books in this dataset say they assume a party of 4-6 PCs, these difficulties are based on a party of five PC.

You can find a summary of the encounter dataset used for this analysis [here]({{ site.data.page-links.encounters-dataset.path }}). 

It's worth noting that there are encounters in this dataset that are not truly meant for the PCs to battle their way through. These are often at the extreme ends of the spectrum, i.e., extremely easy and extremely difficulty on paper. I tried to be conservative in what I excluded from the list of potential combat encounters.

# Encounter Difficulty

Each encounter in one of the official D&D 5e adventures can be assigned to a difficulty category using the method laid out in the _[Basic Rules (2014)](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/building-combat-encounters)_, either Easy, Medium, Hard, or Deadly. For the purposes of this analysis I've added two additional categories: Trivial for all encounters with adjusted XP values below the Easy difficulty XP threshold, and Very Deadly for anything above half the PCs' adventuring day XP budget. A breakdown of how many encounters fall into each category is shown in Fig. \figref{fig:encounter-difficulty-2014} (below).

<figure id="fig:encounter-difficulty-2014">
    {% include_relative fig-encounter-difficulty-2014-small.html %}
    {% include_relative fig-encounter-difficulty-2014-large.html %}
    <figcaption>Distribution of encounter difficulties for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

Trivial encounters were the most common, accounting for roughly $$30\%$$ of all encounters, with each higher difficulty category accounting for a progressively smaller portion of the total encounters until reaching Very Deadly which were about as common as Deadly encounters. If this result seems odd, it's worth recalling that I was purposefully conservative in what encounters I excluded from the list of possible combat encounters for each book.

On the easy side of the spectrum that means encounters like a single zombie against a level 17 party get included (see _Waterdeep: Dungeon of the Mad Mage_), which are clearly not designed to challenge the party. And, on the harder side it means encounters like Tiamat's army against a level 9 party get included (see _Balder's Gate: Descent into Avernus_), which the PCs are intended to avoid fighting at all cost.

As mentioned in the introduction, this approach is likely to inflate the number of encounters at the the extreme ends of the spectrum, but by how much isn't easy to quantify.

<figure id="fig:encounter-difficulty-pdf-2014">
    {% include_relative fig-encounter-difficulty-pdf-2014-small.html %}
    {% include_relative fig-encounter-difficulty-pdf-2014-large.html %}
    <figcaption>Distribution of encounter adjusted XP values relative to half the party's adventuring day budget for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

We can look at this data more granularly by focusing on how each encounter's adjusted XP total compares to half the party's adventuring day XP budget, as shown in Fig. \figref{fig:encounter-difficulty-pdf-2014} (above). With the exception of Trivial encounters, the number of encounters decreases as their relative XP total goes up.

We can make some sense of this trend if we consider picking encounters based on an XP budget. For example, a budget of 200 XP can be filled with a single encounter worth 200 XP, two encounters worth 100 XP each, or four encounters worth 50 XP each. If each encounter difficulty were equally likely to be chosen when filling up the budget, we'd expect the number of encounters for each difficulty to be $$\propto 1 / XP.$$

The trend shown in Fig. \figref{fig:encounter-difficulty-pdf-2014} is close to this for difficulties Easy and above, but deviates from it enough to show a bias towards Medium to Hard encounters as shown in Fig. \figref{fig:encounter-selection-pdf-2014} (below), which divides the observed probabilities by the theoretical one $$\propto 1 / XP.$$

<figure id="fig:encounter-selection-pdf-2014">
    {% include_relative fig-encounter-selection-pdf-2014-small.html %}
    {% include_relative fig-encounter-selection-pdf-2014-large.html %}
    <figcaption>Encounter adjusted XP normalized to account for XP budget construction for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

That said, this XP budget construction weighting isn't a perfect analogy for the encounters from published adventures. While the 2014 encounter building rules do include an XP budget in the form of the adventuring day, there are many encounters throughout these books that are clearly not designed with the adventuring day budget in mind.

Breaking the data down by level reveals a fairly consistent picture across the level spectrum. The median encounter difficulty, as illustrated in Fig. \figref{fig:median-xp-ratio-by-level-2014} (below), tends to fluctuate around the Medium difficulty XP threshold when all encounters are included, and just below the Hard XP threshold when excluding Trivial encounters.

<figure id="fig:encounter-median-xp-ratio-by-level-2014">
    {% include_relative fig-encounter-median-xp-ratio-by-level-2014-small.html %}
    {% include_relative fig-encounter-median-xp-ratio-by-level-2014-large.html %}
    <figcaption>Median encounter XP relative to half the party's adventuring day budget for each level for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

Levels 18 and 19 stand out as being significantly harder than normal. This could be an intentional shift to account for tier 4 PCs being exceptionally strong, or to compensate for combat tending to take longer at higher levels. But it could also simply be statistical noise from there being only a few books with encounters in this level range.

Breaking things down by book reveals a slightly less consistent picture. As shown in Fig. \figref{fig:encounter-median-xp-ratio-by-book} (below), while the median encounter difficulty still fluxtuates about the Medium difficulty XP threshold, three books stand out as being noticeably harder than the rest: _Storm King's Thunder_, _Baulder's Gate: Descent into Avernus_, and _Critical Role: Call of the Netherdeep_.

<figure id="fig:encounter-median-xp-ratio-by-book">
    {% include_relative fig-encounter-median-xp-ratio-by-book-small.html %}
    {% include_relative fig-encounter-median-xp-ratio-by-book-large.html %}
    <figcaption>Median encounter XP relative to half the party's adventuring day budget by book for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

I don't intent to dig into the details of why these three books tend to skew towards having more difficult encounters in this post, but, in broad strokes, they tend to feature a higher number of very difficult encounters the PCs aren't intend to battle their way through, and/or encounters that appear harder but where the PCs have other advantages to balance things out.

A more subtle trend worth pointing out in Fig. \figref{fig:encounter-median-xp-ratio-by-book} is that the difference between the median difficulty with and without Trivial encounters included drops significantly in 2022, starting with _Critical Role: Call of the Netherdeep_. This points to the number of Trivial encounters decreasing for more recent books.

<figure id="fig:encounter-std-xp-ratio-by-book">
    {% include_relative fig-encounter-std-xp-ratio-by-book-small.html %}
    {% include_relative fig-encounter-std-xp-ratio-by-book-large.html %}
    <figcaption>Standard deviation of encounter XP relative to half the party's adventuring day budget by book for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

Since Trivial encounters sit at the low end of the difficulty spectrum, reducing their numbers should reduce the overall variability in encounter difficulties. In other words, it should lead to more consistent encounter difficulties. And, as Fig. \figref{fig:encounter-std-xp-ratio-by-book} (above) shows, this is indeed the case. However, we also see this improved consistency when Trivial encounters are excluded entirely for all books.

This is because, in addition to having fewer Trivial encounters, starting in 2022 WotC adventures have had significantly fewer Easy encounters and Very Deadly encounters as well. A comparison of the encounter difficulty distributions pre- and post-2022 is shown in Fig. \figref{fig:encounter-difficulty-split-2014} (below).

<figure id="fig:encounter-difficulty-split-2014">
    {% include_relative fig-encounter-difficulty-split-2014-small.html %}
    {% include_relative fig-encounter-difficulty-split-2014-large.html %}
    <figcaption>Distribution of encounter difficulties for combat encounter found in adventure books published by WotC.</figcaption>
</figure>

# Conclusion

To reiterate the main observations, for WotC adventures, the number of encounters tends to decrease as the difficulty increases, and the overall average difficulty stays consistent across most tiers of play. Also, starting in 2022 the overall variance in encounter difficulties decreased and became more consistent between books.

Before ending, I'd like to stress that none of these trends are inherently good or bad. More consistent encounter difficulties may work better in some campaigns and for some groups, and less consistent encounter difficulties may work better for others. And higher numbers of very easy encounters may work better in some circumstances than others.

In addition to that, there are more dimensions to this topic than what I've covered here, including how encounters fit within adventuring days and the number and types of monsters used. I have plans to visit each of these topics in the future.