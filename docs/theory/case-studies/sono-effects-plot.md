# Important Factors: |Effects| Plot

*Purpose*
The [|effects| plot](../advanced-topics/eda-effects-plot.md) displays the
results of a Yates analysis
in both a tabular and a graphical format.  It is used to distinguish
between important and unimportant effects.

*Sample |Effects| Plot*
[![the |effects| plot identifies the important factors](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/effect_r.gif)](inn/gifs/effect_f.gif)

*Conclusions from the |effects| plot*
We can make the following conclusions from the |effects| plot.

- A ranked list of main effects and interaction terms is:

$X_2$

$X_7$

$X_1$*$X_3$ (confounded with $X_2$*$X_7$
              and $X_4$*$X_6$)

$X_1$

$X_3$

$X_2$*$X_3$ (confounded with $X_4$*$X_5$
              and $X_1$*$X_7$)

$X_1$*$X_2$ (confounded with $X_3$*$X_7$
              and $X_5$*$X_6$)

$X_3$*$X_4$ (confounded with $X_1$*$X_6$
              and $X_2$*$X_5$)

$X_1$*$X_4$ (confounded with $X_3$*$X_6$
              and $X_5$*$X_7$)

$X_6$

$X_5$

$X_1$*$X_2$*$X_4$ (confounded with other
              3-factor interactions)

$X_4$

$X_2$*$X_4$ (confounded with $X_3$*$X_5$
              and $X_6$*$X_7$)

$X_1$*$X_5$ (confounded with $X_2$*$X_6$
              and $X_4$*$X_7$)

- From the graph, there is a clear dividing line between the
       first seven effects (all |effect| > 50) and the last eight
       effects (all |effect| < 20).  This suggests we retain the
       first seven terms as "important" and discard the remaining
       as "unimportant".

- Again, the confounding structure on the right reminds us that,
       for example, the nominal effect size of 70.0125 for
       $X_1$*$X_3$ (molarity*pH) can come from an
       $X_1$*$X_3$ interaction, an $X_2$*$X_7$
       (solute*clamping) interaction, an $X_4$*$X_6$
       (gas*horn depth) interaction, or any mixture of the three
       interactions.
