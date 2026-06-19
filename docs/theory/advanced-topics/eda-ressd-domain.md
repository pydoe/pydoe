# Using the Model Beyond the Data Domain

Domain?

*Interpolation and extrapolation*
The previous section illustrated how to compute predicted values at
the points included in the design.  One of the virtues of modeling
is that the resulting prediction equation is **not** restricted to
the design data points.  From the prediction equation, predicted
values can be computed elsewhere and anywhere:

- within the domain of the data (interpolation);
   - outside of the domain of the data (extrapolation).

In the hands of an expert scientist/engineer/analyst, the ability
to predict elsewhere is extremely valuable.  Based on the fitted model,
we have the ability to compute predicted values for the response
at a large number of internal and external points.  Thus the
analyst can go beyond the handful of factor combinations
at hand and can get a feel (typically via
subsequent [contour plotting](eda-contour-plot.md)) as to
what the nature of the entire response surface is.

This added insight into the nature of the response is "free" and is an
incredibly important benefit of the entire model-building exercise.

*Predict with caution*
Can we be fooled and misled by such a mathematical and computational
exercise?  After all, is not the only thing that is "real" the data, and
everything else artificial?  The answer is "yes", and so such
interpolation/extrapolation is a double-edged sword that must be wielded
with care.  The best attitude, and especially for extrapolation, is
that the derived conclusions must be viewed with extra caution.

By construction, the recommended fitted models should be good at the
design points.  If the full-blown model were used, the fit will be
perfect.  If the full-blown model is reduced just a bit, then the fit
will still typically be quite good.  By continuity, one would expect
perfection/goodness at the design points would lead to goodness in the
immediate vicinity of the design points.  However, such local goodness
does **not** guarantee that the derived model will be good at some
distance from the design points.

*Do confirmation runs*
Modeling and prediction allow us to go beyond the data to gain
additional insights, but they must be done with great caution.
Interpolation is generally safer than extrapolation, but
mis-prediction, error, and misinterpretation are liable to occur
in either case.

The analyst should definitely perform the model-building process and
enjoy the ability to predict elsewhere, but the analyst must always be
prepared to validate the interpolated and extrapolated predictions by
collection of additional real, confirmatory data.  The general
empirical model that we recommend knows "nothing" about the
engineering, physics, or chemistry surrounding your particular
measurement problem, and although the model is the best generic model
available, it must nonetheless be confirmed by additional data.  Such
additional data can be obtained pre-experimentally or
post-experimentally.  If done pre-experimentally, a recommended
procedure for checking the validity of the fitted model is to augment
the usual $2^k$ or $2^{k-p}$ designs
with additional points at the center of the design.  This is discussed
[in the next section](eda-ressd-confirmation.md).

*Applies only for continuous factors*
Of course, all such discussion of interpolation and extrapolation makes
sense only in the context of continuous ordinal factors such as
temperature, time, pressure, size, etc.  Interpolation and
extrapolation make no sense for discrete non-ordinal factors such as
supplier, operators, design types, etc.
