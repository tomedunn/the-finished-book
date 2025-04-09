---
title: "Calibrating Encounter Math"
excerpt: "All this encounter math is good, but how can we check if it's right?"
permalink: /:collection/:name/
header:
  og_image: /assets/images/calibrating-encounter-math.png
date: 2025-04-08
last_modified_at: 2025-04-08
tags:
  - analysis
  - encounter balancing
  - xp
  - D&D 2014
  - D&D 2024
---

{% include LaTex.html %}

# Introduction

*In science, a theory is only as good as it is testable and verifiable.* 

In several posts throughout this site, I look at the mathematics behind combat in D&D 5th edition, with a specific focus on understanding how the encounter balancing rules work. The recent 2024 rules update for D&D 5e introduced new rules for building and balancing encounters and, while I am taking steps towards a full theoretical analysis of those rules, I wanted to take a moment to discuss how we can go about analyzing them in a more empirical way. That is, by comparing them against combat encounter data from actual games of D&D.

At the time of writing this, I, unfortunately, don't have a large enough dataset to do this kind of analysis. Therefore, I've created this [form](https://docs.google.com/forms/d/e/1FAIpQLScUFtEf9rWG4yVmxiJFeN-mVdYp6jAzpRrad8ujxz5diWG34w/viewform), that I'm hoping people will fill out, in order to collect it. The form has only four required questions, that should be quick and easy to fill out, along with five optional questions.

If all you came for was a link to that form then you have my thanks. But, if you are interested learning more about what data is being collected, and how it can be used to calibrate encounter building rules for D&D 5e, then continue reading. In the section that follows, I go over what data is needed to perform this kind of analysis. And, in the section after that, I show what that analysis might look like using simulated data.

# Collecting data

In order to analyze D&D 5e's encounter building rules empirically, combat encounter data from actual games of D&D 5e is needed. There's a lot of data we could collect that would be useful, but, without an automated way of collecting it, it's probably best to keep that data to just the bare essentials. 

What exactly are those bare essentials?

For starters, we need to be able to calculate the difficulty of each encounter using the game's encounter building rules. That means we'll need to know the levels of each of the player characters in each encounter as well as the challenge ratings of each of the monsters. 

Also, since legendary monsters from the [2024 Monster Manual]({{ site.data.page-links.monster-manual-2024.path }}) are significantly stronger than their non-legendary counterparts, we'll also want to track which monsters in each encounter were legendary and what version of the core rules were being used.

On the other side of the equation, we need a way of measuring how difficult each encounter actually was for the PCs. The simplest, direct measure of difficulty is how much damage the party took during the encounter.

I go through a full mathematical explanation of why damage works as a proxy for difficulty in my post [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}), but, in short, the encounter building rules are an abstract way of calculating how much damage the PCs are likely to take on average relative to their maximum hit points, with each difficulty category's XP value representing a fixed percentage of that maximum.

That means, if we know how much XP an encounter is worth according to the rules, $$\XP_{\mathrm{enc}},$$ and how much damage the PCs took from monsters during that encounter, $$D_{\mathrm{enc}},$$ then the two should be related in the following way, provided the rules are accurate,
\begin{align}
    \frac{ \XP_{\mathrm{enc}} }{ \XP_{\mathrm{party}} } &\propto \frac{ D_{\mathrm{enc}} }{ \HP_{\mathrm{party}} } \,,
    \label{eq:xp-to-damage-conversion}
\end{align}
where $$\HP_{\mathrm{party}}$$ is the party's maximum hit points and $$\XP_{\mathrm{party}}$$ is the party's XP value, which can be calculated following the method discussed in my post [Player Character XP]({{ site.data.page-links.player-character-xp.path }}).

Since the plan isn't to collect data on the PCs' classes, builds, or gear, we'll be limited to using the average value across all classes for $$\XP_{\mathrm{party}}.$$ This can lead to large systematic errors for small datasets, but when averaged across many groups in a large dataset those errors should be fairly negligible.

