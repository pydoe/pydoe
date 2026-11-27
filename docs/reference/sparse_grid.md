# Sparse Grid Designs

The ``PyDOE`` module provides sparse grid construction using **Smolyak's construction** (Smolyak, 1963)
for generating experimental designs with hierarchical grid structures that maintain good
space-filling properties while requiring significantly fewer points than traditional
full grid approaches in high-dimensional spaces.

!!! hint
    All sparse grid functions are available with:

    ```python
    >>> from pydoe import doe_sparse_grid, sparse_grid_dimension
    ```

## Overview

The grid types follow the MATLAB Sparse Grid Interpolation Toolbox by
Andreas Klimke (Klimke & Wohlmuth, 2005). For the default grid type, the
number of points is the one that spinterp's `spdim` function returns. The
points themselves are not checked against spinterp, and they are returned
in a different order.

Sparse grids use **Smolyak's construction** to overcome the curse of dimensionality:
while a full grid in $d$ dimensions with $m$ points per dimension requires
$m^d$ total points, sparse grids require significantly fewer points.

**Grid Types:**

Every grid type is a family of nested one-dimensional point sets
$X^0 \subset X^1 \subset X^2 \subset \dots$ on $[0, 1]$, with $m_l$ points
at level $l$ and the single point $0.5$ at level 0 ($m_0 = 1$):

- **`'clenshaw_curtis'`** (default): $m_l = 2^l + 1$ equidistant points
  including the boundary, $x_j = j / (m_l - 1)$. This is the grid that the
  spinterp toolbox calls Clenshaw-Curtis.
- **`'chebyshev'`**: $m_l = 2^l + 1$ Chebyshev extrema,
  $x_j = \left(1 - \cos(\pi j / (m_l - 1))\right) / 2$, which include the
  boundary and are denser towards it. The number of points is the same as
  for `'clenshaw_curtis'`.
- **`'gauss_patterson'`**: the $m_l = 2^{l+1} - 1$ nodes of the nested
  Gauss-Patterson quadrature rules (Patterson, 1968), mapped to $[0, 1]$.
  They do not include the boundary. The nodes are computed numerically
  and are available up to level 5.

### Sparse Grid Design (``doe_sparse_grid``)

The main function for generating sparse grid designs using Smolyak's construction.

**Syntax:**

```python
>>> doe_sparse_grid(n_level, n_factors, grid_type='clenshaw_curtis')
```

**Parameters**:

- ``n_level`` : int
    Sparse grid level (≥ 0). Higher levels provide more points.
    Level 0 gives a single center point, higher levels add structured points.

- ``n_factors`` : int
    Number of factors/dimensions in the design space (≥ 1).

- ``grid_type`` : {'clenshaw_curtis', 'chebyshev', 'gauss_patterson'}, default 'clenshaw_curtis'
    Type of nested 1D points to use, as described above.

**Returns**:

- ``design`` : ndarray of shape (n_points, n_factors)
    Sparse grid design points in the unit hypercube `[0, 1]^n_factors`,
    without duplicates. The points are ordered by level: the center first,
    then the points that each further level adds. The design of level
    ``n_level - 1`` is therefore the first rows of the design of level
    ``n_level``.

**Raises**: ``ValueError`` if ``n_level`` is negative, ``n_factors`` is less
than 1, ``grid_type`` is not one of the three names above, or ``n_level``
exceeds 5 for the Gauss-Patterson grid.

**Examples:**

