# Constructing a Good Model

*Models for $2^k$ and $2^{k-p}$
designs*
Given that we have a statistic to measure the quality of a model, any
model, we move to the question of how to construct reasonable models
for fitting data from $2^k$ and $2^{k-p}$ designs.

*Initial simple model*
The simplest such proposed model is

   $Y = c + \epsilon$ that is, the response $Y$ = a constant + random error.  This
trivial model says that all of the factors (and interactions) are in
fact worthless for prediction and so the best-fit model is one
that consists of a simple horizontal straight line through the body
of the data.  The least squares estimate for this constant $c$ in
the above model is the sample mean $\bar{Y}$. .
The prediction equation for this model is thus

   $\hat{Y} = \bar{Y}$ The predicted values $\small \hat{Y}$ for this fitted trivial model are thus given by a vector consisting of the
same value (namely $\bar{Y}$) )
throughout.  The residual vector for this model will thus simplify to
simple deviations from the mean:

   $Y - \bar{Y}$ Since the number of fitted coefficients in this model is 1 (namely the
constant $c$), the residual standard deviation is the following:

   $s_{res} = \sqrt{\frac{\sum_{i=1}^{n}{(Y_{i} - \bar{Y})^2}}{n - 1}}$ which is of course the familiar, commonly employed sample standard
deviation.  If the residual standard deviation for this trivial model
were "small enough", then we could terminate the model-building process
right there with no further inclusion of terms.  In practice, however,
this trivial model does **not** yield a residual standard
deviation that is small enough (because the common value $\bar{Y}$ will not be close enough to some of the raw responses
$Y$) and so the model must be augmented--but how?

*Next-step model*
The logical next-step proposed model will consist of the above
additive constant plus some term that will improve the predicted
values the most.  This will equivalently reduce the residuals the
most and thus reduce the residual standard deviation the most.

*Using the most important effects*
As it turns out, it is a mathematical fact that the factor or
interaction that has the largest estimated effect

   $\hat{E} = \bar{Y}(+) - \bar{Y}(-)$ will necessarily, after being included in the model, yield the
"biggest bang for the buck" in terms of improving the predicted
values toward the response values $Y$.  Hence at this point the
model-building process and the effect estimation process merge.

In the previous steps in our analysis, we developed a ranked list
of factors and interactions.  We thus have a ready-made ordering of
the terms that could be added, one at a time, to the model.  This
ranked list of effects is precisely what we need to cumulatively
build more complicated, but better fitting, models.

*Step through the ranked list of factors*
Our procedure will thus be to step through, one by one, the ranked list
of effects, cumulatively augmenting our current model by the next term
in the list, and then compute (for all $n$ design points) the
predicted values, residuals, and residual standard deviation.  We
continue this one-term-at-a-time augmentation until the predicted
values are acceptably close to the observed responses $Y$ (and
hence the residuals and residual standard deviation become acceptably
close to zero).

Starting with the simple average, each cumulative model in this
iteration process will have its own associated residual standard
deviation.  In practice, the iteration continues until the residual
standard deviations become sufficiently small.

*Cumulative residual standard deviation plot*
The cumulative residual standard deviation plot is a graphical summary
of the above model-building process.  On the horizontal axis is a
series of terms (starting with the average, and continuing on with
various main effects and interactions).  After the average, the
ordering of terms on the horizontal axis is identical to the ordering
of terms based on [the half-normal probability
plot](eda-half-normal-plot.md) ranking based on effect magnitude.

On the vertical axis is the corresponding residual standard deviation
that results when the cumulative model has its coefficients fitted via
least squares, and then has its predicted values, residuals, and
residual standard deviations computed.  The first residual standard
deviation (on the far left of the cumulative residual standard
deviation plot) is that which results from the model consisting of

- the average.

The second residual standard deviation plotted is from the model
consisting of

- the average, plus
   - the term with the largest |effect|.

The third residual standard deviation plotted is
from the model consisting of

- the average, plus
   - the term with the largest |effect|, plus
   - the term with the second largest |effect|.

and so forth.
