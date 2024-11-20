---
title: "Variability: Combat"
excerpt: "How much does chance affect combat?"
permalink: /:collection/:name/
date: 2024-07-16
last_modified_at: 2024-11-11
tags:
  - theory
  - variability
---

{% include LaTex.html %}

<div style="display:none">
\(
% generic
\newcommand{\round}{\mathrm{r}}
\newcommand{\ave}{\mathrm{a}}
\newcommand{\cdf}{\mathit{F}}
\newcommand{\pdf}{\mathit{P}}
\newcommand{\dt}{D}
\newcommand{\win}{\mathrm{win}}
\newcommand{\lose}{\mathrm{lose}}
\newcommand{\final}{\mathrm{final}}
\newcommand{\CV}{\mathit{CV}}
\newcommand{\diff}{\mathit{diff}}
\newcommand{\dave}{\mathit{d}_{\ave}}
\newcommand{\dvar}{\mathit{d}_{\mathrm{v}}}
\newcommand{\tave}{\mathit{t}_{\ave}}
\newcommand{\tvar}{\mathit{t}_{\mathrm{v}}}
\)
</div>

# Introduction

The core elements of combat in D&D are inherently variable: attacks can hit or miss, saves can fail or succeed, and damage rolls can give a range of possible results, all depending on how the dice roll. Because of this, it should come as no surprise that the results of combat are also variable. Whether the player characters (PCs) win or lose, how much damage they take, and even how many turns the encounter lasts can all vary considerably depending on how the dice roll.

In this post I look at the math behind the variability in combat, building upon the results from my previous posts on the variability of [damage rolls]({{ site.data.page-links.variability-damage-healing-rolls.path }}), [attacks]({{ site.data.page-links.variability-attacks.path }}), and [saves]({{ site.data.page-links.variability-saves.path }}).

# General case

This section covers the mathematical framework needed to analyze combat in a probabilistic way, as well as how that framework can be used to calculate a number of useful things, such as the the probability of each side winning, how long the encounter will likely be, and the amount of damage each side is likely to take.

For the sake of simplicity, lets consider an encounter with only two combatants. The combatants each take turns damaging one another until one wins. In order for a combatant to win, they must meet two requirements:
1. their total damage dealt must equal or exceed their opponent's maximum hit points;
2. the total damage they've taken must be less than their own maximum hit points.

In other words, a combatant wins if they deal enough damage to defeat their opponent before their opponent is able to defeat them.

Since the damage dealt by a combatant over the course of an encounter is probabilistic in nature, as illustrated in Fig. \figref{fig:example-damage-distribution} (below), we can't describe either of these requirements in certain terms. Instead of calculating a precise turn where one of the combatants wins, the best we can do is calculate their probability of winning on or after a certain number of turns.

<figure id="fig:example-damage-distribution">
    {% include_relative fig-example-damage-distribution-small.html %}
    {% include_relative fig-example-damage-distribution-large.html %}
    <figcaption>Shows damage probability distributions of the first three rounds of combat for a combatant that attacks twice per round, with a \(65\%\) chance to hit for 7.5 (d6 + 4) damage.</figcaption>
</figure>

With this in mind, along with the previous two requirements, the probability of a combatant winning during any given turn must be proportional to the probability of their total damage equalling or exceeding their opponent's maximum hit points during that turn, and the probability that their opponent's total damage is lower than their own maximum hit points.

In order to calculate these probabilities, we need to know something about each combatant's probability of dealing damage. Specifically, we need a function, $$\pdf(d, t)$$, that tells us the probability of a combatant having dealt exactly $$d$$ total damage after $$t$$ turns in the encounter, also known as their total damage's [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution). 

**Note.** How exactly we get $$\pdf(d, t)$$ isn't important to the rest of the math that follows, just that we have some way of obtaining it. For those wishing to do such calculations, there are a variety of tools that can be used to calculate $$\pdf(d, t)$$, such as [anydice.com](https://anydice.com/) and the [icepool](https://pypi.org/project/icepool/) Python library, which I used to generate the distributions throughout this post.
{: .notice--warning}

Once we have $$\pdf(d, t)$$ for a combatant, the probability of their total damage being enough to defeat their opponent after $$t$$ turns can be calculated by adding up $$\pdf(d, t)$$ for all values of $$d$$ equal to or above their opponent's maximum hit points, $$\HP$$,
\begin{align}
    \cdf_{i} \left( d \ge \HP_{j}, t \right) &= \sum_{d = \HP_{j}}^{\infty} \pdf_{i}(d, t) \,.
    \label{eq:damage-win-prob}
