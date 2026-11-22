"""
Hartley's small composite design.

A standard central composite design augments a full :math:`2^k`
factorial with axial (star) points and center runs. Hartley's small
composite design instead augments a small regular two-level fractional
factorial in which no two-factor interaction is aliased with another
two-factor interaction (a main effect may be aliased with one: the star
points separate them) with star points and center runs. This reduces
the run count while still supporting the full quadratic model.

References
----------
Hartley, H. O. (1959). Smallest composite designs for quadratic response
    surfaces. *Biometrics*, 15(4), 611-624.
Box, G. E. P. and Draper, N. R. (2007). *Response Surfaces, Mixtures, and
    Ridge Analyses*, 2nd edition. Wiley.
NIST/SEMATECH e-Handbook of Statistical Methods, Section 5.3.3.6.2 -
    "Constructing response surface designs",
    https://www.itl.nist.gov/div898/handbook/pri/section3/pri336.htm
"""

from __future__ import annotations

import itertools

import numpy as np

from pydoe.factorial.factorial import ff2n
from pydoe.response_surface.center_design import repeat_center
from pydoe.response_surface.union import union


__all__ = ["small_composite_design"]

# Steps the search for a cube of 2**m runs may take before it tries 2**(m+1)
# runs. shortcut: the budget can stop a search that would have succeeded, so
# from 19 factors on the cube may be larger than the smallest possible; up to
# 18 factors the cubes found are the smallest (a smaller cube was ruled out by
# an exhaustive search). Raise the budget, or tabulate the larger cubes, if
# designs for that many factors are needed.
_SEARCH_BUDGET = 20_000


class _Search:
    """Depth-first search for columns whose pairwise sums all differ.

    Parameters
    ----------
    candidates : list of int
        The generated columns to choose from, in the order to try them.
    """

    def __init__(self, candidates: list[int]) -> None:
        self.candidates = candidates
        self.steps = _SEARCH_BUDGET

    def extend(
        self, chosen: list[int], sums: set[int], start: int, need: int
    ) -> list[int] | None:
        """Add ``need`` candidates, from ``start`` on, to ``chosen``.

        Parameters
        ----------
        chosen : list of int
            The columns chosen so far.
        sums : set of int
            The pairwise sums of ``chosen``.
        start : int
            The first candidate to try.
        need : int
            How many columns to add.

        Returns
        -------
        list of int or None
            The extended columns, or ``None`` if there is no extension, or
            the search budget ran out first.
        """
        if need == 0:
            return chosen
        for index in range(start, len(self.candidates) - need + 1):
            self.steps -= 1
            if self.steps < 0:
                return None
            column = self.candidates[index]
            new = [column ^ c for c in chosen]
            if sums.isdisjoint(new):
                found = self.extend(
                    [*chosen, column], sums.union(new), index + 1, need - 1
                )
                if found is not None:
                    return found
        return None


def _cube_columns(n: int) -> tuple[int, list[int]]:
    """Find the columns of the cube of a small composite design.

    The columns are vectors over GF(2) with ``m`` bits, one bit per base
    factor: base factor ``i`` is ``1 << i``, and a generated factor is the
    product of the base factors whose bits it sets. No two two-factor
    interactions are aliased when no four columns sum to zero, that is when
    all pairwise sums of the columns differ. The search takes the base
    factors, then adds generated columns, higher-order products first, by
    depth-first search, for the smallest ``m`` that allows ``n`` columns.

    Parameters
    ----------
    n : int
        Number of factors.

    Returns
    -------
    m : int
        Number of base factors: the cube has ``2**m`` runs.
    columns : list of int
        The ``n`` columns, base factors first.
    """
    m = int(n).bit_length()  # n distinct nonzero columns need 2**m - 1 >= n
    while m < n:
        base = [1 << i for i in range(m)]
        candidates = sorted(
            (v for v in range(1, 2**m) if v.bit_count() >= 2),
            key=lambda v: (-v.bit_count(), v),
        )
        pair_sums = {a ^ b for a, b in itertools.combinations(base, 2)}
        found = _Search(candidates).extend(base, pair_sums, 0, n - m)
        if found is not None:
            return m, found
        m += 1
    return n, [1 << i for i in range(n)]  # the full factorial


def _small_composite_cube(n: int) -> np.ndarray:
    """Return the cube of a small composite design for ``n`` factors.

    Parameters
    ----------
    n : int
        Number of factors.

    Returns
    -------
    np.ndarray
        The cube, with :math:`2^m` runs and coded levels -1 and +1.
    """
    m, columns = _cube_columns(n)
    base = ff2n(m)
    return np.column_stack([
        np.prod(base[:, [b for b in range(m) if (v >> b) & 1]], axis=1)
        for v in columns
    ])


