# What is a Mixture Design?

*When the factors are proportions of a blend, you need to use a
mixture design*
In a mixture experiment, the independent factors are proportions of
different components of a blend.  For example, if you want to optimize
the tensile strength of stainless steel, the factors of interest might
be the proportions of iron, copper, nickel, and chromium in the alloy.
The fact that the proportions of the different factors must sum to 100%
complicates the design as well as the analysis of mixture experiments.

*Standard mixture designs and constrained mixture designs*
When the mixture components are subject to the constraint that they
must sum to one, there are standard mixture designs for fitting
standard models, such as *Simplex-Lattice* designs and
*Simplex-Centroid* designs.  When mixture components are subject
to additional constraints, such as a maximum and/or minimum value
for each component, designs other than the standard mixture designs,
referred to as constrained mixture designs or *Extreme-Vertices*
designs, are appropriate.

*Measured response assumed to depend only on relative proportions*
In mixture experiments, the measured response is assumed to depend
only on the relative proportions of the ingredients or components in
the mixture and not on the amount of the mixture.  The amount of the
mixture could also be studied as an additional factor in the
experiment; however, this would be an example of mixture and process
variables being treated together.

*Proportions of each variable must sum to 1*
The main distinction between mixture experiments and independent
variable experiments is that with the former, the input variables or
components are non-negative proportionate amounts of the mixture, and
if expressed as fractions of the mixture, they must sum to one.  If
for some reason, the sum of the component proportions is less than
one, the variable proportions can be rewritten as scaled fractions
so that the scaled fractions sum to one.

*Purpose of a mixture design*
In mixture problems, the purpose of the experiment is to model the
blending surface with some form of mathematical equation so that:

- Predictions of the response for any mixture or combination
       of the ingredients can be made empirically, or

- Some measure of the influence on the response of each component
       singly and in combination with other components can be
       obtained.

*Assumptions for mixture experiments*
The usual assumptions made for factorial experiments are also made for
mixture experiments.  In particular, it is assumed that the errors are
independent and identically distributed with zero mean and common
variance.  Another assumption that is made, as with factorial designs,
is that the true underlying response surface is continuous over the
region being studied.

*Steps in planning a mixture experiment*
Planning a mixture experiment typically involves the following steps
(Cornell and Piepel, 1994):

- Define the objectives of the experiment.

- Select the mixture components and any other factors to be
       studied. Other factors may include process variables or the
       total amount of the mixture.

- Identify any constraints on the mixture components or other
       factors in order to specify the experimental region.

- Identify the response variable(s) to be measured.

- Propose an appropriate model for modeling the response data as
       functions of the mixture components and other factors selected
       for the experiment.

- Select an experimental design that is sufficient not only to
       fit the proposed model, but which allows a test of model
       adequacy as well.
