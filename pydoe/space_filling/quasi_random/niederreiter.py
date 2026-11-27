r"""
This module implements the Niederreiter sequence in base 2, a
low-discrepancy quasirandom sequence used in numerical integration,
sampling, and global optimization tasks.

The sequence is a digital (t, s)-sequence over GF(2). Dimension $$i$$ is
tied to the $$i$$-th irreducible polynomial $$p_i$$ over GF(2), taken in
order of increasing degree ($$x$$, $$x + 1$$, $$x^2 + x + 1$$, ...), with
degree $$e_i$$. Row $$j$$ of its generating matrix (the row that produces
the $$j$$-th binary digit of the coordinate) holds the coefficients
$$a(q, k, r)$$ of the formal Laurent series

$$\frac{x^k}{p_i(x)^q} = \sum_{r} a(q, k, r) \, x^{-r-1}$$

where

$$j - 1 = (q - 1) e_i + k, \quad 0 \le k < e_i$$

Given the binary expansion of the point index $$n$$, multiplying it
(mod 2) by the generating matrix of a dimension produces the binary
digits of the coordinate for that dimension.

The quality parameter of the sequence is

$$t = \sum_{i=1}^{s} (e_i - 1)$$

The first $$2^m$$ points form a (t, m, s)-net, so every elementary
interval of volume $$2^{t-m}$$ holds exactly $$2^t$$ of them. The first
dimension is the van der Corput sequence, and the first two dimensions
form a (0, 2)-sequence.

References
----------
Niederreiter, H. (1988). "Low-discrepancy and low-dispersion
sequences." *Journal of Number Theory*, 30(1), 51-70.
https://doi.org/10.1016/0022-314X(88)90025-X

Bratley, P., Fox, B. L., & Niederreiter, H. (1994). "Algorithm 738:
Programs to generate Niederreiter's low-discrepancy sequences."
*ACM Transactions on Mathematical Software*, 20(4), 494-495.
https://doi.org/10.1145/198429.198436
"""

import numpy as np


__all__ = ["niederreiter_sequence"]


_MAX_DIMENSION = 20


def _poly_degree(poly: int) -> int:
    """Degree of a polynomial over GF(2) stored as a bit mask."""
    return poly.bit_length() - 1


def _poly_mul(a: int, b: int) -> int:
    """Product of two polynomials over GF(2) (carry-less product)."""
    product = 0
    while b:
        if b & 1:
            product ^= a
        a <<= 1
        b >>= 1
    return product


def _poly_mod(a: int, b: int) -> int:
    """Remainder of the division of ``a`` by ``b`` over GF(2)."""
    degree_b = _poly_degree(b)
    while a and _poly_degree(a) >= degree_b:
        a ^= b << (_poly_degree(a) - degree_b)
    return a


def _irreducible_polynomials(count: int) -> list:
    """
    First ``count`` irreducible polynomials over GF(2), by increasing
    degree and then increasing bit mask (bit ``i`` is the coefficient
    of ``x**i``): ``x``, ``x + 1``, ``x**2 + x + 1``, ...
    """
    found = []
    candidate = 2
    while len(found) < count:
        degree = _poly_degree(candidate)
        if all(
            _poly_mod(candidate, p) != 0
            for p in found
            if 2 * _poly_degree(p) <= degree
        ):
            found.append(candidate)
        candidate += 1
    return found


_IRREDUCIBLE_POLYS = _irreducible_polynomials(_MAX_DIMENSION)


