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

from pydoe.factorial.factorial import ff2n
from pydoe.response_surface.center_design import repeat_center
from pydoe.response_surface.star import star
from pydoe.response_surface.union import union


__all__ = ["ccdesign"]


def ccdesign(
    n: int,
    center: np.ndarray[int] | tuple[int] = (4, 4),
    alpha: Literal["orthogonal", "o", "rotatable", "r"] = "orthogonal",
    face: Literal[
        "circumscribed", "ccc", "inscribed", "cci", "faced", "ccf"
    ] = "circumscribed",
) -> np.ndarray:
    """
    Central composite design

    Parameters
    ----------
    n : int
        The number of factors in the design.

    Optional
    --------
    center : int array
        A 1-by-2 array of integers, the number of center points in each block
        of the design. (Default: (4, 4)).
    alpha : str
        A string describing the effect of alpha has on the variance. ``alpha``
        can take on the following values:

        1. 'orthogonal' or 'o' (Default)

        2. 'rotatable' or 'r'

    face : str
        The relation between the start points and the corner (factorial) points.
        There are three options for this input:

        1. 'circumscribed' or 'ccc': This is the original form of the central
           composite design. The star points are at some distance ``alpha``
           from the center, based on the properties desired for the design.
           The start points establish new extremes for the low and high
           settings for all factors. These designs have circular, spherical,
           or hyperspherical symmetry and require 5 levels for each factor.
           Augmenting an existing factorial or resolution V fractional
           factorial design with star points can produce this design.

        2. 'inscribed' or 'cci': For those situations in which the limits
           specified for factor settings are truly limits, the CCI design
           uses the factors settings as the star points and creates a factorial
           or fractional factorial design within those limits (in other words,
           a CCI design is a scaled down CCC design with each factor level of
           the CCC design divided by ``alpha`` to generate the CCI design).
           This design also requires 5 levels of each factor.

        3. 'faced' or 'ccf': In this design, the star points are at the center
           of each face of the factorial space, so ``alpha`` = 1. This
           variety requires 3 levels of each factor. Augmenting an existing
           factorial or resolution V design with appropriate star points can
           also produce this design.

    Notes
    -----
    - Fractional factorial designs are not (yet) available here.
    - 'ccc' and 'cci' can be rotatable design, but 'ccf' cannot.
    - If ``face`` is specified, while ``alpha`` is not, then the default value
      of ``alpha`` is 'orthogonal'.

    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels -1 and 1

    Raises
    ------
    ValueError
        If input parameters are invalid.

    Examples
    --------
    ::

        >>> ccdesign(3)
        array([[-1.        , -1.        , -1.        ],
               [-1.        , -1.        ,  1.        ],
               [-1.        ,  1.        , -1.        ],
               [-1.        ,  1.        ,  1.        ],
               [ 1.        , -1.        , -1.        ],
               [ 1.        , -1.        ,  1.        ],
               [ 1.        ,  1.        , -1.        ],
               [ 1.        ,  1.        ,  1.        ],
               [ 0.        ,  0.        ,  0.        ],
               [ 0.        ,  0.        ,  0.        ],
               [ 0.        ,  0.        ,  0.        ],
               [ 0.        ,  0.        ,  0.        ],
               [-1.82574186,  0.        ,  0.        ],
               [ 1.82574186,  0.        ,  0.        ],
               [ 0.        , -1.82574186,  0.        ],
               [ 0.        ,  1.82574186,  0.        ],
               [ 0.        ,  0.        , -1.82574186],
               [ 0.        ,  0.        ,  1.82574186],
               [ 0.        ,  0.        ,  0.        ],
               [ 0.        ,  0.        ,  0.        ],
               [ 0.        ,  0.        ,  0.        ],
               [ 0.        ,  0.        ,  0.        ]])


    """
    # Check inputs
    if not (isinstance(n, int) and n > 1):
        raise ValueError('"n" must be an integer greater than 1.')
    if alpha.lower() not in {"orthogonal", "o", "rotatable", "r"}:
        raise ValueError(f'Invalid value for "alpha": {alpha}')
    if face.lower() not in {
        "circumscribed",
        "ccc",
        "inscribed",
        "cci",
        "faced",
        "ccf",
    }:
        raise ValueError(f'Invalid value for "face": {face}')

    nc = len(center)
    if nc != 2:
        raise ValueError(
            f'Invalid number of values for "center" (expected 2, but got {nc})'
        )

    # Orthogonal Design
    if alpha.lower() in {"orthogonal", "o"}:
        H2, a = star(n, alpha="orthogonal", center=center)

    # Rotatable Design
    if alpha.lower() in {"rotatable", "r"}:
        H2, a = star(n, alpha="rotatable")

    # Inscribed CCD
    if face.lower() in {"inscribed", "cci"}:
        H1 = ff2n(n)
        H1 /= a  # Scale down the factorial points
        H2, a = star(n)

    # Faced CCD
    if face.lower() in {"faced", "ccf"}:
        H2, a = star(n)  # Value of alpha is always 1 in Faced CCD
        H1 = ff2n(n)

    # Circumscribed CCD
    if face.lower() in {"circumscribed", "ccc"}:
        H1 = ff2n(n)

    C1 = repeat_center(n, center[0])
    C2 = repeat_center(n, center[1])

    H1 = union(H1, C1)
    H2 = union(H2, C2)
    H = union(H1, H2)

    return H
