---
title: "XP and Encounter Balancing"
excerpt: "A detailed explanation of where XP comes from and how encounter balancing works."
permalink: /:collection/:name/
date: 2022-1-27
last_modified_at: 2022-4-18
tags:
  - encounter balancing
  - encounter multiplier
  - theory
  - xp
---

{% include LaTex.html %}

<div style="display:none">
\(
\newcommand{\eD}{\mathit{eD}}
\newcommand{\D}{\mathit{D}}
\newcommand{\d}{\mathit{d}}
% other
\newcommand{\diff}{\mathit{diff}}

% totals
\newcommand{\eHPtot}{\eHP^{\,\total}}
\newcommand{\eDtot}{\eD^{\,\total}}
\newcommand{\eDPRtot}{\eDPR^{\,\total}}
\newcommand{\XPtot}{\XP^{\,\total}}
\)
</div>

<!--
<div style="display:none">
\(
\newcommand{\RTW}{\mathit{RTW}}
\newcommand{\RND}{\mathit{R}}
\newcommand{\AC}{\mathit{AC}}
\newcommand{\eAC}{\mathit{eAC}}
\newcommand{\HP}{\mathit{HP}}
\newcommand{\eHP}{\mathit{eHP}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\eD}{\mathit{eD}}
\newcommand{\eDPR}{\mathit{eDPR}}
\newcommand{\D}{\mathit{D}}
\newcommand{\DPR}{\mathit{DPR}} 
\newcommand{\DPRhit}{\mathit{DPR}_\mathrm{h}} 
% other
\newcommand{\CR}{\mathit{CR}}
\newcommand{\LV}{\mathit{L}}
\newcommand{\XP}{\mathit{XP}}
\newcommand{\d}{\mathit{d}}
\newcommand{\diff}{\mathit{diff}}
\newcommand{\thresh}{\mathrm{th}}
\newcommand{\EM}{\mathit{EM}}
\newcommand{\W}{\mathit{W}}
% totals
%  - overline
%\newcommand{\eHPtot}{\overline{\eHP}}
%\newcommand{\eDtot}{\overline{\eD}}
%\newcommand{\eDPRtot}{\overline{\eDPR}}
%\newcommand{\XPtot}{\overline{\XP}}
%  - tot
\newcommand{\total}{\mathrm{tot}}
\newcommand{\weighted}{\mathrm{weighted}}
\newcommand{\eHPtot}{\eHP^{\,\total}}
\newcommand{\eDtot}{\eD^{\,\total}}
\newcommand{\eDPRtot}{\eDPR^{\,\total}}
\newcommand{\XPtot}{\XP^{\,\total}}
\newcommand{\eXPtot}{\mathrm{enc}\,\XPtot}
\newcommand{\aXPtot}{\mathrm{adj}\,\XPtot}
% NPCs
\newcommand{\NPC}{\mathrm{n}}
\newcommand{\NPCs}{\mathrm{n}}
%\newcommand{\NPC}{\mathrm{NPC}}
%\newcommand{\NPCs}{\mathrm{NPCs}}
\newcommand{\NRTW}{\RTW_\NPC}
\newcommand{\NeHP}{\eHP_\NPC}
\newcommand{\ND}{\D_\NPC}
\newcommand{\NeD}{\eD_\NPC}
\newcommand{\NeDPR}{\eDPR_\NPC}
\newcommand{\NXP}{\XP_\NPC}
\newcommand{\NRND}{\RND_\NPC}
% PCs
\newcommand{\PC}{\mathrm{p}}
\newcommand{\PCs}{\mathrm{p}}
%\newcommand{\PC}{\mathrm{PC}}
%\newcommand{\PCs}{\mathrm{PCs}}
\newcommand{\PRTW}{\RTW_\PC}
\newcommand{\PHP}{\HP_\PC}
\newcommand{\PeHP}{\eHP_\PC}
\newcommand{\PeDPR}{\eDPR_\PC}
\newcommand{\PXP}{\XP_\PC}
\newcommand{\PXPij}{\XP_{\PC_{ij}}}
\)
</div>

-->



# Introduction

