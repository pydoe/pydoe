# Ordered Data Plot

*Purpose*
The ordered data plot answers the following two questions:

- What is the best setting (based on the data) for each of
       the $k$ factors?
   - What is the most important factor?

In the above two questions, the terms "best" and "important"
need more precise definitions.

Settings may be declared as "best" in three different ways:

- "best" with respect to the data;
   - "best" on average;
   - "best" with respect to predicted values from an
       adequate model.

In the worst case, each of the above three criteria may yield
different "best settings".  If that occurs, then the three answers
must be consolidated at the end of the 10-step process.

The ordered data plot will yield best settings based on the first
criteria (data).  That is, this technique yields those settings
that correspond to the best response value, with the best
value dependent upon the project goals:

- maximization of the response;
   - minimization of the response;
   - hitting a target for the response.

This, in turn, trivially yields the best response value:

- maximization: the observed maximum data point;
   - minimization: the observed minimum data point;
   - target: the observed data value closest to the specified
       target.

With respect to the most "important" factor, this by default refers
to the single factor which causes the greatest change in the
value of the response variable as we proceed from the
"-" setting to the "+" setting of the factor.  In practice, if a
factor has one setting for the best and near-best response values
and the opposite setting for the worst and near-worst response
values, then that factor is usually the most important factor.

*Output*
The output from the ordered data plot is:

- Primary: Best setting for each of the $k$ factors.
   - Secondary: The name of the most important factor.

*Definition*
An ordered data plot is formed by:

- Vertical Axis: The ordered (smallest to largest) raw response
       value for each of the $n$ runs in the experiment.
   - Horizontal Axis: The corresponding dummy run index (1 to
       $n$) with (at each run) a designation of the corresponding
       settings (- or +) for each of the $k$ factors.

In essence, the ordered data plot may be viewed as a scatter plot
of the ordered data versus a single $n$-treatment
consolidation factor.

*Motivation*
To determine the best setting, an obvious place to start is the
best response value.  What constitutes "best"?  Are we trying to
maximize the response, minimize the response, or hit a specific
target value?  This non-statistical question must be addressed
and answered by the analyst.  For example, if the project goal is
ultimately to achieve a large response, then the desired
experimental goal is maximization.  In such a case, the analyst
would note from the plot the largest response value and the
corresponding combination of the $k$-factor settings
that yielded that best response.

*Plot for defective springs data*
Applying the ordered response plot for the defective springs data set
yields the following plot.

[![Ordered response plot for the defective springs data](https://www.itl.nist.gov/div898/handbook/pri/section5/gifs/ordered.r.gif)](gifs/ordered.gif)

*How to interpret*
From the ordered data plot, we look for the following:

- best settings;
   - most important factor.

**Best Settings (Based on the Data):**

At the best (highest or lowest or target) response value, what
are the corresponding settings for each of the $k$ factors?
This defines the best setting based on the raw data.

**Most Important Factor:**

For the best response point and for the nearby neighborhood of
near-best response points, which (if any) of the $k$ factors
has consistent settings?  That is, for the subset of response
values that is best or near-best, do all of these values emanate
from an identical level of some factor?

Alternatively, for the best half of the data, does this half
happen to result from some factor with a common setting?  If yes,
then the factor that displays such consistency is an excellent
candidate for being declared the "most important factor".
For a balanced experimental design, when all of the best/near-best
response values come from one setting, it follows that all of the
worst/near-worst response values will come from the other setting
of that factor.  Hence that factor becomes "most important".

At the bottom of the plot, step though each of the $k$ factors
and determine which factor, if any, exhibits such behavior.  This
defines the "most important" factor.

*Conclusions for the defective springs data*
The application of the ordered data plot to the defective
springs data set results in the following conclusions:

- Best Settings (Based on the Data):

($X_1$, $X_2$, $X_3$) = (+, -, +) = (+1, -1, +1)
       is the best setting since

- the project goal is maximization of the percent
              acceptable springs;
          - $Y$ = 90 is the largest observed response value; and
          - ($X_1$, $X_2$, $X_3$) = (+, -, +) at               $Y$ = 90.

- Most important factor:

$X_1$ is the most important factor since the four largest
       response values (90, 87, 79, and 75) have factor $X_1$ at +1,
       and the four smallest response values (52, 59, 61, and 67)
       have factor $X_1$ at -1.
