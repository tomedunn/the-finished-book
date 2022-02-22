---
title: "XP and Encounter Balancing"
excerpt: "A detailed explanation of where XP comes from and how encounter balancing works."
date: 2022-1-27
last_modified_at: 2022-2-21
#tags:
#  - theory
#  - monsters
#  - classes
---

\\(
\newcommand{\RTW}{\mathit{RTW}}
\newcommand{\AC}{\mathit{AC}}
\newcommand{\eAC}{\mathit{eAC}}
\newcommand{\HP}{\mathit{HP}}
\newcommand{\eHP}{\mathit{eHP}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\eDPR}{\mathit{eDPR}}
\newcommand{\DPR}{\mathit{DPR}} 
\newcommand{\DPRhit}{\mathit{DPR}\_\mathrm{hit}} 
% other
\newcommand{\CR}{\mathit{CR}}
\newcommand{\XP}{\mathit{XP}}
\newcommand{\diff}{\mathit{diff}}
\newcommand{\EM}{\mathit{EM}}
\newcommand{\W}{\mathit{W}}
% NPCs
\newcommand{\NPC}{\mathrm{NPC}}
\newcommand{\NRTW}{\mathit{RTW}\_\mathrm{\NPC}}
\newcommand{\NeHP}{\mathit{eHP}\_\mathrm{\NPC}}
\newcommand{\NeDPR}{\mathit{eDPR}\_\mathrm{\NPC}}
\newcommand{\NXP}{\mathit{XP}\_\mathrm{\NPC}}
% PCs
\newcommand{\PC}{\mathrm{PC}}
\newcommand{\PRTW}{\mathit{RTW}\_\mathrm{\PC}}
\newcommand{\PeHP}{\mathit{eHP}\_\mathrm{\PC}}
\newcommand{\PeDPR}{\mathit{eDPR}\_\mathrm{\PC}}
\newcommand{\PXP}{\mathit{XP}\_\mathrm{\PC}}
\\)

# Introduction

Combat encounters are one of the cornerstones of D&D 5th edition which makes building encounters an essential skill for DMs. Chapter 13 of the _Basic Rules_, "[Building Combat Encounters](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters)", contains guidelines to help DMs balance and estimate the difficulty of their encounters. These guidelines work quite well, overall, but to a casual observer it's not entirely clear why they work the way they do. At the heart of this is why XP is used for balancing encounters instead of CR and why an encounter multiplier needs to be used to adjust the total XP for an encounter.

In this post I will answer these questions by showing how encounter balancing rules can be derived from fundamental equations for how combat works, and how XP arises as a natural product of that derivation.

# Derivation

Just like in my previous post, [Effective HP and Damage]({{ site.url }}{{ site.baseurl }}{% link _theory/effective-hp-and-damage.md %}), let's start with the equation for a measurable quantity to base this derivation on. Specifically, the number of rounds it takes for either the PCs or enemy NPCs to win a combat encounter. The rounds to win $$(\RTW\,)$$ can be calculated by dividing the effective hit points $$(\eHP\,)$$ of one side by the effective damage per round $$(\eDPR)$$ of the other,

\begin{align}
    \PRTW &= \frac{\sum \NeHP}{\sum \PeDPR}\,, \label{eq:rounds-to-win-full-PCs} \\\\ 
    \NRTW &= \frac{\sum \PeHP}{\sum \NeDPR}\,, \label{eq:rounds-to-win-full-NPCs}
\end{align}

where $$\sum$$ denotes a summation over all PCs (NPCs) in the encounter.

The difficulty of a combat encounter can be expressed in terms of the number of rounds it takes each side to win as either a difference or a ratio. For this derivation, I'll focus on the later and express the encounter difficulty as

\begin{equation}
    \diff =\frac{\PRTW}{\NRTW}\,.
    \label{eq:difficulty}
\end{equation}
For easy encounters $$\diff \ll 1$$ (i.e., the PCs win well before the NPC have a chance to), while for deadly encounters $$\diff \simeq 1$$ (i.e., each side wins in a similar number of rounds).

Inserting Eqns. \eqref{eq:rounds-to-win-full-PCs} and \eqref{eq:rounds-to-win-full-NPCs} into Eqn. \eqref{eq:difficulty} yields 
\begin{equation}
    \diff =\frac{\left( \sum \NeHP \right) \cdot \left( \sum \NeDPR \right)}{\left( \sum \PeHP \right) \cdot \left( \sum \PeDPR \right)}\,.
    \label{eq:difficulty-ratio}
