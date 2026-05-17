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

- [ ] **John's 3/4 fractional factorial designs** — semifoldover designs that use only ¾ of the runs of the next regular $2^k$ design; useful when a full foldover is too expensive but full aliasing resolution is needed
- [ ] **Small composite designs (Hartley)** — augment a resolution III fractional factorial with star points to fit a quadratic model with fewer runs than a standard CCD; particularly useful for 4–5 factors in a single batch
