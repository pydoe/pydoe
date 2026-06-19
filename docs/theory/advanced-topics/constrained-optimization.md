# Constrained Optimization

*Optimal operating conditions may fall outside region where
experiment conducted*
Sometimes the optimal operating conditions $\mathbf{x}$*
simply fall outside the region where the experiment was conducted.
In these cases, constrained optimization techniques can be used to
find the solution $\mathbf{x}$* that optimizes
$\hat{Y}(x)$
 
without leaving the region in the factor space where the experiment took
place.

*Ridge analysis is a method for finding optimal factor settings that
satisfy certain constraints*
"Ridge Analysis", as developed by
[Hoerl (1959)](../references/index.md),
[Hoerl (1964)](../references/index.md) and
[Draper (1963)](../references/index.md), is an
optimization technique that finds factor settings
$\mathbf{x}$* such that they

   $\mbox{optimize} \hspace{.5in} \hat{Y}(x) = b_{0} + b'x + x'Bx$

   optimize     (x)
   = b_{0} + b'x + x'Bx

$\mbox{subject to} \hspace{.37in} x'x = \rho^{2}$

   subject to:    
   x'x =
   ^{2}

The solution $\mathbf{x}$* to this problem provides
operating conditions that yield an estimated absolute maximum or
minimum response on a sphere of radius ***ρ***.
Different solutions can be obtained by trying different values of
***ρ***.

*Solve with non-linear programming software*
The original formulation of Ridge Analysis was based on the eigenvalues
of a stationarity system.  With the wide availability of non-linear
programming codes, Ridge Analysis problems can be solved without
recourse to eigenvalue analysis.
