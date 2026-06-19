# Latin Square Designs

*Latin square (and related) designs are efficient designs to block
from 2 to 4 nuisance factors*
Latin square designs, and the related Graeco-Latin square and
Hyper-Graeco-Latin square designs, are a special type of comparative
design.

There is a single factor of primary interest, typically called the
treatment factor, and several nuisance factors.  For Latin square
designs there are 2 nuisance factors, for Graeco-Latin square designs
there are 3 nuisance factors, and for Hyper-Graeco-Latin square designs
there are 4 nuisance factors.

*Nuisance factors used as blocking variables*

The nuisance factors are used as blocking variables.

- For Latin square designs, the 2 nuisance factors are divided
       into a tabular grid with the property that each row and each
       column receive each treatment exactly once.

- As with the Latin square design, a Graeco-Latin square design is
       a $k \times k$ tabular grid in which $k$ is the number
       of levels of the treatment factor.  However, it uses 3 blocking
       variables instead of the 2 used by the standard Latin square
       design.

- A Hyper-Graeco-Latin square design is also a $k \times k$
       tabular grid with $k$ denoting the number of levels of the
       treatment factor.  However, it uses 4 blocking variables instead
       of the 2 used by the standard Latin square design.

*Advantages and disadvantages of Latin square designs*

The advantages of Latin square designs are:

- They handle the case when we have several nuisance factors and
       we either cannot combine them into a single factor or we
       wish to keep them separate.

- They allow experiments with a relatively small number
       of runs.

The disadvantages are:

- The number of levels of each blocking variable must
       equal the number of levels of the treatment factor.

- The Latin square model assumes that there are no interactions
       between the blocking variables or between the treatment variable
       and the blocking variable.

The randomization is more complex.

Note that Latin square designs are equivalent to specific fractional
factorial designs (e.g., the 4x4 Latin square design is equivalent to a
43-1[fractional factorial](fractional-factorial.md) design).

*Summary of designs*

Several useful designs are described in the table below.

**Some Useful Latin Square, Graeco-Latin Square and
Hyper-Graeco-Latin Square Designs**

Name of
      Design
Number of
      Factors

$k$
Number of
      Runs

      N

| 3-by-3 Latin Square | 3 | 9 |
| --- | --- | --- |
| 4-by-4 Latin Square | 3 | 16 |
| 5-by-5 Latin Square | 3 | 25 |
| 3-by-3 Graeco-Latin Square | 4 | 9 |
| 4-by-4 Graeco-Latin Square | 4 | 16 |
| 5-by-5 Graeco-Latin Square | 4 | 25 |

 Tom Ryan suggested not including this

   
      3-by-3 Hyper-Graeco-Latin Square
   </td>
   
      Does not exist
   </td>
</tr>

| 4-by-4 Hyper-Graeco-Latin Square | 5 | 16 |
| --- | --- | --- |
| 5-by-5 Hyper-Graeco-Latin Square | 5 | 25 |
| **Model for Latin Square and Related Designs** |
| *Latin square design model and estimates for effect levels* | The model for a response for a latin square design is |
| $Y_{ijk} = \mu + R_{i} + C_{j} + T_{k} + \mbox{random error}$ |

with

| Symbol | Meaning |
| --- | --- |
| $Y_{ijk}$ | any observation where $X_1 = i$, $X_2 = j$, $X_3 = k$ |
| $X_1$, $X_2$ | blocking factors |
| $X_3$ | primary factor |
| $\mu$ | general location parameter |
| $R_i$ | effect for block $i$ |
| $C_j$ | effect for block $j$ |
| $T_k$ | effect for treatment $k$ |

Models for Graeco-Latin and Hyper-Graeco-Latin squares are the obvious
extensions of the Latin square model, with additional blocking variables
added.

| **Estimates for Latin Square Designs** |
| --- | --- |

*Estimates*

| Parameter | Estimate |
| --- | --- |
| $\mu$ | $\bar{Y}$ (average of all data) |
| $R_i$ | $\bar{Y}_{i} - \bar{Y}$, where $\bar{Y}_{i}$ = average of all $Y$ for which $X_1 = i$ |
| $C_j$ | $\bar{Y}_{j} - \bar{Y}$, where $\bar{Y}_{j}$ = average of all $Y$ for which $X_2 = j$ |
| $T_k$ | $\bar{Y}_{k} - \bar{Y}$, where $\bar{Y}_{k}$ = average of all $Y$ for which $X_3 = k$ |

*Randomize as much as design allows*

