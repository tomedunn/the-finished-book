---
title: "Variability: Attacks"
excerpt: "How do we account for variability of attack rolls in D&D?"
date: 2024-01-16
last_modified_at: 2024-01-16
tags:
  - theory
  - monsters
  - classes
  - variability
  - attacks
---

<!--
todo:
 - what is the average crit / hit ratio for monster attacks?
 - how does the number of attacks a monster makes per round change as CR increases
 - what is the average damage variability from monster attacks?
-->

{% include LaTex.html %}

<div style="display:none">
\(
% generic
\newcommand{\attack}{\mathrm{a}}
\newcommand{\attacks}{\mathrm{A}}
\newcommand{\die}{\mathrm{d}}
\newcommand{\total}{\mathrm{t}}
\newcommand{\CV}{\mathit{CV}}
\newcommand{\miss}{\mathrm{m}}
\newcommand{\hit}{\mathrm{h}}
\newcommand{\crit}{\mathrm{c}}
\)
</div>

# Introduction

Attacks and saving throws form the backbone of D&D's combat system. They are the primary way through which damage is dealt and conditions are applied. And, since both rely on dice rolls to determine their outcomes, they are also two of the most significant sources of variability, i.e., randomness, in the game as well. In this post, I look at one of these elements, attacks, and show how we can characterize the variability that comes from them.

# Attack rolls

Attacks in D&D are made up of two random processes -- an attack roll and a damage roll -- and each of these contributes to the overall variability of an attack. I've already covered the [variability of damage rolls]({{ site.url }}{{ site.baseurl }}{% link _theory/variability-damage-healing-rolls.md %}), so in this section lets take a look at how attack rolls work and how we can characterize them.

Attack rolls differ from damage rolls in that they result in a discrete set of outcomes -- a miss, a hit, or a critical hit -- rather than a continuous range of values. As long as each of these outcomes results in a different value, and the results are random, each with some probability of occurring, there will naturally be some average result and some variation around that average.

To illustrate this, Fig. [1](#fig:simple-hits){: .fig-ref} (below) shows the probability of hitting $$n$$-times with an attack bonus of $$+4$$ against an armor class of $$12$$, with critical hits being counted as hits for the sake of simplicity.

<figure id="fig:simple-hits">
    {% include_relative variability-attacks/fig-simple-hits-small.html %}
    {% include_relative variability-attacks/fig-simple-hits-large.html %}
    <figcaption>Figure 1: Shows the probability of hitting \(n\)-times with an attack bonus of \(+4\) against an armor class of \(12\) after making one attack (blue) and after making five attacks (orange). For simplicity, critical hits are treated as hits.</figcaption>
</figure>

For the scenario where only one attack is made, the probability distribution is a simple binary: either the attack hits or it misses. However, for the scenario where five attacks are made, the probability is much closer to a [Gaussian distribution](https://en.wikipedia.org/wiki/Normal_distribution) (also known as a normal distribution). In fact, it exactly follows the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution).

If we assume each outcome results in a fixed amount of damage, then the average damage dealt by the attack $$(\mu_{\attack})$$ can be calculated as 
\begin{align}
    \mu_{\attack} = \rho_{\miss} \, \mu_{\miss} + \rho_{\hit} \, \mu_{\hit} + \rho_{\crit} \, \mu_{\crit} \,,
    \label{eq:attack-mean-1}
\end{align}
where $$\rho_{\miss}$$, $$\rho_{\hit}$$, and $$\rho_{\crit}$$ are the probability of the attack resulting in a miss, hit, and critical hit respectively, and $$\mu_{\miss}$$, $$\mu_{\hit}$$, and $$\mu_{\crit}$$ are the average damage dealt by a miss, hit, and critical hit respectively.

The [variance](https://en.wikipedia.org/wiki/Variance) of the damage $$(\sigma_{\attack}^2)$$, or the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) $$(\sigma_{\attack})$$ squared, can also be calculated from these,
\begin{align}
    \sigma_{\attack}^2 = \,
            &\rho_{\miss} \, \left( \mu_{\attack} - \mu_{\miss} \right)^2 + \rho_{\hit}  \, \left( \mu_{\attack} - \mu_{\hit}  \right)^2 \nonumber \\\\ 
            &+ \rho_{\crit} \, \left( \mu_{\attack} - \mu_{\crit} \right)^2 \,,
    \label{eq:attack-variance-fixed-1}
\end{align}
which, with a bit of math, can be simplified to
\begin{align}
    \sigma_{\attack}^2 = \rho_{\miss} \, \mu_{\miss}^2 + \rho_{\hit} \, \mu_{\hit}^2 + \rho_{\crit} \, \mu_{\crit}^2 - \mu_{\attack}^2 \,.
    \label{eq:attack-variance-fixed-2}
\end{align}

If we consider that for a typical attack a miss does zero damage, $$\mu_{\miss} = 0$$, and that the average damage from a critical hit can be expressed as a multiple of the average hit damage, $$\mu_{\crit} = m_{\crit} \, \mu_{\hit}$$, where $$m_{\crit}$$ is some value greater than one (and generally less than or equal to two), then the average damage given by Eqn. \eqref{eq:attack-mean-1} becomes
\begin{align}
    \mu_{\attack} = \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right) \mu_{\hit} \,,
    \label{eq:attack-mean-typical}
\end{align}
and the variance given by Eqn. \eqref{eq:attack-variance-fixed-2} becomes
\begin{align}
    \sigma_{\attack}^2 &= \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) \mu_{\hit}^2 - \mu_{\attack}^2 \nonumber \\\\ 
                       &= \left[ \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) - \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right)^2 \right]  \mu_{\hit}^2 \,.
    \label{eq:attack-variance-typical-fixed}
