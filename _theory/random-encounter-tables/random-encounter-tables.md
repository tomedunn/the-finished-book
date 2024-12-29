---
title: "Random Encounter Tables"
excerpt: "Random encounter tables are a great tool, but they can sometimes create problems. Here we explore the math behind random encounter tables and techniques we can use to avoid those problems."
permalink: /:collection/:name/
date: 2024-12-29
last_modified_at: 2024-12-29
tags:
  - theory
  - probability
  - random encounters
  - design
---

{% include LaTex.html %}

<div style="display:none">
\(
% probabilities
\newcommand{\cdf}{\mathit{F}}
\newcommand{\pdf}{\mathit{P}}
\newcommand{\CV}{\mathit{CV}}
% variables
\newcommand{\nRolls}{n_{\mathrm{r}}}
\newcommand{\pEncounter}{p_{\mathrm{e}}}
\newcommand{\nEncounters}{n_{\mathrm{e}}}
\newcommand{\aEncounters}{\mu_{\mathrm{e}}}
\newcommand{\cvEncounters}{\CV_{\mathrm{e}}}
\newcommand{\sEncounters}{\sigma_{\mathrm{e}}}
\newcommand{\pNoEncounter}{p_{\mathrm{n}}}

%\newcommand{\nMin}{n_{\mathrm{min}}}
\newcommand{\nMin}{n_{0}}
%\newcommand{\nMax}{n_{\mathrm{max}}}
\newcommand{\nMax}{n_{1}}
\)
</div>


# Introduction

Random encounter tables are a common tool used by DMs in Dungeons and Dragons. The idea behind them is that, rather than the DM deciding when the adventurers will face an encounter, the DM rolls dice at specific intervals to determine what, if anything, the PCs will face. This can add a fun element of randomness to an adventure, but they can also be a point of frustration depending on how they're implemented and used.

In this post I look at a specific category of random encounter table where the odds of a roll resulting in a encounter are lower than the odds of no encounter occurring. I also show an alternative method for generating random encounters that is statistically similar to the traditional method while requiring fewer rolls.

# Random encounter math

A random encounter table is, as its name suggests, a table of encounters that can be selected at random. This is generally done by rolling a die and then picking the encounter that corresponds to the resulting value. Often, one of the entries in the table will specify that no encounter takes place. If the table doesn't have such an entry, a separate die is generally rolled first to determine if an encounter occurs, before rolling on the encounter table to see which encounter it is.

Regardless of the specifics, each time a random encounter is rolled for there is some probability, $$\pEncounter ,$$ that an encounter will occur, and some probability, $$\pNoEncounter  = 1 - \pEncounter ,$$ that one won't. So long as these probabilities don't change over time, the probability that the PCs will face $$\nEncounters$$ encounters after $$\nRolls$$ rolls will follows the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution),
\begin{align}
    \pdf( \nEncounters ) = \binom{ \nRolls }{ \nEncounters } \, \pEncounter ^{ \nEncounters } \left( 1 - \pEncounter  \right)^{\nRolls - \nEncounters} ,
    \label{eq:encounter-distribution}
\end{align}
where $$\binom{ \nRolls }{ \nEncounters }$$ is the binomial coefficient, which represents the number of ways $$\nEncounters$$ encounters can occur across $$\nRolls$$ rolls, 
\begin{align}
    \binom{ \nRolls }{ \nEncounters }  =  \frac{ \nRolls! }{ \nEncounters! \left( \nRolls - \nEncounters \right) ! } . \\nonumber
\end{align}

The average number of encounters, $$\aEncounters,$$ we expect to see after $$\nRolls$$ rolls simply the probability of an encounter multiplied by the number of rolls,
\begin{align}
    \aEncounters = \nRolls \pEncounter .
    \label{eq:encounter-mean}
\end{align}
From this we can see that the average number of rolls it takes to get an encounter, $$\nRolls / \aEncounters = 1/\pEncounter,$$ increases substantially when the probability of an encounter from a single roll is small. For example, if each roll has only a $$10\%$$ chance of resulting in an encounter, $$\pEncounter = 0.1,$$ it will take $$1 / 0.1 = 10$$ rolls on average for each encounter.

