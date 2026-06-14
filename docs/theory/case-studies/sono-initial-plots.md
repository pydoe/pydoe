# Initial Plots and Main Effects

*Plot the Data: Ordered Data Plot*
The first step in the analysis is to generate an
[ordered data plot](../advanced-topics/eda-ordered-data-plot.md).

[![The ordered data plot shows two points that clearly stand out](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/order_r.gif)](inn/gifs/order_f.gif)

*Conclusions from the Ordered Data Plot*
We can make the following conclusions based on the ordered data
plot.

- Two points clearly stand out.  The first 13 points lie in the
       50 to 100 range, the next point is greater than 100, and the
       last two points are greater than 300.

- Important Factors: For these two highest points, factors
       $X_1$, $X_2$, $X_3$, and $X_7$ have the same
       value (namely, +, -, +, -, respectively) while $X_4$,
       $X_5$, and $X_6$ have differing values.  We
       conclude that $X_1$, $X_2$, $X_3$, and $X_7$
       are potentially important factors, while $X_4$, $X_5$,
       and $X_6$ are not.

- Best Settings: Our first pass makes use of the settings at the
       observed maximum ($Y$ = 373.8).  The settings for this
       maximum are (+, -, +, -, +, -, -).

*Plot the Data: DOE Scatter Plot*
The next step in the analysis is to generate a
DOE scatter plot.

[![plot shows 2 points clearly dominate](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/dexsct_r.gif)](inn/gifs/dexsct_f.gif)

*Conclusions from the DOE Scatter Plot*
We can make the following conclusions based on the DOE scatter
plot.

- Important Factors: Again, two points dominate the plot.
       For $X_1$, $X_2$, $X_3$, and $X_7$, these two
       points emanate from the same setting, (+, -, +, -), while for
       $X_4$, $X_5$, and $X_6$ they emanate from different
       settings.  We conclude that $X_1$, $X_2$, $X_3$,
       and $X_7$ are potentially important, while $X_4$,
       $X_5$, and $X_6$ are probably not important.

- Best Settings: Our first pass at best settings yields
       ($X_1$ = +, $X_2$ = -, $X_3$ = +, $X_4$ =
       either, $X_5$ = either, $X_6$ = either, $X_7$ = -).

*Check for Main Effects: DOE Mean Plot*
The [DOE mean plot](../advanced-topics/eda-mean-plot.md) is generated
to more clearly show the main effects:

[![plot shows X2 and X7 to have the largest effect with X1 and X3 only
 slightly behind](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/gifs/dexmea_r.gif)](inn/gifs/dexmea_f.gif)

*Conclusions from the DOE Mean Plot*
We can make the following conclusions from the DOE mean plot.

- Important Factors:

$X_2$ (effect = large: about -80)

$X_7$ (effect = large: about -80)

$X_1$ (effect = large: about 70)

$X_3$ (effect = large: about 65)

$X_6$ (effect = small: about -10)

$X_5$ (effect = small: between 5 and 10)

$X_4$ (effect = small: less than 5)

- Best Settings: Here we step through each factor, one by one,
       and choose the setting that yields the highest average
       for the sonoluminescent light intensity:

($X_1$,$X_2$,$X_3$,$X_4$,$X_5$,$X_6$,$X_7$)
          = (+,-,+,+,+,-,-)

*Comparison of Plots*
All of the above three plots are used primarily to determine the most
important factors.  Because it plots a summary statistic rather
than the raw data, the DOE mean plot shows the ordering of the main
effects most clearly.  However, it is still recommended to generate
either the ordered data plot or the DOE scatter plot (or both).  Since
these plot the raw data, they can sometimes reveal features of the
data that might be masked by the DOE mean plot.

In this case, the ordered data plot and the DOE scatter plot
clearly show two dominant points.  This feature would not be
obvious if we had generated only the DOE mean plot.

Interpretation-wise, the most important factor $X_2$ (solute) will,
on the average, change the light intensity by about 80 units
regardless of the settings of the other factors.  The other
factors are interpreted similarly.

In terms of the best settings, note that the ordered data plot,
based on the maximum response value, yielded

   +, -, +, -, +, -, -

Note that a consensus best value, with "." indicating a setting for
which the three plots disagree, would be

   +, -, +, ., +, -, -

Note that the factor for which the settings disagree, $X_4$,
invariably defines itself as an "unimportant" factor.
