---
title: "Daily XP and Encounter Difficulty"
excerpt: "Shows how much player character daily XP budgets change with average encounter difficulty."
date: 2022-10-3
last_modified_at: 2023-03-04
tags:
  - analysis
  - adventuring day
  - classes
  - encounter balancing
  - encounter difficulty
  - xp
---

# Introduction

In my previous post, [Player Character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}), I showed how encounter XP values and daily XP budgets can be calculated for player characters. The results I showed focused on full adventuring days composed of Medium encounters with two short rests, but this isn't the only way to build a full adventuring day. In this post, I'll take a quick look at how the average encounter difficulty affects player character daily XP budgets.

# Calculating Daily XP

Calculating the daily XP values for each class follows the same process I outlined [here]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}), but with the number of rounds and encounters adjusted to fit each encounter difficulty. The number of rounds per encounter and encounters per day for a given encounter difficulty vary a bit from level to level, but those variations are small compared to the average for each difficulty. These average values are summarized in the <a href="#tab:rounds-summary" class="fig-ref">Encounters and Rounds</a> table (below).

<div class="dataframe center" style="width:660px;">
<h3 id="tab:rounds-summary">Encounters and Rounds</h3>
{% include_relative daily-xp-and-encounter-difficulty/table-rounds-summary.html %}
</div>

The results of these calculations, averaged across all classes, is shown in Fig. <a href="#fig:daily-xp-budgets-vs-level" class="fig-ref">1</a> (below). Unsurprisingly, as the average encounter difficulty goes up, so does the daily XP the PCs can handle. This is because the number of rounds per day decreases as the difficulty goes up, which allows many of the classes to deal higher average damage per round.

<figure id="fig:daily-xp-budgets-vs-level">
    {% include_relative daily-xp-and-encounter-difficulty/fig-full-daily-xp-vs-level-adventuring-days-large.html %}
    {% include_relative daily-xp-and-encounter-difficulty/fig-full-daily-xp-vs-level-adventuring-days-small.html %}
    <figcaption>Figure 1: PC daily XP values for full adventuring days consisting of either Easy, Medium, Hard, or Deadly encounters.</figcaption>
</figure>

What is perhaps a bit surprisingly, though, is that the difference between each difficulty is relatively small. The largest XP range between adventuring days with Medium and Deadly encounters comes at level 19 and is 17% of the daily budget, or one extra Easy encounter.


<figure id="fig:daily-xp-ratio-vs-level">
    {% include_relative daily-xp-and-encounter-difficulty/fig-daily-xp-ratio-vs-level-large.html %}
    {% include_relative daily-xp-and-encounter-difficulty/fig-daily-xp-ratio-vs-level-small.html %}
    <figcaption>Figure 2: PC daily XP values for full adventuring days consisting of either Easy, Medium, Hard, or Deadly encounters. Values are normalized to the Medium encounters values.</figcaption>
</figure>

Figure <a href="#fig:daily-xp-ratio-vs-level" class="fig-ref">2</a> (above) replots this data relative to the average daily XP values for Medium encounters. Easy encounters come out 10% lower than Medium on average, Hard encounters are 6% higher, and Deadly are 12% higher. This means that only minor corrections to the adventuring day XP budgets are needed in order to compensate for different average encounter difficulties.

To give a sense of where these changes in XP come from, Fig. <a href="#fig:edpr-vs-level" class="fig-ref">3</a> (below) shows how the average effective damage per round for each average encounter difficulty. The relative differences in effective damage per round match those for XP almost exactly. This makes sense, since the amount of damage each class can take is largely independent of the number of encounters they face. 

<figure id="fig:edpr-vs-level">
    {% include_relative daily-xp-and-encounter-difficulty/fig-full-daily-edpr-vs-level-adventuring-days-large.html %}
    {% include_relative daily-xp-and-encounter-difficulty/fig-full-daily-edpr-vs-level-adventuring-days-small.html %}
    <figcaption>Figure 3: PC average effective damage per round for full adventuring days consisting of either Easy, Medium, Hard, or Deadly encounters.</figcaption>
