# John's 3/4 Fractional Factorial Designs

*John's designs require only 3/4 of the number of runs a full
2n factorial would require*
Three-quarter (¾) designs are two-level factorial designs that
require only three-quarters of the number of runs of the 'original'
design. For example, instead of making all of the sixteen runs required
for a 24 fractional factorial design, we need only run 12 of
them.  Such designs were invented by Professor Peter John of the
University of Texas, and are sometimes called 'John's ¾
designs.'

Three-quarter fractional factorial designs can be used to save on
resources in two different contexts. In one scenario, we may wish to
perform additional runs after having completed a fractional factorial,
so as to de-alias certain specific interaction patterns.  Second , we
may wish to use a ¾ design to begin with and thus save on 25%
of the run requirement of a regular design.

**Semifolding Example**

*Four experimental factors*
We have four experimental factors to investigate, namely
$X_1$, $X_2$, $X_3$, and $X_4$, and we have designed and run a 24-1
fractional factorial design. Such a design has eight runs, or rows, if
we don't count center point runs (or replications).

*Resolution IV design*
The 24-1 design is of resolution IV, which means that main
effects are confounded with, at worst, three-factor interactions, and
two-factor interactions are confounded with other two factor
interactions.

*Design matrix*
The design matrix, in standard order, is shown in Table 5.8 along with
all the two-factor interaction columns. Note that the column for
$X_4$ is constructed by multiplying columns for
$X_1$, $X_2$, and $X_3$
together (i.e., 4=123).

**Table 5.8: The 24-1 design plus 2-factor
   interaction columns shown in standard order. Note that 4=123.**

| Run |
| Two-Factor Interaction Columns |
|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number | X1 | X2 | X3 | X4 |
| X1*X2 | X1*X3 | X1*X4 | X2*X3 | X2*X4 | X3*X4 |
| 1 | -1 | -1 | -1 | -1 |
| +1 | +1 | +1 | +1 | +1 | +1 |
| 2 | +1 | -1 | -1 | +1 |
| -1 | -1 | +1 | +1 | -1 | -1 |
| 3 | -1 | +1 | -1 | +1 |
| -1 | +1 | -1 | -1 | +1 | -1 |
| 4 | +1 | +1 | -1 | -1 |
| +1 | -1 | -1 | -1 | -1 | +1 |
| 5 | -1 | -1 | +1 | +1 |
| +1 | -1 | -1 | -1 | -1 | +1 |
| 6 | +1 | -1 | +1 | -1 |
| -1 | +1 | -1 | -1 | +1 | -1 |
| 7 | -1 | +1 | +1 | -1 |
| -1 | -1 | +1 | +1 | -1 | -1 |
| 8 | +1 | +1 | +1 | +1 |
| +1 | +1 | +1 | +1 | +1 | +1 |

 

*Confounding of two-factor interactions*
Note also that 12=34, 13=24, and 14=23. These follow from the generating
relationship 4=123 and tells us that we cannot estimate any two-factor
interaction that is free of some other two-factor alias.

*Estimating two-factor interactions free of confounding*
Suppose that we became interested in estimating some or all of the
two-factor interactions that involved factor $X_1$; that
is, we want to estimate one or more of the interactions 12, 13, and 14
free of two-factor confounding.

One way of doing this is to run the 'other half' of the design: an
additional eight rows formed from the relationship 4 = -123. Putting
these two 'halves' together, the original one and the new one,
we'd obtain a 24 design in sixteen runs. Eight of these
runs would already have been run, so all we'd need to do is run the
remaining half.

*Alternative method requiring fewer runs*
There is a way, however, to obtain what we want while adding only four
more runs.  These runs are selected in the following manner: take the
four rows of Table 5.8 that have '-1' in the '$X_1$' column and switch the '-' sign under $X_1$ to '+' to
obtain the four-row table of Table 5.9.  This is called a foldover on
$X_1$, choosing the subset of runs with
$X_1$ = -1. Note that this choice of 4 runs is not
unique, and that if the initial design suggested that
$X_1$ = -1 were a desirable level, we would have chosen
to experiment at the other four treatment combinations that were omitted
from the initial design.

*Table of the additional design points*

**TABLE 5.9: Foldover on '$X_1$' of the    24-1 design of Table 5.5**

Run
      Number
| X1 | X2 | X3 | X4 |
| --- | --- | --- | --- | --- |
| 9 | +1 | -1 | -1 | -1 |
| 10 | +1 | +1 | -1 | +1 |
| 11 | +1 | -1 | +1 | +1 |
| 12 | +1 | +1 | +1 | -1 |

 