Combat encounters are one of the cornerstones of D&D 5th edition which makes building encounters an essential skill for DMs. Chapter 13 of the _Basic Rules_, "[Building Combat Encounters](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters)", contains guidelines to help DMs balance and estimate the difficulty of their encounters. These guidelines work quite well, overall, but to a casual observer it's not entirely clear why they work the way they do. Why is XP used for balancing encounters instead of challenge rating (CR), and why do the monsters' XP need to be adjusted by an encounter multiplier?

In this post I will answer these questions by showing how encounter balancing rules can be derived from fundamental equations for how combat works, and how XP arises as a natural product of that derivation.

# Review

Before jumping into the [derivation](#derivation) in the next section, let's review how an encounter's difficulty is determined using the rules in chapter 13 of the _Basic Rules_. 

The basic process is relatively straight forward. 

1. Calculate the party's XP threshold $$(\XPtot_{\thresh})$$ for each difficulty category $$(\diff\,)$$ by adding together their individual [XP thresholds](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#XPThresholdsbyCharacterLevel) $$(\XP_{\thresh})$$, as determined by their level $$(\LV)$$, 
\begin{align}
    %\XPtot_{\PCs}\left(\diff\,\right) = \sum_{i=1}^{N_{\PC}} \PXP \left(\LV\_{i}, \diff\,\right)\,, \label{eq:xp-threshold-total-dmg}
    \XPtot_{\thresh}\left(\diff\,\right) = \sum_{i=1}^{N_{\PC}} \XP_{\thresh} \left(\LV\_{i}, \diff\,\right)\,, \label{eq:xp-threshold-total-dmg}
\end{align}
where $$N_{\PC}$$ is the number of PCs in the party.

2. Calculate the total XP for the enemy NPCs in the encounter $$(\XPtot_{\NPCs})$$ by adding together their individual [XP values](https://www.dndbeyond.com/sources/basic-rules/monsters#ExperiencePointsbyChallengeRating) $$(\XP_{\NPC})$$, as determined by their challenge rating $$(\CR\,)$$,
\begin{align}
    \XPtot_{\NPCs} = \sum_{i=1}^{N_{\NPC}} \XP_{\NPC} \left(\CR\_{i}\,\right)\,, \label{eq:xp-total-dmg}
\end{align}
where $$N_{\NPC}$$ is the number of enemy NPCs in the encounter.

3. Multiply $$\XPtot_{\NPCs}$$ by an encounter multiplier $$(\EM\,)$$, which depends on $$N_{\PC}$$ and $$N_{\NPC}$$.

4. Compare the adjusted XP value from the previous step against $$\XPtot_{\thresh}$$ for each $$\diff$$. The difficulty of the encounter is the highest $$\diff\,$$ that satisfies the inequality,
\begin{align}
    \XPtot_{\thresh}\left(\diff\,\right) \leq \EM\left(N_{\PC}, N_{\NPC}\right) \cdot \XPtot_{\NPCs} \,.
    \label{eq:encounter-balance-inequality-dmg}
\end{align}

Calculating $$\XPtot_{\thresh}$$ and evaluating Eqn. \eqref{eq:encounter-balance-inequality-dmg} for each $$\diff$$ to determine an encounter's difficulty is rather cumbersome. Thankfully, this process can be simplified to only a single calculation by noting that the XP thresholds at each level come in fixed ratios as shown in Fig. \figref{fig:pc-xp-thresholds-vs-level} (below).

<figure id="fig:pc-xp-thresholds-vs-level">
    {% include_relative fig-pc-xp-thresholds-vs-level-small.html %}
    {% include_relative fig-pc-xp-thresholds-vs-level-large.html %}
    <figcaption>Plots PC XP thresholds divided by the Easy difficulty XP threshold, taken from the <a href="https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters#XPThresholdsbyCharacterLevel">XP Threshold by Character Level</a> table in chapter 13 of the <i>Basic Rules</i>. The average ratio for each threshold is 1.0 for Easy, 2.0 for Medium, 3.0 for Hard, and 4.5 for Deadly encounters.</figcaption>
</figure>

By defining a reference XP value for the PCs at each level $$(\XP_{\PC})$$ that's also always a fixed ratio of the these threshold XP values, the fourth step can be replace with solving a single equation,
\begin{align}
    \d \cdot \XPtot_{\PCs} = \EM\left(N_{\PC}, N_{\NPC}\right) \cdot \XPtot_{\NPCs} \,, \label{eq:encounter-balance-equation-dmg}
\end{align}
for $$\d\,$$, and then comparing it against fixed values of $$\XP_{\thresh} / \XP_{\PC}$$ for each $$\diff$$ to determine an encounter's difficulty.

For example, using the Easy difficulty category as our reference, $$\XP_{\PC} = \XP_{\thresh}(\mathrm{Easy})$$, would yield $$\d = 1.0$$ for Easy encounters, $$\d = 2.0$$ for Medium encounters, $$\d = 3.0$$ for Hard encounters, and $$\d = 4.5$$ for Deadly encounters.

Replacing $$\XPtot_{\PCs}$$ and $$\XPtot_{\NPCs}$$ with their full summations, Eqn. \eqref{eq:encounter-balance-equation-dmg} becomes
\begin{align}
    \d \cdot \sum_{i=1}^{N_{\PCs}} \XP_{\PC_{i}} = \EM\left(N_{\PC}, N_{\NPC}\right) \cdot \sum_{i=1}^{N_{\NPCs}} \XP_{\NPC_{i}} \,, 
    \label{eq:encounter-balance-equation-full-dmg}
\end{align}
which will prove useful in the derivation that follows in the next section.

# Derivation

Reading through the descriptions for the game's four difficulty categories, it's clear that as encounter difficulty increases the party will take more damage and be forced to use more resources as a result. Because each class uses resources differently, it can be hard to quantify them in an absolute sense. Damage, on the other hand, is relatively easy to quantify. So, **for this derivation,lets use damage dealt to the PCs to define encounter difficulty**.

Thinking about encounter difficulty in terms of damage is convenient in that it gives us a hard range for how far we can push when challenging the PCs. If we think about the party as having some amount of effective hit points $$(\eHPtot_{\PCs})$$ then we'll want to keep the amount of effective damage dealt by the enemy NPCs $$(\eDtot_{\NPCs})$$ between
\begin{align}
    0 \lt \eDtot_{\NPCs} \lt \eHPtot_{\PCs}\,, \label{eq:effective-damage-inequality}
\end{align}
in order to keep the encounter challenging without being overwhelming. For a detailed discussion of what I mean by "effective hit points" and "effective damage", see [Effective HP and Damage]({{ site.data.page-links.effective-hp-and-damage.path }}), but you can think of them as simply hit points and damage for the time being.

If we divide each term in Eqn. \eqref{eq:effective-damage-inequality} by $$\eHPtot_{\PCs}$$, this simplifies to 
\begin{align}
    0 \lt \d \lt 1\,, \label{eq:effective-difficulty-inequality}
\end{align}
where $$\d$$ represents the encounter's difficulty and must satisfy the following "difficulty" equation,
\begin{align}
    \d \cdot \eHPtot_{\PCs} = \eDtot_{\NPCs}\,. 
    \label{eq:difficulty-definition}
\end{align}

<!--
where $$\d$$ represents the amount of damage the PCs are expected to take relative to their maximum health as well as the difficulty of the encounter.
-->

This is similar in form to Eqn. \eqref{eq:encounter-balance-equation-dmg} in an abstract sense, but it's not especially useful because, while $$\eHPtot_{\PCs}$$ is an easily calculable quantity, $$\eDtot_{\NPCs}$$ is not. To fix this, we want to rewrite Eqn. \eqref{eq:difficulty-definition} entirely in terms of effective hit points $$(\eHP\,)$$ and effective damage per round $$(\eDPR\,)$$, since both can be calculated fairly easily from a PC's character sheet or a NPC's stat block. 

We can do this by noting $$\eDtot_{\NPCs}$$ can be calculated from the total effective damage per round of the enemy NPCs $$(\eDPRtot_{\NPCs})$$ and the number of rounds it takes the enemy NPCs to be defeated by the PCs $$(\rounds_{\NPC})$$,
\begin{align}
    \eDtot_{\NPCs} = \eDPRtot_{\NPCs} \cdot \rounds_{\NPC}\,, 
    \label{eq:effective-damage}
\end{align}
and that $$\rounds_{\NPC}$$ can be calculated from the total effective hit points of the enemy NPCs $$(\eHPtot_{\NPCs})$$ and the total effective damage per round of the PCs $$(\eDPRtot_{\PCs})$$,
\begin{align}
    \rounds_{\NPC} = \frac{\eHPtot_{\NPCs}}{\eDPRtot_{\PCs}}\,. 
    \label{eq:npcs-rounds-to-lose}
\end{align}

Placing Eqns. \eqref{eq:effective-damage} and \eqref{eq:npcs-rounds-to-lose} into Eqn. \eqref{eq:difficulty-definition} and moving all the PC terms to the left-hand side of the equation, our difficulty equation becomes
\begin{align}
    \d \cdot \eHPtot_{\PCs} \cdot \eDPRtot_{\PCs} = \eHPtot_{\NPCs}  \cdot \eDPRtot_{\NPCs} \,. 
    \label{eq:effective-difficulty-eq}
\end{align}
This has a form much closer to Eqn. \eqref{eq:encounter-balance-equation-dmg} but the comparison starts to break down when we consider that each term, other than $$\d$$, is actually a summation over (potentially) many creatures,
\begin{align}
    \eHPtot_{\PCs}  &= \sum_{i=1}^{N_{\PC}} \eHP_{\PC_{i}}  \,,\ \eDPRtot_{\PCs} = \sum_{i=1}^{N_{\PC}} \eDPR_{\PC_{i}} \,; 
    \label{eq:ehp-edpr-total-pc} \\\\ 
    \eHPtot_{\NPCs}  &= \sum_{i=1}^{N_{\NPC}} \eHP_{\NPC_{i}}  \,,\ \eDPRtot_{\NPCs} = \sum_{i=1}^{N_{\NPC}} \eDPR_{\NPC_{i}} \,. 
    \label{eq:ehp-edpr-total-npc}
\end{align}
Using these to write out Eqn. \eqref{eq:effective-difficulty-eq} in full detail gives
\begin{align}
    \d \cdot \sum_{i,j = 1}^{N_{\PC}} \eHP_{\PC_{i}} \cdot \eDPR_{\PC_{j}} = \sum_{i,j = 1}^{N_{\NPC}} \eHP_{\NPC_{i}}  \cdot \eDPR_{\NPC_{j}} \,,
    \label{eq:effective-difficulty-eq-full}
\end{align}
where, unlike Eqn. \eqref{eq:encounter-balance-equation-full-dmg}, each side contains a double summation rather than a single one.

To help gain some insight into how Eqn. \eqref{eq:effective-difficulty-eq-full} maps to Eqn. \eqref{eq:encounter-balance-equation-full-dmg}, consider the simple example of an encounter with $$N_{\PCs}$$ identical PCs and $$N_{\NPCs}$$ identical enemy NPCs. Applying these conditions to Eqn. \eqref{eq:effective-difficulty-eq-full}, and performing only one of the summations on each side of the equation, yields
\begin{equation}
    \d \cdot \sum_{i = 1}^{N_{\PC}} \eHP_{\PC_{i}} \cdot \eDPR_{\PC_{i}} = \frac{ N_{\NPCs} }{ N_{\PCs} } \sum_{i = 1}^{N_{\NPC}} \eHP_{\NPC_{i}} \cdot \eDPR_{\NPC_{i}}\,.
    \label{eq:effective-difficulty-eq-simple}
\end{equation}

This simplifies things considerably, allowing Eqn. \eqref{eq:effective-difficulty-eq-simple} to be easily mapped to Eqn. \eqref{eq:encounter-balance-equation-full-dmg} via the following relationships:
\begin{gather}
    \XP_{\PC}   = \eHP_{\PC} \cdot \eDPR_{\PC}\,,                  \label{eq:xp-pc} \\\\ 
    \XP_{\NPC}  = \frac{1}{4} \eHP_{\NPC} \cdot \eDPR_{\NPC}\,,    \label{eq:xp-npc} \\\\ 
    \EM         = \frac{ 4\, N_{\NPCs} }{ N_{\PCs} }\,.            \label{eq:em-example}
\end{gather}

The factor of $$4$$ in the encounter multiplier in Eqn. \eqref{eq:em-example}, as well as the factor of $$1/4$$ in $$\XP_{\NPC}$$ in Eqn. \eqref{eq:xp-npc}, comes from the observation that the DMG lists $$\EM = 1$$ for encounters with four PCs and one NPC. While this choice may appear arbitrary at first, it makes sense in the context of monster CR being defined relative of a party of four PCs.

The implication of Eqns. \eqref{eq:xp-pc} and \eqref{eq:xp-npc}, that XP is the product of a creature's effective hit points and effective damage per round, is quite profound. Not only does it give us a direct way of calculating a creature's XP, independent of the CR calculations in the DMG, it also means a creature's XP can be thought of as a measure for how much damage they can be expected to do in the time it takes them to be defeated.

This is a great first step towards understanding how the game's encounter balancing rules work, but more work is needed. In the section that follows, [Calculating XP](#calculating-xp), I compare the XP values given by Eqn. \eqref{eq:xp-npc} to those assigned to each CR using monster stats from the the DMG. And, in the section after that, [Encounter Multiplier](#encounter-multiplier), I take a deeper look at how the encounter multiplier can be determined for encounters beyond our simple example, as well as how to fully understand the meaning of Eqn. \eqref{eq:effective-difficulty-eq-full}.

# Calculating XP

While the results of the previous section make sense conceptually, they're of little value if they can't accurately reproduce XP values for PCs and NPCs given in the core rules. In this section, let's take a moment to verify that we're heading down the right path by confirming that Eqn. \eqref{eq:xp-npc} matches the monster XP values listed for each CR. 

Taking advantage of the equations for $$\eHP$$ and $$\eDPR$$ from my previous post, [Effective HP and Damage]({{ site.data.page-links.effective-hp-and-damage.path }}), Eqns. \eqref{eq:xp-pc} and \eqref{eq:xp-npc} can be written more explicitly in terms of a creature's armor class $$(\AC\,)$$, attack bonus $$(\AB\,)$$, and average damage per round assuming all attacks hit $$(\DPRhit)$$ as
\begin{gather}
    \XP_{\PC}  = \HP \cdot \DPRhit \cdot 1.077^{\AC + \AB - 15} \,,             \label{eq:xp-pc-explicit} \\\\ 
    \XP_{\NPC}  = \frac{1}{4}\HP \cdot \DPRhit \cdot 1.077^{\AC + \AB - 15}\,.   \label{eq:xp-npc-explicit}
\end{gather}
The factor of $$1.077 \equiv 14/13$$ used in these equations comes from the game following a baseline chance to hit with an attack of $$65\%$$, or $$13/20$$.

This can be simplified further by taking a linear approximation of the exponential term in each equation via $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, which yields
\begin{gather}
    %\XP_{\PC}  &= \HP \cdot \DPRhit \left(1 + 0.077\left(\AC + \AB - 15\right)\right) \,, \label{eq:experience-PC-linear} \\\\ 
    %\XP_{\NPC}  &= \frac{1}{4}\HP \cdot \DPRhit \left(1 + 0.077\left(\AC + \AB - 15\right)\right)\,, \label{eq:experience-NPC-linear}
    \XP_{\PC}  = \HP \cdot \DPRhit \left( \frac{\AC + \AB - 2}{13} \right) \,, \label{eq:experience-PC-linear} \\\\ 
    \XP_{\NPC}  = \frac{1}{4}\HP \cdot \DPRhit \left( \frac{ \AC + \AB - 2 }{13} \right)\,. \label{eq:experience-NPC-linear}
\end{gather}

This approximation loses accuracy as $$\AC + \AB$$ get significantly larger than $$15$$, however, it will prove useful when comparing with the values in the DMG.

To verify that these methods for calculating XP are accurate, Fig. \figref{fig:effective-xp-ratio-vs-cr} (below) plots XP values calculated using Eqns. \eqref{eq:xp-npc-explicit} and \eqref{eq:experience-NPC-linear} for monsters with typical stats taken from [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG.

<figure id="fig:effective-xp-ratio-vs-cr">
    {% include_relative fig-effective-xp-ratio-vs-cr-small.html %}
    {% include_relative fig-effective-xp-ratio-vs-cr-large.html %}
    <figcaption>Plots XP values for typical monsters at each CR calculated using Eqn. \eqref{eq:xp-npc-explicit} (blue) and Eqn. \eqref{eq:experience-NPC-linear} (orange). Typical values for monster statistics were taken from the <a href="https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterStatisticsbyChallengeRating">Monster Statistics by Challenge Rating</a> table in chapter 9 of the DMG.</figcaption>
</figure>

Clearly, the linear approximation given by Eqn. \eqref{eq:experience-NPC-linear} matches the target XP values the best out of the two. From an theoretical perspective, I would consider Eqn. \eqref{eq:experience-NPC-linear} to be less correct than Eqn. \eqref{eq:xp-npc-explicit}, since the approximation needed to reach it doesn't hold up for higher CR monsters. However, since the same approximation would be applied to both PCs and NPCs alike, I think it's unlikely cause to any significant problems unless there is a large gap between $$\AC + \AB\,$$ for the PCs and NPCs in the encounter.

This method also works well for calculating XP values for published monsters and for player characters. For a comparison between calculated XP and target XP values of published monsters, see [Calculating Monster XP]({{ site.data.page-links.calculating-monster-xp.path }}). And, for a comparison of calculated XP values and player character XP thresholds, see [Player Character XP]({{ site.data.page-links.xp-and-player-characters.path }}).


# Encounter multiplier

Now that we've established what XP is and how it's calculated, let's turn our attention back to the encounter multiplier. To start, Eqn. \eqref{eq:effective-difficulty-eq-full} can be rewritten in terms of XP as
\begin{equation}
    \d \sum_{i,j = 1}^{N_{\PCs}} \XP_{\PC\_{ij}} = 4 \sum_{i,j = 1}^{N_{\NPCs}} \XP_{\NPC_{ij}}\,,
    \label{eq:effective-difficulty-xp}
\end{equation}
where $$\XP_{\PC_{ij}}$$ $$(\XP_{\NPC_{ij}})$$ represents the cross term between the $$i$$th and $$j$$th PCs (NPCs), as described by Eqns. \eqref{eq:xp-pc} and \eqref{eq:xp-npc}.

The diagonal terms in Eqn. \eqref{eq:effective-difficulty-xp}, when $$i = j$$, are clearly the individual XP values for each PC (NPC) in the encounter, but what about the off-diagonal terms, when $$i \neq j\,$$? 

To understand this better, consider the diagram in Fig. \figref{fig:xp-encounter-diagram} (below), which gives a graphical representation of the right-hand side of Eqn. \eqref{eq:effective-difficulty-xp} for an encounter with three enemy NPCs.

<figure id="fig:xp-encounter-diagram">
    {% include_relative fig-xp-encounter-diagram-small.html %}
    {% include_relative fig-xp-encounter-diagram-large.html %}
    <figcaption>Graphical representation of the RHS of Eqn. \eqref{eq:effective-difficulty-xp} for and encounter with three NPCs.</figcaption>
</figure>

The area of each square, $$\XP_{ij} \propto \eHP_{i} \cdot \eDPR_{j}$$, represents how much XP it contributes to the difficulty of the encounter. The white regions represent the XP of each NPC individually, and the remaining XP, colored blue and red, represents the XP added to the encounter due to the NPCs being in a group.

Focusing on just the first column, the meaning of this additional XP becomes clear. Moving from bottom to top, the first square, $$\XP_{1,1} \propto \eHP_{1} \cdot \eDPR_{1}$$, is the individual XP for NPC 1 and represents the damage they can be expected to do in the time it takes the PCs to defeat them. The second square, $$\XP_{2,1} \propto \eHP_{2} \cdot \eDPR_{1}$$, represents the extra damage NPC 1 can be expected to do in the time it takes the PCs to defeat NPC 2. Finally, the third square, $$\XP_{3,1} \propto \eHP_{3} \cdot \eDPR_{1}$$, represents the extra damage NPC 1 can be expected to do in the time it takes the PCs to defeat NPC 3.

Of course, if NPC 1 is defeated first then $$\XP_{2,1}$$ and $$\XP_{3,1}$$ shouldn't add to the encounter's difficulty. With this in mind, the blue region in Fig. \figref{fig:xp-encounter-diagram} represents the additional XP added to the encounter when defeating the NPCs one at a time in the following order, NPC 3 $$\rightarrow$$ NPC 2 $$\rightarrow$$ NPC 1, while the red region represents the additional XP for defeating the NPCs in the opposite order.

Looking at Fig. \figref{fig:xp-encounter-diagram}, it's clear that areas of the red and blue regions are not equal in this example. This means the difficulty of the encounter depends on the order the NPCs are defeated in!

Applied more generally, this means the XP added to an encounter's difficulty by the encounter multiplier accounts for the extra damage dealt by some of the NPCs while the PCs are focusing their attention on others. This explains why the DMG applies the encounter multiplier to groups of NPCs fought at the same time but not to encounters where multiple NPCs fought one after the other.

To account for the fact that the order the PCs and NPCs are defeated in changes the total XP on each side of our encounter balancing equation, each term can be given a weight, $$\W_{ij}$$, that depends on how the PCs and NPCs are likely to engage with one another. Doing so, Eqn. \eqref{eq:effective-difficulty-xp} can be rewritten as, 
\begin{equation}
    \d \sum_{i,j = 1}^{N_{\PCs}} \W\_{\,\PC\_{ij}} \cdot \XP\_{\,\PC\_{ij}} = 4 \sum_{i,j = 1}^{N_{\NPCs}} \W\_{\,\NPC\_{ij}} \cdot \XP\_{\,\NPC\_{ij}}\,.
    \label{eq:difficulty-xp-weighted}
\end{equation}

Rearranging Eqn. \eqref{eq:difficulty-xp-weighted} into the same form as Eqn. \eqref{eq:encounter-balance-equation-dmg}, the encounter multiplier can be written in its full general form,
\begin{equation}
    \EM = \left( 
        \frac{ \XP_{\NPCs}^{\,\weighted} }{ \XPtot_{\NPCs} } 
    \right) 
    \cdot \left( 
        \frac{ 4\,  \XPtot_{\PCs} }{ \XP_{\PCs}^{\,\weighted} }
    \right) \,,
    \label{eq:encounter-multiplier-weighted}
\end{equation}
where
\begin{equation}
    \XP^{\,\weighted} = \sum_{i,j = 1}^{N} \W_{ij} \cdot \XP_{ij}
\end{equation}
is the total weighted XP of the NPCs or PCs in the encounter.

At this point, Eqn. \eqref{eq:encounter-multiplier-weighted} probably looks like an incomprehensible mess, and it definitely is, but things can be simplified considerably by making some key assumptions about how the PCs and NPCs choose to engage each other. This is a complex topic that requires much more time and consideration that I can easily fit into this post. For a full detailed discussion of the encounter multiplier, see [Calculating the Encounter Multiplier: part 1]({{ site.data.page-links.encounter-multiplier-p1.path }}).

# Conclusion

To summarize, both XP and the encounter multiplier arise as natural consequences of balancing encounters around the amount of damage the PCs are likely to take relative to their maximum health. XP can be calculated directly from the product of a creature's effective hit points and effective damage per round, as shown in Eqns. \eqref{eq:experience-PC-linear} and \eqref{eq:experience-NPC-linear}, and can be thought of as representing the amount of damage a creature is expected to do in the time it takes them to be defeated. And, the encounter multiplier estimates the additional XP for encounters with multiple creatures, and represents the extra damage some creatures are able to do while their enemies are busy dealing with their allies.

While this covers the key concepts I wanted to touch on for where XP comes from and what the encounter multiplier represents, there is still a lot more to cover on these topics, especially the encounter multiplier, which you can read more about in [Calculating the Encounter Multiplier: part 1]({{ site.data.page-links.encounter-multiplier-p1.path }}).