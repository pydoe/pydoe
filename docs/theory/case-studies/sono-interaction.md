# Interaction Effects

*Check for Interaction Effects: DOE Interaction Plot*
In addition to the main effects, it is also important to check
for interaction effects, especially 2-factor interaction effects.
The [DOE interaction effects
plot](../advanced-topics/eda-interaction-plot.md) is an effective tool for this.

The seven diagonal plots are a replotting of the main effects. They
are plots of the average response versus each of the seven
factors.  The off-diagonal plots have the average response
(vertically) versus the interaction (= the cross-product here)
horizontally.  Thus for the middle plot on the top, the horizontal
axis is X1*X2, where X1 takes on values -1 and +1, X2
takes on -1 and +1, and thus X1*X2 takes on values -1 and +1.

The legend within each plot is the least squares estimate of the
factor (or interaction) effect.  In this orthogonal design case, the
estimated effect is identical to the difference of the mean values.

[![DOE mean interaction effects plot](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/dexeff_r.gif)](inn/gifs/dexeff_f.gif)

*Conclusions from the DOE Interaction Effects Plot*
We make the following conclusions from the DOE interaction
effects plot.

- Important Factors: Looking for the plots that have the steepest
       lines (that is, the largest effects), and noting that the legends
       on each subplot give the estimated effect, we have that

- The diagonal plots are the main effects.  The important
              factors are: $X_2$, $X_7$, $X_1$, and
              $X_3$.  These four factors have |effect| > 60.  The
              remaining three factors have |effect| < 10.

- The off-diagonal plots are the 2-factor interaction
              effects.  Of the 21 2-factor interactions, 9 are nominally
              important, but they fall into three groups of three:

- $X_1$*$X_3$, $X_4$*$X_6$,
                     $X_2$*$X_7$ (effect = 70)
                 - $X_2$*$X_3$, $X_4$*$X_5$,
                     $X_1$*$X_7$ (effect approximately 63.5)
                 - $X_1$*$X_2$, $X_5$*$X_6$,
                     $X_3$*$X_7$ (effect = -59.6)

All remaining 2-factor interactions are small having an
              |effect| < 20.  A virtue of the interaction effects
              matrix plot is that the confounding structure of
              this Resolution IV design can be read off the plot.  In
              this case, the fact that $X_1$*$X_3$,
              $X_4$*$X_6$, and $X_2$*$X_7$ all
              have effect estimates identical to 70 is not a
              mathematical coincidence.  It is a reflection of the
              fact that for this design, the three 2-factor interactions
              are confounded.  This is also true for the other two
              sets of three ($X_2$*$X_3$, $X_4$*$X_5$,
              $X_1$*$X_7$, and $X_1$*$X_2$,
              $X_5$*$X_6$, $X_3$*$X_7$).

- Best Settings: Reading down the diagonal plots, we select,
       as before, the best settings "on the average":

($X_1$,$X_2$,$X_3$,$X_4$,$X_5$,$X_6$,$X_7$)
           = (+,-,+,+,+,-,-)

For the more important factors ($X_1$, $X_2$, $X_3$,
       $X_7$), we note that the best settings (+, -, +, -) are
       consistent with the best settings for the 2-factor interactions
       (cross-products):

$X_1$: +, $X_2$: - with $X_1$*$X_2$: -

$X_1$: +, $X_3$: + with $X_1$*$X_3$: +

$X_1$: +, $X_7$: - with $X_1$*$X_7$: -

$X_2$: -, $X_3$: + with $X_2$*$X_3$: -

$X_2$: -, $X_7$: - with $X_2$*$X_7$: +

$X_3$: +, $X_7$: - with $X_3$*$X_7$: -
