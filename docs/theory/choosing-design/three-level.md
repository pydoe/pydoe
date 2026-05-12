# Three-Level Full Factorial Designs

*Three-level designs are useful for investigating quadratic effects*

The three-level design is written as a $3^k$ factorial design. It means that $k$ factors are considered, each at 3 levels. These are (usually) referred to as low, intermediate and high levels. These levels are numerically expressed as 0, 1, and 2. One could have considered the digits -1, 0, and +1, but this may be confusing with respect to the 2-level designs since 0 is reserved for center points. Therefore, we will use the 0, 1, 2 scheme. The reason that the three-level designs were proposed is to model possible curvature in the response function and to handle the case of nominal factors at 3 levels. A third level for a continuous factor facilitates investigation of a quadratic relationship between the response and each of the factors.

*Three-level design may require prohibitive number of runs*

Unfortunately, the three-level design is prohibitive in terms of the number of runs, and thus in terms of cost and effort. For example a two-level design with center points is much less expensive while it still is a very good (and simple) way to establish the presence or absence of curvature.

## The $3^2$ Design

*The simplest 3-level design — with only 2 factors*

This is the simplest three-level design. It has two factors, each at three levels. The 9 treatment combinations for this type of design can be shown pictorially as follows:

**FIGURE 3.23: A $3^2$ Design Schematic**

![Pictorial representation of a 2-factor 3-level design](https://www.itl.nist.gov/div898/handbook/pri/section3/gifs/fig323.gif){ loading=lazy }

A notation such as "20" means that factor A is at its high level (2) and factor B is at its low level (0).

## The $3^3$ Design

*The model and treatment runs for a 3 factor, 3-level design*

This is a design that consists of three factors, each at three levels. It can be expressed as a $3 \times 3 \times 3 = 3^3$ design. The model for such an experiment is

$$Y_{ijk} = \mu + A_i + B_j + AB_{ij} + C_k + AC_{ik} + BC_{jk} + ABC_{ijk} + \epsilon_{ijk}$$

where each factor is included as a nominal factor rather than as a continuous variable. In such cases, main effects have 2 degrees of freedom, two-factor interactions have $2^2 = 4$ degrees of freedom and $k$-factor interactions have $2^k$ degrees of freedom. The model contains $2 + 2 + 2 + 4 + 4 + 4 + 8 = 26$ degrees of freedom. Note that if there is no replication, the fit is exact and there is no error term (the epsilon term) in the model. In this no replication case, if one assumes that there are no three-factor interactions, then one can use these 8 degrees of freedom for error estimation.

In this model we see that $i = 1, 2, 3$, and similarly for $j$ and $k$, making 27 treatments.

*Table of treatments for the $3^3$ design*

These treatments may be displayed as follows:

**TABLE 3.37: The $3^3$ Design**

| | | Factor A | | |
|---|---|:---:|:---:|:---:|
| **Factor B** | **Factor C** | **0** | **1** | **2** |
| 0 | 0 | 000 | 100 | 200 |
| 0 | 1 | 001 | 101 | 201 |
| 0 | 2 | 002 | 102 | 202 |
| 1 | 0 | 010 | 110 | 210 |
| 1 | 1 | 011 | 111 | 211 |
| 1 | 2 | 012 | 112 | 212 |
| 2 | 0 | 020 | 120 | 220 |
| 2 | 1 | 021 | 121 | 221 |
| 2 | 2 | 022 | 122 | 222 |

*Pictorial representation of the $3^3$ design*

**FIGURE 3.24  A $3^3$ Design Schematic**

![Pictorial representation of the 3^3 design](https://www.itl.nist.gov/div898/handbook/pri/section3/gifs/level33j.gif){ loading=lazy }

*Two types of $3^k$ designs*

Two types of fractions of $3^k$ designs are employed:

- Box-Behnken designs whose purpose is to estimate a second-order model for quantitative factors (discussed earlier in [Box-Behnken Designs](box-behnken.md))
- $3^{k-p}$ orthogonal arrays.
