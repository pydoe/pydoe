# How to Model DOE Data

*DOE models should be consistent with the goal of the experiment*

In general, the trial model that will be fit to DOE data should be consistent with the goal of the experiment and has been predetermined by the goal of the experiment and the experimental design and data collection methodology.

*Comparative designs*

Models were given earlier for comparative designs ([Completely Randomized Designs](../choosing-design/completely-randomized.md), [Randomized Block Designs](../choosing-design/randomized-block.md)).

*Full factorial designs*

For full factorial designs with $k$ factors ($2^k$ runs, not counting any center points or replication runs), the full model contains all the main effects and all orders of interaction terms. Usually, higher-order (three or more factors) interaction terms are included initially to construct the normal (or half-normal) plot of effects, but later dropped when a simpler, adequate model is fit. Depending on the software available or the analyst's preferences, various techniques such as normal or half-normal plots, Youden plots, $p$-value comparisons and stepwise regression routines are used to reduce the model to the minimum number of needed terms. An example of model selection is shown [later in this section](full-factorial-example.md).

*Fractional factorial designs*

For fractional factorial screening designs, it is necessary to know the alias structure in order to write an appropriate starting model containing only the interaction terms the experiment was designed to estimate (assuming all terms confounded with these selected terms are insignificant). This is illustrated by the [fractional factorial example](fractional-factorial-example.md). The starting model is then possibly reduced by the same techniques described above for full factorial models.

*Response surface designs*

Response surface initial models include quadratic terms and may occasionally also include cubic terms. These models were described in [Response Surface Designs](../choosing-design/response-surface.md).

*Model validation*

Of course, as in all cases of model fitting, [residual analysis and other tests of model fit](testing-revising-models.md) are used to confirm or adjust models, as needed.
