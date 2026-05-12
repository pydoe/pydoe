# Completely Randomized Designs

*These designs are for studying the effects of one primary factor without the need to take other nuisance factors into account*

Here we consider completely randomized designs that have one primary factor. The experiment compares the values of a response variable based on the different levels of that primary factor.

For completely randomized designs, the levels of the primary factor are randomly assigned to the experimental units. By randomization, we mean that the run sequence of the experimental units is determined randomly. For example, if there are 3 levels of the primary factor with each level to be run 2 times, then there are 6 factorial possible run sequences (or 6! ways to order the experimental trials). Because of the replication, the number of unique orderings is 90 (since 90 = 6!/(2!\*2!\*2!)). An example of an unrandomized design would be to always run 2 replications for the first level, then 2 for the second level, and finally 2 for the third level. To randomize the runs, one way would be to put 6 slips of paper in a box with 2 having level 1, 2 having level 2, and 2 having level 3. Before each run, one of the slips would be drawn blindly from the box and the level selected would be used for the next run of the experiment.

*Randomization typically performed by computer software*

In practice, the randomization is typically performed by a computer program. However, the randomization can also be generated from random number tables or by some physical mechanism (e.g., drawing the slips of paper).

*Three key numbers*

All completely randomized designs with one primary factor are defined by 3 numbers:

$k$ = number of factors (= 1 for these designs)

$L$ = number of levels

$n$ = number of replications

and the total sample size (number of runs) is $N = k \times L \times n$.

*Balance*

Balance dictates that the number of replications be the same at each level of the factor (this will maximize the sensitivity of subsequent statistical $t$ (or $F$) tests).

*Typical example of a completely randomized design*

A typical example of a completely randomized design is the following:

$k$ = 1 factor ($X_1$)

$L$ = 4 levels of that single factor (called "1", "2", "3", and "4")

$n$ = 3 replications per level

$N$ = 4 levels \* 3 replications per level = 12 runs

*A sample randomized sequence of trials*

The randomized sequence of trials might look like:

| X1 |
|:---:|
| 3 |
| 1 |
| 4 |
| 2 |
| 2 |
| 1 |
| 3 |
| 4 |
| 1 |
| 2 |
| 4 |
| 3 |

Note that in this example there are 12!/(3!\*3!\*3!\*3!) = 369,600 ways to run the experiment, all equally likely to be picked by a randomization procedure.

*Model for a completely randomized design*

The model for the response is

$$Y_{i,j} = \mu + T_i + \text{random error}$$

with

$Y_{i,j}$ being any observation for which $X_1 = i$ ($i$ and $j$ denote the level of the factor and the replication within the level of the factor, respectively)

$\mu$ (or mu) is the general location parameter

$T_i$ is the effect of having treatment level $i$

**Estimates and Statistical Tests**

*Estimating and testing model factor levels*

| | |
|---|---|
| Estimate for $\mu$: | $\bar{Y}$ = the average of all the data |
| Estimate for $T_i$: | $\bar{Y}_i - \bar{Y}$, with $\bar{Y}_i$ = average of all $Y$ for which $X_1 = i$ |

Statistical tests for levels of $X_1$ are shown in the section on one-way ANOVA in Chapter 7.