Unless the number of rolls is infinitely large, it's not especially likely that rolling for encounters $$\nRolls$$ times will result in exactly $$\aEncounters$$ encounters. How close we should expect to get can be characterized by the standard deviation of the number of encounters, $$\sEncounters,$$ which for $$\nRolls$$ rolls is
\begin{align}
    \sEncounters = \sqrt{ \nRolls \pEncounter \left( 1 - \pEncounter \right) } .
    \label{eq:encounter-sigma}
\end{align}

This can be put into relative terms by calculating the coefficient of variation for the number of encounters,
\begin{align}
    \cvEncounters \equiv \frac{ \sEncounters }{ \aEncounters } = \sqrt{ \frac{ 1 - \pEncounter }{ \nRolls \pEncounter } } ,
    \label{eq:encounter-cv}
\end{align}
which tells us how large a typical difference might be relative to the average.

Note that $$\cvEncounters$$ gets smaller as the number of rolls gets larger, and $$\cvEncounters$$ gets larger when the probability of an encounter from a single roll is low. This second point can be seen more clearly in Fig. \figref{fig:cv-scaling} (below), which plots Eqn. \eqref{eq:encounter-cv} across a range of $$\pEncounter$$ values for $$\nRolls = 1$$.

<figure id="fig:cv-scaling">
    {% include_relative fig-cv-scaling-small.html %}
    {% include_relative fig-cv-scaling-large.html %}
    <figcaption>Shows how the coefficient of variation for the number of encounters, \(\cvEncounters,\) depends on the probability of a single roll resulting in an encounter, \(\pEncounter,\) when \(\nRolls = 1.\)</figcaption>
</figure>

Going back to our earlier example, if each roll has a $$10\%$$ chance of resulting in an encounter and we roll $$10$$ times, while the average number of encounters will be $$\aEncounters = 1$$ the standard deviation will be $$\sEncounters \approx 0.95,$$ which gives a coefficient of variation of $$\cvEncounters \approx 0.95$$ as well. In practice, if we were to run such a table in an actual game, this means we should expect the actual number of encounters to differ quite significantly from the average.

## Example

Consider the following example random encounter table taken from the "[Horns of the Beast](https://www.dndbeyond.com/sources/dnd/dmg-2024/creating-adventures#HornsoftheBeast)" example adventure in chapter 4 of the 2024 _Dungeon Master's Guide_.

<div class="dataframe center">
    <h3 id="tab:example-dmg">Example table</h3>
    {% include_relative tab-example-dmg.html %}
</div>

If we ignore the specifics of the individual encounter options, the probability of getting an encounter from a single roll is only $$30\%$$, i.e., $$\pEncounter = 0.3,$$ which means we should expect to see one encounter every $$3.33$$ rolls on average. Since a DM is likely to roll on the table eight times over the course of the adventure, the average number of encounters from the table should be close to $$\aEncounters \approx 2.4$$ with a standard deviation of $$\sEncounters \approx 1.3.$$

<figure id="fig:example-encounter-distribution">
    {% include_relative fig-example-encounter-distribution-small.html %}
    {% include_relative fig-example-encounter-distribution-large.html %}
    <figcaption>Shows the probability of a party experiencing \(n\) encounters after rolling eight times on the example random encounter table.</figcaption>
</figure>

Figure \figref{fig:example-encounter-distribution} (above) shows the full probability distribution, calculated using Eqn. \eqref{eq:encounter-distribution}, for the number of encounters after eight rolls. What's interesting to note here is that, while the most likely outcomes are for the PCs to face $$2-3$$ encounters, those outcomes only account for $$55\%$$ of all outcomes. That's just a little more than half.

The distribution also shows there's a decently high chance of either no encounters occurring or more than double the average occurring, each with probabilities around $$5.8\%.$$ That means a bit more than one in ten groups who run this adventure are going to have a significantly different experience than one might expect using just the average for this part of the adventure.

This behavior isn't inherently good or bad, but it is something worth considering when using this kind of random encounter table in an adventure. In the next section, I discuss an alternative way of running this kind of encounter table that can reduce the number of rolls needed and can also be modified to remove these outliers.

# Alternative approach

