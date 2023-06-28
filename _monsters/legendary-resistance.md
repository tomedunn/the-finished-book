---
title: "The Value of Legendary Resistances"
excerpt: "How valuable are legendary resistances and when should DMs use them?"
date: 2022-09-24
last_modified_at: 2023-03-04
tags:
  - analysis
  - legendary resistance
  - mechanics
  - monsters
---

{% include LaTex.html %}

# Introduction

Legendary resistances are an interesting and unique mechanic within 5th edition D&D. They allow a monster to succeed on a saving throws they otherwise would have failed a set number of times. In short, they act a bit like a "get out of jail free" card. The game allows DMs to decide when to use a monster's legendary resistances, which raises the question, how strong does the effect of failing a saving throw need to be to warrant using one?

In this post, I'll take a brief look at how the game values legendary resistances in order to shed some light on this issue.

# Legendary resistance values

The "Creating a Monster" section from chapter 9 of the DMG covers how monster CRs are estimated from their average hit points, armor class, damage per round, and attack bonus. It also contains suggested values for a number of monster traits in terms of these base parameters. For legendary resistances, the [Monster Features](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterFeatures) table values each use of legendary resistance as being worth a fixed number of hit points, depending on the monster's challenge rating.

> Each per-day use of this trait increases the monster’s effective hit points based on the expected challenge rating: 1–4, 10 hp; 5–10, 20 hp; 11 or higher, 30 hp.

These hit point values can be converted to effective hit points using the following equation,
\begin{align}
    %\eHP &\approx \frac{1}{\sqrt{0.65}} \cdot \HP \left( 1 + 0.077 \left(\AC - 12\right)\right)\,, 
    \eHP &\approx \frac{1}{\sqrt{0.65}} \cdot \HP \left(\frac{\AC - 1 }{ 13 }\right)\,, 
    \label{eq:effective-hit-points-attack-approx} 
\end{align}
where $$\HP$$ represents the hit point value of a legendary resistance, and $$\AC$$ is the typical monster armor class values taken from the [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterStatisticsbyChallengeRating) table from the same chapter (for a full derivation of Eqn. \eqref{eq:effective-hit-points-attack-approx}, see [Effective HP and Damage]({{ site.url }}{{ site.baseurl }}{% link _theory/effective-hp-and-damage.md %})). The results of this calculation are shown in Fig. <a href="#fig:pcs-encounter-edpr-legendary-resistance-vs-level-medium-adventuring-days" class="fig-ref">1</a> (below).

<figure id="fig:pcs-encounter-edpr-legendary-resistance-vs-level-medium-adventuring-days">
    {% include_relative legendary-resistance/fig-pcs-encounter-edpr-legendary-resistance-vs-level-medium-adventuring-days-small.html %}
    {% include_relative legendary-resistance/fig-pcs-encounter-edpr-legendary-resistance-vs-level-medium-adventuring-days-large.html %}
    <figcaption>Figure 1: Effective hit points value of a legendary resistance (solid) and average effective damage per round for PCs (dashed) as a function of monster CR and PC level.</figcaption>
</figure>

When compared against the average effective damage per round for PC base classes taken from [Player Character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %}), it's clear that the two are very similar to one another and follow the same trend. This means, in practice, in order to meet the expected value the game assigns legendary resistances, **each use of legendary resistance should negate the damage or actions of one PC against the monster for a single round of combat**.