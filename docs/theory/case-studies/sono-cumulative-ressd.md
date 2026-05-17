# Cumulative Residual Standard Deviation Plot

*Purpose*
The [cumulative residual standard
deviation plot](../advanced-topics/eda-cumulative-ressd-plot.md) is used to identify the best (parsimonious) model.

*Sample Cumulative Residual Standard Deviation Plot*
[![the cumulative residual standard deviation plot identifies the
 best models](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/cumres_r.gif)](inn/gifs/cumres_f.gif)

*Conclusions from the Cumulative Residual SD Plot*
We can make the following conclusions from the cumulative
residual standard deviation plot.

- The baseline model consisting only of the average
       ($\scriptsize \hat{Y}$
        (
       = 110.6063) has a high residual standard deviation (95).

- The cumulative residual standard deviation shows a significant
       and steady decrease as the following terms are added to the
       average: $X_2$, $X_7$, $X_1$*$X_3$, $X_1$,
       $X_3$, $X_2$*$X_3$, and $X_1$*$X_2$.
       Including these terms reduces the cumulative residual standard
       deviation from approximately 95 to approximately 17.

- Exclude from the model any term after $X_1$*$X_2$ as
       the decrease in the residual standard deviation becomes
       relatively small.

- From the [|effects|](sono-effects-plot.md) plot, we see
       that the average is 110.6063, the estimated $X_2$ effect is
       -78.6126, and so on. (The model coefficients are one half of the
       effect estimates.)  We use this to from the following
       prediction equation:

$\begin{eqnarray*}
             \hat{Y} & = & 110.6063 - 39.3063 X_2 - 39.0563 X_7 + \\
                     &   & 35.00625 X_1 X_3 + 33.106245 X_1 +
                           31.90625 X_3 - \\
                     &    & 31.7313 X_1 X_5 - 29.781 X_1 X_2
             \end{eqnarray*}$

          

Note that $X_1$*$X_3$ is confounded with
       $X_2$*$X_7$ and $X_4$*$X_6$, $X_1$*$X_5$
       is confounded with $X_2$*X6 and $X_4$*$X_7$, and
       $X_1$*$X_2$ is confounded with $X_3$*$X_7$ and
       $X_5$*$X_6$.

From the above graph, we see that the residual standard
       deviation for this model is approximately 17.

The multiplicity of confounding terms in the model can be
       simplified by engineering judgment, numerical considerations,
       or additional data.  Numerics suggest that X4*X6 be dropped
       since neither X4 nor X6 by itself is important.  Likewise,
       X5*X6 should be dropped since neither of the main factors
       X5 and X6 are important.
