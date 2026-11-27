In this section, the following kinds of *randomized designs* will
be described:

- Latin-Hypercube
- Orthogonal Array-based Latin Hypercube
- Sliced Latin Hypercube
- Nested Latin Hypercube
- Maximin Distance Design
- Minimax Distance Design
- Maximum Projection (MaxPro) Design
- Nearly Orthogonal Latin Hypercube
- Random K-Means
- Random Uniform
- Scaling Samples to Bounds

!!! hint
    All available designs can be accessed after a simple import statement:

    ```pycon
    >>> from pydoe import (
    ...     lhs,
    ...     oa_lhd,
    ...     random_k_means,
    ...     random_uniform,
    ...     sliced_lhs,
    ...     nested_lhs,
    ...     maximin_design,
    ...     minimax_design,
    ...     maxpro_design,
    ...     nearly_orthogonal_lhs,
    ...     scale_samples,
    ... )
    ```

## Latin-Hypercube (`lhs`) {#latin-hypercube}

![Latin-hypercube design](../assets/images/lhs.png)

Latin-hypercube designs can be created using the following simple syntax:

```python
lhs(n, [samples, criterion, iterations, random_state, correlation_matrix, seed])
```

where

* **n**: an integer that designates the number of factors (required)
* **samples**: an integer that designates the number of sample points to
  generate for each factor (default: n)