\end{align}

Figure [2](#fig:attack-normalized-damage-fixed-vs-hit){: .fig-ref} (below) plots $$\mu_{\attack}$$ and $$\sigma_{\attack}$$ as functions of $$\rho_{\hit}$$ for Eqns. \eqref{eq:attack-mean-typical} and \eqref{eq:attack-variance-typical-fixed} with $$\rho_{\crit} = 0.05$$ and $$m_{\crit} = 2$$. While the average damage decreases linearly as $$\rho_{\hit}$$ goes down, the standard deviation of the damage follows more of a parabolic trend, with a maximum value near the middle at $$\rho_{\hit} + \rho_{\crit} = 0.45$$, and never dropping below $$\sigma_{\attack} = 0.3$$.

<figure id="fig:attack-normalized-damage-fixed-vs-hit">
    {% include_relative variability-attacks/fig-attack-normalized-damage-fixed-vs-hit-small.html %}
    {% include_relative variability-attacks/fig-attack-normalized-damage-fixed-vs-hit-large.html %}
    <figcaption>Figure 2: Shows the average damage, \(\mu_{\attack}\) (blue), and the standard deviation of the damage, \(\sigma_{\attack}\) (orange), for an attack with \(\rho_{\crit} = 0.05\) and \(m_{\crit} = 2\), calculated from Eqns. \eqref{eq:attack-mean-typical} and \eqref{eq:attack-variance-typical-fixed} and normalized to the average damage of a hit, \(\mu_{\hit}\) .</figcaption>
</figure>

Another useful way of comparing the variance to the average is by calculating the attack roll's [coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation), $$\CV \equiv \sigma / \mu$$ (commonly referred to as sigma over mean), 
\begin{align}
    \CV_{\attack} = \left[ \frac{ \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 }{ \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit} \right)^2 } - 1 \right]^{\frac{1}{2}} \,.
    \label{eq:attack-cov-typical-fixed}
\end{align}
This normalizes the variability of the attack roll to the average, which can be useful in characterizing how likely the outcome of an attack is to be close to its statistical average damage.

