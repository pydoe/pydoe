# Mixture Designs with Process Variables

*Options for setting up experiments for processes that have
both standard process variables and mixture variables*
Consider a mixture experiment consisting of $q$ mixture components and $k$ process variables.  First consider the case
in which each of the process variables to be studied has only two
levels.  Orthogonally scaled factor settings for the process variables
will be used (i.e., -1 is the low level, 1 is the high level, and
0 is the center point). Also assume that each of the components
$x_i$ can range from 0 to 1. The region of interest
then for the process variables is a $k$-dimensional hypercube.

The region of interest for the mixture components is the
($q$-1)-dimensional simplex. The combined region of interest for
both the process variables and the mixture components is of
dimensionality $q$ - 1 + $k$.

*Example of three mixture components and three process variables*
For example, consider three mixture components
($x_1$, $x_2$, $x_3$) with three process variables ($z_1$, $z_2$,
$z_3$). The dimensionality of the region is 5. The
combined region of interest for the three mixture components and three
process variables is shown in the two figures below. The complete space
of the design can be viewed in either of two ways. The first diagram
shows the idea of a full factorial at each vertex of the
three-component simplex region. The second diagram shows the idea of
a three-component simplex region at each point in the full factorial.
In either case, the same overall process space is being
investigated.

*Diagram showing simplex region of a 3-component mixture
with a 2^3 full factorial at each pure mixture run*

![Diagram showing simplex region of a 3-component mixture
 with a 2^3 full factorial at each pure mixture run](https://www.itl.nist.gov/div898/handbook/pri/section5/gifs/simplex6.gif)

**FIGURE 5.13: Simplex Region of a Three Component Mixture with
a 23 Full Factorial at Each Pure Mixture Run**

*Diagram showing process space of a 23 full factorial
with the 3-component simplex region at each point of the full
factorial*

![Diagram showing process space of a 2^3 full factorial with the
three component simplex legion at each point of the full factorial](https://www.itl.nist.gov/div898/handbook/pri/section5/gifs/simplex7.gif)

**FIGURE 5.14: Process Space of a 23 Full Factorial
with the Three Component Simplex Region at Each Point of the Full
Factorial**

*Additional options available*
As can be seen from the above diagrams, setting up the design
configurations in the process variables and mixture components
involves setting up either a mixture design at each point of a
configuration in the process variables, or similarly, creating a
factorial arrangement in the process variables at each point of
composition in the mixture components. For the example depicted in
the above two diagrams, this is not the only design available for
this number of mixture components with the specified number of process
variables. Another option might be to run a fractional factorial
design at each vertex or point of the mixture design, with the same
fraction run at each mixture design point. Still another option might
be to run a fractional factorial design at each vertex or point of the
mixture design, with a different fraction run at each mixture design
point.
