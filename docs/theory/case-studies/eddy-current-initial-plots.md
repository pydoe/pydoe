# Initial Plots and Main Effects

*Plot the Data: Ordered Data Plot*
The first step in the analysis is to generate an
[ordered data plot](../advanced-topics/eda-ordered-data-plot.md).

[![The ordered data plot shows factor 1 clearly important, factor 2
          somewhat important](https://www.itl.nist.gov/div898/handbook/pri/section6/pri612_r01.gif)](splett3/gifs/order_f.gif)

*Conclusions from the Ordered Data Plot*
We can make the following conclusions based on the ordered data
plot.

- Important Factors: The four highest response values have
       $X_1$ = + while the four lowest response values have
       $X_1$ = -.  This implies $X_1$ is the most important
       factor.  When $X_1$ = -, the - values of $X_2$ are
       higher than the + values of $X_2$.  Similarly, when
       $X_1$ = +, the - values of $X_2$ are higher
       than the + values of $X_2$.  This implies $X_2$ is
       important, but less so than $X_1$.  There is no clear
       pattern for $X_3$.

- Best Settings: In this experiment, we are using
       the device as a detector, and so high sensitivities are
       desirable.  Given this, our first pass at best settings
       yields ($X_1$ = +1, $X_2$ = -1, $X_3$ = either).

*Plot the Data: DOE Scatter Plot*
The next step in the analysis is to generate a
DOE scatter plot.

[![plot shows clear effect for factor 1, less clear for factors 2 and 3](https://www.itl.nist.gov/div898/handbook/pri/section6/pri612_r02.gif)](splett3/gifs/dexsct_f.gif)

*Conclusions from the DOE Scatter Plot*
We can make the following conclusions based on the DOE scatter
plot.

- Important Factors: $X_1$ (Number of Turns) is clearly
       important.  When $X_1$ = -1, all four senstivities are low, and
       when $X_1$ = +1, all four sensitivities are high.  $X_2$
       (Winding Distance) is less important.  The four sensitivities for
       $X_2$ = -1 are slightly higher, as a group, than the four
       sensitivities for $X_2$ = +1.  $X_3$ (Wire Gauge) does
       not appear to be important at all.  The sensitivity is about the
       same (on the average) regardless of the settings for $X_3$.

- Best Settings: In this experiment, we are using
       the device as a detector, so high sensitivities are
       desirable.  Given this, our first pass at best settings
       yields ($X_1$ = +1, $X_2$ = -1, $X_3$ = either).

- There does not appear to be any significant outliers.

*Check for Main Effects: DOE Mean Plot*
One of the primary questions is: what are the most important
factors?  The ordered data plot and the DOE scatter plot provide useful
summary plots of the data.  Both of these plots indicated
that $X_1$ is clearly important, $X_2$ is somewhat
important, and $X_3$ is probably not important.

The [DOE mean plot](../advanced-topics/eda-mean-plot.md) shows
the main effects.  This provides probably the easiest to
interpret indication of the important factors.

[![plot shows factor 1 is most significant, factor 2 next most
          significant, factor 3 least significiant](https://www.itl.nist.gov/div898/handbook/pri/section6/pri612_r03.gif)](splett3/gifs/dexmea_f.gif)

*Conclusions from the DOE Mean Plot*
The DOE mean plot (or main effects plot) reaffirms the ordering of
the DOE scatter plot, but additional information is gleaned
because the eyeball distance between the mean values gives an
approximation to the least-squares estimate of the factor
effects.

We can make the following conclusions from the DOE mean plot.

- Important Factors:

$X_1$ (effect = large: about 3 ohms)

$X_2$ (effect = moderate: about -1 ohm)

$X_3$ (effect = small: about 1/4 ohm)

- Best Settings: As before, choose the factor settings
       that (on the average) maximize the sensitivity:

($X_1$,$X_2$,$X_3$) = (+,-,+)

*Comparison of Plots*
All of these plots are used primarily to detect the most
important factors.  Because it plots a summary statistic rather
than the raw data, the DOE mean plot shows the main effects most
clearly.  However, it is still recommended to generate either the
ordered data plot or the DOE scatter plot (or both).  Since these
plot the raw data, they can sometimes reveal features of the
data that might be masked by the DOE mean plot.