To get a sense of how much variability comes attack rolls for a typical attack, Fig. [3](#fig:fixed-attack-cv-vs-hit){: .fig-ref} (below) plots $$\CV_{\attack}$$ for an attack described by Eqn. \eqref{eq:attack-cov-typical-fixed} with $$\rho_{\crit} = 0.05$$ and $$m_{\crit} = 2$$.

<figure id="fig:fixed-attack-cv-vs-hit">
    {% include_relative variability-attacks/fig-fixed-attack-cv-vs-hit-small.html %}
    {% include_relative variability-attacks/fig-fixed-attack-cv-vs-hit-large.html %}
    <figcaption>Figure 3: Shows the coefficient of variation for an attack described by Eqn. \eqref{eq:attack-cov-typical-fixed} for an attack with \(\rho_{\crit} = 0.05\) and \(m_{\crit} = 2\).</figcaption>
</figure>

For a typical chance to hit of $$65\%$$, the attack shown in Fig. [3](#fig:fixed-attack-cv-vs-hit){: .fig-ref} has a $$\CV_{\attack} \simeq 0.8$$ which is substantially higher than the coefficient of variation for a typical damage roll, which tends to fall within the range of $$0.1-0.3$$ for [published monsters]({{ site.url }}{{ site.baseurl }}{% link _theory/variability-damage-healing-rolls.md %}#fig:monster-damage-cv-vs-cr).

It's only for very high chances to hit that $$\CV_{\attack}$$ comes anywhere close to this range. And for low chances to hit, $$\CV_{\attack}$$ increases almost as $$1/\rho_{\hit}$$, due to $$\mu_{\attack}$$ trending towards zero as $$\rho_{\hit}$$ does, while $$\sigma_{\attack}$$ stays relatively high as shown previously in Fig. [2](#fig:attack-normalized-damage-fixed-vs-hit){: .fig-ref}.

Clearly, the amount of variability that comes from just the attack roll portion of an attack is substantial. How it interacts with the variability that comes from damage rolls is explored in detail in the next section.

# Attacks

When the outcomes of an attack roll have their own variability, like when a hit results in a damage roll, that variability compounds with the inherent variability of the initial roll as described in the previous section. This interaction is illustrated in Fig. [4](#fig:simple-damage){: .fig-ref} (below), which shows the probability distribution of the damage resulting from a single attack with an attack bonus of $$+4$$ against a target with an armor class of $$12$$ and deals 1d4+2 damage on a hit, as well as the distribution for five such attacks.

<figure id="fig:simple-damage">
    {% include_relative variability-attacks/fig-simple-damage-small.html %}
    {% include_relative variability-attacks/fig-simple-damage-large.html %}
    <figcaption>Figure 4: Shows the probability of dealing \(x\)-damage with an attack that has an attack bonus of \(+4\) and deals 1d4+2 damage on a hit, against a target with an armor class of \(12\) after making one attack (blue) and five attacks (orange).</figcaption>
</figure>

For the single attack there is a spread in the damage that comes from combining the damage distributions of a hit and a critical hit, as well as an extra peak at zero damage for a miss. The coefficient of variation for this single attack is $$\CV_{\attack} = 0.83$$, which is only slightly higher than $$\CV \simeq 0.75$$ given by Eqn. \eqref{eq:attack-cov-typical-fixed}, despite having $$\CV_{\hit} = 0.25$$ for the damage roll on a hit and $$\CV_{\crit} = 0.23$$ for the damage roll on a critical hit (see [Variability: Damage and Healing Rolls]({{ site.url }}{{ site.baseurl }}{% link _theory/variability-damage-healing-rolls.md %}#rolls-with-multiple-dice) for how to calculate these).

To understand how these different sources of variability are combining, Eqn. \eqref{eq:attack-variance-fixed-1}, used to calculate $$\sigma_{\attack}^2$$ in the previous section, needs to be update to include the variances for the damage rolls of each outcome. This can be done in the following way,
\begin{align}
    \sigma_{\attack}^2 = \,
            &\rho_{\miss} \left( \left( \mu_{\attack} - \mu_{\miss} \right)^2 + \sigma_{\miss}^2 \right) \nonumber \\\\ 
            &+ \rho_{\hit} \left( \left( \mu_{\attack} - \mu_{\hit}  \right)^2 + \sigma_{\hit}^2 \right) \nonumber \\\\ 
            &+ \rho_{\crit} \left( \left( \mu_{\attack} - \mu_{\crit} \right)^2 + \sigma_{\crit}^2 \right) \,,
    \label{eq:attack-variance-1}
\end{align}
where $$\sigma_{\miss}^2$$ is the variance of the damage roll for a miss, $$\sigma_{\hit}^2$$ is the variance for a hit, and $$\sigma_{\crit}^2$$ is the variance for a critical hit.

By expanding the squared terms and simplifying, Eqn. \eqref{eq:attack-variance-1} reduces to
\begin{align}
    \sigma_{\attack}^2 = \,
            &\rho_{\miss} \, \mu_{\miss}^2 + \rho_{\hit} \, \mu_{\hit}^2 + \rho_{\crit} \, \mu_{\crit}^2 - \mu_{\attack}^2 \nonumber \\\\ 
            &+ \rho_{\miss} \, \sigma_{\miss}^2 + \rho_{\hit} \, \sigma_{\hit}^2 + \rho_{\crit} \, \sigma_{\crit}^2 \,.
    \label{eq:attack-variance-2}
\end{align}

The first four terms in Eqn. \eqref{eq:attack-variance-2} are equal to the variance of an attack with fixed damage outcomes described by Eqn. \eqref{eq:attack-variance-fixed-2}, and the remaining terms are simply the variances of each outcome's damage roll weighted to the probability of that outcome occurring.

If we once again consider that for a typical attack $$\mu_{\miss} = 0$$ and $$\sigma_{\miss}^2 = 0$$, and express the average damage from a critical hit as a multiple of the average hit damage, $$\mu_{\crit} = m_{\crit} \, \mu_{\hit}$$, as well as the variance of a critical hit as a multiple of the variance of a hit, $$\sigma_{\crit} = s_{\crit} \, \sigma_{\hit}$$, where $$m_{\crit}$$ and $$s_{\crit}$$ are both constants with values greater than one, then Eqn. \eqref{eq:attack-variance-2} can be written as
\begin{align}
    \sigma_{\attack}^2 = \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) \mu_{\hit}^2 - \mu_{\attack}^2 + \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \sigma_{\hit}^2 \,,
    \label{eq:attack-variance-typical}
\end{align}
where $$\mu_{\attack}^2$$ is the average damage of the attack given by Eqn. \eqref{eq:attack-mean-typical} in the previous section.

As an example, for the attack shown previously in Fig. [4](#fig:simple-damage){: .fig-ref} the damage roll for a hit is 1d4 + 2 ($$\mu_{\hit} = 4.5$$ and $$\sigma_{\hit} = 1.12$$) and the damage roll for a critical hit is 2d4 + 2 ($$\mu_{\hit} = 7.0$$ and $$\sigma_{\hit} = 1.12\,\sqrt{2}$$), which translates to $$m_{\crit} = 1.56$$ and $$s_{\crit} = \sqrt{2}$$.

Figure [5](#fig:attack-normalized-damage-vs-hit){: .fig-ref} (below) plots $$\mu_{\attack}$$ from Eqn. \eqref{eq:attack-mean-typical} and $$\sigma_{\attack}$$ from Eqn. \eqref{eq:attack-variance-typical}, along with its contributions from the attack roll and damage rolls, for and attack with $$\rho_{\crit} = 0.05$$, $$m_{\crit} = 2$$, $$s_{\crit}^2 = 2$$, and $$\sigma_{\hit}/\mu_{\hit} = 0.3$$.

<figure id="fig:attack-normalized-damage-vs-hit">
    {% include_relative variability-attacks/fig-attack-normalized-damage-vs-hit-small.html %}
    {% include_relative variability-attacks/fig-attack-normalized-damage-vs-hit-large.html %}
    <figcaption>Figure 5: Shows the average damage \(\mu_{\attack}\) given by Eqn. \eqref{eq:attack-mean-typical} (blue), as well as the standard deviation of the damage \(\sigma_{\attack}\) given by Eqn. \eqref{eq:attack-variance-typical} (red), and its contributions from the attack roll (orange) and the damage rolls of each outcome (green). All damage values shown are normalized to the average damage of a hit, \(\mu_{\hit}\), and the attack shown has \(\rho_{\crit} = 0.05\), \(m_{\crit} = 2\), \(s_{\crit}^2 = 2\), and \(\sigma_{\hit}/\mu_{\hit} = 0.3\).</figcaption>
</figure>

At low chances to hit the variability of the damage rolls contribute almost nothing to $$\sigma_{\attack}$$. This increase as $$\rho_{\hit}$$ does, but even at $$\rho_{\hit} = 0.9$$ the variability coming from the attack roll and the average damage is still the more dominant term.

Taking the ratio of Eqns. \eqref{eq:attack-variance-typical} and \eqref{eq:attack-mean-typical}, the coefficient of variation, $$\CV \equiv \sigma / \mu$$, is
\begin{align}
    \CV_{\attack} = \left[ \frac{ \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \CV_{\hit}^{\,2} + \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 }{ \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit} \right)^2 } - 1 \right]^{\frac{1}{2}} \,,
    \label{eq:attack-cov-typical}
\end{align}
where $$\CV_{\hit} = \sigma_{\hit}/\mu_{\hit}$$ is the coefficient of variation for the damage rolled on a hit.

For [published monsters]({{ site.url }}{{ site.baseurl }}{% link _theory/variability-damage-healing-rolls.md %}#fig:monster-damage-cv-vs-cr), 
$$\CV_{\hit}$$ typically falls in the range $$0.1-0.3$$. Using this, along with $$\rho_{\crit} = 0.05$$, $$m_{\crit} = 2$$, and $$s_{\crit}^2 = 2$$, Fig. [6](#fig:attack-cv-vs-hit){: .fig-ref} (below) shows how the $$\CV_{\attack}$$ described by Eqn. \eqref{eq:attack-cov-typical} depends on the probability of an attack hitting its target, $$\rho_{\hit}$$.

<figure id="fig:attack-cv-vs-hit">
    {% include_relative variability-attacks/fig-attack-cv-vs-hit-small.html %}
    {% include_relative variability-attacks/fig-attack-cv-vs-hit-large.html %}
    <figcaption>Figure 6: Shows the coefficient of variation described by Eqn. \eqref{eq:attack-cov-typical} for an attack with \(\rho_{\crit} = 0.05\), \(m_{\crit} = 2\), and \(s_{\crit}^2 = 2\).</figcaption>
</figure>

Clearly, damage roll variability has only a minor influence on the overall variability of an attack. This may seem somewhat counter intuitive but it's worth keeping in mind that much of the variability that comes from the attack roll stems from the average damage of a miss being zero and the probability of a critical hit being low.

# Multiple attacks

When dealing with multiple attacks, the average and variance of the total damage can be calculated from the averages and variances of the individual attacks. For the average total damage,
\begin{align}
    \mu_{\total} &= \sum_{\attack \in \attacks} N_{\attack} \, \mu_{\attack} \,,
    \label{eq:multiple-actions-mean}
\end{align}
and for the variance of the total damage,
\begin{align}
    \sigma_{\total}^2 &= \sum_{\attack \in \attacks} N_{\attack} \, \sigma_{\attack}^2 \,.
    \label{eq:multiple-attacks-var}
\end{align}
Here, $$\attacks = \{\attack_1, \attack_2, ... , \attack_N \}$$ is the set of all attacks in the evaluation, $$\mu_{\attack}$$ is an attack's average damage, $$\sigma_{\attack}^2$$ is its variance, and $$N_{\attack}$$ is the number of times the attack is made.

**Note.** The results of Eqn. \eqref{eq:multiple-attacks-var} relies on each attack being completely independent of one another, i.e., they don't share any dice rolls. This is always the case for attacks, which use separate attack rolls and damage rolls for each target, but it's not always the case for saving throws, which sometimes use a single damage roll across multiple targets.
{: .notice--warning}

## Identical attacks

If all of the attacks are the same, Eqns. \eqref{eq:multiple-actions-mean} and \eqref{eq:multiple-attacks-var} simplify to
\begin{align}
    \mu_{\total} &= N_{\attack} \, \mu_{\attack} \,; \\\\ 
    \sigma_{\total}^2 &= N_{\attack} \, \sigma_{\attack}^2 \,,
\end{align}
and the resulting coefficient of variation, $$\CV \equiv \sigma / \mu$$, for the attack is
\begin{align}
    \CV_{\total} &= \frac{ \CV_{\attack} }{ N_{\attack}^{1/2} }\,.
    \label{eq:ma-attack-cov}
\end{align}
As $$N_{\attack}$$ increases, $$\CV_{\total}$$ decreases as $$1/\sqrt{N_{\attack}}$$. Thus, that after four attacks $$\CV_{\total}$$ is half its original value, and after sixteen attacks its a quarter of it. This illustrates how **a character's damage will will tend towards the average over time**.

Solving Eqn. \eqref{eq:ma-attack-cov} for $$N_{\attack}$$,
\begin{align}
    N_{\attack} = \frac{ \CV_{\attack}^{\,2} }{ \CV_{\total}^{\,2} }\,,
\end{align}
tells us the number of attacks needed for a given attack hit a certain $$\CV_{\total}$$ target, which can be useful for assessing how often an ability needs to be used to hit a desired level of variability.


## Fixed damage

Another useful way we can look at how the number of attacks impacts $$\CV_{\total}$$ is to allow $$N_{\attack}$$ to vary while the total average damage $$\mu_{\total}$$ remains fixed. For example, when designing a monster we may need to keep the total damage per round within a certain range to hit a specific CR target.

Consider the case where we have three attacks, $$\attack_1$$, $$\attack_2$$, and $$\attack_3$$, that have identical chances to miss, hit, and critically hit, and have damage rolls $$d_1$$, $$d_2$$, and $$d_3 = d_1 + d_2$$. For simplicity, lets also assume no damage is dealt on a miss, $$\mu_{\miss} = 0$$, and that each damage roll has the same ratio between their average critical hit damage and average hit damage, $$m_{\crit} \equiv \mu_{\crit}/\mu_{\hit}$$ (this will always be true when no damage modifiers are used).

We know from the [variability of damage rolls]({{ site.url }}{{ site.baseurl }}{% link _theory/variability-damage-healing-rolls.md %}) 
that $$\mu_{d_3} = \mu_{d_1} + \mu_{d_2}$$ and that $$\sigma_{d_3}^2 = \sigma_{d_1}^2 + \sigma_{d_2}^2$$, but what about the average damage and variance from attacks that use these damage rolls?

The average damage for attacks 1 and 2 can be calculated using Eqn. \eqref{eq:attack-mean-typical},
\begin{align}
    \mu_{\attack_{1}} &= \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right) \, \mu_{\hit_{1}} \,, \label{eq:cd-attack-mean-1} \\\\ 
    \mu_{\attack_{2}} &= \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right) \, \mu_{\hit_{2}} \,, \label{eq:cd-attack-mean-2}
\end{align}
and their variances can be calculated using Eqn. \eqref{eq:attack-variance-typical},
\begin{align}
    \sigma_{\attack_{1}}^2 &= \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) \mu_{\hit_{1}}^2 - \mu_{\attack_{1}}^2 + \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \sigma_{\hit_{1}}^2 \,;
    \label{eq:cd-attack-variance-1} \\\\ 
    \sigma_{\attack_{2}}^2 &= \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) \mu_{\hit_{2}}^2 - \mu_{\attack_{2}}^2 + \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \sigma_{\hit_{2}}^2 \,.
    \label{eq:cd-attack-variance-2}
\end{align}

The average damage of the third attack can also be calculated using Eqn. \eqref{eq:attack-mean-typical},
\begin{align}
    \mu_{\attack_{3}} &= \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right) \, \mu_{\hit_{3}} \nonumber \\\\ 
                      &= \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right) \, \left( \mu_{\hit_{2}} + \mu_{\hit_{2}} \right) \nonumber \\\\ 
                      &= \mu_{\attack_{1}} + \mu_{\attack_{2}} \,, \label{eq:cd-attack-mean-3}