def small_composite_design(
    n: int, center: np.ndarray[int] | tuple[int, int] = (4, 4)
) -> np.ndarray:
    r"""
    Generate Hartley's small composite design for ``n`` factors.

    The "cube" portion is the smallest regular two-level fraction the
    search finds, with :math:`n_c` runs (rather than the :math:`2^n`
    runs of a full factorial), in which no two-factor interaction is
    aliased with another two-factor interaction, so that the full
    quadratic model can be fitted. Star points are placed at distance
    ``alpha`` along each axis, with
    :math:`\\alpha` chosen by the same orthogonal-blocking formula used
    by [`star`][pydoe.star], but with :math:`n_c` substituted for
    :math:`2^n`:

    .. math::

        \\alpha = \\left(n \\,
            \\frac{1 + n_{ao} / n_a}{1 + n_{co} / n_c}\\right)^{1/2}

    where :math:`n_a = 2n` is the number of axial points, and
    :math:`n_{co}`, :math:`n_{ao}` are the number of center runs added
    to the cube and star portions respectively (``center``).

    Parameters
    ----------
    n : int
        Number of factors, must be at least 3.
    center : array_like of 2 ints, optional
        Number of center runs to add to the cube portion and the star
        portion, respectively. Defaults to ``(4, 4)``.

    Returns
    -------
    ndarray of shape (n_c + 2*n + sum(center), n)
        Design matrix with coded levels, cube portion first followed
        by the star portion, where :math:`n_c` is the number of cube
        runs.

    Raises
    ------
    ValueError
        If ``n < 3`` or ``center`` does not have exactly 2 elements.

    Examples
    --------
    >>> small_composite_design(4, center=(2, 2))
    array([[-1., -1., -1.,  1.],
           [-1., -1.,  1.,  1.],
           [-1.,  1., -1., -1.],
           [-1.,  1.,  1., -1.],
           [ 1., -1., -1., -1.],
           [ 1., -1.,  1., -1.],
           [ 1.,  1., -1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.],
           [-2.,  0.,  0.,  0.],
           [ 2.,  0.,  0.,  0.],
           [ 0., -2.,  0.,  0.],
           [ 0.,  2.,  0.,  0.],
           [ 0.,  0., -2.,  0.],
           [ 0.,  0.,  2.,  0.],
           [ 0.,  0.,  0., -2.],
           [ 0.,  0.,  0.,  2.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.]])

    For 4 factors this needs only 20 runs, versus 30 for a standard
    central composite design built on the full :math:`2^4` factorial:

    >>> small_composite_design(4, center=(2, 2)).shape[0]
    20

    Notes
    -----
    The cube may alias a main effect with a two-factor interaction (a
    word of length 3 in its defining relation), but no two two-factor
    interactions with each other (no word of length 4): the star points
    then separate the main effects from the interactions (Hartley, 1959).
    For 3, 4, 5, 6, 7 and 9 factors the cube has 4, 8, 16, 16, 32 and 64
    runs, as in Box and Draper (2007, p. 501). The cube is found by a
    search, and is the smallest possible for up to 18 factors.

    With ``center=(0, 0)`` the star distance is :math:`\sqrt{n}`, so
    every run lies on a sphere and the intercept cannot be told apart
    from the sum of the squared terms: give at least one center run.

    References
    ----------
    Hartley, H. O. (1959). Smallest composite designs for quadratic
    response surfaces. *Biometrics*, 15(4), 611-624.

    Box, G. E. P. and Draper, N. R. (2007). *Response Surfaces, Mixtures,
    and Ridge Analyses*, 2nd edition. Wiley.
    """
    if n < 3:
        raise ValueError(f"n must be at least 3, got {n}")
    if len(center) != 2:
        raise ValueError(
            f'Invalid number of values for "center" (expected 2, but got '
            f"{len(center)})"
        )

    H1 = _small_composite_cube(n)
    nc = H1.shape[0]
    na = 2 * n
    nco, nao = center
    alpha = (n * (1 + nao / na) / (1 + nco / nc)) ** 0.5

    H2 = np.zeros((2 * n, n))
    for i in range(n):
        H2[2 * i : 2 * i + 2, i] = [-1, 1]
    H2 *= alpha

    H1 = union(H1, repeat_center(n, nco))
    H2 = union(H2, repeat_center(n, nao))
    return union(H1, H2)
