---
title: "Baseline Monster Stats"
excerpt: "What are the baseline monster stats Wizards of the Coast uses for making monsters?"
date: 2023-06-27
last_modified_at: 2023-07-03
tags:
  - analysis
  - monsters
  - xp
---

{% include LaTex.html %}

# Introduction

In the "[Creating a Monster](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#CreatingaMonster)" section of chapter 9 in the _Dungeon Master's Guide_ (DMG), there's a [table](https://www.dndbeyond.com/sources/dmg/dungeon-masters-workshop#MonsterStatisticsbyChallengeRating) that gives typical stats for monsters of each challenge rating (CR). These stats can be used to build a quick monster, or to determine a homebrew monster's CR. Recently, WotC has admitted that these values don't reflect the internal rules they use for building monsters. In this post, I look at published monsters to determine what these values should be.

<!--
The CR Calculation Guide in the DMG is wrong and does not match our internal CR calculation method.
-- Jeremy Crawford at the DnD creator summit
https://twitter.com/Indestructoboy/status/1643057013683789829?s=20
-->

I've covered how published [monsters CR values hold up]({{ site.data.page-links.calculating-monster-cr.path }}) against these targets before, but in relation to [calculating monster CR]({{ site.data.page-links.calculating-monster-cr.path }}) and [calculating monster XP]({{ site.data.page-links.calculating-monster-xp.path }}). While I do provide some alternative monster XP values in the final table, the main focus here is on how monster stats scale.

I'll be covering monster [offensive stats](#offensive-stats) first (average damage per round, attack bonus, and save difficulty class), followed by [defensive stats](#defensive-stats) (average hit points, armor class, and saving throw bonuses). For offensive stats, things are pretty straight forward, but defensive stats, as I'll show, require a bit more consideration.

The monster stats covered here are pulled from official source books and adventure books published by Wizards of the Coast. You can find a summary of the dataset used for this analysis [here]({{ site.data.page-links.monster-dataset.path }}). I've presented each stat in terms of it's adjusted and unadjusted value. Unadjusted monster stats represent how each stat appears in monster stat blocks, while adjusted stats include additional contributions from monster traits and abilities as described in chapter 9 of the DMG. In most cases, the adjusted monster stat is used to determine that stat's baseline values.

For those wishing to jump straight to the final baseline value table, you can find that [here](#tab:monster-baseline-stats).

# Offensive Stats
Jumping straight in, Fig. [1](#fig:dpr-vs-cr){: .fig-ref} (below) shows that the average damage per round (DPR) for published monsters stays close to the target values in the DMG up to CR 20 where the two diverge. For CR 20 and above, the average DPR for published monsters scales slower than expected.

<figure id="fig:dpr-vs-cr">
    {% include_relative monster-baseline-stats/fig-dpr-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-dpr-vs-cr-large.html %}
    <figcaption>Figure 1: Shows average (mean) damage per round for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

The general trend appears to be that DPR increases by 6 for each CR when CR is less than 20, and then increases by 12 for each CR after that,
\begin{eqnarray}
    \DPR \approx
    \begin{cases} 
        \ \ \ \ 6 + \ \ 6 \cdot \CR & \CR \lt 20\,; \\\\ 
        132 + 12 \cdot \left( \CR - 20 \right) & \CR \geq 20\,.
    \end{cases}
    \label{eq:simplified-dpr}
\end{eqnarray}

From this alone, one might naively conclude that high CR published monsters are weaker offensively than they should be, but that depends on how other offensive stats, such as attack bonus (AB) and save difficulty class (save DC), compare to expectations.

The average AB for published monsters, as shown in Fig. [2](#fig:ab-vs-cr){: .fig-ref} (below), start off 1-2 higher than the DMG targets at low CRs, and then scales slightly faster, ending around 4 higher than target. This means, while published monsters are dealing less damage when they do hit, they are hitting more often than one might expect from the DMG target values.

<figure id="fig:ab-vs-cr">
    {% include_relative monster-baseline-stats/fig-ab-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-ab-vs-cr-large.html %}
    <figcaption>Figure 2: Shows average (mean) AB for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

In comparison, while monster save DC values scale slightly faster than the target values given in chapter 9 of the DMG, as shown in Fig. [3](#fig:dc-vs-cr){: .fig-ref} (below), they stay close to those targets across a wide range of CR. Given how few monsters have been published above CR 20, the two trends are close enough that I might consider the two equivalent were it not for the low DPR values shown previously in Fig. [1](#fig:dpr-vs-cr){: .fig-ref}.

<figure id="fig:dc-vs-cr">
    {% include_relative monster-baseline-stats/fig-dc-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-dc-vs-cr-large.html %}
    <figcaption>Figure 3: Shows average (mean) save DC for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

The reason why save DC values appear to match, while AB values don't, is made clear by comparing AB and save DC values within each group. Generally, we expect $$\DC = 8 + \AB$$, since that's how the two are related for spellcasters, as well as most player characters. And for published monsters, as shown in Fig. [4](#fig:dc-vs-ab){: .fig-ref} (below), that appears to be the case. However, for the DMG target values, this relationship doesn't hold, suggesting either the AB or save DC targets are off from what they ought to be.

<figure id="fig:dc-vs-ab">
    {% include_relative monster-baseline-stats/fig-dc-vs-ab-small.html %}
    {% include_relative monster-baseline-stats/fig-dc-vs-ab-large.html %}
    <figcaption>Figure 4: Shows average (mean) save DC vs average (mean) AB for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

Given how well the save DC targets matched the average save DC values for published monsters, I think the most likely answer is that the DMG target AB values are lower than they ought to be, and should be approximately two higher in order to match the save DC targets. This will also bring them into rough alignment with how player character attack bonuses scale from levels 1 - 20 without factoring in class features and magic items, as shown in Fig. [5](#fig:ab-vs-level){: .fig-ref} (below).

<figure id="fig:ab-vs-level">
    {% include_relative monster-baseline-stats/fig-ab-vs-level-small.html %}
    {% include_relative monster-baseline-stats/fig-ab-vs-level-large.html %}
    <figcaption>Figure 5: Shows average (mean) AB for published monsters and for player characters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

The generals for monster AB and save DC are that each increases by one every two levels, and that at CR 1 $$\AB = 4$$ and $$\DC = 12$$,
\begin{align}
    \AB &\approx \ \ 3.5 + \CR / 2 \,;  \label{eq:simplified-ab} \\\\ 
    \DC &\approx 11.5 + \CR / 2\,. \label{eq:simplified-dc}
\end{align}

Finally, we can compare the overall offensive power of published monsters and their DMG target values by calculating their effective DPR, as covered [here]({{ site.data.page-links.effective-hp-and-damage.path }}#linear-approximation),
\begin{align}
    \eDPR  &\approx \sqrt{0.65} \cdot \DPR \cdot \left(\frac{\AB + 10}{13}\right)\,.
    \label{eq:effective-dpr-approx}
\end{align}
The results of this are shown in Fig. [6](#fig:eff-dpr-vs-cr){: .fig-ref} (below). While there are some subtle differences, the average $$\eDPR$$ for published monsters follows the DMG targets quite closely, indicating the overall offensive strength of published monsters is similar to those created using chapter 9 of the DMG.

<figure id="fig:eff-dpr-vs-cr">
    {% include_relative monster-baseline-stats/fig-eff-dpr-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-eff-dpr-vs-cr-large.html %}
    <figcaption>Figure 6: Shows average (mean) effective DPR for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>


# Defensive Stats

Starting off with hit points, as shown in Fig. [7](#fig:hp-vs-cr){: .fig-ref} (below), monster adjusted hit points are significantly higher than unadjusted hit points. This is quite a departure from what we saw previously with offensive stats in the previous section, which showed little difference between adjusted and unadjusted values.

<figure id="fig:hp-vs-cr">
    {% include_relative monster-baseline-stats/fig-hp-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-hp-vs-cr-large.html %}
    <figcaption>Figure 7: Shows average (mean) hit points and adjusted hit points for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

There are several factors that contribute to this difference. Most notably, the Regeneration trait, the Legendary Resistance trait, and damage resistances/immunities that the monster might have. Whatever the sources, we're ultimately interested in the adjusted hit point trendline, which starts off at about half the DMG target and gradually grows closer until the two are equal. By around CR 15, the difference between the two is nearly negligible.

The overall trend appears to be that monster hit points start off near $$32$$, increase by $$16$$ per CR for CRs less than 20, and increase by 48 for each CR after that,
\begin{equation}
    \HP \approx 
    \begin{cases} 
        \ \ 16 + 16 \cdot \CR & \CR \lt 20\,; \\\\ 
        368 + 48 \cdot \left( \CR - 20 \right) & \CR \geq 20\,.
    \end{cases}
    \label{eq:simplified-hp}
\end{equation}

Moving on to armor class (AC), monster adjusted AC is significantly higher than unadjusted AC, as shown in Fig. [8](#fig:ac-vs-cr){: .fig-ref} (below).

<figure id="fig:ac-vs-cr">
    {% include_relative monster-baseline-stats/fig-ac-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-ac-vs-cr-large.html %}
    <figcaption>Figure 8: Shows average (mean) AC for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

The main factors that contribute to this difference include the Magic Resistance trait, which counts as a $$+2$$ AC adjustment, and monsters having multiple saving throw proficiencies, which counts as a $$+2$$ AC adjustment for having 3-4 saving throw proficiencies, and a $$+4$$ AC adjustment for 5-6 proficiencies. This is notable because these adjustments have nothing to do with a monster's defense against attack rolls.

<!--
Just like with hit points, there is a clear difference between the adjusted and unadjusted AB values. However, unlike hit points, the unadjusted values for monster AC come closest to the DMG targets. While monster unadjusted AC stays close to target at lower CRs, monster adjusted AC values are consistently 1-3 AC higher, even before the AC targets hit their maximum value at CR 17.
-->

Subtracting those saving throw adjustments off leave us with adjusted AC values very close to the unadjusted AC data shown in Fig. [8](#fig:ac-vs-cr){: .fig-ref}. For this reason, I've decided to use unadjusted AC to establish a baseline for monster AC. So long as monster saving throw bonuses are handled appropriately, this choice shouldn't negatively impact the results.

The general trend then for monster AC starts off at $$\AC = 13$$ for CR 1 and increase by one every three CR,
\begin{align}
    \AC &\approx 13 + \CR / 3 \,.  \label{eq:simplified-ac}
\end{align}

<!--
Normally, this would indicate the DMG targets are simply too low, as was the case for AB values covered previously. However, for monster AC, the overwhelming majority of the adjustments made to monster AC when calculating their CR comes from things that effect their saving throws. The two most common of these adjustments are for monsters with multiple saving throw proficiencies, and for monsters with the Magic Resistance trait.
-->

Finally, let's look at monster saving throw bonuses (SB). This one is a bit trickier than the rest we've covered so far because the DMG doesn't give any target values we can compare against. However, we can get around this by converting the target AC values in the DMG into their equivalent SB values using the following conversion, $$\SB = \AC - 14$$, taken from my post [Effective Hit Points and Damage]({{ site.data.page-links.effective-hp-and-damage.path }}#saving-throw-bonus-scaling). 

This, along with average SB values for published monsters, is shown in Fig. [9](#fig:sb-vs-cr){: .fig-ref} (below). These averages represent the average across all six saving throws, in addition to within each CR. Since monster saving throw bonuses already include adjustments based on proficiency, the only major factor we need to account for is for the Magic Resistance trait, which I've counted as a +4 SB adjustment. This is twice what the DMG gives when applied to AC but will drop to an overall adjustment of +2 when averaging between a monster's AC and SB values.

<figure id="fig:sb-vs-cr">
    {% include_relative monster-baseline-stats/fig-sb-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-sb-vs-cr-large.html %}
    <figcaption>Figure 9: Shows average (mean) AC for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>

Both the adjusted and unadjusted SB values are noticeably higher than the converted AC targets. This isn't surprising, since the adjusted AC values shown if Fig. [8](#fig:ac-vs-cr){: .fig-ref} were higher as well, due to adjustments that impact monster saving throws. In fact, if we convert the adjusted SB values shown in Fig. [9](#fig:sb-vs-cr){: .fig-ref} into their equivalent AC values, $$\AC = \SB + 14$$, and average between them and the unadjusted AC values shown in Fig. [8](#fig:ac-vs-cr){: .fig-ref}, we find the two are incredibly close to one another, as shown in Fig. [10](#fig:adj-ac-vs-cr){: .fig-ref} (below).

<figure id="fig:adj-ac-vs-cr">
    {% include_relative monster-baseline-stats/fig-adj-ac-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-adj-ac-vs-cr-large.html %}
    <figcaption>Figure 10: Shows average (mean) adjusted AC and average (mean) \((\AC + SB + 14)/2\) for published monsters, as well as target values for AC taken from chapter 9 of the DMG.</figcaption>
</figure>

The closeness of these results is reassuring. It tells us our method for separating AC and SB from one another is both accurate and consistent with how the DMG calculates adjusted AC.

Therefore, the general trend for monster SB values starts off around $$\SB=0.5$$ for CR 1 and increases by one every two levels,
\begin{align}
    \SB &\approx \CR / 2 \,.  \label{eq:simplified-sb}
\end{align}

Just like with offensive stats, we can compare the overall defensive toughness of published monsters with the DMG targets by calculating their effective hit points, as described [here]({{ site.data.page-links.effective-hp-and-damage.path }}#linear-approximation),
\begin{align}
    \eHP  &\approx \frac{1}{\sqrt{0.65}} \cdot \HP \cdot \left(\frac{\AC + 1}{13}\right)\,.
    \label{eq:effective-hp-approx}
\end{align}
The results of this, as shown in Fig. [10](#fig:eff-hp-vs-cr){: .fig-ref} (below), indicate that while low CR monsters are weaker than expected, monsters CR 20 and above are considerably tougher.

<figure id="fig:eff-hp-vs-cr">
    {% include_relative monster-baseline-stats/fig-eff-hp-vs-cr-small.html %}
    {% include_relative monster-baseline-stats/fig-eff-hp-vs-cr-large.html %}
    <figcaption>Figure 11: Shows average (mean) effective hit points for published monsters, as well as target values taken from chapter 9 of the DMG.</figcaption>
</figure>


Before concluding, there's one more point worth discussing here, and that's how monster defenses against saving throws are consistently and significantly stronger than their defenses against attacks. This fact is made clear in Fig. [12](#fig:hit-prob-vs-level){: .fig-ref} (below), which shows the average chance that a CR appropriate monster will be hit by an attack or fail a saving throw from a PC. The PC used here is assumed to starts off with a +3 attack/save modifier at 1st level, which increases to +4 at 4th level and finally to +5 at 8th level. 

<figure id="fig:hit-prob-vs-level">
    {% include_relative monster-baseline-stats/fig-hit-prob-vs-level-small.html %}
    {% include_relative monster-baseline-stats/fig-hit-prob-vs-level-large.html %}
    <figcaption>Figure 12: Shows average chance of a PC hitting a level appropriate monster with an attack, or the monster failing a saving throw against a PC's spell save DC. The PC is assumed to have a +3 attack/save modifier at 1st level, which increases to +4 at 4th level and finally to +5 at 8th level.</figcaption>
</figure>

While the probability of a monster being hit by an attack stays close to the expected baseline of $$65\%$$, the probability of a monster failing a saving throw starts off closer to $$55\%$$ and decreases to around $$45\%$$ by the time they reach level 20.

To put this into context, a spellcaster PC would need a magic item that grants them a +1-2 bonus to their spell save DC to overcome this offset at low levels. And near level 20, even a +3 bonus to their save DC wouldn't be enough to overcome this difference. At least, not on average.

<!--
Monster adjusted SB values, on the other hand, are strictly higher than the DMG targets. They also increase at a faster rate than both the DMG targets and monster AC values. The result of this, as shown in Fig. [7](#fig:hit-prob-vs-level){: .fig-ref} (below), is that published monsters, on average, have consistently stronger defenses against spells than they do attacks.
-->

These probabilities are broken down further in Fig. [13](#fig:save-fail-prob-vs-level){: .fig-ref} (below), which shows the probabilities for each ability score.

<figure id="fig:save-fail-prob-vs-level">
    {% include_relative monster-baseline-stats/fig-save-fail-prob-vs-level-small.html %}
    {% include_relative monster-baseline-stats/fig-save-fail-prob-vs-level-large.html %}
    <figcaption>Figure 13: Shows average chance of a monster failing a saving throw against a PC's spell save DC for each ability score.</figcaption>
</figure>

For the weaker saving throws, Dexterity and Intelligence stay close to $$65\%$$, while Charisma starts off near $$65\%$$ before dropping down above level 11. And for the stronger saving throw, Strength hovers around $$58\%$$, Wisdom performs similarly until around level 15 where it drops closer to $$50\%$$, and Constitution starts of near $$50\%$$, before dropping towards $$40\%$$ near level 20.

Whether these results are intentional or not is hard to tell. But, for the purpose of making monsters, I think it is valuable to know that publish monsters have higher resilience against saving throws than they do attacks, and that certain ability scores are stronger than others in this regard.

<!--
Part of this comes from the increase frequency of the Magic Resistance trait in monsters, which is valued as a $$+4$$ to a monster's SB, and part of it comes from the increased frequency of saving throw proficiencies as well as how proficiency bonuses scale with monster CR (see my post on [monster saving throws]({{ site.data.page-links.monster-saving-throws.path }})).
-->

# Conclusion
To summarize, published monsters do, in fact, deviate from the baseline stats given in chapter 9 of the DMG. To a simple approximation, monster damage per round and hit points scale with CR in the following ways,
\begin{align}
    \DPR &\approx
    \begin{cases} 
        \ \ \ \ 6 + \ \  6 \cdot \CR & \CR \lt 20\,; \\\\ 
        132 + 12 \cdot \left( \CR - 20 \right) & \CR \geq 20\,,
    \end{cases} \\\\ 
    \HP &\approx
    \begin{cases} 
        \ \ 16 + 16 \cdot \CR & \CR \lt 20\,; \\\\ 
        368 + 48 \cdot \left( \CR - 20 \right) & \CR \geq 20\,,
    \end{cases}
\end{align}
and for attack bonus, save DC, armor class, and saving throw bonus values,
\begin{align}
    \AB &\approx \ \ 3.5 + \CR/2 \,, \\\\ 
    \DC &\approx    11.5 + \CR/2 \,, \\\\ 
    \AC &\approx    13.0 + \CR/3 \,, \\\\ 
    \SB &\approx \ \ 0.0 + \CR/2 \,. 
\end{align}

Alternatively, if you want more precise fits to the data, the [Monster Baseline Stats](#tab:monster-baseline-stats) table (below) gives values based on fitting the adjusted hit points, unadjusted AC, adjusted SB, adjusted DPR, adjusted AB, and adjusted DC values from published monsters show in the previous two sections. It also uses those values to calculate new monster XP values using the XP formula discussed in my post on [Calculating Monster XP]({{ site.data.page-links.calculating-monster-xp.path }}#calculating-xp).

<div class="dataframe center" style="width:100%;">
    <h3 id="tab:monster-baseline-stats">Monster Baseline Stats</h3>
    {% include_relative monster-baseline-stats/tab-monster-baseline-stats.html %}
</div>

When using this table to calculate a monster's CR, you can follow the same guidelines in chapter 9 of the DMG. However, instead of increasing the monster's defensive CR by 1 for every two higher their adjusted AC is from the baseline associated with their adjusted hit points, increase it by $$1/2$$ and do the same for their adjusted SB value.

For example, a monster with 180 adjusted hit points would have an initial defensive CR of 10, which has a baseline AC of 17 and SB of +5. If the monster then has an adjusted AC of 19 and an average adjusted SB of +7, then each would add $$1/2$$ to that initial defensive CR, bringing their final defensive CR to 11.

Given the added complexity of this, I can understand why the designers at Wizards of the Coast might have opted for merging AC and SB in their baseline monster table.