Collecting data on which version of the rules the encounter was run using will also prove useful here, since $$\XP_{\mathrm{party}}$$ is likely to be different between the two.

The total hit points for each party, $$\HP_{\mathrm{party}},$$ would also be useful to collect, but it can also be inferred from the PCs' levels and how the hit points of a typical PC scale with level on average (see [Baseline Player Character Stats]({{ site.data.page-links.baseline-player-character-stats.path }})). And, just like with $$\XP_{\mathrm{party}},$$ as long as the final dataset is sufficiently large, and includes a wide range of classes and builds, the average difference between the two approaches should be small.

In summary, to assess the accuracy of the game's encounter building rules, we'll need to collect the following four essential pieces of data for each encounter:

1. The levels of each PC in the encounter.
2. The challenge rating of each monster in the encounter and which monsters are legendary.
3. How much damage the monsters dealt to the PCs during the encounter.
4. The version of the core rules the game is running.

<!--In the next section, I'll show how this data can be used to assess the game's encounter building rules using simulated survey results.-->

# Simulated analysis 
In this section, I show how the analysis of this data might look using a simulated dataset. The simulated dataset used in this analysis had $$1,000$$ encounters, and the methods for generating it are discussed in the subsection that follows. If you aren't interested in how the data was generated, feel free to skip ahead to the [analysis](#analysis).

## Data generation
The dataset used in this analysis was generated by first constructing the encounters, i.e., the PCs and their levels, along with monsters and their CRs, and then using that information to determine the damage dealt to the PCs by the monsters in each encounter.

Parties were generated for each encounter by picking the number of PCs and their levels at random. For simplicity, all PCs within a party were assumed to be the same level.

The number of PCs in each encounter was generated randomly using a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) with an average of 4 a standard deviation of 1.5, and then truncated to remove parties with fewer than 2 PCs, or greater than 8 PCs. The results of this process for the sample dataset are shown in Fig. \figref{fig:sim-party-size-dist} (below).

<figure id="fig:sim-party-size-dist">
    {% include_relative fig-sim-party-size-dist-small.html %}
    {% include_relative fig-sim-party-size-dist-large.html %}
    <figcaption>Shows the distribution of party sizes for the simulated dataset (blue bars) along with a theoretical curve for the normal distribution used to generate them (orange line).</figcaption>
</figure>

The levels of the PCs in each party were generated randomly using a [log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution) with a mean of $$6$$ and a standard deviation of $$5,$$ and then truncated to remove parties with levels than 1 and greater than 20. The results of this process for the sample dataset are shown in Fig. \figref{fig:sim-party-level-dist} (below).

<figure id="fig:sim-party-level-dist">
    {% include_relative fig-sim-party-level-dist-small.html %}
    {% include_relative fig-sim-party-level-dist-large.html %}
    <figcaption>Shows the distribution of party levels for the simulated dataset (blue bars) along with a theoretical curve for the log-normal distribution used to generate them (orange line). </figcaption>
</figure>

Neither of these distributions were intended to be particularly accurate, just to capture some general trends that are likely to show up in the actual data. Namely, that the typical party size is around four PCs and that most games take place around level 5 with a significant drop-off at higher levels.

The encounter building rules in the 2014 _Dungeon Master's Guide_ were used to generate the monsters for each encounter. This was done by assigning each encounter a difficulty (Easy, Medium, Hard, or Deadly) at random following a uniform distribution (i.e., each being equally likely), and then adding monsters to the encounter until the adjusted XP total fell within the allowed range for that difficulty.

To prevent very low CR monsters from being included in encounters with higher level PCs, a lower bound was placed on the monster CRs at one sixth the party's level. Otherwise, all CRs that could be added without exceeding the encounter's XP range were equally likely.

This method for generating monsters is likely a bit different from how most DMs or adventure designers choose monsters for their encounters, but it should still work reasonable well for the purpose of this dataset and analysis. That said, the number of monsters per encounter created by this approach, shown in Fig. \figref{fig:sim-encounter-size-dist} (below), does seem reasonable.

