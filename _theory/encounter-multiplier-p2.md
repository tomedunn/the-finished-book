---
title: "Calculating the Encounter Multiplier: part 2"
excerpt: "A deep dive into the encounter multiplier and how it depends on the number of PCs and NPC strategies."
date: 2022-3-14
last_modified_at: 2022-9-8
#tags:
#  - theory
#  - monsters
#  - encounters
---

{% include LaTex.html %}

<div style="display:none">
\(
% other
\newcommand{\XPwt}{\XP^{\,\weighted}}
\newcommand{\XPtot}{\XP^{\,\total}}
\newcommand{\effMT}{\mathit{eff}^{\,\mathrm{MT}}}
\newcommand{\dMT}{\mathit{d}}
\newcommand{\dMTi}{\dMT_{\mspace{2mu}i}}
\newcommand{\dMTj}{\dMT_{\mspace{2mu}j}}
\)
</div>

# Introduction

In [Calculating the Encounter Multiplier: part 1]({{ site.url }}{{ site.baseurl }}{% link _theory/encounter-multiplier-p1.md %}), I showed how the encounter multiplier depends on the number of enemy NPCs, as well as on the tactics used by the PCs. This gave way to a wide range of possible values the encounter multiplier could take, but it was only half of the picture.

In this post, I will be covering the other half of the encounter multiplier by looking at how the number of PCs affects it, as well as how the DM's strategy does while controlling the enemy NPCs.

# Calculating the encounter multiplier

From [XP and Encounter Balancing]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}), the general equation for calculating the encounter multiplier is
\begin{equation}
    \EM = \left( \frac{ \XPwt_{\NPCs} }{ \XPtot_{\NPCs} } \right) 
    \cdot \left( \frac{ 4\,\XPtot_{\PCs} }{ \XPwt_{\PCs} } \right) \,,
    \label{eq:encounter-multiplier-short}
\end{equation}
where $$\XPtot$$ is the total XP for either the PCs or NPCs, and $$\XPwt$$ is the weighted XP total for the encounter for either the PCs or NPCs.

Since I covered the first term in Eqn. \eqref{eq:encounter-multiplier-short} in part 1, in this post I'll focus on the second term,
\begin{equation}
    \EM = \left( \frac{ 4\,\XPtot_{\PCs} }{ \XPwt_{\PCs} } \right) \,,
    \label{eq:encounter-multiplier-short-simple}
\end{equation}
which is what Eqn. \eqref{eq:encounter-multiplier-short} simplifies to for encounters with only a single enemy NPC. The total XP for the PCs, $$\XPtot_{\PCs}$$, is independent of how the NPCs choose to engage, which means the only term that needs to be considered is the total encounter XP for the PCs, 
\begin{align}
    \XPwt_{\PCs} &= \sum_{i,j} \W\_{\,\PC\_{ij}} \cdot \XP\_{\,\PC\_{ij}}\,.
    \label{eq:encounter-xp-pcs}
\end{align}

The XP terms in the summation on the RHS of Eqn. \eqref{eq:encounter-xp-pcs} are calculated from the effective hit points $$(\eHP\,)$$ and the effective damage per round $$(\eDPR\,)$$ of the PCs in the encounter, 
\begin{equation}
    \XP_{\,\PC_{ij}} = \eHP_{\,\PC_{i}} \cdot \eDPR_{\,\PC_{j}}\,,
    \label{eq:xp-pc}
\end{equation}
and represents the average damage that PC $$\mathit{j}$$ is capable of doing in the time it takes PC $$\mathit{i}$$ to be defeated. The remaining term, $$\W_{\,\PC}$$, weights each of these XP contributions, and depends on the strategy the NPCs take during the encounter. 

Just as in part 1, the real challenge here comes from determining $$\W_{\,\PC}$$ for each terms in Eqn. \eqref{eq:encounter-xp-pcs}.

# PC group size and NPC strategies

