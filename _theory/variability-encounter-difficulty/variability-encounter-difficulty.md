---
title: "Variability: Encounter Difficulty"
excerpt: "What's the probability of winning for each encounter difficulty?"
permalink: /:collection/:name/
date: 2024-07-29
last_modified_at: 2024-11-13
tags:
  - theory
  - variability
---

{% include LaTex.html %}

<div style="display:none">
\(
% probabilities
\newcommand{\cdf}{\mathit{F}}
\newcommand{\pdf}{\mathit{P}}
% combat
\newcommand{\CV}{\mathit{CV}}
\newcommand{\diff}{\mathit{diff}}
% other
\newcommand{\erf}{\mathrm{erf}}
\newcommand{\win}{\mathrm{win}}
\)
</div>



# Introduction

In my previous post [Variability: Combat]({{ site.data.page-links.variability-combat.path }}), I showed how combat in D&D can be modeled probabilistically. In this post, I expand on this by looking at how encounter difficulty and damage variability impact the party's chance of winning or losing.

# Review
From [Variability: Combat]({{ site.data.page-links.variability-combat.path }}), for an encounter with only two combatants, the probability that combatant $$i$$ wins during any given turn $$t$$, by defeating combatant $$j$$, can be expressed in the following way,
\begin{align}
    \pdf_{i} \left( \win, t \right) &= \pdf_{i} \left( d \ge \HP_{j}, t \right) \cdf_{j} \left( d \lt \HP_{i}, t \right) \,.
    \label{eq:win-prob-delta}
\end{align}
Here, $$\pdf_{i} \left( d \ge \HP_{j}, t \right)$$ is the probability of the combatant's total damage equalling or exceeding its opponent's maximum hit points $$\HP_{j}$$ during turn $$t$$, and $$\cdf_{j} \left( d \lt \HP_{i}, t \right)$$ is the cumulative probability that the combatant's opponent's total damage is less than its maximum hit points $$\HP_{i}$$ by the end of turn $$t$$.

Using a Gaussian approximation, these can be expressed in terms of each combatant's average total damage $$\mu(t)$$ and the [variance](https://en.wikipedia.org/wiki/Variance) of its total damage $$\sigma^2(t)$$,
\begin{align}
    \pdf_{i} \left( d \ge \HP_{j}, t \right)
        &= \frac{ 1 }{ 2 } \left[ \erf \left( X_{i} \left( t-1 \right) \right) - \erf \left( X_{i} \left( t \right) \right) \right] , \label{eq:gaussian-pdf} \\\\ 
    \cdf_{j} \left( d \lt \HP_{i}, t \right) 
        &= \frac{ 1 }{ 2 } \left[ 1 + \erf \left( X_{j} \left( t \right) \right) \right] , \label{eq:gaussian-cdf}
