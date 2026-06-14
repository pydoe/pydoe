# Important Factors: Half-Normal Probability Plot

*Purpose*
The [half-normal probability plot](../advanced-topics/eda-half-normal-plot.md)
is used to distinguish between important and unimportant effects.

*Sample Half-Normal Probability Plot*
[![the half-normal probability plot identifies the important factors](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/probpl_r.gif)](inn/gifs/probpl_f.gif)

*Conclusions from the Half-Normal Probability Plot*
We can make the following conclusions from the half-normal
probability plot.

- The points in the plot divide into two clear clusters:

- An upper cluster (|effect| > 60).
          - A lower cluster (|effect| < 20).

- The upper cluster contains the effects:

$X_2$, $X_7$, $X_1$*$X_3$ (and confounding),
          $X_1$, $X_3$, $X_2$*$X_3$ (and confounding),
          $X_1$*$X_2$ (and confounding)

These effects should definitely be considered important.

- The remaining effects lie on a line and form a lower cluster.
       These effects are declared relatively unimportant.

- The effect id's and the confounding structure are given on
       the far right (e.g., 13:13+27+46).