The strategies available to NPCs in combat encounters mirror those available to PCs, which I covered in depth in part 1, but with two major differences that need to be accounted for.

The first of these differences has to do with multi-target strategies available to the NPCs. When calculating an NPC's average damage per round, abilities that are capable of damaging multiple targets simultaneously are assumed to affect a fixed number of creatures. 

For example, the Acid Breath action of a **[black dragon wyrmling](https://www.dndbeyond.com/monsters/black-dragon-wyrmling)** deals 22 (5d8) damage to each target that fails its saving throw. From the [Monster Features](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterFeatures) table in chapter 9 of the DMG, when calculating the wyrmling's average DPR the breath is assumed to affect two creatures, which means it contributes 45 (10d8) damage for one round to the wyrmling's average DPR instead of 22 (5d8).

Adjusting the encounter multiplier to account for the NPCs' multi-target strategies would, therefore, double count their impact on the encounter's difficulty. To avoid this double counting, only single target strategies should be considered for the NPCs when determining the weighting for Eqn. \eqref{eq:encounter-xp-pcs}. If the average number of creatures affected by monster multi-target abilities increases, the best way of accounting for this would be to recalculate those monsters' CRs.

The second difference has to do with how likely the NPCs are to defeat the PCs and win the encounter.

When calculating the encounter multiplier in part 1, it was assumed that some NPCs would live longer than others, and would therefore contribute more XP to the encounter as a result. This made sense because, in the vast majority of combat encounters, all enemy NPCs are defeated. However, the same can't be said for the PCs.

Since the PCs win nearly all encounters, they survive through most encounters as well. In fact, it's uncommon for a PC to be knocked unconscious during an encounter, and rare for one to be killed or taken out permanently. Going off of the descriptions for the different encounter difficulty categories, it's not until the difficulty reaches Deadly that the likelihood of one or more of the PCs dying in combat becomes significant. This means for most encounters $$\W_{\,\PC_{ij}} = 1$$ and   
\begin{align}
    \XPwt_{\PCs} = \sum_{i,j} \XP\_{\,\PC\_{ij}}\,.
    \label{eq:encounter-xp-pcs-simple}
\end{align}

For PCs who are all the same level, i.e., identical PCs,
\begin{align}
    \XPwt_{\PCs} = N^2 \cdot \XP\_{\,\PC}\left(\LV\right)\,,
    \label{eq:encounter-xp-pcs-simple-identical}
\end{align}
where $$\LV$$ is the PCs' level. When put into Eqn. \eqref{eq:encounter-multiplier-short-simple}, this gives an encounter multiplier of
\begin{align}
    %\EM &= 4 \left( \frac{ N \cdot \XP\_{\,\PC}\left(\LV\right) }{ N^2 \cdot \XP\_{\,\PC}\left(\LV\right) } \right) \nonumber \\\\ 
    %    &= \frac{ 4 }{ N }\,.
    \EM &= \frac{ 4 }{ N }\,.
    \label{eq:encounter-multiplier-short-identical}
\end{align}

It's worth pointing out here, that PCs of the same level generally aren't worth the same amount of XP (see [Player Character XP]({{ site.url }}{{ site.baseurl }}{% link _classes/xp-and-player-characters.md %})). However, for parties with a mix of martial and spellcasting PCs, they can still be treated as such when the risk of any PCs dying or being knocked unconscious is low.

To verify that Eqn. \eqref{eq:encounter-multiplier-short-identical} is accurate, Fig. <a href="#fig:encounter-multiplier-vs-pcs" class="fig-ref">1</a> (below) plots the encounter multiplier against the number of PCs using the sensitivities from the [Encounter Multipliers](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#EvaluatingEncounterDifficulty) table in chapter 13 of the _Basic Rules_, and using Eqn. \eqref{eq:encounter-multiplier-short-identical}, which is scaled up for the encounters shown with 7 and 15 NPCs, to account for the impact that multiple enemy NPCs have on the encounter multiplier.

<figure id="fig:encounter-multiplier-vs-pcs">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p2/fig-em-vs-pcs.svg">
    <figcaption>Figure 1: Encounter multiplier vs the number of PCs calculated using the <a href="https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#EvaluatingEncounterDifficulty">Encounter Multipliers</a> table in chapter 13 of the <i>Basic Rules</i> (solid lines) and with scaling using Eqn. \eqref{eq:encounter-multiplier-short-identical} (dashed lines).</figcaption>
</figure>

The two methods are in fairly good agreement for encounters with a single NPC, but match less and less well as the number of NPCs increases. If Eqn. \eqref{eq:encounter-multiplier-short-identical} is to be believed, the encounter multiplier in the DMG generally over-estimates the difficulty of encounter for groups of six or more PCs, generally under-estimates the difficulty for groups of two PCs, and significantly underestimates it for groups with only a single PC.

Given the way the DMG adjusts the encounter multiplier for the number of PCs, this level of disagreement isn't entirely unexpected. Rather than having a matrix of encounter multiplier values for various combinations of PC and NPC group sizes, the DMG only provides values for groups of three to five PCs, and then offers broad adjustments for extending those rules to groups of PCs outside of that range.

In other words, given the sheer simplicity of how the DMG chooses to adjust the encounter multiplier to account for different numbers of PCs, there are bound to be large inaccuracies in the values it gives for group sizes outside the range it explicitly covers.

For encounters with only one PC and one NPC there is no need to consider single or multi-target strategies, or make approximations. The total encounter XP is always equal to the individual XP for each side, i.e., $$\XPwt_{\PCs} = \XP_{\PC_1}$$ and $$\XPwt_{\NPCs} = \XP_{\NPC_1}$$. The encounter multiplier given by Eqn. \eqref{eq:encounter-multiplier-short} for these encounters is simply $$\EM = 4$$, which is nearly three times larger than the value of $$1.5$$ given by the DMG.

Of course, one could argue that the factor of 4 in Eqn. \eqref{eq:encounter-multiplier-short-identical} might simply be incorrect, but given how well that same factor worked for [Calculating Monster XP]({{ site.url }}{{ site.baseurl }}{% link _monsters/calculating-monster-xp.md %}) this is unlikely to be the case. 

# Single target strategies and difficult encounters

The assumption that none of the PCs are defeated during an encounter works well for Easy and Medium difficulty encounters, but breaks down somewhat for Hard encounters, and more significantly for Deadly encounters, where the chance of the PCs being defeated is substantially higher. To account for this, lets looks at how Eqn. \eqref{eq:encounter-multiplier-short-simple} changes when the NPCs use a single target strategy and focus on defeating one only PC at a time.

Taking the results from the "Single target strategies" section for PCs in [part 1]({{ site.url }}{{ site.baseurl }}{% link _theory/encounter-multiplier-p1.md %}) and applying it to NPCs gives us insight into the worse case scenario for the PCs, where the PCs are defeated one at a time until the NPCs defeat them.

The total encounter XP for the PCs under this scenario can be calculated by arranging the PCs in the order they are expected to be defeated in and applying the following weights,
\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 & i \leq j\,; \\\\ 
        0 & i \gt j\,.
    \end{cases}
    \label{eq:encounter-weights-single-target-focused}
\end{equation}

Figure <a href="#fig:xp-encounter-diagram-three-pcs-single-target" class="fig-ref">2</a> (below) provides a visual representation of Eqn. \eqref{eq:encounter-xp-pcs} using these weights for a party of three PCs.

<figure id="fig:xp-encounter-diagram-three-pcs-single-target">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p2/fig-xp-encounter-diagram-three-pcs-single-target.svg">
    <figcaption>Figure 2: PC encounter XP diagram for party with three identical PCs defeated in order. Blue regions represent the XP that contributes to the total encounter XP.</figcaption>
</figure>

When the order isn't known, the average total encounter XP can instead be calculated using the following weighting,
\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 & i = j\,; \\\\ 
        \frac{1}{2} & i \neq j\,.
    \end{cases}
    \label{eq:encounter-weights-single-target-average}
\end{equation}

For a party of $$N$$ PCs, all level $$\LV$$, putting Eqn. \eqref{eq:encounter-weights-single-target-average} into Eqn. \eqref{eq:encounter-xp-pcs} gives a total encounter XP of
\begin{align}
    \XPwt_{\PCs} = \frac{N\left(N + 1\right)}{2} \XP\_{\,\PC}\left(\LV\right)\,,
    \label{eq:encounter-xp-pcs-single-target-identical}
\end{align}
which leads to the encounter multiplier,
\begin{align}
    \EM = \frac{8}{N + 1}\,.
    \label{eq:encounter-multiplier-approx-single-target}
\end{align}

Taking the ratio of Eqn. \eqref{eq:encounter-multiplier-approx-single-target} and Eqn. \eqref{eq:encounter-multiplier-short-identical} results in
\begin{align}
    \left(\frac{8}{N + 1}\right) \left(\frac{ N }{ 4 }\right) = \frac{2\,N}{N + 1}\,,
    \label{eq:encounter-multiplier-approx-single-ratio}
\end{align}
which tells us how much the encounter multiplier might increase by having the NPCs use a focused single target strategy. The results of Eqn. \eqref{eq:encounter-multiplier-approx-single-ratio} are plotted in Fig. <a href="#fig:single-target-em-ratio-vs-pcs" class="fig-ref">3</a> (below).

<figure id="fig:single-target-em-ratio-vs-pcs">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p2/fig-single-target-em-ratio-vs-pcs.svg">
    <figcaption>Figure 3: Plots the ratio between the encounter multipliers given by Eqn. \eqref{eq:encounter-multiplier-approx-single-target} and Eqn. \eqref{eq:encounter-multiplier-short-identical}.</figcaption>
</figure>

For a party of four PCs, having the NPCs focus their damage on defeating only one PC at a time can increase the adjusted XP total for the encounter by as much as 60%. For reference, the Deadly encounter threshold is around 50% higher than the Hard encounter threshold on average. For Hard encounters, this means that how much the NPCs focus their damage can potentially increase the encounter's difficulty by one category.

This covers the worst case scenario for the PCs, but what about intermediate cases where only one or two PCs are defeated by the NPCs using a single target strategy? For the PCs who are defeated during the encounter, their contribution to the encounter XP will be the same as it would be under the previous single target scenario, and they will only contribute extra XP for the PCs who are defeated before them. Alternatively, for the PCs who aren't defeated, their contributions will be the same as in the previous section where all the PCs survived.

For an encounter where the NPCs are able to use a focused single target strategy to defeat $$n$$ PCs, the total encounter XP can be calculated by arranging the PCs in the order they will be defeated in and applying the following weighting,
\begin{equation}
    \W_{ij} = 
    \begin{cases} 
        1 & i \leq j\,; \\\\ 
        1 & i \gt j \;\mathrm{and}\; j \gt n\,; \\\\ 
        0 & i \gt j \;\mathrm{and}\; j \leq n\,.
    \end{cases}
    \label{eq:encounter-weights-single-target-focused-intermediate}
\end{equation}

A visual representation of Eqn. \eqref{eq:encounter-xp-pcs} using this weighting is shown in Fig. <a href="#fig:xp-encounter-diagram-pcs-single-target-partial" class="fig-ref">4</a> (below) for a party of four PCs with $$n = 2$$.

<figure id="fig:xp-encounter-diagram-pcs-single-target-partial">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p2/fig-xp-encounter-diagram-pcs-single-target-partial.svg">
    <figcaption>Figure 4: PC encounter XP diagram for party with four identical PCs where only two of the PCs are defeated during the encounter, PC 1 and PC 2. Blue regions represent the XP that contributes to the total encounter XP.</figcaption>
</figure>

Applied to a party of $$N$$ PCs, all with the same level, this gives a total encounter XP of 
\begin{align}
    \XPwt_{\PCs} = \frac{1}{2} \left(2N^2 - 2n \cdot N + n\left(n + 1\right)\right) \XP\_{\,\PC}\left(\LV\right)\,,
    \label{eq:encounter-xp-pcs-single-target-identical-general}
\end{align}
and an encounter multiplier of
\begin{align}
    \EM &= \frac{ 4 N \cdot \XP\_{\,\PC}\left(\LV\right) }{ \frac{1}{2} \left(2N^2 - 2n \cdot N + n\left(n + 1\right)\right) \XP\_{\,\PC}\left(\LV\right) } \nonumber \\\\ 
        &= \frac{ 8 N  }{ \left(2N^2 - 2n \cdot N + n\left(n + 1\right)\right) }\,.
    \label{eq:encounter-multiplier-single-target-identical-general}
\end{align}

Note that in the limiting case where $$n = 0$$, Eqn. \eqref{eq:encounter-multiplier-single-target-identical-general} gives the same result as Eqn. \eqref{eq:encounter-multiplier-short-identical}. And, on the other side of the spectrum, when $$n = N$$, Eqn. \eqref{eq:encounter-multiplier-single-target-identical-general} matches Eqn. \eqref{eq:encounter-multiplier-approx-single-target}.

To illustrate how the encounter difficulty changes as the number of PC deaths increases, Fig. <a href="#fig:single-target-em-ratio-vs-pcs-deaths" class="fig-ref">5</a> (below) plots the ratio between the encounter multipliers given by Eqn. \eqref{eq:encounter-multiplier-single-target-identical-general} and Eqn. \eqref{eq:encounter-multiplier-short-identical} for different party sizes.

<figure id="fig:single-target-em-ratio-vs-pcs-deaths">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/encounter-multiplier-p2/fig-single-target-em-ratio-vs-pcs-deaths.svg">
    <figcaption>Figure 5: Plots the ratio between the encounter multipliers given by Eqn. \eqref{eq:encounter-multiplier-single-target-identical-general} and Eqn. \eqref{eq:encounter-multiplier-short-identical} for different party sizes and number of PC deaths.</figcaption>
</figure>

# Conclusion

Just as in the part 1, when it comes to the number of PCs and NPC strategies, there is a lot more going on behind the scenes than it appears from the encounter balancing rules in the _Basic Rules_. For campaigns with parties of three or more PCs, the encounter multiplier provided by the DMG works reasonably well, so long as the PCs survive through encounters most of the time. When the number of PCs falls below three, or when the DM chooses to focus on killing only one PC at a time, the encounter multiplier given by the rules can significantly underestimate the encounter's difficulty.

<!--
# Putting it all together

\begin{align}
    %\EM &= \left(\frac{ 8 \NP  }{ \left(2\NP^2 - 2\nP \cdot \NP + \nP\left(\nP + 1\right)\right) }\right)\cdot\left(\frac{\left(\NN + 1\right) \left(1 - \dMTi\right)}{2} + \frac{\dMTi}{\effMT}\right)\,. \nonumber \\\\ 
    %\EM &= \left(\frac{ 8 \NP }{ \left(2\NP^2 - 2\nP \cdot \NP + \nP\left(\nP + 1\right)\right) }\right)\cdot\left(\frac{\effMT \left(\NN + 1\right) \left(1 - \dMTi\right) + 2 \dMTi}{2 \effMT}\right)\,. \nonumber \\\\ 
    \EM &= \frac{ 4 \NP \left( \effMT \left(\NN + 1\right) \left(1 - \dMTi\right) + 2 \dMTi \right) }{ \effMT \left(2\NP^2 - 2\nP \cdot \NP + \nP\left(\nP + 1\right)\right) } \,. 
    \label{eq:encounter-multiplier-full-approx-identical}
\end{align}
-->