\end{align}
Here, $$i$$ denotes the combatant the probability is being calculated for, and $$j$$ denotes their opponent.

Using Fig. \figref{fig:example-damage-distribution} as an example, this tells us how much of the damage probability distribution, $$\pdf(d, t)$$, lies to the right of their opponent's $$\HP$$. As the encounter goes on, and $$t$$ increases, the distribution shifts farther and farther to the right, pushing Eqn. \eqref{eq:damage-win-prob} closer and closer to $$100\%$$. This makes Eqn. \eqref{eq:damage-win-prob} a [cummulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) (CDF) for the combatant's probability of dealing enough damage to defeat their opponent.

The probability of a combatant's total damage exceeding their opponent's $$\HP$$ during a specific turn can be calculated by taking the difference between Eqn. \eqref{eq:damage-win-prob} on turn $$t$$ and the turn before it, $$t - 1$$,
\begin{align}
    \pdf_{i} \left( d \ge \HP_{j}, t \right) &= \cdf_{i} \left( d \ge \HP_{j}, t \right) - \cdf_{i} \left( d \ge \HP_{j}, t-1 \right) \nonumber \\\\ 
    &= \sum_{d = \HP_{j}}^{\infty} \pdf_{i}(d, t) - \pdf_{i}(d, t-1) \,.
    \label{eq:damage-win-prob-delta}
\end{align}

An example of Eqns. \eqref{eq:damage-win-prob} and \eqref{eq:damage-win-prob-delta} is shown in Fig. \figref{fig:example-dt-distribution} (below) for the same example combatant used previously in Fig. \figref{fig:example-damage-distribution} against an opponent with $$\HP = 30$$. The combatant's total damage is most likely to exceed their opponent's $$\HP$$ during their third turn in combat, which is close to the number of turns we'd expect using just the average damage for each of their attacks, $$t = 3.08 = 30 / (2 \cdot 0.65 \cdot 7.5)$$.

<figure id="fig:example-dt-distribution">
    {% include_relative fig-example-dt-distribution-small.html %}
    {% include_relative fig-example-dt-distribution-large.html %}
    <figcaption>Shows the probability of the total damage dealt exceeding 30 for a combatant that attacks twice per round, with a \(65\%\) chance to hit for 7.5 (d6 + 4) damage.</figcaption>
</figure>

At this point, Eqn. \eqref{eq:damage-win-prob-delta} gives us half the information we need in order to calculate the probability of a combatant winning during a given turn. The remaining information we need is the probability that their opponent hasn't dealt enough damage to defeat them, $$\cdf_{j} \left( d \lt \HP_{i}, t \right)$$. This is easily calculated from Eqn. \eqref{eq:damage-win-prob} by noting that the total probability must equal $$100\%,$$
\begin{align}
    \cdf_{j} \left( d \lt \HP_{i}, t \right) 
        &= 1 - \cdf_{j} \left( d \ge \HP_{i}, t \right) \nonumber \\\\ 
        &= \sum_{d = 0}^{\HP_{i} - 1} \pdf_{j}(d, t) \,.
    \label{eq:damage-lose-prob}
\end{align}

Combining the results of Eqns. \eqref{eq:damage-win-prob-delta} and \eqref{eq:damage-lose-prob}, the probability of a combatant winning during a given turn is,
\begin{align}
    \pdf_{i} \left( \win, t \right) &= \pdf_{i} \left( d \ge \HP_{j}, t \right) \cdf_{j} \left( d \lt \HP_{i}, t \right) \,.
    \label{eq:win-prob-delta}
\end{align}

If we add up the results of Eqn. \eqref{eq:win-prob-delta} for the first $$t$$ turns in an encounter, we get the cumulative probability of a combatant having won by that turn,
\begin{align}
    \cdf_{i} \left( \win, t \right) &= \sum_{t^{\prime} = 0}^{t} \pdf_{i} \left( \win, t^{\prime} \right) \,.
    \label{eq:win-prob}
\end{align}
And, if we take the limit as $$t \rightarrow \infty$$ we get their total probability of winning the encounter, $$\pdf_{i} (\win) = \cdf_{i} \left( \win, t \rightarrow \infty \right)$$.

Figure \figref{fig:example-win-distribution} (below) shows the results of Eqns. \eqref{eq:win-prob-delta} and \eqref{eq:win-prob} for an encounter with two combatant: the first combatant has 30 hit points and attacks twice per round, with a $$65\%$$ chance to hit for 7.5 (d6 + 4) damage, and the second has 30 hit points and attacks only once per round, with a $$65\%$$ chance to hit for 9.5 (1d8 + 5) damage.

