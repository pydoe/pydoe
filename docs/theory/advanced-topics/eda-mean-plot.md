# DOE Mean Plot

*Purpose*
The DOE (design of experiments) mean plot answers the following two
questions:

- What is the ranked list of factors (not including the
       interactions)?  The ranking is from the most important
       factor to least important factor.
   - What is the best setting for each of the $k$ factors?

In the above two questions, the terms "important" and "best" need
clarification and specificity.

A factor can be important if it leads to a significant shift in the
location of the response variable as we go from the "-" setting
of the factor to the "+" setting of the factor.  Alternatively, a
factor can be important if it leads to a significant change in
variation (spread) as we go from the "-" to the "+" settings.  Both
definitions are relevant and acceptable.  The default definition of
"important" in engineering/scientific applications is the former
(shift in location).  Unless specified to the contrary, when a factor
is claimed to be important, the implication is that the
factor caused a large location shift in the response.

In this context, a factor setting is best if it results in a typical
response that is closest (in location) to the desired project goal
(that is, a maximization, minimization, or hitting a target).  This
desired project goal is an engineering, not a statistical, question,
and so the desired optimization goal must be overtly specified by
the engineer.

Given the above two definitions of important and best, the DOE
mean plot is a useful tool for determining the important factors and
for determining the best settings.

An alternate name for the DOE mean plot is the "main effects plot".

*Output*
The output from the DOE mean plot is:

- Primary: A ranked list of the factors (not including
       interactions) from most important to least important.
   - Secondary: The best setting for each of the $k$
       factors.

*Definition*
The DOE mean plot is formed by:

- Vertical Axis: The mean response for a given setting ("-" or
       "+") of a factor, for each of the $k$ factors.    - Horizontal Axis: The $k$ factors and the two settings
       ("-" and "+") within each factor.

*Motivation*
If we were interested in assessing the importance of a single factor,
and since important, by default, means shift in location, and
the average is the simplest location estimator, a reasonable
graphics tool to assess a single factor's importance would be a
simple mean plot.  The
vertical axis of such a plot would be the mean response for each
setting of the factor and the horizontal axis is the two settings of
the factor: "-" and "+" (-1 and +1).  A large difference in the two
means would imply the factor is important while a small difference
would imply the factor is not important.

The DOE mean plot is actually a sequence of $k$ such plots,
with one mean plot for each factor.  To assist in comparability and
relative importance, all of the mean plots are on the same scale.

*Plot for defective springs data*
Applying the DOE mean plot to the defective springs data yields
the following plot.

[![DOE mean plot for the defective springs data](https://www.itl.nist.gov/div898/handbook/pri/section5/gifs/dexmean.r.gif)](gifs/dexmean.gif)

*How to interpret*
From the DOE mean plot, we look for the following:

- A ranked list of factors from most important to least important.
   - The best settings for each factor (on average).

**Ranked List of Factors--Most Important to Least Important:**

For each of the $k$ factors, as we go from the "-" setting
to the "+" setting for the factor, is there a shift in location
of the average response?

If yes, we would like to identify the factor with the biggest
shift (the "most important factor"), the next biggest shift (the
"second most important factor"), and so on until all factors
are accounted for.

Since we are only plotting the means and each factor has identical
(-,+) = (-1,+1) coded factor settings, the above simplifies to

- What factor has the steepest line?  This is the
       most important factor.
   - The next steepest line?  This is the second most important
       factor.
   - Continue for the remaining factors.

This ranking of factors based on local means is the most important
step in building the definitive ranked list of factors as required
in screening experiments.

**Best Settings (on Average):**

For each of the $k$ factors, which setting (- or +) yields the
"best" response?

In order to answer this, the engineer must first define "best".  This
is done with respect to the overall project goal in conjunction with
the specific response variable under study.  For some experiments,
"best" means we are trying to maximize the response (e.g., maximizing
the speed of a chip).  For other experiments, "best" means we are
trying to minimize the response (e.g., semiconductor chip scrap).
For yet other experiments, "best" means we are trying to hit a
specific target (e.g., designing a resistor to match a specified
resistance).  Thus the definition of "best" is a precursor to the
determination of best settings.

For example, suppose the analyst is attempting to maximize
the response.  In that case, the analyst would proceed as follows:

- For factor 1, what setting (- or +) has the largest average
       response?
   - For factor 2, what setting (- or +) has the largest average
       response?
   - Continue for the remaining factors.

The resulting $k$-vector of best settings:

   (x1best, x2best, ..., xkbest)

is in general obtained by looking at each factor individually in the
DOE mean plot and choosing that setting (- or +) that has an
average response closest to the desired optimal (maximal, minimal,
target) response.

This candidate for best settings is based on the averages.  This
$k$-vector of best settings should be similar to that obtained
from the [DOE scatter plot](eda-scatter-plot.md), though the
DOE mean plot is easier to interpret.

*Conclusions for the defective springs data*
The application of the DOE mean plot to the defective springs data
set results in the following conclusions:

- Ranked list of factors (excluding interactions):

- $X_1$ (most important).  Qualitatively, this factor
              looks definitely important.
          - $X_2$ (of lesser importantance).  Qualitatively, this
              factor is a distant second to $X_1$.           - $X_3$ (unimportant).  Qualitatively, this factor
              appears to be unimportant.

- Best settings (on average):

($X_1$, $X_2$, $X_3$) = (+, -, +) = (+1, -1, +1)
