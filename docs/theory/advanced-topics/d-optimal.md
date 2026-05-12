# D-Optimal Designs

*D-optimal designs are often used when [classical designs do not apply](when-classical-fail.md)*

D-optimal designs are one form of design provided by a computer algorithm. These types of computer-aided designs are particularly useful when classical designs do not apply.

Unlike standard classical designs such as factorials and fractional factorials, D-optimal design matrices are usually not orthogonal and effect estimates are correlated.

These types of designs are always an option regardless of the type of model the experimenter wishes to fit (for example, first order, first order plus some interactions, full quadratic, cubic, etc.) or the objective specified for the experiment (for example, screening, response surface, etc.). D-optimal designs are straight optimizations based on a chosen optimality criterion and the model that will be fit. The optimality criterion used in generating D-optimal designs is one of maximizing $|X'X|$, the determinant of the information matrix $X'X$.

This optimality criterion results in minimizing the generalized variance of the parameter estimates for a pre-specified model. As a result, the 'optimality' of a given D-optimal design is model dependent. That is, the experimenter must specify a model for the design before a computer can generate the specific treatment combinations. Given the total number of treatment runs for an experiment and a specified model, the computer algorithm chooses the optimal set of design runs from a *candidate set* of possible design treatment runs. This candidate set of treatment runs usually consists of all possible combinations of various factor levels that one wishes to use in the experiment.

In other words, the candidate set is a collection of treatment combinations from which the D-optimal algorithm chooses the treatment combinations to include in the design. The computer algorithm generally uses a stepping and exchanging process to select the set of treatment runs.

!!! Note
    There is no guarantee that the design the computer generates is actually D-optimal.

*D-optimal designs are useful when resources are limited or there are constraints on factor settings*

The reasons for using D-optimal designs instead of standard classical designs generally fall into two categories:

- standard factorial or fractional factorial designs require too many runs for the amount of resources or time allowed for the experiment
- the design space is constrained (the process space contains factor settings that are not feasible or are impossible to run).

*Example*

Suppose an industrial process has three design variables ($k = 3$), and engineering judgment specifies the following model as an appropriate representation of the process.

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_{11} X_1^2 + \epsilon$$

The levels being considered by the researcher are (coded)

- $X_1$: 5 levels (-1, -0.5, 0, 0.5, 1)
- $X_2$: 2 levels (-1, 1)
- $X_3$: 2 levels (-1, 1)

Due to resource limitations, only $n = 12$ data points can be collected.

*Create the candidate set*

Given the experimental specifications, the first step in generating the design is to create a candidate set of points. The candidate set is a data table with a row for each point (run) to be considered for the design, often a full factorial. For our problem, the candidate set is a full factorial in all factors containing $5 \times 2 \times 2 = 20$ possible design runs.

**TABLE 5.1  Candidate Set for Variables X1, X2, X3**

| X1 | X2 | X3 |
|:---:|:---:|:---:|
| -1 | -1 | -1 |
| -1 | -1 | +1 |
| -1 | +1 | -1 |
| -1 | +1 | +1 |
| -0.5 | -1 | -1 |
| -0.5 | -1 | +1 |
| -0.5 | +1 | -1 |
| -0.5 | +1 | +1 |
| 0 | -1 | -1 |
| 0 | -1 | +1 |
| 0 | +1 | -1 |
| 0 | +1 | +1 |
| 0.5 | -1 | -1 |
| 0.5 | -1 | +1 |
| 0.5 | +1 | -1 |
| 0.5 | +1 | +1 |
| +1 | -1 | -1 |
| +1 | -1 | +1 |
| +1 | +1 | -1 |
| +1 | +1 | +1 |

*Generating a D-optimal design*

D-optimal designs maximize the D-efficiency, which is a volume criterion on the generalized variance of the parameter estimates. The D-efficiency of the standard fractional factorial is 100 %, but it is not possible to achieve 100 % D-efficiency when pure quadratic terms such as $X_1^2$ are included in the model.

The D-efficiency values are a function of the number of points in the design, the number of independent variables in the model, and the maximum standard error for prediction over the design points. The best design is the one with the highest D-efficiency. Other reported efficiencies (e.g. A, G, I) help choose an optimal design when various models produce similar D-efficiencies.

*D-optimal design*

The D-optimal design (D=0.6825575, A=2.2, G=1, I=4.6625) using 12 runs is shown in Table 5.2 in standard order. The standard error of prediction is also shown. The design runs should be randomized before the treatment combinations are executed.

**TABLE 5.2  Final D-optimal Design**

| X1 | X2 | X3 | OptStdPred |
|:---:|:---:|:---:|:---:|
| -1 | -1 | -1 | 0.645497 |
| -1 | -1 | +1 | 0.645497 |
| -1 | +1 | -1 | 0.645497 |
| -1 | +1 | +1 | 0.645497 |
| 0 | -1 | -1 | 0.645497 |
| 0 | -1 | +1 | 0.645497 |
| 0 | +1 | -1 | 0.645497 |
| 0 | +1 | +1 | 0.645497 |
| +1 | -1 | -1 | 0.645497 |
| +1 | -1 | +1 | 0.645497 |
| +1 | +1 | -1 | 0.645497 |
| +1 | +1 | +1 | 0.645497 |

!!! Note
    Software packages may have different procedures for generating D-optimal designs, so the final design may be different depending on the software package being used.