\end{equation}
This can also be rearranged in the following way, 
\begin{equation}
    \diff \cdot \left( \sum \PeHP \right) \cdot \left( \sum \PeDPR \right) = \left( \sum \NeHP \right) \cdot \left( \sum \NeDPR \right)\,,
    \label{eq:difficulty-experience}
\end{equation}
which moves all of the PC related terms to the LHS of the equation and all of the NPC related terms to the RHS.

At this point, Eqn. \eqref{eq:difficulty-experience} is far to complicated to be of any practical use. To simplify things, lets see how things play out for an encounter consisting of $$N$$ identical PCs and $$M$$ identical NPCs.  Under these conditions, Eqn. \eqref{eq:difficulty-experience} simplifies to 
\begin{equation}
    \diff \cdot N^{2} \cdot \PeHP \cdot \PeDPR = M^{2}\cdot \NeHP \cdot \NeDPR\,.
    \label{eq:difficulty-experience-simple}
\end{equation}
This bares a striking resemblance to how encounter difficulty is calculated in chapter 13, "[Building Combat Encounters](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters)", from the _Basic Rules_, which can be expressed as the sum of each PC's experience points threshold for a given encounter difficulty, $$\PXP$$, and each NPC's experience points value, $$\NXP$$, 
\begin{equation}
    \sum \PXP(L, \diff\,) = \EM(N, M)\ \sum \NXP(\CR\,)\,.
    \label{eq:encounter-balance-dmg}
\end{equation}
Here $$L$$ represents a PC's level, $$\CR$$ represents a NPC's challenge rating, and $$\EM(N, M)$$ is the encounter multiplier which depends on the number of PCs and NPCs in the encounter.

Equation \eqref{eq:difficulty-experience-simple} can be expressed in this form via  the following relationships:
\begin{gather}
    \PXP(L, \diff\,)  = \diff \cdot \PeHP(L) \cdot \PeDPR(L)\,, \label{eq:experience-PC} \\\\ 
    \NXP(\CR\,)       = \frac{1}{4}\NeHP(\CR\,) \cdot \NeDPR(\CR\,)\,, \label{eq:experience-NPC} \\\\ 
    \EM(N, M)         = \frac{4\,M}{N}\,. \label{eq:encounter-multiplier-full}
\end{gather}

The factor of $$4$$ in the encounter multiplier in Eqn. \eqref{eq:encounter-multiplier-full}, as well as the factor of $$1/4$$ in $$\NXP$$ in Eqn. \eqref{eq:experience-NPC}, comes from the empirical observation that the DMG assigns an encounter with four PCs and one NPC $$\EM(4, 1) = 1$$, rather than $$1 / 4$$ as expected. While this choice may appear arbitrary at first, it makes sense in the context of monster $$\CR$$ being defined relative of a party of four PCs.

The implication of Eqns. \eqref{eq:experience-PC} and \eqref{eq:experience-NPC}, that $$\XP$$ is the product of a creature's effective hit points and effective damage per round, is quite profound. Not only does it give us a direct way of calculating a creature's $$\XP$$ that's independent of the $$\CR$$ calculations in the DMG, it also means that $$\XP$$ can be thought of as a measure for how much damage a creature will likely do in the time it takes an enemy to defeat them.

# Calculating XP

Before moving on to talk about the encounter multiplier and what it represents, let's take a moment to verify that we're heading down the right path by confirming that Eqn. \eqref{eq:experience-NPC} matches the monster $$\XP$$ values listed for each CR. To do this, we'll need a more explicit version of the equation. We need to know how to calculate $$\eHP$$ and $$\eDPR$$. 

Taking advantage of the equations for $$\eHP$$ and $$\eDPR$$ from my previous post, [Effective HP and Damage]({{ site.url }}{{ site.baseurl }}{% link _theory/effective-hp-and-damage.md %}), Eqns. \eqref{eq:experience-PC} and \eqref{eq:experience-NPC} can be written more explicitly in terms of a creature's armor class $$(\AC\,)$$, attack bonus $$(\AB\,)$$, and average damage per round assuming all attacks hit $$(\DPRhit)$$, as

\begin{align}
    \PXP  &= \HP \cdot \DPRhit \cdot 1.083^{\AC + \AB - 16} \,, \label{eq:experience-PC-explicit} \\\\ 
    \NXP  &= \frac{1}{4}\HP \cdot \DPRhit \cdot 1.083^{\AC + \AB - 16}\,. \label{eq:experience-NPC-explicit}
