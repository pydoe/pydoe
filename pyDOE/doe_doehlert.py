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


def doehlert_shell_design(
    num_factors: int, num_center_points: int = 1
) -> np.ndarray:
    """
    Generate a Doehlert design matrix for a given number of factors
    using a shell approach.

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

    Raises
    ------
    ValueError
        If num_factors is less than 1.

    Notes
    -----
    This function implements the "uniform shell" approach originally proposed by
    Doehlert (1970), which allows for adding shells of points around the center.

    References
    ----------
    Doehlert, David H. 1970. “Uniform Shell Designs.” *Applied Statistics*
    19 (3): 231. https://doi.org/10.2307/2346327
    """
    if num_factors < 1:
        raise ValueError("Number of factors must be at least 1.")

    # Start with center points
    design_points = [np.zeros(num_factors) for _ in range(num_center_points)]

    # Add shells progressively
    for shell_index in range(1, num_factors + 1):
        num_shell_points = shell_index + 1
        angles = np.linspace(0, 2 * np.pi, num_shell_points, endpoint=False)
        for angle in angles:
            point = np.zeros(num_factors)
            radius = np.sqrt(shell_index / num_factors)
            point[0] = radius * np.cos(angle)
            point[1] = radius * np.sin(angle)
            design_points.append(point)

    return np.array(design_points)


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

        points, where $$k$$ is the number of factors.

    Notes
    -----
    The simplex approach allows for uniform exploration of the design space.
    It is inspired by the implementation by Moritz von Stosch (2015).

    References
    ----------
    Implementation of simplex design (`version 1.0.0`, 11 July 2015) by Moritz
    von Stosch https://www.mathworks.com/matlabcentral/fileexchange/54048-doehlert-design
    """
    simplex_matrix = np.zeros((num_factors + 1, num_factors))

    for i in range(1, num_factors + 1):
        for j in range(1, i + 1):
            if j == i:
                simplex_matrix[i, j - 1] = np.sqrt(i + 1) / np.sqrt(2 * i)
            else:
                simplex_matrix[i, i - j] = 1 / np.sqrt(
                    2 * (i - (j - 1)) * (i - j)
                )

    extra_points = []
    for i in range(num_factors + 1):
        for j in list(range(1, i)) + list(range(i + 1, num_factors + 1)):
            point = simplex_matrix[i, :] - simplex_matrix[j, :]
            extra_points.append(point)

    full_matrix = np.vstack([simplex_matrix, extra_points])
    return full_matrix
