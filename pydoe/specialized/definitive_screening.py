"""
Definitive screening designs (DSD).

A definitive screening design (Jones & Nachtsheim, 2011) is a
three-level design for *k* factors that requires only :math:`2k + 1`
runs, yet:

- estimates all main effects independently of two-factor interactions
  and of each other,
- estimates all quadratic effects, and
- keeps every two-factor interaction clear of all main effects (though
  not of other two-factor interactions).

This makes DSDs attractive screening designs that, unlike
two-level designs, can also detect curvature without any follow-up
experiments.

References
----------
Jones, B., & Nachtsheim, C. J. (2011). A class of three-level designs
    for definitive screening in the presence of second-order effects.
    *Journal of Quality Technology*, 43(1), 1-15.
Xiao, L., Lin, D. K. J., & Bai, F. (2012). Constructing definitive
    screening designs using conference matrices. *Journal of Quality
    Technology*, 44(1), 2-8.
"""

from __future__ import annotations

import numpy as np


__all__ = ["definitive_screening_design"]


def definitive_screening_design(k: int) -> np.ndarray:
    r"""
    Generate a definitive screening design for ``k`` factors.

    The design is built from a Paley conference matrix :math:`C` of
    order :math:`k`, which satisfies :math:`C^T C = (k - 1) I` with
    zero diagonal and :math:`\\pm 1` off-diagonal entries. Stacking a
    row of zeros (the center run) on top of :math:`C` and its
    fold-over :math:`-C` gives the :math:`(2k + 1) \\times k` design:

    .. math::

        D = \\begin{bmatrix} 0 \\\\ C \\\\ -C \\end{bmatrix}

    A Paley conference matrix of order :math:`k` exists when
    :math:`q = k - 1` is an odd prime, so ``k`` must be one greater
    than an odd prime (e.g. 4, 6, 8, 12, 14, 18, 20, 24, ...).

    Parameters
    ----------
    k : int
        Number of factors. ``k - 1`` must be an odd prime.

    Returns
    -------
    ndarray of shape (2*k + 1, k)
        Design matrix with three coded levels: -1, 0, and 1. The first
        row is the all-zero center run.

    Raises
    ------
    ValueError
        If ``k - 1`` is not an odd prime.

    Examples
    --------
    >>> definitive_screening_design(4)
    array([[ 0.,  0.,  0.,  0.],
           [ 0.,  1.,  1.,  1.],
           [-1.,  0.,  1., -1.],
           [-1., -1.,  0.,  1.],
           [-1.,  1., -1.,  0.],
           [ 0., -1., -1., -1.],
           [ 1.,  0., -1.,  1.],
           [ 1.,  1.,  0., -1.],
           [ 1., -1.,  1.,  0.]])

    Main effects are mutually orthogonal:

    >>> D = definitive_screening_design(4)
    >>> D.T @ D
    array([[6., 0., 0., 0.],
           [0., 6., 0., 0.],
           [0., 0., 6., 0.],
           [0., 0., 0., 6.]])

    Only :math:`2k + 1 = 9` runs are needed for 4 factors:

    >>> D.shape
    (9, 4)
    """
    q = k - 1
    if q < 3 or q % 2 == 0 or not _is_prime(q):
        raise ValueError(
            f"k - 1 = {q} must be an odd prime number, got k = {k}"
        )

    C = _paley_conference_matrix(q)
    design = np.vstack([np.zeros((1, k)), C, -C])
    return design + 0.0  # normalize away signed zeros (-0.)


def _is_prime(n: int) -> bool:
    """
    Check whether ``n`` is a prime number.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    is_prime : bool
        ``True`` if ``n`` is prime, ``False`` otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def _paley_conference_matrix(q: int) -> np.ndarray:
    """
    Construct the Paley conference matrix of order ``q + 1``.

    Parameters
    ----------
    q : int
        An odd prime number.

    Returns
    -------
    C : ndarray of shape (q + 1, q + 1)
        Symmetric or skew-symmetric conference matrix satisfying
        :math:`C^T C = q I`, with zero diagonal and :math:`\\pm 1`
        off-diagonal entries.
    """
    squares = {(i * i) % q for i in range(1, q)}
    chi = np.zeros(q)
    for a in range(1, q):
        chi[a] = 1.0 if a in squares else -1.0

    Q = np.array([[chi[(j - i) % q] for j in range(q)] for i in range(q)])

    n = q + 1
    C = np.zeros((n, n))
    C[0, 1:] = 1.0
    C[1:, 0] = 1.0 if q % 4 == 1 else -1.0
    C[1:, 1:] = Q
    return C
