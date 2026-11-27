r"""
Sparse Grid Design of Experiments
=================================

This module implements sparse grid designs based on Smolyak's construction.
Sparse grids provide efficient sampling of high-dimensional spaces with
good space-filling properties while requiring significantly fewer points
than full tensor product grids.

With nested one-dimensional point sets
$$X^0 \subset X^1 \subset X^2 \subset \dots$$
the sparse grid of level $$n$$ in $$d$$ dimensions is

$$H(n, d) = \bigcup_{l_1 + \dots + l_d \le n}
X^{l_1} \times \dots \times X^{l_d}$$

The grid types follow the MATLAB Sparse Grid Interpolation Toolbox by:
    Copyright (c) 2006 W. Andreas Klimke, Universitaet Stuttgart
    Copyright (c) 2007-2008 W. A. Klimke. All Rights Reserved.
    email: klimkeas@ians.uni-stuttgart.de
    website: https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/spinterp.html

"""

import itertools
from collections.abc import Iterator
from functools import cache
from typing import Literal

import numpy as np
from numpy.polynomial import legendre


__all__ = ["doe_sparse_grid", "sparse_grid_dimension"]


GridType = Literal["clenshaw_curtis", "chebyshev", "gauss_patterson"]

_GRID_TYPES = ("clenshaw_curtis", "chebyshev", "gauss_patterson")

# The Gauss-Patterson nodes are computed numerically; the rule with 63
# nodes (level 5) is accurate to about 1e-12, the next one is not.
_MAX_GAUSS_PATTERSON_LEVEL = 5


def doe_sparse_grid(
    n_level: int, n_factors: int, grid_type: GridType = "clenshaw_curtis"
) -> np.ndarray:
    r"""
    Generate a sparse grid design using Smolyak's construction.

    Parameters
    ----------
    n_level : int
        Sparse grid level. Higher levels provide more points.
    n_factors : int
        Number of factors/dimensions in the design space.
    grid_type : {'clenshaw_curtis', 'chebyshev', 'gauss_patterson'}
        Type of nested 1D points to use, default 'clenshaw_curtis'.
        With $$m_0 = 1$$ point (the center) at level 0 in every case:

        - ``'clenshaw_curtis'``: $$m_l = 2^l + 1$$ equidistant points
          including the boundary, $$x_j = j / (m_l - 1)$$. This is the
          grid that the spinterp toolbox calls Clenshaw-Curtis.
        - ``'chebyshev'``: $$m_l = 2^l + 1$$ Chebyshev extrema,
          $$x_j = (1 - \cos(\pi j / (m_l - 1))) / 2$$, denser towards
          the boundary.
        - ``'gauss_patterson'``: the $$m_l = 2^{l+1} - 1$$ nodes of the
          nested Gauss-Patterson quadrature rules, which do not include
          the boundary. Available up to level 5.

    Returns
    -------
    design : ndarray of shape (n_points, n_factors)
        Sparse grid design points in the unit hypercube [0, 1]^n_factors,
        without duplicates. The points are ordered by level: the center
        first, then the points that each further level adds, so the
        design of level ``n_level - 1`` is the first rows of this one.

    Raises
    ------
    ValueError
        If n_level is negative, n_factors is less than 1, grid_type is
        unknown, or n_level exceeds 5 for the Gauss-Patterson grid.

    References
    ----------
    Smolyak, S. A. (1963). Quadrature and interpolation formulas for tensor
    products of certain classes of functions. Soviet Math. Dokl., 4, 240-243.

    Examples
    --------
    >>> doe_sparse_grid(1, 2)
    array([[0.5, 0.5],
           [0.5, 0. ],
           [0.5, 1. ],
           [0. , 0.5],
           [1. , 0.5]])
    >>> doe_sparse_grid(3, 2).shape
    (29, 2)
    >>> doe_sparse_grid(2, 2, grid_type="gauss_patterson").shape
    (17, 2)
    """
    _check_arguments(n_level, n_factors, grid_type)

    blocks = []
    for levels in _multi_indices(n_level, n_factors):
        axes = [_new_points(grid_type, level) for level in levels]
        blocks.append(np.array(list(itertools.product(*axes))))
    return np.vstack(blocks)


def sparse_grid_dimension(
    n_level: int, n_factors: int, grid_type: GridType = "clenshaw_curtis"
) -> int:
    r"""
    Compute the number of points in a sparse grid design.

    With $$\Delta m_l$$ the number of points that level $$l$$ adds in one
    dimension, the sparse grid has

    $$N(n, d) = \sum_{l_1 + \dots + l_d \le n} \;
    \prod_{i=1}^{d} \Delta m_{l_i}$$

    points. For the default grid this is the count that spinterp's
    ``spdim`` returns.

    Parameters
    ----------
    n_level : int
        Sparse grid level.
    n_factors : int
        Number of dimensions.
    grid_type : {'clenshaw_curtis', 'chebyshev', 'gauss_patterson'}
        Type of 1D points, default 'clenshaw_curtis'. The Clenshaw-Curtis
        and Chebyshev grids have the same number of points.

    Returns
    -------
    n_points : int
        Number of points in the sparse grid.

    Raises
    ------
    ValueError
        If n_level is negative, n_factors is less than 1, grid_type is
        unknown, or n_level exceeds 5 for the Gauss-Patterson grid.

    Examples
    --------
    >>> sparse_grid_dimension(3, 2)
    29
    >>> sparse_grid_dimension(4, 4)
    401
    >>> sparse_grid_dimension(2, 2, grid_type="gauss_patterson")
    17
    """
    _check_arguments(n_level, n_factors, grid_type)

    added = [_n_new_points(grid_type, level) for level in range(n_level + 1)]
    # counts[s]: number of points whose levels sum to s, over the
    # dimensions handled so far
    counts = [1] + [0] * n_level
    for _ in range(n_factors):
        counts = [
            sum(counts[s - level] * added[level] for level in range(s + 1))
            for s in range(n_level + 1)
        ]
    return sum(counts)