def niederreiter_sequence(
    num_points: int, dimension: int, n_bits: int = 30
) -> np.ndarray:
    r"""
    Generate the Niederreiter sequence in base 2.

    The sequence is a digital (t, s)-sequence over GF(2): for each
    dimension a binary generating matrix is derived from the Laurent
    series of $$x^k / p(x)^q$$, where $$p$$ is the irreducible
    polynomial over GF(2) tied to that dimension. The binary
    expansion of the point index `n` is mapped through this matrix
    (mod 2) to obtain the binary digits of the coordinate value.

    Up to 20 dimensions are supported, each backed by its own
    irreducible polynomial over GF(2), in order of increasing degree.
    The first dimension is the van der Corput sequence.

    Parameters
    ----------
    num_points : int
        Number of points to generate. Must be >= 1. The points repeat
        after ``2 ** n_bits`` of them, so `num_points` should not
        exceed that, although larger values are accepted. The first
        ``2 ** m`` points are the best balanced.
    dimension : int
        Number of dimensions of the sequence. Must be between 1
        and 20 (inclusive).
    n_bits : int, optional
        Number of bits of precision used for the generating
        matrices and the binary expansion of each coordinate.
        Must be >= 2. Default is 30.

    Returns
    -------
    points : ndarray of shape (`num_points`, `dimension`)
        The generated sequence points, with values in [0, 1).

    Raises
    ------
    ValueError
        If `num_points` < 1, `dimension` < 1, `dimension` > 20, or
        `n_bits` < 2.

    Examples
    --------
    >>> niederreiter_sequence(4, 2)
    array([[0.  , 0.  ],
           [0.5 , 0.5 ],
           [0.25, 0.75],
           [0.75, 0.25]])

    >>> niederreiter_sequence(8, 3)
    array([[0.    , 0.    , 0.    ],
           [0.5   , 0.5   , 0.25  ],
           [0.25  , 0.75  , 0.75  ],
           [0.75  , 0.25  , 0.5   ],
           [0.125 , 0.625 , 0.5625],
           [0.625 , 0.125 , 0.8125],
           [0.375 , 0.375 , 0.3125],
           [0.875 , 0.875 , 0.0625]])
    """
    if num_points < 1:
        raise ValueError("num_points must be at least 1")
    if dimension < 1:
        raise ValueError("dimension must be at least 1")
    if dimension > _MAX_DIMENSION:
        raise ValueError(
            "dimension must be at most 20 (the table of irreducible "
            "polynomials only covers dimensions 1 through 20)"
        )
    if n_bits < 2:
        raise ValueError("n_bits must be at least 2")

    index = np.arange(num_points, dtype=np.int64)
    # bits[n, r] is bit r of the point index n
    bits = (index[:, None] >> np.arange(n_bits, dtype=np.int64)) & 1
    weights = 2.0 ** -(np.arange(n_bits, dtype=np.float64) + 1.0)

    points = np.empty((num_points, dimension), dtype=np.float64)
    for j, poly in enumerate(_IRREDUCIBLE_POLYS[:dimension]):
        matrix = _generating_matrix(poly, n_bits).astype(np.int64)
        digits = (bits @ matrix.T) % 2
        points[:, j] = digits @ weights

    return points


def _inverse_series(poly: int, length: int) -> list:
    r"""
    Coefficients of the Laurent series of the inverse of a polynomial
    over GF(2):

    $$\frac{1}{b(x)} = \sum_{n \ge m} v_n \, x^{-n}$$

    For a monic $$b(x) = \sum_{i=0}^{m} b_i x^i$$ they follow the
    recurrence

    $$v_m = 1, \qquad v_n = \sum_{l=1}^{m} b_{m-l} \, v_{n-l}
    \pmod 2 \quad (n > m)$$

    Parameters
    ----------
    poly : int
        Bit mask of the polynomial $$b$$ over GF(2), of degree
        $$m \ge 1$$.
    length : int
        Number of coefficients to compute.

    Returns
    -------
    series : list of int
        ``series[n]`` is $$v_n$$ for ``n = 0, ..., length - 1``. The
        first $$m$$ are 0 and ``series[m]`` is 1.
    """
    degree = _poly_degree(poly)
    series = [0] * length
    if degree < length:
        series[degree] = 1
    for n in range(degree + 1, length):
        value = 0
        for lag in range(1, degree + 1):
            if (poly >> (degree - lag)) & 1:
                value ^= series[n - lag]
        series[n] = value
    return series


def _generating_matrix(poly: int, n_bits: int) -> np.ndarray:
    r"""
    Build the binary generating matrix for one dimension.

    With $$e$$ the degree of the polynomial $$p$$, row $$j$$ (0-based)
    is written

    $$j = (q - 1) e + k, \quad 0 \le k < e$$

    and ``matrix[j, r]`` is the coefficient of $$x^{-r-1}$$ in the
    Laurent series of $$x^k / p(x)^q$$.

    Parameters
    ----------
    poly : int
        Bit mask of the irreducible polynomial over GF(2) of the
        dimension.
    n_bits : int
        Size of the (square) generating matrix.

    Returns
    -------
    matrix : ndarray of shape (`n_bits`, `n_bits`)
        The binary generating matrix, with dtype ``np.uint8``.
    """
    degree = _poly_degree(poly)
    matrix = np.zeros((n_bits, n_bits), dtype=np.uint8)
    power = 1
    for row in range(n_bits):
        k = row % degree
        if k == 0:
            # next power of the polynomial: poly ** q
            power = _poly_mul(power, poly)
            series = _inverse_series(power, n_bits + degree)
        # x**k / poly**q: the coefficient of x**(-r-1) is series[k+r+1]
        matrix[row, :] = series[k + 1 : k + 1 + n_bits]

    return matrix
