# How Do You Select an Experimental Design?

*A design is selected based on the experimental objective and the number of factors*

The choice of an experimental design depends on the objectives of the experiment and the number of factors to be investigated.

**Experimental Design Objectives**

*Types of designs are listed here according to the experimental objective they meet*

Types of designs are listed here according to the experimental objective they meet.

- **Comparative objective**: If you have one or several factors under investigation, but the primary goal of your experiment is to make a conclusion about one a-priori important factor, (in the presence of, and/or in spite of the existence of the other factors), and the question of interest is whether or not that factor is "significant", (i.e., whether or not there is a significant change in the response for different levels of that factor), then you have a *comparative problem* and you need a *comparative design* solution.

- **Screening objective**: The primary purpose of the experiment is to select or *screen out* the few important main effects from the many less important ones. These *screening designs* are also termed main effects designs.

- **Response Surface (method) objective**: The experiment is designed to allow us to estimate interaction and even quadratic effects, and therefore give us an idea of the (local) shape of the response surface we are investigating. For this reason, they are termed *response surface method (RSM) designs*. RSM designs are used to:
    - Find improved or optimal process settings
    - Troubleshoot process problems and weak points
    - Make a product or process more *robust* against external and non-controllable influences. "Robust" means relatively insensitive to these influences.

- **Optimizing responses when factors are proportions of a mixture objective**: If you have factors that are proportions of a mixture and you want to know what the "best" proportions of the factors are so as to maximize (or minimize) a response, then you need a *mixture design*.

- **Optimal fitting of a regression model objective**: If you want to model a response as a mathematical function (either known or empirical) of a few continuous factors and you desire "good" model parameter estimates (i.e., unbiased and minimum variance), then you need a *regression design*.

*Mixture and regression designs*

Mixture designs are discussed briefly in section 5 (Advanced Topics) and regression designs for a single factor are discussed in chapter 4. Selection of designs for the remaining 3 objectives is summarized in the following table.

*Summary table for choosing an experimental design for comparative, screening, and response surface designs*

**TABLE 3.1: Design Selection Guideline**

| **Number of Factors** | **Comparative Objective** | **Screening Objective** | **Response Surface Objective** |
|:---:|---|---|---|
| 1 | [1-factor completely randomized design](completely-randomized.md) | — | — |
| 2 - 4 | [Randomized block design](randomized-block.md) | [Full](full-factorial.md) or [fractional factorial](fractional-factorial.md) | [Central composite](central-composite.md) or [Box-Behnken](box-behnken.md) |
| 5 or more | [Randomized block design](randomized-block.md) | [Fractional factorial](fractional-factorial.md) or [Plackett-Burman](plackett-burman.md) | Screen first to reduce number of factors |

*Resources and degree of control over wrong decisions*

Choice of a design from within these various types depends on the amount of resources available and the degree of control over making wrong decisions (Type I and Type II errors for testing hypotheses) that the experimenter desires.

*Save some runs for center points and "redos" that might be needed*

It is a good idea to choose a design that requires somewhat fewer runs than the budget permits, so that [center point](center-points.md) runs can be added to check for curvature in a 2-level screening design and backup resources are available to redo runs that have processing mishaps.
