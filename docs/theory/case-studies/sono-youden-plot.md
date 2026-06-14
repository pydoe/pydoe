# Important Factors: Youden Plot

*Purpose*
The [DOE Youden plot](../advanced-topics/eda-youden-plot.md) is used
to distinguish between important and unimportant factors.

*Sample Youden Plot*
[![the Youden plot identifies the important factors](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/youden_r.gif)](inn/gifs/youden_f.gif)

*Conclusions from the Youden plot*
We can make the following conclusions from the Youden plot.

- In the upper left corner are the interaction term
       $X_1$*$X_3$ and the main effects $X_1$ and $X_3$.

- In the lower right corner are the main effects $X_2$ and
       $X_7$ and the interaction terms $X_2$*$X_3$
       and $X_1$*$X_2$.

- The remaining terms are clustered in the center, which
       indicates that such effects have averages that are
       similar (and hence the effects are near zero),
       and so such effects are relatively unimportant.

- On the far right of the plot, the confounding structure is
       given (e.g., 13: 13+27+46), which suggests that the information
       on $X_1$*$X_3$ (on the plot) must be tempered with the
       fact that $X_1$*$X_3$ is confounded with
       $X_2$*$X_7$ and $X_4$*$X_6$.
