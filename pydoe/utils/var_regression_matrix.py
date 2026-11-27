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

from .build_regression_matrix import build_regression_matrix


def var_regression_matrix(
    H: np.ndarray, x: np.ndarray, model: str, sigma: float = 1
) -> float:
    r"""
    Compute the variance of the 'regression error'.

    Parameters
    ----------
    H : 2d-array
        The regression matrix: one row per run, one column per monomial of
        ``model`` (see ``build_regression_matrix``).
    x : 1d-array
        The coordinates of the point to calculate the regression error
        variance at, one value per variable.
    model : str
        A string of tokens that define the regression model (e.g.
        '1 x1 x2 x1*x2')
    sigma : scalar
        An estimate of the standard deviation of the observation error
        (default: 1).

    Returns
    -------
    var : scalar
        The variance of the regression error, evaluated at ``x``:

        $$\mathrm{var}(x) = \sigma^2 \, f(x)^T (H^T H)^{-1} f(x)$$

        where $$f(x)$$ holds the monomials of ``model`` at ``x``.

    Raises
    ------
    ValueError
        If model and DOE are incompatible: ``H`` does not have full column
        rank, or its columns do not match the monomials of ``model``.

    Examples
    --------
    >>> import numpy as np
    >>> from pydoe.utils import build_regression_matrix
    >>> design = np.array([[-1.0, -1], [1, -1], [-1, 1], [1, 1]])
    >>> H = build_regression_matrix(design, "1 x1 x2")
    >>> float(var_regression_matrix(H, [0.0, 0.0], "1 x1 x2"))
    0.25
    >>> float(var_regression_matrix(H, [1.0, 1.0], "1 x1 x2"))
    0.75

    """
    H = np.atleast_2d(np.asarray(H, dtype=float))
    x = np.asarray(x, dtype=float).reshape(1, -1)

    if np.linalg.matrix_rank(H) < H.shape[1]:
        raise ValueError("model and DOE don't suit together")

    x_mod = build_regression_matrix(x, model)[0]
    if x_mod.shape[0] != H.shape[1]:
        msg = (
            f"H has {H.shape[1]} column(s), but the model has "
            f"{x_mod.shape[0]} monomial(s)"
        )
        raise ValueError(msg)
    return sigma**2 * (x_mod @ np.linalg.solve(H.T @ H, x_mod))
