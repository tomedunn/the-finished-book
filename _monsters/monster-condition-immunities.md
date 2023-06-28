---
title: "Monster Condition Immunities"
excerpt: "An analysis of how monster condition immunities depend on monster type and challenge rating."
date: 2022-12-23
last_modified_at: 2023-06-27
#tags:
#  - analysis
#  - monsters
#  - conditions
#  - immunities
---

# Introduction
Recently, I published a post on [valuing conditions]({{ site.url }}{{ site.baseurl }}{% link _theory/valuing-conditions.md %}) which showed how each of the conditions in 5th edition D&D can be calculated from their mechanical impact. Since those calculations didn't factor in the probability of each condition actually effecting a target, they can be thought of as representing the upper limit in how valuable each condition can be. In practice, these probabilities depend on two things in the majority of cases: how strong the monster's saving throw bonuses are, and whether or not the monster is immune to the condition being applied.

Since I've already covered how [monster saving throws]({{ site.url }}{{ site.baseurl }}{% link _monsters/monster-saving-throws.md %}) scale with monster CR, in this post I'd like to analyze how likely published monsters are to be immune to each condition in 5th edition D&D. You can find a summary of the dataset used for this analysis [here]({{ site.url }}{{ site.baseurl }}{% link _monsters/monster-dataset.md %}).

# Conditions Immunities
To begin, lets look at how likely published monsters are to be immune to each condition on average. As shown in Fig. <a href="#fig:condition-immunity-probability" class="fig-ref">1</a> (below), the most common conditions monsters are immune to are **charmed**, **frightened**, and **poisoned**. Each having an average likelihood between $$25 - 30\%$$.

<figure id="fig:condition-immunity-probability">
    {% include_relative monster-condition-immunities/fig-condition-immunity-probability-small.html %}
    {% include_relative monster-condition-immunities/fig-condition-immunity-probability-large.html %}
    <figcaption>Figure 1: Probability of a published monster being immune to a condition as a percent of total published monsters.</figcaption>
</figure>

While immunity to the poisoned condition is the most common of these three, it's perhaps the least important for player characters, since few classes are capable of regularly applying it. Meanwhile, the charmed and frightened conditions can be essential tools for several classes, especially spellcasters with access to spells like _[fear](https://www.dndbeyond.com/spells/fear)_ and _[hypnotic pattern](https://www.dndbeyond.com/spells/hypnotic-pattern)_.

Between $$10-20\%$$ are immunities to **exhaustion**, **paralyzed**, and **petrified**. Immunity to the petrified condition is the most noteworthing of these for player characters, due to spells like _[hold person](https://www.dndbeyond.com/spells/hold-person)_ and _[hold monster](https://www.dndbeyond.com/spells/hold-monster)_.

Only the **incapacitated** and **invisible** conditions sit firmly at $$0\%$$, with immunity to the remaining conditions between $$2-9\%$$. Of these conditions, the **stunned** conditions stands out as noteworthy, with only $$3\%$$ of monsters immune to it. Compared to similar conditions, like paralyzed and petrified, which come in at $$15\%$$ and $$11\%$$ respectively, immunity to being stunned is quite low indeed. 

# Condition Immunities by Type

The likelihood of a monster being immune to a specific condition can also depend strongly on the monster's type. This is illustrated in Fig. <a href="#fig:condition-immunity-probability-heat-map" class="fig-ref">2</a> (below), which shows how likely a monster is to be immune to a condition depending on its type.

<figure id="fig:condition-immunity-probability-heat-map">
    {% include_relative monster-condition-immunities/fig-condition-immunity-probability-heat-map-small.html %}
    {% include_relative monster-condition-immunities/fig-condition-immunity-probability-heat-map-large.html %}
    <figcaption>Figure 2: Probability of a published monster being immune to a condition as a percent of the total monsters for its type.</figcaption>
</figure>

**Oozes** are the most consistent out of all of the monster types, with every ooze being immune to the blinded, deafened, exhaustion, and prone conditions, and all but one being immune to the charmed condition. This level of consistency is likely due, at least in part, to there only being 13 oozes of CR 1/8 or higher published in official source books.

**Constructs** are the next, with over two thirds being immune to charmed, exhaustion, frightened, paralyzed, petrified, and poisoned.

Celestials, elementals, and undead all have similarly strong results, with over half of **celestials** being immune to charmed, exhaustion, and frightened, over half of **elementals** being immune to paralyzed, petrified, and poisoned, and over half of **undead** immune to charmed, exhaustion, and poisoned.

The rest of the monster types have far fewer condition immunities than those mentioned already, with **humanoids** having the lowest number of condition immunities on average at only $$0.3$$ immunities per creature.

# Condition Immunities by Challenge Rating

The likelihood of a monster being immune to a condition can also depend on their CR. As Fig. <a href="#fig:condition-immunity-prob-vs-cr" class="fig-ref">3</a> (below) shows, some condition immunities depend strongly on CR, while others are completely independent of it.

<figure id="fig:condition-immunity-prob-vs-cr">
    {% include_relative monster-condition-immunities/fig-condition-immunity-prob-vs-cr-small.html %}
    {% include_relative monster-condition-immunities/fig-condition-immunity-prob-vs-cr-large.html %}
    <figcaption>Figure 3: Probability of a published monster being immune to a condition as a percent of the total monsters for their challenge rating (points), along with trend lines for each condition (lines). <i>Note: You can toggle individual conditions on and off by clicking on them in the legend.</i></figcaption>
</figure>

The condition immunities with the strongest dependence on CR are also the most common: **charmed**, **frightened**, and **poisoned**. All three show very similar overall trend lines, with immunity to the poisoned condition having a slightly lower slope and slightly higher value at low CRs. At very high CRs, while the probabilities can vary quite a lot between CRs, the average for each reaches $$80\%$$ and higher. Even for CRs as low as 13, the average value for each is above $$40\%$$.

Immunity to **exhaustion** and **paralyzed** also show a trend with CR, but their likelihood only increases a small amount in comparison (only around $$15-20\%$$ on average).

The only other immunity to show an average trend with CR is the **stunned** condition. However, it remains relatively constant, at around $$3\%$$, until CR 20 where its likelihood starts increasing.