* **criterion**: a string that tells `lhs` how to sample the points
  (default: None, which simply randomizes the points within the intervals):

  - "center" or "c": center the points within the sampling intervals
  - "maximin" or "m": maximize the minimum distance between points, but
    place the point in a randomized location within its interval
  - "centermaximin" or "cm": same as "maximin", but centered within the
    intervals
  - "correlation" or "corr": minimize the maximum correlation coefficient
  - "lhsmu" : Latin hypercube with multifimensional Uniformity. Correlation between
     variable can be enforced by setting a valid correlation matrix. Description of the
     algorithm can be found in [*Latin hypercube sampling with multidimensional uniformity*](https://doi.org/10.1016/j.jspi.2011.09.016).

* **iterations**: an integer giving the number of iterations of the
  "maximin", "centermaximin" and "correlation" algorithms (default: 5)
* **correlation_matrix**: a square array with the correlation to enforce
  between the factors; only used by the "lhsmu" criterion (default: None)
* **seed**: an integer or `np.random.Generator` that controls the random
  draws, for reproducible designs (default: None)
* **random_state**: deprecated; an integer or `np.random.RandomState`.
  Passing it emits a `DeprecationWarning`. Use `seed` instead.

The output design scales all the variable ranges from zero to one which
can then be transformed as the user wishes (like to a specific statistical
distribution using the [`scipy.stats.distributions`](http://docs.scipy.org/doc/scipy/reference/stats.html) `ppf` (inverse
cumulative distribution) function. An example of this is [shown below](#statistical_distribution_usage).

For example, if I wanted to transform the uniform distribution of 5 samples
to a normal distribution (mean=0, standard deviation=1), I would do
something like:

```pycon
>>> from scipy.stats.distributions import norm
>>> lhd = lhs(2, samples=5)
>>> lhd = norm(loc=0, scale=1).ppf(lhd)  # (1)!
```

1. this applies to both factors here

Graphically, each transformation would look like the following, going
from the blue sampled points (from using `lhs`) to the green
sampled points that are normally distributed:

![Custom distribution transformation](../assets/images/lhs_custom_distribution.png)

### Examples

A basic 4-factor latin-hypercube design:

```pycon
>>> lhs(4, criterion="center", seed=42)
array([[0.375, 0.625, 0.125, 0.625],
       [0.125, 0.375, 0.375, 0.875],
       [0.875, 0.875, 0.625, 0.125],
       [0.625, 0.125, 0.875, 0.375]])
```

Let's say we want more samples, like 10:

```pycon
>>> lhs(4, samples=10, criterion="center", seed=42)
array([[0.95, 0.75, 0.45, 0.05],
       [0.35, 0.35, 0.55, 0.15],
       [0.05, 0.45, 0.25, 0.85],
       [0.25, 0.25, 0.05, 0.55],
       [0.85, 0.85, 0.65, 0.25],
       [0.65, 0.95, 0.85, 0.35],
       [0.55, 0.15, 0.95, 0.45],
       [0.75, 0.05, 0.15, 0.95],
       [0.45, 0.65, 0.35, 0.75],
       [0.15, 0.55, 0.75, 0.65]])
```

### Customizing with Statistical Distributions {#statistical_distribution_usage}

Now, let's say we want to transform these designs to be normally
distributed with means = `[1, 2, 3, 4]` and standard deviations = `[0.1, 0.5, 1, 0.25]`:

```python
>>> design = lhs(4, samples=10, seed=42)
>>> from scipy.stats.distributions import norm
>>> means = [1, 2, 3, 4]
>>> stdvs = [0.1, 0.5, 1, 0.25]
>>> for i in range(4):
...     design[:, i] = norm(loc=means[i], scale=stdvs[i]).ppf(design[:, i])
...
>>> design
array([[1.13594132, 2.36663792, 2.95678009, 3.63056147],
       [0.96532419, 1.8502459 , 3.24576985, 3.76982777],
       [0.85771899, 1.88156874, 2.28427246, 4.22784   ],
       [0.92032956, 1.65490697, 1.63330072, 4.05644396],
       [1.09644209, 2.49119469, 3.37635123, 3.86360439],
       [1.04616626, 2.81087004, 4.02346331, 3.88497615],
       [1.01911827, 1.57481955, 4.42340726, 3.9768851 ],
       [1.05693154, 1.14637525, 2.0697235 , 4.45954277],
       [0.9888118 , 2.15203651, 2.59935681, 4.20751801],
       [0.87703694, 2.04449189, 3.75366972, 4.06617543]])
```

!!! note
    Methods for "space-filling" designs and "orthogonal" designs are in the works, so stay tuned! However, simply increasing the samples reduces the need for these anyway.

## Orthogonal Array-based Latin Hypercube (`oa_lhd`) {#orthogonal-array-based-latin-hypercube}

`oa_lhd` builds a Latin hypercube design from a symmetric orthogonal
array using Tang's (1993) construction. Each column of the result is a
permutation of all `N` cell midpoints, jittered within the cell, while
respecting the level structure of the orthogonal array. This gives
better two-dimensional uniformity than a plain random Latin hypercube.

```pycon
>>> oa_lhd(oa, [seed])
```

where

* **oa**: a 2D array-like `OA(N, k, s, 2)` with integer levels
  `0, ..., s - 1`, each level appearing exactly `N / s` times in every
  column (e.g. from [`get_orthogonal_array`](taguchi.md))
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

The output design scales to the unit hypercube $[0, 1)^k$ with `N`
cells.

### Examples

```pycon
>>> from pydoe import get_orthogonal_array, oa_lhd
>>> oa = get_orthogonal_array("L9(3^4)")
>>> oa_lhd(oa, seed=0)
array([[0.31813099, 0.17127347, 0.03330132, 0.26918747],
       [0.00314663, 0.34714259, 0.63006938, 0.40524328],
       [0.17948723, 0.70929751, 0.88857888, 0.77564837],
       [0.63172689, 0.29449548, 0.52093853, 0.82099127],
       [0.45945517, 0.63572093, 0.94726159, 0.14558243],
       [0.38731504, 0.98772087, 0.32600484, 0.59531058],
       [0.9523922 , 0.03576327, 0.7327    , 0.48199014],
       [0.71017989, 0.54336382, 0.13635084, 0.9581319 ],
       [0.78711282, 0.87029379, 0.4207887 , 0.0265966 ]])
```

## Sliced Latin Hypercube (`sliced_lhs`) {#sliced-latin-hypercube}

`sliced_lhs` partitions an $N = mt$-point Latin hypercube design into
`t` slices of `m` points each, such that the full design is a Latin
hypercube over `N` cells *and* every individual slice, once rescaled
to its own unit hypercube, is itself a Latin hypercube over `m` cells.
This is useful for computer experiments that mix qualitative levels
(one per slice) with quantitative factors.

```pycon
>>> sliced_lhs(n_factors, m, t, [seed])
```

where

* **n_factors**: an integer that designates the number of factors
  (required, must be at least 1)
* **m**: an integer that designates the number of points per slice
  (required, must be at least 1)
* **t**: an integer that designates the number of slices (required,
  must be at least 1)
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

`sliced_lhs` returns a tuple `(design, slices)` where `design` is an
`(m * t, n_factors)` array in $[0, 1)^\text{n\_factors}$ and `slices`
is a length-`m * t` array of slice labels `0, ..., t - 1`.

### Examples

```pycon
>>> from pydoe import sliced_lhs
>>> design, slices = sliced_lhs(2, 3, 2, seed=0)
>>> design
array([[0.4344393 , 0.45491609],
       [0.09060417, 0.1558454 ],
       [0.30264226, 0.16712308],
       [0.97623405, 0.67226426],
       [0.78827591, 0.86260927],
       [0.64386315, 0.59024354]])
>>> slices
array([0, 0, 0, 1, 1, 1])
```

## Nested Latin Hypercube (`nested_lhs`) {#nested-latin-hypercube}

`nested_lhs` constructs two Latin hypercube designs, a "small" design
with $n_1$ points and a "large" design with $n_2 = n_1 k$ points, such
that the small design is nested within the large one: every cell of the
small design corresponds to a contiguous block of $k$ cells in the large
design. This is useful for multi-fidelity computer experiments, where the
small design is run on an expensive high-fidelity simulator and the large
design on a cheaper low-fidelity simulator.

```pycon
>>> nested_lhs(n_factors, n1, k, [seed])
```

where

* **n_factors**: an integer that designates the number of factors
  (required, must be at least 1)
* **n1**: an integer that designates the number of points in the small
  design (required, must be at least 1)
* **k**: an integer that designates the ratio of large to small design
  size (required, must be at least 1)
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

`nested_lhs` returns a tuple `(small_design, large_design)` where
`small_design` has shape `(n1, n_factors)` and `large_design` has shape
`(n1 * k, n_factors)`, both in $[0, 1)^\text{n\_factors}$.

### Examples

```pycon
>>> from pydoe import nested_lhs
>>> small, large = nested_lhs(2, 3, 2, seed=0)
>>> small
array([[0.86887859, 0.24316552],
       [0.18120833, 0.64502414],
       [0.60528452, 0.6675795 ]])
>>> large
array([[0.97623405, 0.17226426],
       [0.78827591, 0.02927594],
       [0.14386315, 0.59024354],
       [0.21661865, 0.4037812 ],
       [0.33805328, 0.68738055],
       [0.61177074, 0.94119825]])
```

## Maximin Distance Design (`maximin_design`) {#maximin-design}

`maximin_design` constructs a Latin hypercube design optimized via
coordinate-exchange local search to maximize the minimum pairwise
Euclidean distance between design points. Maximin designs spread points
as far apart as possible, which is desirable for space-filling computer
experiments.

```python
maximin_design(n_points, n_factors, *, iterations=200, seed=None)
```

where

* **n_points**: an integer that designates the number of points
  (required, must be at least 2)
* **n_factors**: an integer that designates the number of factors
  (required, must be at least 1)
* **iterations**: an integer giving the number of local-search swaps to
  attempt (default: 200, must be at least 0)
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

### Examples

```pycon
>>> from pydoe import maximin_design
>>> maximin_design(5, 2, iterations=50, seed=0)
array([[0.5, 0.9],
       [0.9, 0.3],
       [0.7, 0.5],
       [0.1, 0.1],
       [0.3, 0.7]])
```

## Minimax Distance Design (`minimax_design`) {#minimax-design}

`minimax_design` selects `n_points` points from a large random candidate
set so as to minimize the maximum distance from any point in the
candidate set to its nearest selected design point (a k-center / facility
location criterion), refined via swap-based local search.

```python
minimax_design(n_points, n_factors, *, n_candidates=1000,
               iterations=200, seed=None)
```

where

* **n_points**: an integer that designates the number of points to
  select (required, must be at least 1)
* **n_factors**: an integer that designates the number of factors
  (required, must be at least 1)
* **n_candidates**: an integer that designates the size of the random
  candidate pool (default: 1000, must be at least `n_points`)
* **iterations**: an integer giving the number of local-search swaps to
  attempt (default: 200, must be at least 0)
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

### Examples

```pycon
>>> from pydoe import minimax_design
>>> minimax_design(4, 2, n_candidates=200, iterations=50, seed=0)
array([[0.23231148, 0.74875573],
       [0.81812097, 0.62650646],
       [0.33611706, 0.15027947],
       [0.94367777, 0.19929834]])
```

## Maximum Projection Design (`maxpro_design`) {#maxpro-design}

`maxpro_design` constructs a Latin hypercube design optimized via
coordinate-exchange local search to minimize the MaxPro criterion
$\psi = \sum_{i<j} \prod_{k=1}^{p} (x_{ik} - x_{jk})^{-2}$, which
guarantees good space-filling properties in every projection onto a
subset of factors.

```python
maxpro_design(n_points, n_factors, *, iterations=200, seed=None)
```

where

* **n_points**: an integer that designates the number of points
  (required, must be at least 2)
* **n_factors**: an integer that designates the number of factors
  (required, must be at least 1)
* **iterations**: an integer giving the number of local-search swaps to
  attempt (default: 200, must be at least 0)
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

### Examples

```pycon
>>> from pydoe import maxpro_design
>>> maxpro_design(5, 2, iterations=50, seed=0)
array([[0.3, 0.9],
       [0.9, 0.3],
       [0.7, 0.7],
       [0.5, 0.1],
       [0.1, 0.5]])
```

## Nearly Orthogonal Latin Hypercube (`nearly_orthogonal_lhs`) {#nearly-orthogonal-lhs}

`nearly_orthogonal_lhs` constructs a Latin hypercube design optimized via
coordinate-exchange local search to minimize the maximum absolute pairwise
Pearson correlation between columns. This reduces confounding between
factor effect estimates compared to a plain random Latin hypercube.

```python
nearly_orthogonal_lhs(n_points, n_factors, *, iterations=200, seed=None)
```

where

* **n_points**: an integer that designates the number of points
  (required, must be at least 2)
* **n_factors**: an integer that designates the number of factors
  (required, must be at least 1)
* **iterations**: an integer giving the number of local-search swaps to
  attempt (default: 200, must be at least 0)
* **seed**: an integer or `np.random.Generator` for reproducibility
  (default: `None`)

### Examples

```pycon
>>> from pydoe import nearly_orthogonal_lhs
>>> nearly_orthogonal_lhs(8, 3, iterations=100, seed=0)
array([[0.8125, 0.5625, 0.4375],
       [0.5625, 0.3125, 0.5625],
       [0.4375, 0.1875, 0.1875],
       [0.3125, 0.6875, 0.9375],
       [0.6875, 0.8125, 0.8125],
       [0.0625, 0.9375, 0.0625],
       [0.1875, 0.0625, 0.6875],
       [0.9375, 0.4375, 0.3125]])
```

!!! note
    This is an optimization-based construction that directly minimizes
    pairwise column correlation, rather than the tabulated designs of
    Cioppa, T. M., & Lucas, T. W. (2007). "Efficient nearly orthogonal
    and space-filling Latin hypercubes." *Technometrics*, 49(1), 45-55.

## Random K-Means (`random_k_means`) {#random-k-means}

Random K-Means generates cluster centers using MacQueen's K-Means algorithm.
This method creates well-distributed points in the unit hypercube by iteratively
updating cluster centers based on randomly sampled points.

Random K-Means designs can be created using the following syntax:

```python
random_k_means(
    num_points,
    dimension,
    [num_steps, initial_points, callback, random_state, seed],
)
```

where

* `num_points`: an integer that designates the number of cluster centers to generate (required)
* `dimension`: an integer that designates the dimensionality of the space (required)
* `num_steps`: an integer that designates the number of iterations (default: 100 * num_points)
* `initial_points`: an array of shape `(num_points, dimension)` with the initial cluster centers, all in $[0, 1]$ (default: None, which uses random points)
* `callback`: a callable function called at each step with current cluster centers (default: None)
* `seed`: an integer or `np.random.Generator` for reproducibility (default: None)
* `random_state`: deprecated; passing it emits a `DeprecationWarning`. Use `seed` instead

At each step one point is drawn uniformly in the unit hypercube, and the
nearest cluster center is moved to the mean of itself and all the points
assigned to it so far (MacQueen's update).


The output design contains cluster centers that are well-distributed across the
unit hypercube $[0, 1]^\text{dimension}$.

### Examples

A basic 3-point, 2-dimensional Random K-Means design:

```python
>>> random_k_means(3, 2, seed=42)
array([[0.50957531, 0.22400726],
       [0.78810092, 0.70678097],
       [0.20686406, 0.65349212]])
```

With custom initial points:

```python
>>> initial = [[0.1, 0.1], [0.5, 0.5], [0.9, 0.9]]
>>> random_k_means(3, 2, initial_points=initial, num_steps=50, seed=42)
array([[0.4360224 , 0.21207178],
       [0.2761386 , 0.64799756],
       [0.74605502, 0.70867558]])
```

## Random Uniform (`random_uniform`) {#random-uniform}

Random Uniform generates random samples from a uniform distribution over the
half-open interval [0, 1). The samples are drawn from
`numpy.random.default_rng(seed)`, through an interface consistent with
the other PyDOE functions.

Random Uniform designs can be created using the following syntax:

```python
>>> random_uniform(num_points, dimension, seed=None)
```

where

* **num_points**: an integer that designates the number of random points to generate (required)
* **dimension**: an integer that designates the dimensionality of each point (required)
* **seed**: an integer or `np.random.Generator` for reproducibility (default: None)

!!! note
    `random_uniform` has its own generator, so the legacy global seed
    `np.random.seed(...)` has no effect on it. Pass `seed` to get
    reproducible points.

The output design contains completely random points uniformly distributed in
the unit hypercube $[0, 1)^\text{dimension}$.

### Examples

A basic 5-point, 3-dimensional Random Uniform design:

```python
>>> random_uniform(5, 3, seed=42)
array([[0.77395605, 0.43887844, 0.85859792],
       [0.69736803, 0.09417735, 0.97562235],
       [0.7611397 , 0.78606431, 0.12811363],
       [0.45038594, 0.37079802, 0.92676499],
       [0.64386512, 0.82276161, 0.4434142 ]])
```

For 2D visualization:

```pycon
>>> points = random_uniform(20, 2, seed=123)  # (1)!
```

1.  Points are completely random with no structure

## Scaling Samples to Bounds (`scale_samples`) {#scale-samples}

The designs of this section, and the
[low-discrepancy sequences](low_discrepancy_sequences.md) that return
points in the unit hypercube, can be mapped to the actual ranges of the
factors with `scale_samples`:

```python
>>> scale_samples(samples, bounds)
```

where

* **samples**: an array of shape `(n_samples, n_vars)` with values in
  $[0, 1]$
* **bounds**: a list of `(min, max)` pairs, one per column of `samples`

Column $i$ is mapped linearly to its bounds,
$x_i \mapsto \text{min}_i + x_i (\text{max}_i - \text{min}_i)$. The result
has the shape and the data type of `samples`, so `samples` should be a
float array. A `ValueError` is raised if the number of bounds differs
from the number of columns, or if a lower bound is not less than its
upper bound.

### Examples

```pycon
>>> samples = np.array([[0.1, 0.2], [0.8, 0.9]])
>>> scale_samples(samples, [(-1, 1), (0, 10)])
array([[-0.8,  2. ],
       [ 0.6,  9. ]])
```

A Latin hypercube for a temperature between 20 and 80 and a pressure
between 1 and 5:

```pycon
>>> unit = lhs(2, samples=4, criterion="center", seed=42)
>>> scale_samples(unit, [(20, 80), (1, 5)])
array([[42.5,  1.5],
       [27.5,  3.5],
       [57.5,  4.5],
       [72.5,  2.5]])
```

## References

- Qian, P. Z. G. (2009). "Nested Latin hypercube designs." *Biometrika*, 96(4), 957-970.
- Johnson, M. E., Moore, L. M., & Ylvisaker, D. (1990). "Minimax and maximin distance designs." *Journal of Statistical Planning and Inference*, 26(2), 131-148.
- Joseph, V. R., Gul, E., & Ba, S. (2015). "Maximum projection designs for computer experiments." *Biometrika*, 102(2), 371-380.
- Cioppa, T. M., & Lucas, T. W. (2007). "Efficient nearly orthogonal and space-filling Latin hypercubes." *Technometrics*, 49(1), 45-55.

## More Information

If the user needs more information about appropriate designs, please
consult the following articles on Wikipedia:

- [Latin-Hypercube designs](http://en.wikipedia.org/wiki/Latin_hypercube_sampling)

There is also a wealth of information on the [NIST](http://www.itl.nist.gov/div898/handbook/pri/pri.htm) website about the
various design matrices that can be created as well as detailed information
about designing/setting-up/running experiments in general.