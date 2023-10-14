---
title: "Variability: Damage and Healing Rolls"
excerpt: "How do we account for variability of dice rolls in D&D"
date: 2023-10-14
last_modified_at: 2023-10-14
tags:
  - theory
  - monsters
  - classes
  - variability
  - damage
  - healing
---

{% include LaTex.html %}

<div style="display:none">
\(
% generic
\newcommand{\attack}{\mathrm{a}}
\newcommand{\die}{\mathrm{d}}
\newcommand{\total}{\mathrm{t}}
\newcommand{\CV}{\mathit{CV}}
\newcommand{\prob}{\mathit{p}}
\newcommand{\roll}{\mathrm{roll}}
\)
</div>

# Introduction
A lot of analysis around D&D focuses on average outcomes. What's the average damage of a monster's attack? How many targets will a spell hit on average? In fact, much of the analysis on this site relies on analyzing average outcomes as well.

This kind of analysis is useful and can be used to great effect (monster CR estimates are rooted in this kind of analysis), but it can also leave out important information regarding how likely those outcomes are, and how much variability we should expect around those averages.

For example, an attack that has a 100% chance to hit for 10 damage and an attack that has a 50% chance to hit for 20 damage both deal the same average damage. However, after two attacks the first is guaranteed to deal 20 damage and the second only has a 50% chance of doing the same, with a 25% chance of dealing 0 damage and a 25% chance of dealing 40 damage. The second attack has more variability than the first because it has a wider range of probable outcomes.

If these two attacks were given to two otherwise identical monsters, the two monsters would likely feel quite different in play. Groups facing the monster with a 100% chance to hit for 10 damage would all experience similar outcomes, while the outcomes for the groups facing the monster with a 50% chance to hit for 20 damage would likely be much more varied.

There is a lot of ground to explore on the topic of variability in D&D, more than I can cover in a single post. So, in this post I explore how we can characterize the variability of common dice rolls in D&D used for determining effects like damage and healing, and how that variability can be tuned to better serve out needs.

# Single die rolls

The simplest kind of dice roll in D&D are damage/healing rolls, where one or more dice are rolled and then added together, along with an additional modifier in some cases, and the resulting total is then applied as either damage or healing to one or more targets.

Most often, these rolls use only a single type of die (e.g., 3d6 + 4) but they can sometimes include more than one (e.g., 1d6 + 1d8 + 5). Regardless of the number of dice used, the variability of a roll depends on the variability of each component die roll that goes into it.

In this section, I look at the variability of individual dice commonly used in D&D, and the section that follows takes those results and applies them to dice rolls with multiple dice.

At the most basic level, all random processes are described by their probability distribution, $$\prob(x)$$, which tells us the probability of the process resulting in a value $$x$$. For a single roll of a standard $$n$$-sided die, $$\die_n$$, each side is equally likely to come up, which means the probability distribution can be written as
\begin{align}
    \prob_{\die_n}(x) &=
        \begin{cases} 
            \frac{1}{n} & 1 \le x \le n \\\\ 
            0 & \mathrm{otherwise}
        \end{cases}
    \,.
    \label{eq:die-probability-distribution}
