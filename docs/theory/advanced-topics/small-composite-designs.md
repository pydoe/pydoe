# Small Composite Designs

*Small composite designs save runs, compared to Resolution V
response surface designs, by adding star points to a Resolution III
design*
Response surface designs (RSD) were described
[earlier](../choosing-design/response-surface.md). A typical RSD requires
about 13 runs for 2 factors, 20 runs for 3 factors, 31 runs for 4
factors, and 32 runs for 5 factors.  It is obvious that, once you have
four or more factors you wish to include in a RSD, you will need
more than one lot (i.e., batch) of experimental units for your basic
design.  This is what most statistical software today will give you.
However, there is a way to cut down on
the number of runs, as suggested by H.O. Hartley in his paper
'*Smallest Composite Designs for Quadratic Response Surfaces*',
published in Biometrics, December 1959.

This method addresses the theory that using a Resolution V design as
the smallest fractional design to create a RSD is unnecessary.  The
method adds star points to designs of Resolution III and uses the
star points to clear the main effects of aliasing with the two-factor
interactions. The resulting design allows estimation of the
higher-order interactions. It also provides poor interaction coefficient
estimates and should not be used unless the error variability is
negligible compared to the systematic effects of the factors.

*Useful for 4 or 5 factors*
This could be particularly useful when you have a design containing
four or five factors and you wish to only use the experimental units
from one lot (i.e., batch).

*Table containing design matrix for four factors*
The following is a design for four factors.  You would want to
randomize these runs before implementing them;  -1 and +1 represent
the low and high settings, respectively, of each factor.

**TABLE 5.11  Four factors:  Factorial design section is based on a
   generator of I = X1*X2*X3, Resolution    III; -*α* and +*α* are the star points,
   calculated beyond the factorial range; 0 represents the midpoint of
   the factor range**.

| Row | X1 | X2 | X3 | X4 |
| --- | --- | --- | --- | --- |
| 1 | +1 | -1 | -1 | -1 |
| 2 | -1 | +1 | -1 | -1 |
| 3 | -1 | -1 | +1 | -1 |
| 4 | +1 | +1 | +1 | -1 |
| 5 | +1 | -1 | -1 | +1 |
| 6 | -1 | +1 | -1 | +1 |
| 7 | -1 | -1 | +1 | +1 |
| 8 | +1 | +1 | +1 | +1 |
| 9 | -*α* | 0 | 0 | 0 |
| 10 | *α* | 0 | 0 | 0 |
| 11 | 0 | -*α* | 0 | 0 |
| 12 | 0 | *α* | 0 | 0 |
| 13 | 0 | 0 | -*α* | 0 |
| 14 | 0 | 0 | *α* | 0 |
| 15 | 0 | 0 | 0 | -*α* |
| 16 | 0 | 0 | 0 | *α* |
| 17 | 0 | 0 | 0 | 0 |
| 18 | 0 | 0 | 0 | 0 |
| 19 | 0 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 | 0 |

**Determining *α*
in Small Composite Designs**

**α* based on number of treatment combinations in the factorial portion*
To maintain rotatability for usual CCD's, the value of *α* is
determined by the number of treatment combinations in the factorial
portion of the central composite design:

$\alpha = \left[ \mbox{number of factorial runs} \right] ^{1/4}$ *Small composite designs not rotatable*
However, small composite designs are not rotatable, regardless of the
choice of *α*.  For small composite designs,
*α* should not be smaller than $[\text{number of factorial runs}]^{1/4}$ nor larger than $k^{1/2}$.
