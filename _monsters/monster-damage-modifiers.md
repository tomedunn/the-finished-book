---
title: "Monster Damage Modifiers"
excerpt: "An analysis of how damage resistances, immunities, and vulnerabilities depend on monster type and challenge rating."
date: 2023-01-15
last_modified_at: 2023-06-27
tags:
  - analysis
  - damage types
  - immunities
  - mechanics
  - monsters
  - resistances
  - vulnerabilities
---

# Introduction

In 5th edition D&D, damage is broken up into several [damage types](https://www.dndbeyond.com/sources/basic-rules/combat#DamageTypes). These damage types have no general rules on their own, but they can interact with individual monsters in different ways, depending the monster's traits. The most common of these are a monster's damage immunities, resistances, or vulnerabilities.

If a monster is immune to a specific damage type, then any damage it takes of that type is reduced to zero. If they are resistant to a damage type, then any damage they take of that type is halved. And, if they are vulnerable to a damage type, damage they take of that type is doubled. Because each modifies the damage a monster ultimately takes, you can think of them collectively as damage modifiers.

In this post, I look at how common each of these damage modifiers are, as well as how they impact the amount of damage monsters can be expected to take from each damage type, depending on the monster's challenge rating (CR) and monster type. You can find a summary of the dataset used for this analysis [here]({{ site.data.page-links.monster-dataset.path }}).

# Overview

Before digging into how monster types and CR impact a monsters' damage immunities, resistances, and vulnerabilities, lets take a step back and look at things from a broad perspective.

## Non-physical Damage Types
To get a sense of how common each type of damage modification is, Fig. <a href="#fig:nonphysical-modifier-types-by-damage" class="fig-ref">1</a> (below) shows the percent of monsters that are immune, resistant, or vulnerable to each non-physical damage type (everything other than bludgeoning, piercing, and slashing damage).

<figure id="fig:nonphysical-modifier-types-by-damage">
    {% include_relative monster-damage-modifiers/fig-nonphysical-modifier-types-by-damage-small.html %}
    {% include_relative monster-damage-modifiers/fig-nonphysical-modifier-types-by-damage-large.html %}
    <figcaption>Figure 1: Percent of monsters with either resistance, immunity, or vulnerability to each non-physical damage type.</figcaption>
</figure>

Before talking about individual damage types, one thing Fig. <a href="#fig:nonphysical-modifier-types-by-damage" class="fig-ref">1</a> makes clear is that damage vulnerabilities are exceptionally rare. In fact, only $$4\%$$ of monsters have any kind of damage vulnerability, and only one monster is vulnerable to more than one damage type, the slithering tracker from _Mordenkainen Presents: Monsters of the Multiverse_, which is vulnerable to both cold and fire damage.

This means the vast majority of damage modifiers present on monsters are either immunities or resistances.

Going through the non-physical damage types from most affected to least, by far the most affected is **poison** damage, with an average damage reduction of $$28.8\%$$, more than double that of any other damage type! The number of monsters immune to poison damage is especially high, affecting nearly four times as many monsters as any other damage type.

Next comes **cold** damage, which is reduced by $$11.3\%$$ on average, and **fire** damage,  with an average damage reduction of $$11.1\%$$. Fire damage has a bit more immunities than cold damage, but it also has triple the number of vulnerabilities (the highest of all damage types), which almost perfectly balance out.

Rounding out the top half of the spectrum are **lightning** damage at $$8.1\%$$ and **necrotic** damage at $$7.4\%$$ average damage reduction. While there are slightly more monsters immune to necrotic damage than lightning damage, the number of monsters with resistance to lightning is significantly higher.

At the top of the bottom half sits **acid** at $$5.5\%$$ and **psychic** damage at $$5.2\%$$ average damage reduction, which are very similar in all three kinds of damage modifiers. And well below them are **thunder** and **radiant** damage, with $$2.0\%$$ and $$1.0\%$$ average damage reduction respectively, which are significantly different in each modification type.

Finally, at the very bottom, and by far the least affected damage type, is **force** damage. The average damage reduction to force damage is only $$0.4\%$$, nearly 72 times lower than poison damage!

## Physical Damage Types

For physical damage, the picture is a bit more complex. In addition to having monsters who are immune, resistant, or vulnerable to a type of damage, there are also sub-categories, such as monsters who are immune or resistant to damage from non-magical attacks. 

For some of these sub-categories, there can even be multiple wordings that produce subtly different outcomes. Such as the difference between "resistance to damage from non-magical weapons" and "resistance to damage from non-magical attacks". An unarmed strike counts as an attack but not a weapon, which means it would be resisted under the second option but not the first.

Rather than breaking out all of these sub-categories and phrasings, for now I'd just like to focus on a few of the broader categories: immune, resistant, and vulnerable, as well as immune to non-magical damage, and resistant to non-magical damage. The later two are defined by whether or not a magical weapon can be used to overcome them.

<figure id="fig:physical-modifier-types-by-damage">
    {% include_relative monster-damage-modifiers/fig-physical-modifier-types-by-damage-small.html %}
    {% include_relative monster-damage-modifiers/fig-physical-modifier-types-by-damage-large.html %}
    <figcaption>Figure 2: Percent of monsters with either resistance, immunity, or vulnerability to each physical damage type.</figcaption>
</figure>

The probability of a monster falling into each of these categories is shown in Fig. <a href="#fig:physical-modifier-types-by-damage" class="fig-ref">2</a> (above) for each physical damage type. 

While the overall levels of immunity and resistance is on the higher side compared to the non-physical damage types, the vast majority of each can be overcome using a magic weapon, or some other kind of magical attack.

For non-magical damage, the average damage reduction is $$12.1\%$$ for **bludgeoning**, $$12.3\%$$ for **piercing**, and $$12.4\%$$ for **slashing**. This puts the physical damage types just above cold and fire damage, leaving only poison damage worse off in terms of average damage reduction.

However, for magical damage, these averages drop tremendously to $$0.6\%$$ for **bludgeoning**, $$1.0\%$$ for **piercing**, and $$0.9\%$$ for **slashing**, making them as good as the best non-physical damage types, such as force and radiant damage.

# Damage vs Monster CR

With the high level overview out of the way, lets look at how each damage type holds up vs monster CR. Figure <a href="#fig:average-modifier-vs-cr" class="fig-ref">3</a> (below) shows how the average damage changes with CR after applying any damage modifiers a monster might have. The "physical" damage type represents the average across bludgeoning, piercing, and slashing damage.

<figure id="fig:average-modifier-vs-cr">
    {% include_relative monster-damage-modifiers/fig-average-modifier-vs-cr-small.html %}
    {% include_relative monster-damage-modifiers/fig-average-modifier-vs-cr-large.html %}
    <figcaption>Figure 3: Average damage taken after applying damage resistances, immunities, and vulnerabilities for published monsters. Presented as a percent of possible damage done. Physical represents the average of bludgeoning, piercing, and slashing damage.</figcaption>
</figure>

Most damage types show some dependence on CR, but how much varies considerably between them. At the low end are **force**, **radiant**, and **thunder** damage, which are also the damage types with the lowest overall average damage reduction. And at the high end are **cold**, **fire**, **poison**, and **physical** damage, which are also the damage types with the highest overall average damage reduction.

Of the remaining four damage types, **acid** and **lightning** damage show similar trends. Each starts off with low damage reduction before leveling out around $$10\%$$ between CR 7 and 20. Above CR 20 their trends diverge, with the average damage reduction decreasing for acid damage and increasing for lightning damage. 

The average damage reduction for **necrotic** and **psychic** damage also follow similar trends, starting off low and steadily increasing until they peak around CR 20. 

Overall, damage reduction is small below CR 5 for all but poison damage. From CR 5-20, damage reduction remains relatively consistent for most damage types. And for CR 20 and above, damage reduction for cold, fire, lightning, physical, and poison increases significantly.

# Damage vs Monster Type

Breaking down the data by monster type, as shown in Fig. <a href="#fig:damage-reduction-heat-map" class="fig-ref">4</a> (below), also reveals some interesting trends. 

<figure id="fig:damage-reduction-heat-map">
    {% include_relative monster-damage-modifiers/fig-damage-reduction-heat-map-small.html %}
    {% include_relative monster-damage-modifiers/fig-damage-reduction-heat-map-large.html %}
    <figcaption>Figure 4: Average damage reduction for each damage type and monster type.</figcaption>
</figure>

**Force** and **thunder** damage show essentially no dependence on creature type, while **poison** damage reduction is extremely concentrated across constructs, elementals, fiends, and undead.

Several damage types appear especially weak against only a single monster type. **Radiant** damage is only significantly reduce for celestials, **acid** for oozes, **necrotic** for undead, and constructs to **psychic**.

**Cold**, **fire**, and **lightning** damage are all significantly weaker against constructs, dragons, elementals, and fiends, with cold damage also being weak against undead, and lightning against oozes.

Finally, non-magical **bludgeoning**, **piercing**, and **slashing** damage are especially weak against fiends, and to a slightly lesser extend against celestials, constructs, elementals, and undead. Where these physical damage types differ significantly are oozes, which tend to be strong against slashing damage, and plants, which tend to be strong against bludgeoning and piercing damage. These are the only significant sources of damage reduction that remain for physical damage types from magical sources.
