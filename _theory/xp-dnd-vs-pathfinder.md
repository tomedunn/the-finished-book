---
title: "XP in D&D vs Pathfinder"
excerpt: "How similar is the math between the XP and encounter building systems in D&D 5e and Pahtfinder 2e?"
date: 2023-1-17
last_modified_at: 2023-1-17
#tags:
#  - theory
---

<div style="display:none">
\(
\newcommand{\LV}{\mathit{LV}}
\newcommand{\AC}{\mathit{AC}}
\newcommand{\HP}{\mathit{HP}}
\newcommand{\AB}{\mathit{AB}}
\newcommand{\DPR}{\mathit{DPR}} 
\newcommand{\DPRhit}{\mathit{DPR}_\mathrm{hit}} 
% other
\newcommand{\CR}{\mathit{CR}}
\newcommand{\XP}{\mathit{XP}}
\)
</div>

# Introduction
This will be a bit different from my typical post. Until now, I've exclusively covered the game mechanics of D&D 5th edition (D&D 5e), but in this post I'd like to take a look at how the encounter building rules in Pathfinder 2nd edition (PF 2e) work. Specifically, how they compare to the rules in D&D 5e. Most of the math I derived in my previous posts on [XP and Encounter Balancing]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}) is fairly general, which means it should apply to the XP and encounter building rules in PF 2e as well, at least in principles.

# Comparing Systems

