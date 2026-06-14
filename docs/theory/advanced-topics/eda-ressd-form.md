# Form of the Model

*Models for various values of k*
From the above discussion, we thus note and recommend a form
of the model that consists of an additive constant plus a linear
combination of main effects and interactions.  What then is the
specific form for the linear combination?

The following are the full models for various values of $k$.
The selected final model will be a subset of the full model.

- For the $k$ = 1 factor case:

$$
Y = f(X_{1}) + \epsilon = c + B_{1}X_{1} + \epsilon
$$

- For the $k$ = 2 factor case:

$$
\begin{array}{lcl}
  Y & = & f(X_{1},X_{2}) + \epsilon \\
    & = & c + B_{1}X_{1} + B_{2}X_{2} + B_{12}X_{1}X_{2} + \epsilon
\end{array}
$$

- For the $k$ = 3 factor case:

$$
\begin{array}{lcl}
  Y & = & f(X_{1},X_{2},X_{3}) + \epsilon \\
    & = & c + B_{1}X_{1} + B_{2}X_{2} + B_{3}X_{3} + \\
    &   & B_{12}X_{1}X_{2} + B_{13}X_{1}X_{3} + B_{23}X_{2}X_{3} + \\
    &   & B_{123}X_{1}X_{2}X_{3} + \epsilon
\end{array}
$$

- and for the general $k$ case:

$$
\begin{array}{lcl}
  Y & = & f(X_{1},X_{2}, \ldots , X_{k}) + \epsilon \\
    & = & c + \mbox{linear combination of all main} \\
    &   & \mbox{effects and all interactions} + \epsilon
\end{array}
$$

Note that the model equations shown above include coefficients that
represent the change in $Y$ for a one-unit change in
$X_i$.  To obtain an effect estimate, which represents a
two-unit change in $X_i$ if the levels of
$X_i$ are +1 and -1, simply multiply the coefficient by
two.

*Ordered linear combination*
The listing above has the terms ordered with the main effects, then
the 2-factor interactions, then the 3-factor interactions, etc.  In
practice, it is recommended that the terms be ordered by importance
(whether they be main effects or interactions).  Aside from providing a
functional representation of the response, models should help
reinforce what is driving the response, which such a re-ordering does.
Thus for $k$ = 2, if factor 2 is most important, the 2-factor
interaction is next in importance, and factor 1 is least important,
then it is recommended that the above ordering of

$$
\begin{array}{lcl}
  Y & = & f(X_{1},X_{2}) + \epsilon \\
    & = & c + B_{1}X_{1} + B_{2}X_{2} + B_{12}X_{1}X_{2} + \epsilon
\end{array}
$$

be rewritten as

$$
\begin{array}{lcl}
  Y & = & f(X_{1},X_{2}) + \epsilon \\
    & = & c + B_{2}X_{2} + B_{12}X_{1}X_{2} + B_{1}X_{1} + \epsilon
\end{array}
$$