\end{align}
and gives the same average damage as attacks 1 and 2 combined.

The variance of the third attack can be calculated from Eqn. \eqref{eq:attack-variance-typical} as well,
\begin{align}
    \sigma_{\attack_{3}}^2 =&\, \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) \mu_{\hit_{3}}^2 - \mu_{\attack_{3}}^2 + \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \sigma_{\hit_{3}}^2 \nonumber \\\\ 
                           =&\, \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) \left( \mu_{\hit_{1}} + \mu_{\hit_{2}} \right)^2 - \left( \mu_{\attack_{1}} + \attack_{\hit_{2}} \right)^2 \nonumber \\\\ 
                            &+ \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \left( \sigma_{\hit_{1}}^2 + \sigma_{\hit_{2}}^2 \right)\,.
    \label{eq:cd-attack-variance-3}
\end{align}
By expanding out the squared terms and simplifying, the variance for the third attack can be rewritten as
\begin{align}
    \sigma_{\attack_{3}}^2 &= \sigma_{\attack_{1}}^2 + \sigma_{\attack_{2}}^2 + \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) 2 \mu_{\hit_{1}}\,\mu_{\hit_{2}} - 2\,\mu_{\attack_{1}}\,\mu_{\attack_{2}}\,.
\end{align}
Finally, we can substitute Eqns. \eqref{eq:cd-attack-mean-1} and \eqref{eq:cd-attack-mean-2} in for $$\mu_{\attack_{1}}$$ and $$\mu_{\attack_{2}}$$ respectively, yielding
\begin{align}
    \sigma_{\attack_{3}}^2 =&\, \sigma_{\attack_{1}}^2 + \sigma_{\attack_{2}}^2 + 2 \mu_{\hit_{1}}\,\mu_{\hit_{2}} \left( \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) - \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right)^2 \right)\,.
    \label{eq:cd-attack-variance-3-final}