Using the table in the previous section, a DM would need to roll $$3.33$$ times on average before getting an encounter. If the table had a lower chance of each roll resulting in an encounter, this average would be even higher. That's potentially a lot of time spent rolling! 

In this section I'll show how we can reduce the number of rolls needed to just two per encounter, regardless of the encounter probability, by borrowing a method used in computational physics known at [kinetic Monte Carlo](https://en.wikipedia.org/wiki/Kinetic_Monte_Carlo).

The basic approach here is this, rather than rolling each time a random encounter could occur, we roll once to determine how many rolls it would have taken to get our next random encounter, and then once to determine which random encounter the PCs face. To do this, we'll need a way of translating the probability of a random encounter occurring into a new table that tells us how many rolls would be needed before the next random encounter.

To start this process, we need to calculate the probability that the next random encounter occurs after exactly $$n$$ rolls, $$\pdf(n),$$ on our original random encounter table. If the probability of a single roll resulting in an encounter is $$\pEncounter$$, then the probability the next random encounter occurring after just one roll must be the same, i.e., $$\pdf(1) = \pEncounter.$$ In order for the first encounter to occur on the second roll, the first roll must have resulted in no encounter, which occurs with probability $$1 - \pEncounter,$$ and the second roll must have resulted in an encounter, which again occurs with probability $$\pEncounter,$$ for a total probability of $$\pdf(2) = \pEncounter \left( 1 - \pEncounter \right).$$

We can extend this to a general equation by noting that each additional roll it takes for the first encounter to occur adds an extra factor of $$1 - \pEncounter.$$ Thus,
\begin{eqnarray}
    \pdf(n) &=& \pEncounter \left( 1 - \pEncounter \right)^{n - 1} ,
    \label{eq:rolls-needed-pdf}
\end{eqnarray}
the results of which are shown in Fig. \figref{fig:example-rolls-before-encounter} (below) for the case where $$\pEncounter = 0.3.$$

<figure id="fig:example-rolls-before-encounter">
    {% include_relative fig-example-rolls-before-encounter-small.html %}
    {% include_relative fig-example-rolls-before-encounter-large.html %}
    <figcaption>Shows the probability of the next encounter occurring after exactly \(n\) rolls on the example random encounter table when the probability of an encounter from each roll is \(30\%.\)</figcaption>
</figure>

Now that we have these probabilities, we need a way of mapping them onto the range of possible values that can result from rolling whatever standard die we plan on using for our table. Since we know a random encounter has to happen eventually, given sufficiently large $$n,$$ the total probability across all values of $$n$$ must be equal to one,
\begin{align}
    1 &= \sum_{i = 1}^{\infty} \pdf(i).
\end{align}

If we truncate this summation at $$n$$ instead of infinity, we're left with the [cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) of an encounter occurring on or before the $$n\mathrm{-th}$$ roll, 
\begin{align}
    \cdf(n) 
        &= \sum_{i = 1}^{n} \pdf(i) \\nonumber \\\\ 
        %&= \sum_{i=1}^{n} \pEncounter \left( 1 - \pEncounter \right)^{i - 1} \\nonumber \\\\ 
        %&= 1 - \left( 1 - \pEncounter \right)^{n}.
        &= \sum_{i=1}^{n} \pEncounter \, \pNoEncounter^{i - 1} \\nonumber \\\\ 
        &= 1 - \pNoEncounter^{n}.
    \label{eq:rolls-needed-cdf}
\end{align}

In computational physics, the next step in this process would be to generate a random number $$r$$ between 0 and 1, and then finding the value of $$n$$ such that $$\cdf(n-1) \lt r \le \cdf(n).$$ This works because $$\pdf(n) = \cdf(n) - \cdf(n-1)$$ and because $$r$$ can take on an extremely large range of values between 0 and 1.

When using a standard $$D-\mathrm{sided}$$ die, this second point no longer holds true since there are only $$D$$ possible values the die can generate. So, rather than thinking of each side of our die as mapping to a distinct value between 0 and 1, it's better to think of it as representing a range of value covering a width of $$1/D.$$ For example, the value of 1 on a d4 would represent probability values between 0 and 0.25.

