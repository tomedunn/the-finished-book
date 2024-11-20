---
title: "Categorizing Monsters"
excerpt: "Grouping monsters into categories, because not all monsters in D&D 5e should be weighted equally."
permalink: /:collection/:name/
date: 2021-10-15
last_modified_at: 2023-03-09
tags:
  - analysis
  - monsters
  - monster categories
---

# Introduction

Any time we take a statistical look at 5th edition D&D in a way that involves monsters, it's important to keep in mind that not all monsters should be weighted equally. This is especially true when attempting to analyze the strengths and weaknesses of different PC abilities and resources, because a PC is much more likely to faces certain types of monsters than others.

Think of how a campaign is typically structured. Most are broken up across several arcs, or adventures, each of which has an array of different enemies for the PCs to encounter. Enemies encountered towards the beginning tend to be more common and with lower CRs, while those encountered towards the end tend to be more rare and with higher CRs. 

It would be uncommon to have an adventure with only legendary monsters for enemies, but you wouldn't be surprised to face at least one or two legendary monsters by the end of it. Furthermore, the number of legendary monsters you might face in an adventure will likely be far fewer that the number of non-legendary monsters. Put another way, a group of level 10 PCs is much more likely to face five CR 5 **[trolls](https://www.dndbeyond.com/monsters/troll)** during their adventure than they are to face five CR 15 **[adult green dragons](https://www.dndbeyond.com/monsters/adult-green-dragon)**. 

For this reason, when talking about the statistics of monsters, and how PC abilities interact with monsters, it's important that we either weight these rarer monsters lower, or that we break up the results into different categories to provide additional context.

# Monster Categories

To illustrate this point, I've split monsters taken from official source/adventure books into three different categories: "Generic", "Legendary", and "Unique" according to the definitions listed below.

* **Generic.** These monsters are your standard, run-of-the-mill template monster and are the most commonly encounter of the three. You may face any number of these over the course of a campaign. A **[mage](https://www.dndbeyond.com/monsters/mage)** is an example of a generic monster.

* **Legendary.** These are generic monsters that have legendary traits and are significantly less common than their non-legendary counterparts. Over the course of a campaign you may face a handful of these, but it's unlikely you will face more than a few of any specific type. A **[lich](https://www.dndbeyond.com/monsters/lich)** is an example of a legendary monster.

* **Unique.** These monsters are legendary or non-legendary monsters that have a specific name and story significance, and often a unique stat block. Over the course of a campaign they may be roughly as common as Legendary monsters, but you won't encounter more than one of any specific unique monster. The lich **Acererak** is an example of a unique monster.

These categories are designed to group monsters by their relative rarity. Over the course of an adventure, regardless of level, the PCs are far more likely to encounter a Generic monster than they are a Legendary monster or Unique monster. And, while Unique monsters are probably more common at lower levels, due to how rare Legendary monsters are, at high level play they are likely even rarer than Legendary monsters.

<figure id="fig:monster-distribution">
    {% include_relative fig-monster-distribution-small.html %}
    {% include_relative fig-monster-distribution-large.html %}
    <figcaption>Distribution of monsters by CR for each category.</figcaption>
</figure>

Figure \figref{fig:monster-distribution} shows how these categories of monsters are distributed from CR 1 to 30. 

For CR 10 and lower, the vast majority of monsters fall into the Generic category. Meanwhile, the majority of monsters CR 15 and higher fall into the Legendary and Generic categories. As a result, when analyzing aspects of the game that rely on higher CR monster stats, care should be taken to make sure Legendary and Unique monsters aren't being sampled unfairly.