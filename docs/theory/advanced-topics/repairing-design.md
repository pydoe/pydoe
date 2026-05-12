# Repairing a Design

*Repair or augment classical designs*

Computer-aided designs are helpful in either repairing or augmenting a current experimental design. They can be used to repair a 'broken' standard classical design.

*Original design matrix may contain runs that were lost or impossible to achieve*

There may be situations in which, due to improper planning or other issues, the original design matrix contains forbidden or unreachable combinations of the factor settings. A computer-aided design (for example a [D-optimal design](d-optimal.md)) can be used to 'replace' those runs from the original design that were unattainable. The runs from the original design that are attainable are labeled as 'inclusion' runs and will be included in the final computer-aided design.

*Computer-aided design can generate additional attainable runs*

Given a pre-specified model, the computer-aided design can generate the additional attainable runs that are necessary in order to estimate the model of interest. As a result, the computer-aided design is just replacing those runs in the original design that were unattainable with a new set of runs that are attainable, and which still allows the experimenter to obtain information regarding the factors from the experiment.

*Properties of this final design may not compare with those of the original design*

The properties of this final design will probably not compare with those of the original design and there may exist some correlation among the estimates. However, instead of not being able to use any of the data for analysis, generating the replacement runs from a computer-aided design, a D-optimal design for example, allows one to analyze the data. Furthermore, computer-aided designs can be used to augment a classical design with treatment combinations that will break alias chains among the terms in the model or permit the estimation of curvilinear effects.
