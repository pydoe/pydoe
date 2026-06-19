# Advantages of Linear Combinatoric Model

*Advantages: perfect fit and comparable coefficients*

The linear model consisting of main effects

and all interactions has two advantages:

- Perfect Fit: If we choose to include in the model all of the
       main effects and all interactions (of all orders), then the
       resulting least squares fitted model will have the property that
       the predicted values will be **identical** to the raw        response values $Y$.  We will illustrate this in the
       [next section](eda-ressd-predicted.md).

- Comparable Coefficients: Since the model fit has been carried
       out in the coded factor (-1, +1) units rather than the units of
       the original factor (temperature, time, pressure, catalyst
       concentration, etc.), the factor coefficients immediately become
       comparable to one another, which serves as an immediate
       mechanism for the scale-free ranking of the relative importance
       of the factors.

*Example*

To illustrate in detail the above latter point, suppose the (-1, +1)

factor $X_1$ is really a coding of temperature $T$ with the original
temperature ranging from 300 to 350 degrees and the (-1, +1) factor
$X_2$ is really a coding of time $t$ with the original time
ranging from 20 to 30 minutes.  Given that, a linear model in the
original temperature $T$ and time $t$ would yield coefficients whose
magnitude depends on the magnitude of $T$ (300 to 350) and $t$ (20 to
30), and whose value would change if we decided to change the units of $T$
(e.g., from Fahrenheit degrees to Celsius degrees) and $t$
(e.g., from minutes to seconds).  All of this is avoided by carrying
out the fit not in the original units for $T$ (300,350) and $t$
(20, 30), but in the coded units of $X_1$ (-1, +1) and $X_2$ (-1, +1).  The
resulting coefficients are unit-invariant, and thus the coefficient
magnitudes reflect the true contribution of the factors and
interactions without regard to the unit of measurement.

*Coding does not lead to loss of generality*

Such coding leads to no loss of generality since the coded factor

may be expressed as a simple linear relation of the original factor
($X_1$ to $T$, $X_2$ to $t$).  The unit-invariant coded
coefficients may be easily transformed to unit-sensitive original
coefficients if so desired.
