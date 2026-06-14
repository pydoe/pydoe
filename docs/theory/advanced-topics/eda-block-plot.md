# Block Plot

*Purpose*
The block plot answers the following two general questions:

- What are the important factors (including interactions)?
   - What are the best settings for these important factors?

The basic (single) block plot is a multifactor EDA technique to
determine if a factor is important and to ascertain if that
importance is unconditional (robust) over all settings of all
other factors in the system.  In an experimental design context, the
block plot is actually a sequence of block plots with one plot
for each of the $k$ factors.

Due to the ability of the block plot to determine whether a
factor is important over all settings of all other factors,
the block plot is also referred to as a DOE robustness plot.

*Output*
The block plot provides specific information on

- Important factors (of the $k$ factors and the
       $\left(
               \begin{array}{c}
                   k \\
                   2
               \end{array}
          \right)$ 2-factor interactions); and
   - Best settings of the important factors.

*Definition*
The block plot is a series of $k$ basic block plots with each
basic block plot for a main effect.  Each basic block plot asks the
question as to whether that particular factor is important:

- The first block plot asks the question:
       "Is factor $X_1$ important?
   - The second block plot asks the question:
       "Is factor $X_2$ important?
   - Continue for the remaining factors.

The $i$-th basic block plot, which targets factor $i$ and asks whether factor $X_i$ is important, is formed by:

- Vertical Axis: Response

- Horizontal Axis: All $2^k$-1 possible        combinations of the ($k$-1) non-target factors (that
       is, "robustness" factors).  For example, for the block plot
       focusing on factor $X_1$ from a 23 full factorial
       experiment, the horizontal axis will consist of all
       23-1 = 4 distinct combinations of factors $X_2$        and $X_3$.  We create this robustness factors axis because
       we are interested in determining if $X_1$ is important        robustly.  That is, we are interested in whether $X_1$ is
       important not only in a general/summary kind of way, but also
       whether the importance of $X$ is universally and
       consistently valid over each of the 23-1 = 4
       combinations of factors $X_2$ and $X_3$.  These four        combinations are ($X_2$, $X_3$) = (+, +), (+, -), (-, +),
       and (-, -).  The robustness factors on the horizontal axis change
       from one block plot to the next.  For example, for the
       $k$ = 3 factor case:

- the block plot targeting $X_1$ will have robustness               factors $X_2$ and $X_3$;           - the block plot targeting $X_2$ will have robustness               factors $X_1$ and $X_3$;           - the block plot targeting $X_3$ will have robustness               factors $X_1$ and $X_2$.

- Plot Character: The setting (- or +) for the target factor
       $X_i$.  Each point in a block plot has an
       associated setting for the target factor
       $X_i$.  If $X_i$ = "-", the
       corresponding plot point will be "-"; if
       $X_i$ = "+", the corresponding plot
       point will be "+".

For a particular combination of robustness factor settings
(horizontally), there will be two points plotted above it
(vertically):

- one plot point for $X_i$ = "-"; and    - the other plot point for $X_i$ = "+".

In a block plot, these two plot points are surrounded by a box
(a block) to focus the eye on the
internal within-block differences as opposed to the distraction
of the external block-to-block differences.  Internal block
differences reflect on the importance of the target factor (as
desired).  External block-to-block differences reflect on the
importance of various robustness factors, which is not of primary
interest.

Large within-block differences (that is, tall blocks) indicate a
large local effect on the response which, since all robustness
factors are fixed for a given block, can only be attributed to the
target factor.  This identifies an "important" target factor.
Small within-block differences (small blocks) indicate that the
target factor $X_i$ is unimportant.

For a given block plot, the specific question of interest is thus

   Is the target factor $X_i$ important?  That is,
   as we move within a block from the target factor setting of "-" to
   the target factor setting of "+", does the response variable
   value change by a large amount?

The height of the block reflects the "local" (that is, for that
particular combination of robustness factor settings) effect on
the response due to a change in the target factor settings.  The
"localized" estimate for the target factor effect for
$X_i$ is in fact identical to the difference in the
response between the target factor $X_i$ at the "+"
setting and at the "-" setting.  Each block height of a robustness
plot is thus a localized estimate of the target factor effect.

In summary, important factors will have both

- consistently large block heights; and
   - consistent +/- sign arrangements

where the "consistency" is over all settings of robustness factors.
Less important factors will have only one of these two properties.
Unimportant factors will have neither property.

*Plot for defective springs data*
Applying the ordered response plot to the defective springs data set
yields the following plot.