<figure id="fig:sim-encounter-size-dist">
    {% include_relative fig-sim-encounter-size-dist-small.html %}
    {% include_relative fig-sim-encounter-size-dist-large.html %}
    <figcaption>Shows the distribution of monsters per encounter for a simulated dataset. </figcaption>
</figure>

And the average monster CR faced by parties of each level, shown in Fig. \figref{fig:sim-average-cr-vs-level} (below), is also fairly reasonable, if perhaps a bit lower than expected.

<figure id="fig:sim-average-cr-vs-level">
    {% include_relative fig-sim-average-cr-vs-level-small.html %}
    {% include_relative fig-sim-average-cr-vs-level-large.html %}
    <figcaption>Shows the average monster CR faced by the PCs as a function of party level for a simulated dataset.</figcaption>
</figure>

With the input data established, the final step is to generate the damage done to the PCs for each encounter. To do this, we effectively need to decide what the "correct" answer will be for the analysis that follows. Since the encounters were constructed using the 2014 rules, I decided to use the 2024 rules to determine the damage done to the PCs.

The damage for each encounter was generated randomly following a normal distribution, with an average damage calculated from Eqn. \eqref{eq:xp-to-damage-conversion}, 
\begin{align}
    D_{\mathrm{ave}} = \HP_{\mathrm{party}} \left( \frac{ \XP_{\mathrm{enc}} }{ \XP_{\mathrm{party}} } \right)\,,
    \label{eq:example-damage-mean}
\end{align}
where $$\HP_{\mathrm{party}} = N (1 + 7\,L) $$ is the total hit points of a party of $$N$$ PCs, all at level $$L,$$ and $$\XP_{\mathrm{party}}$$ is the party's XP, which was taken to be half their adventuring day XP. The standard deviation used to generate this data was calculated using the [coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation) (sigma over mean) data for published monsters from my post on [variability and encounter difficulty]({{ site.data.page-links.variability-encounter-difficulty.path }}#fig:monster-dpr-cv).

## Analysis

With the explanation for how the data was generated out of the way, lets move on to analyzing it. To start, lets define a measure of the accuracy of our encounter building rules by taking the ratio of the left and right sides of Eqn. \eqref{eq:xp-to-damage-conversion},
\begin{align}
    \mathrm{accuracy} \equiv
    \frac{ D_{\mathrm{enc}} / \HP_{\mathrm{party}} }{ \XP_{\mathrm{enc}} / \XP_{\mathrm{party}} } \,.
    \label{eq:accuracy-definition}
\end{align}
Recall, $$D_{\mathrm{enc}}$$ is the damage done to the PCs during an encounter, $$\HP_{\mathrm{party}}$$ is the party's total hit points, $$\XP_{\mathrm{enc}}$$ is the encounter's XP calculated via the encounter building rules, and $$\XP_{\mathrm{party}}$$ is the party's XP value, which can be calculated following the method discussed in my post [Player Character XP]({{ site.data.page-links.player-character-xp.path }}).

The accuracy defined by Eqn. \eqref{eq:accuracy-definition} is effectively a measure of how much damage the PCs took relative to how much damage the encounter building rules expected them to take. When $$\mathrm{accuracy} = 1,$$ the encounter building rules correctly predicted the encounter's difficultly, when $$\mathrm{accuracy} < 1$$ they overestimated it and the PCs took less damage than expected, and when $$\mathrm{accuracy} > 1$$ they underestimated it and the PCs took more damage than expected.

<figure id="fig:sim-accuracy-distribution">
    {% include_relative fig-sim-accuracy-distribution-small.html %}
    {% include_relative fig-sim-accuracy-distribution-large.html %}
    <figcaption>Shows the distribution of accuracy values, calculated using Eqn. \eqref{eq:accuracy-definition}, for the 2014 (blue) and 2024 (orange) encounter building rules.</figcaption>
