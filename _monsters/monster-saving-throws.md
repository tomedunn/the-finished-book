---
title: "Monster Saving Throws"
excerpt: "An analysis of how monster saving throw modifiers scale with CR."
date: 2021-10-23
last_modified_at: 2023-06-27
tags:
  - analysis
  - mechanics
  - monsters
  - saving throws
---

# Introduction

Monster saving throw bonuses are an important part of D&D 5th edition, especially when it comes to evaluating the strengths and weaknesses of various class features and spells. Despite their importance, though, they're also an aspect of analyzing the game that people frequently get wrong.

In this post, I go through how the different saving throw bonuses for published monsters compare to one another, followed by a detailed breakdown of how monster ability score modifiers and saving throw proficiencies combine to produce these results. You can find a summary of the dataset used for this analysis [here]({{ site.url }}{{ site.baseurl }}{% link _monsters/monster-dataset.md %}).

# Saving Throw Bonuses

To begin, lets look at the how saving throw bonuses scale with monster CR. It's important to note that these trends are what's observed from published sources. It's not as statement on how the various saving throws bonuses ought to scale.

<figure alt="Saving Throw Modifier vs CR" id="fig:monster-saving-throw-modifier-trends">
    {% include_relative monster-saving-throws/fig-saving-throw-modifier-vs-cr-small.html %}
    {% include_relative monster-saving-throws/fig-saving-throw-modifier-vs-cr-large.html %}
    <figcaption>Figure 1: Monster average saving throw bonuses as a function of CR. Monsters are grouped in CR bins of width 3.</figcaption>
</figure>

Figure <a href="#fig:monster-saving-throw-modifier-trends" class="fig-ref">1</a> shows how the average saving throw bonus scales with monster CR for each ability score. Here, the monsters have been grouped into CR bins with a width of 3 in order to reduce the noise in the data at higher CRs.

At low CRs all six ability scores are relatively close to one another with only about +3 separating the strongest from the weakest. However, at high CRs this gap almost doubles, with a range of about +6 separating the strongest from the weakest.

Strength and Intelligence both start off as stronger saves for monsters at low CRs. However, since they increase slower than the other four ability scores they end up on the weaker side of the spectrum at high CRs. Also, while both Strength and Intelligence appear to scale similarly, they do so for entirely different reasons.

# Ability Score Modifiers

There are two key factors that go into defining a monster's saving throw bonus, their ability score modifiers and what saving throws they are proficient in. In this section we'll look at how the different ability score modifiers scale, and in the next section we'll look at how saving throw proficiency impacts monster saving throw bonuses.

<figure alt="Ability Score Modifier vs CR" id="fig:monster-ability-score-modifier-trends">
    {% include_relative monster-saving-throws/fig-ability-score-modifier-vs-cr-small.html %}
    {% include_relative monster-saving-throws/fig-ability-score-modifier-vs-cr-large.html %}
    <figcaption>Figure 2: Monster average ability score modifiers as a function of CR. Monsters are grouped in CR bins of width 3.</figcaption>
</figure>

Figure <a href="#fig:monster-ability-score-modifier-trends" class="fig-ref">2</a> shows how the average (mean) ability score modifier scales with monster CR. Here, again, the monsters have been grouped into CR bins with a width of 3 in order to reduce the noise in the data at higher CRs.

The non-physical ability scores, Intelligence, Wisdom, and Charisma perform similarly across the full range of CRs. Charisma and Intelligence follow very similar trends, with Charisma being about 1 higher than Intelligence on average. Wisdom starts off as the highest of the three but increases slightly slower than the other two, ending slightly below Intelligence.

Strength and Constitutions stand out as the strongest out of all the ability scores, about 2 higher than the non-physical ability scores on average. Dexterity is the clear outlier of the bunch, showing almost no growth across the full range of CRs.

In total, three ability scores -- Constitution, Intelligence, and Charisma -- match what we saw in the previous section while the other three -- Strength, Dexterity, and Wisdom -- don't. For Wisdom, the difference isn't nearly as pronounced as it is for Strength and Dexterity, but it is sufficient enough to make Wisdom look like it would be the second lowest save at higher CRs, when in truth it's the second highest save. The reason for these difference, of course, lies in monster saving throw proficiencies.

# Saving Throw Proficiencies

As mentioned earlier, the second half of the picture comes from how saving throw proficiencies scale with monster CR. Figure <a href="#fig:monster-saving-throw-proficiency-trends" class="fig-ref">3</a> shows the probability of a monster having a particular saving throw proficiency at a given CR, where the CRs are binned in groups of three as they were in the previous plots.

<figure alt="Saving Throw Proficiency vs CR" id="fig:monster-saving-throw-proficiency-trends">
    {% include_relative monster-saving-throws/fig-saving-throw-proficiency-vs-cr-small.html %}
    {% include_relative monster-saving-throws/fig-saving-throw-proficiency-vs-cr-large.html %}
    <figcaption>Figure 3: Monster average saving throw proficiency rates as a function of CR. Monsters are grouped in CR bins of width 3.</figcaption>
</figure>

Strength is, by far, the least likely saving throw for monsters to be proficient in, which explains why it goes from being one of the highest monster ability scores to only average as a saving throw bonus. Dexterity, on the other hand, is in the middle of the pack for proficiencies, which explains why its average saving throw bonus increases so much more than its average ability score modifier, which was essentially flat. Finally, Wisdom is clearly the most common saving throw proficiency, which explains why it shifts from only an average ability score modifier at higher CRs to the second strongest saving throw bonus.

It's worth pointing out that monster proficiency bonuses increases with CR as well. Figure <a href="#fig:monster-saving-throw-proficiency-bonus-trends" class="fig-ref">4</a> shows the same data with proficiency bonus factored in.

<figure alt="Saving Throw Proficiency Bonus vs CR" id="fig:monster-saving-throw-proficiency-bonus-trends">
    {% include_relative monster-saving-throws/fig-saving-throw-proficiency-bonus-vs-cr-small.html %}
    {% include_relative monster-saving-throws/fig-saving-throw-proficiency-bonus-vs-cr-large.html %}
    <figcaption>Figure 4: Monster average saving throw proficiency bonuses as a function of CR. Monsters are grouped in CR bins of width 3.</figcaption>
</figure>

<!--
# Extra Credit

For those wanting to see the trends for ability score modifiers and proficiency bonuses side by side, Fig. <a href="#fig:ability-mods-and-prof-bonus-vs-cr" class="fig-ref">5</a> shows a side by side comparison between the two.

<figure class="half" id="fig:ability-mods-and-prof-bonus-vs-cr">
    {% include_relative monster-saving-throws/fig-ability-score-modifier-vs-cr-small.html %}
    {% include_relative monster-saving-throws/fig-ability-score-modifier-vs-cr-large.html %}
    {% include_relative monster-saving-throws/fig-saving-throw-proficiency-bonus-vs-cr-small.html %}
    {% include_relative monster-saving-throws/fig-saving-throw-proficiency-bonus-vs-cr-large.html %}
    <figcaption>Figure 5: Monster average ability score modifier and proficiency bonuses as a function of CR. Monsters are grouped in CR bins of width 3.</figcaption>
</figure>
-->