*Table with new design points added to the original design points*
Add this new block of rows to the bottom of Table 5.8 to obtain a
design in twelve rows. We show this in Table 5.10 and also add in the
two-factor interactions as well for illustration (not needed when we
do the runs).

**TABLE 5.10: A twelve-run design based on the 24-1
   also showing all two-factor interaction columns**

| Run |
| Two-Factor Interaction Columns |
|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number | X1 | X2 | X3 | X4 |
| X1*X2 | X1*X3 | X1*X4 | X2*X3 | X2*X4 | X3*X4 |
| 1 | -1 | -1 | -1 | -1 |
| +1 | +1 | +1 | +1 | +1 | +1 |
| 2 | +1 | -1 | -1 | +1 |
| -1 | -1 | +1 | +1 | -1 | -1 |
| 3 | -1 | +1 | -1 | +1 |
| -1 | +1 | -1 | -1 | +1 | -1 |
| 4 | +1 | +1 | -1 | -1 |
| +1 | -1 | -1 | -1 | -1 | +1 |
| 5 | -1 | -1 | +1 | +1 |
| +1 | -1 | -1 | -1 | -1 | +1 |
| 6 | +1 | -1 | +1 | -1 |
| -1 | +1 | -1 | -1 | +1 | -1 |
| 7 | -1 | +1 | +1 | -1 |
| -1 | -1 | +1 | +1 | -1 | -1 |
| 8 | +1 | +1 | +1 | +1 |
| +1 | +1 | +1 | +1 | +1 | +1 |
| 1 | +1 | -1 | -1 | -1 |
| -1 | -1 | -1 | +1 | +1 | +1 |
| 10 | +1 | +1 | -1 | +1 |
| +1 | -1 | +1 | -1 | +1 | -1 |
| 11 | +1 | -1 | +1 | +1 |
| -1 | +1 | +1 | -1 | -1 | +1 |
| 12 | +1 | +1 | +1 | -1 |
| +1 | +1 | -1 | +1 | -1 | -1 |

 

*Design is resolution V*
Examine the two-factor interaction columns and convince yourself that
no two are alike. This means that no two-factor interaction involving
$X_1$ is aliased with any other two-factor interaction.
Thus, the design is resolution V, which is not always the case when
constructing these types of ¾ foldover designs.

*Estimating X1 two-factor interactions*
What we now have is a design with 12 runs, with which we can estimate
all the two-factor interactions involving $X_1$ free of
aliasing with any other two-factor interaction. It is called a ¾
design because it has ¾ the number of rows of the next regular
factorial design (a 24).

*Standard errors of effect estimates*
If one fits a model with an intercept, a block effect, the four main
effects and the six two-factor interactions, then each coefficient has a
standard error of
*σ*/81/2, instead of
*σ*/121/2, because the design is not orthogonal
and each estimate is correlated with two other estimates.  Note that no
degrees of freedom exists for estimating *σ*.  Instead, one
should plot the 10 effect estimates using a normal (or half-normal)
effects plot to judge which effects to declare significant.

*Further information*
For more details on ¾ fractions obtained by adding a follow-up
design that is half the size of the original design, see
[Mee
and Peralta (2000)](../references/index.md).

Next we consider an example in which a ¾ fraction arises when the
(¾) 2k-p design is planned from the start because it
is an efficient design that allows estimation of a sufficient number of
effects.

**A 48-Run 3/4 Design Example**

*Estimate all main effects and two-factor interactions for 8 factors*
Suppose we wish to run an experiment for $k$=8 factors, with which
we want to estimate all main effects and two-factor interactions. We
could use the $2_{V}^{8-2}$ design described in the [summary table
of fractional factorial designs](../choosing-design/fractional-factorial-tables.md), but this would require a 64-run
experiment to estimate the 1 + 8 + 28 = 37 desired coefficients. In
this context, and especially for larger resolution V designs, ¾
of the design points will generally suffice.

*Construction of the 48-run design*
The 48 run-design is constructed as follows: start by creating the full
$2_{V}^{8-2}$ design using the generators 7 = 1234 and 8 = 1256. The defining relation
is I = 12347 = 12568 = 345678 (see the summary table
[details](../section3/eqns/2to8m2.txt) for this design).

Next, arrange these 64 treatment combinations into four blocks of size
16, blocking on the interactions 135 and 246 (i.e., block 1 has
135 = 246 = -1 runs, block 2 has 135 = -1, 246 = +1, block 3 has
135 = +1, 246 = -1 and block 4 has 135 = 246 = +1). If we exclude the
first block in which 135 = 246 = -1, we have the desired ¾ design
reproduced below (the reader can verify that these are the runs
described in the summary table, excluding the runs numbered 1, 6, 11,
16, 18, 21, 28, 31, 35, 40, 41,46, 52, 55, 58 and 61).

