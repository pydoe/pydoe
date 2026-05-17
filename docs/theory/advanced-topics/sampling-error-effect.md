# Effect of Sampling Error

*Experimental error means all derived optimal operating conditions
are just estimates - confidence regions that are likely to contain the
optimal points can be derived*
Process engineers should be aware that the estimated optimal operating
conditions $\mathbf{x}$* represent a single estimate of
the true (unknown) system optimal point.  That is, due to sampling
(experimental) error, if the experiment is repeated, a different
quadratic function will be fitted which will yield a different
stationary point $\mathbf{x}$*.  Some authors
([Box and Hunter](../references/index.md), 1954;
[Myers and Montgomery](../references/index.md), 1995)
provide a procedure that allows one to compute a region in the factor
space that, with a specified probability, contains the system
stationary point.  This region is useful information for a process
engineer in that it provides a measure of how "good" the point
estimate $\mathbf{x}$* is.  In general, the larger this
region is, the less reliable the point estimate
$\mathbf{x}$* is.  When the number of factors, $k$,
is greater than 3, these confidence regions are difficult to visualize.

*Confirmation runs are very important*
Awareness of experimental error should make a process engineer realize
the importance of performing confirmation runs at
$\mathbf{x}$*, the estimated optimal operating conditions.
