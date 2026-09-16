---
title: "Adventure Encounter Monsters"
excerpt: "An analysis of how monsters are used in encounters in official 5e adventures."
permalink: /:collection/:name/
date: 2026-09-16
last_modified_at: 2026-09-16
header:
  og_image: /assets/images/adventure-encounter-monsters.png
tags:
  - analysis
  - adventures
  - combat
  - encounters
  - monsters
  - xp
---

# Introduction

In my previous post [Adventure Encounter Difficulties]({{ site.data.page-links.adventure-encounter-difficulties.path }}), I looked at the difficulties of combat encounters from official D&D 5th edition (5e) adventures published by Wizards of the Coast (WotC). This post I expands on that analysis by looking at how monsters are used in those encounters.

As with that post, you can find a summary of the encounter dataset used for this analysis [here]({{ site.data.page-links.encounters-dataset.path }}). The difficulties for these encounters were calculated relative to a party of five PCs using the 2014 rules for building encounters.

# Encounter Composition

The difficutly of combat encounters in 5e depends on the composition of monsters in the encounter, i.e., the number of monsters and their individual challenge ratings (CR). In this section I break down those aspect of the combat encounters published by WotC.

At any level of play a party of PCs will face monsters from a wide range of CRs. While it's common to imagine this range to be roughly centered around a CR equal to the party's average PC level this isn't the case for combat encounters from official 5e adventures as shown in Fig. \figref{fig:monster-cr-range-vs-level} (below).

<figure id="fig:monster-cr-range-vs-level">
    {% include_relative fig-monster-cr-range-vs-level-small.html %}
    {% include_relative fig-monster-cr-range-vs-level-large.html %}
    <figcaption>Median monster CR (line) and 60% confidence interval (shaded) as a function of party level for combat encounters found in adventure books published by WotC.</figcaption>
</figure>

Not only is the median monster CR significantly below the party's level, so too is the 80th percentile. In fact, on average around $$93\%$$ of monsters the PCs face in official adventures have CR below the expected party level of the adventure.

The gap between the party's level and the average monster CR also grows as the party goes up in level. This can give the impression that the average monster gets weaker relative to the PCs as they level up, but that's not, in fact, the case. This is because a monster's strength in combat is generally proportional to their XP value and not their CR.

If we look at how monster XP values scale relative to the PCs XP thresholds, as shown in Fig. \figref{fig:monster-xp-range-vs-level} (below), we see that the average monster for each level tends to hover around $$20\%$$ of a single PC's encounter XP budget (i.e., half their adventuring day XP budget).

<figure id="fig:monster-xp-range-vs-level">
    {% include_relative fig-monster-xp-range-vs-level-small.html %}
    {% include_relative fig-monster-xp-range-vs-level-large.html %}
    <figcaption>Median monster XP normalized to half the adventuring day XP of a single PC (line) and 60% confidence interval (shaded) as a function of party level for combat encounters found in adventure books published by WotC. Dashed line denotes the normalized XP for a monster with CR equal to the party level.</figcaption>
</figure>

If we break things down by encounter difficulty, as shown in Fig. \figref{fig:monster-xp-vs-level-by-difficulty}, a more nuanced picture emerges. The average monster per encounter gets stronger as the difficulty increases, an effect that gets more pronounced as the PCs level up. For example, a typical monster in a Deadly encounter at level 1 is worth roughly twice the XP of a typical monster from an Easy encounter, and at level 20 it's worth roughly four times the XP instead.

<figure id="fig:monster-xp-vs-level-by-difficulty">
    {% include_relative fig-monster-xp-vs-level-by-difficulty-small.html %}
    {% include_relative fig-monster-xp-vs-level-by-difficulty-large.html %}
    <figcaption>Median monster XP normalized to half the adventuring day XP of a single PC as a function of party level for combat encounters found in adventure books published by WotC. Dashed line denotes the normalized XP for a monster with CR equal to the party level.</figcaption>
</figure>

