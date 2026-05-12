# Three-Level, Mixed Level and Fractional Factorial Designs

*Mixed level designs have some factors with, say, 2 levels, and some with 3 levels or 4 levels*

The $2^k$ and $3^k$ experiments are special cases of factorial designs. In a factorial design, one obtains data at every combination of the levels. The importance of factorial designs, especially 2-level factorial designs, was stated by Montgomery (1991): *It is our belief that the two-level factorial and fractional factorial designs should be the cornerstone of industrial experimentation for product and process development and improvement.* He went on to say: *There are, however, some situations in which it is necessary to include a factor (or a few factors) that have more than two levels.*

This section will look at how to add three-level factors starting with two-level designs, obtaining what is called a *mixed-level* design. We will also look at how to add a four-level factor to a two-level design. The section will conclude with a listing of some useful orthogonal three-level and mixed-level designs (a few of the so-called Taguchi "L" orthogonal array designs), and a brief discussion of their benefits and disadvantages.

## Generating a Mixed Three-Level and Two-Level Design

*Montgomery scheme for generating a mixed design*

Montgomery (1991) suggests how to derive a variable at three levels from a $2^3$ design, using a rather ingenious scheme. The objective is to generate a design for one variable, $A$, at 2 levels and another, $X$, at three levels. This will be formed by combining the -1 and 1 patterns for the $B$ and $C$ factors to form the levels of the three-level factor $X$:

**TABLE 3.38: Generating a Mixed Design**

| Two-Level | | Three-Level |
|:---:|:---:|:---:|
| B | C | X |
| -1 | -1 | $x_1$ |
| +1 | -1 | $x_2$ |
| -1 | +1 | $x_2$ |
| +1 | +1 | $x_3$ |

Similar to the $3^k$ case, we observe that $X$ has 2 degrees of freedom, which can be broken out into a linear and a quadratic component. To illustrate how the $2^3$ design leads to the design with one factor at two levels and one factor at three levels, consider the following table, with particular attention focused on the column labels.

*Table illustrating the generation of a design with one factor at 2 levels and another at 3 levels from a $2^3$ design*

| | A | XL | XL | AXL | AXL | XQ | AXQ | TRT | MNT |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Run | A | B | C | AB | AC | BC | ABC | A | X |
| 1 | -1 | -1 | -1 | +1 | +1 | +1 | -1 | Low | Low |
| 2 | +1 | -1 | -1 | -1 | -1 | +1 | +1 | High | Low |
| 3 | -1 | +1 | -1 | -1 | +1 | -1 | +1 | Low | Medium |
| 4 | +1 | +1 | -1 | +1 | -1 | -1 | -1 | High | Medium |
| 5 | -1 | -1 | +1 | +1 | -1 | -1 | +1 | Low | Medium |
| 6 | +1 | -1 | +1 | -1 | +1 | -1 | -1 | High | Medium |
| 7 | -1 | +1 | +1 | -1 | -1 | +1 | -1 | Low | High |
| 8 | +1 | +1 | +1 | +1 | +1 | +1 | +1 | High | High |

*If quadratic effect negligible, we may include a second two-level factor*

If we believe that the quadratic effect is negligible, we may include a second two-level factor, D, with D = ABC. In fact, we can convert the design to exclusively a main effect (resolution III) situation consisting of four two-level factors and one three-level factor. This is accomplished by equating the second two-level factor to AB, the third to AC and the fourth to ABC. Column BC cannot be used in this manner because it contains the quadratic effect of the three-level factor X.

## More Than One Three-Level Factor

*3-Level factors from $2^4$ and $2^5$ designs*

We have seen that in order to create one three-level factor, the starting design can be a $2^3$ factorial. Without proof we state that a $2^4$ can split off 1, 2 or 3 three-level factors; a $2^5$ is able to generate 3 three-level factors and still maintain a full factorial structure. For more on this, see Montgomery (1991).

## Generating a Two- and Four-Level Mixed Design

*Constructing a design with one 4-level factor and two 2-level factors*

We may use the same principles as for the three-level factor example in creating a four-level factor. We will assume that the goal is to construct a design with one four-level and two two-level factors.

Initially we wish to estimate all main effects and interactions. It has been shown (see Montgomery, 1991) that this can be accomplished via a $2^4$ (16 runs) design, with columns A and B used to create the four level factor $X$.

