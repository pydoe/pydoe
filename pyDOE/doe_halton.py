"""
This module implements the Halton sequence, a low-discrepancy quasirandom sequence
used in numerical integration, sampling, and global optimization tasks.

The Halton sequence generates points in a unit hypercube [0, 1]^d using radical
inversion with respect to a sequence of prime number bases. It is especially
useful in high-dimensional integration where uniformity and low correlation
between sample points are desired.

Each dimension in the Halton sequence uses a unique base (a prime number), and
points are computed using the van der Corput sequence in that base.

References
----------
Halton, J. H. (1964). "Algorithm 247: Radical-inverse quasi-random point sequence."
*Communications of the ACM*, 7(12), 701. https://doi.org/10.1145/355588.365104
"""

import numpy as np

__all__ = ["halton_sequence"]


def halton_sequence(num_points, dimension, skip=0):
    """
    Generate a Halton sequence in a given dimension.

    The Halton sequence is a low-discrepancy, quasi-random point set commonly
    used in numerical integration, sampling, and global optimization. Each
    dimension uses a different prime base to generate values via the van der Corput
    sequence.

    Parameters
    ----------
    num_points : int
        Number of points to generate in the sequence.
    dimension : int
        Number of dimensions (features) of the sequence.
    skip : int, optional
        Number of initial points in the sequence to skip. Default is 0.

    Returns
    -------
    points : ndarray of shape (`num_points`, `dimension`)
        The generated Halton sequence points.
    """
    bases = next_primes(dimension)

    # Preallocate the output array
    samples = np.empty((num_points, dimension), dtype=np.float64)

    for dim in range(dimension):
        base = bases[dim]
        for i in range(num_points):
            index = i + skip
            samples[i, dim] = van_der_corput(index, base)

    return samples


def van_der_corput(index, base):
    """
    Compute a single value of the van der Corput sequence.

    The van der Corput sequence generates low-discrepancy values in [0, 1) using
    radical inversion in a specified base.

    Parameters
    ----------
    index : int
        The index in the sequence.
    base : int
        The base to use (must be >= 2).

    Returns
    -------
    value : float
        The van der Corput value at the given index and base.
    """
    result = 0.0
    f = 1.0 / base
    while index > 0:
        index, mod = divmod(index, base)
        result += mod * f
        f /= base

    return result


def next_primes(n):
    """
    Generate the first `n` prime numbers.

    Parameters
    ----------
    n : int
        Number of prime numbers to generate.

    Returns
    -------
    primes : list of int
        List containing the first `n` prime numbers.
    """
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    return primes


def is_prime(n):
    """
    Check whether a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    is_prime : bool
        True if `n` is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