<figure id="fig:example-win-distribution">
    {% include_relative fig-example-win-distribution-small.html %}
    {% include_relative fig-example-win-distribution-large.html %}
    <figcaption>Shows the probability of winning for a combat encounter with two combatant. The first combatant has 30 hit points and attacks twice per round, with a \(65\%\) chance to hit for 7.5 (d6 + 4) damage. The second combatant has 30 hit points and attacks only once per round, with a \(65\%\) chance to hit for 9.5 (1d8 + 5) damage.</figcaption>
</figure>

If we were to just use the average damage, it would take the first combatant $$3.1$$ rounds to win and the second combatant $$4.9$$ rounds, which means we'd expect the first combatant to win at the start of the forth round. However, after looking at all possible outcomes, the most likely result is for the first combatant to win at the start of the third round, with the encounter only reaching the fourth round $$31\%$$ of the time. 

Lastly, while the average damage approach might suggest the first combatant always wins, a probabilistic approach shows the first combatant only wins $$90\%$$ of the time.

# Other calculations

## Final encounter length

We can calculate the average number of turns it takes for the encounter to end, $$\tave,$$ using Eqn. \eqref{eq:win-prob-delta},
\begin{align}
    \tave &= \sum_{t = 1}^{\infty} t \, \pdf \left( \win, t \right) \,,
\end{align}
where $$\pdf \left( \win, t \right)$$ is the total probability of either combatant winning during turn $$t$$. 

The variance in the number of turns it takes for the encounter to end, $$\tvar,$$ can be calculated similarly,
\begin{align}
    \tvar &= \sum_{t = 1}^{\infty} \left( t - \tave \right)^2 \, \pdf \left( \win, t \right) \,.
\end{align}

In the example encounter shown in Fig. \figref{fig:example-win-distribution}, the average length of the encounter is $$\tave = 2.8$$ rounds and the standard deviation is $$0.84$$ rounds ($$\tvar = 0.71$$). The average here is slightly shorter than the $$3.1$$ rounds we'd expect using just the average damage done by each combatant. This difference comes from the fact that using the average damage ignores the chance of the second combatant getting lucky and winning the encounter before the first combatant has a chance to defeat them.


## Final damage distribution

In order to determine how much damage a combatant can be expected to deal during an encounter we need to know the probability distribution of that damage, $$\pdf (d)$$, after taking all possible outcomes into account. This can be constructed using the damage probability distributions for each turn, $$\pdf(d, t)$$, and the probability of the encounter ending on that turn, as described by Eqn. \eqref{eq:win-prob-delta}.

If the combatant we're interested in wins during their turn, then the total damage they will have done is equal to their opponent's $$\HP$$. Therefore, we can say that the probability of their final damage equally $$\HP$$ is the same as the probability of winning the encounter, $$\pdf (d = \HP) = \pdf (\win)$$.

For any other damage value between $$0$$ and $$\HP - 1$$, the combatant must have dealt that much damage by the end of a turn, which has a probability of occurring described by $$\pdf(d, t)$$, and their opponent must not have dealt enough damage to win during that turn, which has a probability of occurring equal to $$\pdf ( d \lt \HP, t)$$. Adding up the probability of these two things happening across all turns gives us the final probability of having dealt that total damage,
\begin{equation}
    \pdf_{i} (d) = 
    \begin{cases} 
        \sum\limits_{t = 1}^{\infty} \pdf_{j}(d \ge \HP_{i}, t) \, \pdf_{i}(d, t) & d < \HP_{j} , \\\\ 
        \pdf_{i} (\win) & d = \HP_{j} , \\\\ 
        0 & \mathrm{otherwise} .
    \end{cases}
    \label{eq:final-damage-distribution}
\end{equation}

The average damage taken, $$\dave,$$ and the damage variance, $$\dvar,$$ can be calculated using the final damage distribution given by Eqn. \eqref{eq:final-damage-distribution} in the typical ways,
\begin{align}
    \dave &= \sum_{d = 0}^{\infty} d \, \pdf_{i} (d) \,, \\\\ 
    \dvar &= \sum_{d = 0}^{\infty} \left(d - \dave \right)^2 \, \pdf_{i} (d) \,.
\end{align}

An example final damage distribution given by Eqn. \eqref{eq:final-damage-distribution} is shown in Fig. \figref{fig:final-damage-distribution} (below) for the second combatant from the encounter shown previously in Fig. \figref{fig:example-win-distribution}.

