# How Do You Select and Scale the Process Variables?

**Guidelines to assist the engineering judgment process of selecting process variables for a DOE**

Process variables include both *inputs* and *outputs* — i.e., *factors* and *responses*. The selection of these variables is best done as a team effort. The team should

- Include all important factors (based on engineering judgment).
- Be bold, but not foolish, in choosing the low and high factor levels.
- Check the factor settings for impractical or impossible combinations — i.e., very low pressure and very high gas flows.
- Include all relevant responses.
- Avoid using only responses that combine two or more measurements of the process. For example, if interested in selectivity (the ratio of two etch rates), measure both rates, not just the ratio.

*Be careful when choosing the allowable range for each factor*

We have to choose the range of the settings for input factors, and it is wise to give this some thought beforehand rather than just try extreme values. In some cases, extreme values will give runs that are not feasible; in other cases, extreme ranges might move one out of a smooth area of the response surface into some jagged region, or close to an asymptote.

*Two-level designs have just a "high" and a "low" setting for each factor*

The most popular experimental designs are *two-level designs*. Why only two levels? There are a number of good reasons why two is the most common choice amongst engineers: one reason is that it is ideal for screening designs, simple and economical; it also gives most of the information required to go to a multilevel response surface experiment if one is needed.

*Consider adding some center points to your two-level design*

The term "two-level design" is something of a misnomer, however, as it is recommended to include some center points during the experiment (center points are located in the middle of the design 'box').

## Notation for 2-Level Designs

*Matrix notation for describing an experiment*

The standard layout for a 2-level design uses +1 and -1 notation to denote the "high level" and the "low level" respectively, for each factor. For example, the matrix below

| | Factor 1 (X1) | Factor 2 (X2) |
|---|:---:|:---:|
| Trial 1 | -1 | -1 |
| Trial 2 | +1 | -1 |
| Trial 3 | -1 | +1 |
| Trial 4 | +1 | +1 |

describes an experiment in which 4 trials (or runs) were conducted with each factor set to high or low during a run according to whether the matrix had a +1 or -1 set for the factor during that trial. If the experiment had more than 2 factors, there would be an additional column in the matrix for each additional factor.

!!! Note
    Some authors shorten the matrix notation for a two-level design by just recording the plus and minus signs, leaving out the "1's".

*Coding the data*

The use of +1 and -1 for the factor settings is called *coding* the data. This aids in the interpretation of the coefficients fit to any experimental model. *After factor settings are coded, center points have the value "0"*. Coding is described in more detail in the DOE glossary.

## The Model or Analysis Matrix

*Design matrices*

If we add an "I" column and an "X1\*X2" column to the matrix of 4 trials for a two-factor experiment described earlier, we obtain what is known as the *model or analysis matrix* for this simple experiment, which is shown below. The model matrix for a three-factor experiment is shown later in this section.

| I | X1 | X2 | X1\*X2 |
|:---:|:---:|:---:|:---:|
| +1 | -1 | -1 | +1 |
| +1 | +1 | -1 | -1 |
| +1 | -1 | +1 | -1 |
| +1 | +1 | +1 | +1 |

*Model for the experiment*

The model for this experiment is

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_{12} X_1 X_2 + \text{experimental error}$$

and the "I" column of the design matrix has all 1's to provide for the $\beta_0$ term. The $X_1 \cdot X_2$ column is formed by multiplying the "$X_1$" and "$X_2$" columns together, row element by row element. This column gives the interaction term for each trial.

*Model in matrix notation*

In matrix notation, we can summarize this experiment by

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \text{experimental error}$$

for which $\mathbf{X}$ is the 4 by 4 design matrix of 1's and -1's shown above, $\boldsymbol{\beta}$ is the vector of unknown model coefficients $(\beta_0, \beta_1, \beta_2, \beta_{12})$ and $\mathbf{Y}$ is a vector consisting of the four trial response observations.

## Orthogonal Property of Scaling in a 2-Factor Experiment

*Coding produces orthogonal columns*

Coding is sometimes called "*orthogonal coding*" since all the columns of a coded 2-factor design matrix (except the "I" column) are typically orthogonal. That is, the dot product for any pair of columns is zero. For example, for $X_1$ and $X_2$:

$$(-1)(-1) + (+1)(-1) + (-1)(+1) + (+1)(+1) = 0$$
