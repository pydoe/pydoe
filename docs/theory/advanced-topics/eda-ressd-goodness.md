# Goodness-of-fit Metric

Metric for a Model?

*Motivation*
This question deals with the issue of how to construct a metric, a
statistic, that may be used to ascertain the quality of the fitted
model.  The statistic should be such that for one range of values, the
implication is that the model is good, whereas for another range of
values, the implication is that the model gives a poor fit.

*Sum of absolute residuals*
Since a model's adequacy is inversely related to the size of its
residuals, one obvious statistic is the sum of the absolute
residuals.

$$
\mbox{AR} = \sum_{i=1}^{n}{|r_{i}|}
$$

 </ul>

Clearly, for a fixed $n$,the smaller this sum is, the smaller
are the residuals, which implies the closer the predicted values are
to the raw data $Y$, and hence the better the fitted model.  The
primary disadvantage of this statistic is that it may grow larger
simply as the sample size $n$ grows larger.

*Average absolute residual*
A better metric that does not change (much) with increasing sample
size is the average absolute residual:

$$
\mbox{AAR} = \frac{\sum_{i=1}^{n}{|r_{i}|}} {n}
$$

 </ul>

with $n$ denoting the number of response values.  Again,
small values for this statistic imply better-fitting models.

*Square root of the average squared residual*
An alternative, but similar, metric that has better statistical
properties is the square root of the average squared residual.

$$
\sqrt{ \frac{\sum_{i=1}^{n}{r_{i}^{2}}} {n}}
$$

 </ul>

As with the previous statistic, the smaller this statistic,
the better the model.

*Residual standard deviation*
Our final metric, which is used directly in inferential statistics,
is the residual standard deviation

$$
s_{res} = \sqrt{ \frac{\sum_{i=1}^{n}{r_{i}^{2}}} {n-p}}
$$

 </ul>

with $p$ denoting the number of fitted coefficients in the
model.  This statistic is the standard deviation of the residuals
from a given model.  The smaller is this residual standard deviation,
the better fitting is the model.  We shall use the residual standard
deviation as our metric of choice for evaluating and comparing
various proposed models.
