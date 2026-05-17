# How Do You Optimize a Process?

**How do you determine the optimal region to run a process?**

*Often the primary DOE goal is to find the operating conditions that maximize (or minimize) the system responses*

The optimal region to run a process is usually determined after a sequence of experiments has been conducted and a series of empirical models obtained. In many engineering and science applications, experiments are conducted and empirical models are developed with the objective of improving the responses of interest. From a mathematical point of view, the objective is to find the operating conditions (or factor levels) $X_1, X_2, \ldots, X_k$ that maximize or minimize the $r$ system response variables $Y_1, Y_2, \ldots, Y_r$. In experimental optimization, different optimization techniques are applied to the *fitted* response equations $\hat{Y}_1, \hat{Y}_2, \ldots, \hat{Y}_r$. Provided that the fitted equations approximate adequately the true (unknown) system responses, the optimal operating conditions of the model will be "close" to the optimal operating conditions of the true system.

*The DOE approach to optimization*

The experimental optimization of response surface models differs from classical optimization techniques in at least three ways:

*Find approximate (good) models and iteratively search for (near) optimal operating conditions*

- Experimental optimization is an iterative process; that is, experiments conducted in one set of experiments result in fitted models that indicate where to search for improved operating conditions in the next set of experiments. Thus, the coefficients in the fitted equations (or the form of the fitted equations) may change during the optimization process. This is in contrast to classical optimization in which the functions to optimize are supposed to be fixed and given.

*Randomness (sampling variability) affects the final answers and should be taken into account*

- The response models are fit from experimental data that usually contain random variability due to uncontrollable or unknown causes. This implies that an experiment, if repeated, will result in a different fitted response surface model that might lead to different optimal operating conditions. Therefore, sampling variability should be considered in experimental optimization.

    In contrast, in classical optimization techniques the functions are deterministic and given.

*Optimization process requires input of the experimenter*

- The fitted responses are local approximations, implying that the optimization process requires the input of the experimenter (a person familiar with the process). This is in contrast with classical optimization which is always automated in the form of some computer algorithm.
