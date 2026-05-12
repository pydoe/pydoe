# Single Response Case

*Optimizing of a single response usually starts with line searches in the direction of maximum improvement*

The experimental optimization of a single response is usually conducted in two phases or steps, following the advice of Box and Wilson. The first phase consists of a sequence of line searches in the direction of maximum improvement. Each search in the sequence is continued until there is evidence that the direction chosen does not result in further improvements. The sequence of line searches is performed as long as there is no evidence of lack of fit for a simple first-order model of the form

$$\hat{Y} = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k$$

*If there is lack of fit for linear models, quadratic models are tried next*

The second phase is performed when there is lack of linear fit in Phase I, and instead, a second-order or quadratic polynomial regression model of the general form

$$\begin{aligned}
\hat{Y} = & \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k + \\
          & \beta_{11} X_1^2 + \beta_{22} X_2^2 + \cdots + \beta_{kk} X_k^2 + \\
          & \beta_{12} X_1 X_2 + \beta_{13} X_1 X_3 + \cdots + \beta_{1k} X_1 X_k + \\
          & \beta_{23} X_2 X_3 + \cdots + \beta_{2k} X_2 X_k + \cdots + \beta_{k-1,k} X_{k-1} X_k
\end{aligned}$$

is fit. Not all responses will require quadratic fit, and in such cases Phase I is stopped when the response of interest cannot be improved any further. Each phase is explained and illustrated in the next few sections.

*"Flowchart" for two phases of experimental optimization*

The following is a flow chart showing the two phases of experimental optimization.

![Flowchart for two phases of experimental optimization](https://www.itl.nist.gov/div898/handbook/pri/section5/gifs/img9a.gif){ loading=lazy }
/// caption
**FIGURE 5.1: The Two Phases of Experimental Optimization**
///