\end{align}
For each size of die, this produces a flat probability distribution, as shown in Fig. [1](#fig:die-pd){: .fig-ref} (below).

<figure id="fig:die-pd">
    {% include_relative variability-damage-healing-rolls/fig-die-pd-small.html %}
    {% include_relative variability-damage-healing-rolls/fig-die-pd-large.html %}
    <figcaption>Figure 1: Shows the probability distribution for common dice sizes use in damage and healing rolls in D&D.</figcaption>
</figure>

Other useful tools for describing a random process, like a die roll, is through its [mean](https://en.wikipedia.org/wiki/Mean) $$(\mu)$$ and [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) $$(\sigma)$$, which can both be calculated from the process's probability distribution.

For a single $$n$$-sided die, the mean result $$(\mu_{\die_n})$$ can be calculated by taking the weighted average of all possible results using Eqn. \eqref{eq:die-probability-distribution},
\begin{align}
    \mu_{\die_n } &= \sum_{x=1}^{n} \prob_{\die_n}(x) \cdot x \nonumber \\\\ 
                  &= \sum_{x=1}^{n} \frac{x}{n} \nonumber \\\\ 
                  &= \left( \frac{ n   + 1 }{ 2 } \right) \,,
    \label{eq:die-mean}
\end{align}
and the standard deviation $$(\sigma_{\die_n})$$ can be calculated similarly,
\begin{align}
    \sigma_{\die_n} &= \left[ \left( \sum_{x=1}^{n} \prob_{\die_n}(x) \cdot x^2 \right) - \mu_{\die_n}^2 \right]^{1/2} \nonumber \\\\ 
        &= \left[ \left( \sum_{x=1}^{n} \frac{ x^2 }{ n } \right) - \mu_{\die_n}^2 \right]^{1/2} \nonumber \\\\ 
        &= \left[ \left( \frac{ \left(n   + 1\right) \left(2n + 1\right) }{ 6 } \right) - \left( \frac{ n   + 1 }{ 2 } \right)^2 \right]^{1/2} \nonumber \\\\ 
        &= \left( \frac{n^2 - 1}{12} \right)^{1/2}\,.
    %\sigma_{\die_n}^2 &= \left( \frac{n^2 - 1}{12} \right)\,.
    \label{eq:die-sigma}
\end{align}

Since the dice rolls used in D&D almost always result in positive values, the ratio between these two, known as the [coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation) $$(\CV\,)$$ (commonly referred to as sigma over mean), can also prove useful as it allows the variability of rolls with different means to compared with one another.

The $$\CV$$ for a single $$n$$-sided die, $$\die_n$$, can be calculated using Eqns. \eqref{eq:die-mean} and \eqref{eq:die-sigma}, which gives,
\begin{align}
    \CV_{\die_n} &= \left( \frac{ n - 1 }{ 3 \left( n + 1 \right) } \right)^{1/2}\,.
    \label{eq:die-cv}
\end{align}

The [Dice Stats](#tab:die-stats){: .fig-ref} table (below) gives $$\mu$$, $$\sigma$$, and $$\CV$$ values, calculated using the above equations, for the most common dice used in damage/healing rolls. Note that $$\CV$$ increase along with $$n$$, meaning **larger dice offer more variability relative to their mean value than smaller dice**.

<div class="dataframe center" style="width:300; max-width: 100%;">
    <h3 id="tab:die-stats">Dice Stats</h3>
    {% include_relative variability-damage-healing-rolls/tab-die-stats.html %}
</div>

**Note.** A $$\die_1$$ represents a one-sided die, i.e., a constant, and can be used to represent any modifiers added onto a roll.
{: .notice--warning}

# Rolls with multiple dice

For damage/healing rolls that uses more than one die, the mean value of the roll $$(\mu_{\roll})$$ can be calculated by performing a weighted average of each possible outcome, just like we did for a single die in the previous section, but doing so becomes increasingly difficult as the number of dice increases. A much quicker way to calculate the mean is to simply add up the means of the individual dice, 
\begin{align}
    \mu_{\roll} &= \sum_{n = 1}^{\infty} N_{\die_n} \cdot \mu_{\die_n} \,, 
    \label{eq:damage-roll-mean}
\end{align}
where $$N_{\die_n}$$ is the number of $$n$$-sided dice in the roll. 

A similar shortcut can be used when calculating a roll's standard deviation $$(\sigma_{\roll})$$, where the variances (standard deviation squared) of each die are added together before taking the square root of the resulting total,
\begin{align}
    %\sigma_{\roll}^2 &= \sum_{n = 1}^{\infty} N_{\die_n} \cdot \sigma_{\die_n}^2 \,.
    \sigma_{\roll} &= \left( \sum_{n = 1}^{\infty} N_{\die_n} \cdot \sigma_{\die_n}^2 \right)^{1/2} \,.
    \label{eq:damage-roll-variance}
\end{align}

Finally, a roll's coefficient of variation can be calculate in the usual way by taking the ratio between $$\sigma_{\roll}$$ and $$\mu_{\roll}$$,
\begin{align}
    \CV_{\roll} &= \frac{ \left( \sum_{n = 1}^{\infty} N_{\die_n} \cdot \sigma_{\die_n}^2 \right)^{1/2} }{ \sum_{n = 1}^{\infty} N_{\die_n} \cdot \mu_{\die_n} }\,.
    \label{eq:damage-roll-coef-variation}
\end{align}


For rolls with only a single type of die and modifier, which covers the vast majority of damage and healing rolls in D&D, Eqns. \eqref{eq:damage-roll-mean} and \eqref{eq:damage-roll-variance} simplify to 
\begin{align}
    \mu_{\roll} &= N_{\die_n} \cdot \mu_{\die_n} + N_{\die_0} \,; \label{eq:sd-roll-mean} \\\\ 
    \sigma_{\roll} &= \sqrt{N_{\die_n}} \cdot \sigma_{\die_n} \,, \label{eq:sd-roll-sigma}
\end{align}
where $$\mu_{\die_n}$$ and $$\sigma_{\die_n}$$ can be calculated using Eqns. \eqref{eq:die-mean} and \eqref{eq:die-sigma} respectively, or taken directly from the [Dice Stats](#tab:die-stats){: .fig-ref} table in the previous section.

To get a better sense of how these scale with the size and number of dice, Fig. [2](#fig:cv-die-sigma-vs-mean){: .fig-ref} (below) plots $$\mu_{\roll}$$ and $$\sigma_{\roll}$$ values for common dice sizes ($$n = 4$$, $$6$$, $$8$$, $$10$$, and $$12$$), for the case where $$N_{\die_0} = 0$$, along with lines of constant $$\CV$$ for reference.

<figure id="fig:cv-die-sigma-vs-mean">
    {% include_relative variability-damage-healing-rolls/fig-cv-die-sigma-vs-mean-small.html %}
    {% include_relative variability-damage-healing-rolls/fig-cv-die-sigma-vs-mean-large.html %}
    <figcaption>Figure 2: Shows mean and standard deviation values for common dice rolls without modifiers, along with reference lines of constant \(\CV\) (dashed lines). Hovering over a point, or selecting it on mobile, shows the dice equation along with its \(\CV\). Each roll's \(\CV\) can be reduced by adding a modifier, increasing its mean and shifting its point to the right.</figcaption>
</figure>

One of the most interesting trends shown in Fig. [2](#fig:cv-die-sigma-vs-mean){: .fig-ref} is that **as the number of dice increases the variability of the roll decreases**. We can confirm this trend by using Eqns. \eqref{eq:sd-roll-mean} and \eqref{eq:sd-roll-sigma}, with $$N_{\die_0} = 0$$, to calculate $$\CV = \sigma/\mu$$ for the roll,
\begin{align}
    \CV_{\roll} &= \frac{ \sqrt{N_{\die_n}} \cdot \sigma_{\die_n} }{ N_{\die_n} \cdot \mu_{\die_n} } \nonumber \\\\ 
                &= \frac{ \CV_{\die_n} }{ \sqrt{N_{\die_n}} }\,.
\end{align}
This shows that as the number of dice, $$N_{\die_n}$$, increases, the the variability decreases as $$1/\sqrt{N_{\die_n}}$$.

Figure [2](#fig:cv-die-sigma-vs-mean){: .fig-ref} can also be used to determine which dice and modifier can be used to achieve a given $$\mu$$ and $$\CV$$, by drawing a vertical line at the target $$\mu$$ and a horizontal line that intersects it near the desired $$\CV$$. Any roll close to that horizontal line can be used, with $$N_{\die_0}$$ equal to the points horizontal distance from the vertical line.

For example, when building a roll with $$\mu \simeq 15$$ and a $$\CV \simeq 0.20$$, this method gives two options, 1d10 + 10 and 3d6 + 5. A comparison of these two rolls is shown in Fig. [3](#fig:damage-roll-example){: .fig-ref} (below).
<figure id="fig:damage-roll-example-2">
    {% include_relative variability-damage-healing-rolls/fig-damage-roll-example-small.html %}
    {% include_relative variability-damage-healing-rolls/fig-damage-roll-example-large.html %}
    <figcaption>Figure 3: Shows the probability distribution for the rolls 1d10 + 10 (blue) and 3d6 + 5 (orange).</figcaption>
</figure>


# Case Study: monster damage variability

To get a sense of what values are typically used by the game, lets look at how damage roll variability looks for published monsters in D&D. Figure [4](#fig:monster-damage-cv-vs-cr){: .fig-ref} plots the average $$\CV$$ values for monster actions that deal damage as a function of monster CR (this does not include damage from spells at this time). As monster CRs increase, the average $$\CV$$ for their damaging actions decreases steadily from around 0.30 to 0.15. 

<figure id="fig:monster-damage-cv-vs-cr">
    {% include_relative variability-damage-healing-rolls/fig-monster-damage-cv-vs-cr-small.html %}
    {% include_relative variability-damage-healing-rolls/fig-monster-damage-cv-vs-cr-large.html %}
    <figcaption>Figure 4: Shows the average \(\CV\) value for published monsters as a function of their challenge rating.</figcaption>
</figure>

This trend helps to explain why low level play often feels quite deadly in D&D compared to higher level play. The higher variability of monster damage at low levels means the players are more likely to experience the "extreme" ends of the spectrum. If they're lucky, that means combat will feel significantly easier than expected, and significantly deadlier if they're unlucky.

The cause of this drop in $$\CV$$ is made clean in Fig. [5](#fig:monster-damage-sigma-vs-mean){: .fig-ref} (below), which plots this data on top of the common dice rolls from Fig. [2](#fig:cv-die-sigma-vs-mean){: .fig-ref} in the previous section. This shows that the average die size and the number of dice used both increase along with monster CR. Since most damage rolls from monsters generally include some kind of modifier, the average damage die likely starts off at a d6, increases to a d8 around CR 10, and ends close to a d10 for CRs 20 and above.

<figure id="fig:monster-damage-sigma-vs-mean">
    {% include_relative variability-damage-healing-rolls/fig-monster-damage-sigma-vs-mean-small.html %}
    {% include_relative variability-damage-healing-rolls/fig-monster-damage-sigma-vs-mean-large.html %}
    <figcaption>Figure 5: Shows the average damage mean and standard deviation values for published monsters, in comparison to the common dice rolls shown in Fig. <a href="#fig:cv-die-sigma-vs-mean" class="fig-ref">2</a> and reference lines of constant \(\CV\) (dashed lines).</figcaption>
</figure>

It's also interesting to note that while the average number of dice used must increase with monster CR, the average number of dice never goes above five. This is likely done to make calculating the damage easier, especially at higher levels.

# Conclusion

The amount of variability introduced by damage/healing rolls in D&D can be tuned by adjusting the size of the modifier, the number of dice, and the size of the dice used by the roll. If you want to lower a roll's variability, consider using a larger modifier and smaller dice. And if you want to increase a roll's variability, consider using a smaller modifier and larger dice.

As I mentioned in the introduction, there's plenty more to cover on the topic of variability in D&D. I plan to cover how attack rolls and saving throws introduce variability next, and then I would like to extend that analysis to combat and monsters by revisiting monster CR and XP calculations.