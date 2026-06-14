# What is a Model?

*Mathematical models: functional form and coefficients*
A model is a mathematical function that relates the response $Y$
to the factors $X_1$ to $X_k$.  A model
has a

- functional form; and
   - coefficients.

An excellent and easy-to-use functional form that we find particularly
useful is a linear combination of the main effects and the interactions
(the selected model is a subset of the full model and almost always
a proper subset).  The coefficients in this linear
model are easy to obtain via application of the
least squares estimation
criterion (regression).  A given functional form with estimated
coefficients is referred to as a "fitted model" or a "prediction
equation".

*Predicted values and residuals*
For given settings of the factors $X_1$ to
$X_k$, a fitted model will yield predicted values.  For
each (and every) setting of the $X_i$'s, a
"perfect-fit" model is one in which the predicted values are identical
to the observed responses $Y$ at these $X_i$'s.
In other words, a perfect-fit model would yield a vector of predicted
values identical to the observed vector of response values.  For these
same $X_i$'s, a "good-fitting" model is one that yields
predicted values "acceptably near", but not necessarily identical to,
the observed responses $Y$.

The residuals (= deviations = error) of a model are the vector of
differences (Y - $\small \hat{Y}$) )
between the responses and the predicted values from the model.  For
a perfect-fit model, the vector of residuals would be all zeros.  For a
good-fitting model, the vector of residuals will be acceptably
(from an engineering point of view) close to zero.
