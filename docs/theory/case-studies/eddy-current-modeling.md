# Modeling and Prediction Equations

*Parameter Estimates Don't Change as Additional Terms Added*
In most cases of least-squares fitting, the model coefficient
estimates for previously added terms change depending on what
was successively added.  For example, the estimate for the $X_1$
coefficient might change depending on whether or not an $X_2$ term
was included in the model.  This is **not** the case when the
design is orthogonal, as is this 23 full factorial
design.  In such a case, the estimates for the previously included
terms do not change as additional terms are added.  This means
the list of effect estimates in
[section 5.6.1.5](eddy-current-estimate-effects.md)
serves as the least-squares coefficient estimates for
progressively more complicated models.

*Default Model: Grand Mean*
If none of the factors are important, the prediction equation
defaults to the mean of all the response values (the overall
or grand mean).  That is,

   $\hat{Y} = 2.65875$
    

For our example, the default model has a grand mean of 2.65875 with a
residual standard deviation (a measure of goodness of fit) of
1.74106 ohms.

*Possible Prediction Equations*
We add effects to the default model in decreasing order of
absolute magnitude and compute the residual standard deviation
after adding each effect.  The prediction equations and their
residual standard deviations are shown below.

Residual
Model Terms                                                Std. Dev.
-----------------------------------------------------      ---------
Mean + X1                                                    0.57272
Mean + X1 + X2                                               0.30429
Mean + X1 + X2 + X2*X3                                       0.26737
Mean + X1 + X2 + X2*X3 + X1*X3                               0.23341
Mean + X1 + X2 + X2*X3 + X1*X3 + X3                          0.19121
Mean + X1 + X2 + X2*X3 + X1*X3 + X3 + X1*X2*X3               0.18031
Mean + X1 + X2 + X2*X3 + X1*X3 + X3 + X1*X2*X3 + X1*X2            NA

Note that the full model is a perfect fit to the data.
