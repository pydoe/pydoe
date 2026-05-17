# Best Confirmation Point

Interpolation?

*Augment via center point*
For the usual continuous factor case, the best (most efficient and
highest leverage) additional model-validation point that may be added
to a $2^k$ or $2^{k-p}$ design is
at the center point.  This center point augmentation "costs" the
experimentalist only one additional run.

*Example*
For example, for the $k$ = 2 factor (Temperature
(300 to 350), and time (20 to 30)) experiment discussed in the
previous sections, the usual [4-run
22 full factorial design](eda-ressd-domain.md) may be replaced by the
following 5-run 22 full factorial design with a center point.

| $X_1$ | $X_2$ | $Y$ |
| --- | --- | --- |
| - | - | 2 |
| + | - | 4 |
| - | + | 6 |
| + | + | 8 |
| 0 | 0 |

*Predicted value for the center point*
Since "-" stands for -1 and "+" stands for +1, it is natural to code
the center point as (0,0).  Using the recommended model

$\hat{Y} = 5 + 2 X_{2} + X_{1}$ =
5 + 2*X_{2} + X_{1}

we can substitute 0 for $X_1$ and $X_2$ to generate the predicted value of 5 for the confirmatory run.

*Importance of the confirmatory run*
The importance of the confirmatory run cannot be overstated.  If the
confirmatory run at the center point yields a data value of, say,
$Y$ = 5.1, since the predicted value at the center is 5 and
we know the model is perfect at the corner points, that would give the
analyst a greater confidence that the quality of the fitted model may
extend over the entire interior (interpolation) domain.  On the other
hand, if the confirmatory run yielded a center point data value quite
different (e.g., $Y$ = 7.5) from the center point predicted value
of 5, then that would prompt the analyst to **not** trust the fitted
model even for interpolation purposes.  Hence when our factors are
continuous, a single confirmatory run at the center point helps
immensely in assessing the range of trust for our model.

*Replicated center points*
In practice, this center point value frequently has two, or even three
or more, replications.  This not only provides a reference point for
assessing the interpolative power of the model at the center, but it
also allows us to compute model-free estimates of the natural error
in the data.  This in turn allows us a more rigorous method for
computing the uncertainty for individual coefficients in the model
and for rigorously carrying out a lack-of-fit test for assessing
general model adequacy.
