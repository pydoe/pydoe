"""
This code was originally published by the following individuals for use with
Scilab:
    Copyright (C) 2012 - 2013 - Michael Baudin
    Copyright (C) 2012 - Maria Christopoulou
    Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
    Copyright (C) 2009 - Yann Collette
    Copyright (C) 2009 - CEA - Jean-Marc Martinez

    website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

Much thanks goes to these individuals. It has been converted to Python by
Abraham Lee.
"""

from __future__ import annotations

import numpy as np

from pydoe.factorial.factorial import ff2n
from pydoe.response_surface.center_design import repeat_center


__all__ = ["bbdesign"]


def _cyclic(base: tuple[int, ...], n: int) -> tuple[tuple[int, ...], ...]:
    """Develop the block ``base`` cyclically modulo ``n``.

    Parameters
    ----------
    base : tuple of int
        The factors of the first block, numbered from 0.
    n : int
        The number of factors.

    Returns
    -------
    blocks : tuple of tuple of int
        The ``n`` blocks ``base + i`` (mod ``n``), ``i = 0, ..., n - 1``.
    """
    return tuple(tuple(sorted((j + i) % n for j in base)) for i in range(n))


# Box and Behnken (1960), Table 4: the factors (numbered from 0) of each block
# of an incomplete-block design. Each block carries a two-level factorial in
# its factors, with every other factor at its centre. Six, nine, ten, twelve
# and sixteen factors use partially balanced designs; seven and eleven use
# balanced ones. Seven factors are written cyclically, which is the published
# design up to a relabelling of the factors; the others are as printed.
_PUBLISHED_BLOCKS: dict[int, tuple[tuple[int, ...], ...]] = {
    6: ((0, 1, 3), (1, 2, 4), (2, 3, 5), (0, 3, 4), (1, 4, 5), (0, 2, 5)),
    7: _cyclic((0, 1, 3), 7),
    # Five sets of three blocks; the fifth repeats the first.
    9: (
        *((0, 3, 6), (1, 4, 7), (2, 5, 8)),
        *((0, 1, 2), (3, 4, 5), (6, 7, 8)),
        *((0, 4, 8), (2, 3, 7), (1, 5, 6)),
        *((0, 5, 7), (1, 3, 8), (2, 4, 6)),
        *((0, 3, 6), (1, 4, 7), (2, 5, 8)),
    ),
    10: (
        (1, 5, 6, 9),
        (0, 1, 4, 9),
        (1, 2, 6, 7),
        (1, 3, 5, 8),
        (0, 7, 8, 9),
        (2, 3, 4, 9),
        (0, 3, 6, 7),
        (2, 4, 6, 8),
        (0, 2, 5, 8),
        (3, 4, 5, 7),
    ),
    11: _cyclic((0, 1, 2, 4, 7), 11),
    12: _cyclic((0, 1, 4, 6), 12),
    # Six sets of four blocks, each set a partition of the sixteen factors.
    16: (
        *((0, 1, 5, 8), (2, 3, 7, 10), (4, 9, 12, 13), (6, 11, 14, 15)),
        *((1, 2, 6, 9), (0, 3, 4, 11), (5, 10, 13, 14), (7, 8, 12, 15)),
        *((1, 4, 5, 12), (3, 6, 7, 14), (0, 8, 9, 13), (2, 10, 11, 15)),
        *((2, 5, 6, 13), (0, 4, 7, 15), (1, 9, 10, 14), (3, 8, 11, 12)),
        *((0, 2, 12, 14), (1, 3, 13, 15), (4, 6, 8, 10), (5, 7, 9, 11)),
        *((3, 5, 9, 15), (2, 4, 8, 14), (0, 6, 10, 12), (1, 7, 11, 13)),
    ),
}

# Factor counts whose blocks of five carry the half fraction
# x1 x2 x3 x4 x5 = +1 (Table 4, design 8) rather than the full 2^5 factorial.
_HALF_FRACTION = frozenset({11})


