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

import re
from collections.abc import Sequence

import numpy as np


_FACTOR = re.compile(r"^x(\d+)(?:(?:\^|\*\*)(\d+))?$")


def _parse_monomial(token: str, n_vars: int) -> tuple[float, list[int]]:
    """Split a monomial such as ``2*x1*x3^2`` into (coefficient, powers)."""
    coefficient = 1.0
    powers = [0] * n_vars
    # Protect the power operator "**" before splitting on the product "*".
    for factor in token.replace("**", "^").split("*"):
        match = _FACTOR.match(factor)
        if match is None:
            try:
                coefficient *= float(factor)
            except ValueError:
                msg = f"invalid term {factor!r} in monomial {token!r}"
                raise ValueError(msg) from None
            continue
        index = int(match.group(1))
        if not 1 <= index <= n_vars:
            msg = (
                f"monomial {token!r} uses x{index}, but the design has "
                f"{n_vars} variable(s) (x1 to x{n_vars})"
            )
            raise ValueError(msg)
        powers[index - 1] += int(match.group(2) or 1)
    return coefficient, powers


def build_regression_matrix(
    design: np.ndarray, model: str, build: Sequence[bool] | None = None
) -> np.ndarray:
    """
    Build a regression matrix using a DOE matrix and a list of monomials.

    Parameters
    ----------
    design : 2d-array
        The design matrix, one run per row and one variable per column.
        A 1d-array is read as a single run.
    model : str
        The monomials of the regression model, separated by spaces. The
        variables are named ``x1``, ``x2``, ... in the order of the columns
        of ``design``; a monomial is a product of numbers and variables, with
        optional integer powers (e.g. ``'1 x1 x2 x1*x2 x1^2'``).
    build : sequence of bool, optional
        One flag per monomial; the monomials flagged ``False`` are left out
        of the regression matrix. By default, all monomials are kept.

    Returns
    -------
    R : 2d-array
        The regression matrix, one row per run of ``design`` and one column per
        kept monomial.

    Raises
    ------
    ValueError
        If ``build`` does not have one flag per monomial, if a monomial is
        malformed, or if it uses a variable that ``design`` does not have.

    Examples
    --------
    >>> import numpy as np
    >>> design = np.array([[-1.0, -1], [1, -1], [-1, 1], [1, 1]])
    >>> build_regression_matrix(design, "1 x1 x2 x1*x2")
    array([[ 1., -1., -1.,  1.],
           [ 1.,  1., -1., -1.],
           [ 1., -1.,  1., -1.],
           [ 1.,  1.,  1.,  1.]])

    """
    design = np.atleast_2d(np.asarray(design, dtype=float))
    tokens = model.split()
    if build is None:
        build = [True] * len(tokens)
    if len(build) != len(tokens):
        msg = (
            f"build has {len(build)} flag(s), but the model has "
            f"{len(tokens)} monomial(s)"
        )
        raise ValueError(msg)
    tokens = [token for token, keep in zip(tokens, build, strict=True) if keep]

    R = np.empty((design.shape[0], len(tokens)))
    for j, token in enumerate(tokens):
        coefficient, powers = _parse_monomial(token, design.shape[1])
        R[:, j] = coefficient * np.prod(design ** np.array(powers), axis=1)
    return R
