# Axes

*What factors go on the two axes?*
For this first item, we choose the two most important
factors in the experiment as the plot axes.

These are determined from the ranked list of important factors
as discussed in the previous steps.  In particular, the
[|effects| plot](eda-effects-plot.md) includes a ranked factor
table.  For the defective springs data, that ranked list
consists of

| Factor/Interaction | Effect Estimate |
| --- | --- |
| $X_1$ | 23 |
| $X_1$*$X_3$ | 10 |
| $X_2$ | -5 |
| $X_3$ | 1.5 |
| $X_1$*$X_2$ | 1.5 |
| $X_1$*$X_2$*$X_3$ | 0.5 |
| $X_2$*$X_3$ | 0 |

*Possible choices*
In general, the two axes of the contour plot could consist of

- $X_1$ and $X_2$,    - $X_1$ and $X_3$, or    - $X_2$ and $X_3$.

In this case, since $X_1$ is the top item in the ranked list, with
an estimated effect of 23, $X_1$ is the most important factor and
so will occupy the horizontal axis of the contour plot.
The admissible list thus reduces to

- $X_1$ and $X_2$, or    - $X_1$ and $X_3$.

To decide between these two pairs, we look to the second item in the
ranked list.  This is the interaction term $X_1$*$X_3$, with an estimated effect of 10.  Since interactions are **not** allowed as contour plot axes, $X_1$*$X_3$ must be set aside.  On the other hand, the components of this interaction ($X_1$ and
$X_3$) are not to be set aside.  Since $X_1$ has already been
identified as one axis in the contour plot, this suggests that the
other component ($X_3$) be used as the second axis.  We do so.
Note that $X_3$ itself does **not** need to be important (in fact, it is noted that $X_3$ is ranked fourth in the listed
table with a value of 1.5).

In summary then, for this example the contour plot axes are:

Horizontal Axis: $X_1$

   Vertical Axis: $X_3$

*Four cases for recommended choice of axes*
Other cases can be more complicated.  In general, the
recommended rule for selecting the two plot axes is that they
be drawn from the first two items in the ranked list of factors.
The following four cases cover most situations in practice:

- Case 1:

- Item 1 is a main effect (e.g., $X_3$)           - Item 2 is another main effect (e.g., $X_5$)

Recommended choice:

- Horizontal axis: item 1 (e.g., $X_3$);           - Vertical axis: item 2 (e.g., $X_5$).

- Case 2:

- Item 1 is a main effect (e.g., $X_3$)
           - Item 2 is a (common-element) interaction
               (e.g., $X_3$*$X_4$)

Recommended choice:

- Horizontal axis: item 1 (e.g., $X_3$);
           - Vertical axis: the remaining component in item 2
               (e.g., $X_4$).

- Case 3:

- Item 1 is a main effect  (e.g., $X_3$)
           - Item 2 is a (non-common-element) interaction
               (e.g., $X_2$*$X_4$)

Recommended choice:

- Horizontal axis: item 1 (e.g., $X_3$);
           - Vertical axis: either component in item 2 (e.g.,
               $X_2$, or $X_4$), but preferably the one with
               the largest individual effect (thus scan the rest of
               the ranked factors and if the $X_2$                |effect| > $X_4$ |effect|, choose $X_2$;                otherwise choose $X_4$).

- Case 4:

- Item 1 is a (2-factor) interaction (e.g.,
               $X_2$*$X_4$)
           - Item 2 is anything

Recommended choice:

- Horizontal axis: component 1 from the item 1
               interaction (e.g., $X_2$);
           - Horizontal axis: component 2 from the item 1
               interaction (e.g., $X_4$).