\end{align}
Since $$m_{\crit} > 1$$, we know that $$\rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 > \rho_{\hit} + \rho_{\crit} \, m_{\crit}\,.$$ This means that as long as $$\rho_{\hit} + \rho_{\crit} \, m_{\crit} < 1$$ (this is virtually always the case in D&D) then the third term in Eqn. \eqref{eq:cd-attack-variance-3-final} is strictly positive and $$\sigma_{\attack_{3}}^2 > \sigma_{\attack_{1}}^2 + \sigma_{\attack_{2}}^2\,.$$ Thus, splitting a fixed pool of damage up across two identical attacks will virtually always result in a lower variance than applying the entire pool to a single attack.

This principle can be applied recursively as well, so long as the damage pools of a resulting attack after splitting can be further split in two. Therefore, a more general statement would be that **the variance from a pool of damage divided up across multiple identical attacks gets smaller and smaller as the number of attacks increases**.

For a damage pool consisting of $$N$$ dice, $$\mathrm{D} = \left\{\die_{1}, \die_{2}, \dots, \die_{N}\right\}$$, the lowest variance will come when the damage pool can no longer be split up, i.e., one die per attack. The minimum total variance can therefore be calculated using Eqn. \eqref{eq:attack-variance-typical},
\begin{align}
    \sigma_{\mathrm{min}}^2 = &\, \left( \left( \rho_{\hit} + \rho_{\crit} \, m_{\crit}^2 \right) - \left( \rho_{\hit}  + \rho_{\crit} \, m_{\crit} \right)^2 \right) \sum_{\die \in \mathrm{D}} \mu_{\die}^2 \nonumber \\\\ 
    &+ \left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \sigma_{\mathrm{D}}^2 \,,
    \label{eq:cd-attack-variance-min}
