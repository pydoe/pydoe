# Work This Example Yourself

*View Dataplot Macro for this Case
Study*
This page allows you to repeat the analysis outlined in the
case study description on the previous page using
Dataplot.  It is required that you have already
downloaded and installed Dataplot and
configured your browser to run Dataplot.  Output from each analysis
step below will be displayed in one or more of the Dataplot windows.
The four main windows are the Output window, the Graphics window, the
Command History window, and the Data Sheet window.  Across the top of
the main windows there are menus for executing Dataplot commands.
Across the bottom is a command entry window where commands can be typed
in.

Data Analysis Steps
Results and Conclusions

*Click on the links below to start
Dataplot and run this case study yourself.  Each
step may use results from previous steps, so
please be patient.  Wait until the software
verifies that the current step is complete before
clicking on the next step.*
*The links in this column will connect you with more
detailed information about each analysis step from the case
study description.*

1. Get set up and started.

[1. Read in the data.](inn/dpmacros/data.dp)

[1. You have read 8 columns of numbers
    into Dataplot: variables Y, X1, X2,
    X3, X4, X5, X6, and X7.](sono-background.md)

2. Plot the main effects.

[1. Ordered data plot.](inn/dpmacros/order.dp)
[2. DOE scatter plot.](inn/dpmacros/dexsct.dp)
[3. DOE mean plot.](inn/dpmacros/dexmea.dp)
[1. Ordered data plot shows 2 points
    that stand out.  Potential
    important factors are X1, X2, X3,
    and X7.](sono-initial-plots.md)
[2. DOE scatter plot identifies X1, X2,
    X3, and X7 as important factors.](sono-initial-plots.md)
[3. DOE mean plot identifies X1, X2,
    X3, and X7 as important factors.](sono-initial-plots.md)

3. Plots for interaction effects

[1. Generate a DOE interaction
      effects plot.](inn/dpmacros/dexeff.dp)
[1. The DOE interaction effects
    plot shows several important
    interaction effects.](sono-interaction.md)

4. Block plots for main and interaction effects

[1. Generate block plots.](inn/dpmacros/blockp.dp)
[1. The block plots are not
    particularly helpful in
    this case.](sono-block-plots.md)

5. Youden plot to identify important factors

[1. Generate a Youden plot.](inn/dpmacros/youden.dp)
[1. The Youden plot identifies
    X1, X2, X3, and X7 as important
    factors.  It also identifies a
    number of important interactions
    (X1*X3, X1*X2, X2*X3).](sono-youden-plot.md)

| 6. |Effects|

plot to identify important factors

[1. Generate |effects| plot.](inn/dpmacros/effect.dp)
| [1. The |effects|

plot identifies
    X2, X7, X1*X3, X1, X3, X2*X3,
    and X1*X2 as important factors
    and interactions.](sono-effects-plot.md)

7. Half-normal probability plot to
   identify important factors

[1. Generate half-normal probability
      plot.](inn/dpmacros/probpl.dp)
[1. The half-normal probability plot
    identifies X2, X7, X1*X3, X1, X3,
    X2*X3, and X1*X2 as important
    factors and interactions.](sono-half-normal.md)

8. Cumulative residual standard
   deviation plot

[1. Generate a cumulative residual
      standard deviation plot.](inn/dpmacros/cumres.dp)
[1. The cumulative residual standard
    deviation plot results in a model
    with 4 main effects and 3 2-factor
    interactions.](sono-cumulative-ressd.md)

9. DOE contour plot

[1. Generate a DOE contour plot using
      factors 2 and 7.](inn/dpmacros/dexcon.dp)
[1. The DOE contour plot shows
    X2 = -1 and X7 = -1 to be the
    best settings.](sono-contour-plot.md)
