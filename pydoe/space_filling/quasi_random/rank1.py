import numpy as np


__all__ = ["rank1_lattice"]


def rank1_lattice(
    num_points: int,
    dimension: int,
    generator_vector: np.ndarray = None,
    *,
    seed: int | np.random.Generator | None = None,
) -> np.ndarray:
    r"""
    Generate a rank-1 lattice design matrix.

    Rank-1 lattices are quasi-random designs used for numerical integration
    and high-dimensional sampling. This algorithm generates deterministic
    points with linear runtime.

    Parameters
    ----------
    num_points : int
        The number of points to generate.
    dimension : int
        The dimensionality of the space.
    generator_vector : array_like of int, optional
        A generator vector of length `dimension`. If None, one is randomly
        generated using integers in [2, num_points).
    seed : int or numpy.random.Generator, optional
        Seed of the random generator vector, for reproducible designs.
        Only used when `generator_vector` is None.

    Returns
    -------
    design : (num_points, dimension) ndarray
        The resulting integer-valued rank-1 lattice matrix. Each row represents
        a point in the design.

    Notes
    -----
    The design uses modular arithmetic to construct each point via:

    $$x_i = (i \cdot z) \bmod n$$

    where $$i$$ is the point index, $$z$$ is the generator vector, and $$n$$
    is the total number of points. All operations are performed modulo
    `num_points`.

    Raises
    ------
    ValueError
        If generator_vector shape does not match dimension, or if no
        generator_vector is given and num_points is less than 3.

    Examples
    --------
    >>> rank1_lattice(5, 2, generator_vector=[1, 2])
    array([[0, 0],
           [1, 2],
           [2, 4],
           [3, 1],
           [4, 3]])
    >>> a = rank1_lattice(7, 3, seed=42)
    >>> b = rank1_lattice(7, 3, seed=42)
    >>> bool((a == b).all())
    True
    """
    if generator_vector is None:
        if num_points < 3:
            raise ValueError(
                "num_points must be at least 3 to draw a random "
                "generator_vector; pass generator_vector instead"
            )
        rng = np.random.default_rng(seed)
        generator_vector = rng.integers(2, num_points, dimension)

    generator_vector = np.asarray(generator_vector) % num_points
    if generator_vector.shape != (dimension,):
        raise ValueError(
            f"Expected generator_vector of shape ({dimension},), "
            f"got {generator_vector.shape}"
        )

    points = np.array(
        [(i * generator_vector) % num_points for i in range(num_points)],
        dtype=int,
    )

    return points