<figure id="fig:final-damage-distribution">
    {% include_relative fig-final-damage-distribution-small.html %}
    {% include_relative fig-final-damage-distribution-large.html %}
    <figcaption>Shows the probability distribution for the final damage dealt by the second combatant in an encounter with two combatants. The first combatant has 30 hit points and attacks twice per round, with a \(65\%\) chance to hit for 7.5 (d6 + 4) damage. The second combatant has 30 hit points and attacks only once per round, with a \(65\%\) chance to hit for 9.5 (1d8 + 5) damage.</figcaption>
</figure>

This is equivalent to the final distribution of the damage taken by the first combatant, and with an average of $$15.5$$ damage out of $$30$$ hit points, this would fall into the Hard encounter difficulty category for the first combatant. It's also interesting to note that the standard deviation for the damage taken by the first combatant is $$8.8$$, which is quite large. This means the encounter could easily play out as Medium or even Deadly depending on how the dice roll.

# Gaussian approximation

So far, I've assumed we have some means of determining $$\pdf(d, t)$$ for each combatant, but for a variety of reasons that may not be the case. In this section we'll look at how the results from the previous section can be approximated using just the average and standard deviation of each combatant's total damage.

From the [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem), we know that after a sufficiently higher number of rounds of combat, the damage dealt by each of our combatants will converge to a [Gaussian distributions](https://en.wikipedia.org/wiki/Normal_distribution) (also known as normal distributions). This is particularly useful for our purposes because the general form for a Gaussian distribution,
\begin{align}
    \pdf \left( x \right) &= \frac{ 1 }{ \sqrt{ 2 \pi \, \sigma^2 } } e^{ - \frac{ \left( x - \mu \right)^2 }{ 2 \hspace{1pt} \sigma^2 } } \,,
    \label{eq:gaussian-generic}
\end{align}
can be calculated for any value $$x$$ by knowing the distribution's average, $$\mu$$, and standard deviation, $$\sigma$$.

This means, if we can calculate $$\mu$$ and $$\sigma$$ for each combatant's total damage, then as long as our combat encounters are sufficiently long, we can use Gaussian distributions to calculate the probabilities needed in the previous section,
\begin{align}
    \pdf \left( d, t \right) &= \frac{ 1 }{ \sqrt{ 2 \pi \, \sigma^2 (t) } } e^{ - \frac{ \left( d - \mu (t) \right)^2 }{ 2 \hspace{1pt} \sigma^2 (t) } } \,.
    \label{eq:gaussian-damage-pdf}
\end{align}
Here, $$\mu(t)$$ and $$\sigma(t)$$ represent the average and standard deviation, respectively, of a combatant's total damage after turn $$t$$. 

We can see the central limit theorem in practice in Fig. \figref{fig:example-gaussian-fit} (below), which shows $$\pdf(d, t)$$ from Fig. \figref{fig:example-damage-distribution} along with their corresponding Gaussian approximations calculated using Eqn. \eqref{eq:gaussian-damage-pdf}. While the Gaussian approximation is a poor fit after only one round, the fit for the second round is substantially better, and by the third round the two are nearly identical.

<figure id="fig:example-gaussian-fit">
    {% include_relative fig-example-gaussian-fit-small.html %}
    {% include_relative fig-example-gaussian-fit-large.html %}
    <figcaption>Shows damage probability distributions of the first three rounds of combat for a combatant that attacks twice per round, with a \(65\%\) chance to hit for 7.5 (d6 + 4) damage, as well as gaussian distributions with the same means and standard deviations.</figcaption>
</figure>

In my previous posts on variability, I show how $$\mu$$ and $$\sigma$$ can be calculated for [attacks]({{ site.data.page-links.variability-attacks.path }}) and [saves]({{ site.data.page-links.variability-saves.path }}), which constitute the vast majority of the damage dealt in combat in D&D. That leaves only the question of how many rounds of combat are needed for our damage distributions to be sufficiently Gaussian?

To get a better sense of this, Fig. \figref{fig:attacks-for-gaussian} (below) shows the number of attacks needed for the resulting damage distribution be fit by a Gaussian with matching mean and standard deviation with a [coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination), or r-squared, of 0.95 or higher.

<figure id="fig:attacks-for-gaussian">
    {% include_relative fig-attacks-for-gaussian-small.html %}
    {% include_relative fig-attacks-for-gaussian-large.html %}
    <figcaption>Shows the number of attacks need before a Gaussian distribution fits the damage probability distributions with a r-squared of 0.95. Each attack rolls the specified damage die on a hit, and two dice are used for critical hits.</figcaption>
</figure>

If we expect most encounters to end in roughly three rounds of combat, then a party of four player characters will have a sufficiently Gaussian damage distribution so long as their chance to hit is greater than $$30\%$$. Similarly, in an encounter with a single monster, a monster that makes only one attack per round would need around a $$70\%$$ chance ot hit or higher, while one that makes two attacks per round would need a $$50\%$$ or higher chance to hit. 

Given that the number of attacks a monster makes each round tends to increase along with their CR, the results from using a Gaussian approximation should improve as monster CR increases.

Another useful feature of Gaussian distributions is that the probability a result $$x$$ being below a certain threshold value $$y$$ has an exact analytic solution,
\begin{align}
    \cdf \left( x \lt y \right) &= \frac{ 1 }{ 2 } \left[ 1 + \mathrm{erf}\left( \frac{ x - \mu }{ \sqrt{2 \sigma^{2} } } \right)   \right] \,.
    \label{eq:gaussian-generic-cdf}
\end{align}
Here, $$\mathrm{erf}$$ refers to the [error function](https://en.wikipedia.org/wiki/Error_function), which is a common function used in Gaussian statistics that can be found in the math libraries for most programming languages, as well as in popular spreadsheet programs like [Excel](https://support.microsoft.com/en-us/office/erf-function-c53c7e7b-5482-4b6c-883e-56df3c9af349) and [Google Sheets](https://support.google.com/docs/answer/9116267).

**Note.** Equation \eqref{eq:gaussian-generic-cdf} assumes the Gaussian distribution described by Eqn. \eqref{eq:gaussian-generic} is continuous, meaning $$x$$ can take on decimal values as well as whole numbers. This isn't the case for damage distributions in D&D because damage can only be a whole number, making Eqn. \eqref{eq:gaussian-generic-cdf} only an approximate solution. The accuracy of this approximation can be improved by substituting $$y \rightarrow y - 0.5$$.
{: .notice--warning}

Applying this result to Eqn. \eqref{eq:damage-win-prob}, the probability of a combatant dealing enough damage to win, yields 
\begin{align}
    \cdf_{i} \left( d \ge \HP_{j}, t \right) 
        &= \frac{ 1 }{ 2 } \left[ 1 - \mathrm{erf}\left( \frac{ \HP_{j} - \mu_{i}(t) }{ \sigma_{i}(t) \sqrt{2} } \right) \right] ,
\end{align}
and applying it to Eqn. \eqref{eq:damage-lose-prob}, the probability of a combatant not dealing enough damage to win, yields
\begin{align}
    \cdf_{j} \left( d \lt \HP_{i}, t \right) 
        &= \frac{ 1 }{ 2 } \left[ 1 + \mathrm{erf}\left( \frac{ \HP_{i} - \mu_{j}(t) }{ \sigma_{j}(t) \sqrt{2} } \right) \right] .
\end{align}

As a stress test of this approach, Fig. \figref{fig:example-gaussian-dt-distribution} shows $$\cdf_{i} \left( d \ge \HP_{j}, t \right)$$ and $$\pdf_{i} \left( d \ge \HP_{j}, t \right)$$, calculated exactly and using a Gaussian approximation, for a combatant that attacks once per round, with a $$65\%$$ chance to hit for 7.5 (d6 + 4) damage, against an opponent with 15 hit points.

<figure id="fig:example-gaussian-dt-distribution">
    {% include_relative fig-example-gaussian-dt-distribution-small.html %}
    {% include_relative fig-example-gaussian-dt-distribution-large.html %}
    <figcaption>Shows the probability of dealing 15 damage or more for a combatant that attacks once per round, with a \(65\%\) chance to hit for 7.5 (d6 + 4) damage.</figcaption>
</figure>

The Gaussian approximation differs from the exact solution slightly, underestimating the chance of the combatant dealing enough damage to win during the second round of combat by $$5.5\%$$, and overestimating it during the third and fourth rounds by $$3.7\%$$ and $$1.1\%$$ respectively. The combatant in this example is right on the limit shown previously in Fig. \figref{fig:attacks-for-gaussian} for a r-squared of 0.95. For combatants with a higher chance to hit, or who make more attacks per round, the results will be even closer.


# Conclusion

Variability is an important aspect D&D's combat system that is often critically overlooked. The math presented in this post helps to form a robust framework for analyzing that variability, but more work is needed.

While I had hoped to include more in this post, I think this is a good place to stop. I have plans to explore this topic further in at least two posts: the first looks at how the Gaussian approximation can be applied to [encounter difficulty]({{ site.data.page-links.variability-encounter-difficulty.path }}) to calculate the probabilities of winning and losing, and the second looks at how initiative influences combat variability.