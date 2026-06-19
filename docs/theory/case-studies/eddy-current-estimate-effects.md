# Estimate Main and Interaction Effects

*Effects Estimation*
Although the effect estimates were given on the
[DOE interaction plot](eddy-current-interaction.md) on a previous
page, we also display them in tabular form.

The full model for the 23 factorial design is

$\begin{eqnarray*}
   Y &=& \mu + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 +
         \beta_{12} X_1 X_2 \\
     &+& \beta_{13} X_1 X_3 + \beta_{23} X_2 X_3 +
         \beta_{123} X_1 X_2 X_3 + \epsilon
   \end{eqnarray*}$

Data from factorial designs with two levels can be analyzed using
least-squares regression.  The regresson coefficients represent
the change per one unit of the factor variable, the effects shown
on the interaction plot represent changes between high and low
factor levels so they are twice as large as the regression
coefficients.

*Effect Estimates*
The parameter estimates from a least-squares regression analysis
for the full model are shown below.

Effect    Estimate
     ------    --------
     Mean       2.65875
     X1         1.55125
     X2        -0.43375
     X3         0.10625
     X1*X2      0.06375
     X1*X3      0.12375
     X2*X3      0.14875
     X1*X2*X3   0.07125

Because we fit the full model to the data, there are no degrees
of freedom for error and no significance tests are available.

If we sort the effects from largest to smallest (excluding the mean),
the four most important factors are:  X1 (number of turns),
X2 (winding distance), X2*X3 (winding distance by wire gauge interaction),
and X1*X3 (number of turns by wire gauge interaction).
