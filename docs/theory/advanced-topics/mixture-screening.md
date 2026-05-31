# Mixture Screening Designs

*Screening experiments can be used to identify the important
mixture factors*
In some areas of mixture experiments, for example, certain chemical
industries, there is often a large number, $q$, of potentially
important components that can be considered candidates in an
experiment. The objective of these types of experiments is to screen
the components to identify the ones that are most important.  In this
type of situation, the experimenter should consider a
[screening experiment](../choosing-design/fractional-factorial.md) to reduce
the number of possible components.

*A first order mixture model*
The construction of screening designs and their corresponding models
often begins with the first-order or first-degree mixture model

$$
E(Y) = \beta_{1}x_{1} + \beta_{2}x_{2} + \cdots \beta_{q}x_{q}
$$

for which the beta coefficients are non-negative and sum to one.

*Choices of types of screening designs depend on constraints*
If the experimental region is a [simplex](simplex-lattice.md), it
is generally a good idea to make the ranges of the components as
similar as possible. Then the relative effects of the components can
be assessed by ranking the ratios of the parameter estimates
(i.e., the estimates of the $\beta_{i}$,
 
_{i}),
relative to their standard errors.  Simplex screening designs are
recommended when it is possible to experiment over the total simplex
region. [Constrained mixture designs](constrained-mixture.md) are
suggested when the proportions of some or all of the components are
restricted by upper and lower bounds.  If these designs are not
feasible in this situation, then [D-optimal](d-optimal.md)
designs for a linear model are always an option.
