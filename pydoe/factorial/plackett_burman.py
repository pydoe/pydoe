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

import numpy as np
from scipy.linalg import hankel, toeplitz


__all__ = ["pbdesign"]

# Plackett and Burman's (1946) generating row for 36 runs, as Box and Draper
# (2007, p. 153) and Montgomery (2012, Table 8.23) print it. Their rows for
# 24, 44, 48 and 60 runs are identical to the rows of Paley's first
# construction, which builds them; 36 is not of that form.
_PRINTED_ROWS = {36: "-+-+++---+++++-+++--+----+-+-++--+-"}

# Box and Draper (2007), Table 5.8: the three 9 x 9 blocks X, Y and Z of
# Plackett and Burman's 28-run design, row by row. The design is the blocks
# written as X Y Z / Z X Y / Y Z X, then a run of minus signs (Montgomery,
# 2012, Table 8.23).
_BLOCKS_28 = (
    (
        "+-++++---",
        "++-+++---",
        "-+++++---",
        "---+-++++",
        "---++-+++",
        "----+++++",
        "+++---+-+",
        "+++---++-",
        "+++----++",
    ),
    (
        "-+---+--+",
        "--++--+--",
        "+---+--+-",
        "--+-+---+",
        "+----++--",
        "-+-+---+-",
        "--+--+-+-",
        "+--+----+",
        "-+--+-+--",
    ),
    (
        "++-+-++-+",
        "-++++-++-",
        "+-+-++-++",
        "+-+++-+-+",
        "++--++++-",
        "-+++-+-++",
        "+-++-+++-",
        "++-++--++",
        "-++-+++-+",
    ),
)

# Baumert, Golomb and Hall (1962): the first rows of four symmetric
# circulants A, B, C and D of order 23 with A^2 + B^2 + C^2 + D^2 = 92 I,
# which give a Hadamard matrix of order 92 in the Goethals-Seidel array.
_WILLIAMSON_23 = (
    "++---+---+-++-+---+---+",
    "+-++-++--++++++--++-++-",
    "+++---++-+-++-+-++---++",
    "+++-+++-+------+-+++-++",
)


def _signs(row: str) -> np.ndarray:
    """Return a row of ``+`` and ``-`` as an array of +1 and -1.

    Parameters
    ----------
    row : str
        The signs.

    Returns
    -------
    np.ndarray
        One float per sign.
    """
    return np.array([1.0 if sign == "+" else -1.0 for sign in row])


def _cyclic(row: np.ndarray) -> np.ndarray:
    """Return the Hadamard matrix of a cyclic Plackett-Burman design.

    The design's first column is ``row``, each next column is the one
    before moved down one run, and a run of minus signs follows; a column
    of ones is put in front.

    Parameters
    ----------
    row : np.ndarray
        The generating row, of length ``N - 1``.

    Returns
    -------
    np.ndarray
        The ``N x N`` Hadamard matrix, first column all ones.
    """
    design = np.column_stack([np.roll(row, shift) for shift in range(len(row))])
    design = np.vstack([design, -np.ones(len(row))])
    return np.column_stack([np.ones(len(design)), design])


def _is_prime(m: int) -> bool:
    """Return whether ``m`` is a prime number.

    Parameters
    ----------
    m : int
        The number.

    Returns
    -------
    bool
        ``True`` if ``m`` is prime.
    """
    return m > 1 and all(m % d for d in range(2, int(m**0.5) + 1))


def _jacobsthal(q: int) -> np.ndarray | None:
    """Return the Jacobsthal matrix of GF(q), for a prime ``q`` or its square.

    ``Q[a, b]`` is the quadratic character of ``b - a``: 0 when it is zero,
    +1 when it is a non-zero square and -1 otherwise. GF(p^2) is built as
    ``a + b x`` with ``x^2 = r`` for a non-square ``r`` modulo ``p``.

    Parameters
    ----------
    q : int
        The order of the field.

    Returns
    -------
    np.ndarray or None
        The ``q x q`` matrix, or ``None`` if ``q`` is neither an odd prime
        nor the square of one.
    """
    if _is_prime(q) and q > 2:
        p, degree = q, 1
    elif _is_prime(round(q**0.5)) and round(q**0.5) ** 2 == q and q % 2:
        p, degree = round(q**0.5), 2
    else:
        return None
    squares_mod_p = {(v * v) % p for v in range(1, p)}
    r = next(v for v in range(2, p) if v not in squares_mod_p)
    elements = [
        (a, b) for b in range(p if degree == 2 else 1) for a in range(p)
    ]
    squares = {
        ((a * a + b * b * r) % p, (2 * a * b) % p) for a, b in elements[1:]
    }
    character = {
        e: 0 if e == (0, 0) else (1 if e in squares else -1) for e in elements
    }
    return np.array([
        [character[((c - a) % p, (d - b) % p)] for c, d in elements]
        for a, b in elements
    ])