```python
>>> import numpy as np
>>> from pydoe import doe_sparse_grid

>>> # Level 1 in 2D: the center and two points on each axis
>>> doe_sparse_grid(n_level=1, n_factors=2)
array([[0.5, 0.5],
       [0.5, 0. ],
       [0.5, 1. ],
       [0. , 0.5],
       [1. , 0.5]])

>>> # Basic 2D sparse grid
>>> design = doe_sparse_grid(n_level=3, n_factors=2)
>>> print(f"Generated {len(design)} points in 2D")
Generated 29 points in 2D

>>> # High-dimensional sparse grid
>>> design = doe_sparse_grid(n_level=4, n_factors=4)
>>> print(f"4D design with {len(design)} points")
4D design with 401 points

>>> # Chebyshev sparse grid
>>> design = doe_sparse_grid(n_level=2, n_factors=3, grid_type='chebyshev')
>>> print(f"Chebyshev grid: {design.shape}")
Chebyshev grid: (25, 3)

>>> # Gauss-Patterson sparse grid: no points on the boundary
>>> doe_sparse_grid(n_level=1, n_factors=2, grid_type='gauss_patterson')
array([[0.5       , 0.5       ],
       [0.5       , 0.11270167],
       [0.5       , 0.88729833],
       [0.11270167, 0.5       ],
       [0.88729833, 0.5       ]])
```

The designs are nested: a lower level is the first rows of a higher level.

```python
>>> low = doe_sparse_grid(n_level=2, n_factors=2)
>>> high = doe_sparse_grid(n_level=3, n_factors=2)
>>> bool(np.array_equal(low, high[:len(low)]))
True
```

An unknown grid type is an error:

```python
>>> doe_sparse_grid(2, 2, grid_type='uniform')
Traceback (most recent call last):
    ...
ValueError: grid_type must be one of ('clenshaw_curtis', 'chebyshev', 'gauss_patterson'), got 'uniform'
```

!!! note
    For the Clenshaw-Curtis and Chebyshev grids in $d$ dimensions, the
    first point counts are:

    - Level 0: 1 point (center)
    - Level 1: 2*d + 1 points
    - Level 2: 2*d² + 2*d + 1 points

    The full grid with the same one-dimensional resolution has
    $(2^n + 1)^d$ points: 83521 for level 4 in 4 dimensions, against 401
    for the sparse grid.

### Sparse Grid Dimension (``sparse_grid_dimension``)

Returns the number of points in a sparse grid without generating the
actual points. This is useful for planning and memory estimation.

**Syntax:**

```python
>>> sparse_grid_dimension(n_level, n_factors, grid_type='clenshaw_curtis')
```

- ``n_level``: Sparse grid level (integer ≥ 0)
- ``n_factors``: Number of factors/dimensions (integer ≥ 1)
- ``grid_type``: Type of 1D points, one of ``'clenshaw_curtis'`` (default),
  ``'chebyshev'`` and ``'gauss_patterson'``. The Clenshaw-Curtis and
  Chebyshev grids have the same number of points.

**Returns**: Integer number of points that ``doe_sparse_grid`` generates for
the same arguments. Invalid arguments raise ``ValueError``, as for
``doe_sparse_grid``.

**Example:**

```python
>>> # Check point count before generation
>>> point_count = sparse_grid_dimension(n_level=5, n_factors=8)
>>> print(f"Level 5, 8D grid will have {point_count} points")
Level 5, 8D grid will have 15713 points

>>> # Compare different levels
>>> for level in range(1, 6):
...     count = sparse_grid_dimension(level, 4)
...     print(f"Level {level}: {count} points")
Level 1: 9 points
Level 2: 41 points
Level 3: 137 points
Level 4: 401 points
Level 5: 1105 points

>>> # The Gauss-Patterson grid has more points per level
>>> sparse_grid_dimension(2, 2)
13
>>> sparse_grid_dimension(2, 2, grid_type='gauss_patterson')
17
```



## Mathematical Background

### Smolyak's Construction

With the nested one-dimensional point sets
$X^0 \subset X^1 \subset X^2 \subset \dots$ of a grid type, the sparse grid
of level $n$ in $d$ dimensions is the union of the tensor grids whose
levels sum to at most $n$:

$$
H(n, d) = \bigcup_{l_1 + \dots + l_d \le n}
X^{l_1} \times \dots \times X^{l_d}
$$

