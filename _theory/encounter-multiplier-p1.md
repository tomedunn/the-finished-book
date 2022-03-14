---
title: "Calculating the Encounter Multiplier"
excerpt: "A deep dive into the encounter multiplier and how to calculate it more accurately."
date: 2022-2-21
last_modified_at: 2022-2-28
#tags:
#  - theory
#  - monsters
#  - encounters
---

\\(
\newcommand{\HP}{\mathit{HP}}
\newcommand{\eHP}{\mathit{eHP}}
\newcommand{\eD}{\mathit{eD}}
\newcommand{\eDPR}{\mathit{eDPR}}
\newcommand{\DPR}{\mathit{DPR}} 
% other
\newcommand{\XP}{\mathit{XP}}
\newcommand{\XPtot}{\overline{\mathit{XP}}}
\newcommand{\eXPtot}{\mathrm{enc}\,\overline{\mathit{XP}}}
\newcommand{\EM}{\mathit{EM}}
\newcommand{\W}{\mathit{W}}
\newcommand{\effMT}{\mathit{eff}^{\,\mathrm{MT}}}
\newcommand{\eDPRMT}{\mathit{eDRT}^\mathrm{\,MT}}
\newcommand{\eDPRST}{\mathit{eDRT}^\mathrm{\,ST}}
\newcommand{\eDPTMT}{\mathit{eDPT}^\mathrm{\,MT}}
\newcommand{\eDPTST}{\mathit{eDPT}^\mathrm{\,ST}}
\newcommand{\dMT}{\mathit{d}}
\newcommand{\dMTi}{\mathit{d}\_{\mspace{2mu}i}}
\newcommand{\dMTj}{\mathit{d}\_{\mspace{2mu}j}}
% NPCs
\newcommand{\NPC}{\mathrm{NPC}}
\newcommand{\NeHP}{\mathit{eHP}\_\mathrm{\NPC}}
\newcommand{\NeDPR}{\mathit{eDPR}\_\mathrm{\NPC}}
\\)

# Introduction

In my previous post, [XP and Encounter Balancing]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}), I showed how monster XP and the encounter multiplier could be derived from fundamental equations for combat. I went through some simple examples of the encounter multiplier in practice, but only enough to establish a basic understanding of how it could be interpreted.

In this post, I would like to go much deeper into analyzing the encounter multiplier. Specifically, how the encounter multiplier relates to the number of enemy NPCs in the equation, as well as how the PCs choose to engage them.

# Calculating the encounter multiplier

From my previous post, the encounter multiplier can be calculated for an encounter using the general equation,

\begin{equation}
    \EM = \left( \frac{ \eXPtot_\mathrm{NPCs} }{ \XPtot_\mathrm{NPCs} } \right) 
    \cdot \left( \frac{ 4\,\XPtot_\mathrm{PCs} }{ \eXPtot_\mathrm{PCs} } \right) \,.
    \label{eq:encounter-multiplier-short}
\end{equation}

Here, $$\XPtot$$ is the total XP for either the PCs or NPCs, and $$\eXPtot$$ is the total encounter XP for either the PCs or NPCs.

Since the goal of this post is to look at how the number of NPCs impacts the encounter multiplier, the second term in Eqn. \eqref{eq:encounter-multiplier-short} can be ignored for now, which simplifies the calculation. This is the equivalent to calculating the full encounter multiplier for parties with four PCs, in which case,

\begin{equation}
    \EM = \left( \frac{ \eXPtot_\mathrm{NPCs} }{ \XPtot_\mathrm{NPCs} } \right) \,.
    \label{eq:encounter-multiplier-short-simple}
\end{equation}

Furthermore, since the total XP for the NPCs, $$\XPtot_\mathrm{NPCs}$$, is independent of how the PCs choose to engage, the only term that needs to be considered is the total encounter XP for the NPCs, 

\begin{align}
    \eXPtot_\mathrm{NPCs} &= \sum_{i,j} \W\_{\,\NPC\_{ij}} \cdot \XP\_{\,\NPC\_{ij}}\,.
    \label{eq:encounter-xp-npcs}
\end{align}

The XP terms in Eqn. \eqref{eq:encounter-xp-npcs} are calculated from the effective hit points $$(\eHP\,)$$ and the effective damage per round $$(\eDPR\,)$$ of the NPCs in the encounter, 

