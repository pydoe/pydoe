# An EDA Approach to Experiment Design

*Introduction*
This section presents an
exploratory data analysis (EDA)
approach to analyzing the data from a designed experiment.  This
material is meant to complement, not replace, the more model-based
approach for analyzing experiment designs given in
[section 4 of this chapter](../analysis-doe/index.md).

Choosing an appropriate design is discussed in detail in
[section 3 of this chapter](../choosing-design/select-design.md).

**Starting point**

*Problem category*
The problem category we will address is the screening problem.
Two characteristics of screening problems are:

- There are many factors to consider.
   - Each of these factors may be either continuous or
       discrete.

*Desired output*
The desired output from the analysis of a screening problem is:

- A ranked list (by order of importance) of factors.
   - The best settings for each of the factors.
   - A good model.
   - Insight.

*Problem essentials*
The essentials of the screening problem are:

- There are $k$ factors with $n$ observations.
   - The generic model is:

$Y = f(X_1, X_2, \ldots, X_k) + \varepsilon$

*Design type*
In particular, the EDA approach is applied to $2^k$
[full factorial](../choosing-design/full-factorial.md) and
$2^{k-p}$
[fractional factorial](../choosing-design/fractional-factorial.md) designs.

An EDA approach is particularly applicable to screening designs
because we are in the preliminary stages of understanding our
process.

*EDA philosophy*
EDA is not a single technique.  It is an approach to analyzing
data.

- EDA is data-driven.  That is, we do not assume an initial
       model.  Rather, we attempt to let the data speak for
       themselves.

- EDA is question-based.  That is, we select a technique
       to answer one or more questions.

- EDA utilizes multiple techniques rather than depending on a
       single technique.  Different plots have a different basis,
       focus, and sensitivities, and therefore may bring out different
       aspects of the data.  When multiple
       techniques give us a redundancy of conclusions, this increases
       our confidence that our conclusions are valid.  When they give
       conflicting conclusions, this may be giving us a clue as
       to the nature of our data.

- EDA tools are often graphical.  The primary objective is
       to provide insight into the data, which graphical
       techniques often provide more readily than quantitative
       techniques.

*10-Step process*
The following is a 10-step EDA process for analyzing the data
from $2^k$ full factorial and $2^{k-p}$ fractional factorial designs.

- [Ordered data plot](eda-ordered-data-plot.md)
- [DOE scatter plot](eda-scatter-plot.md)
- [DOE mean plot](eda-mean-plot.md)
- [Interaction effects matrix plot](eda-interaction-plot.md)
- [Block plot](eda-block-plot.md)
- [DOE Youden plot](eda-youden-plot.md)
- [|Effects| plot](eda-effects-plot.md)
- [Half-normal probability plot](eda-half-normal-plot.md)
- [Cumulative residual standard
       deviation plot](eda-cumulative-ressd-plot.md)
- [DOE contour plot](eda-contour-plot.md)

Each of these plots will be presented with the following format:

- Purpose of the plot
   - Output of the plot
   - Definition of the plot
   - Motivation for the plot
   - An example of the plot using the defective springs data
   - A discussion of how to interpret the plot
   - Conclusions we can draw from the plot for the defective springs
       data

**Data set**

*Defective springs data*
The plots presented in this section are demonstrated with
a data set from
[Box and Bisgaard (1987)](../references/index.md).

These data are from a 23 full factorial data set that
contains the following variables:

- Response variable $Y$ = percentage of springs without
       cracks
   - Factor 1 = oven temperature (2 levels: 1450 and 1600 F)
   - Factor 2 = carbon concentration (2 levels: 0.5% and 0.7%)
   - Factor 3 = quench temperature (2 levels: 70 and 120 F)

     Y         X1              X2            X3
  Percent     Oven           Carbon        Quench
Acceptable  Temperature  Concentration   Temperature
----------------------------------------------------
    67         -1              -1            -1
    79         +1              -1            -1
    61         -1              +1            -1
    75         +1              +1            -1
    59         -1              -1            +1
    90         +1              -1            +1
    52         -1              +1            +1
    87         +1              +1            +1

(The reader can download the data as a
text file.)