This is the set of points at which Smolyak's formula (Smolyak, 1963)
evaluates a function. With univariate interpolation or quadrature rules
$\mathcal{U}^{i}$, $i \ge 1$, where $\mathcal{U}^{i}$ uses the points
$X^{i-1}$, and $q = n + d$, the formula is

$$
\mathcal{A}(q, d) = \sum_{q-d+1 \leq |\mathbf{i}|_1 \leq q} (-1)^{q-|\mathbf{i}|_1}
\binom{d-1}{q-|\mathbf{i}|_1} \bigotimes_{j=1}^d \mathcal{U}^{i_j}
$$

where $\mathbf{i} = (i_1, \ldots, i_d)$ is a multi-index with $i_j \ge 1$
and $|\mathbf{i}|_1 = i_1 + \cdots + i_d$. `doe_sparse_grid` returns the
points only; it does not compute interpolation or quadrature weights.

### Point Count Formula

Let $\Delta m_l = m_l - m_{l-1}$ be the number of points that level $l$
adds in one dimension, with $\Delta m_0 = 1$. For sparse grid level $n$ and
dimension $d$:

$$
N(n, d) = \sum_{l_1 + \dots + l_d \le n} \; \prod_{i=1}^{d} \Delta m_{l_i}
$$

For the Clenshaw-Curtis and Chebyshev grids $\Delta m_1 = 2$ and
$\Delta m_l = 2^{l-1}$ for $l \ge 2$; for the Gauss-Patterson grid
$\Delta m_l = 2^l$ for $l \ge 1$.

### Grid Types

- **Clenshaw-Curtis**: $2^l + 1$ equidistant points including the boundary
- **Chebyshev**: $2^l + 1$ Chebyshev extrema including the boundary
- **Gauss-Patterson**: $2^{l+1} - 1$ nested quadrature nodes, none on the
  boundary, up to level 5

For detailed mathematical exposition, see the [SPINTERP documentation](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/whatis.html).

## Example Usage

Generate a sparse grid design for 3 factors at level 4:

```python
>>> import numpy as np
>>> from pydoe import doe_sparse_grid, sparse_grid_dimension
>>>
>>> # Check point count first
>>> n_points = sparse_grid_dimension(n_level=4, n_factors=3)
>>> print(f"Expected points: {n_points}")
Expected points: 177
>>>
>>> # Generate sparse grid
>>> design = doe_sparse_grid(n_level=4, n_factors=3)
>>> print(f"Generated: {design.shape}")
Generated: (177, 3)
```



## References

- Genz, A. (1987). A package for testing multiple integration subroutines.
  In P. Keast & G. Fairweather (Eds.), *Numerical Integration: Recent Developments,
  Software and Applications* (pp. 337-340). Reidel. ISBN: 9027725144. https://doi.org/10.1007/978-94-009-3889-2_33

- Klimke, A., & Wohlmuth, B. (2005). Algorithm 847: SPINTERP: Piecewise
  multilinear hierarchical sparse grid interpolation in MATLAB. *ACM Transactions on
  Mathematical Software*, 31(4), 561-579. https://doi.org/10.1145/1114268.1114275

- Klimke, A. (2006). *SPINTERP V2.1: Piecewise multilinear hierarchical
  sparse grid interpolation in MATLAB: Documentation*.

- Patterson, T. N. L. (1968). The optimum addition of points to quadrature
  formulae. *Mathematics of Computation*, 22(104), 847-856.

- Smolyak, S. (1963). Quadrature and interpolation formulas for tensor
  products of certain classes of functions. *Doklady Akademii Nauk SSSR*, 4, 240-243.

**Original MATLAB Documentation:**

- [SPINTERP Toolbox](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/spinterp.html)
- [Mathematical Details](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/whatis.html)
- [Implementation Guide](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/getting_started.html)
- [Function Reference](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/functions_list.html)