\begin{equation}
    \XP\_{\,\NPC\_{ij}} = \frac{1}{4} \eHP\_{\,\NPC\_{i}} \cdot \eDPR\_{\,\NPC\_{j}}\,,
    \label{eq:xp-npc}
\end{equation}

and represents the average damage NPC $$\mathit{j}$$ can be expected to do in the time it takes NPC $$\mathit{i}$$ to be defeated. 

The other term in Eqn. \eqref{eq:encounter-xp-npcs}, $$\W_{\,\NPC_{ij}}$$, is the weight of each XP term in the summation, which depend on how the PCs choose to engage the NPCs in the encounter. This is ultimately where the difficulty lies in calculating the encounter multiplier, determining what $$\W_{\,\NPC_{ij}}$$ should be for each pair of NPCs in an encounter, depending on the strategy the PCs choose to take.

To help in understanding how these weights are calculated, I've included visual representations of Eqn. \eqref{eq:encounter-xp-npcs}, like the one shown in Fig. <a href="#fig:xp-encounter-diagram-example" class="fig-ref">1</a> below, for the various strategies discussed in this post. The area of each square in these diagrams is proportional to one of the XP terms found in Eqn. \eqref{eq:encounter-xp-npcs}, as described by Eqn. \eqref{eq:xp-npc}.

<figure id="fig:xp-encounter-diagram-example">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-xp-encounter-diagram-two-npcs.svg">
    <figcaption>Figure 1: Visual representation of Eqn. \eqref{eq:encounter-xp-npcs} for an encounter with two NPCs.</figcaption>
</figure>


# Single target strategies

The first type of strategy I'd like to discuss are single target strategies, where the PCs choose to use abilities that damage only one NPC at a time. The most straight forward of these strategies is one where the PCs all focus on defeating a single NPC before moving on to the next one.

As a simple example of this kind of strategy, consider an encounter with only two NPCs, which I'll refer to as NPC 1 and NPC 2. The total encounter XP for these NPCs can be written out in full as,

\begin{align}
    \eXPtot_\mathrm{NPCs} &= \W_{1,1}\cdot\XP_{1,1} + \W_{2,1}\cdot\XP_{2,1} \nonumber \\\\ 
                          &+ \W_{1,2}\cdot\XP_{1,2} + \W_{2,2}\cdot\XP_{2,2}\,.
    \label{eq:encounter-xp-two-npcs-general}
\end{align}

This is visualized in the encounter diagram shown in Fig. <a href="#fig:xp-encounter-diagram-example" class="fig-ref">1</a> from the previous section.

The first and last terms are just the individual XPs for each NPC, $$\W_{1,1} = \W_{2,2} = 1$$, which leave only weights for middle two group XP terms, $$\W_{2,1}$$ and $$\W_{1,2}$$, that need to be determined.

Taking a look at $$\XP_{2,1}$$ first, recall that this represents the average damage NPC 1 can be expected to do in the time it takes the PCs to defeat NPC 2. Similarly, $$\XP_{2,1}$$ represents the average damage NPC 2 can be expected to do in the time it takes the PCs to defeat NPC 1.

If the PCs choose to focus all of their damage on defeating NPC 1 first, then NPC 2 will get to gain the full benefit of $$\XP_{1,2}$$ while NPC 1 won't gain any benefit from $$\XP_{2,1}$$. Therefore, if NPC 1 is defeated first, $$\W_{2,1} = 0$$ and $$\W_{1,2} = 1$$. Similarly, if NPC 2 is defeated first $$\W_{2,1} = 1$$ and $$\W_{1,2} = 0$$.

For our example encounter with only two NPCs, if the PCs choose to focus on defeating one NPC and then the other,

\begin{equation}
    \eXPtot_\mathrm{NPCs} = 
    \begin{cases} 
        \XP_{1,1} + \XP_{1,2} + \XP_{2,2} & \NPC\,1\ \mathrm{first}\,; \\\\ 
        \XP_{1,1} + \XP_{2,1} + \XP_{2,2} & \NPC\,2\ \mathrm{first}\,.
    \end{cases}
    \label{eq:encounter-xp-two-npcs-focused}
\end{equation}

These two scenarios are visualized in Fig. <a href="#fig:xp-encounter-diagram-single" class="fig-ref">2</a> below, where the area of the blue regions represent the XP that contributes to the total encounter XP from \eqref{eq:encounter-xp-two-npcs-focused}.

