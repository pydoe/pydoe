# Work This Example Yourself

DEP *View Dataplot Macro for this Case Study*
This page allows you to repeat the analysis outlined in the
case study description on the previous page using Dataplot.
 It is required that you have already
downloaded and installed Dataplot and
configured your browser to run Dataplot.  Output from each analysis
step below will be displayed in one or more of the Dataplot windows.
The four main windows are the Output window, the Graphics window, the
Command History window, and the Data Sheet window.  Across the top of
the main windows are menus for executing Dataplot commands.  Across
the bottom is a command entry window where commands can be typed in.

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

[1. Read in the data.](splett3/dpmacros/data.dp)

[1. You have read 4 columns of numbers
    into Dataplot: variables Y, X1, X2,
    and X3.](eddy-current-background.md)

2. Plot the main effects.

[1. Ordered data plot.](splett3/dpmacros/order.dp)
[2. DOE scatter plot.](splett3/dpmacros/dexsct.dp)
[3. DOE mean plot.](splett3/dpmacros/dexmea.dp)
[1. Ordered data plot shows factor 1
    clearly important, factor 2
    somewhat important.](eddy-current-initial-plots.md)
[2. DOE scatter plot shows significant
    differences for factors 1 and 2.](eddy-current-initial-plots.md)
[3. DOE mean plot shows significant
    differences in means for factors
    1 and 2.](eddy-current-initial-plots.md)

3. Plots for interaction effects

[1. Generate a DOE interaction
      effects matrix plot.](splett3/dpmacros/dexeff.dp)
[1. The DOE interaction effects matrix
    plot does not show any major
    interaction effects.](eddy-current-interaction.md)

4. Block plots for main and interaction effects

[1. Generate block plots.](splett3/dpmacros/blockp.dp)
[1. The block plots show that the
    factor 1 and factor 2 effects
    are consistent over all
    combinations of the other
    factors.](eddy-current-block-plots.md)

5. Estimate main and interaction effects

[1. Perform a Yates fit to estimate the
      main effects and interaction effects.](splett3/dpmacros/yates.dp)
[1. The Yates analysis shows that the
    factor 1 and factor 2 main effects
    are significant, and the interaction
    for factors 2 and 3 is at the
    boundary of statistical significance.](eddy-current-estimate-effects.md)

6. Model selection

[1. Generate half-normal
      probability plots of the effects.](splett3/dpmacros/normpr.dp)
[2. Generate a Youden plot of the
      effects.](splett3/dpmacros/youden.dp)
[1. The probability plot indicates
    that the model should include
    main effects for factors 1 and 2.](eddy-current-important-factors.md)
[2. The Youden plot indicates
    that the model should include
    main effects for factors 1 and 2.](eddy-current-important-factors.md)

7. Model validation

[1. Compute residuals and predicted values
      from the partial model suggested by
      the Yates analysis.](splett3/dpmacros/fitpart.dp)
[2. Generate residual plots to validate
      the model.](splett3/dpmacros/part.dp)
[1. Check the link for the
    values of the residual and
    predicted values.](eddy-current-validate.md)
[2. The residual plots do not
    indicate any major problems
    with the model using main
    effects for factors 1 and 2.](eddy-current-validate.md)

8. DOE contour plot

[1. Generate a DOE contour plot using
      factors 1 and 2.](splett3/dpmacros/dexcon.dp)
[1. The DOE contour plot shows
    X1 = -1 and X2 = +1 to be the
    best settings.](eddy-current-using-model.md)
