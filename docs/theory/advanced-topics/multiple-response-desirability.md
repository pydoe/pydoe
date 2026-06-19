# Multiple Responses: The Desirability Approach

*The desirability approach is a popular method that assigns a
"score" to a set of responses and chooses factor settings that
maximize that score*
The desirability function approach is one of the most widely used
methods in industry for the optimization of multiple response
processes.  It is based on the idea that the "quality" of a product
or process that has multiple quality characteristics, with one of
them outside of some "desired" limits, is completely unacceptable.
The method finds operating conditions $\mathbf{x}$
that provide the "most desirable" response values.

For each response **$Y_i$($x$)**,
a desirability function
**$d_i$($Y_i$)** assigns numbers between 0 and 1 to the possible values of **$Y_i$**,
with
**$d_i$($Y_i$) = 0** representing
a completely undesirable value of
**$Y_i$** and
**$d_i$($Y_i$) = 1** representing
a completely desirable or ideal response value.  The individual
desirabilities are then combined using the geometric mean, which gives
the *overall desirability* $D$:

   $D = \left( d_{1}(Y_{1}) d_{2}(Y_{2}) \cdots
   d_{k}(Y_{k})\right) ^{1/k}$ with $k$ denoting the number of responses. Notice that if
any response **$Y_i$** is completely undesirable
**($d_i$($Y_i$) = 0)**,
then the overall desirability is zero.  In practice, fitted response
values $\hat{Y}_{i}$
are used in place of the **$Y_i$**.

*Desirability functions of Derringer and Suich*
Depending on whether a particular response
**$Y_i$** is to be maximized, minimized, or assigned
a target value, different desirability functions
**$d_i$($Y_i$)** can be used.  A
useful class of desirability functions was proposed by
[Derringer and Suich (1980)](../references/index.md).
Let **$L_i$, $U_i$** and
**$T_i$** be the lower, upper, and target values,
respectively, that are desired for response
**$Y_i$**, with **$L_i$** ≤
**$T_i$** ≤ **$U_i$**.

