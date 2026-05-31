# A 2^(3-1) Half-Fraction Design

*We can run a fraction of a full factorial experiment and still be able to estimate main effects*

Consider the two-level, full factorial design for three factors, namely the $2^3$ design. This implies eight runs (not counting replications or center points). Graphically, as shown [earlier](completely-randomized.md), we can represent the $2^3$ design by the following cube:

![Cube diagram representing a 2^3 full factorial design](https://www.itl.nist.gov/div898/handbook/pri/section3/gifs/arnonf1.gif)
/// caption
**FIGURE 3.4:** A $2^3$ Full Factorial Design; Factors $X_1$, $X_2$, $X_3$. (The arrows show the direction of increase of the factors. Numbers '1' through '8' at the corners of the design cube reference the 'Standard Order' of runs)
///

*Tabular representation of the design*

In tabular form, this design (also showing eight observations $y_j$ ($j$ = 1,...,8)) is given by:

**TABLE 3.11: A $2^3$ Two-level, Full Factorial Design Table Showing Runs in 'Standard Order,' Plus Observations ($y_j$)**

| $X_1$ | $X_2$ | $X_3$ | $Y$ |
| --- | --- | --- | --- | --- |
| 1 | -1 | -1 | -1 | $y_1 = 33$ |
| 2 | +1 | -1 | -1 | $y_2 = 63$ |
| 3 | -1 | +1 | -1 | $y_3 = 41$ |
| 4 | +1 | +1 | -1 | $Y_4 = 57$ |
| 5 | -1 | -1 | +1 | $y_5 = 57$ |
| 6 | +1 | -1 | +1 | $y_6 = 51$ |
| 7 | -1 | +1 | +1 | $y_7 = 59$ |
| 8 | +1 | +1 | +1 | $y_8 = 53$ |

*Responses in standard order*

The right-most column of the table lists '$y_1$' through '$y_8$' to indicate the responses measured for the experimental runs when listed in standard order. For example, '$y_1$' is the response (i.e., output) observed when the three factors were all run at their 'low' setting. The numbers entered in the '$y$' column will be used to illustrate calculations of effects.

*Computing $X_1$ main effect*

From the entries in the table we are able to compute all 'effects' such as main effects, first-order 'interaction' effects, etc. For example, to compute the main effect estimate '$c_1$' of factor $X_1$, we compute the average response at all runs with $X_1$ at the 'high' setting, namely (1/4)($y_2$ + $y_4$ + $y_6$ + $y_8$), minus the average response of all runs with $X_1$ set at 'low,' namely (1/4)($y_1$ + $y_3$ + $y_5$ + $y_7$). That is,

$$c_1 = \frac{1}{4}(y_2 + y_4 + y_6 + y_8) - \frac{1}{4}(y_1 + y_3 + y_5 + y_7)$$

$$= \frac{1}{4}(63 + 57 + 51 + 53) - \frac{1}{4}(33 + 41 + 57 + 59) = 8.5$$

*Can we estimate $X_1$ main effect with four runs?*

Suppose, however, that we only have enough resources to do four runs. Is it still possible to estimate the main effect for $X_1$? Or any other main effect? The answer is yes, and there are even different choices of the four runs that will accomplish this.

*Example of computing the main effects using only four runs*

For example, suppose we select only the four light (unshaded) corners of the design cube. Using these four runs (1, 4, 6 and 7), we can still compute $c_1$ as follows:

$$c_1 = \frac{1}{2}(y_4 + y_6) - \frac{1}{2}(y_1 + y_7) = \frac{1}{2}(57 + 51) - \frac{1}{2}(33 + 59) = 8$$

Similarly, we would compute $c_2$, the effect due to $X_2$, as

$$c_2 = \frac{1}{2}(y_4 + y_7) - \frac{1}{2}(y_1 + y_6) = \frac{1}{2}(57 + 59) - \frac{1}{2}(33 + 51) = 16$$

Finally, the computation of $c_3$ for the effect due to $X_3$ would be

$$c_3 = \frac{1}{2}(y_6 + y_7) - \frac{1}{2}(y_1 + y_4) = \frac{1}{2}(51 + 59) - \frac{1}{2}(33 + 57) = 10$$

*Alternative runs for computing main effects*

We could also have used the four dark (shaded) corners of the design cube for our runs and obtained similar, but slightly different, estimates for the main effects. In either case, we would have used half the number of runs that the full factorial requires. *The half fraction we used is a new design written as $2^{3-1}$*. Note that $2^{3-1} = 2^3/2 = 2^2 = 4$, which is the number of runs in this half-fraction design. In the next [section](constructing-half-fraction.md), a general method for choosing fractions that "work" will be discussed.

*Example of how fractional factorial experiments often arise in industry*

**Example**: An engineering experiment calls for running three factors, namely Pressure, Table speed, and Down force, each at a 'high' and a 'low' setting, on a production tool to determine which has the greatest effect on product uniformity. Interaction effects are considered negligible, but uniformity measurement error requires that at least two separate runs (replications) be made at each process setting. In addition, several 'standard setting' runs (centerpoint runs) need to be made at regular intervals during the experiment to monitor for process drift. As experimental time and material are limited, no more than 15 runs can be planned.

A full factorial $2^3$ design, replicated twice, calls for 8×2 = 16 runs, even without centerpoint runs, so this is not an option. However a $2^{3-1}$ design replicated twice requires only 4×2 = 8 runs, and then we would have 15-8 = 7 spare runs: 3 to 5 of these spare runs can be used for centerpoint runs and the rest saved for backup in case something goes wrong with any run. As long as we are confident that the interactions are negligibly small (compared to the main effects), and as long as complete replication is required, then the above replicated $2^{3-1}$ fractional factorial design (with center points) is a very reasonable choice.

On the other hand, if interactions are potentially large (and if the replication required could be set aside), then the usual $2^3$ full factorial design (with center points) would serve as a good design.
