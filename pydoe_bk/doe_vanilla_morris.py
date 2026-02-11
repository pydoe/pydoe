"""
This module implements the original (unoptimized) Morris method for
global sensitivity analysis, a computationally efficient screening
technique that estimates the importance of input variables by analyzing
one-at-a-time (OAT) trajectories through a discretized parameter space.
It is especially useful for identifying influential parameters in
high-dimensional models with relatively low computational cost.

References
----------
1. Morris, M.D., 1991.
   Factorial Sampling Plans for Preliminary Computational Experiments.
   Technometrics 33, 161-174.
   https://doi.org/10.1080/00401706.1991.10484804

2. Campolongo, F., Cariboni, J., & Saltelli, A., 2007.
   An effective screening design for sensitivity analysis of large models.
   Environmental Modelling & Software, 22(10), 1509-1518.
   https://doi.org/10.1016/j.envsoft.2006.10.004

3. Ruano, M.V., Ribes, J., Seco, A., Ferrer, J., 2012.
   An improved sampling strategy based on trajectory design for application
   of the Morris method to systems with many input factors.
   Environmental Modelling & Software 37, 103-109.
   https://doi.org/10.1016/j.envsoft.2012.03.008
"""

from __future__ import annotations

import numpy as np


__all__ = ["morris_sampling"]


def morris_sampling(
    num_vars: int, N: int, num_levels: int = 4, seed: int | None = None
) -> np.ndarray:
    """
    Generate samples using the Morris Method (Vanilla, no optimization).

    Parameters
    ----------
    num_vars : int
        Number of input variables (i.e., the dimensionality of the problem).
    N : int
        Number of trajectories to generate
    num_levels : int, optional
        Number of levels in the grid (must be even). Default is 4.
    seed : int, optional
        Random seed for reproducibility

    Returns
    -------
    samples : ndarray
        Matrix of shape (N * (num_vars + 1), num_vars) with Morris samples.

    Raises
    ------
    ValueError
        If num_levels is not even.
    """
    if num_levels % 2 != 0:
        raise ValueError("num_levels must be an even number")

    rng = np.random.default_rng(seed)
    D = num_vars

    delta = num_levels / (2 * (num_levels - 1))
    G = np.linspace(0, 1 - delta, num_levels // 2)

    samples = []

    for _ in range(N):
        # Starting point x* on the grid
        x_star = rng.choice(G, size=D)

        # Diagonal matrix of directions (+1 or -1)
        D_star = np.diag(rng.choice([-1, 1], size=D))

        # Lower-triangular B matrix
        B = np.tril(np.ones((D + 1, D), dtype=int), -1)

        # Random permutation matrix P*
        P_star = np.eye(D)
        rng.shuffle(P_star)

        # J: ones matrix
        J = np.ones((D + 1, D))

        # Construct B* (trajectory matrix)
        B_star = x_star + delta / 2 * ((2 * B @ P_star - J) @ D_star + J)

        samples.append(B_star)

    samples = np.vstack(samples)

    return samples
