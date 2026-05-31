# Choosing the Step Length

*A procedure for choosing how far along the direction of steepest
ascent to go for the next trial run*
Once the search direction is determined, the second decision needed
in Phase I relates to how far in that direction the process should be
"moved".  The most common procedure for selecting a step length is
based on choosing a step size in one factor and then computing step
lengths in the other factors proportional to their parameter estimates.
This provides a point on the direction of maximum improvement.  The
procedure is given below. A similar approach is obtained by choosing
increasing values of $\rho$
 
in

$x_{i}^{*} = \rho \frac{b_{i}}{\sqrt{\sum_{j=1}^{k}{b_{j}^{2}}}}
\hspace{.3in} i = 1, 2, \ldots , k$

.

However, the procedure below considers the original units of
measurement which are easier to deal with than the coded "distance"
$\rho$.
 .

**Procedure: selection of step length**

*Procedure for selecting the step length*
The following is the procedure for selecting the step length.

- Choose a step length $\Delta X_{j}$ X
       (in natural units of measurement) for some factor $j$.        Usually, factor $j$ is chosen to be the one engineers feel
       more comfortable varying, or the one with the largest
       **|$b_j$|**.  The value of $\Delta X_{j}$ X
       can be based on the width of the confidence cone around the
       steepest ascent/descent direction.  Very wide cones indicate that
       the estimated steepest ascent/descent direction is not reliable,
       and thus $\Delta X_{j}$ X
       should be small.  This usually occurs when the $R_2$
       value is low.  In such a case, additional experiments can be
       conducted in the current experimental region to obtain a better
       model fit and a better search direction.

- Transform to coded units:

$\Delta x_{j} = \frac{\Delta X_{j}}{s_{j}}$ with $s_j$ denoting the scale factor used for factor $j$ (e.g., $s_j = \text{range}_j / 2$).

- Set $\Delta x_{i} = \frac{b_{i}}{b_{j}} \Delta x_{j}$ for all other factors $i$.

- Transform all the $\Delta x_{i}$'s x's
       to natural units:

       $\Delta X_{i} = (\Delta x_{i})(s_{i})$. X_{i} =
       ( x_{i})(s_{i}).

**Example: Step Length Selection.**

*An example of step length selection*
The following is an example of the step length selection procedure.

- For the chemical process experiment described [previously](single-response-steepest-ascent.md),
       the process engineer selected $\Delta X_{2} = 50$
       minutes. This was based on process engineering considerations.
       It was also felt that $\Delta X_{2} = 50$ X_{2} = 50
       does not move the process too far away from the current region
       of experimentation.  This was desired since the
       $R_2$ value of 0.6580 for the fitted model is quite
       low, providing a not very reliable steepest ascent direction (and a
       wide confidence cone, see
       [Technical
       Appendix 5B](confidence-region.md)).

- $\Delta x_{2} = \frac{50}{50} = 1.0$ .

- $\Delta x_{1} = \frac{-1.2925}{11.14} = -0.1160$
        .

- $\Delta X_{2} = (-0.1160)(30) = -3.48^{\circ}C$ X_{2} = (-0.1160)(30) =
       -3.48^{o}C.

Thus the step size is $\Delta X$' X'
**= (-3.48oC, 50 minutes)**.

**Procedure: Conducting Experiments Along the Direction of Maximum
Improvement**

*Procedure for conducting experiments along the direction of
maximum improvement*
The following is the procedure for conducting experiments along the
direction of maximum improvement.

- Given current operating conditions
       $X_{0}^{'} = (X_{1}, X_{2}, \dots , X_{k})$ = (X_{1}, X_{2}, ...,
       X_{k})
       and a step size
       $\Delta X' = (\Delta X_{1}, \Delta X_{2}, \dots ,
       \Delta X_{k})$, X' =
       ( X_{1}, X_{2}, ..., X_{k}),
       perform experiments at factor levels
       $X_{0} + \Delta X, X_{0} + 2 \Delta X, X_{0} + 3 \Delta X,
       \dots$
        X_{0} + X,
       X_{0} +
       2 X,
       X_{0} +
       3 X, ...
       as long as improvement in the response $Y$
       (decrease or increase, as desired) is observed.

