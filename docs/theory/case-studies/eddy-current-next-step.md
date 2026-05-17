# Conclusions and Next Step

*Conclusions*
The goals of this case study were:

- Determine the most important factors.
    - Determine the best settings for the factors.
    - Determine a good prediction equation for the data.

The various plots and analysis showed that the number of turns
($X_1$) and the winding distance ($X_2$) were the most important
factors and a good prediction equation for the data is:

$\hat{Y} = 2.65875 + 1.55125 X_{1} - 0.43375 X_{2}$

The DOE contour plot gave us the best settings for the factors
($X_1$ = -1 and $X_2$ = 1).

*Next Step*
Full and fractional designs are typically used to identify the
most important factors.  In some applications, this is sufficient
and no further experimentation is performed.  In other applications,
it is desired to maximize (or minimize) the response variable.
This typically involves the use of
[response surface designs](../choosing-design/response-surface.md).
The DOE contour plot can provide guidance on the settings to use for
the factor variables in this next phase of the experiment.

This is a common sequence for designed experiments in engineering
and scientific applications.  Note the iterative nature of this
approach.  That is, you typically do not design one large experiment
to answer all your questions.  Rather, you run a series of smaller
experiments.  The initial experiment or experiments are used to
identify the important factors.  Once these factors are identified,
follow-up experiments can be run to fine tune the optimal
settings (in terms of maximizing/minimizing the response variable)
for these most important factors.

For this particular case study, a response surface design was
not used.
