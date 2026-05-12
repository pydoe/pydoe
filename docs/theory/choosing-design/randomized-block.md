# Randomized Block Designs

*Blocking to "remove" the effect of nuisance factors*

For randomized block designs, there is one factor or variable that is of primary interest. However, there are also several other nuisance factors.

Nuisance factors are those that may affect the measured result, but are not of primary interest. For example, in applying a treatment, nuisance factors might be the specific operator who prepared the treatment, the time of day the experiment was run, and the room temperature. All experiments have nuisance factors. The experimenter will typically need to spend some time deciding which nuisance factors are important enough to keep track of or control, if possible, during the experiment.

*Blocking used for nuisance factors that can be controlled*

When we can control nuisance factors, an important technique known as blocking can be used to reduce or eliminate the contribution to experimental error contributed by nuisance factors. The basic concept is to create homogeneous blocks in which the nuisance factors are held constant and the factor of interest is allowed to vary. Within blocks, it is possible to assess the effect of different levels of the factor of interest without having to worry about variations due to changes of the block factors, which are accounted for in the analysis.

*Definition of blocking factors*

*A nuisance factor is used as a blocking factor if every level of the primary factor occurs the same number of times with each level of the nuisance factor.* The analysis of the experiment will focus on the effect of varying levels of the primary factor within each block of the experiment.

*Block for a few of the most important nuisance factors*

The general rule is:

*"Block what you can, randomize what you cannot."*

Blocking is used to remove the effects of a few of the most important nuisance variables. Randomization is then used to reduce the contaminating effects of the remaining nuisance variables.

*Table of randomized block designs*

One useful way to look at a randomized block experiment is to consider it as a collection of completely randomized experiments, each run within one of the blocks of the total experiment.

**Randomized Block Designs (RBD)**

| Name of Design | Number of Factors $k$ | Number of Runs $n$ |
|---|:---:|:---:|
| 2-factor RBD | 2 | $L_1 \times L_2$ |
| 3-factor RBD | 3 | $L_1 \times L_2 \times L_3$ |
| 4-factor RBD | 4 | $L_1 \times L_2 \times L_3 \times L_4$ |
| $k$-factor RBD | $k$ | $L_1 \times L_2 \times \cdots \times L_k$ |

with $L_1$ = number of levels (settings) of factor 1, $L_2$ = number of levels (settings) of factor 2, ..., $L_k$ = number of levels (settings) of factor $k$.

**Example of a Randomized Block Design**

*Example of a randomized block design*

Suppose engineers at a semiconductor manufacturing facility want to test whether different wafer implant material dosages have a significant effect on resistivity measurements after a diffusion process taking place in a furnace. They have four different dosages they want to try and enough experimental wafers from the same lot to run three wafers at each of the dosages.

*Furnace run is a nuisance factor*

The nuisance factor they are concerned with is "furnace run" since it is known that each furnace run differs from the last and impacts many process parameters.

*Ideal would be to eliminate nuisance furnace factor*

An ideal way to run this experiment would be to run all the 4x3=12 wafers in the same furnace run. That would eliminate the nuisance furnace factor completely. However, regular production wafers have furnace priority, and only a few experimental wafers are allowed into any furnace run at the same time.

*Non-Blocked method*

A non-blocked way to run this experiment would be to run each of the twelve experimental wafers, in random order, one per furnace run. That would increase the experimental error of each resistivity measurement by the run-to-run furnace variability and make it more difficult to study the effects of the different dosages. The blocked way to run this experiment, assuming you can convince manufacturing to let you put four experimental wafers in a furnace run, would be to put four wafers with different dosages in each of three furnace runs. The only randomization would be choosing which of the three wafers with dosage 1 would go into furnace run 1, and similarly for the wafers with dosages 2, 3 and 4.

*Description of the experiment*

Let $X_1$ be dosage "level" and $X_2$ be the blocking factor furnace run. Then the experiment can be described as follows:

$k$ = 2 factors (1 primary factor $X_1$ and 1 blocking factor $X_2$)

$L_1$ = 4 levels of factor $X_1$

$L_2$ = 3 levels of factor $X_2$

$n$ = 1 replication per cell

$N = L_1 \times L_2 = 4 \times 3 = 12$ runs

*Design trial before randomization*

Before randomization, the design trials look like:

| $X_1$ | $X_2$ |
|:---:|:---:|
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 2 | 2 |
| 2 | 3 |
| 3 | 1 |
| 3 | 2 |
| 3 | 3 |
| 4 | 1 |
| 4 | 2 |
| 4 | 3 |

*Matrix representation*

An alternate way of summarizing the design trials would be to use a 4 by 3 matrix whose 4 rows are the levels of the treatment $X_1$ and whose columns are the 3 levels of the blocking variable $X_2$. The cells in the matrix have indices that match the $X_1$, $X_2$ combinations above.

By extension, note that the trials for any $K$-factor randomized block design are simply the cell indices of a $K$ dimensional matrix.

**Model for a Randomized Block Design**

*Model for a randomized block design*

The model for a randomized block design with one nuisance variable is

$$Y_{i,j} = \mu + T_i + B_j + \text{random error}$$

where

| Symbol | Definition |
|---|---|
| $Y_{i,j}$ | is any observation for which $X_1 = i$ and $X_2 = j$ |
| $X_1$ | is the primary factor |
| $X_2$ | is the blocking factor |
| $\mu$ | is the general location parameter (i.e., the mean) |
| $T_i$ | is the effect for being in treatment $i$ (of factor $X_1$) |
| $B_j$ | is the effect for being in block $j$ (of factor $X_2$) |

**Estimates for a Randomized Block Design**

*Estimating factor effects for a randomized block design*

| | |
|---|---|
| Estimate for $\mu$: | $\bar{Y}$ = the average of all the data |
| Estimate for $T_i$: | $\bar{Y}_i - \bar{Y}$, with $\bar{Y}_i$ = average of all $Y$ for which $X_1 = i$ |
| Estimate for $B_j$: | $\bar{Y}_j - \bar{Y}$, with $\bar{Y}_j$ = average of all $Y$ for which $X_2 = j$ |
