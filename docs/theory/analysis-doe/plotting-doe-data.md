# How to "Look" at DOE Data

*The importance of looking at the data with a wide array of plots or visual displays cannot be over-stressed*

The right graphs, plots or visual displays of a dataset can uncover anomalies or provide insights that go beyond what most quantitative techniques are capable of discovering. Indeed, in many cases quantitative techniques and models are tools used to confirm and extend the conclusions an analyst has already formulated after carefully "looking" at the data.

Most software packages have a selection of different kinds of plots for displaying DOE data. Some of these useful ways of looking at data are mentioned below, with links to detailed explanations in Chapter 1 (Exploratory Data Analysis or EDA) or to other places where they are illustrated and explained. In addition, examples and detailed explanations of visual (EDA) DOE techniques can be found in [An EDA Approach to Experiment Design](https://www.itl.nist.gov/div898/handbook/pri/section5/pri59.htm).

*Plots for viewing the response data*

**First "Look" at the Data**

- Histogram of responses
- Run-sequence plot (pay special attention to results at center points)
- Scatter plot (for pairs of response variables)
- Lag plot
- Normal probability plot
- Autocorrelation plot

*Plots for viewing main effects and 2-factor interactions, explanation of normal or half-normal plots to detect possible important effects*

**Subsequent Plots: Main Effects, Comparisons and 2-Way Interactions**

- Quantile-quantile (q-q) plot
- Block plot
- Box plot
- Bi-histogram
- DOE scatter plot
- DOE mean plot
- DOE standard deviation plot
- DOE interaction plots
- Normal or half-normal probability plots for effects.

!!! Note
    These links show how to generate plots to test for normal (or half-normal) data with points lining up along a straight line, approximately, if the plotted points were from the assumed normal (or half-normal) distribution. For two-level full factorial and fractional factorial experiments, the points plotted are the estimates of all the model effects, including possible interactions. Those effects that are really negligible should have estimates that resemble normally distributed noise, with mean zero and a constant variance. Significant effects can be picked out as the ones that do not line up along the straight line. Normal effect plots use the effect estimates directly, while half-normal plots use the absolute values of the effect estimates.

- Youden plots

*Plots for testing and validating models*

**Model testing and Validation**

- Response vs predictions
- Residuals vs predictions
- Residuals vs independent variables
- Residuals lag plot
- Residuals histogram
- Normal probability plot of residuals

*Plots for model prediction*

**Model Predictions**

- Contour plots
