---
title: "Variability: Saves"
excerpt: "How do we account for variability of saving throws in D&D?"
permalink: /:collection/:name/
date: 2024-02-17
last_modified_at: 2024-02-17
tags:
  - theory
  - monsters
  - classes
  - variability
  - saving throws
---

{% include LaTex.html %}

<div style="display:none">
\(
% generic
\newcommand{\action}{\mathrm{a}}
\newcommand{\actions}{\mathrm{A}}
\newcommand{\die}{\mathrm{d}}
\newcommand{\total}{\mathrm{t}}
\newcommand{\CV}{\mathit{CV}}
\newcommand{\roll}{\mathrm{r}}
\newcommand{\state}{\mathit{s}}
\newcommand{\states}{\mathit{S}}
\newcommand{\dicepool}{\mathrm{dp}}
\newcommand{\miss}{\mathrm{m}}
\newcommand{\hit}{\mathrm{h}}
\newcommand{\crit}{\mathrm{c}}
\newcommand{\fail}{\mathrm{f}}
\newcommand{\save}{\mathrm{s}}
\)
</div>



# Introduction

Attacks and saves form the backbone of D&D's combat system. They are the primary way through which damage is dealt and conditions are applied. And, since both rely on dice rolls to determine their outcomes, they are also two of the most significant sources of variability, i.e., randomness, in the game as well.

In [Variability: Attacks]({{ site.data.page-links.variability-attacks.path }}) I looked at the variability that comes from attacks, what contributes to it and how it can be characterized. In this post, I aim to complete this set by giving saves the same treatment.

# Saving throws

Like with attacks, resolving a save generally involves two random processes -- the saving throw and a possible damage roll -- and both contribute to the total variability of the outcome in different ways. I've already covered the [variability of damage rolls]({{ site.data.page-links.variability-damage-healing-rolls.path }}), so in this section I'll focus on the variability that comes from the saving throw, and in the section that follows I'll look at how the two interact with one another.

While an attack roll can result in three possible states -- a miss, hit, and a critical hit -- saving throws only result in two: a success or a failure. A saving throw is a success when the result is equal to or greater than the save's difficulty class (DC) and failure otherwise. 

If we consider, for now, that each of these states results in a fixed amount of damage, then the average damage that results from the saving throw $$(\mu_{\action})$$ can be expressed as
\begin{align}
    \mu_{\action} &= \rho_{\fail} \, \mu_{\fail} + \rho_{\save} \, \mu_{\save}\,.
    \label{eq:save-mean}
\end{align}
where $$\mu_{\fail}$$ is the damage dealt on a failed save, $$\rho_{\fail}$$ is the probability of the target failing the saving throw, $$\mu_{\save}$$ is the damage dealt on a successful save, and $$\rho_{\save} = 1 - \rho_{\fail}$$ is the probability that the target succeeds on the saving throw.