def _published_design(n: int) -> np.ndarray:
    """Return Box and Behnken's published design for ``n`` factors.

    Parameters
    ----------
    n : int
        The number of factors: a key of ``_PUBLISHED_BLOCKS``.

    Returns
    -------
    H : 2d-array
        The design without centre points, block by block.
    """
    parts = []
    for block in _PUBLISHED_BLOCKS[n]:
        corners = ff2n(len(block))
        if n in _HALF_FRACTION:
            corners = corners[np.prod(corners, axis=1) > 0]
        part = np.zeros((len(corners), n))
        part[:, list(block)] = corners
        parts.append(part)
    return np.vstack(parts)


def bbdesign(n: int, center: int | None = None) -> np.ndarray:
    """
    Create a Box-Behnken design

    Parameters
    ----------
    n : int
        The number of factors in the design

    Optional
    --------
    center : int
        The number of center points to include. By default, 3 for 3 and 4
        factors, 6 for 5 to 7 factors, 12 for 11 and 12 factors, and ``n``
        for any other number of factors.

    Returns
    -------
    mat : 2d-array
        The design matrix

    Examples
    --------
    ::

        >>> bbdesign(3)
        array([[-1., -1.,  0.],
               [-1.,  1.,  0.],
               [ 1., -1.,  0.],
               [ 1.,  1.,  0.],
               [-1.,  0., -1.],
               [-1.,  0.,  1.],
               [ 1.,  0., -1.],
               [ 1.,  0.,  1.],
               [ 0., -1., -1.],
               [ 0., -1.,  1.],
               [ 0.,  1., -1.],
               [ 0.,  1.,  1.],
               [ 0.,  0.,  0.],
               [ 0.,  0.,  0.],
               [ 0.,  0.,  0.]])

    From 6 factors on, the design is Box and Behnken's published design:

        >>> bbdesign(7, center=0).shape
        (56, 7)

    Raises
    ------
    ValueError
        If n is less than 3.

    Notes
    -----
    For 3, 4 and 5 factors, every pair of factors carries a :math:`2^2`
    factorial with the other factors at their centre, which is the design
    Box and Behnken (1960) give. For 6, 7, 9, 10, 11, 12 and 16 factors they
    use balanced or partially balanced incomplete blocks of 3, 4 or 5
    factors, each block carrying a two-level factorial; these are the
    designs returned (48, 56, 120, 160, 176, 192 and 384 runs before the
    centre points). Box and Behnken published no design for 8, 13 to 15, or
    more than 16 factors: these pair every two factors.

    References
    ----------
    Box, G. E. P. and Behnken, D. W. (1960). Some new three level designs
    for the study of quantitative variables. *Technometrics*, 2(4), 455-475.
    """
    if n < 3:
        raise ValueError("Number of variables must be at least 3")

    if n in _PUBLISHED_BLOCKS:
        H = _published_design(n)
    else:
        H = _all_pairs_design(n)

    if center is None:
        if n <= 16:
            points = [0, 0, 0, 3, 3, 6, 6, 6, 8, 9, 10, 12, 12, 13, 14, 15, 16]
            center = points[n]
        else:
            center = n

    H = np.c_[H.T, repeat_center(n, center).T].T

    return H


def _all_pairs_design(n: int) -> np.ndarray:
    """Return a :math:`2^2` factorial in every pair of ``n`` factors.

    Parameters
    ----------
    n : int
        The number of factors.

    Returns
    -------
    H : 2d-array
        The design without centre points, pair by pair.
    """
    # First, compute a factorial DOE with 2 parameters
    H_fact = ff2n(2)
    # Now we populate the real DOE with this DOE

    # We made a factorial design on each pair of dimensions
    # - So, we created a factorial design with two factors
    # - Make two loops
    index = 0
    nb_lines = int((0.5 * n * (n - 1)) * H_fact.shape[0])
    H = repeat_center(n, nb_lines)

    for i in range(n - 1):
        for j in range(i + 1, n):
            index += 1
            H[
                max([0, (index - 1) * H_fact.shape[0]]) : index
                * H_fact.shape[0],
                i,
            ] = H_fact[:, 0]
            H[
                max([0, (index - 1) * H_fact.shape[0]]) : index
                * H_fact.shape[0],
                j,
            ] = H_fact[:, 1]

    return H
