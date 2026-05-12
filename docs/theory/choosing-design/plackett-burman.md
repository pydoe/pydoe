# Plackett-Burman Designs

*Plackett-Burman designs*

In 1946, R.L. Plackett and J.P. Burman published their now famous paper "The Design of Optimal Multifactorial Experiments" in *Biometrika* (vol. 33). This paper described the construction of very economical designs with the run number a multiple of four (rather than a power of 2). Plackett-Burman designs are very efficient screening designs when only main effects are of interest.

*These designs have run numbers that are a multiple of 4*

Plackett-Burman (PB) designs are used for screening experiments because, in a PB design, main effects are, in general, heavily confounded with two-factor interactions. The PB design in 12 runs, for example, may be used for an experiment containing up to 11 factors.

*12-Run Plackett-Burman design*

**TABLE 3.18: Plackett-Burman Design in 12 Runs for up to 11 Factors**

| | Pattern | *X*1 | *X*2 | *X*3 | *X*4 | *X*5 | *X*6 | *X*7 | *X*8 | *X*9 | *X*10 | *X*11 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | +++++++++++ | +1 | +1 | +1 | +1 | +1 | +1 | +1 | +1 | +1 | +1 | +1 |
| 2 | -+-+++---+- | -1 | +1 | -1 | +1 | +1 | +1 | -1 | -1 | -1 | +1 | -1 |
| 3 | --+-+++---+ | -1 | -1 | +1 | -1 | +1 | +1 | +1 | -1 | -1 | -1 | +1 |
| 4 | +--+-+++--- | +1 | -1 | -1 | +1 | -1 | +1 | +1 | +1 | -1 | -1 | -1 |
| 5 | -+--+-+++-- | -1 | +1 | -1 | -1 | +1 | -1 | +1 | +1 | +1 | -1 | -1 |
| 6 | --+--+-+++- | -1 | -1 | +1 | -1 | -1 | +1 | -1 | +1 | +1 | +1 | -1 |
| 7 | ---+--+-+++ | -1 | -1 | -1 | +1 | -1 | -1 | +1 | -1 | +1 | +1 | +1 |
| 8 | +---+--+-++ | +1 | -1 | -1 | -1 | +1 | -1 | -1 | +1 | -1 | +1 | +1 |
| 9 | ++---+--+-+ | +1 | +1 | -1 | -1 | -1 | +1 | -1 | -1 | +1 | -1 | +1 |
| 10 | +++---+--+- | +1 | +1 | +1 | -1 | -1 | -1 | +1 | -1 | -1 | +1 | -1 |
| 11 | -+++---+--+ | -1 | +1 | +1 | +1 | -1 | -1 | -1 | +1 | -1 | -1 | +1 |
| 12 | ----------- | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

*No defining relation*

These designs do not have a defining relation since interactions are not identically equal to main effects. With the $2_{III}^{k-p}$ designs, a main effect column $X_i$ is either orthogonal to $X_i X_j$ or identical to plus or minus $X_i X_j$. For Plackett-Burman designs, the two-factor interaction column $X_i X_j$ is correlated with every $X_k$ (for $k$ not equal to $i$ or $j$).

*Economical for detecting large main effects*

However, these designs are very useful for economically detecting large main effects, assuming all interactions are negligible when compared with the few important main effects.
