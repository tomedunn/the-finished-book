---
title: "Initiative Probabilities"
excerpt: "How likely are you to roll higher than your opponent in initiative? How often will you go first or second? This post looks at the math behind initiative ordering needed to answer these questions and more."
permalink: /:collection/:name/
date: 2024-10-23
last_modified_at: 2024-10-23
tags:
  - theory
  - probability
  - combat
  - initiative
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
\newcommand{\ave}{\mathrm{ave}}
\newcommand{\var}{\mathrm{var}}
\newcommand{\erf}{\mathrm{erf}}
\newcommand{\win}{\mathrm{win}}

\newcommand{\order}{\mathcal{o}}
\newcommand{\orders}{\mathcal{O}}

\newcommand{\initBonus}{\mathit{m}}
\newcommand{\initRoll}{\mathit{i}}


\newcommand{\state}{\mathit{s}}
\newcommand{\states}{\mathit{S}}

\newcommand{\ahead}{\mathrm{A}}
\newcommand{\tie}{\mathrm{T}}
\newcommand{\behind}{\mathrm{B}}

\newcommand{\position}{\mathit{p}}

\newcommand{\expectation}{\mathrm{E}}
\newcommand{\variance}{\mathrm{V}}

\newcommand{\dtwenty}{\mathrm{d}20}


\)
</div>

# Introduction

In D&D, combat encounters begin by rolling initiative to determine the order the characters will take their turns in, known as the initiative order. This process relies on rolling dice, making it inherently probabilistic. In this post I look at how the probabilities associated with rolling initiative can be calculated.

# Initiative probabilities

When rolling initiative, each character determines their initiative roll by rolling a $$\dtwenty$$ and adding their initiative bonus, typically their Dexterity modifier. The initiative order is then determined by placing the characters in descending order of their initiative roll. So, the character with the highest initiative roll goes first, the one with the second highest goes second, and so on.

Occasionally, two or more characters will end up with the same initiative roll. In those cases, some additional method is used to determine their relative order, such as the DM choosing the order or using some random process to break the tie. In this post, I assume a random process is used in these scenarios and that each outcome is equally likely.

That all said, there are several ways we can look at the probabilities surrounding rolling initiative and initiative orders. The sections that follow look at initiative probabilities through three different angles. 

* **Relative Position.** This looks at the odds of a character going before or after one specific character in the initiative order.
* **General Position.** This looks at the probability of a character having a specific position within the initiative order, without worrying about the specific positions of the other characters. 
* **Specific Order.** This looks the probability of the initiative order following a specific order.

## Relative Position

As our first step into calculating initiative probabilities, let's look at a simple scenario with two characters, $$A$$ and $$B$$, who each have their own initiative modifiers of $$\initBonus_{A}$$ and $$\initBonus_{B}$$ respectively. When $$A$$ and $$B$$ roll initiative, there are three possible outcomes: $$A$$ could roll higher than $$B$$, $$B$$ could roll higher than $$A$$, or $$A$$ and $$B$$ could roll the same values.

The probability of these outcomes can be determined in a relatively straight forward manner, by simply going through all $$400$$ $$(20^2)$$ combinations of their initiative rolls. However, for reasons that will become clear later on, lets break this process up into two steps: first, calculate the probability of $$B$$ rolling higher, lower, or equalling $$A$$ given $$A$$ has initiative roll of $$\initRoll_{A}$$; second, average the results across all 20 values that $$\initRoll_{A}$$ can take to determine the overall probabilities.

Given an initiative roll $$\initRoll_{A}$$, the probability that $$\initRoll_{A} > \initRoll_{B}$$ is equivalent to the probability of $$\initRoll_{A} - \initBonus_{B} > \dtwenty$$. Since a $$\dtwenty$$ can only take on values between $$1$$ and $$20$$, if $$\initRoll_{A} - \initBonus_{B} \le 1$$ then $$B$$ will always roll higher than $$A$$ and the probability of $$\initRoll_{A} > \initRoll_{B}$$ is equal to zero. Similarly, if $$\initRoll_{A} - \initBonus_{B} > 20$$ then $$A$$ will always roll higher than $$B$$ and the probability of $$\initRoll_{A} > \initRoll_{B}$$ is equal to one. Outside of these scenarios, there are exactly $$\initRoll_{A} - \initBonus_{B} - 1$$ values that $$B$$ could roll that would result in $$\initRoll_{A} > \initRoll_{B}$$.