We can see this trend reflected in the number of monsters per encounter shown in Fig. \figref{fig:monsters-per-encounter-by-difficulty} (below). At low levels, where the differences in the average monster XP for each difficulty is small, the number of monsters per encounter increases significantly with the encounter difficulty. As the party's level increases this gap becomes smaller and smaller until it eventually inverts around level 14. By level 20 Hard encounters tend to have one fewer monsters than Easy encounters do. 

<figure id="fig:monsters-per-encounter-vs-level-by-difficulty">
    {% include_relative fig-monsters-per-encounter-vs-level-by-difficulty-small.html %}
    {% include_relative fig-monsters-per-encounter-vs-level-by-difficulty-large.html %}
    <figcaption>Average number of monsters per encounter as a function of party level for combat encounters found in adventure books published by WotC.</figcaption>
</figure>

Put another way, at low levels higher difficulty encounters tend to be constructed by increasing the number of monsters, and at high levels they tend to be constructed by increasing the strength of the individual monsters.

Before wrapping up this section I think it's important to take a look at how Fig. \figref{fig:monsters-per-encounter-vs-level-by-difficulty} is a bit misleading. It can be tempting to look at Fig. \figref{fig:monsters-per-encounter-vs-level-by-difficulty} and read it to mean that a "typical" encounter will have around four monsters in it, but that's not actually the case. If we look at the distribution of monsters per encounter, as shown in Fig. \figref{fig:monsters-per-encounter-by-difficulty} (below), we see that the most common number of monsters is just one for Easy, Medium, and Hard difficulties. It's not until the difficulty reaches Deadly and above that it shifts away from one monster to three monsters.

<figure id="fig:monsters-per-encounter-by-difficulty">
    {% include_relative fig-monsters-per-encounter-by-difficulty-small.html %}
    {% include_relative fig-monsters-per-encounter-by-difficulty-large.html %}
    <figcaption>Distribution of combat encounters based on the number of monsters they have for combat encounters found in adventure books published by WotC.</figcaption>
</figure>

The reason why the average number of monsters per encounter ends up around four, as shown previously in Fig. \figref{fig:monsters-per-encounter-vs-level-by-difficulty}, is that the tail of the distributions shown in Fig. \figref{fig:monsters-per-encounter-by-difficulty} is long. And a big reason for that boils down to how the 2014 encounter building rules handle groups of monsters when determining the encounter's difficulty.

# Monster Stats

In this section I'd like to expand on the observation made in the previous section regarding Fig. \figref{fig:monster-cr-range-vs-level}, that the average CR for monsters is significantly lower than the expected party level for official 5e adventures. This results impacts all monster stats, but for the purposes of this post I've focused on how it impacts the chance to hit for both PCs and monsters. The game's math is generally centered around an average chance to hit of $$65\%$$ for PCs and monsters, and deviations from that can skew the accuracy of encounter difficulty calculations as I covered in my previous post [XP Approximations]({{ site.data.page-links.xp-approximations.path }}).

