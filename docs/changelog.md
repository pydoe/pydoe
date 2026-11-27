# Changelog

All notable changes to PyDOE are documented here.

---

## [**Latest**](https://github.com/pydoe/pydoe/compare/v1.7.0...master)

### :material-plus-circle: Added
- `optimal_design` and the five algorithms (`sequential_dykstra`, `simple_exchange_wynn_mitchell`, `fedorov`, `modified_fedorov`, `detmax`) take the inputs of the C-, V- and T-criteria as keywords: `c_vector` (the linear combination of parameters), `test_points` (the points to predict at) and `model_diff` (the difference between the two models, as values at the candidates or as a function of the points). They could not be passed before, so C always used a vector of ones, V and T scored every design the same and returned the first candidates — [@saudzahirr](https://github.com/saudzahirr)
- `optimal_design` and the five algorithms take `replicates=True` to let a candidate be run more than once, as the published algorithms do. Exact optimal designs often need it: the D-optimal design of a quadratic in one factor with 6 runs has two runs at each of -1, 0 and 1. The default still gives designs of distinct candidates, and asking for more runs than candidates now raises a `ValueError` that says so — [@saudzahirr](https://github.com/saudzahirr)
- `rank1_lattice`, `korobov_sequence` and `generate_candidate_set` take a keyword `seed` for the random generator vector, generator parameter and random candidates, which came from the global random state and could not be reproduced. `sparse_grid_dimension` takes the `grid_type` — [@saudzahirr](https://github.com/saudzahirr)

### :material-wrench: Fixed
- `niederreiter_sequence` is now the Niederreiter sequence in base 2 (Niederreiter, 1988; Bratley, Fox and Niederreiter, 1994). Its generating matrices were Hankel matrices of a shift-register sequence, whose rank is at most the degree of the polynomial: 1024 points took only 4, 8, 8, 16 and 16 distinct values in the first five dimensions. The matrices now come from the Laurent series of $x^k / p(x)^q$ for the irreducible polynomials $x$, $x+1$, $x^2+x+1$, ...; the first dimension is the van der Corput sequence and the first $2^m$ points form a $(t, m, s)$-net with $t = \sum (e_i - 1)$. Every point changes — [@saudzahirr](https://github.com/saudzahirr)
- `doe_sparse_grid` builds Smolyak's sparse grid. It placed points by a heuristic, padded them with arbitrary grid points up to the count of a formula, and ignored `grid_type`, so the three grid types gave the same design and any string was accepted. `'clenshaw_curtis'` is now the equidistant nested grid that the spinterp toolbox calls by that name, `'chebyshev'` the Chebyshev extrema and `'gauss_patterson'` the nested Gauss-Patterson nodes (up to level 5); an unknown type raises a `ValueError`. The points are ordered by level, so a lower level is the first rows of a higher one. `sparse_grid_dimension` counts the points of the construction, where its table stopped at level 7 and returned that count for every higher level; the counts of the default grid up to level 7 are unchanged — [@saudzahirr](https://github.com/saudzahirr)
- `doehlert_shell_design` and `doehlert_simplex_design` return Doehlert's (1970) uniform shell design: the center and $k^2 + k$ points at distance 1 from it, the differences of the vertices of a regular simplex (a hexagon for 2 factors, a cuboctahedron for 3). The shell design only filled its first two columns, so every further factor stayed at 0, and it had $k(k+3)/2$ points instead of $k^2+k$; the simplex design overwrote one coordinate of each simplex vertex, so its points were not at equal distances — [@saudzahirr](https://github.com/saudzahirr)
- `var_regression_matrix` raised `AttributeError` on every call (`np.rank` no longer exists), and its helper `build_regression_matrix` could not run either. Both work now: the model is a string of monomials such as `'1 x1 x2 x1*x2 x1^2'`, with `x1` the first column — [@saudzahirr](https://github.com/saudzahirr)
- `sukharev_grid` accepts every perfect power. It rejected `sukharev_grid(125, 3)` and `sukharev_grid(1000, 3)`, because the floating-point cube roots 4.999... and 9.999... were truncated — [@saudzahirr](https://github.com/saudzahirr)
- `t_optimality` is the criterion of Atkinson and Fedorov (1975), the lack-of-fit sum of squares $d^T (I - P_X) d$ that the model leaves of the rival model's responses. It returned $d^T P_X d$, the part that the model does explain, which is largest for the designs that discriminate the least — [@saudzahirr](https://github.com/saudzahirr)
- `s_optimality` is the criterion of Shin and Xiu (2016), $\sqrt{\det M} / \prod_j \sqrt{M_{jj}}$: between 0 and 1, 1 for orthogonal columns, and independent of the scale of the columns. It used $\det M$ in place of its square root. In a search it is computed without `alpha`, which made a column that the design does not span count as orthogonal — [@saudzahirr](https://github.com/saudzahirr)
- The V-criterion in `criterion_value` and `optimal_design` averages the prediction variance over the candidates when no `test_points` are given. It averaged over the design's own runs, which gives the number of parameters for every design. The T-criterion raises a `ValueError` without a model difference instead of scoring 0 — [@saudzahirr](https://github.com/saudzahirr)
- The optimal-design searches no longer stall on designs that cannot estimate the model. With the D-, E- and S-criteria (D and E at the default `alpha=0`) such designs all scored 0, so the first points were the first candidates in order; they are now ranked by the rank of their model matrix. `modified_fedorov` could also place the same candidate in two runs of a design without replicates — [@saudzahirr](https://github.com/saudzahirr)
- `lhs(criterion="lhsmu")` keeps the spread of the points it selects: each point goes to the stratum of its rank. The strata were assigned through the inverse permutation, which left a valid Latin hypercube with no more spread than a random one. With a `correlation_matrix` the samples now have that correlation; the Cholesky factor was applied transposed, which gave 0.47 and 0.63 for targets of 0.8 and 0.3. Designs with this criterion change — [@saudzahirr](https://github.com/saudzahirr)
- `sobol_sequence` accepts `skip` with the default `use_pow_of_2=True`; it raised unless `skip + n` was a power of 2 — [@saudzahirr](https://github.com/saudzahirr)
- `random_k_means` converts integer `initial_points` to floats; the incremental means were truncated to integers. `scale_samples` does the same for integer samples, whose scaled values were truncated — [@saudzahirr](https://github.com/saudzahirr)
- `GaussianProcessRegressor` returns the posterior standard deviation in the units of the targets: the signal variance of the kernel is the variance of the training targets, where it was fixed at 1. The posterior mean is unchanged; `sequential_design` balances exploration and exploitation in the same way whatever the scale of the objective — [@saudzahirr](https://github.com/saudzahirr)

### :material-file-document: Documentation
- The Users page lists the organizations, laboratories and universities whose public projects depend on PyDOE, with a description of each project and of how it uses PyDOE ([#204](https://github.com/pydoe/pydoe/pull/204)) — [@saudzahirr](https://github.com/saudzahirr)
- The reference pages follow the code again: the examples built on `ff2n` use its current row order, parameter names match the signatures (`halton_sequence`, `rank1_lattice`, `korobov_sequence`, `cranley_patterson_shift`), wrong values are corrected (Taguchi signal-to-noise example, sparse grid point counts), and `scale_samples`, `var_regression_matrix`, the optimality criteria and the algorithm functions have reference entries — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.7.0**](https://github.com/pydoe/pydoe/releases/tag/v1.7.0) <small>2026-11-22</small>

### :material-plus-circle: Added
- `ccdesign` takes a fractional factorial cube through the keyword `generators` (a `fracfact` generator string), and `star` takes the cube's run count through the keyword `n_cube`. The orthogonal and rotatable axial distances use that count instead of $2^n$: for 5 factors on the 16-run half fraction the rotatable distance is now 2, as in Box and Draper (2007) and Montgomery (2012), not the 2.378 of the full factorial. Existing calls are unchanged ([#188](https://github.com/pydoe/pydoe/issues/188), [#189](https://github.com/pydoe/pydoe/pull/189)) — [@kgdunn](https://github.com/kgdunn)

### :material-refresh: Changed
- `pbdesign` builds every multiple of 4 up to 112 runs. It built only 2^e, 12 x 2^e and 20 x 2^e runs, so 28, 36, 44, 52, 56, 60, 68, 72, 76, 84, 88, 92 and 100 runs raised "n must be a multiple of 4". The 24- to 60-run designs are Plackett and Burman's (1946) cyclic and block designs; the other new sizes, and many above 112 runs, use Paley's two constructions, doubling, and, for 92 runs, the Williamson matrices of Baumert, Golomb and Hall (1962). The designs of 12 x 2^e runs above 12 (24, 48, 96, 192, 384, ...) change: they were the 12-run design doubled, in which 11 sets of three columns of the 24-run design have a constant product, and are now Plackett and Burman's cyclic 24- and 48-run designs and their doublings. All other run counts are unchanged ([#192](https://github.com/pydoe/pydoe/issues/192), [#196](https://github.com/pydoe/pydoe/pull/196)) — [@kgdunn](https://github.com/kgdunn)
- `fracfact_by_res` returns, among the designs of the smallest run count, the one of the highest resolution the search finds. The run counts are unchanged; the resolution rises where the same runs allow it: `fracfact_by_res(6, 5)` is now the 2^(6-1)_VI design and `fracfact_by_res(7, 5)` the 2^(7-1)_VII, as in Montgomery (2012, p. 374), and `fracfact_by_res(4, 3)` is the 2^(4-1)_IV ([#194](https://github.com/pydoe/pydoe/issues/194), [#197](https://github.com/pydoe/pydoe/pull/197)) — [@kgdunn](https://github.com/kgdunn)

### :material-wrench: Fixed
- `bbdesign` now returns Box and Behnken's (1960) published designs for 6, 7, 9, 10, 11, 12 and 16 factors: incomplete blocks of 3, 4 or 5 factors, each carrying a two-level factorial (a half fraction for 11 factors). It paired every two factors for any number of factors, which is the published design only for 3 to 5 factors and uses 12.5% to 50% more runs from 6 factors on (84 instead of 56 runs for 7 factors). The 7-factor design is now rotatable, and `bbdesign(6)` has the 54 runs that Table 3.28 of the docs gives. Designs for 3 to 5, 8, and 13 to 15 or more than 16 factors are unchanged, and the docstring now states the default number of center points ([#186](https://github.com/pydoe/pydoe/issues/186), [#190](https://github.com/pydoe/pydoe/pull/190)) — [@kgdunn](https://github.com/kgdunn)
- Orthogonal arrays: `L27(2^1 3^12)` and `L36(3^23)` are renamed `L27(3^13)` and `L36(2^11 3^12)`, the arrays they always held; the former names still work in `get_orthogonal_array` and `taguchi_design`, with a `DeprecationWarning`; `ORTHOGONAL_ARRAYS` and `list_orthogonal_arrays` hold only the new names. `L64(2^31)` had 59 unbalanced pairs of columns and is now the fold-over of `L32(2^31)`, which is balanced and keeps main effects clear of two-factor interactions. Taguchi's standard `L18(2^1 3^7)` is added, built from `L18(6^1 3^6)` ([#193](https://github.com/pydoe/pydoe/issues/193), [#195](https://github.com/pydoe/pydoe/pull/195)) — [@kgdunn](https://github.com/kgdunn)
- `small_composite_design` now builds Hartley's (1959) design for 5 or more factors. Its cube was the smallest resolution III fraction (`fracfact_by_res(n, 3)`), which from 5 factors on aliases two-factor interactions with each other, so the full quadratic model could not be fitted with any number of center runs. The cube is now the smallest regular fraction the search finds (the smallest possible for up to 18 factors) in which no two-factor interaction is aliased with another; for 3, 4, 5, 6, 7 and 9 factors it has 4, 8, 16, 16, 32 and 64 runs, as in Box and Draper (2007, p. 501). Designs for 3 and 4 factors are unchanged ([#187](https://github.com/pydoe/pydoe/issues/187), [#191](https://github.com/pydoe/pydoe/pull/191)) — [@kgdunn](https://github.com/kgdunn)

### :material-file-document: Documentation
- Document `fisher_information` and `jacobian_optimal_design` in the optimal design reference and the README; they were released in v1.6.0 without documentation ([#199](https://github.com/pydoe/pydoe/pull/199)) — [@saudzahirr](https://github.com/saudzahirr)
- Split the changelog into the v1.4.0, v1.5.0 and v1.6.0 releases ([#198](https://github.com/pydoe/pydoe/pull/198)) — [@saudzahirr](https://github.com/saudzahirr)
- Point the Zenodo DOI badge at this repository; it showed the DOI of the `pyDOE3` fork ([#202](https://github.com/pydoe/pydoe/pull/202)) — [@saudzahirr](https://github.com/saudzahirr)

### :material-cog: Infrastructure
- Re-lock `uv.lock` with `requires-python >= 3.11`, to match `pyproject.toml` ([#200](https://github.com/pydoe/pydoe/pull/200)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.6.0**](https://github.com/pydoe/pydoe/releases/tag/v1.6.0) <small>2026-10-21</small>

### :material-plus-circle: Added
- Fisher-information optimal design over Jacobians: `fisher_information` builds the Fisher information matrix of selected rows of a model Jacobian under a given noise covariance, and `jacobian_optimal_design` selects rows (with replicates) that optimize the D, A, E or S criterion by greedy selection and point exchange. A 3D Jacobian averages the information over several parameter-space points for robust designs ([#179](https://github.com/pydoe/pydoe/pull/179)) — [@saudzahirr](https://github.com/saudzahirr)

### :material-wrench: Fixed
- `regularized_inv` inverts with `assume_a="pos"` (Cholesky), so a numerically indefinite information matrix — a positive-semidefinite matrix with a tiny negative eigenvalue from roundoff — is regularized instead of yielding an inverse with a negative trace ([#180](https://github.com/pydoe/pydoe/pull/180)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.5.0**](https://github.com/pydoe/pydoe/releases/tag/v1.5.0) <small>2026-08-20</small>

### :material-wrench: Fixed
- `fracfact_opt` no longer rejects saturated designs. The feasibility check compared the number of erased factors against $\binom{n_{\text{aliases}}}{p}$ instead of against the number of available interaction columns $2^m - m - 1$, so every resolution III design with $k = 2^m - 1$ factors in $2^m$ runs — such as $2^{7-4}_{III}$ and $2^{15-11}_{III}$ — raised *"Too many erased factors to create aliasing"*. `fracfact_opt(n, 0)` also raised `IndexError` instead of returning the full factorial ([#152](https://github.com/pydoe/pydoe/issues/152)) — [@saudzahirr](https://github.com/saudzahirr)
- `fracfact_by_res` now returns the smallest design that actually reaches the requested resolution. It was driven by a hand-written table of base-factor counts and a generator rule that only bounded the length of each generator taken on its own, which had three consequences: `fracfact_by_res(7, 3)` used 16 runs instead of the 8 of the saturated $2^{7-4}_{III}$ design; resolution IV and V requests were over-provisioned by a factor of two throughout; and resolution V requests for 9 or more factors silently returned resolution **IV** designs, because products of generators can be shorter than the generators themselves. Columns are now selected directly against the $\mathrm{GF}(2)^k$ criterion — resolution $\ge R$ iff no $R-1$ or fewer columns sum to zero — so the guarantee covers the whole defining relation. Requests with fewer factors than base factors, such as `fracfact_by_res(4, 5)`, no longer raise from `itertools.islice` ([#153](https://github.com/pydoe/pydoe/issues/153)) — [@saudzahirr](https://github.com/saudzahirr)

### :material-speedometer: Performance
- `fracfact_aliasing` reduces each contrast to the bit pattern of its negative rows, so the elementwise product of a subset of columns becomes a bitwise exclusive or. The alias structure of a 15-factor design is now found in well under a second instead of about a minute ([#152](https://github.com/pydoe/pydoe/issues/152)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.4.0**](https://github.com/pydoe/pydoe/releases/tag/v1.4.0) <small>2026-08-05</small>

### :material-refresh: Changed
- Generalize `definitive_screening_design` with arbitrary continuous-factor counts, two-level categorical factors, orthogonal and interaction-de-aliased methods, minimum-run augmentation, and fake factors while preserving historical one-argument results ([#145](https://github.com/pydoe/pydoe/pull/145)) — [@danieleongari](https://github.com/danieleongari)

### :material-cog: Infrastructure
- Update the lint suppressions to Ruff 0.16 and require explicit preview rules ([#147](https://github.com/pydoe/pydoe/pull/147)) — [@danieleongari](https://github.com/danieleongari)
- Scope the SonarQube Cloud analysis to the package source ([#148](https://github.com/pydoe/pydoe/pull/148)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.3.0**](https://github.com/pydoe/pydoe/releases/tag/v1.3.0) <small>2026-06-10</small>

### :material-plus-circle: Added
- Maximum projection design (`maxpro_design`) — optimizes Latin hypercube projections through coordinate-exchange search — [@saudzahirr](https://github.com/saudzahirr)
- Nearly orthogonal Latin hypercube (`nearly_orthogonal_lhs`) — minimizes correlation while retaining Latin hypercube stratification — [@saudzahirr](https://github.com/saudzahirr)
- Maximin and minimax distance designs (`maximin_design`, `minimax_design`) — spread points by optimizing pairwise or covering distances — [@saudzahirr](https://github.com/saudzahirr)
- Faure and Niederreiter low-discrepancy sequences (`faure_sequence`, `niederreiter_sequence`) — deterministic space-filling sequences for quasi-Monte Carlo sampling — [@saudzahirr](https://github.com/saudzahirr)
- Sequential Bayesian-optimization designs (`sequential_design`) with Gaussian-process regression and expected-improvement, probability-improvement, and upper-confidence-bound acquisition functions — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.2.0**](https://github.com/pydoe/pydoe/releases/tag/v1.2.0) <small>2026-06-10</small>

### :material-plus-circle: Added
- Latin square (`latin_square`), Graeco-Latin square (`graeco_latin_square`), and hyper-Graeco-Latin square (`hyper_graeco_latin_square`) designs — remove the effect of two, three, or more nuisance factors using mutually orthogonal Latin squares — [@saudzahirr](https://github.com/saudzahirr)
- Hammersley point set (`hammersley_sequence`) — finite, fixed-size low-discrepancy point set with one equispaced coordinate and the remaining coordinates from the Halton sequence — [@saudzahirr](https://github.com/saudzahirr)
- Iman-Conover method (`iman_conover`) — induces a target rank correlation structure among sampled variables while preserving their marginal distributions — [@saudzahirr](https://github.com/saudzahirr)
- Mixture axial (screening) design (`mixture_axial_design`) — places one point at the simplex centroid and one axial point per component for screening blending effects — [@saudzahirr](https://github.com/saudzahirr)
- Extreme-vertices design (`extreme_vertices_design`) — enumerates the vertices of a constrained mixture region defined by per-component lower/upper bounds — [@saudzahirr](https://github.com/saudzahirr)
- Mixture-process variable design (`mixture_process_design`) — crosses a mixture design with an independent process-variable design — [@saudzahirr](https://github.com/saudzahirr)
- Blocking of full factorial designs (`block_full_factorial`) — splits a $2^k$ factorial into $2^p$ blocks by confounding chosen interactions with block effects — [@saudzahirr](https://github.com/saudzahirr)
- Orthogonally-blocked central composite design (`block_ccdesign`) — splits a CCD into a factorial block and an axial block with `alpha` chosen for orthogonal blocking — [@saudzahirr](https://github.com/saudzahirr)
- Hartley's small composite design (`small_composite_design`) — augments a resolution-III fractional factorial with star points, requiring fewer runs than a standard CCD — [@saudzahirr](https://github.com/saudzahirr)
- Definitive screening design (`definitive_screening_design`) — three-level Jones-Nachtsheim design requiring only $2k+1$ runs, built from a Paley conference matrix and its fold-over — [@saudzahirr](https://github.com/saudzahirr)
- Supersaturated design (`supersaturated_design`) — random-search construction of $k > n$ two-level designs minimizing $E(s^2)$ for screening under effect sparsity — [@saudzahirr](https://github.com/saudzahirr)
- Nested Latin hypercube (`nested_lhs`) — constructs nested designs for multi-fidelity experiments — [@saudzahirr](https://github.com/saudzahirr)
- Orthogonal array-based Latin hypercube design (`oa_lhd`) — Tang's (1993) construction turning a symmetric orthogonal array into a Latin hypercube with improved two-dimensional uniformity — [@saudzahirr](https://github.com/saudzahirr)
- Sliced Latin hypercube design (`sliced_lhs`) — partitions an $N=mt$-point Latin hypercube into $t$ slices of $m$ points, each a Latin hypercube in its own right — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.1.0**](https://github.com/pydoe/pydoe/releases/tag/v1.1.0) <small>2026-06-09</small>

### :material-plus-circle: Added
- Simplex-lattice design (`simplex_lattice_design`) — mixture experiment design placing lattice points on the *q*-component simplex at resolution 1/*m*; supports fitting Scheffé polynomial models of degree *m* — [@saudzahirr](https://github.com/saudzahirr)
- Simplex-centroid design (`simplex_centroid_design`) — mixture experiment design with the centroids of all $2^q - 1$ non-empty subsets; supports estimation of all Scheffé interaction blending coefficients — [@saudzahirr](https://github.com/saudzahirr)
- John's 3/4 fractional factorial design (`john_three_quarter_design`) — semifoldover design using exactly 3/4 of the runs of the next full $2^k$ design; de-aliases all two-factor interactions involving the chosen factor — [@saudzahirr](https://github.com/saudzahirr)
- `pydoe --debug` prints the versions of PyDOE, Python and the dependencies for bug reports, and the repository has a bug report issue template ([#120](https://github.com/pydoe/pydoe/pull/120)) — [@laraibg786](https://github.com/laraibg786)

### :material-wrench: Fixed
- Eliminate 604 test warnings by correctly catching `scipy.linalg.LinAlgWarning` in `regularized_inv`; suppress scipy Sobol advisory in the Saltelli path — [@saudzahirr](https://github.com/saudzahirr)
- Tests no longer hide failed assertions inside `try`/`except` blocks ([#121](https://github.com/pydoe/pydoe/pull/121)) — [@laraibg786](https://github.com/laraibg786)

### :material-file-document: Documentation
- Fix contributing docs to reference `zensical` instead of `mkdocs serve` — [@saudzahirr](https://github.com/saudzahirr)
- Add `Mixture Designs` reference page — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.0.2**](https://github.com/pydoe/pydoe/releases/tag/v1.0.2) <small>2026-05-17</small>

### :material-plus-circle: Added
- Add theory documentation pages ([#114](https://github.com/pydoe/pydoe/pull/114)) — [@saudzahirr](https://github.com/saudzahirr)

### :material-wrench: Fixed
- Fix typo in `factorial.md` ([#111](https://github.com/pydoe/pydoe/pull/111)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.0.1**](https://github.com/pydoe/pydoe/releases/tag/v1.0.1) <small>2026-05-05</small>

Patch release following the 1.0.0 stable release. — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v1.0.0**](https://github.com/pydoe/pydoe/releases/tag/v1.0.0) <small>2026-05-05</small>

:tada: **First stable release.** No breaking changes from 0.9.9.

---

## [**v0.9.9**](https://github.com/pydoe/pydoe/releases/tag/v0.9.9) <small>2026-04-07</small>

### :material-file-document: Documentation
- Migrate documentation tooling from MkDocs to Zensical ([#71](https://github.com/pydoe/pydoe/pull/71)) — [@saudzahirr](https://github.com/saudzahirr)
- Update copyright information ([#92](https://github.com/pydoe/pydoe/pull/92)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.9.8**](https://github.com/pydoe/pydoe/releases/tag/v0.9.8) <small>2026-03-31</small>

### :material-wrench: Fixed
- Fix unexpected number of runs generated for fractional factorial designs ([#89](https://github.com/pydoe/pydoe/pull/89)) — [@Noor-Mustafa123](https://github.com/Noor-Mustafa123)

### :material-file-document: Documentation
- Format and clean up documentation ([#78](https://github.com/pydoe/pydoe/pull/78)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.9.7**](https://github.com/pydoe/pydoe/releases/tag/v0.9.7) <small>2026-02-21</small>

### :material-plus-circle: Added
- Compatibility shim for legacy `pyDOE` import paths ([#70](https://github.com/pydoe/pydoe/pull/70)) — [@laraibg786](https://github.com/laraibg786)

---

## [**v0.9.6**](https://github.com/pydoe/pydoe/releases/tag/v0.9.6) <small>2026-02-16</small>

### :material-refresh: Changed
- Restructure codebase into modular package layout ([#63](https://github.com/pydoe/pydoe/pull/63)) — [@laraibg786](https://github.com/laraibg786)
- Rename modules to `snake_case` to comply with PEP 8 ([#62](https://github.com/pydoe/pydoe/pull/62)) — [@saudzahirr](https://github.com/saudzahirr)

### :material-wrench: Fixed
- Use `np.isclose` for logical float comparison in `pbdesign` ([#65](https://github.com/pydoe/pydoe/pull/65)) — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.9.5**](https://github.com/pydoe/pydoe/releases/tag/v0.9.5) <small>2026-02-11</small>

### :material-refresh: Changed
- Refresh documentation badges and `project.urls` ([#59](https://github.com/pydoe/pydoe/pull/59)) — [@saudzahirr](https://github.com/saudzahirr)

### :material-wrench: Fixed
- Fix the smoke test that runs after the package is published ([#60](https://github.com/pydoe/pydoe/pull/60)) — [@laraibg786](https://github.com/laraibg786)

---

## [**v0.9.4**](https://github.com/pydoe/pydoe/releases/tag/v0.9.4) <small>2026-02-10</small>

:rocket: **First public PyPI release.**

### :material-plus-circle: Added
- Factorial designs resolution table in documentation ([#54](https://github.com/pydoe/pydoe/pull/54)) — [@saudzahirr](https://github.com/saudzahirr)
- Type annotations throughout the codebase ([#49](https://github.com/pydoe/pydoe/pull/49)) — [@saudzahirr](https://github.com/saudzahirr)
- Ruff as default linter and formatter with Codecov integration ([#47](https://github.com/pydoe/pydoe/pull/47)) — [@saudzahirr](https://github.com/saudzahirr)
- PyPI release workflow ([#57](https://github.com/pydoe/pydoe/pull/57)) — [@laraibg786](https://github.com/laraibg786)
- `uv` as package manager with updated `pyproject.toml` ([#40](https://github.com/pydoe/pydoe/pull/40)) — [@laraibg786](https://github.com/laraibg786)
- Dynamic versioning without a `_version` file ([#38](https://github.com/pydoe/pydoe/pull/38)) — [@laraibg786](https://github.com/laraibg786)
- Documentation site on MkDocs, migrated from Sphinx ([#41](https://github.com/pydoe/pydoe/pull/41)) — [@laraibg786](https://github.com/laraibg786)
- Reusable build and test workflows with a Python version matrix, and Dependabot for the Python dependencies ([#39](https://github.com/pydoe/pydoe/pull/39), [#50](https://github.com/pydoe/pydoe/pull/50), [#56](https://github.com/pydoe/pydoe/pull/56)) — [@laraibg786](https://github.com/laraibg786)

### :material-wrench: Fixed
- Buggy resolution values in fractional factorial designs ([#52](https://github.com/pydoe/pydoe/pull/52)) — [@Noor-Mustafa123](https://github.com/Noor-Mustafa123)
- `lhsmu` `TypeError` when using NumPy `Generator` API ([#44](https://github.com/pydoe/pydoe/pull/44)) — [@saudzahirr](https://github.com/saudzahirr)
- Negative determinant bug in `d_efficiency`, with Python 3.14 added to the test matrix ([#42](https://github.com/pydoe/pydoe/pull/42)) — [@relf](https://github.com/relf)
- Singular information matrix handling — [@saudzahirr](https://github.com/saudzahirr)
- Improve RAM usage in `_lhsclassic` ([#43](https://github.com/pydoe/pydoe/pull/43)) — [@dargen3](https://github.com/dargen3)

---

## [**v0.9.3**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.9.3) <small>2026-01-29</small>

### :material-plus-circle: Added
- Type annotations throughout the codebase — [@saudzahirr](https://github.com/saudzahirr)
- Ruff as linter and formatter with Codecov integration — [@saudzahirr](https://github.com/saudzahirr)

### :material-file-document: Documentation
- Update and deploy documentation — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.9.2**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.9.2) <small>2026-01-07</small>

### :material-plus-circle: Added
- Migrate documentation site from Sphinx to MkDocs — [@laraibg786](https://github.com/laraibg786)
- Integrate `uv` as package manager — [@laraibg786](https://github.com/laraibg786)
- Dynamic versioning without a `_version` file — [@laraibg786](https://github.com/laraibg786)

### :material-wrench: Fixed
- Fix `lhsmu` `TypeError` when using NumPy `Generator` API — [@saudzahirr](https://github.com/saudzahirr)
- Fix negative determinant bug in `d_efficiency` — [@relf](https://github.com/relf)
- Improve RAM usage in `_lhsclassic` — [@dargen3](https://github.com/dargen3)

---

## [**v0.9.1**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.9.1) <small>2025-11-27</small>

### :material-wrench: Fixed
- Fix singular information matrix handling — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.9.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.9.0) <small>2025-11-05</small>

### :material-plus-circle: Added
- Add `doe_sparse_grid` using Smolyak's sparse grid construction — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.8.1**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.8.1) <small>2025-10-27</small>

### :material-refresh: Changed
- Replace legacy NumPy `RandomState` with `Generator` API throughout — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.8.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.8.0) <small>2025-10-24</small>

### :material-plus-circle: Added
- Add `morris_sampling` for Morris one-at-a-time sensitivity screening — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)
- Add `saltelli_sampling` for variance-based Sobol' sensitivity analysis — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)
- Add `random_uniform` and `random_k_means` space-filling designs — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)
- Deprecate `random_state` parameter in `lhs` in favour of `seed` — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)

---

## [**v0.7.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.7.0) <small>2025-09-09</small>

### :material-plus-circle: Added
- Add `halton_sequence`, `sobol_sequence`, `korobov_sequence`, `rank1_lattice`, and `sukharev_grid` — [@saudzahirr](https://github.com/saudzahirr)
- Add `cranley_patterson_shift` for randomising quasi-random sequences — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.6.2**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.6.2) <small>2025-09-02</small>

### :material-plus-circle: Added
- Add `optimal_design` with D, A, E, G, I, V, C, S, T optimality criteria — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)
- Add Fedorov, modified Fedorov, DETMAX, and Dykstra algorithms — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)

---

## [**v0.6.1**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.6.1) <small>2025-07-08</small>

### :material-plus-circle: Added
- Add `doehlert_shell_design` and `doehlert_simplex_design` — [@saudzahirr](https://github.com/saudzahirr), [@relf](https://github.com/relf)

---

## [**v0.6.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.6.0) <small>2025-07-03</small>

### :material-plus-circle: Added
- Add `taguchi_design` with orthogonal array lookup, SNR computation, and `TaguchiObjective` enum — [@saudzahirr](https://github.com/saudzahirr)

---

## [**v0.5.5**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.5.5) <small>2025-05-16</small>

### :material-wrench: Fixed
- Update `gsd` to accept level count of 1 — [@mutricyl](https://github.com/mutricyl), [@relf](https://github.com/relf)

---

## [**v0.5.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.5.0) <small>2023-10-25</small>

### :material-cog: Infrastructure
- Migrate build system to `pyproject.toml` with Hatchling, versions from VCS tags and automated PyPI releases — [@ovidner](https://github.com/ovidner), [@relf](https://github.com/relf)
- Add full test suite and CI automation — [@relf](https://github.com/relf), Antoine Averland

### :material-wrench: Fixed
- Replace Black with Ruff; fix `fracfact_opt` for Python 3; add doc-tests — [@relf](https://github.com/relf)
- Refactor `fracfact` with test updates and minor bug fixes — [@relf](https://github.com/relf), Hiroaki Imoto

---

## [**v0.4.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.4.0) <small>2021-03-03</small>

### :material-plus-circle: Added
- Add `gsd` (Generalized Subset Design), with `fracfact_by_res`, `fracfact_opt` and `fracfact_aliasing` — [@RickardSjogren](https://github.com/RickardSjogren), with contributions from [@ovidner](https://github.com/ovidner), [@beckermr](https://github.com/beckermr), Daniel Svensson, Julien Schueller, Eduardo Valle, andife, rockandsalt, Andrei and Todd

---

## [**v0.3.9**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.9) <small>2017-04-25</small>

### :material-wrench: Fixed
- Fix integer division for Python 3 compatibility — [@joergdietrich](https://github.com/joergdietrich)

---

## [**v0.3.8**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.8) <small>2015-07-13</small>

### :material-wrench: Fixed
- Fix incorrect indexing variable in `_pdist` — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.7**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.7) <small>2014-12-09</small>

### :material-refresh: Changed
- Clarify BSD 3-clause license — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.6**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.6) <small>2014-09-22</small>

### :material-refresh: Changed
- Add code credits to original authors — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.5**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.5) <small>2014-02-18</small>

### :material-plus-circle: Added
- Add `var_regression_matrix` to public API — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.4**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.4) <small>2014-02-18</small>

### :material-wrench: Fixed
- Fix Python 3 import and compatibility issues — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.3**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.3) <small>2014-02-12</small>

### :material-wrench: Fixed
- Remove package import for better Python 3 compatibility — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.2**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.2) <small>2014-02-09</small>

### :material-wrench: Fixed
- Fix indexing problem; improve Python 3 compatibility — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.1**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.1) <small>2014-02-09</small>

### :material-wrench: Fixed
- Fix indexing issue — [@tisimst](https://github.com/tisimst)

---

## [**v0.3.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.3.0) <small>2013-11-08</small>

### :material-refresh: Changed
- Simplify design function inputs to accept number of factors directly — [@tisimst](https://github.com/tisimst)
- Improve consistency across all design functions — [@tisimst](https://github.com/tisimst)

---

## [**v0.2.2**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.2.2) <small>2013-10-23</small>

### :material-plus-circle: Added
- Add `criterion` keyword argument to `lhs` for more flexible sampling — [@tisimst](https://github.com/tisimst)

---

## [**v0.2.1**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.2.1) <small>2013-09-13</small>

### :material-wrench: Fixed
- Fix syntax errors and update documentation links — [@tisimst](https://github.com/tisimst)

---

## [**v0.2.0**](https://github.com/pydoe/pydoe-archive/releases/tag/v0.2.0) <small>2013-09-13</small>

### :material-plus-circle: Added
- Add response surface designs (`bbdesign`, `ccdesign`) — [@tisimst](https://github.com/tisimst)
- Add Latin hypercube sampling (`lhs`) — [@tisimst](https://github.com/tisimst)

---

## [**0.1.alpha**](https://github.com/pydoe/pydoe-archive/releases/tag/0.1.alpha) <small>2013-09-05</small>

:seedling: **Initial release** with `fullfact`, `ff2n`, `fracfact`, `pbdesign`, and `gsd`. — [@tisimst](https://github.com/tisimst)