Putting these all together, the probability of $$\initRoll_{A} > \initRoll_{B}$$, given a specific value of $$\initRoll_{A}$$, is
\begin{eqnarray}
    P(\initRoll_{A} > \initRoll_{B} | \initRoll_{A}) = 
    \begin{cases} 
        0 &, &\initRoll_{A} - \initBonus_{B} <  1 \,; \\\\ 
        \frac{ \initRoll_{A} - \initBonus_{B} - 1 }{ 20 } &, &1 \le \initRoll_{A} - \initBonus_{B} \le 20 \,; \\\\ 
        1 &, &20 < \initRoll_{A} - \initBonus_{B} \,; \\\\ 
        %\frac{ \initRoll_{A} - \initBonus_{B} - 1 }{ 20 } &, &\mathrm{otherwise} \,.
    \end{cases}
    \label{eq:prob-ia-gt-ib-assuming-ia}
\end{eqnarray}

Applying similar logic, the probability that $$\initRoll_{A} < \initRoll_{B}$$, given a specific value of $$\initRoll_{A}$$, is
\begin{eqnarray}
    P(\initRoll_{A} < \initRoll_{B} | \initRoll_{A}) = 
    \begin{cases} 
        1 &, &\initRoll_{A} - \initBonus_{B} < 1 \,; \\\\ 
        \frac{ 20 - (\initRoll_{A} - \initBonus_{B})}{ 20 } &, &1 \le \initRoll_{A} - \initBonus_{B} \le 20 \,; \\\\ 
        0 &, &20 < \initRoll_{A} - \initBonus_{B}  \,. \\\\ 
        %\frac{ 20 - (\initRoll_{A} - \initBonus_{B})}{ 20 } &, &\mathrm{otherwise} \,.
    \end{cases}
    \label{eq:prob-ia-lt-ib-assuming-ia}
\end{eqnarray}
And the probability that $$\initRoll_{A} = \initRoll_{B}$$, given a specific value of $$\initRoll_{A}$$, is
\begin{eqnarray}
    P(\initRoll_{A} = \initRoll_{B} | \initRoll_{A}) = 
    \begin{cases} 
        \frac{ 1 }{ 20 } &, &1 \le \initRoll_{A} - \initBonus_{B} \le 20 \,; \\\\ 
        0 &, &\mathrm{otherwise} \,.
    \end{cases}
    \label{eq:prob-ia-eq-ib-assuming-ia}
\end{eqnarray}

