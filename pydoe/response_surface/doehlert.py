"""
This module implements the Doehlert experimental design.

An alternative and very useful design for fitting second-order models
is the uniform shell design proposed by Doehlert in 1970 (Doehlert 1970).
Doehlert designs are particularly advantageous for optimizing multiple
variables, offering a more efficient alternative to central composite designs.
They require fewer experimental runs while maintaining flexibility to explore
the experimental domain effectively.

The Doehlert design defines a spherical experimental domain and emphasizes
uniform space filling. Although the resulting matrix is neither orthogonal
nor rotatable, its variance properties are generally acceptable and do not
compromise its effectiveness in practical applications.

References
----------
Doehlert, David H. 1970. “Uniform Shell Designs.” *Applied Statistics*
19 (3): 231. https://doi.org/10.2307/2346327

Implementation of simplex design (`version 1.0.0`, 11 July 2015) by Moritz von
Stosch https://www.mathworks.com/matlabcentral/fileexchange/54048-doehlert-design
"""

import numpy as np


__all__ = ["doehlert_shell_design", "doehlert_simplex_design"]


def _regular_simplex(num_factors: int) -> np.ndarray:
    r"""
    Vertices of Doehlert's regular simplex: the origin and ``num_factors``
    points at distance 1 from the origin and from each other.

    Vertex $$i$$ (1-based) has, on axis $$j$$, the coordinate

    $$x_{ij} = \frac{1}{\sqrt{2 j (j + 1)}} \quad (j < i), \qquad
    x_{ii} = \sqrt{\frac{i + 1}{2 i}}, \qquad
    x_{ij} = 0 \quad (j > i)$$
    """
    if num_factors < 1:
        raise ValueError("Number of factors must be at least 1.")
    simplex = np.zeros((num_factors + 1, num_factors))
    for i in range(1, num_factors + 1):
        for j in range(1, i):
            simplex[i, j - 1] = 1 / np.sqrt(2 * j * (j + 1))
        simplex[i, i - 1] = np.sqrt((i + 1) / (2 * i))
    return simplex


def doehlert_shell_design(
    num_factors: int, num_center_points: int = 1
) -> np.ndarray:
    """
    Generate a Doehlert design matrix for a given number of factors:
    the center followed by the points of the first uniform shell.

    Parameters
    ----------
    num_factors : int
        Number of factors (variables).
    num_center_points : int, optional
        Number of center (replicate) points. Default is 1.

    Returns
    -------
    np.ndarray
        Design matrix of shape (N, num_factors), where

        $$N = k^2 + k + C$$

        with
        - $$k$$ the number of factors,
        - $$C$$ the number of center points.

        The center points come first. The $$k^2 + k$$ shell points all lie
        at distance 1 from the center, and each is at distance 1 from its
        nearest neighbors.

    Raises
    ------
    ValueError
        If num_factors is less than 1 or num_center_points is negative.

    Notes
    -----
    This function implements the uniform shell design of Doehlert (1970):
    the shell points are the differences between every two vertices of a
    regular simplex with unit edges. For two factors they form a regular
    hexagon, for three factors a cuboctahedron. The shell points are those
    of ``doehlert_simplex_design``, in the same order.

    References
    ----------
    Doehlert, David H. 1970. “Uniform Shell Designs.” *Applied Statistics*
    19 (3): 231. https://doi.org/10.2307/2346327

    Examples
    --------
    >>> doehlert_shell_design(2).round(3) + 0.0
    array([[ 0.   ,  0.   ],
           [ 1.   ,  0.   ],
           [ 0.5  ,  0.866],
           [-1.   ,  0.   ],
           [-0.5  , -0.866],
           [ 0.5  , -0.866],
           [-0.5  ,  0.866]])
    """
    if num_center_points < 0:
        raise ValueError("Number of center points must not be negative.")
    shell = doehlert_simplex_design(num_factors)[1:]
    center = np.zeros((num_center_points, num_factors))
    return np.vstack([center, shell])


def doehlert_simplex_design(num_factors: int) -> np.ndarray:
    """
    Generate a Doehlert design matrix using a simplex-based approach.

    Parameters
    ----------
    num_factors : int
        Number of factors included in the design.

    Returns
    -------
    np.ndarray
        Design matrix with experiments at different coded levels.
        The design matrix contains

        $$ (k+1) + k \times (k+1 - 1) = k^2 + k + 1 $$

        points, where $$k$$ is the number of factors: the center, then
        $$k^2 + k$$ points at distance 1 from it.

    Raises
    ------
    ValueError
        If num_factors is less than 1.

    Notes
    -----
    The design starts from a regular simplex with unit edges and one vertex
    at the origin, and adds the differences between every two of its
    vertices. The first $$k + 1$$ rows are the simplex itself.
    It is inspired by the implementation by Moritz von Stosch (2015).

    References
    ----------
    Implementation of simplex design (`version 1.0.0`, 11 July 2015) by Moritz
    von Stosch https://www.mathworks.com/matlabcentral/fileexchange/54048-doehlert-design
    """
    simplex_matrix = _regular_simplex(num_factors)

    extra_points = []
    for i in range(num_factors + 1):
        for j in list(range(1, i)) + list(range(i + 1, num_factors + 1)):
            point = simplex_matrix[i, :] - simplex_matrix[j, :]
            extra_points.append(point)

    # num_factors >= 1, so there are always k^2 + k >= 2 extra points
    full_matrix = np.vstack([simplex_matrix, extra_points])
    return full_matrix
