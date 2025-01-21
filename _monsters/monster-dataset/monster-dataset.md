---
title: "Monster Dataset"
excerpt: "A list of the book that make up the monster datasets used for these analysis."
permalink: /:collection/:name/
date: 2023-06-27
last_modified_at: 2025-01-20
tags:
  - analysis
  - monsters
---

The [Book Progress](#tab:book-progress){: .fig-ref} table (below) summarizes the dataset used throughout these posts for analyzing monsters from D&D 5th edition. The "Added" column signifies the number of monsters from each book that have been added to the dataset, which means they can be referenced for basic monster statistics, and the "Processed" column indicates the number of monsters who have been analyzed in more detail, which means they can be reference for more advanced monster statistics. Here is a list of stats available from each of these categories:

* **Added Monster Stats.** Monsters who have been added to the dataset can be referenced for size, type, subtype, hit points, armor class, speed, ability scores, saving throws, skill, resistances, immunities, senses, languages, and challenge ratings.

* **Processed Monster Stats.** Monsters who have been processed within the dataset can also be referenced for adjusted hit points, adjusted armor class, damage per round, adjusted damage per round, attack bonus, adjusted attack bonus, save difficulty class, and adjusted save difficulty class.

Adding monsters to the dataset is mostly automated, making it a relatively easy and quick process. Processing monsters, on the other hand, is unfortunately still done by hand. I try to go through each book shortly after it's release, but because of its time consuming nature and my general lack of free time, delays are common.

<div class="dataframe center" style="width:100%;">
    <h3 id="tab:book-progress">Book Progress</h3>
    <style>
        table td:nth-child(n+5) {
            text-align: right;
        }
    </style>
    {% include_relative source-books-summary.html %}
</div>

<!--
[Monster Dataset](https://raw.githubusercontent.com/tomedunn/the-finished-book/master/assets/data/monsters.csv){: .btn .btn--primary}
-->

