# Optimal Setting

*Optimal setting*
The "near-point" optimality setting is the intersection of the
[steepest-ascent line](eda-contour-steepest.md) with the
[optimal setting curve](eda-contour-optimal-curve.md).

Theoretically, any ($X_1$, $X_3$) setting along the optimal curve would generate the desired response of $Y$ = 100.  In
practice, however, this is true only if our estimated contour surface
is identical to "nature's" response surface.  In reality, the plotted
contour curves are truth estimates based on the available (and "noisy")
$n$ = 8 data values.  We are confident of the contour curves in
the vicinity of the data points (the four corner points on the chart),
but as we move away from the corner points, our confidence in the
contour curves decreases.  Thus the point on the $Y$ = 100 optimal
response curve that is "most likely" to be valid is the one that is
closest to a corner point.  Our objective then is to locate that
"near-point".

*Defective springs example*
In terms of the defective springs contour plot, we draw a line from
the best corner, (+, +), outward and perpendicular to the $Y$ = 90,
$Y$ = 95, and $Y$ = 100 contour curves.  The $Y$ = 100
intersection yields the "nearest point" on the optimal response curve.

Having done so, it is of interest to note the coordinates of that
optimal setting.  In this case, [from the
graph](eda-contour-plot.md), that setting is (in coded units) approximately at

   ($X_1$ = 1.5, $X_3$ = 1.3)

*Table of coded and uncoded factors*
With the determination of this setting, we have thus, in theory,
formally completed our original task.  In practice, however, more
needs to be done.  We need to know "What is this optimal setting, not
just in the coded units, but also in the original (uncoded) units"?
That is, what does ($X_1$=1.5, $X_3$=1.3) correspond to in the units of the original data?

To deduce his, we need to refer back to the original (uncoded) factors
in this problem.  They were:

Coded
     Factor
| Uncoded Factor |
| --- | --- |
| $X_1$ | OT: Oven Temperature |
| $X_2$ | CC: Carbon Concentration |
| $X_3$ | QT: Quench Temperature |

*Uncoded and coded factor settings*
These factors had settings-- what were the settings of the coded
and uncoded factors?  From the original description of the problem,
the uncoded factor settings were:

- Oven   Temperature   (1450 and 1600 degrees)
   - Carbon Concentration (0.5 %  and 0.7 %)
   - Quench Temperature   (70   and 120 degrees)

with the usual settings for the corresponding
coded factors:

- $X_1$                   (-1, +1)    - $X_2$                   (-1, +1)    - $X_3$                   (-1, +1)

*Diagram*
To determine the corresponding setting for ($X_1$=1.5, $X_3$=1.3), we thus
refer to the following diagram, which mimics a scatter plot of
response averages--oven temperature (OT) on the horizontal axis and
quench temperature (QT) on the vertical axis:

![diagram representing response averages at optimal contour](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des7.gif)

                           .
                            .
                             ?
                              .
                                .
   120 +1 --------------
   Q      |55.5    88.5|
   u T    |            |
   e e  X |            |
   n m  3 |            |
   c p    |            |
   h      |            |
          |64        77|
    70 -1 --------------
          -1    X1    +1
         1450  Oven 1600
               Temp
</PRE>

The "X" on the chart represents the "near
point" setting on the optimal curve.

*Optimal setting for $X_1$ (oven temperature)*
To determine what "X" is in uncoded units, we note (from the graph)
that a linear transformation between OT and $X_1$ as defined by

   OT = 1450 => $X_1$ = -1

   OT = 1600 => $X_1$ = +1

yields

$X_1$ = 0 being at OT = (1450 + 1600) / 2 = 1525

thus

           |-------------|-------------|
X1:       -1             0            +1
OT:      1450          1525          1600

and so $X_1$ = +2, say, would be at oven temperature OT = 1675:

           |-------------|-------------|-------------|
X1:       -1             0            +1            +2
OT:      1450          1525          1600          1675

and hence the optimal $X_1$ setting of 1.5 must be at

   OT = 1600 + 0.5*(1675-1600) = 1637.5

*Optimal setting for $X_3$ (quench temperature)*
Similarly, from the graph we note that a linear transformation between
quench temperature QT and coded factor $X_3$ as specified by

   QT =  70 => $X_3$ = -1

   QT = 120 => $X_3$ = +1

yields

$X_3$ = 0 being at QT = (70 + 120) / 2 = 95

as in

        |-------------|-------------|
X3:    -1             0            +1
QT:    70            95           120

and so $X_3$ = +2, say, would be quench temperature = 145:

        |-------------|-------------|-------------|
X3:    -1             0            +1            +2
QT:    70            95           120           145

Hence, the optimal $X_3$ setting of 1.3 must be at

   QT = 120 + 0.3*(145-120)

   QT = 127.5

*Summary of optimal settings*
In summary, the optimal setting is

   coded  : ($X_1$ = +1.5, $X_3$ = +1.3)

   uncoded: (OT = 1637.5 degrees, QT = 127.5 degrees)

and finally, including the best setting of the fixed $X_2$ factor (carbon concentration CC) of $X_2$ = -1 (CC = 0.5 %), we thus have
the final, complete recommended optimal settings for all three factors:

   coded  : ($X_1$ = +1.5, $X_2$ = -1.0, $X_3$ = +1.3)

   uncoded: (OT = 1637.5, CC = 0.7 %, QT = 127.5)

If we were to run another experiment, this is the point (based on the
data) that we would set oven temperature, carbon concentration, and
quench temperature with the hope/goal of achieving 100 % acceptable
springs.

*Options for next step*
In practice, we could either

- collect a single data point (if money and time are an issue) at
       this recommended setting and see how close to 100 % we achieve, or

- collect two, or preferably three, (if money and time are less of
       an issue) replicates at the center point (recommended setting).

- if money and time are not an issue, run a 22 full
       factorial design with center point.  The design is centered on
       the optimal setting ($X_1$ = +1, 5, $X_3$ = +1.3) with        one overlapping new corner point at ($X_1$ = +1, $X_3$        = +1) and with new corner points at ($X_1$, $X_3$)
       = (+1, +1), (+2, +1), (+1, +1.6), (+2, +1.6).  Of these four new
       corner points, the point (+1, +1) has the advantage that it
       overlaps with a corner point of the original design.
