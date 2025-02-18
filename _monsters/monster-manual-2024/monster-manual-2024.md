---
title: "Monster Manual (2024)"
excerpt: "A comprehensive breakdown of the 2024 Monster Manual."
permalink: /:collection/:name/
date: 2025-02-17
last_modified_at: 2025-02-17
header:
  og_image: /assets/images/monster-manual-2024.png
tags:
  - D&D 2024
  - monsters
  - combat
  - xp
  - analysis
---

{% include LaTex.html %}


# Introduction
With the release of the 2024 rules update for D&D 5th edition (D&D 2024) there have been a number of changes that directly impact how combat is balanced. In the updated _Player's Handbook_ player characters became stronger in a variety of ways. And, in the updated _Dungeon Master's Guide_ the [encounter building rules](https://www.dndbeyond.com/sources/dnd/free-rules/combat#CombatEncounterDifficulty) dropped the encounter XP multiplier, allowing for encounters with greater numbers of monsters. In this post I break down the third piece of this puzzle by analyzing how monsters in the updated _Monster Manual_ have changed relative to their D&D 2014 counterparts.

There are many ways these changes can be analyzed but, in keeping with the theme of how the new monsters fit into the games combat system, I'll be focussing on these stats in particular:

* **Offensive Stats.** Attack bonus (AB), save difficulty class (DC), and damage per round (DPR), assuming all attacks hit and all saves fail, averaged across the first three rounds of combat.
* **Defensive Stats.** Armor class (AC), average save bonus (SB), and hit points (HP).

All of the stats presented here are adjusted to account for various traits and mechanics a monster might have. For example, if a monster with an attack bonus of $$+5$$ has a trait that gives them advantage whenever they attack then their adjusted attack bonus will be increased by $$+4$$ to account for this for an AB of $$+9$$. My previous post on [valuing conditions]({{ site.data.page-links.valuing-conditions.path }}) covers how many of these adjustments can be calculated. For things not covered there, the [Creating a Monster](https://www.dndbeyond.com/sources/dnd/dmg-2014/dungeon-masters-workshop#CreatingaMonster) section from chapter 9 of the 2014 _Dungeon Master's Guide_ (p. 273) is also a useful reference.

As a result of using adjusted stats, the numbers shown here may be a bit different from those covered by others, such as Teos Abadía's [video breakdown](https://www.youtube.com/watch?v=Bk5SulZGdZk) on the Alphastream YouTube channel and Paul Hughes's analysis on the [Blog of Holding](https://www.blogofholding.com/?p=8469). These differences should be small for all stats except monster HP, which tend to have large adjustments for certain monsters, such as those with multiple damage resistances or immunities, healing abilities, or legendary resistances.

As a final note before jumping into the analysis, throughout this post there are two sets of data used as reference: individual monster data from the 2014 _Monster Manual_ (MM 2014), and [baseline monster stats]({{ site.data.page-links.monster-baseline-stats.path }}#tab:monster-baseline-stats) averaged across all monsters from official D&D 2014 source books and adventure modules.

# Offensive Stats

Starting off with monster attack bonuses, around $$25\%$$ of the monsters present in both books saw a change in AB. While AB decrease for some of those monsters, the majority saw their AB increase, with about half of those increases coming from traits that conferred advantage in some way.

<figure id="fig:ab-vs-cr">
    {% include_relative fig-ab-vs-cr-small.html %}
    {% include_relative fig-ab-vs-cr-large.html %}
    <figcaption>Shows average (mean) attack bonus for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

As a result, the average AB for MM 2024 monsters is generally higher than is was for MM 2014 monsters, but only by a relatively small amount. As Fig. \figref{fig:ab-vs-cr} (above) shows, the overall trend of AB with CR for MM 2024 monsters remains consistent with the D&D 2014 historic baseline.

Monster save DC values also increased slightly while remaining close to the D&D 2014 baseline, as shown in Fig. \figref{fig:save-dc-vs-cr} (below).

<figure id="fig:save-dc-vs-cr">
    {% include_relative fig-save-dc-vs-cr-small.html %}
    {% include_relative fig-save-dc-vs-cr-large.html %}
    <figcaption>Shows average (mean) save difficulty class for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

The number of monster abilities that featured compound effects, requiring both an attack roll and a saving throw to confer an effect, decreased and as a result around $$4\%$$ of monsters lost their save DC altogether, while a nearly equal amount gained abilities with saving throws that didn't have one before.

In total, the accuracy of offensive abilities for MM 2024 monsters remains consistent with the historic trends seen throughout D&D 2014. These trends can be approximated using the following equations:
\begin{align}
    \AB &\approx \ \ 3.5 + \CR / 2 \,;  \label{eq:simplified-ab} \nonumber \\\\ 
    \DC &\approx 11.5 + \CR / 2\,. \label{eq:simplified-dc} \nonumber
\end{align}

Moving on to DPR we see our first major difference. A whopping $$92\%$$ of monsters appearing in both books had their DPR changed! And for nearly three quarters of these monsters their DPR increased. The DPR increases for monsters CR 10 and higher were particularly large, as shown in Fig. \figref{fig:dpr-vs-cr} (below), resulting in higher CR monsters dealing significantly more damage than MM 2014 monsters as well as the historic D&D 2014 baseline.

<figure id="fig:dpr-vs-cr">
    {% include_relative fig-dpr-vs-cr-small.html %}
    {% include_relative fig-dpr-vs-cr-large.html %}
    <figcaption>Shows average (mean) damage per round for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

To help understand this trend in a more nuanced way, Fig. \figref{fig:dpr-ratio-vs-cr} (below) normalizes DPR for each CR by dividing it by the D&D 2014 baseline value, and splits the MM 2024 data up in terms of legendary and non-legendary (normal) monsters.

<figure id="fig:dpr-ratio-vs-cr">
    {% include_relative fig-dpr-ratio-vs-cr-small.html %}
    {% include_relative fig-dpr-ratio-vs-cr-large.html %}
    <figcaption>Shows average (mean) normalized damage per round for MM 2014 monsters (blue), MM 2024 normal monsters (orange circles), and MM 2024 legendary monsters (orange squares).</figcaption>
</figure>

Here we can see that this increase in DPR for monsters above CR 10 comes entirely from legendary monsters. While normal monsters continue to follow the historic D&D 2014 baseline, legendary monsters show an average increase in DPR of around $$40\%$$! For non-legendary monsters this trend can be approximated as
\begin{align}
    \DPR_{\mathrm{N}} &\approx
    \begin{cases} 
        \ \ \ \ 6 + \ \  6 \cdot \CR & \CR \lt 20\,, \\\\ 
        132 + 12 \cdot \left( \CR - 20 \right) & \CR \geq 20\,; 
    \end{cases} \nonumber 
\end{align}
and for legendary monsters as
\begin{align}
    \DPR_{\mathrm{L}} &\approx
    \begin{cases} 
        \ \ \ \ 8 + \ \  8 \cdot \CR & \CR \lt 20\,, \\\\ 
        176 + 16 \cdot \left( \CR - 20 \right) & \CR \geq 20\,.
    \end{cases} \nonumber 
\end{align}

# Defensive Stats

Moving on to defensive stats, roughly $$33\%$$ of monsters appearing in both books saw a change in their AC, with the majority seeing a small increase. The net effect of this, shown in Fig. \figref{fig:ac-vs-cr} (below), is that MM 2024 monsters have slightly higher AC than MM 2014 monsters.

<figure id="fig:ac-vs-cr">
    {% include_relative fig-ac-vs-cr-small.html %}
    {% include_relative fig-ac-vs-cr-large.html %}
    <figcaption>Shows average (mean) armor class for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

That said, since the net increase is quite small, and since both sets of MM monsters have trends that are slightly above the D&D 2014 historic baseline, I don't think there's sufficient evidence to suggest a change in the baseline for D&D 2024. The historic trend for AC from D&D 2014 can be approximated as 
\begin{align}
    \AC &\approx    13.0 + \CR/3 \,. \nonumber 
\end{align}

Monster SB values saw considerably more changes than AC. Nearly half of all monsters present in both books saw a change in SB, with the bulk of these changes coming from the unadjusted stat, i.e., from changes to their ability score modifiers and saving throw proficiencies.

While these changes were fairly evenly balanced between higher and lower values, those with lower SB values were much more likely to be higher CR monsters. This trend can be seen in Fig. \figref{fig:sb-vs-cr} (below) for MM 2024 monsters relative to MM 2014 monsters for CR 14 and above, and relative to the D&D 2014 baseline above CR 20.

<figure id="fig:sb-vs-cr">
    {% include_relative fig-sb-vs-cr-small.html %}
    {% include_relative fig-sb-vs-cr-large.html %}
    <figcaption>Shows average (mean) save bonus across all ability scores for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

The cause of this trends is highlighted in Fig. \figref{fig:sp-delta-by-ability} (below), which shows the number of monsters that gained or lost proficiency in each saving throw from MM 2014 to MM 2024. A significant number of monsters lost their proficiencies in Constitution and Charisma saving throws and, given the trend observed previously in Fig. \figref{fig:sb-vs-cr}, those monsters tended to come from higher CRs.

<figure id="fig:sp-delta-by-ability">
    {% include_relative fig-sp-delta-by-ability-small.html %}
    {% include_relative fig-sp-delta-by-ability-large.html %}
    <figcaption>Shows the number of MM 2024 monsters that gained proficiency (blue) or lost their proficiency (orange) in each type of saving throw.</figcaption>
</figure>

From my previous post on D&D 2014 [monster saving throws]({{ site.data.page-links.monster-saving-throws.path }}), Constitution and Charisma have historically been two of the stronger saving throws for higher CR monsters. This change doesn't make those saves weak by any means -- high CR monsters tend to have high Constitution and Charisma modifiers, and that hasn't change -- but it does bring them more in line with the remaining four saving throws, as shown in Fig. \figref{fig:all-sb-vs-cr} (below), resulting in a tighter overall distribution in monster saving throw bonuses at higher CRs.

<figure id="fig:all-sb-vs-cr">
    {% include_relative fig-all-sb-vs-cr-small.html %}
    {% include_relative fig-all-sb-vs-cr-large.html %}
    <figcaption>Shows average (mean) save bonus for each ability scores for MM 2024 monsters.</figcaption>
</figure>

These changes brings down the overall trend for SB from increasing $$+1$$ roughly every 2 CR to roughly every 3 CR, which is the same rate that AC has historically increased at. This new trend can be approximated with the following equation:
\begin{align}
    \SB &\approx \ \ 1.0 + \CR/3 \,. \nonumber 
\end{align}

Finally, we have hit points. From Fig. \figref{fig:hp-vs-cr} (below) we see that for CR 12 and lower HP stays close to the MM 2014 average and the D&D 2014 historic baseline, and for CR 13 and above it's noticeably higher.

<figure id="fig:hp-vs-cr">
    {% include_relative fig-hp-vs-cr-small.html %}
    {% include_relative fig-hp-vs-cr-large.html %}
    <figcaption>Shows average (mean) hit points for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

Just like with DPR in the previous section, this trend can also be broken up between non-legendary (normal) and legendary monsters. Doing so, as shown in Fig. \figref{fig:hp-ratio-vs-cr} (below), reveals that this shift towards higher HP also appears to be exclusive to legendary monsters, with an average increase in HP of around $$15\%$$. Though, this distinction is not quite as convincing as it was was DPR.

<figure id="fig:hp-ratio-vs-cr">
    {% include_relative fig-hp-ratio-vs-cr-small.html %}
    {% include_relative fig-hp-ratio-vs-cr-large.html %}
    <figcaption>Shows average (mean) normalized hit points for MM 2014 monsters (blue), as well as normal MM 2024 monsters (orange circles) and legendary MM 2024 monsters (orange squares).</figcaption>
</figure>

For non-legendary monsters, the trend for HP can be approximated as
\begin{align}
    \HP_{\mathrm{N}} &\approx
    \begin{cases} 
        \ \ 16 + 16 \cdot \CR & \CR \lt 20\,, \\\\ 
        368 + 48 \cdot \left( \CR - 20 \right) & \CR \geq 20\,; 
    \end{cases} \nonumber 
\end{align}
and for legendary monsters as
\begin{align}
    \HP_{\mathrm{L}} &\approx
    \begin{cases} 
        \ \ 19 + 19 \cdot \CR & \CR \lt 20\,, \\\\ 
        437 + 57 \cdot \left( \CR - 20 \right) & \CR \geq 20\,. 
    \end{cases} \nonumber 
\end{align}

Despite this relatively small change, a lot changed behind the scenes for MM 2024 monsters around their HP values. Most significant were the changes to damage resistances and immunities. Specifically, for the physical damage types: bludgeoning, piercing, and slashing damage.

Roughly $$25\%$$ of MM 2014 monsters had some form of resistance or immunity to physical damage types, but with the caveat that the damage come from non-magical sources. For MM 2024 monsters this has been entirely redone. The caveat for magical physical damage has been eliminated and monsters that had these traits have been updated.

Monsters that previously had resistances to non-magical physical damage have been converted to either standard resistances (10 out of 54 monsters) or no damage mitigation (44 out of 54 monsters). And monsters that previously had immunity to non-magical physical damage have been similarly converted to either standard resistance (4 out of 15 monsters) or no damage mitigation (11 out of 15 monsters). The end result is that significantly fewer MM 2024 monsters, roughly $$7\%$$ of monsters CR 1 or higher, have any form of physical damage mitigation.

These types of physical damage resistances and immunities contributed significantly to HP for the MM 2014 monsters that had them. As a result, the MM 2024 versions of monsters that lost these traits saw an average increase in their unadjusted hit points of nearly $$30\%$$, while the average increase to their HP (adjusted hit points) was a more modest $$9\%$$. This closes the gap between adjusted and unadjusted hit points for MM 2024 monsters, especially non-legendary ones, which should lead to more consistent performances in combat between groups with and without magic weapons.

For non-physical damage types, while there were some monsters that saw changes to their resistances and immunities, these changes accounted for less than $$4\%$$ of monsters present in both books.

# Overall combat power

Having established how MM 2024 monsters have change in terms of their offensive and defensive stats, lets combine everything together and look at their overall combat power via their calculated XP values. 

For a detailed breakdown of what monster XP is and how it's calculated, see my previous posts [XP and Encounter Balancing]({{ site.data.page-links.xp-and-encounter-balancing.path }}) and [Calculating Monster XP]({{ site.data.page-links.calculating-monster-xp.path }}). 

That said, in simple terms, monster XP values are an abstract way of measuring how much damage a monster is likely to do in the time it take for them to be defeated. This is done by multiplying their effective hit points $$(\eHP\,)$$ and effective damage per round $$(\eDPR\,)$$ together in the following way, 
\begin{equation}
    \XP = \frac{1}{4} \eHP \cdot \eDPR\,,
    \nonumber
    \label{eq:XP-simple}
\end{equation}
which, for the purposes of this post, we can approximated as, 
\begin{equation}
    \XP = \frac{1}{4}\HP \cdot \DPR \left( \frac{ \AC + \AB - 2 }{13} \right)\,,
    \nonumber
    \label{eq:XP-full}
\end{equation}
where $$\HP$$ is the monster's average hit points, $$\AC$$ is their effective armor class, $$\DPR$$ is their average damage per round across the first three rounds of combat assuming all abilities deal their normal damage, and $$\AB$$ is their effective attack bonus. The values used in this calculation correspond to the adjusted stats shown in the previous sections, with the exception of $$\AC$$ which comes from a combination of AC and SB.

The results of this calculation can be seen in Fig. \figref{fig:xp-ratio-vs-cr} (below), where the values for each CR have been normalized to the D&D 2014 baseline XP value (effectively, the XP value listed in the monster's stat block for their CR). The average XP for non-legendary (normal) MM 2024 monsters stays close to the D&D 2014 historic baseline, averaging around $$10\%$$ higher for monsters CR 5 and above, while legendary MM 2024 monsters are consistently well above the baseline, averaging around $$60\%$$ higher!

<figure id="fig:xp-ratio-vs-cr">
    {% include_relative fig-xp-ratio-vs-cr-small.html %}
    {% include_relative fig-xp-ratio-vs-cr-large.html %}
    <figcaption>Shows average (mean) normalized XP values for MM 2014 monsters (blue), MM 2024 normal monsters (orange triangles), and MM 2024 legendary monsters (orange circles).</figcaption>
</figure>

The full distribution of normalized XP values shown in Fig. \figref{fig:xp-ratio-distribution} (below) makes it quite clear that the offset seen for MM 2024 legendary monsters is not due to statistical outliers. In fact, the distribution for legendary MM 2024 monsters is quite narrow, especially when compared to the distribution for legendary MM 2014 monsters.

<figure id="fig:xp-ratio-distribution">
    {% include_relative fig-xp-ratio-distribution-small.html %}
    {% include_relative fig-xp-ratio-distribution-large.html %}
    <figcaption>Shows normalized XP values for individual monsters, broken up by book and legendary status.</figcaption>
</figure>

For reference, the average normalized XP for legendary MM 2014 monsters is also higher than expected (around $$25\%$$ higher). However, its distribution is also much wider and a significant portion of those monsters have XP near their expected values. As time would show, the reason for the MM 2014 average being higher than expected was because one group of monsters in that book, legendary dragons, were outliers compared to the rest of D&D 2014. For more details, see my post on [Early Legendary Monsters]({{ site.data.page-links.early-legendary-monsters.path }}#source-books).

Time will ultimately tell if this trend holds true for D&D 2024 legendary monsters, but setting aside the statistics, there's a good reason for why this increase in XP for legendary monsters may be intentional, and that's to cover an edge case in the updated encounter building rules. Let me explain.

In the introduction I noted the updated encounter building rules no longer use an XP multiplier to account for how encounter difficulty increases when multiple monsters are grouped together. This simplifies the math and makes the rules more accessible, which is good, but those improvements aren't without their tradeoffs.

I cover the encounter XP multiplier in detail [here]({{ site.data.page-links.encounter-multiplier-p1.path }}) but, in short, from a mathematical perspective it should exist to account for how monsters tend to live longer when grouped together than they do when encountered alone. Removing it means the results will be less accurate when the number of monsters deviates from the default number the rules were built around. More specifically, when more monsters are used the rules will underestimate the difficulty, and when fewer monsters are used they'll overestimate it.

The encounter building rules in the 2014 DMG were centered around a party of four PCs facing a single monster. If the new rules were based on the same assumption then they would underestimate the difficulty by increasing amounts as the number of monsters increase. However, if the new rules were updated to be centered around one monster per PC then the size of this error would be reduced for a wide range of likely encounter sizes, with single monster encounters being the most common exception.

The alternate encounter building rules in _Xanathar's Guide to Everything_ function without an encounter XP multiplier and they do so by using this exact method of re-centering the math around one monster per PC as I showed in my analysis of those rules [here]({{ site.data.page-links.xgte-encounter-building.path }}). To get around the issue this change creates for single monster encounters, those rules also included an entirely separate method for just that kind of encounter.

Legendary monsters aren't the only type of monster that can be used when building single monster encounters. However, when trying to create a challenging single monster encounter, legendary monsters are the most natural choice. Making legendary monsters punch well above their CR shrinks the size of this error significantly for those encounters.

**Note.** Because legendary monsters now hit well above their CR, they shouldn't be paired with other legendary monsters of similar CR when building encounters.
{: .notice--warning}

# Initiative
As a final topic before concluding, I'd like to focus on monster initiative bonuses. For the past decade D&D 2014 monsters have used their Dexterity modifiers when rolling initiative. On average those modifiers [change very little with CR]({{ site.data.page-links.monster-saving-throws.path }}#fig:monster-ability-score-modifier-trends). This is not the case for MM 2024 monsters, as shown in Fig. \figref{fig:initiative-vs-cr} (below).

<figure id="fig:initiative-vs-cr">
    {% include_relative fig-initiative-vs-cr-small.html %}
    {% include_relative fig-initiative-vs-cr-large.html %}
    <figcaption>Shows average (mean) initiative bonus for MM 2014 monsters (blue) and MM 2024 monsters (orange).</figcaption>
</figure>

Initiative bonuses for PCs do increase on average as they level up, but not to nearly the same extent as shown here. This means the average position monsters have in the initiative order will improve for monsters as their CR increases, resulting in those monsters dealing more damage to the PCs as a result. 

I've been working on a post on this topic for some time now, which I hope to have done soon, but as a simple estimate a monster with an initiative bonus $$+6$$ higher than the PCs will deal around $$10\%$$ more damage on average than they would if their initiative bonuses were the same, and a monster with $$+15$$ will deal roughly $$20\%$$ more.

# Conclusion

To summarize, in most ways MM 2024 monsters appear to be built to the same targets as MM 2014 monsters were with a few exceptions. Their average saving throw bonus now scales slightly slower, and legendary monsters are now built to have around $$40\%$$ higher DPR and $$15\%$$ higher HP than their normal counterparts.

For anyone wishing to build new monsters that match this new trend for D&D 2024, here's a summary of the equations listed throughout this post for approximating each of these stats. For damage per round and hit points of non-legendary monsters,
\begin{align}
    \DPR_{\mathrm{N}} &\approx
    \begin{cases} 
        \ \ \ \ 6 + \ \  6 \cdot \CR & \CR \lt 20\,, \\\\ 
        132 + 12 \cdot \left( \CR - 20 \right) & \CR \geq 20\,, 
    \end{cases} \nonumber \\\\ 
    \HP_{\mathrm{N}} &\approx
    \begin{cases} 
        \ \ 16 + 16 \cdot \CR & \CR \lt 20\,, \\\\ 
        368 + 48 \cdot \left( \CR - 20 \right) & \CR \geq 20\,, 
    \end{cases} \nonumber 
\end{align}
and for legendary monsters,
\begin{align}
    \DPR_{\mathrm{L}} &\approx
    \begin{cases} 
        \ \ \ \ 8 + \ \  8 \cdot \CR & \CR \lt 20\,, \\\\ 
        176 + 16 \cdot \left( \CR - 20 \right) & \CR \geq 20\,, 
    \end{cases} \nonumber \\\\ 
    \HP_{\mathrm{L}} &\approx
    \begin{cases} 
        \ \ 19 + 19 \cdot \CR & \CR \lt 20\,, \\\\ 
        437 + 57 \cdot \left( \CR - 20 \right) & \CR \geq 20\,. 
    \end{cases} \nonumber 
\end{align}
And for attack bonus, save difficulty class, armor class, and saving throw bonus values,
\begin{align}
    \AB &\approx \ \ 3.5 + \CR/2 \,, \nonumber \\\\ 
    \DC &\approx    11.5 + \CR/2 \,, \nonumber \\\\ 
    \AC &\approx    13.0 + \CR/3 \,, \nonumber \\\\ 
    \SB &\approx \ \ 1.0 + \CR/3 \,. \nonumber 
\end{align}

Keep in mind, these values represent adjusted stats. If a monster has traits or abilities that let them act as though they have a higher value in any of these then the corresponding value in their stat block should be lowered to balance that out.
