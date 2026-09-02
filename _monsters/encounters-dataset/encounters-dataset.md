---
title: "Encounter Dataset"
excerpt: "Summary of the encounter dataset for 5th edition D&D adventures."
permalink: /:collection/:name/
date: 2026-09-02
last_modified_at: 2026-09-02
tags:
  - data
  - combat
  - encounters
  - adventures
---

In order to analyze the encounters found in D&D adventures we first need a dataset that catalogues them in a way that's useful for us. To my knowledge, no such dataset already existed that fit this description, so I made one myself using Python scripts and many hours of checking and editing the results by hand.

For anyone wishing to use this data, each encounter contains the following entries:
* **id.** A unique identifier generated at random using [UUIDv4](https://en.wikipedia.org/wiki/Universally_unique_identifier).
* **type.** Encounters that are likely to result in combat have a type of "combat", while those that aren't likely to result in combat have "non-combat" for their type. When an adventure has multiple versions of an encounter, one of those encounters will have "combat" for its type and the remaining ones will have "alternate combat" instead to avoid double counting monsters.
* **book_path.** The encounter's location within the book constructed from the book's name, chapter name, and section headers separated by "; ".
* **allies.** A list of creatures that can help the PCs during the encounter.
* **bystanders.** A list of creatures present in the encounter but don't aid or hinder the PCs.
* **enemies.** A list of creatures hostile to the PCs in the encounter.

Each entry in the `allies`, `bystanders`, and `enemies` is a list that includes the number of creatures, their monster ID from the [D&D Beyond](https://www.dndbeyond.com/monsters) website, their XP value (this may differ from the one in their stat block), and the the number of round that pass before they join the encounter (this can be omitted for monsters present at the start of the encounter).

Here's an example encounter taken from chapter 1 of _Tyranny of Dragons_.

```json
{
    "id": "52ae7c16-71a1-48b7-88e2-85d91dee99ad",
    "type": "combat",
    "book_path": "Tyranny of Dragons; Greenest in Flames; Wandering Encounters; Chapter 1 Encounters",
    "allies": [],
    "bystanders": [],
    "enemies": [
        [3, "16939-kobold", 25],
        [1, "17466-ambush-drake", 100]
    ]
}
```

# Dataset

The following table contains a list of all the books currently in the dataset, along with links to their respective data files.

<div class="dataframe center" style="width:100%;">
    <h3 id="tab:encounters">Encounters</h3>
    {% include_relative encounters-table.html %}
</div>
