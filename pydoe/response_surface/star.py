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

from typing import Literal

import numpy as np


def star(
    n: int,
    alpha: Literal["faced", "orthogonal", "rotatable"] = "faced",
    center: np.ndarray[int] | tuple[int] = (1, 1),
    *,
    n_cube: int | None = None,
) -> tuple[np.ndarray, float]:
    """
    Create the star points of various design matrices

    Parameters
    ----------
    n : int
        The number of variables in the design

    Optional
    --------
    alpha : str
        Available values are 'faced' (default), 'orthogonal', or 'rotatable'
    center : array
        A 1-by-2 array of integers indicating the number of center points
        assigned in each block of the response surface design. Default is
        (1, 1).
    n_cube : int, optional
        The number of runs in the factorial (cube) portion of the design.
        ``None`` (default) counts the :math:`2^n` runs of the full
        factorial. Give the run count of a fractional factorial cube so
        that the 'orthogonal' and 'rotatable' distances use it: the
        rotatable distance is then ``n_cube ** 0.25``. 'faced' does not
        use it, but it must still be a positive integer.

    Returns
    -------
    H : 2d-array
        The star-point portion of the design matrix (i.e. at +/- alpha)
    a : scalar
        The alpha value to scale the star points with.

    Raises
    ------
    ValueError
        If ``alpha`` is not one of the accepted strings, or ``n_cube`` is
        not a positive integer.

    Examples
    --------
    ::

        >>> star(3)
        (array([[-1.,  0.,  0.],
               [ 1.,  0.,  0.],
               [ 0., -1.,  0.],
               [ 0.,  1.,  0.],
               [ 0.,  0., -1.],
               [ 0.,  0.,  1.]]), 1)

    For 5 factors on the 16-run half fraction, the rotatable distance is
    :math:`16^{1/4} = 2`, not the :math:`32^{1/4}` of the full factorial:

        >>> float(star(5, alpha="rotatable", n_cube=16)[1])
        2.0

    """
    if n_cube is None:
        n_cube = 2**n
    elif (
        isinstance(n_cube, bool)
        or not isinstance(n_cube, int | np.integer)
        or n_cube < 1
    ):
        raise ValueError(f'"n_cube" must be a positive integer, got {n_cube!r}')

    # Star points at the center of each face of the factorial
    if alpha == "faced":
        a = 1
    elif alpha == "orthogonal":
        nc = n_cube  # factorial points
        nco = center[0]  # center points to factorial
        na = 2 * n  # axial points
        nao = center[1]  # center points to axial design
        # value of alpha in orthogonal design
        a = (n * (1 + nao / float(na)) / (1 + nco / float(nc))) ** 0.5
    elif alpha == "rotatable":
        nc = n_cube  # number of factorial points
        a = nc ** (0.25)  # value of alpha in rotatable design
    else:
        raise ValueError(f'Invalid value for "alpha": {alpha}')

    # Create the actual matrix now.
    H = np.zeros((2 * n, n))
    for i in range(n):
        H[2 * i : 2 * i + 2, i] = [-1, 1]

    H *= a

    return H, a