*Desirability function for "target is best"*
If a response is of the "target is best"
kind, then its individual desirability function is

   $d_{i}(\hat{Y}_{i}) =
     \left\{ \begin{array}{ll}
             0  & \mbox{if } \hspace{.1in} \hat{Y}_{i}(x) < L_{i} \\
             \left( \frac{\hat{Y}_{i}(x) - L_{i}} {T_{i} - L_{i}}
             \right) ^{s} &
             \mbox{if } \hspace{.1in}
                         L_{i} \le \hat{Y}_{i}(x) \le T_{i} \\
             \left( \frac{\hat{Y}_{i}(x) - U_{i}} {T_{i} - U_{i}}
             \right) ^{t} &
             \mbox{if } \hspace{.1in}
                         T_{i} \le \hat{Y}_{i}(x) \le U_{i} \\
             0  & \mbox{if } \hspace{.1in} \hat{Y}_{i}(x) > U_{i}
            \end{array}
     \right.$

with the exponents $s$ and $t$ determining how important it is to hit the target value.  For **$s$ = $t$
= 1**, the desirability function increases linearly towards
**$T_i$**; for **$s$ < 1,
$t$ < 1**, the function is convex, and for
**$s$ > 1, $t$ > 1**, the function is concave (see
the example below for an illustration).

*Desirability function for maximizing a response*
If a response is to be maximized instead, the individual desirability
is defined as

   $d_{i}(\hat{Y}_{i}) =
     \left\{ \begin{array}{ll}
             0  & \mbox{if } \hspace{.1in} \hat{Y}_{i}(x) < L_{i} \\
             \left( \frac{\hat{Y}_{i}(x) - L_{i}} {T_{i} - L_{i}}
             \right) ^{s} &
             \mbox{if } \hspace{.1in}
                         L_{i} \le \hat{Y}_{i}(x) \le T_{i} \\
             1.0  & \mbox{if } \hspace{.1in} \hat{Y}_{i}(x) > T_{i}
            \end{array}
     \right.$

with *$T_i$*** in this case interpreted as a large
enough value for the response.

*Desirability function for minimizing a response*
Finally, if we want to minimize a response, we could use

   $d_{i}(\hat{Y}_{i}) =
     \left\{ \begin{array}{ll}
             1.0  & \mbox{if } \hspace{.1in} \hat{Y}_{i}(x) < T_{i} \\
             \left( \frac{\hat{Y}_{i}(x) - U_{i}} {T_{i} - U_{i}}
             \right) ^{s} &
             \mbox{if } \hspace{.1in}
                         T_{i} \le \hat{Y}_{i}(x) \le U_{i} \\
             0  & \mbox{if } \hspace{.1in} \hat{Y}_{i}(x) > U_{i}
            \end{array}
     \right.$

with *$T_i$*** denoting a small enough value for
the response.

*Desirability approach steps*
The desirability approach consists of the following steps:

- Conduct experiments and fit response models for all $k$
       responses;

- Define individual desirability functions for each response;

- *Maximize* the overall desirability $D$ with
       respect to the controllable factors.

**Example:**

*An example using the desirability approach*
[Derringer and Suich (1980)](../references/index.md)
present the following multiple response experiment arising in the
development of a tire tread compound.  The controllable factors are:
**$x_1$**, hydrated silica level,
**$x_2$**, silane coupling agent level, and
**$x_3$**, sulfur level.  The four responses to be
optimized and their desired ranges are:

*Factor and response variables*

| Source | Desired range |
| --- | --- |
| PICO Abrasion index, **$Y_1$** | 120 < **$Y_1$** |
| 200% modulus, **$Y_2$** | 1000 < **$Y_2$** |
| Elongation at break, **$Y_3$** | 400 < **$Y_3$** < 600 |
| Hardness, **$Y_4$** | 60 < **$Y_4$** < 75 |

 
The first two responses are to be maximized, and the value
*$s=1$* was chosen for their desirability functions. The
last two responses are "target is best" with
**$T_3$ = 500** and
**$T_4$ = 67.5**.  The values
**s=t=1** were chosen in both cases.

*Experimental runs from a central composite design*
The following experiments were conducted using a central
composite design.

Run
      Number
| $x_1$ | $x_2$ | $x_3$ | $Y_1$ | $Y_2$ | $Y_3$ | $Y_4$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | -1.00 | -1.00 | -1.00 | 102 | 900 | 470 | 67.5 |
| 2 | +1.00 | -1.00 | -1.00 | 120 | 860 | 410 | 65.0 |
| 3 | -1.00 | +1.00 | -1.00 | 117 | 800 | 570 | 77.5 |
| 4 | +1.00 | +1.00 | -1.00 | 198 | 2294 | 240 | 74.5 |
| 5 | -1.00 | -1.00 | +1.00 | 103 | 490 | 640 | 62.5 |
| 6 | +1.00 | -1.00 | +1.00 | 132 | 1289 | 270 | 67.0 |
| 7 | -1.00 | +1.00 | +1.00 | 132 | 1270 | 410 | 78.0 |
| 8 | +1.00 | +1.00 | +1.00 | 139 | 1090 | 380 | 70.0 |
| 9 | -1.63 | 0.00 | 0.00 | 102 | 770 | 590 | 76.0 |
| 10 | +1.63 | 0.00 | 0.00 | 154 | 1690 | 260 | 70.0 |
| 11 | 0.00 | -1.63 | 0.00 | 96 | 700 | 520 | 63.0 |
| 12 | 0.00 | +1.63 | 0.00 | 163 | 1540 | 380 | 75.0 |
| 13 | 0.00 | 0.00 | -1.63 | 116 | 2184 | 520 | 65.0 |
| 14 | 0.00 | 0.00 | +1.63 | 153 | 1784 | 290 | 71.0 |
| 15 | 0.00 | 0.00 | 0.00 | 133 | 1300 | 380 | 70.0 |
| 16 | 0.00 | 0.00 | 0.00 | 133 | 1300 | 380 | 68.5 |
| 17 | 0.00 | 0.00 | 0.00 | 140 | 1145 | 430 | 68.0 |
| 18 | 0.00 | 0.00 | 0.00 | 142 | 1090 | 430 | 68.0 |
| 19 | 0.00 | 0.00 | 0.00 | 145 | 1260 | 390 | 69.0 |
| 20 | 0.00 | 0.00 | 0.00 | 142 | 1344 | 390 | 70.0 |

(The reader can download the data as a
text file.)

*Fitted response*
Using ordinary least squares and standard diagnostics, the fitted
responses are:

$\begin{array}{lcl}
    \hat{Y}_{1} & = & 139.12 + 16.49 x_{1} + 17.88 x_{2} + 2.21 x_{3} \\
                &   & -4.01 x_{1}^{2} - 3.45 x_{2}^{2} -
                      1.57 x_{3}^{2} \\
                &   & + 5.12 x_{1} x_{2} - 7.88 x_{1} x_{3} -
                      7.13 x_{2} x_{3}
    \end{array}$ (**$R^2$ = 0.8369** and adjusted **$R^2$ = 0.6903**);

$\begin{array}{lcl}
    \hat{Y}_{2} & = & 1261.13 + 268.15 x_{1} + 246.5 x_{2} -
                      102.6 x_{3} \\
                &   & - 83.57 x_{1}^{2} - 124.92 x_{2}^{2} +
                      199.2 x_{3}^{2} \\
                &   & + 69.37 x_{1} x_{2} - 104.38 x_{1} x_{3} -
                      94.13 x_{2} x_{3}
    \end{array}$ (**$R^2$ = 0.7137** and adjusted **$R^2$ = 0.4562**);

$\hat{Y}_{3} = 417.5 - 99.67 x_{1} - 31.4 x_{2} - 27.42 x_{3}$ (**$R_2$ = 0.682** and adjusted **$R_2$ = 0.6224**);

$\begin{array}{lcl}
    \hat{Y}_{4} & = & 68.91 - 1.41 x_{1} + 4.32 x_{2} + 0.21 x_{3} \\
                &   & + 1.56 x_{1}^{2} + 0.058 x_{2}^{2} -
                      0.32 x_{3}^{2} \\
                &   & - 1.62 x_{1} x_{2} + 0.25 x_{1} x_{3} -
                      0.12 x_{2} x_{3}
    \end{array}$ (**$R^2$ = 0.8667** and adjusted **$R^2$ = 0.7466**).

Note that no interactions were significant for response 3 and that
the fit for response 2 is quite poor.

*Best Solution*
The best solution is $\mathbf{x}^* = (-0.10, 0.15, -1.0)$ and results in:

| $d_{1}(\hat{Y}_{1}) = 0.34$ | $(\hat{Y}_{1}(x^{*}) = 136.4)$ |
| --- | --- |
| $d_{2}(\hat{Y}_{2}) = 1.0$ | $(\hat{Y}_{2}(x^{*}) = 1571.05)$ |
| $d_{3}(\hat{Y}_{3}) = 0.49$ | $(\hat{Y}_{3}(x^{*}) = 450.56)$ |
| $d_{4}(\hat{Y}_{4}) = 0.76$ | $(\hat{Y}_{4}(x^{*}) = 69.26)$ |

The overall desirability for this solution is 0.596. All responses
are predicted to be within the desired limits.

*3D plot of the overall desirability function*
Figure 5.8 shows a 3D plot of the overall desirability function
$D(x)$ for the
**($x_2$, $x_3$)** plane when
**$x_1$** is fixed at -0.10. The function
$D(x)$ is quite "flat" in the vicinity of the
optimal solution, indicating that small variations around
$\mathbf{x}$* are predicted to not change the overall
desirability drastically.  However, the importance of performing
confirmatory runs at the estimated optimal operating conditions should
be emphasized.  This is particularly true in this example given the
poor fit of the response models (e.g., $\hat{Y}_{2}$).).

![3D plot of overall desirability function in the (x2,x3) plane](https://www.itl.nist.gov/div898/handbook/pri/section5/pri5322_r01.gif)

**FIGURE 5.8: Overall Desirability Function for Example
Problem**