*Table containing the design matrix*

| X1 | X2 | X3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X4 | X5 | X6 | X7 | X8 |
| +1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| -1 | +1 | -1 | -1 | -1 | -1 | -1 | -1 |
| +1 | +1 | -1 | -1 | -1 | -1 | +1 | +1 |
| -1 | -1 | +1 | -1 | -1 | -1 | -1 | +1 |
| -1 | +1 | +1 | -1 | -1 | -1 | +1 | -1 |
| +1 | +1 | +1 | -1 | -1 | -1 | -1 | +1 |
| -1 | -1 | -1 | +1 | -1 | -1 | -1 | +1 |
| +1 | -1 | -1 | +1 | -1 | -1 | +1 | -1 |
| +1 | +1 | -1 | +1 | -1 | -1 | -1 | +1 |
| -1 | -1 | +1 | +1 | -1 | -1 | +1 | +1 |
| +1 | -1 | +1 | +1 | -1 | -1 | -1 | -1 |
| -1 | +1 | +1 | +1 | -1 | -1 | -1 | -1 |
| -1 | -1 | -1 | -1 | +1 | -1 | +1 | -1 |
| -1 | +1 | -1 | -1 | +1 | -1 | -1 | +1 |
| +1 | +1 | -1 | -1 | +1 | -1 | +1 | -1 |
| +1 | -1 | +1 | -1 | +1 | -1 | +1 | +1 |
| -1 | +1 | +1 | -1 | +1 | -1 | +1 | +1 |
| +1 | +1 | +1 | -1 | +1 | -1 | -1 | -1 |
| -1 | -1 | -1 | +1 | +1 | -1 | -1 | -1 |
| +1 | -1 | -1 | +1 | +1 | -1 | +1 | +1 |
| -1 | +1 | -1 | +1 | +1 | -1 | +1 | +1 |
| -1 | -1 | +1 | +1 | +1 | -1 | +1 | -1 |
| +1 | -1 | +1 | +1 | +1 | -1 | -1 | +1 |
| +1 | +1 | +1 | +1 | +1 | -1 | +1 | -1 |
| -1 | -1 | -1 | -1 | -1 | +1 | +1 | -1 |
| +1 | -1 | -1 | -1 | -1 | +1 | -1 | +1 |
| +1 | +1 | -1 | -1 | -1 | +1 | +1 | -1 |
| -1 | -1 | +1 | -1 | -1 | +1 | -1 | -1 |
| +1 | -1 | +1 | -1 | -1 | +1 | +1 | +1 |
| -1 | +1 | +1 | -1 | -1 | +1 | +1 | +1 |
| +1 | -1 | -1 | +1 | -1 | +1 | +1 | +1 |
| -1 | +1 | -1 | +1 | -1 | +1 | +1 | +1 |
| +1 | +1 | -1 | +1 | -1 | +1 | -1 | -1 |
| -1 | -1 | +1 | +1 | -1 | +1 | +1 | -1 |
| -1 | +1 | +1 | +1 | -1 | +1 | -1 | +1 |
| +1 | +1 | +1 | +1 | -1 | +1 | +1 | -1 |
| -1 | -1 | -1 | -1 | +1 | +1 | +1 | +1 |
| +1 | -1 | -1 | -1 | +1 | +1 | -1 | -1 |
| -1 | +1 | -1 | -1 | +1 | +1 | -1 | -1 |
| -1 | -1 | +1 | -1 | +1 | +1 | -1 | +1 |
| +1 | -1 | +1 | -1 | +1 | +1 | +1 | -1 |
| +1 | +1 | +1 | -1 | +1 | +1 | -1 | +1 |
| -1 | -1 | -1 | +1 | +1 | +1 | -1 | +1 |
| -1 | +1 | -1 | +1 | +1 | +1 | +1 | -1 |
| +1 | +1 | -1 | +1 | +1 | +1 | -1 | +1 |
| +1 | -1 | +1 | +1 | +1 | +1 | -1 | -1 |
| -1 | +1 | +1 | +1 | +1 | +1 | -1 | -1 |
| +1 | +1 | +1 | +1 | +1 | +1 | +1 | +1 |

*Good precision for coefficient estimates*
This design provides 11 degrees of freedom for error and also provides
good precision for coefficient estimates (some of the coefficients have
a standard error of $\sigma/\sqrt{32}$ and some have a standard error of $\sigma/\sqrt{42.55}$. ).

*Further information*
More about John's ¾ designs can be found in
[John (1971)](../references/index.md) or
[Diamond (1989)](../references/index.md).
