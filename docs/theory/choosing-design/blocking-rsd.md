# Blocking a Response Surface Design

**How can we block a response surface design?**

**When augmenting a resolution V design to a CCC design by adding star points, it may be desirable to block the design**

If an investigator has run either a $2^k$ full factorial or a $2^{k-p}$ fractional factorial design of at least resolution V, augmentation of that design to a central composite design (either CCC or CCF) is easily accomplished by adding an additional set (block) of star and centerpoint runs. If the factorial experiment indicated (via the $t$ test) curvature, this composite augmentation is the best follow-up option.

*An orthogonal blocked response surface design has advantages*

An important point to take into account when choosing a response surface design is the possibility of running the design in blocks. Blocked designs are better designs if the design allows the estimation of individual and interaction factor effects independently of the block effects. This condition is called orthogonal blocking. Blocks are assumed to have no impact on the nature and shape of the response surface.

*CCF designs cannot be orthogonally blocked*

The CCF design does not allow orthogonal blocking and the Box-Behnken designs offer blocking only in limited circumstances, whereas the CCC does permit orthogonal blocking.

*Axial and factorial blocks*

In general, when two blocks are required there should be an axial block and a factorial block. For three blocks, the factorial block is divided into two blocks and the axial block is not split. The blocking of the factorial design points should result in orthogonality between blocks and individual factors and between blocks and the two factor interactions.

The following Central Composite design in two factors is broken into two blocks.

*Table of CCD design with 2 factors and 2 blocks*

**TABLE 3.29: CCD: 2 Factors, 2 Blocks**

| Pattern | Block | *X*1 | *X*2 | Comment |
|:---:|:---:|:---:|:---:|---|
| -- | 1 | -1 | -1 | Full Factorial |
| -+ | 1 | -1 | +1 | Full Factorial |
| +- | 1 | +1 | -1 | Full Factorial |
| ++ | 1 | +1 | +1 | Full Factorial |
| 00 | 1 | 0 | 0 | Center-Full Factorial |
| 00 | 1 | 0 | 0 | Center-Full Factorial |
| 00 | 1 | 0 | 0 | Center-Full Factorial |
| -0 | 2 | -1.414214 | 0 | Axial |
| +0 | 2 | +1.414214 | 0 | Axial |
| 0- | 2 | 0 | -1.414214 | Axial |
| 0+ | 2 | 0 | +1.414214 | Axial |
| 00 | 2 | 0 | 0 | Center-Axial |
| 00 | 2 | 0 | 0 | Center-Axial |
| 00 | 2 | 0 | 0 | Center-Axial |

Note that the first block includes the full factorial points and three centerpoint replicates. The second block includes the axial points and another three centerpoint replicates. Naturally these two blocks should be run as two separate random sequences.

*Table of CCD design with 3 factors and 3 blocks*

The following three examples show blocking structure for various designs.

**TABLE 3.30: CCD: 3 Factors 3 Blocks, Sorted by Block**

| Pattern | Block | *X*1 | *X*2 | *X*3 | Comment |
|:---:|:---:|:---:|:---:|:---:|---|
| --- | 1 | -1 | -1 | -1 | Full Factorial |
| -++ | 1 | -1 | +1 | +1 | Full Factorial |
| +-+ | 1 | +1 | -1 | +1 | Full Factorial |
| ++- | 1 | +1 | +1 | -1 | Full Factorial |
| 000 | 1 | 0 | 0 | 0 | Center-Full Factorial |
| 000 | 1 | 0 | 0 | 0 | Center-Full Factorial |
| --+ | 2 | -1 | -1 | +1 | Full Factorial |
| -+- | 2 | -1 | +1 | -1 | Full Factorial |
| +-- | 2 | +1 | -1 | -1 | Full Factorial |
| +++ | 2 | +1 | +1 | +1 | Full Factorial |
| 000 | 2 | 0 | 0 | 0 | Center-Full Factorial |
| 000 | 2 | 0 | 0 | 0 | Center-Full Factorial |
| -00 | 3 | -1.681793 | 0 | 0 | Axial |
| +00 | 3 | +1.681793 | 0 | 0 | Axial |
| 0-0 | 3 | 0 | -1.681793 | 0 | Axial |
| 0+0 | 3 | 0 | +1.681793 | 0 | Axial |
| 00- | 3 | 0 | 0 | -1.681793 | Axial |
| 00+ | 3 | 0 | 0 | +1.681793 | Axial |
| 000 | 3 | 0 | 0 | 0 | Axial |
| 000 | 3 | 0 | 0 | 0 | Axial |

*Table of CCD design with 4 factors and 3 blocks*

**TABLE 3.31  CCD: 4 Factors, 3 Blocks**

