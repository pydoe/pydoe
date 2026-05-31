# Next Step: DOE Contour Plot

*Purpose*
The [DOE contour plot](../advanced-topics/eda-contour-plot.md) is used
to determine the best factor settings for the two most important
factors in the next iteration of the experiment.

From the previous plots, we identified $X_2$ (solute) and $X_7$
(horn depth) as the two most important factors.

*Sample DOE Contour Plot*
[![the DOE contour plot identifies best settings for 2 most
 important factors X2 and X7](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/dexcon_r.gif)](inn/gifs/dexcon_f.gif)

*Conclusions from the DOE Contour Plot*
We can make the following conclusions from the DOE contour plot.

- The best (high light intensity) setting for $X_2$ is "-"
       and the best setting for $X_7$ is "-".  This combination
       yields an average response of approximately 224.  The next
       highest average response from any other combination of these
       factors is only 76.

- The non-linear nature of the contour lines implies that the
       $X_2$*$X_7$ interaction is important.

- On the left side of the plot from top to bottom, the contour
       lines start at 0, increment by 50 and stop at 400.  On the
       bottom of the plot from right to left, the contour lines start
       at 0, increment by 50 and stop at 400.

To achieve a light intensity of, say 400, this suggests an
       extrapolated best setting of ($X_2$, $X_7$) = (-2,-2).

- Such extrapolation only makes sense if $X_2$ and $X_7$
       are continuous factors.  Such is not the case here.  In this
       example, $X_2$ is solute (-1 = sugar and +1 = glycerol) and
       $X_7$ is flask clamping (-1 is unclamped and +1 is clamped).
       Both factors are discrete, and so extrapolated settings are not
       possible.
