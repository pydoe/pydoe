import numpy as np

__all__ = ["rank1_lattice"]


def rank1_lattice(num_points, dimension, generator_vector=None):
    """
    Generate a rank-1 lattice design matrix.

    Rank-1 lattices are quasi-random designs used for numerical integration and
    high-dimensional sampling. This algorithm generates deterministic points with
    linear runtime.

    Parameters
    ----------
    num_points : int
        The number of points to generate.
    dimension : int
        The dimensionality of the space.
    generator_vector : array_like of int, optional
        A generator vector of length `dimension`. If None, one is randomly generated
        using integers in [2, num_points).

    Returns
    -------
    design : (num_points, dimension) ndarray
        The resulting integer-valued rank-1 lattice matrix. Each row represents
        a point in the design.

    Notes
    -----
    The design uses modular arithmetic to construct each point via:

        x_i = (i * z) mod n

    where `i` is the point index, `z` is the generator vector, and `n` is the
    total number of points. All operations are performed modulo `num_points`.
    """
    if generator_vector is None:
        generator_vector = np.random.randint(2, num_points, dimension)

    generator_vector = np.asarray(generator_vector) % num_points
    if generator_vector.shape != (dimension,):
        raise ValueError(
            f"Expected generator_vector of shape ({dimension},), got {generator_vector.shape}"
        )

    points = np.array(
        [(i * generator_vector) % num_points for i in range(num_points)], dtype=int
    )

    return points
