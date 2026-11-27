# Optimal Experimental Designs

The `pydoe.optimal` module provides algorithms for constructing
**optimal experimental designs**: designs that select, from a set of candidate
points, the runs that are best for a polynomial model according to a chosen
optimality criterion.

!!! hint
    All optimal design tools can be imported from the top-level package:

    ```python
    >>> from pydoe import optimal_design, generate_candidate_set
    ```

## Overview

Optimal experimental design is based on maximizing or minimizing certain properties of the information matrix, typically denoted as $M$. For a design with $n$ runs, PyDOE uses the information matrix per run:
$$ M = \frac{1}{n} X^T X $$
where $X$ is the model (design) matrix of the $n$ runs.

### Design Matrix (Model Matrix)

The design (model) matrix $X$ encodes the relationship between the model parameters and the input variables. For a polynomial model of degree $d$ with $k$ factors:
$$ \text{Linear:}\quad y = \beta_0 + \sum_{i=1}^k \beta_i x_i $$
$$ \text{Quadratic:}\quad y = \beta_0 + \sum_{i=1}^k \beta_i x_i + \sum_{i=1}^k \beta_{ii} x_i^2 + \sum_{i<j} \beta_{ij} x_i x_j $$

The design matrix X for n points and p parameters is constructed as:
$$
X = \begin{bmatrix}
1 & x_1^{(1)} & x_2^{(1)} & \cdots & (x_1^{(1)})^2 & \cdots & x_1^{(1)} x_2^{(1)} & \cdots \\\\
1 & x_1^{(2)} & x_2^{(2)} & \cdots & (x_1^{(2)})^2 & \cdots & x_1^{(2)} x_2^{(2)} & \cdots \\\\
\vdots & \vdots & \vdots & & \vdots & & \vdots & \\\\
\end{bmatrix}
$$
where each row corresponds to a design point and each column to a model term. The columns are ordered as: intercept, linear terms, pure squares, two-factor products and then, for each degree from 3 up to `degree`, all monomials of that degree. See [`build_design_matrix`](#build_design_matrix).

### Efficiency Criteria

- **D-efficiency:**
  $$ \text{D-efficiency} = 100 \times (\det(M))^{1/p} $$
  $$ M = \frac{1}{n} X^T X $$
  where p is the number of parameters.

- **A-efficiency:**
  $$ \text{A-efficiency} = 100 \times \frac{p}{\operatorname{tr}(M^{-1})} $$
  $$ M = \frac{1}{n} X^T X $$
  where p is the number of parameters.

### Optimality Criteria

Below, $f(x)$ is the row of the model matrix for the point $x$, $n$ is the
number of runs and $p$ the number of model parameters.

- **D-optimality**: Maximizes the determinant of the information matrix.
  $$ \text{D-optimality:}\quad \max \det(M) $$

- **A-optimality**: Minimizes the average variance of the parameter estimates (trace of the inverse information matrix).
  $$ \text{A-optimality:}\quad \min \operatorname{tr}(M^{-1}) $$

- **I-optimality**: Minimizes the average prediction variance over the candidate set $\mathcal{X}$ (with $N_0$ points).
  $$ \text{I-optimality:}\quad \min \operatorname{tr}(M_0 M^{-1}) = \min \frac{1}{N_0} \sum_{x \in \mathcal{X}} f(x)^T M^{-1} f(x), \qquad M_0 = \frac{1}{N_0} X_0^T X_0 $$
  where $X_0$ is the model matrix of the candidates.

- **C-optimality**: Minimizes the variance of a linear combination $c^T \beta$ of the parameters. The vector $c$ is given by `c_vector`, one entry per column of the model matrix (default: all ones).
  $$ \text{C-optimality:}\quad \min c^T M^{-1} c $$

- **E-optimality**: Maximizes the smallest eigenvalue of the information matrix.
  $$ \text{E-optimality:}\quad \max \lambda_{\min}(M) $$

- **G-optimality**: Minimizes the maximum prediction variance over the candidate set.
  $$ \text{G-optimality:}\quad \min \max_{x \in \mathcal{X}} f(x)^T M^{-1} f(x) $$

- **V-optimality**: Minimizes the average prediction variance at a set of $m$ chosen points, given by `test_points`. By default these are the candidates, and V-optimality then coincides with I-optimality.
  $$ \text{V-optimality:}\quad \min \frac{1}{m} \sum_{i=1}^m f(x_i)^T M^{-1} f(x_i) $$

- **S-optimality** (Shin & Xiu, 2016): Maximizes the mutual orthogonality of the columns $X_j$ of the model matrix together with the determinant.
  $$ \text{S-optimality:}\quad \max \frac{\sqrt{\det(M)}}{\prod_{j=1}^{p} \sqrt{M_{jj}}} = \max \frac{\sqrt{\det(X^T X)}}{\prod_{j=1}^{p} \lVert X_j \rVert} $$
  The value does not depend on the scale of the columns, lies between 0 and 1, and is 1 exactly when the columns of $X$ are orthogonal. It is Shin and Xiu's $S(X)$ raised to the power $p$. It is always computed from the plain $X^T X$: the augmentation `alpha` (see below) is not applied to it.

- **T-optimality** (Atkinson & Fedorov, 1975): Model discrimination. Maximizes the lack of fit that remains when the model is fitted to the responses of a rival model at the design points.
  $$ \text{T-optimality:}\quad \max\; d^T (I - P_X) d = \max\; \min_{\beta} \lVert d - X \beta \rVert^2, \qquad P_X = X (X^T X)^{-1} X^T $$
  Here $d$ is the vector of the model differences at the design points: the responses of the rival model, or their difference from any response of the fitted model. It is given by `model_diff`, which is required for this criterion. The value is the residual sum of squares over the $n$ runs (not divided by $n$); it is 0 when the design cannot tell the two models apart.

All criteria are implemented as scores for which **larger is better**: the criteria that are minimized (A, I, C, G, V) are returned with a negative sign.

### Algorithms

All algorithms select the design from the candidate set and decide every
step by the value of the chosen criterion, so the same searches serve all
criteria (the published algorithms are stated for D-optimality). They are
deterministic.

- **Sequential (Dykstra)** (`method="sequential"`): the sequential algorithm
  of Dykstra (1971) starts from an empty design and adds, one at a time,
  the candidate that improves the criterion the most. It is fast, but as a
  greedy method it may stop well short of the optimum. The other
  algorithms start from its design.
- **Simple Exchange (Wynn-Mitchell)** (`method="simple_exchange"`): the
  simple exchange of Mitchell and Miller (1970) and Wynn (1972) changes
  one point per iteration: a point is added to the design and another is
  deleted. This implementation deletes first, removing the point whose
  loss hurts the criterion the least, then adds the best candidate, and
  keeps the exchange only if the criterion improves.
- **Fedorov** (`method="fedorov"`): the exchange algorithm of Fedorov
  (1972) evaluates every swap of a design point with a candidate and makes
  the single best one in each iteration, until no swap improves the
  criterion. It is more thorough and more expensive than the simple
  exchange.
- **Modified Fedorov** (`method="modified_fedorov"`): the algorithm of
  Cook and Nachtsheim (1980) goes through the design points in turn and
  immediately replaces each one by its best swap, so one pass can change
  every point of the design.
- **DETMAX** (`method="detmax"`): DETMAX (Mitchell, 1974) improves a
  design through excursions, in which the design grows or shrinks by
  several points before it returns to the requested size. This
  implementation is a reduced form of it: it starts from the simple
  exchange design, makes single swaps while they improve the criterion,
  and then tries an excursion of one point (add the best candidate, then
  delete the least useful point). It does not make the longer excursions
  or keep the list of failed designs of the original.

Like every exchange algorithm, they stop at a local optimum that need not
be the global one.

**Replicates.** By default a candidate is used at most once in a design.
The published algorithms let a point be run several times, and exact
optimal designs often need that (a quadratic in one factor with more than
3 runs, for instance). Pass `replicates=True` for this behavior. Without
it, `n_points` cannot exceed the number of candidates.

**Augmentation.** With `alpha > 0` the algorithms work on the augmented
matrix of Mitchell (1974),

$$ X^T X + \alpha \, \frac{X_0^T X_0}{N_0} $$

where $X_0$ is the model matrix of the $N_0$ candidates; the information
matrix is this matrix divided by $n$. It keeps the matrix positive
definite while the design has fewer points than the model has terms. A
small value such as 0.001 is enough. The default is `alpha=0.0` (no
augmentation).

!!! note "Numerical conditioning during optimization"
    During iterative search, algorithms evaluate candidate designs that may
    produce an ill-conditioned or singular information matrix (e.g. when
    too few distinct points span the model space). The criteria that need
    $M^{-1}$ (A, I, C, G, V) handle this automatically: when the Cholesky
    inversion of $M$ fails or reports an ill-conditioned matrix, a Tikhonov
    regularization term $\lambda I$ with $\lambda = 10^{-8}$ is added before
    inverting. For the D, E and S criteria (D and E only when `alpha` is 0),
    a design whose model matrix has rank $r < p$ is scored $r - p$ instead
    of 0, so that a search starting from few points can progress. The
    `score` reported for a final design that cannot estimate the model is
    then this negative integer.

## Example Usage

Generate a D-optimal design for a quadratic model with 2 factors:

```python
>>> import numpy as np
>>> from pydoe import optimal_design, generate_candidate_set
>>> candidates = generate_candidate_set(n_factors=2, n_levels=5)
>>> design, info = optimal_design(
...     candidates=candidates,
...     n_points=10,
...     degree=2,
...     criterion="D",
...     method="detmax"
... )
>>> design
array([[-1. , -1. ],
       [-1. ,  0. ],
       [-0.5, -1. ],
       [ 1. , -1. ],
       [ 1. ,  1. ],
       [-1. ,  1. ],
       [ 0. ,  1. ],
       [ 1. ,  0. ],
       [ 0. ,  0. ],
       [ 0.5, -1. ]])
>>> print(f"D-efficiency: {info['D_eff']:.2f}%")
D-efficiency: 44.64%
```

After an optimal design is selected and experiments are performed, we can model our system by estimating the regression parameters using:
$$ \hat{\beta} = (X^{T} X)^{-1} X^{T} y $$
where X is the design matrix and y is the vector of observed responses.

## Reference

### `optimal_design`

```python
optimal_design(
    candidates, n_points, degree, criterion="D", method="sequential",
    alpha=0.0, max_iter=200, *, c_vector=None, test_points=None,
    model_diff=None, replicates=False
)
```

- `candidates`: array of shape `(N0, k)`, the candidate points.
- `n_points`: number of runs of the design. It should be at least the
  number of model parameters $p$ for the model to be estimable.
- `degree`: polynomial degree of the model (1 = linear, 2 = quadratic, ...).
- `criterion`: one of `"D"`, `"A"`, `"I"`, `"C"`, `"E"`, `"G"`, `"V"`,
  `"S"`, `"T"` (default `"D"`).
- `method`: one of `"sequential"` (default), `"simple_exchange"`,
  `"fedorov"`, `"modified_fedorov"`, `"detmax"`.
- `alpha`: augmentation parameter (default 0.0), see above.
- `max_iter`: maximum number of iterations of the iterative methods
  (default 200); not used by `"sequential"`.
- `c_vector` (keyword only): C-optimality, the coefficients $c$ of the
  linear combination of the model parameters, in the order of the columns
  of `build_design_matrix` (default: all ones).
- `test_points` (keyword only): V-optimality, array of shape `(m, k)` with
  the points at which the average prediction variance is minimized
  (default: the candidates).
- `model_diff` (keyword only): T-optimality, the difference between the
  responses of the rival model and of the fitted model: either an array
  with one value per candidate, or a callable that takes an array of
  points of shape `(n, k)` and returns `n` values. Required for `"T"`.
- `replicates` (keyword only): if `True`, a candidate may be run more than
  once (default `False`).

It returns the tuple `(design, info)`. `design` is an array of shape
`(n_points, k)`. `info` is a dictionary with the keys `criterion`,
`method`, `alpha`, `score` (the value of the criterion, larger is better),
`det_XTX` ($\det(X^T X)$), `D_eff` and `A_eff` (the efficiencies defined
above, in percent), `p_columns` (the number of model parameters) and
`n_runs`.

A `ValueError` is raised for an unknown `method` or `criterion`, when an
input of the criterion is missing (`model_diff` for `"T"`) or has the
wrong shape, when `n_points` is less than 1, and when `n_points` exceeds
the number of candidates while `replicates` is `False`.

#### Replicated runs

The D-optimal design for a quadratic model in one factor on $[-1, 1]$
puts one third of the runs at each of $-1$, $0$ and $1$. With 6 runs this
needs every point twice, which requires `replicates=True`; the score is
$\det(M) = 4/27$:

```python
>>> candidates = generate_candidate_set(n_factors=1, n_levels=21)
>>> design, info = optimal_design(
...     candidates, 6, 2, criterion="D", method="fedorov", replicates=True
... )
>>> sorted(design.ravel().round(2).tolist())
[-1.0, -1.0, 0.0, 0.0, 1.0, 1.0]
>>> round(info["score"], 6), round(4 / 27, 6)
(0.148148, 0.148148)
```

Without replicates the six runs must be six different candidates, and the
design is worse:

```python
>>> design, info = optimal_design(
...     candidates, 6, 2, criterion="D", method="fedorov"
... )
>>> sorted(design.ravel().round(2).tolist())
[-1.0, -0.9, 0.0, 0.1, 0.9, 1.0]
>>> round(info["score"], 6)
0.112395
```

#### C-optimality: `c_vector`

To estimate the quadratic coefficient $\beta_{11}$ of
$y = \beta_0 + \beta_1 x + \beta_{11} x^2$ as precisely as possible, set
$c = (0, 0, 1)$. With 4 runs, the design puts one run at each end and two
at the center:

```python
>>> design, info = optimal_design(
...     candidates, 4, 2, criterion="C", method="fedorov",
...     c_vector=[0, 0, 1], replicates=True
... )
>>> sorted(design.ravel().round(2).tolist())
[-1.0, 0.0, 0.0, 1.0]
>>> round(info["score"], 6)
-4.0
```

The score is $-c^T M^{-1} c$.

#### V-optimality: `test_points`

For a straight line that will be used to predict at $x = 0$ and $x = 1$
only, the design moves runs towards $x = 1$:

```python
>>> design, info = optimal_design(
...     candidates, 4, 1, criterion="V", method="fedorov",
...     test_points=[[0.0], [1.0]], replicates=True
... )
>>> sorted(design.ravel().round(2).tolist())
[-1.0, 1.0, 1.0, 1.0]
>>> round(info["score"], 6)
-1.333333
```

#### T-optimality: `model_diff`

To discriminate between a straight line and the cubic
$1 + x + x^3$ on $[-1, 1]$, the fitted model is the line (`degree=1`) and
`model_diff` gives the responses of the rival model. The T-optimal design
puts weights $1/6$, $1/3$, $1/3$, $1/6$ on $-1$, $-1/2$, $1/2$, $1$
(Dette & Titoff, 2009); with 6 runs the lack-of-fit sum of squares is
$6/16$:

```python
>>> def cubic(points):
...     x = points[:, 0]
...     return 1 + x + x**3
>>> design, info = optimal_design(
...     candidates, 6, 1, criterion="T", method="fedorov",
...     model_diff=cubic, replicates=True
... )
>>> sorted(design.ravel().round(2).tolist())
[-1.0, -0.5, -0.5, 0.5, 0.5, 1.0]
>>> round(info["score"], 6)
0.375
```

`model_diff` can also be an array with one value per candidate:

```python
>>> design, info = optimal_design(
...     candidates, 6, 1, criterion="T", method="fedorov",
...     model_diff=cubic(candidates), replicates=True
... )
>>> round(info["score"], 6)
0.375
```

### Algorithm functions

`optimal_design` dispatches to one of five functions, which can also be
called directly. They take the same arguments as `optimal_design` (without
`method`) and return the design only, an array of shape `(n_points, k)`.

```python
sequential_dykstra(
    candidates, n_points, degree, criterion="D", alpha=0.0, *,
    c_vector=None, test_points=None, model_diff=None, replicates=False
)
simple_exchange_wynn_mitchell(
    candidates, n_points, degree, criterion="D", alpha=0.0, max_iter=200, *,
    c_vector=None, test_points=None, model_diff=None, replicates=False
)
fedorov(
    candidates, n_points, degree, criterion="D", alpha=0.0, max_iter=200, *,
    c_vector=None, test_points=None, model_diff=None, replicates=False
)
modified_fedorov(
    candidates, n_points, degree, criterion="D", alpha=0.0, max_iter=100, *,
    c_vector=None, test_points=None, model_diff=None, replicates=False
)
detmax(
    candidates, n_points, degree, criterion="D", alpha=0.0, max_iter=100, *,
    c_vector=None, test_points=None, model_diff=None, replicates=False
)
```

| Function | Algorithm |
|---|---|
| `sequential_dykstra` | Sequential (Dykstra): greedy, one point added at a time. |
| `simple_exchange_wynn_mitchell` | Simple exchange: delete one point, add one point. |
| `fedorov` | Fedorov: the best single swap per iteration. |
| `modified_fedorov` | Modified Fedorov: the best swap for each design point in turn. |
| `detmax` | Reduced DETMAX: single swaps, then one-point excursions. |

Note that `modified_fedorov` and `detmax` have a default `max_iter` of 100
when called directly, while `optimal_design` passes its own `max_iter`
(default 200).

```python
>>> from pydoe import fedorov
>>> design = fedorov(candidates, 6, 2, replicates=True)
>>> sorted(design.ravel().round(2).tolist())
[-1.0, -1.0, 0.0, 0.0, 1.0, 1.0]
```

### Model and candidate set

#### `generate_candidate_set` {#generate_candidate_set}

```python
generate_candidate_set(
    n_factors, bounds=None, n_levels=3, grid_type="full_factorial", *, seed=None
)
```

Generates the candidate points.

- `bounds`: a `(low, high)` tuple for all factors or a list of one tuple
  per factor (default: `(-1, 1)` for every factor).
- `grid_type="full_factorial"`: the grid of `n_levels` equally spaced
  levels per factor, `n_levels ** n_factors` points, last factor varying
  fastest.
- `grid_type="uniform_random"`: `n_levels ** n_factors` points drawn
  uniformly within the bounds.
- `seed` (keyword only): integer or `numpy.random.Generator` for the
  `"uniform_random"` grid; not used by the `"full_factorial"` grid.

A `ValueError` is raised if `bounds` does not match `n_factors` or
`grid_type` is unknown.

```python
>>> generate_candidate_set(2, n_levels=2)
array([[-1., -1.],
       [-1.,  1.],
       [ 1., -1.],
       [ 1.,  1.]])
>>> generate_candidate_set(
...     2, bounds=[(0, 1), (10, 20)], n_levels=2,
...     grid_type="uniform_random", seed=0
... )
array([[ 0.63696169, 12.69786714],
       [ 0.04097352, 10.16527636],
       [ 0.81327024, 19.12755577],
       [ 0.60663578, 17.29496561]])
```

#### `build_design_matrix` {#build_design_matrix}

```python
build_design_matrix(candidates, degree)
```

Builds the model matrix $X$ of the points `candidates` (shape
`(n_points, n_factors)`) for the full polynomial model of degree `degree`
(at least 1, otherwise `ValueError`). The columns are the intercept, the
linear terms, then for `degree >= 2` the pure squares followed by the
two-factor products, then for each degree from 3 to `degree` all monomials
of that degree.

```python
>>> X = build_design_matrix(np.array([[-1.0], [0.0], [1.0]]), 2)
>>> X
array([[ 1., -1.,  1.],
       [ 1.,  0.,  0.],
       [ 1.,  1.,  1.]])
>>> build_design_matrix(np.array([[2.0, 3.0]]), 2)  # 1, x1, x2, x1^2, x2^2, x1*x2
array([[1., 2., 3., 4., 9., 6.]])
```

#### `information_matrix` {#information_matrix}

```python
information_matrix(X, *, normalized=True, alpha=0.0, X0=None)
```

Returns the information matrix of the model matrix `X` with $n$ rows:

$$ M = \frac{1}{n} \left( X^T X + \alpha \, \frac{X_0^T X_0}{N_0} \right) $$

With `normalized=False` the factor $1/n$ is left out. The augmentation
term is only added when `alpha` is not zero and `X0` (the model matrix of
the $N_0$ candidates) is given.

```python
>>> M = information_matrix(X)
>>> M
array([[1.        , 0.        , 0.66666667],
       [0.        , 0.66666667, 0.        ],
       [0.66666667, 0.        , 0.66666667]])
>>> information_matrix(X, normalized=False)
array([[3., 0., 2.],
       [0., 2., 0.],
       [2., 0., 2.]])
```

#### `build_uniform_moment_matrix` {#build_uniform_moment_matrix}

```python
build_uniform_moment_matrix(X0)
```

Returns the moment matrix $M_0 = X_0^T X_0 / N_0$ of the model matrix
`X0` of the $N_0$ candidates, used by I-optimality. It weights all
candidates equally.

```python
>>> X0 = build_design_matrix(candidates, 2)
>>> build_uniform_moment_matrix(X0).round(4)
array([[1.    , 0.    , 0.3667],
       [0.    , 0.3667, 0.    ],
       [0.3667, 0.    , 0.2413]])
```

### Criterion functions

Each function returns a float for which larger is better. `M` is an
information matrix of shape `(p, p)`, as returned by `information_matrix`.

| Function | Value |
|---|---|
| `d_optimality(M)` | $\det(M)$ |
| `a_optimality(M)` | $-\operatorname{tr}(M^{-1})$ |
| `i_optimality(M_X, moment_matrix)` | $-\operatorname{tr}(M_0 M_X^{-1})$, with the moment matrix $M_0$ |
| `c_optimality(M, c)` | $-c^T M^{-1} c$, with `c` an array of shape `(p,)` |
| `e_optimality(M)` | $\lambda_{\min}(M)$ |
| `g_optimality(M, candidates)` | $-\max_i f_i^T M^{-1} f_i$ over the rows $f_i$ of `candidates` |
| `v_optimality(M, test_points)` | $-\frac{1}{m} \sum_{i=1}^{m} f_i^T M^{-1} f_i$ over the rows $f_i$ of `test_points` |
| `s_optimality(M)` | $\sqrt{\det(M)} \, / \prod_j \sqrt{M_{jj}}$ |
| `t_optimality(X, model_diff_subset)` | $d^T (I - P_X) d$ |

For `g_optimality` and `v_optimality`, `candidates` and `test_points` are
**model-matrix rows** (arrays of shape `(N, p)`, as returned by
`build_design_matrix`), not points. `t_optimality` takes the model matrix
`X` of the design, not an information matrix, and the vector
`model_diff_subset` of the model differences at its rows.

For the three-point design above:

```python
>>> from pydoe import (
...     d_optimality, a_optimality, i_optimality, c_optimality,
...     e_optimality, g_optimality, v_optimality, s_optimality,
...     t_optimality,
... )
>>> round(d_optimality(M), 6)
0.148148
>>> round(a_optimality(M), 6)
-9.0
>>> round(i_optimality(M, build_uniform_moment_matrix(X0)), 6)
-2.4357
>>> round(c_optimality(M, np.array([0.0, 1.0, 0.0])), 6)
-1.5
>>> round(e_optimality(M), 6)
0.146149
>>> round(g_optimality(M, X0), 6)
-3.0
>>> round(v_optimality(M, X0), 6)
-2.4357
>>> round(s_optimality(M), 6)
0.57735
```

The model matrix of a two-level factorial design for a linear model has
orthogonal columns, so its S-optimality value is 1:

```python
>>> from pydoe import ff2n
>>> X_ff = build_design_matrix(ff2n(2), 1)
>>> round(s_optimality(information_matrix(X_ff)), 6)
1.0
```

A straight line fitted to the responses $(1, 0, 1)$ of a rival model at
$x = -1, 0, 1$ leaves a residual sum of squares of $2/3$:

```python
>>> X_line = build_design_matrix(np.array([[-1.0], [0.0], [1.0]]), 1)
>>> round(t_optimality(X_line, np.array([1.0, 0.0, 1.0])), 6)
0.666667
```

#### `criterion_value` {#criterion_value}

```python
criterion_value(X, criterion, X0=None, alpha=0.0, M_moment=None, **kwargs)
```

Computes the criterion `criterion` (`"D"`, `"A"`, `"I"`, `"C"`, `"E"`,
`"G"`, `"V"`, `"S"` or `"T"`, case-insensitive) for the model matrix `X`
of a design. It builds
`M = information_matrix(X, normalized=True, alpha=alpha, X0=X0)` and calls
the criterion function above. `X0` is the model matrix of the candidates.
The extra inputs are:

- `"I"`: `M_moment`, the moment matrix (default:
  `build_uniform_moment_matrix(X0)`; one of `X0` and `M_moment` must be
  given).
- `"C"`: keyword `c_vector` (default: all ones).
- `"G"`: keyword `candidates`, model-matrix rows (default: `X0`, or `X`
  when `X0` is `None`).
- `"V"`: keyword `test_points`, model-matrix rows (default: `X0`, or `X`
  when `X0` is `None`). Averaging over the rows of `X` itself gives
  $-p$ for every design.
- `"T"`: keyword `model_diff_subset`, the model differences at the rows of
  `X` (required).
- `"S"`: computed from `X` alone; `alpha` is not applied.

An unknown criterion, or a missing `model_diff_subset` for `"T"`, raises
`ValueError`.

```python
>>> from pydoe import criterion_value
>>> round(criterion_value(X, "D"), 6)
0.148148
>>> round(criterion_value(X, "I", X0), 6)
-2.4357
>>> round(criterion_value(X, "C", c_vector=[0, 1, 0]), 6)
-1.5
>>> round(criterion_value(X_line, "T", model_diff_subset=[1.0, 0.0, 1.0]), 6)
0.666667
```

### Efficiencies

```python
d_efficiency(X)
a_efficiency(X)
```

Both take the model matrix `X` of a design (shape `(n, p)`) and return a
percentage, computed with $M = X^T X / n$:

$$ \text{D-efficiency} = 100 \times \det(M)^{1/p}, \qquad
\text{A-efficiency} = 100 \times \frac{p}{\operatorname{tr}(M^{-1})} $$

`d_efficiency` returns 0 when the determinant is negative (roundoff of a
singular matrix). Both are 100 when $M = I$. They depend on the coding
of the factors, so they compare designs for the same model and the same
candidate region.

```python
>>> from pydoe import d_efficiency, a_efficiency
>>> round(float(d_efficiency(X)), 4)
52.9134
>>> round(float(a_efficiency(X)), 4)
33.3333
```

### Prediction variance (`var_regression_matrix`) {#var_regression_matrix}

```python
var_regression_matrix(H, x, model, sigma=1)
```

Computes the variance of the prediction of a linear regression model at
the point `x`, for a design whose regression matrix is `H`:

$$ \mathrm{var}(x) = \sigma^2 \, f(x)^T (H^T H)^{-1} f(x) $$

where $f(x)$ holds the monomials of the model at `x`. Unlike the criteria
above, it uses $H^T H$ without the factor $1/n$, and the model is given as
a string instead of a polynomial degree.

- `H`: the regression matrix, one row per run and one column per monomial
  of `model`. It can be built from the design points with
  `pydoe.utils.build_regression_matrix(design, model)`.
- `x`: the coordinates of the point, one value per variable.
- `model`: the monomials of the model, separated by spaces. The variables
  are named `x1`, `x2`, ... in the order of the columns of the design; a
  monomial is a product of numbers and variables with optional integer
  powers, e.g. `"1 x1 x2 x1*x2 x1^2"`.
- `sigma`: standard deviation of the observation error (default 1).

A `ValueError` is raised if `H` does not have full column rank, if its
number of columns differs from the number of monomials of `model`, or if
a monomial is malformed or uses a variable that `x` does not have.

For the $2^2$ factorial design and a first-order model, the variance is
$1/4$ at the center and $3/4$ at a corner:

```python
>>> from pydoe import ff2n, var_regression_matrix
>>> from pydoe.utils import build_regression_matrix
>>> design = ff2n(2)
>>> H = build_regression_matrix(design, "1 x1 x2")
>>> H
array([[ 1., -1., -1.],
       [ 1., -1.,  1.],
       [ 1.,  1., -1.],
       [ 1.,  1.,  1.]])
>>> float(var_regression_matrix(H, [0.0, 0.0], "1 x1 x2"))
0.25
>>> float(var_regression_matrix(H, [1.0, 1.0], "1 x1 x2"))
0.75
>>> float(var_regression_matrix(H, [1.0, 1.0], "1 x1 x2", sigma=2))
3.0
```

## Fisher-Information Designs over Jacobians

The algorithms above build the model matrix from candidate points of a
polynomial model. When the model is nonlinear in its parameters, or the
sensitivities come from a simulator, the design is instead chosen from the
**Jacobian** $J$ of the model response with respect to the parameters,
evaluated at the candidate experiments.

### `fisher_information`

```python
fisher_information(jacobian, rows=None, covariance=None)
```

For a Jacobian $J$ of shape `(N, p)` (rows are candidate experiments,
columns are parameters) the Fisher information matrix of the rows in `rows`
(all rows by default; repeats allowed) is

$$M = J^T \Sigma^{-1} J$$

where $\Sigma$ is the observation-noise covariance over the candidates:
`covariance` is `None` for the identity, a float for a common variance, a
vector of shape `(N,)` for independent variances, or a full `(N, N)` matrix.
The sub-matrix belonging to `rows` is used.

A 3D Jacobian of shape `(N, p, K)` holds the sensitivities at $K$ points of
the parameter space. A FIM is computed for each point and the mean FIM is
returned,

$$\bar M = \frac{1}{K} \sum_{k=1}^K J_k^T \Sigma^{-1} J_k$$

which is the robust (Bayesian-style) formulation of optimal experimental
design for nonlinear models.

```pycon
>>> import numpy as np
>>> from pydoe import fisher_information
>>> J = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
>>> fisher_information(J)
array([[2., 1.],
       [1., 2.]])
>>> fisher_information(J, rows=[0, 2], covariance=[1.0, 1.0, 4.0])
array([[1.25, 0.25],
       [0.25, 0.25]])
```

### `jacobian_optimal_design`

```python
jacobian_optimal_design(
    jacobian, n_points, covariance=None, criterion="D", max_iter=100
)
```

Selects `n_points` rows of the Jacobian (replicates allowed) that maximize
the `criterion` — one of `"D"`, `"A"`, `"E"` or `"S"` — evaluated on the
(mean) Fisher information matrix. Rows are first chosen greedily, then
improved with up to `max_iter` point-exchange passes. It returns the
selected row indices and a dictionary holding the `criterion`, its
`score` and the final `fim`.

For a straight line $y = a + b x$ on $x \in [0, 1]$, the D-optimal design
puts half of the runs at each end of the interval:

```pycon
>>> import numpy as np
>>> from pydoe import jacobian_optimal_design
>>> x = np.linspace(0, 1, 11)
>>> J = np.stack([np.ones_like(x), x], axis=1)  # columns: dy/da, dy/db
>>> idx, info = jacobian_optimal_design(J, 4)
>>> sorted(idx.tolist())
[0, 0, 10, 10]
>>> info["criterion"]
'D'
>>> info["fim"]
array([[4., 2.],
       [2., 2.]])
```

## References

- Atkinson, A. C., & Donev, A. N. (1992). *Optimum Experimental Designs*. Oxford University Press.
- Atkinson, A. C., & Fedorov, V. V. (1975). The design of experiments for discriminating between two rival models. *Biometrika*, 62(1), 57-70. https://doi.org/10.1093/biomet/62.1.57
- Cook, R. D., & Nachtsheim, C. J. (1980). A comparison of algorithms for constructing exact D-optimal designs. *Technometrics*, 22(3), 315-324.
- Dette, H., & Titoff, S. (2009). Optimal discrimination designs. *The Annals of Statistics*, 37(4), 2056-2082. https://doi.org/10.1214/08-AOS635
- Dykstra, O. (1971). The augmentation of experimental data to maximize |X'X|. *Technometrics*, 13(3), 682-688.
- Fedorov, V. V. (1972). *Theory of Optimal Experiments*. Academic Press.
- Mitchell, T. J. (1974). An algorithm for the construction of "D-optimal" experimental designs. *Technometrics*, 16(2), 203-210.
- Mitchell, T. J., & Miller, F. L. (1970). Use of design repair to construct designs for special linear models. Oak Ridge National Laboratory, Mathematics Division Annual Progress Report (ORNL-4661).
- Shin, Y., & Xiu, D. (2016). Nonadaptive quasi-optimal points selection for least squares linear regression. *SIAM Journal on Scientific Computing*, 38(1), A385-A411. https://doi.org/10.1137/15M1015868
- Wynn, H. P. (1972). Results in the theory and construction of D-optimum experimental designs. *Journal of the Royal Statistical Society B*, 34(2), 133-147.
- Pukelsheim, F. (2006). *Optimal Design of Experiments*. SIAM.
- NIST: https://www.itl.nist.gov/div898/handbook/pri/section5/pri521.htm
- [Optimal experimental design](https://en.wikipedia.org/wiki/Optimal_experimental_design)
- Ryan, E. G., Drovandi, C. C., McGree, J. M., & Pettitt, A. N. (2016). A review of modern computational algorithms for Bayesian optimal design. *International Statistical Review*, 84(1), 128-154. https://doi.org/10.1111/insr.12107

