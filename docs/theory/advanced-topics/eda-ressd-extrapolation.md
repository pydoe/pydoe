# Extrapolation

Extrapolation?

*Graphical representation of extrapolation*
Extrapolation is performed similarly to
[interpolation](eda-ressd-extrapolation.md).  For example, the predicted
value at temperature $T$ = 375 and time $t$ = 28 is
indicated by the "X":

![Graphical representation of the design with an extrapolated point](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des5.gif)

    30 +1 --------------
          |6          8|
     T    |            |     ?
     i  X |            |
     m  2 |            |
     e    |            |
          |            |
          |2          4|
    20 -1 --------------
          -1    X1    +1
          300  Temp  350

and is computed by substituting the values $X_1$ = +2.0 ($T$=375) and $X_2$ = +0.8 ($t$=28) into the prediction
equation

$\hat{Y} = 5 + 2 X_{2} + X_{1}$ =
5 + 2*X_{2} + X_{1}

yielding a predicted value of 8.6.  Thus we have

![Graphical representation of the design with the predicted value for
 an extrapolated point](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des6.gif)

    30 +1 --------------
          |6          8|
     T    |            |   8.6
     i  X |            |
     m  2 |            |
     e    |            |
          |            |
          |2          4|
    20 -1 --------------
          -1    X1    +1
          300  Temp  350

*Pseudo-data*
The predicted value from the modeling effort may be viewed as
pseudo-data, data obtained without the experimental
effort.  Such "free" data can add tremendously to the insight via the
application of graphical techniques (in particular, the
[contour plots](eda-contour-plot.md) and can add significant insight
and understanding as to the nature of the response surface relating
$Y$ to the $X$'s.

But, again, a final word of caution: the "pseudo data" that results
from the modeling process is exactly that, pseudo-data.  It is
**not** real data, and so the model and the model's predicted values
must be validated by additional confirmatory (real) data points.  A
more balanced approach is that:

   Models may be trusted as "real" \[that is, to
   generate predicted values and contour curves\],
   but must always be verified \[that is, by the addition of
   confirmatory data points\].

The rule of thumb is thus to take advantage of the available and
recommended model-building mechanics for these 2-level designs, but
do treat the resulting derived model with an equal dose of both
optimism and caution.

*Summary*
In summary, the motivation for model building is that it gives us
insight into the nature of the response surface along with the ability
to do interpolation and extrapolation; further, the motivation for the
use of the cumulative residual standard deviation plot is that it
serves as an easy-to-interpret tool for determining a good
and parsimonious model.
