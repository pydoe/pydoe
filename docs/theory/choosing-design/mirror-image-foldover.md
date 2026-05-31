# Mirror-Image Foldover Designs

*A foldover design is obtained from a fractional factorial design
by reversing the signs of all the columns*
A mirror-image fold-over (or foldover, without the hyphen) design is
used to augment [fractional factorial designs](fractional-factorial.md) to
increase the [resolution](../glossary/index.md) of $2_{III}^{3-1}$
and Plackett-Burman designs.  It is obtained by reversing the signs of
all the columns of the original design matrix.  The original design
runs are combined with the mirror-image fold-over design runs, and this
combination can then be used to estimate all main effects clear of any
two-factor interaction.  This is referred to as: *breaking the alias link between main effects and two-factor interactions.*

Before we illustrate this concept with an example, we briefly review
the basic concepts involved.

| **Review of Fractional 2k-p Designs** |
| --- | --- |
| *A resolution III design, combined with its mirror-image foldover, |

becomes resolution IV*
In general, a design type that uses a specified fraction of the runs
from a full factorial and is balanced and orthogonal is called a
*fractional factorial*.

A 2-level fractional factorial is constructed as follows: *Let the
number of runs be 2k-p. Start by constructing the full
factorial for the k-p variables.  Next associate the extra factors
with higher-order interaction columns.  The
[Table](fractional-factorial-tables.md) shown previously details how to
do this to achieve a minimal amount of confounding.*

For example, consider the 25-2 design (a resolution III
design).  The full factorial for $k$ = 5 requires 25 = 32
runs.  The fractional factorial can be achieved in 25-2 = 8
runs, called a quarter (1/4) fractional design, by setting
$X_4$ = $X_1$*$X_2$ and
$X_5$ = $X_1$*$X_3$.

*Design matrix for a 25-2 fractional factorial*

The design matrix for a 25-2 fractional factorial looks like:

**TABLE 3.34: Design Matrix for a 25-2 Fractional
   Factorial**

| run | $X_1$ | $X_2$ | $X_3$ | $X_4$ = $X_1$$X_2$ | $X_5$ = $X_1$$X_3$ |
| --- | --- | --- | --- | --- | --- |
| 1 | -1 | -1 | -1 | +1 | +1 |
| 2 | +1 | -1 | -1 | -1 | -1 |
| 3 | -1 | +1 | -1 | -1 | +1 |
| 4 | +1 | +1 | -1 | +1 | -1 |
| 5 | -1 | -1 | +1 | +1 | -1 |
| 6 | +1 | -1 | +1 | -1 | +1 |
| 7 | -1 | +1 | +1 | -1 | -1 |
| 8 | +1 | +1 | +1 | +1 | +1 |
| **Design Generators, Defining Relation and the Mirror-Image Foldover** |
| --- | --- |
| *Increase to resolution IV design by augmenting design matrix* | In this design the $X_1$$X_2$ column was |

used to generate the $X_4$ main effect and the
$X_1$$X_3$ column was used to generate the
$X_5$ main effect.  The design generators are:
4 = 12 and 5 = 13 and the defining relation is I = 124 = 135 = 2345.
Every main effect is confounded (aliased) with at least one first-order
interaction (see the [confounding structure](eqns/2to5m2.txt)
for this design).

We can increase the resolution of this design to IV if we augment the
8 original runs, adding on the 8 runs from the mirror-image fold-over
design.  These runs make up another 1/4 fraction design with design
generators 4 = -12 and 5 = -13 and defining relation
I = -124 = -135 = 2345. The augmented runs are:

*Augmented runs for the design matrix*

| run | $X_1$ | $X_2$ | $X_3$ | $X_4$ = -$X_1$$X_2$ |

$X_5$ = -$X_1$$X_3$
| 9 | +1 | +1 | +1 | -1 | -1 |
| 10 | -1 | +1 | +1 | +1 | +1 |
| 11 | +1 | -1 | +1 | +1 | -1 |
| 12 | -1 | -1 | +1 | -1 | +1 |
| 13 | +1 | +1 | -1 | -1 | +1 |
| 14 | -1 | +1 | -1 | +1 | -1 |
| 15 | +1 | -1 | -1 | +1 | +1 |
| 16 | -1 | -1 | -1 | -1 | -1 |
| *Mirror-image foldover design reverses all signs in original design |
*Mirror-image foldover design reverses all signs in original design
matrix*
A *mirror-image foldover design* is the original design with *all A *mirror-image foldover design* is the original design with *all signs reversed*.  It breaks the alias chains between *every main factor and two-factor interaction*of a resolution III design.  That
is, we can estimate *all the main effects clear of any two-factor
interaction*.

| **A 1/16 Design Generator |
| --- | --- |
| **A 1/16 Design Generator |

Example**

*27-3 example*

Now we consider a more complex example.

We would like to study the effects of 7 variables.  A full 2-level
factorial, 27, would require 128 runs.

Assume economic reasons restrict us to 8 runs.  We will build a
27-4 = 23 full factorial and assign certain
products of columns to the $X_4$, $X_5$, $X_6$ and
$X_7$ variables.  This will generate a resolution III
design in which all of the main effects are aliased with first-order
and higher interaction terms.  The design matrix (see the previous
[Table](fractional-factorial-tables.md) for a complete description of
this fractional factorial design) is:

*Design matrix for 27-3 fractional factorial*

**Design Matrix for a 27-3 Fractional Factorial** |  |  |  |  |
| run | $X_1$ | $X_2$ | $X_3$ | $X_4$ = $X_1$$X_2$ | $X_5$ = $X_1$$X_3$ | $X_6$ = $X_2$$X_3$ | $X_7$ = |

      $X_1$$X_2$$X_3$

| 1 | -1 | -1 | -1 | +1 | +1 | +1 | -1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | +1 | -1 | -1 | -1 | -1 | +1 | +1 |
| 3 | -1 | +1 | -1 | -1 | +1 | -1 | +1 |
| 4 | +1 | +1 | -1 | +1 | -1 | -1 | -1 |
| 5 | -1 | -1 | +1 | +1 | -1 | -1 | +1 |
| 6 | +1 | -1 | +1 | -1 | +1 | -1 | -1 |
| 7 | -1 | +1 | +1 | -1 | -1 | +1 | -1 |
| 8 | +1 | +1 | +1 | +1 | +1 | +1 | +1 |
*Design generators and defining relation for this example*

The design generators for this 1/16 fractional factorial design are:

   4 = 12, 5 = 13, 6 = 23 and 7 = 123

From these we obtain, by multiplication, the defining relation:

   I = 124 = 135 = 236 = 347 = 257 = 167 = 456 = 1237 =

2345 = 1346 = 1256 = 1457 = 2467 = 3567 = 1234567.

*Computing alias structure for complete design*

Using this defining relation, we can easily compute the alias structure

for the complete design, as shown previously in the
[link to the fractional design Table](eqns/2to7m4.txt) given
[earlier](fractional-factorial-tables.md).  For example, to figure out which
effects are aliased (confounded) with factor $X_1$ we
multiply the defining relation by 1 to obtain:

   1 = 24 = 35 = 1236 = 1347 = 1257 = 67 = 1456 = 237 = 12345 = 346
   = 256 = 457 = 12467 = 13567 = 234567

In order to simplify matters, let us ignore all interactions with 3 or
more factors; we then have the following 2-factor alias pattern for
$X_1$: 1 = 24 = 35 = 67 or, using the full notation,
$X_1$ = $X_2$*$X_4$ =
$X_3$*$X_5$ =
$X_6$*$X_7$.

The same procedure can be used to obtain all the other aliases for each
of the main effects, generating the following list:

1 = 24 = 35 = 67

2 = 14 = 36 = 57

3 = 15 = 26 = 47

4 = 12 = 37 = 56

5 = 13 = 27 = 46

6 = 17 = 23 = 45

7 = 16 = 25 = 34

*Signs in every column of original design matrix reversed for
mirror-image foldover design*
The chosen design used a set of generators with all positive signs.
The mirror-image foldover design uses generators with negative signs for
terms with an even number of factors or, 4 = -12, 5 = -13, 6 = -23 and
7 = 123.  This generates a design matrix that is equal to the original
design matrix with every sign in every column reversed.

If we augment the initial 8 runs with the 8 mirror-image foldover design
runs (with all column signs reversed), we can de-alias all the main
effect estimates from the 2-way interactions. The additional runs are:

*Design matrix for mirror-image foldover runs*

**Design Matrix for the Mirror-Image Foldover Runs of the

   27-3 Fractional Factorial**

| run | $X_1$ | $X_2$ | $X_3$ | $X_4$ = $X_1$$X_2$ | $X_5$ = $X_1$$X_3$ | $X_6$ = $X_2$$X_3$ | $X_7$ = |
| --- | --- | --- | --- | --- | --- | --- | --- |
| run | $X_1$ | $X_2$ | $X_3$ | $X_4$ = $X_1$$X_2$ | $X_5$ = $X_1$$X_3$ | $X_6$ = $X_2$$X_3$ | $X_7$ = |

      $X_1$$X_2$$X_3$

| 1 | +1 | +1 | +1 | -1 | -1 | -1 | +1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | -1 | +1 | +1 | +1 | +1 | -1 | -1 |
| 3 | +1 | -1 | +1 | +1 | -1 | +1 | -1 |
| 4 | -1 | -1 | +1 | -1 | +1 | +1 | +1 |
| 5 | +1 | +1 | -1 | -1 | +1 | +1 | -1 |
| 6 | -1 | +1 | -1 | +1 | -1 | +1 | +1 |
| 7 | +1 | -1 | -1 | +1 | +1 | -1 | +1 |
| 8 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
*Alias structure for augmented runs*

Following the same steps as before and making the same assumptions about

the omission of higher-order interactions in the alias structure, we
arrive at:

1 = -24 = -35 = -67

2 = -14 = -36 =- 57

3 = -15 = -26 = -47

4 = -12 = -37 = -56

5 = -13 = -27 = -46

6 = -17 = -23 = -45

7 = -16 = -25 = -34

With both sets of runs, we can now estimate all the main effects free
from two factor interactions.

*Build a resolution IV design from a resolution III design*
**Note***: In general, a mirror-image foldover design is a method
to build a resolution IV design from a resolution III design. It is never
used to follow-up a resolution IV design*.