<figure class="half" id="fig:xp-encounter-diagram-single">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-xp-encounter-diagram-two-npcs-forward.svg">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-xp-encounter-diagram-two-npcs-reverse.svg">
    <figcaption>Figure 2: Graphical representation of the total encounter XP contributions for the two strategies described by Eqn. \eqref{eq:encounter-xp-two-npcs-focused}. The blue regions represent the XP that contributes to the total encounter XP for each strategy.</figcaption>
</figure>

Applying this strategy more generally, in encounters where the PCs choose to focus on defeating one NPC at a time, each NPC will only add extra XP to the encounter for the NPC that were defeated before it. In terms of Eqn. \eqref{eq:encounter-xp-npcs}, the total encounter XP can be calculated by arranging the NPCs in the order they are expected to be defeated in and applying the following weights to each term,

\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 & i \geq j\,; \\\\ 
        0 & i \lt j\,.
    \end{cases}
    \label{eq:encounter-weights-single-target-focused}
\end{equation}

For encounters where there is no obvious order the NPCs will be defeated in, it can be useful to look at the total encounter XP averaged across all possible orders. Performing this average yields,

\begin{equation}
    \eXPtot_\mathrm{NPCs} = \frac{ \sum_{i, j} \XP_{ij}  + \sum_{i} \XP_{i}}{2}\,,
    %\overline{\aXP}_{\rm NPCs} = \frac{\left( \sum \NeHP \right) \cdot \left( \sum \NeDPR \right) + \sum \NeHP \NeDPR}{8}\,,
    \label{eq:adjusted-experience-average}
\end{equation}

or half the sum of the the maximum total encounter XP and the total XP for the NPCs. The weights needed to produce this result from Eqn. \eqref{eq:encounter-xp-npcs} are,

\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 & i = j\,; \\\\ 
        \frac{1}{2} & i \neq j\,.
    \end{cases}
    \label{eq:encounter-weights-single-target-average}
\end{equation}

For a group of $$N$$ identical NPCs, putting Eqn. \eqref{eq:adjusted-experience-average} into Eqn. \eqref{eq:encounter-multiplier-short-simple} gives an encounter multiplier of

\begin{align}
    \EM = \frac{\left(N + 1\right)}{2}\,.
    \label{eq:encounter-multiplier-approx-single-target}
\end{align}

This is plotted in Fig. <a href="#fig:encounter-multiplier-approx-single" class="fig-ref">3</a> below for a range of NPC group sizes.

<figure id="fig:encounter-multiplier-approx-single">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-encounter-approximate-general-single-target.svg">
    <figcaption>Figure 3: Encounter multiplier for single target strategies calculated using Eqn. \eqref{eq:encounter-multiplier-approx-single-target} for identical NPCs.</figcaption>
</figure>

For groups of three NPCs or fewer, this single target encounter multiplier matches what's given by the DMG exactly. However, for more than three NPCs the single target strategy clearly predicts a harder encounter than the DMG does. In order to bring the encounter multiplier down, strategies that target multiple NPCs at once are needed.

<!--
## Single target approximations

Without knowing $$\eHP$$ and $$\eDPR$$ for each creature in an encounter, Eqn. \eqref{eq:adjusted-experience-average} can be approximated as

\begin{equation}
    \aXP \approx \frac{\left(\sum\_{i} \XP^{1/2}_i\right)^2 + \sum\_{i} \XP_i}{2}\,,
\end{equation}

where each summation is over all individual NPCs in the encounter.


For N identical NPCs this simplifies to 

\begin{equation}
    \aXP \approx \frac{N \left(N + 1\right)}{2} \XP\,,
\end{equation}


\begin{equation}
    \EM \approx \frac{N + 1}{2}\,,
\end{equation}
-->


<!--
Of course, defeating each NPC one at a time is not the only option available to the PCs. The PCs can also damage multiple NPCs simultaneously using area of effect spells and abilities. Under these circumstances, the time it takes the PCs to defeat certain NPCs may not increase the damage of others because they take similar damage at the same time. 