def _goethals_seidel(rows: tuple[str, str, str, str]) -> np.ndarray:
    """Return the Hadamard matrix of the Goethals-Seidel array.

    Parameters
    ----------
    rows : tuple of 4 str
        The first rows, in signs, of the four circulants.

    Returns
    -------
    np.ndarray
        The Hadamard matrix of order ``4 t``, for rows of length ``t``.
    """
    a, b, c, d = (
        np.array([np.roll(_signs(row), shift) for shift in range(len(row))])
        for row in rows
    )
    r = np.eye(len(rows[0]))[::-1]  # the back-diagonal matrix
    return np.block([
        [a, b @ r, c @ r, d @ r],
        [-b @ r, a, -d.T @ r, c.T @ r],
        [-c @ r, d.T @ r, a, -b.T @ r],
        [-d @ r, -c.T @ r, b.T @ r, a],
    ])


def _published(runs: int) -> np.ndarray | None:
    """Return the cyclic or block design of ``runs`` runs, as a Hadamard
    matrix: Plackett and Burman's printed row for 36 runs, Paley's first
    construction when ``runs - 1`` is a prime equal to 3 (mod 4), or
    Plackett and Burman's blocks for 28 runs.

    Parameters
    ----------
    runs : int
        The number of runs, a multiple of 4.

    Returns
    -------
    np.ndarray or None
        The matrix, first column all ones, or ``None``.
    """
    q = runs - 1
    if runs in _PRINTED_ROWS:
        return _cyclic(_signs(_PRINTED_ROWS[runs]))
    if _is_prime(q) and q % 4 == 3:
        # Paley's first construction: +1 at 0 and on the non-zero squares
        # modulo q, so that each column has as many + as - signs. For 24,
        # 44, 48 and 60 runs this is the row Box and Draper (2007, p. 153)
        # print.
        squares = {0} | {(v * v) % q for v in range(1, q)}
        return _cyclic(
            np.array([1.0 if v in squares else -1.0 for v in range(q)])
        )
    if runs == 28:
        x, y, z = (
            np.array([_signs(row) for row in block]) for block in _BLOCKS_28
        )
        design = np.vstack([
            np.hstack([x, y, z]),
            np.hstack([z, x, y]),
            np.hstack([y, z, x]),
            -np.ones((1, 27)),
        ])
        return np.column_stack([np.ones(28), design])
    return None


def _paley_ii(runs: int) -> np.ndarray | None:
    """Return Paley's second construction of order ``runs``, if it applies.

    It needs ``q = runs / 2 - 1`` to be a prime, or the square of one, with
    ``q = 1 (mod 4)``: for example 52, 76 and 100 runs.

    Parameters
    ----------
    runs : int
        The number of runs, a multiple of 4.

    Returns
    -------
    np.ndarray or None
        The matrix, first column all ones, or ``None``.
    """
    half = runs // 2
    q = half - 1
    jacobsthal = _jacobsthal(q) if q >= 5 and q % 4 == 1 else None
    if jacobsthal is None:
        return None
    conference = np.zeros((half, half))  # symmetric, since q = 1 (mod 4)
    conference[0, 1:] = conference[1:, 0] = 1
    conference[1:, 1:] = jacobsthal
    eye = np.eye(half)
    h = np.block([
        [conference + eye, conference - eye],
        [conference - eye, -conference - eye],
    ])
    return h * h[:, [0]]