</figure>

Figure \figref{fig:sim-accuracy-distribution} (above) shows the accuracy values of each encounter for the simulated dataset, calculated using Eqn. \eqref{eq:accuracy-definition}, for both the 2014 and 2024 encounter building rules. While there is certainly a lot of noise in the data, these results clearly show that, on average, the 2024 rules correctly predict the damage the party will take, while the 2014 rules consistently overestimate it by around $$32\%.$$

Given the damage done to the PCs in the simulated dataset was generated using the 2024 rules, these results are exactly what we expect to see. The cause of this difference stems from how the 2014 and 2024 rules scale their calculations differently with the number of monsters and PCs in an encounter. Therefore, we should expect to see a difference in how the accuracy of each rules-set scales along these lines as well.

<figure id="fig:sim-accuracy-vs-encounter-size">
    {% include_relative fig-sim-accuracy-vs-encounter-size-small.html %}
    {% include_relative fig-sim-accuracy-vs-encounter-size-large.html %}
    <figcaption>Shows the accuracy, calculated using Eqn. \eqref{eq:accuracy-definition}, vs. the number of monsters per encounter for the 2014 (blue) and 2024 (orange) encounter building rules. Each point represents an individual encounter and each line connects the average (mean) for each encounter size. Also shows the inverse of the 2014 rules' XP multiplier for a party of four PCs (black, dashed).</figcaption>
</figure>

The impact the number of monsters per encounter has on the accuracy is shown in Fig. \figref{fig:sim-accuracy-vs-encounter-size} (above). The 2014 rules are most accurate for encounters with only one monster, and they tend to overestimate the difficulty as the number of monsters increases. This is consistent with how the 2014 encounter XP multiplier scales with the number of monsters. In comparison, the 2024 rules maintain a consistent accuracy regardless of the number of monsters.

<figure id="fig:sim-accuracy-vs-party-size">
    {% include_relative fig-sim-accuracy-vs-party-size-small.html %}
    {% include_relative fig-sim-accuracy-vs-party-size-large.html %}
    <figcaption>Shows the accuracy, calculated using Eqn. \eqref{eq:accuracy-definition}, vs. the number of PCs per encounter for the 2014 (blue) and 2024 (orange) encounter building rules. Each point represents an individual encounter and each line connects the average (mean) for each party size. Also shows the inverse of the 2014 rules' XP multiplier for an encounter with two monsters (black, dashed).</figcaption>
</figure>

The impact the number of PCs per encounter has on the accuracy of each rules-set is shown in Fig. \figref{fig:sim-accuracy-vs-party-size} (above). As expected, while the 2024 rules accurately predict the average difficulty regardless of the number of PCs in the encounter, the 2014 rules overestimate the difficulty for parties of fewer than six PC.

In this case, the reason why the 2014 rules need six or more PCs to match the 2024 rules, and not between three and five as one might expect, is because the average number of monsters per encounter is roughly two for the simulated dataset and not one, as shown previously in Fig. \figref{fig:sim-encounter-size-dist}.

# Conclusion

In summary, in order to properly assess the accuracy of any encounter building rules, we need actual encounter data from real games of D&D 5e. This data is bound to be noisy, due to a variety of factors, which means we'll need a lot of it. The simulated analysis in this post consisted of only $$1,000$$ encounters, and that was still enough to easily differentiate between the 2014 and 2024 encounter building rules. That's an achievable amount of data, but more may still be needed depending on how the data is distributed.

If it turns out that significantly more data is needed that what people are able to submit [here](https://docs.google.com/forms/d/e/1FAIpQLScUFtEf9rWG4yVmxiJFeN-mVdYp6jAzpRrad8ujxz5diWG34w/viewform), then there's always the option of using data collected automatically from digital tools used to create and run encounters. I don't have access to any such data, but I imagine encounter logs from sites like roll20 and D&D Beyond could be used for this purpose for people with access to it.