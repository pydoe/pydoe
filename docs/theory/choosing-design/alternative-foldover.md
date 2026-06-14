# Alternative Foldover Designs

*Alternative foldover designs can be an economical way to break up
a selected alias pattern*
The mirror-image foldover (in which signs in all columns are reversed)
is only one of the possible follow-up fractions that can be run to
augment a fractional factorial design.  It is the most common choice
when the original fraction is resolution III.  However, alternative
foldover designs with fewer runs can often be utilized to break up
selected alias patterns.  We illustrate this by looking at what
happens when the signs of a single factor column are reversed.

*Example of de-aliasing a single factor*

[Previously](mirror-image-foldover.md), we described

how we de-alias all the factors of a 27-4 experiment.
Suppose that we only want to de-alias the $X_4$ factor.
This can be accomplished by only changing the sign of
$X_4$ = $X_1$$X_2$ to
$X_4$ = -$X_1$$X_2$.
The resulting design is:

*Table showing design matrix of a reverse X4 foldover design*

**TABLE 3.36: A "Reverse X4" Foldover Design** |  |  |  |  |
| run | $X_1$ | $X_2$ | $X_3$ | $X_4$ = -$X_1$$X_2$ | $X_5$ = -$X_1$$X_3$ | $X_6$ = $X_2$$X_3$ | $X_7$ = |

      $X_1$$X_2$$X_3$

| 1 | -1 | -1 | -1 | -1 | +1 | +1 | -1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | +1 | -1 | -1 | +1 | -1 | +1 | +1 |
| 3 | -1 | +1 | -1 | +1 | +1 | -1 | +1 |
| 4 | +1 | +1 | -1 | -1 | -1 | -1 | -1 |
| 5 | -1 | -1 | +1 | -1 | -1 | -1 | +1 |
| 6 | +1 | -1 | +1 | +1 | +1 | -1 | -1 |
| 7 | -1 | +1 | +1 | +1 | -1 | +1 | -1 |
| 8 | +1 | +1 | +1 | -1 | +1 | +1 | +1 |
*Alias patterns and effects that can be estimated in the example design*

The two-factor alias patterns for $X_4$ are:

- Original experiment: $X_4$ =        $X_1$$X_2$ =        $X_3$$X_7$ =        $X_5$$X_6$;    - "Reverse $X_4$" foldover experiment:         $X_4$ = -$X_1$$X_2$         = -$X_3$$X_7$ =         -$X_5$$X_6$.

The following effects can be estimated by combining the original $2_{III}^{7-4}$ with the "Reverse $X_4$" foldover
fraction:

$X_1$ + $X_3$$X_5$ +        $X_6$$X_7$

$X_2$ + $X_3$$X_6$ +        $X_5$$X_7$

$X_3$ + $X_1$$X_5$ +        $X_2$$X_6$

$X_4$

$X_5$ + $X_1$$X_3$ +        $X_2$$X_7$

$X_6$ + $X_2$$X_3$ +        $X_1$$X_7$

$X_7$ + $X_2$$X_5$ +        $X_1$$X_6$

$X_1$$X_4$

$X_2$$X_4$

$X_3$$X_4$

$X_4$$X_5$

$X_4$$X_6$

$X_4$$X_7$

$X_1$$X_2$ +        $X_3$$X_7$ +        $X_5$$X_6$

**Note:** The 16 runs allow estimating the above 14 effects, with one
degree of freedom left over for a possible block effect.

*Advantage and disadvantage of this example design*

The advantage of this follow-up design is that it permits estimation of

the $X_4$ effect and each of the six two-factor interaction
terms involving $X_4$.

The disadvantage is that the combined fractions still yield a resolution
III design, with all main effects other than $X_4$ aliased
with two-factor interactions.

*Case when purpose is simply to estimate all two-factor interactions
of a single factor*
Reversing a single factor column to obtain de-aliased two-factor
interactions for that one factor works for any resolution III or IV
design.  When used to follow-up a resolution IV design, there are
relatively few new effects to be estimated (as compared to 2^{k-p}
$2_{III}^{k-p}$ designs).  When the original resolution IV fraction
provides sufficient precision, and the purpose of the follow-up runs is
simply to estimate all two-factor interactions for one factor, the
*semifolding* option should be considered.

| **Semifolding** |
| --- | --- |

*Number of runs can be reduced for resolution IV designs*
For resolution IV fractions, it is possible to economize on the number
of runs that are needed to break the alias chains for all two-factor
interactions of a single factor.  In the above case we needed 8
additional runs, which is the same number of runs that were used in the
original experiment.  This can be improved upon.

*Additional information on John's 3/4 designs*

We can repeat only the points that were set at the high levels of the

factor of choice and then run them at their low settings in the next
experiment.  For the given example, this means an additional 4 runs
instead 8.  We mention this technique only in passing, more details
may be found in the references (or see
John's 3/4 designs).