In the extreme case, where all NPCs are defeated simultaneously and in similar time as they would be if faced individually, there is no additional $$\XP$$ and the adjusted $$\XP$$ total for the encounter is simply the sum of the individual $$\XP$$ for each NPC. In this way, the sum of the individual $$\XP$$ for each NPC in the encounter can be thought of as a lower limit to an encounter's difficulty.

Since it's unlikely that the PCs will use area of effect attacks in encounters where single target attacks would be more efficient, the single target case can be treated as a practical upper limit to an encounter's difficulty. This can be used as a good check for determining when the encounter multiplier given by the [Encounter Multiplier](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#EvaluatingEncounterDifficulty) table from chapter 3 of the DMG (p. 82) is providing too much of a boost to the adjusted $$\XP$$ total of an encounter.

Combining these two previous observations, the average adjusted $$\XP$$ total for an encounter should fall somewhere between 

\begin{equation}
    \sum \XP_i \le \aXP \le \frac{ \sum \XP_{i, j}  + \sum \XP_{i}}{2}\,.
    \label{eq:adjusted-experience-range}
\end{equation}

When put in terms of the encounter multiplier for a party of four PCs this gives

\begin{equation}
    1 \le \EM \le \frac{1}{2}\left(1 + \frac{\sum \XP_{i, j} }{\sum \XP_{i}}\right)\,.
    \label{eq:encounter-multiplier-range}
\end{equation}

Without knowing $$\eHP$$ and $$\eDPR$$ for each creature in an encounter, Eqn. \eqref{eq:encounter-multiplier-range} can be approximated as

\begin{equation}
    1 \le \EM \lessapprox \frac{1}{2} \left( 1 + \frac{\left(\sum \XP^{1/2}\_i\right)^2}{\sum \XP_{i}} \right)\,,
    \label{eq:encounter-multiplier-range-approx}
\end{equation}

which depends only on the the individual $$\XP$$ values for each NPC in an encounter. For encounters with $$M$$ identical NPCs, Eqn. \eqref{eq:encounter-multiplier-range-approx} becomes $$1 \le \EM(M) \lessapprox (1 + M)/2$$.
-->

# Multiple target strategies

The next type of strategy I'd like to discuss are multi-target strategies, where the PCs use abilities capable of damaging multiple targets simultaneously. Because multi-target abilities damage multiple NPCs simultaneously, the way they affect the extra group XP added to an encounter is fundamentally different from what I covered previous for single target strategies.

The simplest type of multi-target strategy is one where the PCs damage all of the enemy NPCs equally and simultaneously for the entire encounter. To help build a basic understanding of how this strategy works, let's apply it to the example encounter with only two NPCs discussed in the previous sections and described by Eqn. \eqref{eq:encounter-xp-two-npcs-focused}.

If both NPCs are being damaged equally and simultaneously, then neither gains the benefit of living longer while the PCs focus on the others. As a result, neither NPC contributes extra group XP to the encounter, which means $$\W_{2,1} = \W_{1,2} = 0$$. This leaves just the weights for the individual XP terms in Eqn. \eqref{eq:encounter-xp-two-npcs-focused}, $$\W_{1,1}$$ and $$\W_{2,2}$$, that need to be calculated.

For these individual XP terms, one might naively assume that $$\W_{1,1} = \W_{2,2} = 1$$, in which case the total encounter XP would be equal to the total XP for the two NPCs in the encounter. This would be equivalent to two separate encounters where NPC 1 and NPC 2 were both fought alone using single target abilities.

If NPCs 1 and NPC 2 survive equally long in both encounter then this makes sense. However, since multi-target abilities generally deal less damage per target than their single target counterparts, this is unlikely to be the case. Because of this, both NPCs are likely to live longer when fought together using multi-target abilities than they are when fought separately using single target abilities.

<figure id="fig:xp-encounter-diagram-multiple">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-xp-encounter-diagram-two-npcs-multi-uniform.svg">
    <figcaption>Figure 4: Graphical representation of the total encounter XP contributions for two NPCs damaged simultaneously using multi-target abilities. Red regions represent the XP contributing to the total encounter XP using this strategy.</figcaption>
</figure>

If we assume that the PCs' multi-target abilities deal only a fraction of the damage of their single target abilities to each target, then we can define an efficiency value for PCs' multi-target damage in the following way, 

\begin{equation}
    \effMT = \frac{\eDPRMT\_\mathrm{PCs}}{\eDPRST\_\mathrm{PCs}}\,,
\end{equation}

where $$\eDPRMT_\mathrm{PCs}$$ is the average effective DPR per target for the PCs' multi-target abilities, and $$\eDPRST_\mathrm{PCs}$$ is the average effective DPR for the PCs' single target abilities.

How much longer each NPC is expected to survive can be calculated from the inverse of this, $$1/\effMT$$, which means the value of each NPC's individual XP terms is

\begin{align}
    \W\_{ii}\cdot\XP\_{ii} &= \frac{1}{4}\left(\frac{\eHP\_{i}}{\effMT}\right)\cdot \eDPR\_{i} \nonumber \\\\ 
    &= \frac{\XP\_{ii}}{\effMT}\,.
    %\label{eq:npc-xp-prime}
\end{align}

<!--
How much longer each NPC survives can be accounted for through their effective hit points in the following way,

\begin{equation}
    \eHP\_{\,\NPC}^{\,\prime} = \frac{\eHP\_{\,\NPC}}{\effMT}\,,
    \label{eq:effective-hp-prime}
\end{equation}

where $$\effMT$$ is the PCs' multi-target damage efficiency,

\begin{equation}
    \effMT = \frac{\eDPR_\mathrm{MT}}{\eDPR_\mathrm{ST}}\,, 
\end{equation}

and where $$\eDPR_\mathrm{MT}$$ is the effective DPR per target for the PCs' multi-target abilities, and $$\eDPR_\mathrm{ST}$$ is the effective DPR for the PCs' single target abilities.

Inserting Eqn. \eqref{eq:effective-hp-prime} into Eqn. \eqref{eq:xp-npc} gives the new individual XPs for each NPC,

\begin{equation}
    \XP\_{\,\NPC}^{\,\prime} = \frac{\XP\_{\,\NPC}}{\effMT}\,.
    \label{eq:npc-xp-prime}
\end{equation}
-->

With this, the total encounter XP for our two NPC example encounter is 

\begin{equation}
    %\eXPtot_\mathrm{NPCs} = \frac{1}{\effMT} \left(\XP_{1,1} + \XP_{2,2}\right)\,.
    \eXPtot_\mathrm{NPCs} = \frac{\XP_{1,1} + \XP_{2,2}}{\effMT}\,.
    \label{eq:encounter-xp-two-npcs-multi-target}
\end{equation}

Applied to the general case, the total encounter XP for this sort of multi-target strategy can be calculated using Eqn. \eqref{eq:encounter-xp-npcs} along with the following weighting,

\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        \frac{1}{\effMT} & i = j\,; \\\\ 
        0 & i \neq j\,,
    \end{cases}
    \label{eq:encounter-weights-multi-target-equal}
\end{equation}

which simplifies to just the total XP for the NPCs in the encounter divided by the PCs' multi-target damage efficiency,

\begin{equation}
    \eXPtot_\mathrm{NPCs} = \frac{\XPtot_\mathrm{NPCs}}{\effMT}\,.
    \label{eq:encounter-xp-general-multi-target}
\end{equation}

The encounter multiplier for this kind of multi-target strategy, therefore, is simply,

\begin{equation}
    \EM = \frac{1}{\effMT}\,.
    \label{eq:encounter-multiplier-general-multi-target}
\end{equation}

Figure <a href="#fig:xp-encounter-multiplier-aoe" class="fig-ref">5</a> (below), plots this encounter multiplier as a function of the multi-target damage efficiency.

<figure id="fig:xp-encounter-multiplier-aoe">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-encounter-multiplier-general-multi-target.svg">
    <figcaption>Figure 5: Encounter multiplier for multi-target strategies that damage all enemies equally and simultaneously as a function of multi-target damage efficiency.</figcaption>
</figure>

Using the [Spell Damage](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#SpellDamage) table in chapter 9 of the DMG as a reference gives $$\effMT \approx 0.70$$ for spells, which translates to $$\EM \approx 1.43$$. Against monsters who are resistant to spell damage, or the specific damage type dealt by the PCs' spells, this changes to $$\effMT \approx 0.35$$ and $$\EM \approx 2.86$$, assuming the single target alternatives aren't effected by those same resistances. 

# Mixed strategies

While the multi-target strategy used in previous section is certainly efficient, it's also impractical in a lot of situations. Most abilities that deal damage to multiple targets do so by affecting creatures within a specific area, known as an area of effect (AoE). These AoE abilities can often be used effectively at the start of combat, but lose their effectiveness as time goes on as the number of NPCs decreases and the PCs and NPC get more and more intermingled. For this reason, another common strategy is for the PCs to begin the encounter using multi-target AoE abilities and then transition to a single target strategy part way through the encounter.

Just like in the previous section, under this strategy each NPC in the encounter takes an equal amount of effective damage simultaneously from multi-target abilities. However, unlike in the previous section, that damage is limited to a specific amount per target, denoted by $$\eDPTMT$$, before the PCs transition to single target damage. The amount of damage done to each NPC via single target abilities is therefore,

\begin{equation}
    \eDPTST_{i} = \eHP_{i} - \eDPTMT\,.
    \label{eq:effective-dpt-single}
\end{equation}

Since multi-target effects typically deal less damage per target than their single target counterparts, each NPC's individual XP values will be increased, similarly to how they were in the previous section. However, the size of the increase will be smaller due to the multi-target damage taking up a smaller fraction of the total damage they receive.

Applying this to each NPC's individual XP contribution to the total encounter XP yields

\begin{align}
    \W_{ii} \cdot \XP_{ii} &= \frac{1}{4} \left(\eDPTST_{i} + \frac{\eDPTMT}{\effMT}\right) \eDPR_{i} \nonumber \\\\ 
    &= \frac{1}{4} \left(\eHP_{i} - \eDPTMT + \frac{\eDPTMT}{\effMT}\right) \eDPR_{i} \nonumber \\\\ 
    &= \frac{1}{4} \eHP_{i} \cdot \eDPR_{i} \left(1 - \frac{\eDPTMT}{\eHP_{i}} + \frac{\eDPTMT}{\eHP_{i} \cdot \effMT}\right) \nonumber \\\\ 
    &= \XP_{ii} \left(1 - \dMTi + \frac{\dMTi}{\effMT}\right)\,.
    \label{eq:encounter-xp-mixed-individual}
\end{align}

Here, $$\dMTi = \eDPTMT/\eHP_{i}$$ is the ratio of the effective damage per target done by the multi-target effects and the given NPC's effective hit points. Since the amount of effective damage an NPC takes can't exceed their total effective hit points, $$0 \le \dMTi \le 1$$.

This covers the contributions from each of the NPC's individual XP, when $$i = j$$, but what about the extra group XP, when $$i \neq j$$?

From the previous section, we know that an NPC doesn't contribute any extra group XP when another NPC is damaged, if it's damaged at the same time. Since all of the NPCs are damaged simultaneously in this strategy, only the remaining single target damage is able to contribute extra group XP to the encounter in this way. 

Ignoring the order the NPCs are dealt with using single target abilities, the maximum contribution these terms can have is,

\begin{align}
    \W_{ij} \cdot \XP_{ij} &= \frac{1}{4} \eDPTST_{i} \cdot \eDPR_{j} \nonumber \\\\ 
    &= \frac{1}{4} \left( \eHP_{i} - \eDPTMT \right) \eDPR_{j} \nonumber \\\\ 
    &= \frac{1}{4} \eHP_{i} \cdot \eDPR_{j} \left(1  - \frac{\eDPTMT}{\eHP_{i}} \right) \nonumber \\\\ 
    &= \XP_{ij} \left(1 - \dMTi\right)\,.
    \label{eq:encounter-xp-mixed-group}
\end{align}

To help visualize all of this, Fig. <a href="#fig:xp-encounter-diagram-mixed" class="fig-ref">6</a> below show an encounter diagram for our example encounter with two NPCs with a mixed strategy applied to them where NPC 1 is defeated first.

<figure id="fig:xp-encounter-diagram-mixed">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-xp-encounter-diagram-two-npcs-mixed-forward.svg">
    <figcaption>Figure 6: Graphical representation of the total encounter XP contributions for two NPCs using a mixed strategy. Red regions represent the XP added to the encounter using multi-target abilities at the start of the encounter, and blue regions represent the XP added to the encounter using single target abilities.</figcaption>
</figure>

Before I bring this all together, there is one additional subtlety that needs to be addressed. If $$\eHP_{i} \le \eDPTMT$$ for one of the NPCs in the encounter, then the multi-target damage was enough to defeat them and they aren't able to contribute any extra group XP to the encounter due to being in a group, nor are the other NPCs able to benefit from being in a group with them as well.

With that in mind, if the order the NPCs will be focused after switching to single target abilities is known, the total encounter XP for this sort of mixed strategy can be calculated using Eqn. \eqref{eq:encounter-xp-npcs} by arranging the NPCs in the order they will be defeated in, with the following weights applied,

\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 - \dMTi + \frac{\dMTi}{\effMT} & i = j\,; \\\\ 
        %0 & i < j \ \mathrm{or}\ \dMTi \ge 1\ \mathrm{or}\ \dMTj \ge 1\,; \\\\ 
        0 & i < j\,; \\\\ 
        0 & \dMTj = 1\,; \\\\ 
        1 - \dMTi & \mathrm{otherwise}\,.
    \end{cases}
    \label{eq:encounter-weights-mixed-target-ordered}
\end{equation}

And, if the order is not known, the average total encounter XP can be calculated using Eqn. \eqref{eq:encounter-xp-npcs} along with the following weighting,

\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 - \dMTi + \frac{\dMTi}{\effMT} & i = j\,; \\\\ 
        0 & \dMTj = 1\,; \\\\ 
        \frac{1 - \dMTi}{2} & \mathrm{otherwise}\,.
    \end{cases}
    \label{eq:encounter-weights-mixed-target-average}
\end{equation}

It's worth noting that if $$\dMTi = 0$$ for all NPCs then Eqns. \eqref{eq:encounter-weights-mixed-target-ordered} and \eqref{eq:encounter-weights-mixed-target-average} are equal to their single target strategy equivalents, Eqns. \eqref{eq:encounter-weights-single-target-focused} and \eqref{eq:encounter-weights-single-target-average}. And, if $$\dMTi = 1$$ for all NPCs then Eqns. \eqref{eq:encounter-weights-mixed-target-ordered} and \eqref{eq:encounter-weights-mixed-target-average} are both equal to the multi-target weights given by Eqn. \eqref{eq:encounter-weights-multi-target-equal}.

For a group of $$N$$ identical NPCs, putting Eqn. \eqref{eq:encounter-weights-mixed-target-average} into Eqn. \eqref{eq:encounter-multiplier-short-simple} gives an encounter multiplier of

\begin{align}
    \EM = \frac{\left(N + 1\right) \left(1 - \dMTi\right)}{2} + \frac{\dMTi}{\effMT}\,.
    \label{eq:encounter-multiplier-approx-mixed-target}
\end{align}

<figure id="fig:encounter-multiplier-approx-mixed">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p1/fig-encounter-multiplier-approx-mixed-target.svg">
    <figcaption>Figure 7: Encounter multiplier for several mixed target strategies calculated using Eqn. \eqref{eq:encounter-multiplier-approx-single-target} for identical NPCs with multi-target damage efficiency of 70%.</figcaption>
</figure>

This encounter multiplier is plotted in Fig. <a href="#fig:encounter-multiplier-approx-mixed" class="fig-ref">7</a> (above) for $$\effMT = 0.7$$ and for several values of $$\dMTi$$. For $$N > 3$$ and $$\effMT = 0.7$$, the encounter multiplier given by the DMG falls between a multi-target damage efficiency of $$50\%$$ and $$75\%$$. This means the encounter multiplier given by the DMG assumes the PCs are able to rather effectively deal multi-target damage in combat with large numbers of enemies. For groups that have weak AoE damage capabilities, encounter difficulties calculated using the encounter multiplier in the DMG will likely underestimate the encounter's difficulty by as much as $$50\%$$.

# Conclusion

As this post has hopefully shown, there is a lot going on behind the scenes regarding the encounter multiplier, and how a group of PCs choose to engage an encounter, or how and encounter is set up by the DM can have a huge impact on the overall difficulty. 

The strategies I've shown here are the simplest each category has to offer, and there are other types of strategies I haven't even touched on, such as using abilities to incapacitate one or more of the NPCs for some part of the encounter. And I still need to address how the number of PCs and how the DM chooses to play the NPCs impacts the encounter difficulty, which I plan to cover in [part 2]({{ site.url }}{{ site.baseurl }}{% link _theory/encounter-multiplier-p2.md %}).

All of this is to say, I've really just scratched the surface of this topic.