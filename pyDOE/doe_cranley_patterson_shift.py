"""
This module implements the Cranley-Patterson rotation for randomizing
low-discrepancy sequences, such as those produced by Halton or Sobol' methods.

Cranley-Patterson rotation improves the statistical robustness of quasi-random
point sets by applying a uniform random shift and wrapping the result into the
unit hypercube [0, 1)^d. This preserves the low-discrepancy properties while
enabling repeated randomized sampling and error estimation.

The method is useful in quasi-Monte Carlo integration and experimental designs
where randomized replicates are desirable.

References
----------
Cranley, R., and Patterson, T. N. L. 1976. "Randomization of Number Theoretic Methods
for Multiple Integration." *SIAM Journal on Numerical Analysis*, 13(6): 904-914.
"""

import numpy as np

__all__ = ["cranley_patterson_shift"]


def cranley_patterson_shift(points, seed=None):
    """
    Apply Cranley-Patterson rotation to quasi-random points.

    The Cranley-Patterson rotation randomizes a low-discrepancy sequence
    by adding a random uniform shift vector and wrapping the result into [0, 1).

    Parameters
    ----------
    points : array_like of shape (n_samples, n_dimensions)
        2D array of quasi-random points in [0, 1)^d.
    seed : int or None, optional
        Random seed for reproducibility. Default is None.

    Returns
    -------
    shifted_points : ndarray of shape (n_samples, n_dimensions)
        Rotated point set, wrapped into the unit hypercube.

    References
    ----------
    Cranley, R., and Patterson, T. N. L. 1976. "Randomization of Number Theoretic Methods
    for Multiple Integration." *SIAM Journal on Numerical Analysis*, 13(6): 904-914.
    """
    points = np.asarray(points)
    if points.ndim != 2:
        raise ValueError("Input `points` must be a 2D array.")

    _, dim = points.shape
    rng = np.random.default_rng(seed)
    shift_vector = rng.random(dim)

    shifted_points = (points + shift_vector) % 1

    return shifted_points