\end{align}
where $$\sigma_{\mathrm{D}}^2$$ is the total variance from the entire damage pool.

Note that the contribution of the damage pool to the total variance, $$\left( \rho_{\hit} + \rho_{\crit} \, s_{\crit}^2 \right) \sigma_{\mathrm{D}}^2$$, is the same as it would be with just a single attack. The term that gets smaller as the number of attacks increases is therefore that of the attack roll. This makes intuitive sense, since the number of attack rolls is increasing while the total dice rolled when determining the damage remains unchanged.

An example of how the $$\CV$$ decreases as the number of attacks increases is shown in Fig. [7](#fig:cd-cv-example){: .fig-ref} (below) for a damage pool consisting of 8d6.

<figure id="fig:cd-cv-example">
    {% include_relative variability-attacks/fig-cd-cv-example-small.html %}
    {% include_relative variability-attacks/fig-cd-cv-example-large.html %}
    <figcaption>Figure 7: Shows the coefficient of variation for a damage pool of 8d6 divided up evenly across multiple attacks (blue), each of which has \(\rho_{\hit} = 0.60\) and \(\rho_{\crit} = 0.05\), along with a reference line for minimum \(\CV\) calculated using Eqn. \eqref{eq:cd-attack-variance-min} (dashed).</figcaption>
</figure>

# Conclusion

The variability that comes from attack rolls is dominated by the attack roll. This can be improved by increasing the attack's chance to hit, but even at extremely high chances to hit the variability of the attack roll dominates over that of the damage rolls. Therefore, the only practical way of reducing the overall variability from attacks is to increase the number of attacks, either over time or by splitting a given damage target across multiple attacks.

Since the number of attacks made, both by player characters and monsters, tends to increase as their levels and challenge ratings increase, this means that the damage from attacks in lower tiers of play is inherently more variable than it is in higher tiers of play. This is yet another factor that contributes to combat feeling deadlier and more volatile in lower tiers of play than in higher ones.