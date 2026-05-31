# Background and Data

*Background and Motivation*
Sonoluminescence is the process of turning sound energy into
light.  An ultrasonic horn is used to resonate a bubble of air
in a medium, usually water.  The bubble is ultrasonically compressed
and then collapses to light-emitting plasma.

In the general physics community, sonoluminescence studies are
being carried out to characterize it, to understand it, and to
uncover its practical uses.  An unanswered question in the community
is whether sonoluminescence may be used for cold fusion.

NIST's motive for sonoluminescent investigations is to assess its
suitability for the dissolution of physical samples, which is needed
in the production of homogeneous Standard Reference Materials (SRMs).
It is believed that maximal dissolution coincides with maximal energy
and maximal light intensity.  The ultimate motivation for striving
for maximal dissolution is that this allows improved determination
of alpha-and beta-emitting radionuclides in such samples.

The objectives of the NIST experiment were to determine the
important factors that affect sonoluminescent light intensity
and to ascertain optimal settings of such factors that will
predictably achieve high intensities.  An original list of 49
factors was reduced, based on physics reasons, to the following
seven factors: molarity (amount of solute), solute type, pH,
gas type in the water, water depth, horn depth, and flask
clamping.

Time restrictions caused the experiment to be about one month,
which in turn translated into an upper limit of roughly 20 runs.
A 7-factor, 2-level fractional factorial design (Resolution IV)
was constructed and run.  The factor level settings are given
below.

Eva Wilcox and Ken Inn of the NIST Physics Laboratory conducted this
experiment during 1999.  Jim Filliben of the NIST Statistical
Engineering Division performed the analysis of the experimental data.

*Software*
The analyses used in this case study can be generated using
both [Dataplot code](pri621.dp) and
     .
The reader can download the data as a
text file.

*Response Variable, Factor Variables, and Factor-

Level Settings*
This experiment utilizes the following response and factor variables.

- Response Variable ($Y$) = The sonoluminescent light
       intensity.

- Factor 1 ($X_1$) = Molarity (amount of Solute).  The coding
       is -1 for 0.10 mol and +1 for 0.33 mol.

- Factor 2 ($X_2$) = Solute type.  The coding is
       -1 for sugar and +1 for glycerol.

- Factor 3 ($X_3$) = pH.  The coding is
       -1 for 3 and +1 for 11.

- Factor 4 ($X_4$) = Gas type in water.  The coding is
       -1 for helium and +1 for air.

- Factor 5 ($X_5$) = Water depth.  The coding is
       -1 for half and +1 for full.

- Factor 6 ($X_6$) = Horn depth.  The coding is
       -1 for 5 mm and +1 for 10 mm.

- Factor 7 ($X_7$) = Flask clamping.  The coding is
       -1 for unclamped and +1 for clamped.

This data set has 16 observations.  It is a 27-3
design with no center points.

*Goal of the Experiment*

This case study demonstrates the analysis of a 27-3
fractional factorial experimental design.  The goals of
this case study are:

- Determine the important factors that affect the
        sonoluminescent light intensity.  Specifically, we are
        trying to maximize this intensity.

- Determine the best settings of the seven factors so as
        to maximize the sonoluminescent light intensity.

*Data Used in the Analysis*
The following are the data used for this analysis.  This data set
is given in Yates order.

  Y           X1      X2      X3      X4      X5      X6      X7
Light             Solute             Gas   Water    Horn    Flask
Intensity Molarity  type     pH     Type   Depth   Depth  Clamping
------------------------------------------------------------------
 80.6       -1.0    -1.0    -1.0    -1.0    -1.0    -1.0    -1.0
 66.1        1.0    -1.0    -1.0    -1.0    -1.0     1.0     1.0
 59.1       -1.0     1.0    -1.0    -1.0     1.0    -1.0     1.0
 68.9        1.0     1.0    -1.0    -1.0     1.0     1.0    -1.0
 75.1       -1.0    -1.0     1.0    -1.0     1.0     1.0     1.0
373.8        1.0    -1.0     1.0    -1.0     1.0    -1.0    -1.0
 66.8       -1.0     1.0     1.0    -1.0    -1.0     1.0    -1.0
 79.6        1.0     1.0     1.0    -1.0    -1.0    -1.0     1.0
114.3       -1.0    -1.0    -1.0     1.0     1.0     1.0    -1.0
 84.1        1.0    -1.0    -1.0     1.0     1.0    -1.0     1.0
 68.4       -1.0     1.0    -1.0     1.0    -1.0     1.0     1.0
 88.1        1.0     1.0    -1.0     1.0    -1.0    -1.0    -1.0
 78.1       -1.0    -1.0     1.0     1.0    -1.0    -1.0     1.0
327.2        1.0    -1.0     1.0     1.0    -1.0     1.0    -1.0
 77.6       -1.0     1.0     1.0     1.0     1.0    -1.0    -1.0
 61.9        1.0     1.0     1.0     1.0     1.0     1.0     1.0