Designs for Latin squares with 3-, 4-, and 5-level factors are given

next.  These designs show what the treatment combinations should be for
each run.  ***When using any of these designs, be sure to randomize
the treatment units and trial order, as much as the design
allows**.*

For example, one recommendation is that a Latin square design
be randomly selected from those available, then randomize the run
order.

| **Latin Square Designs for 3-, 4-, and 5-Level Factors** |
| --- | --- | --- |
| *Designs for 3-level factors (and 2 nuisance or blocking factors)* | **3-Level Factors** |
| $X_1$ | $X_2$ | $X_3$ |
| row |
|

      blocking

      factor
column
      blocking

      factor
treatment
      factor

| 1 | 1 | 1 |
| --- | --- | --- |
| 1 | 2 | 2 |
| 1 | 3 | 3 |
| 2 | 1 | 3 |
| 2 | 2 | 1 |
| 2 | 3 | 2 |
| 3 | 1 | 2 |
| 3 | 2 | 3 |
| 3 | 3 | 1 |

with

$k$ = 3 factors (2 blocking factors and 1 primary factor)

$L_1$ = 3 levels of factor $X_1$ (block)

$L_2$ = 3 levels of factor $X_2$ (block)

$L_3$ = 3 levels of factor $X_3$
   (primary)

$N$ = $L_1$ * $L_2$ = 9 runs

This can alternatively be represented as

| A | B | C |
| --- | --- | --- |
| C | A | B |
| B | C | A |
| *Designs for 4-level factors (and 2 nuisance or blocking factors)* | **4-Level Factors** |
| $X_1$ | $X_2$ | $X_3$ |
| row |
|

      blocking

      factor
column
      blocking

      factor
treatment
      factor

| 1 | 1 | 1 |
| --- | --- | --- |
| 1 | 2 | 2 |
| 1 | 3 | 4 |
| 1 | 4 | 3 |
| 2 | 1 | 4 |
| 2 | 2 | 3 |
| 2 | 3 | 1 |
| 2 | 4 | 2 |
| 3 | 1 | 2 |
| 3 | 2 | 4 |
| 3 | 3 | 3 |
| 3 | 4 | 1 |
| 4 | 1 | 3 |
| 4 | 2 | 1 |
| 4 | 3 | 2 |
| 4 | 4 | 4 |

with

$k$ = 3 factors (2 blocking factors and 1 primary factor)

$L_1$ = 4 levels of factor $X_1$ (block)

$L_2$ = 4 levels of factor $X_2$ (block)

$L_3$ = 4 levels of factor $X_3$
   (primary)

$N$ = $L_1$ * $L_2$ = 16 runs

This can alternatively be represented as

| A | B | D | C |
| --- | --- | --- | --- |
| D | C | A | B |
| B | D | C | A |
| C | A | B | D |
| *Designs for 5-level factors (and 2 nuisance or blocking factors)* | **5-Level Factors** |
| $X_1$ | $X_2$ | $X_3$ |
| row |

      blocking

      factor
column
      blocking

      factor
treatment
      factor

| 1 | 1 | 1 |
| --- | --- | --- |
| 1 | 2 | 2 |
| 1 | 3 | 3 |
| 1 | 4 | 4 |
| 1 | 5 | 5 |
| 2 | 1 | 3 |
| 2 | 2 | 4 |
| 2 | 3 | 5 |
| 2 | 4 | 1 |
| 2 | 5 | 2 |
| 3 | 1 | 5 |
| 3 | 2 | 1 |
| 3 | 3 | 2 |
| 3 | 4 | 3 |
| 3 | 5 | 4 |
| 4 | 1 | 2 |
| 4 | 2 | 3 |
| 4 | 3 | 4 |
| 4 | 4 | 5 |
| 4 | 5 | 1 |
| 5 | 1 | 4 |
| 5 | 2 | 5 |
| 5 | 3 | 1 |
| 5 | 4 | 2 |
| 5 | 5 | 3 |

with

$k$ = 3 factors (2 blocking factors and 1 primary factor)

$L_1$ = 5 levels of factor $X_1$ (block)

$L_2$ = 5 levels of factor $X_2$ (block)

$L_3$ = 5 levels of factor $X_3$
   (primary)

$N$ = $L_1$ * $L_2$ = 25 runs

This can alternatively be represented as

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| C | D | E | A | B |
| E | A | B | C | D |
| B | C | D | E | A |
| D | E | A | B | C |
| *Further information* | More details on Latin square designs can be found in Box, Hunter, and |

Hunter ([1978](../references/index.md)).