In D&D 5e, monster are assigned challenge ratings (CR), as well as experience point (XP) values based on their CR. These XP values are a measure of how dangerous an individual monster is in combat, and the [encounter building rules](https://www.dndbeyond.com/sources/basic-rules/building-combat-encounters) use them to determine how deadly an encounter is, by comparing them with similar XP thresholds for the player characters (PCs), that depend on the PCs' level.

In comparison, in PF 2e, monsters have levels and XP values, but their XP values are defined [relative](https://2e.aonprd.com/Rules.aspx?ID=499) to the PCs' level, rather than in absolute terms. The rules for [building combat encounters](https://2e.aonprd.com/Rules.aspx?ID=497) still use XP to determine how deadly an encounter is, but because those XP values are relative, the XP thresholds they use are fixed, rather than scaling with the PCs' levels.

In general terms, the XP system is D&D 5e is absolute, while the XP system in PF 2e is relative. Both systems can work equally well in theory. However, in order for a relative XP system to work effectively, monsters have to scale in combat strength in a consistent manner.

# XP scaling in Pathfinder

The XP and encounter building rules in PF 2e actually come in two flavors: "standard" and "proficiency without level" (PWL). In the "standard" version of the rules, a creature's level is added to their armor class, attack bonus, and saving throw bonuses, while in the PWL version it isn't. So a level 10 creature might have an attack bonus of +17 in the "standard" rules and a +7 under PWL.

This difference means that monsters under the "standard" system increase in absolute combat power faster than they do under PWL, which means they should also scale faster in relative terms as well. The [Standard vs PWL XP](#tab:standard-vs-pwl-xp) table (below) shows the relative XP values for PF 2e's "[standard](https://2e.aonprd.com/Rules.aspx?ID=499)" and [PWL](https://2e.aonprd.com/Rules.aspx?ID=1371) systems, and this faster scaling for the "standard" system is clearly evident.

<div class="dataframe center" style="width:660px;">
<h3 id="tab:standard-vs-pwl-xp">Standard vs PWL XP</h3>
<table border="0" style="width: 600px; max-width: 100%; margin-left: auto; margin-right: auto;">
    <thead>
        <tr>
            <td style="text-align:center"><strong>Creature Level</strong></td>
            <td style="text-align:center"><strong>Standard XP</strong></td>
            <td style="text-align:center"><strong>PWL XP</strong></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">Party Level -4</td>
            <td style="text-align:center">10</td>
            <td style="text-align:center">18</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -3</td>
            <td style="text-align:center">15</td>
            <td style="text-align:center">21</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -2</td>
            <td style="text-align:center">20</td>
            <td style="text-align:center">26</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level -1</td>
            <td style="text-align:center">30</td>
            <td style="text-align:center">32</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level</td>
            <td style="text-align:center">40</td>
            <td style="text-align:center">40</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +1</td>
            <td style="text-align:center">60</td>
            <td style="text-align:center">48</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +2</td>
            <td style="text-align:center">80</td>
            <td style="text-align:center">60</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +3</td>
            <td style="text-align:center">120</td>
            <td style="text-align:center">72</td>
        </tr>
        <tr>
            <td style="text-align:center">Party Level +4</td>
            <td style="text-align:center">160</td>
            <td style="text-align:center">90</td>
        </tr>
    </tbody>
</table>
</div>

Now, the way attack rolls, saving throws, and damage work in PF 2e is generally very similar the way they work in D&D 5e, which means the underlying math should be essentially the same. In that case, the [XP formula]({{ site.url }}{{ site.baseurl }}{% link _theory/xp-and-encounter-balancing.md %}#mjx-eqn-eq:experience-NPC-explicit) I previously derived for D&D 5e should work as a means of translating between these two systems. 

Recall, for D&D 5e, I showed a monster's XP can be calculated using the following formula,

\begin{align}
    \XP  &\propto \HP \cdot \DPRhit \cdot 1.083^{\AC + \AB - 16} \,, \label{eq:xp-dnd}
\end{align}

where $$\HP$$ is the creature's average hit points, $$\DPRhit$$ is their average damage assuming all attacks hit, $$\AC$$ is their effective armor class, and $$\AB$$ is their effective attack bonus.

Translating between PF 2e's "standard" and PWL versions, $$\AB \rightarrow \AB - \LV$$ and $$\AC \rightarrow \AC - \LV$$, where $$\LV$$ represents the creature's level. Inserting these into Eqn. \eqref{eq:xp-dnd}, the formula for XP under PWL becomes,

\begin{align}
    \XP_{\mathrm{PWL}}  &\propto \HP \cdot \DPRhit \cdot 1.083^{(\AC - \LV\,) + (\AB - \LV\,) - 16} \nonumber \\\\ 
         &= \HP \cdot \DPRhit \cdot 1.083^{\AC + \AB - 16} \cdot 1.083^{- 2\,\LV} \nonumber \\\\ 
         &= \XP_{\mathrm{S}} \cdot 1.083^{- 2\,\LV} \,, \label{eq:xp-pf-pwl}
\end{align}

where $$\XP_{\mathrm{S}}$$ is the creature's absolute XP value under the "standard" system.

Because Eqn. \eqref{eq:xp-pf-pwl} scales exponentially with the creature's level, it can easily be applied to Pathfinder's relative level system by replacing a creature's level with their relative level, giving us an easy way of translating between the two XP values. A comparison between PF 2e's PWL XP values and those predicted by Eqn. \eqref{eq:xp-pf-pwl} is shown in Fig. <a href="#fig:pf-xp-theory" class="fig-ref">1</a> (below). 

<figure id="fig:pf-xp-theory">
    {% include_relative xp-dnd-vs-pathfinder/fig-pf-xp-theory-small.html %}
    {% include_relative xp-dnd-vs-pathfinder/fig-pf-xp-theory-large.html %}
    <figcaption>Figure 1: Pathfinder 2nd edition monster XP vs relative level for "Proficiency Without Level" system, along with a theoretical XP values calculated from "standard" proficiency scaling rules.</figcaption>
</figure>

Overall, Eqn. \eqref{eq:xp-pf-pwl} shows excellent agreement with the values provided in the PF 2e rules for PWL. This strongly suggests the encounter building systems for D&D 5e and PF 2e are based on the same fundamental math.

<!--
| Creature Level | PWL XP (rules) | PWL XP (theory) |
|:--------------:|:--------------:|:---------------:|
| Party Level -4 |             18 |              19 |
| Party Level -3 |             21 |              14 |
| Party Level -2 |             26 |              38 |
| Party Level -1 |             32 |              35 |
| Party Level    |             40 |              40 |
| Party Level +1 |             48 |              51 |
| Party Level +2 |             60 |              58 |
| Party Level +3 |             72 |              74 |
| Party Level +4 |             90 |              84 |
-->

# Comparing Pathfinder vs D&D

In the last section, I showed how Pathfinder's two XP systems could be translated between using the XP formula I previously derived for D&D 5e. In this section, I expand on this by showing how 5th edition's XP values can be translated into a relative XP system, effectively reproducing Pathfinder's PWL XP values.

As I mentioned earlier, in order for a relative XP system, like PF 2e's, to work, monster absolute XP values need to scale in a consistent way. For example, the relative XP values used by PF 2e's "Standard" rules double every two levels, which means their absolute XP values should scale like

\begin{align}
    \XP_{\mathrm{S}}  &= \XP_1 \cdot 2^{0.5\,\LV} \,, \label{eq:xp-pf-absolute}
\end{align}

where $$\XP_1$$ is the absolute XP value of a level 1 creature.

Combining Eqns. \eqref{eq:xp-pf-pwl} and \eqref{eq:xp-pf-absolute} gives the absolute XP scaling for PWL,

\begin{align}
    \XP_{\mathrm{PWL}}  &= \XP_1 \cdot 2^{0.5 \, \LV} \cdot 1.083^{- 2\,\LV} \nonumber \\\\ 
    &= \XP_1 \cdot 2^{0.5 \, \LV} \cdot 2^{-0.231 \, \LV} \nonumber \\\\ 
    &= \XP_1 \cdot 2^{0.269 \, \LV} \,, \label{eq:xp-pf-absolute-pwl}
\end{align}

where I used $$1.083 = 2^{0.1155}$$ to go from the first to the second line.

The XP values for D&D 5e don't follow such an exact scaling, but an approximate scaling can be calculated by fitting to an exponential of the form

\begin{align}
    \XP_{\mathrm{5e}}  &= 2^{A\,\LV + B} \,. \label{eq:xp-dnd-fit}
\end{align}

Doing so yields values of $$A = 0.265$$ and $$B = 9.555$$. A comparison of this fit and XP values taken from the [Experience Points by Challenge Rating](https://www.dndbeyond.com/sources/basic-rules/monsters#ExperiencePointsbyChallengeRating) table in chapter 12 of the _Basic Rules_ is show in Fig. <a href="#fig:dnd-xp-fit" class="fig-ref">2</a> (below).

<figure id="fig:dnd-xp-fit">
    {% include_relative xp-dnd-vs-pathfinder/fig-dnd-xp-fit-small.html %}
    {% include_relative xp-dnd-vs-pathfinder/fig-dnd-xp-fit-large.html %}
    <figcaption>Figure 2: Monster XP vs CR for D&D 5e, along with an exponential fit.</figcaption>
</figure>

Careful readers will have already noticed that the level dependent term in this fit, $$A = 0.265$$, is nearly identical to the calculated value of $$0.269$$ for Pathfinder's PWL system! Given the similarities of these two systems, this result isn't too surprising, but it does give further confidence in the overall approach taken here.

The closeness of this fit also means we can use the PWL system for building combat encounters in D&D 5e. At least, up to a scaling constant.

This is the point where I must admit my overall knowledge of PF 2e is lacking. In D&D 5e, a monster who's CR equals the PCs' level is worth roughly $$30\%$$ of how much XP a party of four PCs can handle (i.e., the point where the PCs are evenly matched). In comparison, in PF 2e, a monster who's level equals the PCs' level is worth $$25\%$$ of an "Extreme" encounter, which the rules describe as being an even match for the PCs. These both appear very similar, but there are factors that might skew the results.

One such factor is the lack of an encounter multiplier in PF 2e's encounter building rules. For those unfamiliar, in the D&D 5e encounter building rules, the encounter multiplier is used to adjust a group of monsters' total XP value based on the number of monsters and PCs in the encounter. I dig into the math behind this adjustment in my posts on the [Encounter Multiplier]({{ site.url }}{{ site.baseurl }}{% link _theory/encounter-multiplier-p1.md %}), but in simple terms, it accounts for some monsters living longer than they would normally when grouped together.

The fact that such an adjustment doesn't exist in the PF 2e's encounter building rules, suggest they have either accounted for it their relative XP values,  that they assume more monsters per encounter by default, or that the AoE capabilities of a typical party are substantially different than in D&D 5e. The first option is unlikely, given how well the XP scaling matched between the two games, which leaves the second and third options as the most likely point of difference.

If the PF 2e encounter building rules do assume more monster's per encounter for their baseline (the D&D 5e rules assume only one), then they'll be most accurate when the number of monsters is close to that number, and will get less accurate the farther an encounter deviates from it. If the AoE capabilities of a typical party if PF 2e is substantially stronger than it is in D&D 5e, then this loss in accuracy will be smaller for encounter with more monsters than baseline, and potentially larger for encounters with fewer.

In both cases, this means the PF 2e encounter building rules likely underestimate the difficulty of encounters with only a single monster. For example, while a monster of Party Level +3 might appear to be a Severe threat encounter on paper, it may be closer to an Extreme encounter or harder in practice. 

# Conclusion

This analysis shows that, while their presentation is quite different, the XP and encounter building rules in D&D 5e and PF 2e are quite similar. In fact, they're likely based on the same underlying math.

This means it should be entirely possible to translate D&D 5e's encounter building rules into the same form as PF 2e, however, more work is needed to iron out the details. I'll update this post if I'm able to do so, but I felt these results were interesting enough to post now, rather than wait for all the details to be ironed out.

