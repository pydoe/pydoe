# Interaction Effects

*Check for Interaction Effects: DOE Interaction Plot*
In addition to the main effects, it is also important to check
for interaction effects, especially two-factor interaction effects.
The
[DOE interaction effects plot](../advanced-topics/eda-interaction-plot.md)
is an effective tool for this.  The effects on the plot represent
the change in sensitivity from low to high levels of the factors.

The three diagonal plots are a replotting of the main effects. They
are plots of the average response versus each of the three
factors.  The off-diagonal plots have the average response
(vertically) versus the interaction (= the cross-product here)
horizontally.  Thus for the middle plot on the top, the horizontal
axis is X1*X2, where X1 takes on values -1 and +1, X2
takes on -1 and +1, and thus X1*X2 takes on values -1 and +1.

The legend within each plot is the least squares estimate of the
factor (or interaction) effect.  In this orthogonal design case, the
estimated effect is identical to the difference of the mean values.

[![the DOE mean interaction effects reveals no significant
         interaction effects](https://www.itl.nist.gov/div898/handbook/pri/section6/pri613_r01.gif)](splett3/gifs/dexeff_f.gif)

*Conclusions from the DOE Interaction Effects Plot*
We can make the following conclusions from the DOE interaction
effects plot.

- Important Factors: Looking for the plots that have the steepest
       lines (that is, largest effects), we note that:

- $X_1$ (number of turns) is the most important effect:
              estimated effect = -3.1025;
          - $X_2$ (winding distance) is next most important:
              estimated effect = -0.8675;
          - $X_3$ (wire gauge) is relatively unimportant;
          - All three two-factor interactions are relatively
              unimporant.

- Best Settings: As with the main effects plot, the best
       settings to maximize the sensitivity are

($X_1$,$X_2$,$X_3$) = (+1,-1,+1)

but with the $X_3$ setting of +1 mattering little.