To give a sense of how these probabilities depend on $$\initRoll_{A}$$ and $$\initBonus_{B}$$, Fig. [1](#fig:relative-probs-given-ia){: .fig-ref} (below) plots the values given by Eqns. \eqref{eq:prob-ia-gt-ib-assuming-ia} - \eqref{eq:prob-ia-eq-ib-assuming-ia} over the range $$1 \le \initRoll_{A} - \initBonus_{B} \le 20$$.

<figure id="fig:relative-probs-given-ia">
    {% include_relative fig-relative-probs-given-ia-small.html %}
    {% include_relative fig-relative-probs-given-ia-large.html %}
    <figcaption>Figure 1: Shows the probability of character \(A\) rolling a higher, lower, or tying character \(B,\) who has an initiative bonus of \(\initBonus_{B}\), as a function of character \(A\mathrm{'s}\) initiative roll \(\initRoll_{A}.\)</figcaption>
</figure>


In order to calculate the overall probability of each outcome occurring, we now need to average each of the previous three equations across all possible values of $$\initRoll_{A} = \dtwenty + \initBonus_{A}$$. In all three of these equations the value of $$\initRoll_{A} - \initBonus_{B}$$ determines their behavior, which can also be written as $$\dtwenty + \Delta \initBonus$$ where $$\Delta \initBonus = \initBonus_{A} - \initBonus_{B}$$.

Applying this to Eqn. \eqref{eq:prob-ia-gt-ib-assuming-ia}, the probability that $$\initRoll_{A} > \initRoll_{B}$$ can be expressed in the following way, 
\begin{eqnarray}
    P(\initRoll_{A} > \initRoll_{B}) 
        &=& \frac{1}{20} \sum_{\initRoll_{A}} P(\initRoll_{A} > \initRoll_{B} | \initRoll_{A}) \nonumber \\\\ 
        &=& \frac{1}{20} \sum_{d = 1}^{20} 
        \begin{cases} 
            0 &, &d + \Delta \initBonus <  1 \,; \\\\ 
            \frac{ d + \Delta \initBonus - 1 }{ 20 } &, &1 \le d + \Delta \initBonus \le 20 \,; \\\\ 
            1 &, &20 < d + \Delta \initBonus \,; \\\\ 
        \end{cases}
    \label{eq:prob-ia-gt-ib-1}
\end{eqnarray}

If $$\Delta \initBonus < 0$$ then first $$-\Delta \initBonus$$ terms in this summation are zero. The remaining $$20-\Delta \initBonus$$ terms increase linearly from $$1/20$$ to $$(19 + \Delta \initBonus)/20$$, which gives the summation a total value of $$(19 + \Delta \initBonus) (20 + \Delta \initBonus)/40$$. Applying this same logic to the case where $$\Delta \initBonus > 0$$ yields similar results. Therefore the overall probability of $$\initRoll_{A} > \initRoll_{B}$$ is equal to
\begin{eqnarray}
    P(\initRoll_{A} > \initRoll_{B}) 
        &=& \begin{cases} 
            \frac{ \left( 19 + \Delta \initBonus \right) \left( 20 + \Delta \initBonus \right) }{ 800 } &, &\Delta \initBonus < 0 \,; \\\\ 
            1 - \frac{ \left( 20 - \Delta \initBonus \right) \left( 21 - \Delta \initBonus \right) }{ 800 } &, &\Delta \initBonus \ge  0 \,.
        \end{cases}
    \label{eq:prob-ia-gt-ib}
\end{eqnarray}

The probability of $$\initRoll_{A} < \initRoll_{B}$$ can be obtained from Eqn. \eqref{eq:prob-ia-gt-ib} by swapping $$A$$ and $$B$$, i.e., letting $$\Delta \initBonus \rightarrow -\Delta \initBonus$$. Doing so yields
\begin{eqnarray}
    P(\initRoll_{A} < \initRoll_{B}) 
        &=& \frac{1}{20} \sum_{\initRoll_{A}} P(\initRoll_{A} < \initRoll_{B} | \initRoll_{A}) \nonumber \\\\ 
        &=& \begin{cases} 
            1 - \frac{ \left( 20 - \Delta \initBonus \right) \left( 21 - \Delta \initBonus \right) }{ 800 } &, &\Delta \initBonus <  0 \,; \\\\ 
            \frac{ \left( 19 + \Delta \initBonus \right) \left( 20 + \Delta \initBonus \right) }{ 800 } &, &\Delta \initBonus \ge 0 \,.
        \end{cases}
    \label{eq:prob-ia-lt-ib}
\end{eqnarray}

Finally, the overall probability of a tie between $$A$$ and $$B$$ can be calculated from Eqn. \eqref{eq:prob-ia-eq-ib-assuming-ia} as
\begin{eqnarray}
    P(\initRoll_{A} = \initRoll_{B} ) 
        &=& \frac{1}{20} \sum_{\initRoll_{A}} P(\initRoll_{A} = \initRoll_{B} | \initRoll_{A}) \nonumber \\\\ 
        &=& \frac{1}{20} \sum_{d = 1}^{20}
        \begin{cases} 
            \frac{ 1 }{ 20 } &, &1 \le d + \Delta \initBonus \le 20 \,; \\\\ 
            0 &, &\mathrm{otherwise} \,.
        \end{cases}
    \label{eq:prob-ia-eq-ib-1}
\end{eqnarray}
Whether $$\Delta \initBonus$$ is positive or negative, the number of non-zero terms in the summation is equal to $$20 - \lvert \Delta \initBonus \rvert$$. Therefore, 
\begin{eqnarray}
    P(\initRoll_{A} = \initRoll_{B} ) 
        &= \frac{ 20 - \lvert \Delta \initBonus \rvert }{ 400 } \,.
    \label{eq:prob-ia-eq-ib}
\end{eqnarray}

The dependence of Eqns. \eqref{eq:prob-ia-gt-ib} - \eqref{eq:prob-ia-eq-ib} on $$\Delta \initBonus$$ is shown in Fig. [2](#fig:relative-probs){: .fig-ref} (below).

<figure id="fig:relative-probs">
    {% include_relative fig-relative-probs-small.html %}
    {% include_relative fig-relative-probs-large.html %}
    <figcaption>Figure 2: Shows the probability of character \(A\) rolling a higher, lower, or tying character \(B.\) Characters \(A\) and \(B\) have initiative bonuses of \(\initBonus_{A}\) and \(\initBonus_{B}\) respectively.</figcaption>
</figure>

As a final step, we can calculate the probabilities of either $$A$$ or $$B$$ going first from Eqns. \eqref{eq:prob-ia-gt-ib} - \eqref{eq:prob-ia-eq-ib} by noting that $$A$$ always goes first when their initiative roll is higher than $$B\mathrm{'s}$$ and that $$A$$ has a $$50\%$$ chance of going first when it equals $$B\mathrm{'s},$$
\begin{eqnarray}
    P(A \, \mathrm{first} ) 
        &= P(\initRoll_{A} > \initRoll_{B} ) + \frac{1}{2} P(\initRoll_{A} = \initRoll_{B} )  \,.
    \label{eq:prob-a-before-b}
\end{eqnarray}
Conversely, $$B$$ always goes first when their initiative roll is higher than $$A\mathrm{'s}$$ and they have a $$50\%$$ chance of going first when it equals $$A\mathrm{'s},$$
\begin{eqnarray}
    P(B \, \mathrm{first} ) 
        &= P(\initRoll_{A} < \initRoll_{B} ) + \frac{1}{2} P(\initRoll_{A} = \initRoll_{B} )  \,.
    \label{eq:prob-b-before-a}
\end{eqnarray}

The dependence of these probabilities on $$\Delta \initBonus$$ is shown in Fig. [3](#fig:relative-order-probs){: .fig-ref} (below). Note that for $$\Delta \initBonus$$ near zero the probabilities change in roughly a linear fashion, but as $$\Delta \initBonus$$ grows more positive or more negative both probabilities get less and less sensitive to changes in $$\Delta \initBonus$$.
<figure id="fig:relative-order-probs">
    {% include_relative fig-relative-order-probs-small.html %}
    {% include_relative fig-relative-order-probs-large.html %}
    <figcaption>Figure 3: Shows the probability of characters \(A\) and \(B\) going first in the initiative order relative to one another. Characters \(A\) and \(B\) have initiative bonuses of \(\initBonus_{A}\) and \(\initBonus_{B}\) respectively.</figcaption>
</figure>

## Explicit order

The results of the previous section are useful when trying to determine probabilities for the relative initiative order of two characters, but they aren't sufficient for orders with more characters. For this, a different approach is needed.

The most direct way to determine the probability of a specific initiative order, with more than two character, occurring is to calculate it directly by counting all possible initiative roll combinations that could result in it and dividing by the total number of possible rolls. For an encounter with $$N$$ combatants, we can perform this calculation for the initiative order $$\order = \left( C_{1}, C_{2}, \cdots, C_{N} \right)$$ using the following equation,
\begin{eqnarray}
    P(\order) = \frac{ 1 }{ 20^{N} }
        \sum_{\initRoll_{1} = 1+\initBonus_{1}}^{20+\initBonus_{1}} 
        \sum_{\initRoll_{2} = 1+\initBonus_{2}}^{20+\initBonus_{2}} 
        \cdots 
        \sum_{\initRoll_{N} = 1+\initBonus_{N}}^{20+\initBonus_{N}} 
        w\left(\initRoll_{1}, \initRoll_{2}, \cdots, \initRoll_{N} \right)
        .
    \label{eq:initiative-order-probability-full}
\end{eqnarray}
Here, $$\initBonus$$ represents a character's initiative bonus, and $$w\left(\initRoll_{1}, \initRoll_{2}, \cdots, \initRoll_{N} \right)$$ is a weighting function that returns values between 0 and 1 depending on the initiative rolls. The factor of $$1/20^N$$ in front of the summations normalizes the results to the total number of possible initiative roll combinations.

When the initiative rolls aren't in descending order, i.e., when $$\initRoll_{j} \lt \initRoll_{j+1}$$ for at least one character in the order, the weighting function returns $$w = 0.$$ And, when the initiative rolls are in *strictly* descending order, i.e., $$\initRoll_{1} \gt \initRoll_{2} \gt \cdots \gt \initRoll_{N}$$ with no ties, the weighting function returns $$w = 1.$$

The rest of the time, when the rolls are in descending order and two or more characters have the same initiative roll, the value returned by the weighting function falls somewhere in the range $$[0, 1]$$, depending on how ties are resolved when rolling initiative. As in the previous section, I've assumed all ties are broken randomly, with each outcome being equally likely. Meaning, if characters $$C_{1}$$ and $$C_{2}$$ have the same initiative rolls, the order $$(C_{1}, C_{2})$$ is just as likely as $$(C_{2}, C_{1}),$$ and the probability of the tie-break process resulting in $$(C_{1}, C_{2})$$ is equal to $$1/2.$$

To understand how $$w$$ depends on the number of tied initiative rolls, we can expand on the previous example by considering a three way initiative tie, $$\initRoll_{1} = \initRoll_{2} = \initRoll_{3}.$$ For this scenario there are $$6$$ possible orders that could result from the tie-break process, which means the specific order $$\order = \left( C_{1}, C_{2}, C_{3} \right)$$ has only a $$1/6$$ chance of occurring. Extending this to a tie consisting of $$n$$ characters, the number of possible orders is equal to $$n!$$ (or the [factorial](https://en.wikipedia.org/wiki/Factorial) of $$n$$) which means the probability of any specific order is $$1/n!.$$

If there are multiple groups of tied characters the results compound with one another, and the total probability of getting any one specific order is equal to the product of the probability for each group individually. For example, if an encounter has a two way initiative tie at $$i=15$$ and a three way initiative tie at $$i=10$$, there would be $$12 = (2!)(3!)$$ possible initiative orders and the probability of getting one specific order would be $$1/12.$$

Putting this all together, the weighting function in Eqn. \eqref{eq:initiative-order-probability-full} takes the form
\begin{eqnarray}
    w\left(\initRoll_{1}, \initRoll_{2}, \cdots, \initRoll_{N} \right) = 
    \begin{cases} 
        \prod_{\initRoll} \frac{ 1 }{ n_{\initRoll} ! } &, &\initRoll_{1} \ge \initRoll_{2} \ge \cdots \ge \initRoll_{N} \,, \\\\ 
        0 &, &\mathrm{otherwise}\,,
    \end{cases}
    \label{eq:weighting-function}
\end{eqnarray}
where $$n_{\initRoll}$$ is the number of creatures with $$\initRoll$$ for their initiative roll. 

**Note.** Eqn. \eqref{eq:weighting-function} takes advantage of the fact that $$0! = 1$$, which is why $$w = 1$$ when there are no ties and the initiative rolls are in a descending order.
{: .notice--warning}

Figure [4](#fig:explicit-order-probs){: .fig-ref} (below) shows the probability of every possible initiative order for an example encounter with three combatants, calculated using Eqns. \eqref{eq:initiative-order-probability-full} and \eqref{eq:weighting-function}.

<figure id="fig:explicit-order-probs">
    {% include_relative fig-explicit-order-probs-small.html %}
    {% include_relative fig-explicit-order-probs-large.html %}
    <figcaption>Figure 4: Shows the probability of each initiative order for an encounter with three combatants, \(A,\) \(B,\) and \(C,\) with initiative bonuses \(\initBonus_{A}=2,\) \(\initBonus_{B}=5,\) and \(\initBonus_{C}=0.\)</figcaption>
</figure>

It's worth noting that while Eqn. \eqref{eq:initiative-order-probability-full} will give the probability of seeing a specific initiative order, it also scales extremely poorly with the number of characters in the encounter. Since each character can have 20 different initiative values, the total number of initiative rolls that need to be checked for any given order is equal to $$20^N$$. Meaning, for an encounter with a party of four PCs against one monster, $$3,200,000$$ combinations are need to calculate the probability of just one initiative order. And with $$120 = 5!$$ possible initiative orders, 384 million combinations are needed to calculate probabilities for them all.

We can improve issue somewhat by noting that $$w = 0$$ if the rolls aren't in decreasing order. This means that if any initiative roll is larger than the one ahead of it in the order, $$\initRoll_{j} > \initRoll_{j-1}$$, then $$w = 0$$ and we can skip it. To do so, we can adjust the upper limit of our summations from $$20 + \initBonus_{j}$$ to $$\initRoll_{j}^{\mathrm{max}} = \mathrm{min}\left( \initRoll_{j-1}, 20 + \initBonus_{j} \right)$$. Since there aren't any characters ahead of $$C_{1}$$ in the initiative order, the upper limit of their summation remains the same, and Eqn. \eqref{eq:initiative-order-probability-full} becomes
\begin{eqnarray}
    P(\order) = \frac{ 1 }{ 20^{N} }
        \sum_{\initRoll_{1} = 1+\initBonus_{1}}^{20 + \initBonus_{1}} 
        \sum_{\initRoll_{2} = 1+\initBonus_{2}}^{\initRoll_{2}^{\mathrm{max}}} 
        \cdots 
        \sum_{\initRoll_{N} = 1+\initBonus_{N}}^{\initRoll_{N}^{\mathrm{max}}} 
        w\left(\initRoll_{1}, \initRoll_{2}, \cdots, \initRoll_{N} \right)\,.
    \label{eq:initiative-order-probability-reduced} 
\end{eqnarray}

This approach reduces the number of initiative roll combinations that need to be checked for each individual initiative order, but the total number across all possible initiative orders still scales $$\propto 20^N.$$ The next section looks at a different method for calculating the probability of a single character's placement within the initiative order that scales significantly better.

## General position

Another question we might want to answer regarding initiative is the probability of a specific character going second or third in the initiative order. This can be done by using Eqn. \eqref{eq:initiative-order-probability-reduced} to calculate the probability of each initiative orders with that outcome, but the time it takes to do so grows rather quickly with the number of characters. 

To speed up this calculation we can take advantage of the fact that we only need to fix one character's position within the initiative order. The remaining characters can be shuffled around in front of and behind the character we're interested without having to worry about their positions relative to one another. For example, we can calculate the probability of characters $$A$$ and $$B$$ going before character $$C$$ without having to worry about whether $$A$$ goes before $$B$$ or not.

This effectively reduces the calculation to whether each character's initiative roll is higher, lower, or ties the character we're interested in. If the character we're interested, $$C_{1},$$ gets $$\initRoll_{1}$$ for their initiative roll, then the probability of them going in position $$\position$$ in the order can be determined from
\begin{eqnarray}
    P_{1}\left( \position \right) = 
        \sum_{\initRoll_{1}}
        %\sum_{\state_{1} = \tie } 
        \sum_{\state_{2} \in \states}
        \cdots 
        \sum_{\state_{N} \in \states}
        %P\left(\state_{1}, \state_{2}, \cdots, \state_{N} \mid \position, \initRoll_{1} \right)\,.
        \prod_{i = 1}^{N} P_{i} \left( \state_{i} \mid \initRoll_{1} \right) 
        %\nonumber \\\\ \times
        w\left(n_{\ahead}, n_{\tie}, n_{\behind}, \position \right)
    \label{eq:initiative-position-probability} 
\end{eqnarray}
Here, $$\states = \{\mathrm{ahead}, \mathrm{tied}, \mathrm{behind} \}$$ represents the three possible states that can result from each character's initiative roll. Here also, $$P_{i} \left( \state_{i} \mid \initRoll_{1} \right)$$ gives the probability of character $$C_{i}$$ ending up in state $$\state_{i}$$ given $$C_{1}$$ has an initiative roll of $$\initRoll_{1}$$. These can be calculated using Eqns. \eqref{eq:prob-ia-gt-ib-assuming-ia} - \eqref{eq:prob-ia-eq-ib-assuming-ia}. Finally, as in the previous section, $$w\left(n_{\ahead}, n_{\tie}, n_{\behind}, \position \right)$$ is a weighting function that returns a value between $$0$$ and $$1$$ based on the number of creatures ahead of, $$n_{\ahead}$$, behind, $$n_{\behind}$$, and tied, $$n_{\tie}$$, with character $$C_{1}$$.

We can understand the weighting function in Eqn. \eqref{eq:initiative-position-probability} by looking at a few limiting cases. When $$n_{\ahead} \ge \position$$, too many characters are ahead of $$C_{1}$$ in the initiative order, making position $$\position$$ impossible for them, and therefore $$w = 0.$$ Similarly, when $$n_{\behind} \gt N - \position$$, too many characters are behind $$C_{1}$$ in the initiative order, and $$w = 0$$ as well. Finally, when there are exactly the right number of characters ahead of and behind $$C_{1}$$ to make position $$\position$$ work, $$n_{\ahead} = \position - 1$$ and $$n_{\behind} = N - \position$$, then $$w = 1.$$

This leave only combinations with $$n_{\ahead} \lt p$$ as well as $$n_{\ahead} + n_{\tie} \ge \position$$ unaccounted for. For these cases, character $$C_{1}$$ ending up in position $$\position$$ requires them to go through the tie-break process and end up in position $$\position - n_{\ahead}$$ relative to the characters they're tied with. Since there are $$n_{\tie} + 1$$ possible positions character $$C_{1}$$ could take within this sub-group, and since each one is equally likely, the probability of them ending up in exactly the position needed for an overall position of $$\position$$ is simply $$1/(n_{\tie} + 1).$$

Putting this all together, the weighting function used by Eqn. \eqref{eq:initiative-position-probability} can be expressed as
\begin{eqnarray}
    w\left(n_{\ahead}, n_{\tie}, n_{\behind}, \position \right) = 
        %\prod_{i = 1}^{N} P_{i} \left( \state_{i} | i_{1} \right) 
        \begin{cases} 
            \left( n_{\tie} + 1 \right)^{-1} , & n_{\ahead} \lt \position \, \mathrm{and} \, n_{\behind} \le N - \position \,; \\\\ 
            0 , &\mathrm{otherwise} \,.
        \end{cases}
        \,.
    \label{eq:general-weighting-function}
\end{eqnarray}

As an example of Eqns. \eqref{eq:initiative-position-probability} and \eqref{eq:general-weighting-function} in action, Fig. [5](#fig:general-position-example-use){: .fig-ref} (below) shows the probability of a character being in each initiative position in an encounter with four monsters, each with an initiative bonus of zero. This can be useful when trying to assess the value of increasing a character's initiative bonus, a topic I plan to cover in a future post.

<figure id="fig:general-position-example-use">
    {% include_relative fig-general-position-example-use-small.html %}
    {% include_relative fig-general-position-example-use-large.html %}
    <figcaption>Figure 5: Shows the average initiative order position and standard deviation for a character, as a function of their initiative bonus, in an encounter with three other characters, each with an initiative bonus \(\initBonus=0.\)</figcaption>
</figure>

As a final comment on this method, since there are only three states that each character can take, the number of combinations needed for Eqn. \eqref{eq:initiative-position-probability} grows with the number of characters as $$20 \cdot 3^{N-1}$$. This scales considerably better than Eqn. \eqref{eq:initiative-order-probability-reduced} from the previous section, which grows as $$20^N$$ with the number of characters. A comparison of this is shown in Fig. [6](#fig:calculation-scaling){: .fig-ref} (below).

<figure id="fig:calculation-scaling">
    {% include_relative fig-calculation-scaling-small.html %}
    {% include_relative fig-calculation-scaling-large.html %}
    <figcaption>Figure 6: Shows how the number of calculations scales with the number of characters in an encounter.</figcaption>
</figure>


# Conclusion

Calculating the probabilities surrounding initiative is not especially straight forward. The methods for calculating the probability of a specific initiative order, or the general position of a character in the initiative order can't be be reduced to a simple analytic equation for encounters with more than two characters. Still, being able to calculate these probabilities is an important tool in understanding the math behind combat encounters due to how important the initiative order is to the difficulty of an encounter. I plan to discuss this, as well as the impact initiative has on encounter variability in a future post.