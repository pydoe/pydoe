"""
This module implements the Korobov lattice generator for quasi-random sampling.

Korobov lattices are a subclass of rank-1 lattice rules used for generating
low-discrepancy sequences. These sequences are widely applied in quasi-Monte
Carlo methods, global optimization, and numerical integration of
high-dimensional functions.

The construction uses modular arithmetic to build the generator vector using
a single integer parameter. When the number of points and the generator are
coprime, the resulting design exhibits Latin Hypercube-like properties with
excellent uniform coverage.

This implementation is based on a simplified rank-1 lattice formulation and
uses a linear-time algorithm.
"""

from __future__ import annotations

import random

import numpy as np

from pyDOE.doe_rank1 import rank1_lattice


__all__ = ["korobov_sequence"]


def korobov_sequence(
    num_points: int, dimension: int, generator_param: int | None = None
) -> np.ndarray:
    r"""
    Generate a Korobov lattice design matrix.

    Korobov lattices form a class of low-discrepancy sequences for quasi-Monte
    Carlo methods. They are constructed using a generator vector derived from
    modular exponentiation of a single integer. The generated matrix represents
    samples in a uniform virtual grid.

    Parameters
    ----------
    num_points : int
        Number of design points to generate.
    dimension : int
        Number of dimensions in the design space.
    generator_param : int, optional
        Generator parameter used in modular construction. If None, a random
        value in [2, `num_points`) is selected.

    Returns
    -------
    design : ndarray of shape (`num_points`, `dimension`)
        Integer-valued design matrix corresponding to bins on a modular grid.

    Notes
    -----
    The Korobov method is a special case of a rank-1 lattice. The generator
    vector is defined as:

        $$ z_i = (a^i) \mod N $$

    for i = 0 to d-1, where `a` is the generator_param and `N` is num_points.
    The resulting design has uniformity properties ideal for integration and
    high-dimensional optimization.

    To ensure good coverage, it's recommended that
    `gcd(generator_param, num_points) == 1`.

    Raises
    ------
    ValueError
        If generator_param is not greater than 1.
    """
    if generator_param is None:
        generator_param = random.randrange(2, num_points)
    generator_param %= num_points
    if generator_param <= 1:
        raise ValueError("generator_param must be greater than 1.")

    generator_vector = [1] * dimension
    for i in range(1, dimension):
        generator_vector[i] = (
            generator_param * generator_vector[i - 1]
        ) % num_points

    return rank1_lattice(num_points, dimension, generator_vector)