\end{align}
where $$\erf$$ is the [error function](https://en.wikipedia.org/wiki/Error_function), and 
\begin{align}
    X_{i} \left( t \right) = \frac{ \HP_{j} - \mu_{i}(t) }{  \sqrt{2 \sigma_{i}^2(t)} } .
    \label{eq:xi-general}
\end{align}
Under this approximation, the probability of either combatant winning, either in total or during each turn of the encounter, is dictated by $$X(t)$$ from Eqn. \eqref{eq:xi-general}.


# Encounter difficulty

From my previous post on [XP and encounter balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}#derivation), the difficulty of an encounter can be thought of as measuring how much damage the player characters (PCs) take, on average, relative to their maximum hit points. Casting this into an encounter with just two combatants, the difficulty of the encounter for combatant $$i$$ would be
\begin{align}
    \diff_{i} &= \frac{ d_{j} }{ \HP_{i} } \,,
    \label{eq:diff-general}
\end{align}
where $$\HP_{i}$$ is the combatant's maximum hit points, and $$d_{j}$$ is the average total damage dealt by their opponent, combatant $$j$$, during the encounter.

<!--
While $$d$$ could be calculated from the [final damage distribution]({{ site.data.page-links.variability-combat.path }}#final-damage-distribution), 
-->

In the case where the average damage each turn, $$\mu$$, for each combatant remains constant throughout the encounter, the total damage done by a combatant's opponent is simply $$d_{j} = \mu_{j} N_{i}$$, where $$N_{i} = \HP_{j} / \mu_{i}$$ is the number of turns it would take the combatant to defeat their opponent on average. 

Combining these together Eqn. \eqref{eq:diff-general} can be rewritten as
\begin{align}
    \diff_{i} 
        = \frac{ \HP_{j} \, \mu_{j} }{ \HP_{i} \, \mu_{i} } 
        = \frac{ N_{i} }{ N_{j} } \,.
    \label{eq:diff-constant-dpr}
\end{align}

This makes sense intuitively. If the PCs are capable of defeating all the enemy monsters in only two rounds, while the monsters would need ten rounds to defeat all the PCs, then $$\diff_{i} = 0.2$$ and the encounter would be quite easy for the PCs. Alternatively, if both the PCs and the monsters are capable of defeating their opponent is three rounds, then $$\diff_{i} = 1.0$$ and the encounter would be quite deadly for the PCs.

If we continue on with this simplification and assume the variance of each combatant's damage per turn, $$\sigma^2$$, also remains constant throughout the encounter, then the average and variance of the total damage for each combatant simplifies to
\begin{align}
    \mu(t)      &= n(t) \, \mu      \,, \\\\ 
    \sigma^2(t) &= n(t) \, \sigma^2 \,,
\end{align}
where $$n(t)$$ is the number of turns the combatant has taken by turn $$t$$ of the encounter. For example, on the first turn of an encounter with two combatants, $$i$$ and $$j$$ where $$i$$ goes first, $$n_{i}(1) = 1$$ and $$n_{j}(1) = 0$$, and on the fourth turn $$n_{i}(4) = 2$$ and $$n_{j}(4) = 2$$.

Plugging these into Eqn. \eqref{eq:xi-general} yields
\begin{align}
    X_{i} \left( t \right) 
        &= \frac{ \HP_{j} - n_{i}(t) \, \mu_{i} }{ \sqrt{2 \, n_{i}(t) \, \sigma_{i}^2 } } \,,
\end{align}
which can simplify further by substituting $$N_{i} \, \mu_{i} = \HP_{j}$$,
\begin{align}
    X_{i} \left( t \right) 
        &= \frac{ N_{i} \, \mu_{i} - n_{i}(t) \, \mu_{i} }{ \sqrt{2 \, n_{i}(t) \, \sigma_{i}^2 } } \nonumber \\\\ 
        &= \frac{ N_{i} -  n_{i}(t) }{ \CV_{i} \sqrt{2 \, n_{i}(t) } } \,,
\end{align}
where $$\CV_{i} = \sigma_{i} / \mu_{i}$$ is the [coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation) (commonly known as sigma over mean) of the combatant's damage per turn.

Combining this with Eqn. \eqref{eq:diff-constant-dpr}, the probability of a combatant winning an encounter can be determined by the encounter's difficulty for the combatant, $$\diff_{i},$$ the coefficient of variation of the damage per turn for the combatant, $$\CV_{i},$$ and its opponent, $$\CV_{j},$$ and the number of rounds it takes the combatant to win on average, $$N_{i},$$ via Eqns. \eqref{eq:win-prob-delta} -- \eqref{eq:gaussian-cdf} with
\begin{align}
    X_{i} \left( t \right) 
        &= \frac{ N_{i} -  n_{i}(t) }{ \CV_{i} \sqrt{2 \, n_{i}(t) } } \,, \\\\ 
    X_{j} \left( t \right) 
        &= \frac{ \left( N_{i} / \diff_{i} \, \right) -  n_{j}(t) }{ \CV_{j} \sqrt{2 \, n_{j}(t) } } \,. \label{eq:xi-simple-single}
\end{align}

# Analysis

With the results of the previous section in hand, lets look at how encounter difficulty impacts the probability of the PCs winning a combat encounter. 

For this analysis, I've used a party of four identical PCs in an encounter with a single NPC. The average number of turns it takes the PCs to win is $$N_{i} = 12$$, or three rounds of combat. I plan on exploring the impact of initiative in a future post, but for now I've assumed the NPC always goes third in the initiative order. For the sake of simplicity, I've also assumed none of the PCs are taken out early in the encounter. In other words, the four PCs here act as a single combatant that takes four turns per round.

Because the previous section assumed only two combatants, we need to modify Eqn. \eqref{eq:xi-simple-single} slightly to make it work for a party of four PCs. This is done generally by multiplying $$N_{i} / \diff\,$$ by $$R_{j} / R_{i}$$, where $$R_{i}$$ and $$R_{j}$$ are the number of turns taken each round by the PCs and NPCs respectively. Therefore, for an encounter with four PCs and one NPC, $$R_{i} = 4$$ and $$R_{j} = 1$$, the needed substitution into Eqn. \eqref{eq:xi-simple-single} is $$N_{i} / \diff \rightarrow N_{i} / (4 \, \diff\,)$$.

Figure [1](#fig:win-vs-diff-deadly){: .fig-ref} (below) shows the probability of the PCs winning as a function of the encounter difficulty for the PCs, $$\diff_{i}$$, with $$\CV_{i} = 0.5$$ and $$\CV_{j} = 0.5$$ (these values fall roughly in the middle of the observed values for PCs and NPCs).

<figure id="fig:win-vs-diff-deadly">
    {% include_relative fig-win-vs-diff-deadly-small.html %}
    {% include_relative fig-win-vs-diff-deadly-large.html %}
    <figcaption>Figure 1: Shows the probability of each side winning in an encounter with four identical PCs and one NPC who goes third in initiative. For the PCs \(N_{i} = 12\) and \(\CV_{i} = 0.5\), and for the NPC \(\CV_{j} = 0.5\). The encounter difficulty thresholds shown here are \(\diff_{i} = 0.15\) for Easy, \(\diff_{i} = 0.30\) for Medium, \(\diff_{i} = 0.45\) for Hard, and \(\diff_{i} = 0.70\) for Deadly.</figcaption>
</figure>

The probability of the PCs winning behaves largely as expected, starting out near one and decreasing with the encounter difficulty past the start of the Hard difficulty range. By the end of the Hard difficulty range, the probability of the PCs winning has dropped to around $$89\%$$, and it continues to drop in a fairly linear fashion throughout the Deadly difficulty range until reaching $$50\%$$ at $$\diff_{i} = 1$$.

That the PCs have only a $$50\%$$ chance of winning when $$\diff_{i} = 1$$ makes intuitive sense, since the PCs and NPCs are expected to win in the same number of rounds before factoring in variability. This result is helped by the fact that the enemy NPC always goes third in the initiative order. If they had gone earlier in the initiative order then their chances of winning would be higher, and they had gone later the chances would be lower.

**Note.** The difficulty ranges shown in Fig. [1](#fig:win-vs-diff-deadly){: .fig-ref} assume the PCs overall power level, both their damage output and survivability, matches the baseline values assumed by the D&D encounter building rules. For a variety of reasons, this may not be the case. Groups that are stronger or weaker than those baselines can be accounted for by moving their difficulty thresholds up or down accordingly.
{: .notice--warning}

To understand the impact of the NPC's damage variability, Fig. [2](#fig:win-vs-npc-cv-deadly){: .fig-ref} (below) shows how the probability of the PCs and NPC winning change across a range of $$\CV_{j}$$ values for a Deadly encounter with $$\diff_{i} = 0.7$$. As the NPC's damage variability increases, their odds of winning increase in a nearly linear fashion.

<figure id="fig:win-vs-npc-cv-deadly">
    {% include_relative fig-win-vs-npc-cv-deadly-small.html %}
    {% include_relative fig-win-vs-npc-cv-deadly-large.html %}
    <figcaption>Figure 2: Shows the probability of each side winning in a Deadly encounter, \(\diff_{i} = 0.7\), with four identical PCs against one NPC, as a function of NPC damage variability \(\CV_{j}\). For the PCs, \(N_{i} = 12\) and \(\CV_{i} = 0.5\), and the NPC goes third in the initiative order.</figcaption>
</figure>

This result can be understood by considering how higher $$\CV_{j}$$ values impact the NPC's damage distributions during each round of combat. As $$\CV_{j}$$ increases, the width of the NPC's damage distribution gets wider. Since their average damage is dictated by the encounter's difficulty, which is held fixed at $$\diff_{i} = 0.7$$, higher $$\CV_{j}$$ increases the probability of the NPC doing larger amounts of damage. As a result, the chance of the NPC getting lucky and defeating the PCs quickly increases, reducing the PCs' overall chance of winning the encounter.

This same approach can be applied to understand the impact of the PCs' damage variability, the results of which are shown in Fig. [3](#fig:win-vs-pc-cv-deadly){: .fig-ref} (below). While the overall change isn't as large as it was in the previous example, increasing the PCs' damage variability also increases the NPC's odds of winning. 

<figure id="fig:win-vs-pc-cv-deadly">
    {% include_relative fig-win-vs-pc-cv-deadly-small.html %}
    {% include_relative fig-win-vs-pc-cv-deadly-large.html %}
    <figcaption>Figure 3: Shows the probability of each side winning in a Deadly encounter, \(\diff_{i} = 0.7\), with four identical PCs against one NPC, as a function of the PCs damage variability \(\CV_{i}\). For the PCs, \(N_{i} = 12\) and \(\CV_{i} = 0.5\), and the NPC goes third in the initiative order.</figcaption>
</figure>

This may seem counter intuitive, but, just like in the previous example, the results can be understood by considering how higher $$\CV_{i}$$ values affect the PCs' damage distributions. As $$\CV_{i}$$ increases, the width of the the PCs' damage distributions gets wider. This increases the probability of the PCs getting unlucky and dealing damage far below their average. As a result, there is a higher chance that the PCs will take more rounds than the average to win, leaving more room of the NPC to get lucky and defeat them first.

What both of these examples illustrate is that **increasing the overall damage variability makes unlikely outcomes more likely to occur**. Since the PCs were favored in these example, the unlikely outcome is the enemy NPC winning. If we were to look at example encounters where the enemy NPC was favored to win instead, the sensitivities to $$\CV$$ would be reversed and higher levels of variability would increase the odds of the PCs winning instead of the NPC.

# Tiers of play

The results of the previous section make it clear that higher values of $$\CV$$, for both PCs and for NPCs, lead to combat being more deadly for the PCs at typical difficulty levels. This has profound implications for how deadly the game is in different tiers of play.

As shown in Fig. [4](#fig:monster-dpr-cv){: .fig-ref} (below) for non-legendary monsters from several published D&D source books, damage per round (DPR) $$\CV$$ values for monsters drop significantly, on average, as their challenge rating (CR) increases. This is because higher CR monsters tend to attack and force saves more often, and their attacks and saves are [more accurate]({{ site.data.page-links.baseline-player-character-stats.path }}#fig:hp-vs-level) than they are at lower CRs.

<figure id="fig:monster-dpr-cv">
    {% include_relative fig-monster-dpr-cv-small.html %}
    {% include_relative fig-monster-dpr-cv-large.html %}
    <figcaption>Figure 4: Shows monster damage per round \(\CV\) (sigma over mean) for 409 monsters from the 2014 <em>Monster Manual</em>, <em>Fizban's Treasury of Dragons</em>, <em>Mordenkainen Presents: Monsters of the Multiverse</em>, and <em>Bigby Presents: Glory of the Giants</em>. Legendary monsters and monsters that relied on spellcasting were not included.</figcaption>
</figure>

If we take typical $$\CV$$ values from Fig. [4](#fig:monster-dpr-cv){: .fig-ref} for each tier of play ($$\CV = 0.8$$ for tier 1, $$\CV = 0.6$$ for tier 2, $$\CV = 0.4$$ for tier 3, and $$\CV = 0.2$$ for tier 4) and apply them to both the PCs and NPCs, then we can get a sense for how much the deadliness of combat changes as the PCs level up. The results of this are shown in Fig. [5](#fig:win-vs-diff-tiers){: .fig-ref} (below) for encounters of the same form shown previously in Fig. [1](#fig:win-vs-diff-deadly){: .fig-ref}.

<figure id="fig:win-vs-diff-tiers">
    {% include_relative fig-win-vs-diff-tiers-small.html %}
    {% include_relative fig-win-vs-diff-tiers-large.html %}
    <figcaption>Figure 5: Shows the probability of the PCs losing in an encounter with four identical PCs and one NPC. For the PCs \(N_{i} = 12\), and the NPC goes third in the initiative order. The tiers of play correspond to different damage sigma over mean values used for each combatant: \(\CV = 0.8\) for tier 1, \(\CV = 0.6\) for tier 2, \(\CV = 0.4\) for tier 3, and \(\CV = 0.2\) for tier 4. The encounter difficulty thresholds shown here are \(\diff_{i} = 0.15\) for Easy, \(\diff_{i} = 0.30\) for Medium, \(\diff_{i} = 0.45\) for Hard, and \(\diff_{i} = 0.70\) for Deadly.</figcaption>
</figure>

The difference in deadliness is quite significant in two ways. For low tiers of play, especially tier 1, the odds of the PCs losing to a Deadly encounter is quite significant, and even Hard difficulty encounters have a non-trivial chance of the PCs losing. For higher tiers of play, especially tier 4, the PCs don't have a significant chance of losing until the difficulty is well into the Deadly category, after which it increases rapidly to $$50\%$$.

Before concluding, it's important to stress here that this difference in how deadly encounters are between low level and high level play is not because of some miscalibration of our difficulty metric $$\diff_{i}$$. Regardless of the value of $$\CV$$ used, the average damage taken by the PCs is the same for each value of $$\diff_{i}$$. The trends shown here are purely the result of variability, i.e., the randomness that comes from rolling dice to determine outcomes in combat.

# Percieved difficulty

Previously, we defined the encounter difficulty, $$\diff,$$ based on the damage we expect the PCs to take, on average, but the actual damage will differ from this within some range about that average. As a result, how difficult the encounter feels in play will also vary about the intended difficulty.

We can see an example of this in Fig. [6](#fig:damage-vs-diff){: .fig-ref} (below) which shows the average damage taken by each side in the encounter shown previously in Fig. [1](#fig:win-vs-diff-deadly){: .fig-ref}, along with the a $$60\%$$ confidence interval about that average.

<figure id="fig:damage-vs-diff">
    {% include_relative fig-damage-vs-diff-small.html %}
    {% include_relative fig-damage-vs-diff-large.html %}
    <figcaption>Figure 6: Shows the average damage taken for each side in an encounter with four identical PCs and one NPC who goes third in initiative. For the PCs \(N_{i} = 12\) and \(\CV_{i} = 0.5\), and for the NPC \(\CV_{j} = 0.5\). The encounter difficulty thresholds shown here are \(\diff_{i} = 0.15\) for Easy, \(\diff_{i} = 0.30\) for Medium, \(\diff_{i} = 0.45\) for Hard, and \(\diff_{i} = 0.70\) for Deadly.</figcaption>
</figure>

For Hard encounters and below the average damage taken by the PCs matches the expected value, but for higher difficulties the damage is lower. This trend comes from the damage taken being capped at the maximum hit points for each side. This causes the low damage portions of the distribution to pull the average down. If we were to plot the median damage instead of the mean for the average, it would continue to follow the expected trend all the way up to $$\diff=1.$$

We can convert the final damage distribution for an encounter into a difficulty distribution using the $$\diff$$ ranges for each difficulty: $$0.0-0.15$$ for Trivial, $$0.15-0.3$$ for Easy, $$0.3-0.45$$ for Medium, $$0.45-0.7$$ for Hard, $$0.7-1.0$$ for Deadly, and $$\ge 1$$ for a TPK. Figure [7](diff-probabilities){: .fig-ref} (below) shows this for the encounter described previously in Fig. [6](#fig:damage-vs-diff){: .fig-ref} with target $$\diff$$ values at the center of each difficulty range.

<figure id="fig:diff-probabilities">
    {% include_relative fig-diff-probabilities-small.html %}
    {% include_relative fig-diff-probabilities-large.html %}
    <figcaption>Figure 7: Shows the probability an encounter's damage falls into each difficulty ranges based on the targeted encounter difficulties at the center of each difficulty range; \(\diff_{i} = 0.225\) for Easy, \(\diff_{i} = 0.375\) for Medium, \(\diff_{i} = 0.575\) for Hard, and \(\diff_{i} = 0.85\) for Deadly. The encounter has four identical PCs and one NPC who goes third in initiative. For the PCs \(N_{i} = 12\) and \(\CV_{i} = 0.5\), and for the NPC \(\CV_{j} = 0.5\).</figcaption>
</figure>

While the most probable perceived difficulty is the target for each difficulty category, only the Easy encounter is on target more than $$50\%$$ of the time. For the rest the perceived difficulty is more likely to be either one category higher or lower than on target.

The $$\CV$$ values used here reflect those near the end of tier 2 and the beginning of tier 3. Therefore, these distributions will be broader at low levels, where $$\CV$$ is higher, and narrower at higher levels, where $$\CV$$ is lower.

# Conclusion

Variability, especially from damage, plays a major role in determining how deadly encounters are for the PCs in D&D. Higher levels of damage variability increase the likelihood of the PCs being defeated for Deadly, and even Hard encounters. And, since damage variability tends to be higher at lower levels for both PCs and monsters, this makes low level combat considerably more deadly than high level combat and perceived accuracy of the encounter building rules to be lower. Results that are frequently observed by people who play D&D 5th edition.

While approach used here should be sufficient to illustrate the general trends for how variability impacts the odds of the PCs winning or losing combat encounters of different difficulties, it isn't sufficiently robust to cover all combat scenarios. I have one more post planned for this series that looks at the impact of initiative, but it would also be good to revisit this topic for encounters with multiple monsters, encounters where individual combatants can be defeated before the end of the encounter, and encounters where healing can be used to improve survivability and bring back fallen allies.