| Pattern | Block | *X*1 | *X*2 | *X*3 | *X*4 | Comment |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| ---+ | 1 | -1 | -1 | -1 | +1 | Full Factorial |
| --+- | 1 | -1 | -1 | +1 | -1 | Full Factorial |
| -+-- | 1 | -1 | +1 | -1 | -1 | Full Factorial |
| -+++ | 1 | -1 | +1 | +1 | +1 | Full Factorial |
| +--- | 1 | +1 | -1 | -1 | -1 | Full Factorial |
| +-++ | 1 | +1 | -1 | +1 | +1 | Full Factorial |
| ++-+ | 1 | +1 | +1 | -1 | +1 | Full Factorial |
| +++- | 1 | +1 | +1 | +1 | -1 | Full Factorial |
| 0000 | 1 | 0 | 0 | 0 | 0 | Center-Full Factorial |
| 0000 | 1 | 0 | 0 | 0 | 0 | Center-Full Factorial |
| ---- | 2 | -1 | -1 | -1 | -1 | Full Factorial |
| --++ | 2 | -1 | -1 | +1 | +1 | Full Factorial |
| -+-+ | 2 | -1 | +1 | -1 | +1 | Full Factorial |
| -++- | 2 | -1 | +1 | +1 | -1 | Full Factorial |
| +--+ | 2 | +1 | -1 | -1 | +1 | Full Factorial |
| +-+- | 2 | +1 | -1 | +1 | -1 | Full Factorial |
| ++-- | 2 | +1 | +1 | -1 | -1 | Full Factorial |
| ++++ | 2 | +1 | +1 | +1 | +1 | Full Factorial |
| 0000 | 2 | 0 | 0 | 0 | 0 | Center-Full Factorial |
| 0000 | 2 | 0 | 0 | 0 | 0 | Center-Full Factorial |
| -000 | 3 | -2 | 0 | 0 | 0 | Axial |
| +000 | 3 | +2 | 0 | 0 | 0 | Axial |
| 0-00 | 3 | 0 | -2 | 0 | 0 | Axial |
| 0+00 | 3 | 0 | +2 | 0 | 0 | Axial |
| 00-0 | 3 | 0 | 0 | -2 | 0 | Axial |
| 00+0 | 3 | 0 | 0 | +2 | 0 | Axial |
| 000- | 3 | 0 | 0 | 0 | -2 | Axial |
| 000+ | 3 | 0 | 0 | 0 | +2 | Axial |
| 0000 | 3 | 0 | 0 | 0 | 0 | Center-Axial |
| 0000 | 3 | 0 | 0 | 0 | 0 | Center-Axial |

*Table of CCD design with 5 factors and 2 blocks*

**TABLE 3.32  CCD: 5 Factors, 2 Blocks**

| Pattern | Block | *X*1 | *X*2 | *X*3 | *X*4 | *X*5 | Comment |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| ----+ | 1 | -1 | -1 | -1 | -1 | +1 | Fractional Factorial |
| ---+- | 1 | -1 | -1 | -1 | +1 | -1 | Fractional Factorial |
| --+-- | 1 | -1 | -1 | +1 | -1 | -1 | Fractional Factorial |
| --+++ | 1 | -1 | -1 | +1 | +1 | +1 | Fractional Factorial |
| -+--- | 1 | -1 | +1 | -1 | -1 | -1 | Fractional Factorial |
| -+-++ | 1 | -1 | +1 | -1 | +1 | +1 | Fractional Factorial |
| -++-+ | 1 | -1 | +1 | +1 | -1 | +1 | Fractional Factorial |
| -+++- | 1 | -1 | +1 | +1 | +1 | -1 | Fractional Factorial |
| +---- | 1 | +1 | -1 | -1 | -1 | -1 | Fractional Factorial |
| +--++ | 1 | +1 | -1 | -1 | +1 | +1 | Fractional Factorial |
| +-+-+ | 1 | +1 | -1 | +1 | -1 | +1 | Fractional Factorial |
| +-++- | 1 | +1 | -1 | +1 | +1 | -1 | Fractional Factorial |
| ++--+ | 1 | +1 | +1 | -1 | -1 | +1 | Fractional Factorial |
| ++-+- | 1 | +1 | +1 | -1 | +1 | -1 | Fractional Factorial |
| +++-- | 1 | +1 | +1 | +1 | -1 | -1 | Fractional Factorial |
| +++++ | 1 | +1 | +1 | +1 | +1 | +1 | Fractional Factorial |
| 00000 | 1 | 0 | 0 | 0 | 0 | 0 | Center-Fractional Factorial |
| 00000 | 1 | 0 | 0 | 0 | 0 | 0 | Center-Fractional Factorial |
| 00000 | 1 | 0 | 0 | 0 | 0 | 0 | Center-Fractional Factorial |
| 00000 | 1 | 0 | 0 | 0 | 0 | 0 | Center-Fractional Factorial |
| 00000 | 1 | 0 | 0 | 0 | 0 | 0 | Center-Fractional Factorial |
| 00000 | 1 | 0 | 0 | 0 | 0 | 0 | Center-Fractional Factorial |
| -0000 | 2 | -2 | 0 | 0 | 0 | 0 | Axial |
| +0000 | 2 | +2 | 0 | 0 | 0 | 0 | Axial |
| 0-000 | 2 | 0 | -2 | 0 | 0 | 0 | Axial |
| 0+000 | 2 | 0 | +2 | 0 | 0 | 0 | Axial |
| 00-00 | 2 | 0 | 0 | -2 | 0 | 0 | Axial |
| 00+00 | 2 | 0 | 0 | +2 | 0 | 0 | Axial |
| 000-0 | 2 | 0 | 0 | 0 | -2 | 0 | Axial |
| 000+0 | 2 | 0 | 0 | 0 | +2 | 0 | Axial |
| 0000- | 2 | 0 | 0 | 0 | 0 | -2 | Axial |
| 0000+ | 2 | 0 | 0 | 0 | 0 | +2 | Axial |
| 00000 | 2 | 0 | 0 | 0 | 0 | 0 | Center-Axial |