\end{align}

This can be simplified further by taking a linear approximation for the exponential term in each equation via $$\left(1 + x\right)^n \approx 1 + n \cdot x$$ when $$x \ll 1$$, 

\begin{align}
    \PXP  &= \HP \cdot \DPRhit \cdot \left(1 + 0.083\left(\AC + \AB - 16\right)\right) \,, \label{eq:experience-PC-linear} \\\\ 
    \NXP  &= \frac{1}{4}\HP \cdot \DPRhit \left(1 + 0.083\left(\AC + \AB - 16\right)\right)\,. \label{eq:experience-NPC-linear}
\end{align}

This approximation loses accuracy as $$\AC + \AB$$ get significantly larger than $$16$$, however, it will prove useful when comparing with the values in the DMG.

To verify that these methods for calculating $$\XP$$ are accurate, Fig. <a href="#fig:effective-xp-ratio-vs-cr" class="fig-ref">1</a> below plots $$\XP$$ values, calculated using Eqns. \eqref{eq:experience-NPC-explicit} and \eqref{eq:experience-NPC-linear}, for monsters with typical stats taken from [Monster Statistics by Challenge Rating](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterStatisticsbyChallengeRating) table in chapter 9 of the DMG.

<figure id="fig:effective-xp-ratio-vs-cr">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/xp-and-encounter-balancing/fig-effective-xp-ratio-vs-cr.svg">
    <figcaption>Figure 1: Plots XP values for typical monsters at each CR calculated using Eqn. \eqref{eq:experience-NPC-explicit} (blue) and Eqn. \eqref{eq:experience-NPC-linear} (orange). Typical values for monster statistics were taken from the Monster Statistics by Challenge Rating table in chapter 9 of the DMG.</figcaption>
</figure>

Clearly, the linear approximation given by Eqn. \eqref{eq:experience-NPC-linear} matches the target $$\XP$$ values the best out of the two. From an theoretical perspective, I would consider Eqn. \eqref{eq:experience-NPC-linear} to be less correct than \eqref{eq:experience-NPC-explicit}. However, since the since the same approximation would be applied to both PCs and NPCs alike, I think it's unlikely this loss in theoretical correctness leads to any significant problems.

For a more expansive analysis of how this method of calculating monster $$\XP$$ holds up for actual monsters published in official source books, check out [Calculating Monster XP]({{ site.url }}{{ site.baseurl }}{% link _monsters/calculating-monster-xp.md %}).

# Encounter multiplier

Now that I've established what $$\XP$$ is and how it's calculated, let's turn our attention back to the encounter multiplier.

To start, Eqn. \eqref{eq:difficulty-experience} can be rewritten in terms of $$\XP$$, 

\begin{equation}
    \diff \sum_{i,j} \XP\_{\,\mathrm{PC}\_{ij}} = 4 \sum_{i,j} \XP\_{\,\mathrm{NPC}\_{ij}}\,,
    \label{eq:difficulty-xp}
\end{equation}

where $$\XP_{\,\mathrm{PC}_{ij}}$$ $$(\XP_{\,\mathrm{NPC}_{ij}})$$ represents the cross term between the $$i$$th and $$j$$th PCs (NPCs), and the summation on each side represents the sum over all combinations of PCs (NPCs).

This is simpler to write, but it doesn't offer any immediately improved understanding. The diagonal terms, when $$i = j$$, are clearly the individual $$\XP$$ values for each PC (NPC), but what about the off diagonal terms when $$i \neq j\,$$? 

To understand this better, consider the diagram in Fig. <a href="#fig:xp-encounter-diagram" class="fig-ref">2</a> (below), which is a graphical representation of the RHS of Eqn. \eqref{eq:difficulty-xp} for and encounter with three enemy NPCs.

<figure id="fig:xp-encounter-diagram">
    <img src="{{ site.url }}{{ site.baseurl }}/theory/xp-and-encounter-balancing/fig-xp-encounter-diagram.svg" style="width:700px;min-width:50%;max-width:100%">
    <figcaption>Figure 2: Graphical representation of the RHS of Eqn. \eqref{eq:difficulty-xp} for and encounter with three NPCs.</figcaption>
</figure>

The area of each square, $$\XP_{ij} \propto \eHP_{i} \cdot \eDPR_{j}$$, represents how much $$\XP$$ each contributes to the difficulty of the encounter. The white regions represent the $$\XP$$ of each NPC individually, and the remaining $$\XP$$, colored blue and red, represents the $$\XP$$ added to the encounter due to the NPCs being in a group.

