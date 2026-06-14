# Simplex-Centroid Designs

*Definition of simplex-

centroid designs*
A second type of mixture design is the simplex-centroid design. In the
$q$-component simplex-centroid design, the number of distinct points
is 2$q$ - 1. These points correspond to $q$
permutations of (1, 0, 0, ..., 0) or $q$ single component blends, the
$\small \left( \begin{array}{c} q \\ 2 \end{array} \right)$ permutations of (.5, .5, 0, ..., 0) or all binary mixtures, the
$\small \left( \begin{array}{c} q \\ 3 \end{array} \right)$ permutations of (1/3, 1/3, 1/3, 0, ..., 0), ..., and so on, with
finally the overall centroid point (1/$q$, 1/$q$, ..., 1/$q$) or $q$-nary mixture.

*Model supported by simplex-

centroid designs*
The design points in the Simplex-Centroid design will support
the polynomial

$$
\begin{array}{lcl}
   E(Y) & = & \sum_{i=1}^{q}{\beta_{i}x_{i}} +
              \sum_{i=1}^{q}{\sum_{i < j}^{q}{\beta_{ij}x_{i}x_{j}}} + \\
        &   & \sum_{k=1}^{q}{\sum_{j < k}^{q}{\sum_{i < j}^{q}
              {\beta_{ijk}x_{i}x_{j}x_{k}}}} + \cdots + \\
        &   & \beta_{12 \dots q}x_{i}x_{j} \dots x_{q}
   \end{array}
$$
 which is the $q$th-order mixture polynomial. For $q$ = 2, this is the quadratic model. For $q$ = 3, this is the
special cubic model.

*Example of runs for three and four components*
For example, the fifteen runs for a four component ($q$ = 4) For example, the fifteen runs for a four component ($q$ = 4)
simplex-centroid design are:

   (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (.5,.5,0,0),
   (.5,0,.5,0) ..., (0,0,.5,.5), (1/3,1/3,1/3,0), ...,(0,1/3,1/3,1/3),
   (1/4,1/4,1/4,1/4).

The runs for a three component simplex-centroid design of degree 2 are

   (1,0,0), (0,1,0), (0,0,1), (.5,.5,0), (.5,0,.5), (0,.5,.5),
   (1/3, 1/3, 1/3).

However, in order to fit a first-order model with $q$ =4, only
the five runs with a "1" and all "1/4's" would be needed.  To fit a
second-order model, add the six runs with a ".5" (this also fits a
saturated third-order model, with no degrees of freedom left for error).