- Once a point has been reached where there is no further
       improvement, a new first-order experiment (e.g., a
       **$2^{k-p}$** fractional factorial)
       should be performed with repeated center runs to assess lack
       of fit. If there is no significant evidence of lack of fit,
       the new first-order model will provide a new search direction,
       and another iteration is performed as indicated in Figure 5.3.
       Otherwise (there is evidence of lack of fit), the experimental
       design is augmented and a second-order model should be fitted.
       That is, the experimenter should proceed to "Phase II".

**Example: Experimenting Along the Direction of Maximum
Improvement**

*Step 1: increase factor levels by $\delta$ *
**Step 1:**

Given **$X_0$** = (200oC, 200 minutes) and
$\Delta X$ X
= (-3.48oC, 50 minutes), the next experiments were
performed as follows (the step size in temperature was rounded to
-3.5oC for practical reasons):

| $X_1$ | $X_2$ | $x_1$ | $x_2$ | $Y$ (= yield) |
| --- | --- | --- | --- | --- | --- |
| $X_0$ | 200 | 200 | 0 | 0 |
| $X_0$ +  $\Delta X$ |
| X |
| 196.5 | 250 | -0.1160 | 1 | 56.2 |
| --- | --- | --- | --- | --- | --- |
| $X_0$ +  $2 \Delta X$ | 193.0 | 300 | -0.2320 | 2 | 71.49 |
| $X_0$ +  $3 \Delta X$ | 189.5 | 350 | -0.3480 | 3 | 75.63 |
| $X_0$ +  $4 \Delta X$ | 186.0 | 400 | -0.4640 | 4 | 72.31 |
| $X_0$ +  $5 \Delta X$ | 182.5 | 450 | -0.5800 | 5 | 72.10 |

 
Since the goal is to maximize $Y$, the point of maximum
observed response is
**$X_1$** = 189.5oC,
**$X_2$** = 350 minutes.  Notice that the search was
stopped after 2 consecutive drops in response, to assure that
we have passed by the "peak" of the "hill".

*Step 2: new factorial experiment*
**Step 2:**

A new $2^2$ factorial experiment is performed with
$X' = (189.5, 350)$ as the origin.  Using the same scaling
factors as before, the new scaled controllable factors are:

$x_{1} = \frac{X_{1} - 189.5} {30} \hspace{.5in}$
and
$\hspace{.5in} x_{2} = \frac{X_{2} - 350} {50}$ Five center runs (at **$X_1$ = 189.5,
$X_2$ = 350**)
were repeated to assess lack of fit. The experimental results were:

| $x_1$ | $x_2$ | $X_1$ | $X_2$ | $Y$ (= yield) |
| --- | --- | --- | --- | --- |
| -1 | -1 | 159.5 | 300 | 64.33 |
| +1 | -1 | 219.5 | 300 | 51.78 |
| -1 | +1 | 159.5 | 400 | 77.30 |
| +1 | +1 | 219.5 | 400 | 45.37 |
| 0 | 0 | 189.5 | 350 | 62.08 |
| 0 | 0 | 189.5 | 350 | 79.36 |
| 0 | 0 | 189.5 | 350 | 75.29 |
| 0 | 0 | 189.5 | 350 | 73.81 |
| 0 | 0 | 189.5 | 350 | 69.45 |

 
(The reader can download the data as a
text file.)

The corresponding ANOVA table for a linear model is

                SUM OF            MEAN     F
SOURCE         SQUARES    DF     SQUARE  VALUE  PROB > F

MODEL          505.376     2    252.688  4.731   0.0703
CURVATURE      336.364     1    336.364  6.297   0.0539
RESIDUAL       267.075     5     53.415
  LACK OF FIT   93.896     1     93.896  2.168   0.2149
  PURE ERROR   173.179     4     43.295

COR TOTAL     1108.815     8

From the table, the linear effects (model) are significant and there is
no evidence of lack of fit. However, there is a significant curvature
effect (at the 5.4 % significance level), which implies that the
optimization should proceed with Phase II; that is, the fit and
optimization of a second-order model.