def _hadamard(runs: int) -> np.ndarray | None:
    """Return a Hadamard matrix of order ``runs`` with a first column of ones.

    The constructions are tried in this order: the cyclic and block designs
    of ``_published``, doubling a smaller matrix, Paley's second
    construction, and the Goethals-Seidel array for 92 runs.

    Parameters
    ----------
    runs : int
        The order, a multiple of 4.

    Returns
    -------
    np.ndarray or None
        The matrix, or ``None`` if none of the constructions reaches
        ``runs``.
    """
    h = _published(runs)
    if h is None and runs % 8 == 0:
        inner = _classical(runs // 2)
        if inner is None:
            inner = _hadamard(runs // 2)
        if inner is not None:
            h = np.block([[inner, inner], [inner, -inner]])
    if h is None:
        h = _paley_ii(runs)
    if h is None and runs == 92:
        h = _goethals_seidel(_WILLIAMSON_23)
        h *= h[:, [0]]
    return h


def pbdesign(n: int) -> np.ndarray:
    """
    Generate a Plackett-Burman design

    Parameter
    ---------
    n : int
        The number of factors to create a matrix for.

    Returns
    -------
    H : 2d-array
        An orthogonal design matrix with n columns, one for each factor, and
        the number of rows being the next multiple of 4 higher than n (e.g.,
        for 1-3 factors there are 4 rows, for 4-7 factors there are 8 rows,
        etc.)

    Example
    -------

    A 3-factor design::

        >>> pbdesign(3)
        array([[-1., -1.,  1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1.,  1.]])

    A 5-factor design::

        >>> pbdesign(5)
        array([[-1., -1.,  1., -1.,  1.],
               [ 1., -1., -1., -1., -1.],
               [-1.,  1., -1., -1.,  1.],
               [ 1.,  1.,  1., -1., -1.],
               [-1., -1.,  1.,  1., -1.],
               [ 1., -1., -1.,  1.,  1.],
               [-1.,  1., -1.,  1., -1.],
               [ 1.,  1.,  1.,  1.,  1.]])

    A 27-factor design has Plackett and Burman's 28 runs:

        >>> pbdesign(27).shape
        (28, 27)

    Raises
    ------
    ValueError
        If n is not a positive integer, or no design is built here for the
        number of runs: every multiple of 4 up to 112 is available, and the
        first that is not is 116.

    Notes
    -----
    Run counts of the form :math:`2^e`, 12 and :math:`20 \\times 2^e` double
    the 1-, 12- or 20-run core, as before. Up to 112 runs, the others use:

    - Paley's first construction, for 24, 44, 48, 60, 68, 72, 84, 104 and
      108 runs. For 24 to 60 runs it gives the cyclic designs of Plackett
      and Burman (1946), with the generating rows Box and Draper (2007,
      p. 153) print.
    - Plackett and Burman's generating row for 36 runs, and their blocks
      for 28 runs.
    - Paley's second construction, for 52, 76 and 100 runs.
    - Doubling, for 56, 88, 96 and 112 runs.
    - The Williamson matrices of Baumert, Golomb and Hall (1962), for 92
      runs. Plackett and Burman give no design of this size.

    References
    ----------
    Plackett, R. L. and Burman, J. P. (1946). The design of optimum
    multifactorial experiments. *Biometrika*, 33(4), 305-325.

    Baumert, L., Golomb, S. W. and Hall, M. (1962). Discovery of an
    Hadamard matrix of order 92. *Bulletin of the American Mathematical
    Society*, 68(3), 237-238.

    Box, G. E. P. and Draper, N. R. (2007). *Response Surfaces, Mixtures,
    and Ridge Analyses*, 2nd edition. Wiley.
    """
    if n <= 0:
        raise ValueError("Number of factors must be a positive integer")
    keep = int(n)
    runs = 4 * (int(n / 4) + 1)  # the next multiple of 4 above n
    H = _classical(runs)
    if H is not None:
        return np.flipud(H[:, 1 : (keep + 1)])
    H = _hadamard(runs)
    if H is None:
        raise ValueError(
            f"No Plackett-Burman design with {runs} runs is built here, so "
            f"{keep} factors cannot be accommodated. Every multiple of 4 up "
            "to 112 runs is available."
        )
    return H[:, 1 : (keep + 1)]


def _classical(runs: int) -> np.ndarray | None:
    """Return the original construction for ``runs`` of the form 2^e, 12 or
    20 x 2^e, or ``None`` for any other number of runs.

    The 1-, 12- or 20-run core is doubled ``e`` times. Doubling the 12-run
    core is not Plackett and Burman's design, so 24, 48, ... runs come from
    ``_hadamard`` instead.

    Parameters
    ----------
    runs : int
        The number of runs, a multiple of 4.

    Returns
    -------
    H : np.ndarray or None
        The Hadamard matrix, first column all ones, or ``None``.
    """
    n = runs
    f, e = np.frexp([n, n / 12.0, n / 20.0])
    k = [
        idx
        for idx, val in enumerate(np.logical_and(np.isclose(f, 0.5), e > 0))
        if val
    ]
    if not k or (k[0] == 1 and e[1] != 1):  # 12 x 2^e with e >= 1
        return None

    k = k[0]
    e = e[k] - 1

    if k == 0:  # N = 1*2**e
        H = np.ones((1, 1))
    elif k == 1:  # N = 12*2**e
        H = np.vstack((
            np.ones((1, 12)),
            np.hstack((
                np.ones((11, 1)),
                toeplitz(
                    [-1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1],
                    [-1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1],
                ),
            )),
        ))
    elif k == 2:  # N = 20*2**e
        H = np.vstack((
            np.ones((1, 20)),
            np.hstack((
                np.ones((19, 1)),
                hankel(
                    [
                        -1,
                        -1,
                        1,
                        1,
                        -1,
                        -1,
                        -1,
                        -1,
                        1,
                        -1,
                        1,
                        -1,
                        1,
                        1,
                        1,
                        1,
                        -1,
                        -1,
                        1,
                    ],
                    [
                        1,
                        -1,
                        -1,
                        1,
                        1,
                        -1,
                        -1,
                        -1,
                        -1,
                        1,
                        -1,
                        1,
                        -1,
                        1,
                        1,
                        1,
                        1,
                        -1,
                        -1,
                    ],
                ),
            )),
        ))

    # Kronecker product construction
    for _ in range(e):
        H = np.vstack((np.hstack((H, H)), np.hstack((H, -H))))

    return H