Focusing on just the first column, the meaning of this additional $$\XP$$ becomes clear. Moving from bottom to top, the first square, $$\XP_{1,1} \propto \eHP_{1} \cdot \eDPR_{1}$$, is the individual $$\XP$$ for NPC 1 and represents the damage they do in the time it takes the PCs to defeat them. The second square, $$\XP_{2,1} \propto \eHP_{2} \cdot \eDPR_{1}$$, represents the extra damage dealt by NPC 1 in the time it takes the PCs to defeat NPC 2. Finally, the third square, $$\XP_{3,1} \propto \eHP_{3} \cdot \eDPR_{1}$$, represents the extra damage dealt by NPC 1 in the time it takes the PCs to defeat NPC 3.

Of course, if NPC 1 is defeated first then $$\XP_{2,1}$$ and $$\XP_{3,1}$$ shouldn't add to the encounter's difficulty. With this in mind, the blue region in Fig. <a href="#fig:xp-encounter-diagram" class="fig-ref">2</a> represents the additional $$\XP$$ added to the encounter when defeating the NPCs one at a time in the following order, NPC 3 $$\rightarrow$$ NPC 2 $$\rightarrow$$ NPC 1, while the red region represents the additional $$\XP$$ for defeating the NPCs in the opposite order.

Looking at Fig. <a href="#fig:xp-encounter-diagram" class="fig-ref">2</a>, it's clear that areas of the red and blue regions are not equal in this example. This means the difficulty of the encounter depends on the order the NPCs are defeated in!

Applied more generally, this means the $$\XP$$ added to an encounter's difficulty by the encounter multiplier accounts for the extra damage dealt by some of the NPCs while the PCs are focusing their attention on others. This explains why the DMG applies the encounter multiplier to groups of NPCs fought at the same time but not to encounters where multiple NPCs fought one after the other.

To account for the fact that the order the PCs and NPCs are defeated in changes the total $$\XP$$ on each side of our encounter balancing equation, each term can be given a weight, $$\W_{ij}$$, that depends on how the PCs and NPCs are likely to engage with one another. Doing so, Eqn. \eqref{eq:difficulty-xp} can be rewritten as, 

\begin{equation}
    \diff \sum_{i,j} \W\_{\,\PC\_{ij}} \cdot \XP\_{\,\PC\_{ij}} = 4 \sum_{i,j} \W\_{\,\NPC\_{ij}} \cdot \XP\_{\,\NPC\_{ij}}\,.
    \label{eq:difficulty-xp-weighted}
\end{equation}

Rearranging Eqn. \eqref{eq:difficulty-xp-weighted} into the same form as Eqn. \eqref{eq:encounter-balance-dmg}, the encounter multiplier can be written in its full general form,

\begin{equation}
    \EM = \left( \frac{ \sum_{i,j} \W\_{\,\NPC\_{ij}} \cdot \XP\_{\,\NPC\_{ij}} }{ \sum_{i} \XP\_{\,\NPC\_{i}} } \right) 
    \cdot \left( \frac{ 4\,\sum_{i} \XP\_{\,\PC\_{i}} }{ \sum_{i,j} \W\_{\,\PC\_{ij}} \cdot \XP\_{\,\PC\_{ij}} } \right) \,.
    \label{eq:encounter-multiplier-weighted}
\end{equation}

At this point, Eqn. \eqref{eq:encounter-multiplier-weighted} probably looks like an incomprehensible mess, and it definitely is, but things can be simplified considerably by making some key assumptions about how the PCs and NPCs choose to engage each other, which I will talk about in a future post.

# Conclusion

To summarize, both XP and the encounter multiplier arise as natural consequences of encounter balancing. XP can be calculated directly from the product of a creature's effective hit points and effective damage per round, as shown in Eqns. \eqref{eq:experience-PC-linear} and \eqref{eq:experience-NPC-linear}, and can be thought of as representing the amount of damage a creature is expected to do in the time it takes them to be defeated. And, the encounter multiplier estimates the additional XP for encounters with multiple creatures, and represents the extra damage some creatures are able to do while their enemies are busy dealing with their allies.

While this covers the key concepts I wanted to touch on for where XP comes from and what the encounter multiplier represents, there is still a lot more to cover on these topics, especially the encounter multiplier, which you can read more about [here]({{ site.url }}{{ site.baseurl }}{% link _theory/encounter-multiplier.md %}).