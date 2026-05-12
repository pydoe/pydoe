# Fractional Factorial Designs

*Full factorial experiments can require many runs*

The ASQC (1983) Glossary & Tables for Statistical Quality Control defines fractional factorial design in the following way: "*A factorial experiment in which only an adequately chosen fraction of the treatment combinations required for the complete factorial experiment is selected to be run.*"

*A carefully chosen fraction of the runs may be all that is necessary*

Even if the number of factors, *k*, in a design is small, the $2^k$ runs specified for a full factorial can quickly become very large. For example, $2^6 = 64$ runs is for a two-level, full factorial design with six factors. To this design we need to add a good number of centerpoint runs and we can thus quickly run up a very large resource requirement for runs with only a modest number of factors.

*Later sections will show how to choose the "right" fraction for 2-level designs — these are both balanced and orthogonal*

The solution to this problem is to use only a fraction of the runs specified by the full factorial design. Which runs to make and which to leave out is the subject of interest here. In general, we pick a fraction such as ½, ¼, etc. of the runs called for by the full factorial. We use various strategies that ensure an appropriate choice of runs. The following sections will show you how to choose an appropriate fraction of a full factorial design to suit your purpose at hand. *Properly chosen fractional factorial designs for 2-level experiments have the desirable properties of being both balanced and orthogonal.*

!!! Note
    We will be emphasizing fractions of two-level designs only. This is because two-level fractional designs are, in engineering at least, by far the most popular fractional designs. Fractional factorials where some factors have three levels will be covered briefly in [Three-level, mixed level and fractional factorial designs](mixed-level.md).