[![Block plots for the defective springs data](https://www.itl.nist.gov/div898/handbook/pri/section5/gifs/blockplt.r.gif)](gifs/blockplt.gif)

*How to interpret*
From the block plot, we are looking for the following:

- Important factors (including 2-factor interactions);
   - Best settings for these factors.

We will discuss each of these in turn.

**Important factors (including 2-factor interactions):**

Look at each of the $k$ block plots.  Within a given block plot,

      Are the corresponding block heights
      consistently large as we scan across the
      within-plot robustness factor
      settings--yes/no; and are the within-block
      sign patterns (+ above -, or - above +)
      consistent across all robustness factors
      settings--yes/no?

To facilitate intercomparisons, all block plots have the same
vertical axis scale.  Across such block plots,

- Which plot has the consistently largest block heights,
       along with consistent arrangement of within-block +'s
       and -'s?  This defines the "most important factor".

- Which plot has the consistently next-largest block heights,
       along with consistent arrangement of within-block
       +'s and -'s?   This defines the "second most important
       factor".

- Continue for the remaining factors.

This scanning and comparing of the $k$ block plots easily
leads to the identification of the most important factors.  This
identification has the additional virtue over previous steps in
that it is robust.  For a given important factor, the consistency
of block heights and sign arrangement across robustness factors
gives additional credence to the robust importance of that factor.
The factor is important (the change in the response will be large)
irrespective of what settings the robustness factors have.  Having
such information is both important and comforting.

**Important Special Case; Large but Inconsistent:**

What happens if the block heights are large but **not** consistent?
Suppose, for example, a 23 factorial experiment is being
analyzed and the block plot focusing on factor $X_1$ is being
examined and interpreted so as to address the usual question of
whether factor $X_1$ is important.

Let us consider in some detail how such a block plot might
appear.  This $X_1$ block plot will have 23-1 = 4
combinations of the robustness factors $X_2$ and $X_3$ along
the horizontal axis in the following order:

   ($X_2$, $X_3$) = (+, +);  ($X_2$, $X_3$) = (+, -);    ($X_2$, $X_3$) = (-, +);  ($X_2$, $X_3$) = (-, -).

If the block heights are consistently large (with "+" above "-" in
each block) over the four combinations of settings for $X_2$ and
$X_3$, as in

| ($X_2$, $X_3$) | block height (= local $X_1$ effect) |
| --- | --- |
| (+, +) | 30 |
| (+, -) | 29 |
| (-, +) | 29 |
| (-, -) | 31 |

then from binomial considerations there is one chance in
24-1 = 1/8 $\approx$ 12.5 % of the the four local $X_1$ effects having the same
sign (i.e., all positive or all negative).  The usual statistical
cutoff of 5 % has not been achieved here, but the 12.5 % is suggestive.
Further, the consistency of the four $X_1$ effects (all near 30) is evidence of a robustness of the $X$ effect
over the settings of the other two factors.  In summary, the
above suggests:

- Factor 1 is probably important (the issue of how large the
       effect has to be in order to be considered important will
       be discussed in more detail in a later section); and
   - The estimated factor 1 effect is about 30 units.

On the other hand, suppose the 4 block heights for
factor 1 vary in the following cyclic way:

| ($X_2$, $X_3$) | block height (= local $X_1$ effect) |
| --- | --- |
| (+, +) | 30 |
| (+, -) | 20 |
| (-, +) | 30 |
| (-, -) | 20 |

then how is this to be interpreted?

The key here to such interpretation is that the block plot is
telling us that the estimated $X_1$ effect is in fact at least 20 units, but **not** consistent.  The effect is
changing, but it is changing in a structured way.  The "trick"
is to scan the $X_2$ and $X_3$ settings and deduce what that
substructure is.  Doing so from the above table, we see that the
estimated $X_1$ effect is 30

- for point 1 ($X_2$, $X_3$) = (+, +) and    - for point 3 ($X_2$, $X_3$) = (-, +)

and then the estimated $X_1$ effect drops 10 units to 20

- for point 2 ($X_2$, $X_3$) = (+, -) and    - for point 4 ($X_2$, $X_3$) = (-, -)

We thus deduce that the estimated $X_1$ effect is

- 30 whenever $X_3$ = "+"    - 20 whenever $X_3$ = "-"

When the factor $X_1$ effect is not consistent,  but in fact changes
depending on the setting of factor $X_3$, then definitionally that is said to be an "$X_1$*$X_3$ interaction".  That is precisely
the case here, and so our conclusions would be:

- factor $X_1$ is probably
       [important](eda-scatter-plot.md);
   - the estimated factor $X_1$ effect is 25
       (the average of 30, 20, 30, and 20);
   - the $X_1$*$X_3$ interaction is probably important;
   - the estimated $X_1$*$X_3$ interaction is about 10        (the change in the factor $X_1$ effect as $X_3$
       changes = 30 - 20 = 10);
   - hence the $X_1$*$X_3$ interaction is less        important than the $X_1$ effect.

Note that we are using the term important in a qualitative sense here.
More precise determinations of importance in terms of statistical
or engineering significance are discussed in later sections.

The block plot gives us the structure and the detail to allow
such conclusions to be drawn and to be understood.  It is a
valuable adjunct to the previous analysis steps.

**Best settings:**

After identifying important factors, it is also of use to
determine the best settings for these factors.  As usual, best
settings are determined for main effects only (since main
effects are all that the engineer can control).  Best settings
for interactions are not done because the engineer has
no direct way of controlling them.

In the block plot context, this determination of best factor
settings is done simply by noting which factor setting (+ or -)
within each block is closest to that which the engineer is
ultimately trying to achieve.  In the defective springs case,
since the response variable is percent acceptable springs, we are clearly
trying to maximize (as opposed to minimize, or hit a target) the
response and the ideal optimum point is 100 %.  Given this, we would
look at the block plot of a given important factor and note within
each block which factor setting (+ or -) yields a data value
closest to 100 % and then select that setting as the best for that
factor.

Since an important factor by definition will have
consistent +/- setting arrangements, then the selected best
setting will be consistent over all of the blocks as it should be.

From the defective springs block plots, we would thus conclude that

- the best setting for factor 1 is +;
   - the best setting for factor 2 is -;
   - the best setting for factor 3 cannot be easily determined.

*Conclusions for the defective springs data*
In summary, applying the block plot to the defective springs
data set results in the following conclusions:

- Unranked list of important factors (including interactions):

- $X_1$ is important;           - $X_2$ is important;           - $X_1$*$X_3$ is important.

- Best Settings:

($X_1$, $X_2$, $X_3$) = (+, -, ?) = (+1, -1, ?)
