# TODO: DOE Methods

Design methods not implemented in pydoe.

## Mixture Designs

The entire mixture design family is absent. Mixture experiments differ from standard factorial designs because the factors are proportions that must sum to 1.

- [ ] **Mixture screening designs** — screen important components in a mixture using a sparse design
- [ ] **Simplex-lattice designs** — place design points on a regular lattice over the simplex (all proportions summing to 1); parameterized by degree *m* giving ${q+m-1 \choose m}$ points for *q* components
- [ ] **Simplex-centroid designs** — include all subsets of components at equal proportions; for *q* components generates $2^q - 1$ points (vertices, edge midpoints, face centroids, overall centroid)
- [ ] **Constrained mixture designs (Extreme-Vertices)** — handle lower and upper bounds on each component proportion; points are extreme vertices of the constrained region
- [ ] **Mixture + process variable designs** — combined designs where some factors are mixture proportions and others are independent process variables

## Factorial Design Extensions

- [ ] **Latin square designs** — arrange treatments in a square grid so that each treatment appears exactly once in each row and column; removes two nuisance factors simultaneously
- [ ] **Graeco-Latin square designs** — superimpose two orthogonal Latin squares; removes three nuisance factors
- [ ] **Hyper-Graeco-Latin square designs** — extension to four or more orthogonal Latin squares
- [ ] **Blocking of full factorial designs** — partition a full $2^k$ design into blocks while keeping main effects and interactions estimable
- [ ] **Blocking of response surface designs** — orthogonally block CCC/CCI central composite designs into factorial and axial blocks (currently `ccdesign` has no blocking support)
- [ ] **Mirror-image foldover designs** — augment a resolution III fractional factorial with its mirror image to achieve resolution IV
- [ ] **Alternative foldover designs** — selective foldover on a single factor to break specific alias pairs without running a full mirror image

## Specialized Designs

- [ ] **Small composite designs (Hartley)** — augment a resolution III fractional factorial with star points to fit a quadratic model with fewer runs than a standard CCD; particularly useful for 4–5 factors in a single batch
- [ ] **Supersaturated designs** — designs with more factors than runs; used in screening when only a very small fraction of factors are active; typically constructed to minimize the squared off-diagonal elements of $X^T X$
- [ ] **Definitive Screening Designs (DSD)** — three-level designs introduced by Jones & Nachtsheim (2011) that can estimate all main effects, all quadratic effects, and any two-factor interaction clear of other quadratic effects; require only $2k+1$ runs for $k$ factors
- [ ] **Mirror-image foldover designs** — augment a resolution III fractional factorial with its mirror image to achieve resolution IV

## Space-Filling Design Extensions

- [ ] **Orthogonal Array-based Latin Hypercube (OA-LHD)** — construct Latin hypercube designs whose projection on every pair of factors is an orthogonal array; better two-dimensional uniformity than plain LHS
- [ ] **Sliced Latin Hypercube Design (SLHD)** — partition a Latin hypercube into slices such that each slice is itself a scaled Latin hypercube; useful for computer experiments with qualitative and quantitative factors
- [ ] **Nested Latin Hypercube Design** — construct two or more LHDs such that one is nested inside the other; useful for multi-fidelity simulation experiments
- [ ] **Maximum Projection (MaxPro) Design** — minimize the average reciprocal of squared pairwise distances across all subsets of dimensions; guarantees good projections onto any subset of factors
- [ ] **Nearly Orthogonal Latin Hypercubes (NOLH)** — LHDs constructed to be nearly orthogonal (near-zero pairwise correlations) while remaining space-filling; available via Cioppa & Lucas (2007) tables
- [ ] **Minimax/Maximin distance designs** — minimax: minimize the maximum distance from any point to its nearest design point; maximin: maximize the minimum distance between any two design points

## Low-Discrepancy Sequence Extensions

- [ ] **Faure sequences** — base-$p$ ($p$ prime) low-discrepancy sequences with better uniformity than Halton in higher dimensions; use permuted digit expansions
- [ ] **Hammersley point set** — finite, fixed-size low-discrepancy point set that places one coordinate as $i/n$ and the rest as a Halton sequence; optimal for fixed sample sizes
- [ ] **Niederreiter sequences** — generalization of Faure sequences using formal Laurent series over finite fields; achieve optimal theoretical discrepancy for high dimensions

## Sequential and Adaptive Designs

- [ ] **Sequential DOE / Adaptive designs** — designs that use the results of previous runs to select the next run location; includes Bayesian optimization acquisition functions (EI, UCB, PI) and active learning strategies
- [ ] **Iman-Conover method** — induce target rank correlations among inputs sampled from arbitrary marginal distributions; used in Monte Carlo sensitivity analysis to model correlated uncertain parameters