The [variance](https://en.wikipedia.org/wiki/Variance) of the damage that results from the saving throw $$(\sigma_{\action}^2)$$, i.e., the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) $$(\sigma_{\action})$$ squared, can be used to characterize how likely an individual result is to be close to the average, and it can also be calculated in terms of these values,
\begin{align}
    \sigma_{\action}^2 = 
            \rho_{\fail} \, \left( \mu_{\action} - \mu_{\fail} \right)^2 + \rho_{\save} \, \left( \mu_{\action} - \mu_{\save} \right)^2\,,
\end{align}
which can be simplified by substituting the results of Eqn. \eqref{eq:save-mean} in for $$\mu_{\action}$$,
\begin{align}
    \sigma_{\action}^2 = \rho_{\fail} \, \rho_{\save} \left( \mu_{\fail} - \mu_{\save} \right)^2 \,.
    \label{eq:save-variance-fixed}
\end{align}

Since the damage dealt by a successful save is typically some fraction of the damage dealt by a failed one, $$\mu_{\save} = m_{\save} \, \mu_{\fail}$$ where $$m_{\save}$$ is some number between zero and one, these can also be written as
\begin{align}
    \mu_{\action} 
        &= \left( \rho_{\fail} + \rho_{\save} \, m_{\save} \right) \, \mu_{\fail} \,,
    \label{eq:typical-save-mean}
\end{align}
and
\begin{align}
    \sigma_{\action}^2 
        &= \rho_{\fail} \, \rho_{\save} \,\left( 1 - m_{\save} \right)^2 \, \mu_{\fail}^2 \,.
    \label{eq:typical-save-variance-fixed}
\end{align}

Note that while $$\mu_{\action}$$ gets larger as $$m_{\save}$$ increases, $$\sigma_{\action}$$ gets smaller and eventually goes to zero when $$m_{\save} = 1$$, i.e., when the damage on a successful saving throw equals the damage on a failed one. This makes the damage dealt on a successful saving throw a powerful knob in controlling the overall variability of the damage from a save.

Figure [1](#fig:fixed-save-normalized-damage){: .fig-ref} (below) plots $$\mu_{\action}$$ and $$\sigma_{\action}$$ for saves with $$m_{\save} = 0.5$$ and for $$m_{\save} = 0$$. For both of these saves, the standard deviation follows a parabolic trajectory, with a maximum at $$\rho_{\fail} = 0.5$$, and the average damage increases linearly with $$\rho_{\fail}$$. In comparison, when $$m_{\save} = 0.5$$, the save's $$\sigma_{\action}$$ is half as large as it is when $$m_{\save} = 0$$, and while $$\mu_{\action}$$ also increases linearly with $$\rho_{\fail}$$, it does so at half the rate and never drops below $$\mu_{\fail} / 2$$.

<figure id="fig:fixed-save-normalized-damage">
    {% include_relative fig-fixed-save-normalized-damage-small.html %}
    {% include_relative fig-fixed-save-normalized-damage-large.html %}
    <figcaption>Figure 1: Shows average damage and the standard deviation of the damage for a save that deals no damage on a successful saving throw (blue) and one that deals half damage on a successful saving throw (orange). Damage values are all normalized to the damage dealt on a failed saving throw.</figcaption>
</figure>

It's also worth noting that for a typical chance of a target failing their saving throw of $$\rho_{\fail} = 0.65$$, the average damage for $$m_{\save} = 0.5$$ is  $$\mu_{\action} = 0.82 \, \mu_{\fail}$$, which is roughly $$25\%$$ higher than it is for $$m_{\save} = 0$$, which has an average damage of $$\mu_{\action} = 0.65 \, \mu_{\fail}$$. This explains why the rules for [creating a spell](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#SpellDamage) from chapter 9 of the _Dungeon Master's Guide_ recommend increasing the damage for spells with $$m_{\save} = 0$$ by $$25\%$$ over the values listed in that section.

The scale of the variance can be put into a more useful context by dividing it by the average to calculate the save's [coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation), $$\CV \equiv \sigma / \mu$$ (commonly referred to as sigma over mean), 
\begin{align}
    \CV_{\action} 
        &= \frac{ \left( 1 - m_{\save} \right) \, \sqrt{ \rho_{\fail} \, \rho_{\save} } }{ \rho_{\fail} + \rho_{\save} \, m_{\save} } \,.
    \label{eq:typical-save-cov-fixed}
\end{align}

Figure [2](#fig:fixed-save-cv){: .fig-ref} (below) shows the results of Eqn. \eqref{eq:typical-save-cov-fixed} for saving throws where $$m_{\save} = 0$$ and for saving throws where $$m_{\save} = 0.5$$.

<figure id="fig:fixed-save-cv">
    {% include_relative fig-fixed-save-cv-small.html %}
    {% include_relative fig-fixed-save-cv-large.html %}
    <figcaption>Figure 2: Shows the coefficient of variation, \(\CV \equiv \sigma / \mu\), for a save that deals no damage on a successful saving throw (blue) and for one that deals half damage on a successful saving throw (orange).</figcaption>
</figure>

For saves with $$m_{\save} = 0$$, the results shown in Fig. [2](#fig:fixed-save-cv){: .fig-ref} closely match those shown previously for [attack rolls]({{ site.data.page-links.variability-attacks.path }}/#fig:fixed-attack-cv-vs-hit), getting asymptotically large as $$\rho_{\fail}$$ goes to zero. This makes sense, since a save with $$m_{\save} = 0$$ is equivalent to an attack that does the same damage on a critical hit as it does on a hit.

However, for saves with $$m_{\save} = 0.5$$ the results are entirely different. On top of $$\CV_{\action}$$ being substantially smaller at typical values of $$\rho_{\fail}$$ (nearly $$60\%$$ smaller when $$\rho_{\fail} = 0.65$$), it also never exceeds $$\CV_{\action} = 0.35$$, even as $$\rho_{\fail}$$ tends towards zero. This is because the average damage $$\mu_{\action}$$ never approaches zero, like it does when $$m_{\save} = 0.$$ 

To put this lower innate variability in perspective, a save with $$m_{\save} = 0$$ would need to have $$\rho_{\fail} \ge 0.95$$ in order to have a lower $$\CV_{\action}$$ than a save with $$m_{\save} = 0.5$$ that has $$\rho_{\fail} = 0.65$$.

# Saves

To account for the variability associated with damage rolls used in saves, Eqn. \eqref{eq:save-variance-fixed} from the previous section can be updated as follow,
\begin{align}
    \sigma_{\action}^2 = 
            &\rho_{\fail} \, \left( \left( \mu_{\action} - \mu_{\fail} \right)^2 + \sigma_{\fail}^2 \right) \nonumber \\\\ 
            &+ \rho_{\save} \, \left( \left( \mu_{\action} - \mu_{\save} \right)^2 + \sigma_{\save}^2 \right) \,.
\end{align}
Here, $$\mu_{\fail}$$ and $$\mu_{\save}$$ now represent the average damage dealt on a failed saving throw and a successful one respectively, $$\sigma_{\fail}^2$$ is the variance of the damage dealt on a failed saving throw, and $$\sigma_{\save}^2$$ is the variance of the damage dealt on a successful saving throw.

This can be simplified by substituting the results of Eqn. \eqref{eq:save-mean} in for $$\mu_{\action}$$,
\begin{align}
    \sigma_{\action}^2 = \rho_{\fail} \, \rho_{\save} \left( \mu_{\fail} - \mu_{\save} \right)^2 + \rho_{\fail} \, \sigma_{\fail}^2 + \rho_{\save} \, \sigma_{\save}^2 \,.
    \label{eq:save-variance}
\end{align}
The first term is just the variance described by Eqn. \eqref{eq:save-variance-fixed} when using fixed outcomes, and the remaining terms are the sum of the variances of each outcome's damage roll weighted to the probability of those outcomes occurring.

A successful save typically does some fraction of the damage dealt by a failed save, $$\mu_{\save} = m_{\save} \, \mu_{\fail}$$ where $$m_{\save}$$ is some value between zero and one. And, since this is generally done by multiplying the results of the damage roll for a failed saving throw by $$m_{\save}$$, in can be shown that the standard deviation is reduced by the same amount, $$\sigma_{\save} = m_{\save}\,\sigma_{\fail}$$. Using this, Eqn. \eqref{eq:save-variance} can also be written as
\begin{align}
    \sigma_{\action}^2 
        &= \rho_{\fail} \, \rho_{\save} \left( 1 - m_{\save} \right)^2 \mu_{\fail}^2 + \left( \rho_{\fail} + \rho_{\save} \, m_{\save}^2 \right) \sigma_{\fail}^2 \,.
        %&= \left( \rho_{\fail} + \rho_{\save} s_{\save}^2 \right)\, \sigma_{\fail}^2 + \rho_{\fail} \, \rho_{\save} \left( 1 - m_{\save} \right)^2 \, \mu_{\fail}^2 \,.
    \label{eq:typical-save-variance}
\end{align}

**Note.** The above formulation ignores the fact that fractional damage in D&D is always rounded down. This changes the results slightly, but also makes a general formulation much more complicated without any practical benefits towards the purpose of this analysis. For those who wish to test their skills, including this rounding for saves that deal half damage on a successful save results in $$\mu_{\save} = \frac{1}{2} \left(\mu_{\fail} - 1/2 \right)$$ and $$\sigma_{\save}^2 = \frac{1}{4} \left( \sigma_{\fail}^2 + 1/4 \right)$$.
{: .notice--warning}

The two most common types of saves in D&D are ones where no damage is dealt on a successful saving throw, $$m_{\save} = 0$$, and where a successful saving throw deals half the damage dealt on a failed saving throw, $$m_{\save} = 0.5$$. For the later case, Fig. [3](#fig:save-normalized-damage){: .fig-ref} (below) shows how the terms in Eqn. \eqref{eq:typical-save-variance} compare to one another and to the average given by Eqn. \eqref{eq:typical-save-mean} for a save with $$\CV_{\fail} = 0.3$$.

<figure id="fig:save-normalized-damage">
    {% include_relative fig-save-normalized-damage-small.html %}
    {% include_relative fig-save-normalized-damage-large.html %}
    <figcaption>Figure 3: Shows the average damage given by Eqn. \eqref{eq:typical-save-mean} (blue) for a save with \(m_{\save} = 0.5\) and \(\CV_{\fail} = 0.3\), as well as the standard deviation of the damage \(\sigma_{\action}\) given by Eqn. \eqref{eq:typical-save-variance} (red), and its contributions from the saving throw (orange) and damage rolls (green). All damage values shown are normalized to the average damage of a failed save, \(\mu_{\fail}\).</figcaption>
</figure>

At very low and very high values of $$\rho_{\fail}$$, the variability of the damage rolls dominate the total variability, but for more typical values of $$\rho_{\save}$$, e.g., $$\rho_{\save} = 0.65$$, the damage rolls and the saving throw contribute similar amounts to the total variability. This is in stark contrast to what was observed for attacks previously, which showed the variability of the attack roll playing a dominant role over the damage rolls for all but the most extreme cases.

As mentioned in the previous section, when $$m_{\save} = 0$$ the results are identical to those of an attack that does the same damage on a critical hit as it does on a hit. And just like we saw for [attacks previously]({{ site.data.page-links.variability-attacks.path}}/#fig:attack-cv-vs-hit), the total variability for saves with $$m_{\save} = 0$$ is dominated by the variability of the saving throw, with the variability of the damage rolls contributing very little.

The coefficient of variation, $$\CV \equiv \sigma / \mu$$, can be calculated by taking the ratio of Eqn. \eqref{eq:typical-save-variance} and Eqn. \eqref{eq:typical-save-mean},
\begin{align}
    \CV_{\action}^{\,2} 
        %&= \frac{ \left( \rho_{\fail} + \rho_{\save} s_{\save}^2 \right) \CV_{\fail}^{\,2} + \rho_{\fail} \, \rho_{\save} \left( 1 - m_{\save} \right)^2 }
        &= \frac{ \left( \rho_{\fail} + \rho_{\save} \, m_{\save}^2 \right) \CV_{\fail}^{\,2} + \rho_{\fail} \, \rho_{\save} \left( 1 - m_{\save} \right)^2 }
            { \left( \rho_{\fail} + \rho_{\save} \, m_{\save} \right)^2 }\,,
    \label{eq:typical-save-cov}
\end{align}
where $$\CV_{\fail} = \sigma_{\fail}/\mu_{\fail}$$ is the coefficient of variation of the damage rolled on a failed saving throw.

Figure [4](#fig:save-cv){: .fig-ref} (below) shows the results of Eqn. \eqref{eq:typical-save-cov} as a function of $$\rho_{\fail}$$ for a range of $$\CV_{\fail}$$ values that cover the typical range seen for damage rolls from [published monsters]({{ site.data.page-links.variability-damage-healing-rolls.path }}#fig:monster-damage-cv-vs-cr).

<figure id="fig:save-cv">
    {% include_relative fig-save-cv-small.html %}
    {% include_relative fig-save-cv-large.html %}
    <figcaption>Figure 4: Shows the coefficient of variation described by Eqn. \eqref{eq:typical-save-cov} for a saving throw with \(m_{\save} = 0.5\).</figcaption>
</figure>

As expected from the results shown previously in Fig. [3](#fig:save-normalized-damage){: .fig-ref}, when $$m_{\save} = 0.5$$ the variability of the damage rolls contributes significantly to the overall variability across the full range of $$\rho_{\fail}$$. This means saves that deal half damage on a successful saving throw are more sensitive to the variability of their damage rolls. However, even for large levels of damage roll variability, the overall $$\CV$$ for saves with $$m_{\save} = 0.5$$ remain significantly smaller than it is for saves with $$m_{\save} = 0$$ that deal a fixed amount of damage.

<!--
Lastly, since $$\CV_{\fail}$$ tends to decrease as monster CR increases, this means the overall damage dealt by a monster from a single save is more likely to be close to the average as monster CR increases when $$m_{\save} = 0.5$$.
-->

# Multiple targets

While attacks are limited to only a single target, saves can sometimes have multiple targets for a single use. When they do, each target makes its own saving throw against the save's DC but only a single damage roll is made.

The fact that a single damage roll is used for all targets limits the number of possible results the total damage can take. As a result, the variability for these saves is higher than it would be if a separate damage roll was used for each target instead.

An example of this is shown in Fig. [5](#fig:multi-target-example){: .fig-ref} (below) for the _[shatter](https://www.dndbeyond.com/spells/shatter)_ spell when cast against two targets. When the same damage roll is used for both targets the probability distribution of the total damage is wider and it takes on a jagged appearance. While the average damage is unchanged, this results in a larger standard deviation for the total damage.

<figure id="fig:multi-target-example">
    {% include_relative fig-multi-target-example-small.html %}
    {% include_relative fig-multi-target-example-large.html %}
    <figcaption>Figure 5: Shows the distribution of damage for a 2nd level <em>shatter</em> spell cast against two target when only a single damage roll is used (blue), as well as when a separate damage roll is used for each target (orange). Both targets have a \(65\%\) chance of failing their saving throw.</figcaption>
</figure>

We can make sense of these results by considering how the damage dealt to each target is connected. When only one damage roll is made, if the first target fails their saving throw and takes 12 damage then the second target can either take 12 damage on failed saving throw or 6 damage on successful one. In comparison, when each target gets their own damage roll, if the first target fails their saving throw and takes 12 damage, the second target can still take anywhere between 3 and 24 damage on a failed saving throw or between 1 and 12 on a successful one.

For a group of $$N$$ targets, each with their own $$\rho_{\fail}$$ and $$\rho_{\save}$$ values, the average damage is still calculated by adding up the average damage for each target as follows,
\begin{align}
    \mu_{\total} &= \sum_{i = 1}^{N} \mu_{i} \,.
    \label{eq:multiple-targets-mean}
\end{align}
When calculating the variance under these conditions though, things are not as straight forward. 

Previously, when analyzing damage rolls and attacks, the total variance from $$N$$ sources was simply equal to the sum of their individual variances,
\begin{align}
    \sigma_{\total}^2 = \sum_{i = 1}^{N} \sigma_{i}^2 \,.
\end{align}
This formulation is correct, but only when the results for each source are independent of one another. This is true for attacks, since each attack only affects a single target and has its own attack roll and damage roll.

A more general formula for the total variance from $$N$$ random processes, that doesn't rely on each process being independent of one another, is
\begin{align}
    \sigma_{\total}^2 &= \sum_{i=1}^{N} \sum_{j=1}^{N} \sigma_{ij}^2  \,,
    %\sigma_{\total}^2 &= \sum_{i, j}^{N} \sigma_{ij}^2  \,,
    \label{eq:total-covariance-general}
\end{align}
where $$\sigma_{ij}^2$$ is the [covariance](https://en.wikipedia.org/wiki/Covariance) between random processes $$i$$ and $$j$$,
\begin{align}
    \sigma_{ij}^2 \equiv \sum_{d_{i}} \sum_{d_{j}} \rho\left( d_{i}, d_{j} \right) \left( d_{i} - \mu_{\action_{i}} \right) \left( d_{j} - \mu_{\action_{j}} \right)  \,.
    \label{eq:covariance-definition}
\end{align}
Here, $$\rho\left( d_{i}, d_{j} \right)$$ is the probability of process $$i$$ resulting in a value of $$d_{i}$$ and process $$j$$ resulting in a value of $$d_{j},$$ $$\mu_{\action_{i}}$$ is the average outcome of process $$i$$, and $$\mu_{\action_{j}}$$ is the average outcome of process $$j$$.

Since the variance of a random process is defined as its covariance with itself, $$\sigma_{i}^2 \equiv \sigma_{ii}^2$$, Eqn. \eqref{eq:total-covariance-general} can also be written as,
\begin{align}
    \sigma_{\total}^2 &= \sum_{i = j} \sigma_{i}^2 + \sum_{i \neq j} \sigma_{ij}^2  \,,
    \label{eq:total-covariance-general-2}
\end{align}
where the first summation is over all combinations of $$i$$ and $$j$$ where $$i = j$$, and the second summation is over all combinations where $$i \neq j$$. If we think of Eqn. \eqref{eq:total-covariance-general} as adding up all of the terms in a matrix, the the first summation here covers all of the terms on the diagonal of that matrix and the second covers all the off-diagonal terms.

\begin{bmatrix}
    \sigma_{1}^{2}   &\sigma_{12}^{2}  &\ldots      &\sigma_{1N}^{2}    \\\\ 
    \sigma_{21}^{2}  & \sigma_{2}^{2}  &\ldots      &\sigma_{2N}^{2}    \\\\ 
    \vdots           &\vdots           &\ddots      &\vdots             \\\\ 
    \sigma_{N1}^{2}  &\sigma_{N2}^{2}  &\ldots      &\sigma_{N}^{2} 
\end{bmatrix}

When two random process are completely independent of one another, the covariance between them is equal to zero. So, for any collection of independent random processes, $$\sigma_{ij} = 0$$ for all combinations where $$i \neq j$$, which causes the second term Eqn. \eqref{eq:total-covariance-general-2} to vanish, reducing it to Eqn. \eqref{eq:total-covariance-general} as expected.

For the sake of space, I won't subject you to the full derivation, which is quite long, but it can be shown that for a save that damages multiple targets via a single damage roll, the covariance of the damage between any two targets is
\begin{align}
    \sigma_{ij}^{2} &= 
        \left( \rho_{\fail_{i}} \, \sigma_{\fail} + \rho_{\save_{i}} \, \sigma_{\save} \right)
        \left( \rho_{\fail_{j}} \, \sigma_{\fail} + \rho_{\save_{j}} \, \sigma_{\save} \right)\,,
    \label{eq:multi-target-covariance}
\end{align}
where $$\rho_{\fail_{i}}$$ and $$\rho_{\save_{i}}$$ are the probabilities of target $$i$$ failing and succeeding on their save respectively, and $$\rho_{\fail_{j}}$$ and $$\rho_{\save_{j}}$$ are the probabilities of target $$j$$ failing and succeeding on their save respectively.

Noting, once again, that the damage dealt on a successful saving throw is typically a constant multiple of the damage dealt on a failed save, $$m_{\save} = \mu_{\save} / \mu_{\fail} = \sigma_{\save} / \sigma_{\fail}$$, the covariance given by Eqn. \eqref{eq:multi-target-covariance} can also be written as,
\begin{align}
    \sigma_{ij}^{2} &= \sigma_{\fail}^2
        \left( \rho_{\fail_{i}} + \rho_{\save_{i}} \, m_{\save} \right)
        \left( \rho_{\fail_{j}} + \rho_{\save_{j}} \, m_{\save} \right)\,.
    \label{eq:typical-multi-target-covariance}
\end{align}

Inserting Eqns. \eqref{eq:typical-save-variance} and \eqref{eq:typical-multi-target-covariance} into Eqn. \eqref{eq:total-covariance-general-2}, the total variance for a save with multiple targets can be expressed in full,
\begin{align}
    \sigma_{\total}^2 =
        &  \sum_{i = 1}^{N} \sigma_{\fail}^2 \left( \rho_{\fail_{i}} + \rho_{\save_{i}} \, m_{\save}^2 \right) + \rho_{\fail_{i}} \, \rho_{\save_{i}} \mu_{\fail}^2 \left( 1 - m_{\save} \right)^2 \nonumber \\\\ 
        &+ \sum_{i \neq j} \sigma_{\fail}^2
        \left( \rho_{\fail_{i}} + \rho_{\save_{i}} \, m_{\save} \right)
        \left( \rho_{\fail_{j}} + \rho_{\save_{j}} \, m_{\save} \right)  \,,
    \label{eq:multi-target-variance}
\end{align}
where the second summation is, once again, over all combinations of $$i$$ and $$j$$ where $$i \neq j$$.


## Identical targets

When each target of a save has an identical chance of failing or succeeding on their saving throw, the total average damage given by Eqn. \eqref{eq:multiple-targets-mean} simplifies to
\begin{align}
    \mu_{\total} 
        &= N \, \mu_{\action} \nonumber \\\\ 
        &= N \left( \rho_{\fail} + \rho_{\save} \, m_{\save} \right) \, \mu_{\fail} \,,
    \label{eq:multiple-identical-targets-mean}
\end{align}
and the total variance given by Eqn. \eqref{eq:multi-target-variance} simplifies to
\begin{align}
    \sigma_{\total}^{2} =
        & N \sigma_{\action}^2 + N \left( N + 1 \right) \, \left( \rho_{\fail} + \rho_{\save} \, m_{\save} \right)^2 \sigma_{\fail}^{2} \,,
    \label{eq:multiple-identical-targets-variance}
\end{align}
where $$\sigma_{\action}^2$$ is the damage variance of the save against a single target as described by Eqn. \eqref{eq:typical-save-variance}.

Combining these two results to calculate the coefficient of variation, $$\CV \equiv \sigma / \mu$$, gives
\begin{align}
    \CV_{\total} = 
        & \left[ \frac{ \CV_{\action}^{\,2} + \left( N + 1 \right) \, \CV_{\fail}^{\,2}  }{ N } \right]^{1/2} \,.
    \label{eq:multiple-identical-targets-cov}
\end{align}
where $$\CV_{\action}$$ is the coefficient of variation for the save against a single target given by Eqn. \eqref{eq:typical-save-cov}, and $$\CV_{\fail}$$ is the coefficient of variation of the damage dealt on a failed saving throw.

Figure [6](#fig:multi-target-save-cv){: .fig-ref} (below) shows how $$\CV_{\total}$$ for the _[fireball](https://www.dndbeyond.com/spells/fireball)_ spell ($$\mu_{\fail} = 28$$, $$\sigma_{\fail} = 4.8$$, and $$m_{\save} = 0.5$$) depends on the number of targets, as well as for a hypothetical variant of the spell where a separate damage roll is made for each target. While the total $$\CV$$ improves as the number of targets increase for both versions of the spell, the official version of the spell does so at a much slower rate than the variant.

<figure id="fig:multi-target-save-cv">
    {% include_relative fig-multi-target-save-cv-small.html %}
    {% include_relative fig-multi-target-save-cv-large.html %}
    <figcaption>Figure 6: Shows how the coefficient of variation for total damage from the <em>fireball</em> spell with \(\rho_{\fail} = 0.65\) depends on the number of targets when a single damage roll is used for all targets (blue) and when separate rolls are made for each target (orange). The dashed reference line at \(\CV_{\fail} \simeq 0.17\) marks coefficient of variation for the damage dealt by the spell on a failed saving throw of 8d6.</figcaption>
</figure>

The official version of the spell also appears to slow down asymptotically as it approaches $$\CV_{\fail} \simeq 0.17$$ for the spell. Taking the limit of Eqn. \eqref{eq:multiple-identical-targets-cov} as $$N \rightarrow \infty$$, the contribution to $$\CV_{\total}$$ from the saving throw vanishes and $$\CV_{\total} = \CV_{\fail}$$ which confirms this is indeed the case. This makes sense when we consider that in this limit, while infinite saving throws are made, only a single damage roll is used across all targets.

# Conclusion

The variability that comes from saves depends strongly on whether the save deals half damage or no damage on a successful saving throw, as well as on whether a single damage roll is used for all targets or a separate damage roll is used for each.

Saves that deal no damage on a successful saving throw behave fundamentally similar to attacks, with nearly all their variability coming from the saving throw and very little coming from the damage roll. As such, their variability can be improved in similar ways: by increasing the probability the target fails their saving throw via the save's DC, or by increasing the number of times the save is used or the number of targets the save affects.

In comparison, saves that deal half damage on a successful saving throw have significantly lower variability coming from the saving throw. This amplifies the importance of the save's damage rolls, and makes improving their variability another practical option for improving the save's overall variability.

In both cases, for saves that are capable of affecting multiple targets per use, how much the overall variability improves with the number of targets depends on the number of damage rolls made by the save. Saves that use a single damage roll for all targets show smaller improvements in their overall variability as the number of targets increases compared to those that use a separate damage roll for each. This difference is largest when the variability of the save's damage rolls is high, making it a more practical option for content that will be used in lower tiers of play.