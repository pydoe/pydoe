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

This implementation is based on the MATLAB Sparse Grid Interpolation Toolbox by
Andreas Klimke (Klimke & Wohlmuth, 2005) and provides exact compatibility with MATLAB spinterp's spdim function.

Sparse grids use **Smolyak's construction** to overcome the curse of dimensionality:
while a full grid in :math:`d` dimensions with :math:`n` points per dimension requires 
:math:`n^d` total points, sparse grids require significantly fewer points.

**Grid Types:**
    - **Clenshaw-Curtis**: Nested grids based on Chebyshev polynomials (recommended)
    - **Chebyshev**: Points at Chebyshev polynomial extrema  
    - **Gauss-Patterson**: Quadrature-based points

### Sparse Grid Design (``doe_sparse_grid``)

The main function for generating sparse grid designs using Smolyak's construction.
This implementation exactly matches MATLAB spinterp's theoretical point counts.

**Syntax:**

```python
>>> doe_sparse_grid(n_level, n_factors, grid_type='clenshaw_curtis')
```

**Parameters**:

- ``n_level`` : int
    Sparse grid level. Higher levels provide more points and better accuracy.
    Level 0 gives a single center point, higher levels add structured points.

- ``n_factors`` : int
    Number of factors/dimensions in the design space.

- ``grid_type`` : {'clenshaw_curtis', 'chebyshev', 'gauss_patterson'}, default 'clenshaw_curtis'
    Type of 1D grid points to use:

    - ``'clenshaw_curtis'``: Nested Clenshaw-Curtis points (recommended)
    - ``'chebyshev'``: Chebyshev polynomial extrema points  
    - ``'gauss_patterson'``: Gauss-Patterson quadrature points

**Returns**:

- ``design`` : ndarray of shape (n_points, n_factors)
    Sparse grid design points in the unit hypercube [0, 1]^n_factors.

**Examples:**

```python
>>> import numpy as np
>>> from pydoe import doe_sparse_grid

>>> # Basic 2D sparse grid
>>> design = doe_sparse_grid(n_level=3, n_factors=2)
>>> print(f"Generated {len(design)} points in 2D")
Generated 29 points in 2D

>>> # High-dimensional sparse grid
>>> design = doe_sparse_grid(n_level=4, n_factors=4)
>>> print(f"4D design with {len(design)} points")
4D design with 177 points

>>> # Chebyshev sparse grid
>>> design = doe_sparse_grid(n_level=2, n_factors=3, grid_type='chebyshev')
>>> print(f"Chebyshev grid: {design.shape}")
Chebyshev grid: (25, 3)
```

!!! note
    The point counts follow exact polynomial formulas from Schreiber (2000) that match
    MATLAB spinterp's spdim function:

    - Level 0: 1 point (center)
    - Level 1: 2*d + 1 points  
    - Level 2: 2*d² + 2*d + 1 points
    - Higher levels: polynomial growth in dimension

### Sparse Grid Dimension (``sparse_grid_dimension``)

Returns the expected number of points in a sparse grid without generating the
actual points. This is useful for planning and memory estimation.

**Syntax:**

```python
>>> sparse_grid_dimension(n_level, n_factors)
```

- ``n_level``: Sparse grid level (integer ≥ 0)
- ``n_factors``: Number of factors/dimensions (integer ≥ 1)

**Returns**: Integer number of points that would be generated

**Example:**

```python
>>> # Check point count before generation
>>> point_count = sparse_grid_dimension(n_level=5, n_factors=8)
>>> print(f"Level 5, 8D grid will have {point_count} points")

>>> # Compare different levels
>>> for level in range(1, 6):
...     count = sparse_grid_dimension(level, 4)
...     print(f"Level {level}: {count} points")
```



## Mathematical Background

### Smolyak's Construction

Sparse grids are constructed using Smolyak's formula (Smolyak, 1963), which combines univariate
interpolation rules. For a multivariate function :math:`f`, the sparse grid 
interpolation operator is:

$$
\mathcal{A}^d_{n} f = \sum_{|\mathbf{i}|_1 \leq n+d-1} (-1)^{n+d-1-|\mathbf{i}|_1} 
\binom{d-1}{n+d-1-|\mathbf{i}|_1} \bigotimes_{j=1}^d \mathcal{U}^{i_j}
$$

where $\mathbf{i} = (i_1, \ldots, i_d)$ is a multi-index and $|\mathbf{i}|_1 = i_1 + \cdots + i_d$.

### Point Count Formula

For sparse grid level $n$ and dimension $d$:
$$ N(n,d) = \sum_{k=0}^{n} \binom{n-k+d-1}{d-1} \cdot 2^k $$

### Grid Types

- **Clenshaw-Curtis**: Nested grids based on Chebyshev polynomials (recommended)
- **Chebyshev**: Points at Chebyshev polynomial extrema
- **Gauss-Patterson**: Quadrature-based nested points

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

- Smolyak, S. (1963). Quadrature and interpolation formulas for tensor 
  products of certain classes of functions. *Doklady Akademii Nauk SSSR*, 4, 240-243.

**Original MATLAB Documentation:**

- [SPINTERP Toolbox](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/spinterp.html)
- [Mathematical Details](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/whatis.html)
- [Implementation Guide](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/getting_started.html)
- [Function Reference](https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/functions_list.html)