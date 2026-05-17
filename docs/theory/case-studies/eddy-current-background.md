# Background and Data

*Background*
The data for this case study is a subset of a study performed by
[Capobianco, Splett, and Iyer](../references/index.md).
Capobianco was a member of the NIST Electromagnetics Division and
Splett and Iyer were members of the NIST Statistical Engineering
Division at the time of this study.

The goal of this project is to develop a nondestructive portable
device for detecting cracks and fractures in metals.  A primary
application would be the detection of defects in
airplane wings.  The internal mechanism of the detector would be
for sensing crack-induced changes in the detector's electromagnetic
field, which would in turn result in changes in the impedance level
of the detector.  This change of impedance is termed "sensitivity"
and it is a sub-goal of this experiment to maximize such
sensitivity as the detector is moved from an unflawed region to
a flawed region on the metal.

*Statistical Goals*
The case study illustrates the analysis of a 23
full factorial experimental design.  The specific statistical goals
of the experiment are:

- Determine the important factors that affect
        sensitivity.
    - Determine the settings that maximize sensitivity.
    - Determine a predicition equation that functionally
        relates sensitivity to various factors.

*Software*
The analyses used in this case study can be generated using
both [Dataplot code](pri611.dp) and
     .
The reader can download the data as a
text file.

*Data Used in the Analysis*
There were three detector wiring component factors under
consideration:

- $X_1$ = Number of wire turns
   - $X_2$ = Wire winding distance
   - $X_3$ = Wire gauge

Since the maximum number of runs that could be afforded timewise
and costwise in this experiment was $n$ = 10, a 23
full factoral experiment (involving $n$ = 8 runs) was chosen.  With
an eye to the usual monotonicity assumption for two-level factorial
designs, the selected settings for the three factors were as
follows:

- $X_1$ = Number of wire turns : -1 = 90, +1 = 180
   - $X_2$ = Wire winding distance: -1 = 0.38, +1 = 1.14
   - $X_3$ = Wire gauge           : -1 = 40, +1 = 48

The experiment was run with the eight settings executed in random
order. The following data resulted.
Y          X1        X2        X3
  Probe      Number   Winding     Wire     Run
Impedance   of Turns  Distance    Gauge  Sequence
-------------------------------------------------
  1.70         -1        -1        -1           2
  4.57         +1        -1        -1           8
  0.55         -1        +1        -1           3
  3.39         +1        +1        -1           6
  1.51         -1        -1        +1           7
  4.59         +1        -1        +1           1
  0.67         -1        +1        +1           4
  4.29         +1        +1        +1           5
Note that the independent variables are coded as +1 and -1.  These
represent the low and high settings for the levels of each variable.
Factorial designs often have two levels for each factor (independent
variable) with the levels being coded as -1 and +1.  This is a
scaling of the data that can simplify the analysis.  If desired,
these scaled values can be converted back to the original units of
the data for presentation.