If we assign each side, $$d,$$ on our die as covering a range from $$\left(d - 1\right)/D$$ to $$d/D$$ then we can use the midpoint of that range, $$\left(d - 0.5\right)/D,$$ to determine the value of $$n$$ it corresponds to using following formula,
\begin{align}
    %n &= \left\lceil \frac{ \log \left( 1 - \frac{ d - 0.5 }{ D } \right) }{ \log \left(1 - \pEncounter \right) } \right\rceil ,
    n &= \left\lceil \frac{ \log \left( 1 - \frac{ d - 0.5 }{ D } \right) }{ \log \left( \pNoEncounter \right) } \right\rceil ,
    \label{eq:roll-value-converter}
\end{align}
where $$\lceil x \rceil$$ is the [ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), which rounds $$x$$ up to the nearest integer value.

**Note.** Using the midpoint to determine $$n$$ reduces the accuracy of this approach somewhat. There are more accurate approaches that we could use instead, but they are also more complicated and the improvements in accuracy are rather small.
{: .notice--warning}

## Example revisited

Applying this method to our previous [example table](#tab:example-dmg), the number of days between encounters can be mapped to a d20 as shown in the [d20 alternative table](#tab:d20-alternative) (below). When determining when the next random encounter will occur, the DM rolls a d20 and then consults the table to determine the day of the encounter. If that day happens after the PCs have left the area the table applies to then no encounter occurs.

<div class="dataframe center">
    <h3 id="tab:d20-alternative">d20 alternative</h3>
    {% include_relative tab-alt-d20.html %}
</div>

For example, if the DM rolled a 5 then the encounter would occur on the first day. If the PCs were just starting their journey this would be the first day of their travels. Alternatively, if the party had just had an encounter, this would be on the first day after that encounter.

After rolling to determine when the next encounter occurs, the DM would then roll a d6 to determine which of the six random encounters the PCs would face, using the [alternative encounter table](#tab:alternative-encounters) (below).

<div class="dataframe center">
    <h3 id="tab:alternative-encounters">Alternative encounters</h3>
    {% include_relative tab-alt-encounters.html %}
</div>

We can check how accurately this reproduces the results of the original table by calculating the probability distribution for the number of encounters the PCs are likely to face during the eight day journey in the example adventure. The results of this are shown in Fig. \figref{fig:example-d20-encounter-distribution} (below).

<figure id="fig:example-d20-encounter-distribution">
    {% include_relative fig-example-d20-encounter-distribution-small.html %}
    {% include_relative fig-example-d20-encounter-distribution-large.html %}
    <figcaption>Shows the probability of a party experiencing \(n\) encounters using the original table or our approximate d20 table.</figcaption>
</figure>

While not perfect, the alternative table closely matches the probability distribution of the original. If we were to use a larger die, like a d100, instead of a d20 then the difference would be even smaller. 

# Tightening the distribution

Before closing, there is one other aspect of this alternative encounter table presentation worth exploring, and that's how the low and high numbers of encounters are generated from it. 

The probability of the PCs experiencing zero encounters in Fig. \figref{fig:example-d20-encounter-distribution} is around $$5\%$$ for both methods. Using the original table this comes from rolling a d20 value between $$1-14$$ eight times. We can adjust the size of this range to alter the chance of no encounters occurring, but the only way to reduce it to zero would be for an encounter to occur on each roll. In comparison, using the alternate table this can only happen if the very first d20 roll is a $$20,$$ putting the next encounter on day 11, after the PCs have concluded their travels.

Similarly, the only way the alternate table can produce five or more encounters during the adventure is if at least one of the d20 rolls is between $$1-6$$, causing the next encounter to occur on the next day. In both cases, removing these rows from the alternate table eliminates the possibility of the PCs facing no encounters or five or more encounters. This results in a tighter distribution for the number of encounters the PCs might face during this portion of the adventure, while still allowing for some randomness on the number of days between encounters.

These adjustments certainly could be done by hand, i.e., by actually eliminating rows from the previously generated alternate table. However, that would change the size of the die needed by the table, which could make using it a bit more difficult. So instead, the same effect can be accomplished by limiting the maximum and minimum number of days between encounters when constructing the table, and then renormalizing the results so the total probability of an encounter occurring within that range is still equal to one.

Taking this approach, the cumulative distribution function of an encounter occurring described by Eqn. \eqref{eq:rolls-needed-cdf} becomes
\begin{align}
    \cdf(n) 
        %&= \frac{ 1 - \left( 1 - \pEncounter \right)^{n - \nMin + 1} }{ 1 - \left( 1 - \pEncounter \right)^{\nMax - \nMin + 1} }
        %&= \frac{ 1 - \pNoEncounter^{n - \nMin + 1} }{ 1 - \pNoEncounter^{\nMax - \nMin + 1} } ,
        &= \frac{ 1 - \pNoEncounter^{n - \nMin^\prime} }{ 1 - \pNoEncounter^{\nMax - \nMin^\prime} } ,
    \label{eq:adj-rolls-needed-cdf}
\end{align}
where $$\nMax$$ is the maximum number of days allowed between encounters, $$\nMin$$ is the minimum number of days between encounters and $$\nMin^\prime \equiv \nMin - 1.$$

Applying these changes to Eqn. \eqref{eq:roll-value-converter}, the new equation for mapping die value to the number of rolls between encounters is
\begin{align}
    %n &= \nMin - 1 + \left\lceil \frac{ \log \left( 1 - \left( \frac{ d - 0.5 }{ D } \right) \left( 1 - \left(1 - \pEncounter \right)^{\nMax - \nMin + 1} \right) \right) }{ \log \left(1 - \pEncounter \right) } \right\rceil ,
    %n &= \nMin - 1 + \left\lceil \frac{ \log \left( 1 - \left( \frac{ d - 0.5 }{ D } \right) \left( 1 - \pNoEncounter^{\nMax - \nMin + 1} \right) \right) }{ \log \left( \pNoEncounter \right) } \right\rceil ,
    n &= \nMin^\prime + \left\lceil \frac{ \log \left( 1 - \left( \frac{ d - 0.5 }{ D } \right) \left( 1 - \pNoEncounter^{\nMax - \nMin^\prime} \right) \right) }{ \log \left( \pNoEncounter \right) } \right\rceil ,
    \label{eq:adj-roll-value-converter}
\end{align}
where, again, $$d$$ is a face value on the $$D\mathrm{-sided}$$ die used by the alternate table, and $$\lceil x \rceil$$ is the [ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), which rounds $$x$$ up to the nearest integer value.

# Example truncated

Applying this method to the [example table](#tab:example-dmg) and limiting the days between encounters to between $$2-8$$, the number of days between encounters can be mapped to a d20 as shown in the [d20 truncated table](#tab:d20-truncated) (below).

<div class="dataframe center">
    <h3 id="tab:d20-truncated">d20 truncated</h3>
    {% include_relative tab-truncated-d20.html %}
</div>

The effect this has on the probability distribution for the number of encounters across eight days of travel is shown in Fig. \figref{fig:truncated-d20-encounter-distribution} (below). The results show much more consistent outcomes that given by the original example table while still allowing for a bit of randomness.

<figure id="fig:truncated-d20-encounter-distribution">
    {% include_relative fig-truncated-d20-encounter-distribution-small.html %}
    {% include_relative fig-truncated-d20-encounter-distribution-large.html %}
    <figcaption>Shows the probability of a party experiencing \(n\) encounters using the original table or our approximate d20 table.</figcaption>
</figure>


# Conclusion

Generating random encounters by rolling for the time between encounters, rather than whether or not an encounter occurs at fixed intervals, can reduce the number of rolls a DM has to make. These tables can also be easily modified to better control the overall range of possible encounters the PCs experience during an adventure. These are both benefits worth considering when using random encounters.

This approach isn't without its drawbacks, though. The mathematical process for generating these tables is a bit involved, which can be a big hurdle for DMs and adventure designers. A simpler approach, in practice, would be to skip all the math and just create a table for the days between encounter by hand. DMs will also need to learn to use these alternative encounter tables and become comfortable doing so.

Finally, I think it's worth pointing out that the method shown here can also be applied to other mechanics within the game. For example, when running combat with large numbers of monsters a table could be used to determine the number of monsters that need to attack before the hit occurs. This would allow for some randomness in the process without forcing the DM to roll for each individual monster.