*Table showing design with 4-level, two 2-level factors in 16 runs*

**TABLE 3.39: A Single Four-level Factor and Two Two-level Factors in 16 runs**

| Run | (A | B) | = X | C | D |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | -1 | -1 | $x_1$ | -1 | -1 |
| 2 | +1 | -1 | $x_2$ | -1 | -1 |
| 3 | -1 | +1 | $x_3$ | -1 | -1 |
| 4 | +1 | +1 | $x_4$ | -1 | -1 |
| 5 | -1 | -1 | $x_1$ | +1 | -1 |
| 6 | +1 | -1 | $x_2$ | +1 | -1 |
| 7 | -1 | +1 | $x_3$ | +1 | -1 |
| 8 | +1 | +1 | $x_4$ | +1 | -1 |
| 9 | -1 | -1 | $x_1$ | -1 | +1 |
| 10 | +1 | -1 | $x_2$ | -1 | +1 |
| 11 | -1 | +1 | $x_3$ | -1 | +1 |
| 12 | +1 | +1 | $x_4$ | -1 | +1 |
| 13 | -1 | -1 | $x_1$ | +1 | +1 |
| 14 | +1 | -1 | $x_2$ | +1 | +1 |
| 15 | -1 | +1 | $x_3$ | +1 | +1 |
| 16 | +1 | +1 | $x_4$ | +1 | +1 |

The "+" and "-" are substituted for +1 and -1, to conserve space on the page.

## Some Useful (Taguchi) Orthogonal "L" Array Designs

**L9 — A $3^{4-2}$ Fractional Factorial Design: 4 Factors at Three Levels (9 runs)**

| Run | X1 | X2 | X3 | X4 |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 2 |
| 3 | 1 | 3 | 3 | 3 |
| 4 | 2 | 1 | 2 | 3 |
| 5 | 2 | 2 | 3 | 1 |
| 6 | 2 | 3 | 1 | 2 |
| 7 | 3 | 1 | 3 | 2 |
| 8 | 3 | 2 | 1 | 3 |
| 9 | 3 | 3 | 2 | 1 |

**L18 — A $2 \times 3^{7-5}$ Fractional Factorial (Mixed-Level) Design: 1 Factor at Two Levels and Seven Factors at 3 Levels (18 Runs)**

| Run | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | 1 | 1 | 3 | 3 | 3 | 3 | 3 | 3 |
| 4 | 1 | 2 | 1 | 1 | 2 | 2 | 3 | 3 |
| 5 | 1 | 2 | 2 | 2 | 3 | 3 | 1 | 1 |
| 6 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 |
| 7 | 1 | 3 | 1 | 2 | 1 | 3 | 2 | 3 |
| 8 | 1 | 3 | 2 | 3 | 2 | 1 | 3 | 1 |
| 9 | 1 | 3 | 3 | 1 | 3 | 2 | 1 | 2 |
| 10 | 2 | 1 | 1 | 3 | 3 | 2 | 2 | 1 |
| 11 | 2 | 1 | 2 | 1 | 1 | 3 | 3 | 2 |
| 12 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 3 |
| 13 | 2 | 2 | 1 | 2 | 3 | 1 | 3 | 2 |
| 14 | 2 | 2 | 2 | 3 | 1 | 2 | 1 | 3 |
| 15 | 2 | 2 | 3 | 1 | 2 | 3 | 2 | 1 |
| 16 | 2 | 3 | 1 | 3 | 2 | 3 | 1 | 2 |
| 17 | 2 | 3 | 2 | 1 | 3 | 1 | 2 | 3 |
| 18 | 2 | 3 | 3 | 2 | 1 | 2 | 3 | 1 |

## Advantages and Disadvantages of Three-Level and Mixed-Level "L" Designs

*Advantages and disadvantages of three-level mixed-level designs*

The good features of these designs are:

- They are orthogonal arrays. Some analysts believe this simplifies the analysis and interpretation of results while other analysts believe it does not.
- They obtain a lot of information about the main effects in a relatively few number of runs.
- You can test whether non-linear terms are needed in the model, at least as far as the three-level factors are concerned.

On the other hand, there are several undesirable features of these designs to consider:

- They provide limited information about interactions.
- They require more runs than a comparable $2^{k-p}$ design, and a two-level design will often suffice when the factors are continuous and monotonic (many three-level designs are used when two-level designs would have been adequate).