If we look at monster attack bonuses, as shown in Fig. \figref{fig:monster-adj-ab-vs-level} (below), we can see on average, and across all difficulties, the attack bonuses faced by the PCs in WotC adventures are significantly lower than the baseline average (i.e., when monster CR equals the PCs' level). This effect is most pronounced for monsters in Easy encounters and gets gradually less as the encounter difficulty increases, but even for Deadly encounters the average hovers around 3 below the baseline.

<figure id="fig:monster-adj-ab-vs-level">
    {% include_relative fig-monster-adj-ab-vs-level-small.html %}
    {% include_relative fig-monster-adj-ab-vs-level-large.html %}
    <figcaption>Average monster attack bonus for combat encounters found in adventure books published by WotC for Easy encounters (blue), Medium encounters (Yellow), Hard encounters (Green), and Deadly encounters (Red), along with the average attack bonus for all monsters published by WotC (black).</figcaption>
</figure>

The impact this has on monster chance to hit can be seen in Fig. \figref{fig:monster-hit-prob-vs-level-by-difficulty} (below). This calculation uses the PC armor class values from [Baseline Player Character Stats]({{ site.data.page-links.baseline-player-character-stats.path }}).

At low levels the average chance to hit for monsters is just a bit below the baseline at around $$50\%$$, but as the players level up it only increases slightly. While the baseline chance to hit increases above $$80\%$$ at high levels, the chance to hit for monsters in WotC adventures barely eclipses $$60\%$$ and only for Hard and Deadly encounters.

<figure id="fig:monster-hit-prob-vs-level-by-difficulty">
    {% include_relative fig-monster-hit-prob-vs-level-by-difficulty-small.html %}
    {% include_relative fig-monster-hit-prob-vs-level-by-difficulty-large.html %}
    <figcaption>Average monster chance to hit a PC for combat encounters found in adventure books published by WotC for Easy encounters (blue), Medium encounters (Yellow), Hard encounters (Green), and Deadly encounters (Red), along with the average attack bonus for all monsters published by WotC (black).</figcaption>
</figure>

Across the full level range the average chance to hit for the baseline is $$68.5\%$$, which is just a bit higher than the $$65\%$$ center point for the game's math, while the average chance to hit is $$49.7\%$$ monsters in Easy encounters, $$53.4\%$$ for Medium encounters, $$56.3\%$$ for Hard encounters, and $$56.7\%$$ for Deadly encounters.

Note, these chance to hit values don't assume the PCs having magic items capable of increasing their armor class. For campaigns that provide the PCs with such magic items the chance to hit will be lower, especially at higher levels where the PCs are more likely to have such items.

Turning our attention to monster armor class values, a slightly different picture emerges as shown in Fig. \figref{fig:monster-adj-ac-vs-level} (below). Like attack bonus the average armor class for monsters falls noticeably below the baseline value. However, unlike attack bonus this gap stays roughly constant as the PCs level up.

<figure id="fig:monster-adj-ac-vs-level">
    {% include_relative fig-monster-adj-ac-vs-level-small.html %}
    {% include_relative fig-monster-adj-ac-vs-level-large.html %}
    <figcaption>Average monster armor class for combat encounters found in adventure books published by WotC for Easy encounters (blue), Medium encounters (Yellow), Hard encounters (Green), and Deadly encounters (Red), along with the average attack bonus for all monsters published by WotC (black).</figcaption>
</figure>

The effect this has on the PCs average chance to hit is shown in Fig. \figref{fig:pc-hit-prob-vs-level-by-difficulty} (below). This calculation, again, uses the PC attack bonus values from [Baseline Player Character Stats]({{ site.data.page-links.baseline-player-character-stats.path }}).

<figure id="fig:pc-hit-prob-vs-level-by-difficulty">
    {% include_relative fig-pc-hit-prob-vs-level-by-difficulty-small.html %}
    {% include_relative fig-pc-hit-prob-vs-level-by-difficulty-large.html %}
    <figcaption>Average PC chance to hit against monsters from combat encounters found in adventure books published by WotC for Easy encounters (blue), Medium encounters (Yellow), Hard encounters (Green), and Deadly encounters (Red), along with the average attack bonus for all monsters published by WotC (black).</figcaption>
</figure>

While these values are only a little higher than the baseline chance to hit, they're all generally close to the $$65\%$$ center point for the games math. Across the full level range the average PC chance to hit is $$71.5\%$$ for monsters in Easy encounters, $$68.7\%$$ for Medium encounters, $$68.0\%$$ for Hard encounters, and $$66.1\%$$ for Deadly encounters. The baseline chance to hit has an average value of $$60.3\%$$, which is similarly close to the center point of $$65\%$$, but on the lower side of the spectrum.

Just like with the monster's chance to hit, these values assume the PCs have no magic items capable of increasing their chance to hit. For adventures that include such magic items the PCs' chance to hit would be even higher, possibly pushing above $$80\%$$ by level 20.

# Conclusion

The average monster CR faced by the PCs in published adventures for 5e from WotC falls significantly below the expected party level across all level of play. The result of this is that the average chance to hit for both monsters and PCs differs from the game's center point of around $$65\%.$$

The way the game calculates monster XP values generally undervalues differences in change to hit from the assumed center point, causing it to overestimate the difficulty of monsters with CRs below the party's level and underestimate those above it (see [XP Approximations]({{ site.data.page-links.xp-approximations.path }})). Therefore, it's likely that a significant portion of the combat encounters in these adventures are somewhat easier in practice than they appear on paper.

Before ending this post, I think it's worth putting these results in context. This outcome was essentially inevitable given how encounter building works.

To a simple approximation the average XP for a Deadly encounter is about three times the XP of a single monster whose CR equals the party level for a party of five PCs. If we ignore the encounter XP multiplier, which will bring these values down, the average monster CR will drop below the party's level when the average number of monsters per encounter exceeds three. For Hard encounters this threshold drops to an average of 2 monsters per encounter, then to 1.5 For Medium encounters, and finally to just 1 for Easy encounters.

Therefore, the only way to produce encounters that don't result in an average monster CR significantly below the party's level is to heavily favor higher difficulty encounters and to restrict the vast majority of encounters to having only a small number of monsters in them.

<!--
## math

{% include LaTex.html %}

These results aren't at all unexpected and are largely the result of how encounters are designed according to the rules. 

To explain, if we wanted to build an encounter of a specific difficulty we would add monsters to the encounter until the adjusted XP total fell within the XP range for that difficulty. If we ignore the range aspect to this and think of an XP target instead then the average XP per monster $$(\XP_{\mathrm{m}})$$ will depend on the number of monsters $$(n)$$ in the following way,
\begin{align}
    \XP_{\mathrm{m}} (n) = \frac{ \XP }{ n \, \EM(n) }\,.
\end{align}
Here, $$\EM$$ is the encounter multiplier described in the 2014 encounter building rules.

For a collection of encounters, all targeting the same difficulty, but covering a range of different encounter sizes (i.e., with different number of monsters in them) the average monster XP $$\XP_{\mathrm{m}}$$ can be calculated from
\begin{align}
    \XP_{\mathrm{m}} = \frac{ \XP_{\mathrm{t}} }{ n_{\mathrm{m}} } \,,
\end{align}
where $$XP_{\mathrm{t}}$$ is the average XP total available for monsters (after being reduced by the encounter multiplier) and $$n_{\mathrm{m}}$$ is the average encounter size.

The average XP total available for monsters for the collection can be calculated as
\begin{align}
    \XP_{\mathrm{t}}
        &= \sum_{n} P(n) \, n \, \XP_{\mathrm{m}} (n) \nonumber \\\\ 
        &= \XP \sum_{n}  \frac{ P(n) }{ \EM(n) }\,,
        \label{eq:mean-monster-xp-total}
\end{align}
and the average encounter size as
\begin{align}
    n_{\mathrm{m}} = \sum_{n} P(n) \, n\,.
    \label{eq:mean-monsters-per-encounter}
\end{align}
In both of these equations $$P(n)$$ represents the fraction of encounters with $$n$$ monsters in it.

The roll of the encounter XP multiplier, $$\EM,$$ is fairly straight forward. It reduces the total XP available for monsters, $$\XP_{\mathrm{t}},$$ and therefore $$\XP_{\mathrm{m}}.$$ How much depends on how $$\EM$$ scales with the number of monsters, as well as on how the collection of encounters is distributed across the various encounter sizes through $$P(n).$$ If encounters with large $$\EM$$ values are common then $$\XP_{\mathrm{m}}$$ will be significantly lower than it would be if they weren't.

The distribution of encounter sizes, i.e., $$P(n),$$ also affects $$\XP_{\mathrm{m}}$$ through $$n_{\mathrm{m}}$$ in Eqn. \eqref{eq:mean-monsters-per-encounter}. As encounters with more monsters in them become more common $$n_{\mathrm{m}}$$ increase and $$\XP_{\mathrm{m}}$$ goes down as a result.
-->