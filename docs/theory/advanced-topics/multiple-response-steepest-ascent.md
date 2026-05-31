# Path of Steepest Ascent (Multiple Responses)

*Objective: consider and balance the individual paths of
maximum improvement*
When the responses exhibit adequate linear fit (i.e., the response
models are all linear), the objective is to find a direction or path
that simultaneously considers the individual paths of maximum
improvement and balances them in some way.  This case is addressed
next.

When there is a mix of linear and higher-order responses, or when all
empirical response models are of higher-order, see sections
[5.5.3.2.2](multiple-response-desirability.md) and
[5.5.3.2.3](multiple-response-math-programming.md).  The desirability method (section
[5.5.3.2.2](multiple-response-desirability.md)) can also be used when all
response models are linear.

**Procedure: Path of Steepest Ascent, Multiple Responses**

*A weighted priority strategy is described using the path of
steepest ascent for each response*
The following is a weighted priority strategy using the path of
steepest ascent for each response.

- Compute the gradients $g_i$
       ($i$ = 1, 2, . . ., $k$) of all responses as
       explained in section [5.5.3.1.1](single-response-steepest-ascent.md).
       If one of the responses is clearly of primary interest compared
       to the others, use only the gradient of this response and
       follow the procedure of section
       [5.5.3.1.1](single-response-steepest-ascent.md).  Otherwise, continue with
       step 2.

- Determine relative priorities $\pi_{i}$
        
       for each of the $k$ responses. Then, the weighted
       gradient for the search direction is given by

$$
g = \frac{\pi_{1}g_{1} +\pi_{2}g_{2} + \cdots +
          \pi_{k}g_{k}} {\sum_{i=1}^{k}{\pi_{i}}}
$$
 and the weighted direction is

$d = \frac{g} {\parallel g \parallel}$ *Weighting factors based on $R^2$*
The confidence cone for the direction of maximum improvement explained
in [section 5.5.3.1.2](confidence-region.md) can be used to weight
down "poor" response models that provide very wide cones and unreliable
directions.  Since the width of the cone is proportional to
**(1 - $R^2$)**,
we can use

$$
\pi_{j} \frac{R_{j}^{2}} {\sum_{i=1}^{k}{R_{i}^{2}}} \hspace{.5in}
j = 1, 2, \dots , k
$$
 *Single response steepest ascent procedure*
Given a weighted direction of maximum improvement, we can follow the
single response steepest ascent procedure as in section
[5.5.3.1.1](single-response-steepest-ascent.md) by selecting points with
coordinates
$\mathbf{x} = \rho d_i$, $i = 1, 2, \ldots, k$.  These and related issues are
explained more fully in [Del
Castillo (1996)](../references/index.md).

**Example: Path of Steepest Ascent, Multiple Response Case**

*An example using the weighted priority method*
Suppose the response model:

   $\hat{y}_{1} = 711.0 + 50.9 x_{1} + 154.8 x_{2}$ with $R_{1}^{2} = 0.8968$ = 0.8968
represents the average yield of a production process obtained from a
replicated factorial experiment in the two controllable factors (in
coded units).  From the same experiment, a second response model for
the process standard deviation of the yield is obtained and given by

   $\hat{y}_{2} = 19.26 + 6.31 x_{1} + 6.28 x_{2}$ with $R_{2}^{2} = 0.5977$. = 0.5977.
We wish to maximize the mean yield while minimizing the standard
deviation of the yield.

**Step 1: compute the gradients:**

*Compute the gradients*
We compute the gradients as follows.

$$
\begin{array}{lcl}
      g_{1}^{'} & = & \left( \frac{50.9}{\sqrt{50.9^{2} + 154.8^{2}}},
                             \frac{154.8}{\sqrt{50.9^{2} + 154.8^{2}}}
                      \right) \\
                & = & (0.3124, 0.9500)
       \end{array}
$$
 
$$
\begin{array}{lcl}
      g_{2}^{'} & = & \left( \frac{-6.31}{\sqrt{6.31^{2} + 6.28^{2}}},
                             \frac{-6.28}{\sqrt{6.31^{2} + 6.28^{2}}}
                      \right) \\
                & = & (-0.7088, -0.7054)
       \end{array}
$$
 (recall we wish to *minimize* **$y_2$**).

**Step 2: find relative priorities:**

*Find relative priorities*
Since there are no clear priorities, we use the quality of fit as
the priority:

   $\pi_{1} = \frac{0.8968}{0.8968 + 0.5977} = 0.6$ $\pi_{2} = \frac{0.5977}{0.8968 + 0.5977} = 0.4$ Then, the weighted gradient is

$\mathbf{g}' = (0.6(0.3124) + 0.4(-0.7088),\ 0.6(0.95) + 0.4(-0.7054)) = (-0.096, 0.2878)$
 

which, after scaling it (by dividing each coordinate by
$\small \sqrt{(-0.096)^{2} + 0.2878^{2}}$), ),
gives the weighted direction $\mathbf{d}' = (-0.03164, 0.9486)$.

Therefore, if we want to move ***ρ* = 1**
coded units along the path of maximum improvement, we will set
**$x_1$ = (1)(-0.3164) = -0.3164,
$x_2$ = (1)(0.9486) = 0.9486** in the next run
or experiment.
