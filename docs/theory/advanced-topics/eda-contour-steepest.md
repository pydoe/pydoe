# Steepest Ascent/Descent

*Start at optimum corner point*
From the [optimum corner point](eda-contour-best-corner.md), based on the
nature of the contour surface at that corner, step out in the
direction of steepest ascent (if maximizing) or steepest descent
(if minimizing).

*Defective springs example*
Since our goal for the defective springs problem is to maximize the
response, we seek the path of steepest ascent.  Our starting point is
the best corner (the upper right corner (+, +)), which has an average
response value of 88.5.  The [contour lines](eda-contour-plot.md)
for this plot have increments of 5 units.  As we move from left to
right across the contour plot, the contour lines go from low to high
response values.  In the plot, we have drawn the maximum contour level,
105, as a thick line.  For easier identification, we have also drawn
the contour level of 90 as thick line.  This contour level of 90 is
immediately to the right of the best corner

*Conclusions on steepest ascent for defective springs example*
The nature of the contour curves in the vicinity of (+, +) suggests
a path of steepest ascent

- in the "northeast" direction
   - about 30 degrees above the horizontal.