def _check_arguments(n_level: int, n_factors: int, grid_type: str) -> None:
    if n_level < 0:
        raise ValueError("n_level must be non-negative")
    if n_factors < 1:
        raise ValueError("n_factors must be positive")
    if grid_type not in _GRID_TYPES:
        msg = f"grid_type must be one of {_GRID_TYPES}, got {grid_type!r}"
        raise ValueError(msg)
    if grid_type == "gauss_patterson" and n_level > _MAX_GAUSS_PATTERSON_LEVEL:
        msg = (
            "the gauss_patterson grid is available up to n_level "
            f"{_MAX_GAUSS_PATTERSON_LEVEL}, got {n_level}"
        )
        raise ValueError(msg)


def _multi_indices(total: int, dimension: int) -> Iterator[tuple]:
    """
    Yield the tuples of ``dimension`` non-negative levels whose sum is at
    most ``total``, by increasing sum.
    """

    def with_sum(remaining: int, dims: int) -> Iterator[tuple]:
        if dims == 1:
            yield (remaining,)
            return
        for first in range(remaining + 1):
            for rest in with_sum(remaining - first, dims - 1):
                yield (first, *rest)

    for level_sum in range(total + 1):
        yield from with_sum(level_sum, dimension)


def _n_new_points(grid_type: str, level: int) -> int:
    """Number of 1D points that ``level`` adds to the levels below it."""
    if level == 0:
        return 1
    if grid_type == "gauss_patterson":
        return 2**level
    return 2 if level == 1 else 2 ** (level - 1)


@cache
def _new_points(grid_type: str, level: int) -> tuple:
    """1D points in [0, 1] that ``level`` adds to the levels below it."""
    if level == 0:
        return (0.5,)
    if grid_type == "gauss_patterson":
        return tuple(float(x) for x in (_patterson_new_nodes(level) + 1) / 2)
    # 2**level + 1 points j / 2**level; the odd j are new (all but the
    # center at level 1)
    j = np.array([0, 2]) if level == 1 else np.arange(1, 2**level, 2)
    x = j / 2**level
    if grid_type == "chebyshev":
        x = (1 - np.cos(np.pi * x)) / 2
    return tuple(float(v) for v in x)


@cache
def _patterson_nodes(level: int) -> np.ndarray:
    """All nodes on [-1, 1] of the Gauss-Patterson rule of ``level``."""
    if level == 0:
        return np.zeros(1)
    return np.sort(
        np.concatenate([
            _patterson_nodes(level - 1),
            _patterson_new_nodes(level),
        ])
    )


@cache
def _patterson_new_nodes(level: int) -> np.ndarray:
    r"""
    Nodes on [-1, 1] that the Gauss-Patterson rule of ``level`` adds.

    With $$G$$ the polynomial whose roots are the $$n$$ nodes of the rule
    below, the $$n + 1$$ new nodes are the roots of the polynomial
    $$E$$ of degree $$n + 1$$ for which

    $$\int_{-1}^{1} G(x) E(x) x^k \, dx = 0, \quad k = 0, \dots, n$$

    so that the extended rule with $$2n + 1$$ nodes is exact for
    polynomials of degree $$3n + 1$$ (Patterson, 1968). Level 1 is the
    3-point Gauss-Legendre rule.
    """
    old = _patterson_nodes(level - 1)
    n = len(old)
    g = legendre.legfromroots(old)
    x, w = legendre.leggauss(2 * n + 2)
    g_x = legendre.legval(x, g)
    # basis[j] holds the Legendre polynomial P_j at the quadrature nodes
    basis = legendre.legvander(x, n + 1).T
    # E = P_{n+1} + sum_j c_j P_j has the parity of n + 1
    parity = [j for j in range(n + 1) if (n + 1 - j) % 2 == 0]
    a = np.array([
        [np.sum(w * g_x * basis[j] * basis[k]) for j in parity]
        for k in range(n + 1)
    ])
    b = -np.array([
        np.sum(w * g_x * basis[n + 1] * basis[k]) for k in range(n + 1)
    ])
    coefficients = np.zeros(n + 2)
    coefficients[n + 1] = 1.0
    coefficients[parity] = np.linalg.lstsq(a, b, rcond=None)[0]
    roots = np.sort(np.real(legendre.legroots(coefficients)))
    # symmetrize: the nodes come in pairs -x, x
    return (roots - roots[::-1]) / 2
