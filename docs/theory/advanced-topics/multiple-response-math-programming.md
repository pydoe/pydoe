# Multiple Responses: Mathematical Programming

approach

*The mathematical programming approach maximizes or minimizes a
primary response, subject to appropriate constraints on all other
responses*
The analysis of multiple response systems usually involves some type
of optimization problem.  When one response can be chosen as the
"primary", or most important response, and bounds or targets can be
defined on all other responses, a mathematical programming approach
can be taken.  If this is not possible, the desirability approach
should be used instead.

In the mathematical programming approach, the primary response is
maximized or minimized, as desired, subject to appropriate constraints
on all other responses.  The case of two responses ("dual" responses)
has been studied in detail by some authors and is presented first.
Then, the case of more than 2 responses is illustrated.

- Dual response
       systems

- More than 2 responses

**Dual response systems**

*Optimization of dual response systems*
The optimization of dual response systems (DRS) consists of finding
operating conditions $\mathbf{x}$ that

   $\mbox{optimize:} \hspace{.5in} \hat{Y}_{p}(x)$ $\begin{array}{ll}
      \mbox{subject to:} \hspace{.2in} & \hat{Y}_{s}(x) = T \\
                                        & x'x \le \rho^{2}
      \end{array}$ with $T$ denoting the target value for the secondary response,
$p$ the number of primary responses (i.e., responses to
be optimized), $s$ the number of secondary responses
(i.e., responses to be constrained), and ***ρ*** is the
 radius of a spherical constraint that limits the region in the
controllable factor space where the search should be undertaken.  The
value of ***ρ*** should be chosen with the purpose of
avoiding solutions that extrapolate too far outside the region where the
experimental data were obtained.  For example, if the experimental design
is a central composite design, choosing
$\rho = \alpha$ (axial distance) is a logical choice.  Bounds of the form $L \leq x_i \leq U$
 
can be used instead if a cubical experimental region were used (e.g.,
when using a factorial experiment).  Note that a Ridge Analysis
problem is related to a DRS problem when the secondary constraint is
absent.  Thus, any algorithm or solver for DRS's will also work for
the Ridge Analysis of single response systems.

*Nonlinear programming software required for DRS*
In a DRS, the response models
$\hat{Y}_{p}$ and $\hat{Y}_{s}$
  and

can be linear, quadratic or even cubic polynomials.  A nonlinear
programming algorithm has to be used for the optimization of a DRS. For
the particular case of quadratic responses, an equality constraint for
the secondary response, and a spherical region of experimentation,
specialized optimization algorithms exist that guarantee global optimal
solutions.  In such a case, the algorithm DRSALG can be used (download
from http://www.stat.cmu.edu/jqt/29-3), but a Fortran compiler is
necessary.

*More general case*
In the more general case of inequality constraints or a cubical region
of experimentation, a general purpose nonlinear solver must be used and
several starting points should be tried to avoid local optima. This is
illustrated in the next section.

**Example for more than 2 responses**

*Example: problem setup*
The values of three components
**($x_1$, $x_2$, $x_3$)**
of a propellant need to be selected to maximize a primary response,
burning rate **($Y_1$)**, subject to satisfactory
levels of two secondary reponses; namely, the variance of the burning
rate **($Y_2$)** and the cost
**($Y_3$)**.  The three components must add to 100%
of the mixture.  The fitted models are:

$\begin{array}{lcl}
         \hat{Y}_{1} & = & 35.4 x_{1} + 42.77 x_{2} + 70.36 x_{3} +
                           16.02 x_{1} x_{2} \\
                     &   & + 36.33 x_{1} x_{3} + 136.8 x_{2} x_{3} +
                           854.9 x_{1} x_{2} x_{3}
   \end{array}$ $\begin{array}{lcl}
         \hat{Y}_{2} & = & 3.88 x_{1} + 9.03 x_{2} + 13.63 x_{3} -
                           0.1904 x_{1} x_{2} \\
                     &   & - 16.61 x_{1} x_{3} - 27.67 x_{2} x_{3}
   \end{array}$ $\hat{Y}_{3} = 23.13 x_{1} + 19.73 x_{2} + 14.73 x_{3}$ *The optimization problem*
The optimization problem is therefore:

| **maximize** | $\hat{Y}_{1}(x)$ |
| --- | --- | _{1}(x)

| **subject to:** | $\begin{array}{c} |
| --- | --- |
| **subject to:** | \( \begin{array}{c} |

         \hat{Y}_{2}(x) \le 4.5 \\
         \hat{Y}_{3}(x) \le 20 \\
         x_{1} + x_{2} + x_{3} = 1 \\
         0 \le x_{1} \le 1 \\
         0 \le x_{2} \le 1 \\
         0 \le x_{3} \le 1
         \end{array}$ _{2}(x) 4.5

   
   </td>
    _{3}(x) 20
   </td>
</tr>

   
   </td>
   
      x_{1} + x_{2} +
      x_{3} = 1.0
   </td>
</tr>

   
   </td>
   
      0 x_{1} 1
   </td>
</tr>

   
   </td>
   
      0 x_{2} 1
   </td>
</tr>

   
   </td>
   
      0 x_{3} 1
   </td>
</tr>

 

*Solution*

The solution is
$\mathbf{x}^* = (0.212, 0.343, 0.443)$ which provides
$\hat{Y}_{1} = 106.62$,
$\hat{Y}_{2} = 4.17$, and
$\hat{Y}_{3} = 18.23$. _{1}
= 106.62, _{2}
= 4.17, and _{3}
= 18.23.
Therefore, both secondary responses are below the specified upper bounds.
The optimization should be implemented using a variety of starting points
to avoid local optima.  Once again, confirmatory experiments should be
conducted at the estimated optimal operating conditions.

The solution to the optimization problem can be obtained using.
