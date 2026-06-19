# Constructing the Half-Fraction Design

*Construction of a $2^{3-1}$ half fraction design by starting with a $2^2$ full factorial design*

First note that, mathematically, $2^{3-1} = 2^2$. This gives us the first step, which is to start with a regular $2^2$ full factorial design. That is, we start with the following design table.

**TABLE 3.12: A Standard Order $2^2$ Full Factorial Design Table**

| $X_1$ | $X_2$ |
| --- | --- | --- |
| 1 | -1 | -1 |
| 2 | +1 | -1 |
| 3 | -1 | +1 |
| 4 | +1 | +1 |

*Assign the third factor to the interaction column of a $2^2$ design*

This design has four runs, the right number for a half-fraction of a $2^3$, but there is no column for factor $X_3$. We need to add a third column to take care of this, and we do it by adding the $X_1 X_2$ interaction column. This column is, as you will recall from full factorial designs, constructed by multiplying the row entry for $X_1$ with that of $X_2$ to obtain the row entry for $X_1 X_2$.

**TABLE 3.13: A $2^2$ Design Table Augmented with the $X_1 X_2$ Interaction Column '$X_1 X_2$'**

| $X_1$ | $X_2$ | $X_1 X_2$ |
| --- | --- | --- | --- |
| 1 | -1 | -1 | +1 |
| 2 | +1 | -1 | -1 |
| 3 | -1 | +1 | -1 |
| 4 | +1 | +1 | +1 |

*Design table with $X_3$ set to $X_1 X_2$*

We may now substitute '$X_3$' in place of '$X_1 X_2$' in this table.

**TABLE 3.14: A $2^{3-1}$ Design Table with Column $X_3$ set to $X_1 X_2$**

| $X_1$ | $X_2$ | $X_3$ |
| --- | --- | --- | --- |
| 1 | -1 | -1 | +1 |
| 2 | +1 | -1 | -1 |
| 3 | -1 | +1 | -1 |
| 4 | +1 | +1 | +1 |

*Design table with $X_3$ set to $-X_1 X_2$*

Note that the rows of Table 3.14 give the dark-shaded corners of the design in [Figure 3.4](latin-squares.md). If we had set $X_3 = -X_1 X_2$ as the rule for generating the third column of our $2^{3-1}$ design, we would have obtained:

**TABLE 3.15: A $2^{3-1}$ Design Table with Column $X_3$ set to $-X_1 X_2$**

| $X_1$ | $X_2$ | $X_3$ |
| --- | --- | --- | --- |
| 1 | -1 | -1 | -1 |
| 2 | +1 | -1 | +1 |
| 3 | -1 | +1 | +1 |
| 4 | +1 | +1 | -1 |

*Main effect estimates from fractional factorial not as good as full factorial*

This design gives the light-shaded corners of the box of [Figure 3.4.](half-fraction-design.md) Both $2^{3-1}$ designs that we have generated are equally good, and both save half the number of runs over the original $2^3$ full factorial design. If $c_1$, $c_2$, and $c_3$ are our [estimates](half-fraction-design.md) of the main effects for the factors $X_1$, $X_2$, $X_3$ (i.e., the difference in the response due to going from "low" to "high" for an effect), then the precision of the estimates $c_1$, $c_2$, and $c_3$ are not quite as good as for the full 8-run factorial because we only have four observations to construct the averages instead of eight; this is one price we have to pay for using fewer runs.

*Example*

**Example:** For the 'Pressure (P), Table speed (T), and Down force (D)' design situation of the [previous example](half-fraction-design.md), here's a replicated $2^{3-1}$ in randomized run order, with five centerpoint runs ('000') interspersed among the runs. This design table was constructed using the technique discussed above, with D = P*T.

*Design table for the example*

**TABLE 3.16: A $2^{3-1}$ Design Replicated Twice, with Five Centerpoint Runs Added**

| Pattern | P | T | D | Center Point |
| --- | --- | --- | --- | --- | --- |
| 1 | 000 | 0 | 0 | 0 | 1 |
| 2 | +-- | +1 | -1 | -1 | 0 |
| 3 | -+- | -1 | +1 | -1 | 0 |
| 4 | 000 | 0 | 0 | 0 | 1 |
| 5 | +++ | +1 | +1 | +1 | 0 |
| 6 | --+ | -1 | -1 | +1 | 0 |
| 7 | 000 | 0 | 0 | 0 | 1 |
| 8 | +-- | +1 | -1 | -1 | 0 |
| 9 | --+ | -1 | -1 | +1 | 0 |
| 10 | 000 | 0 | 0 | 0 | 1 |
| 11 | +++ | +1 | +1 | +1 | 0 |
| 12 | -+- | -1 | +1 | -1 | 0 |
| 13 | 000 | 0 | 0 | 0 | 1 |