</figure>


## Class Breakdown
We can take this a step further and look at how these hold up for each class as well. Figure <a href="#fig:class-daily-xp-ratio-vs-level" class="fig-ref">4</a> (below) shows how the daily XP for full adventuring days with Deadly encounters compares against one with Medium encounters for each class.

<figure id="fig:class-daily-xp-ratio-vs-level">
    {% include_relative daily-xp-and-encounter-difficulty/fig-class-daily-xp-ratio-vs-level-large.html %}
    {% include_relative daily-xp-and-encounter-difficulty/fig-class-daily-xp-ratio-vs-level-small.html %}
    <figcaption>Figure 4: Daily XP values for each class for full adventuring days consisting of Deadly encounters. Values are normalized to the Medium encounters values. <i>Note: You can toggle individual lines on and off by clicking on them in the legend.</i></figcaption>
</figure>

For most of spellcasting classes (bard, druid, sorcerer, and wizard), the gap between Deadly and Medium adventuring days steadily increases up until level 10 where it plateaus at around 20%. Clerics also increase up to near 20%, but their growth plateaus from levels 7-12 at around 12%. Warlocks, unsurprisingly, show a different trend from the other spellcasters, quickly reaching a plateau of around 12% and staying there all the way up to level 20.

Like clerics, the martial-spellcaster classes (paladin and ranger) show a steady increase between their Deadly and Medium adventuring days to a maximum of around 20% at level 20.

Unlike spellcasters and martial-spellcasters, martial classes have no general trend. Rogues, unsurprisingly, show no difference between their Deadly and Medium adventuring days due to their damage per round being entirely resource independent. Fighters, on the other hand, show a modest 7% increase until they reach level 17 and pick up a second use of Action surge, which causes them to jump up to around 12%. 

Monks, paradoxically, seem to jump between increases similar to fighters at low and high levels, and rogues for levels 9 - 17. On the low end, this trend is due to the ever increasing size of the monk's ki pool, which they use to fuel their offensive capabilities through Flurry of Blows (Stunning Strike is not yet included in this model). The increase dropping to zero at level 9 represents the point where a monk has enough ki to use Flurry of Blows every round for both Deadly and Medium encounter adventuring days. The spike at levels 18 - 20 comes from the monk gaining Empty Body, which provides a huge benefit to the monks survivability at the cost of lower damage per round. Since Empty Body is used during the first round of combat, this loss in DPR is smaller for longer encounters.

Finally, barbarians show a trend unlike any of the other classes, with a 30% increase between levels 3 and 11, that decreases in steps down to zero at level 20. This trend exactly follows the number of time the barbarian can use their Rage feature each day. From levels 3 - 11, the barbarian can use Rage three times, once for each encounter of a adventuring day with Deadly encounters, but less than half of the encounters in a Medium adventuring day. As they gain more uses, they cover more and more encounters for adventuring days made up of Medium encounters, until they reach level 20 and are finally able to Rage in every encounter, regardless of how many there are in the day.

# Conclusion

For full adventuring day with two short rests, as the average encounter difficulty increases the amount of encounter XP the PCs can handle goes up as well, but not by that much. Relative to a full adventuring day of Medium encounters, on a day with Hard encounters the PCs can handle 6% more encounter XP on average, and for Deadly encounters they can handle 12% more. This increase comes from the PCs being able to maintain a higher average DPR due to the total rounds of combat being lower.

On average, these differences in daily XP are small enough that they can likely be ignored by most DMs who aren't looking to push their PCs to their absolute limits in a controlled fashion. For DMs who are, it's also worth noting that these increases can be a bit larger (closer to 10% for Hard and 20% for Deadly) for higher level parties, as well as parties composed entirely of spellcasters and martial spellcasters.