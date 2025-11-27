import numpy as np

from pyDOE.doe_optimal.utils import information_matrix
from pyDOE.doe_optimal.criterion import regularized_inv


def d_efficiency(X):
    """
    Compute D-efficiency for a given design matrix.

    D-efficiency is defined as:

    $$100 \times (\det(M_X))^{1/p}$$

    where $M_X = (1/n) X^T X$.

    Parameters
    ----------
    X : ndarray of shape (n_points, p)
        Design matrix.

    Returns
    -------
    float
        D-efficiency percentage.
    """
    M = information_matrix(X, normalized=True, alpha=0.0, X0=None)
    p = X.shape[1]
    return 100.0 * (np.linalg.det(M) ** (1.0 / p))


def a_efficiency(X):
    """
    Compute A-efficiency for a given design matrix.

    A-efficiency is defined as:

        $$100 \times \frac{p}{\operatorname{tr}(M_X^{-1})}$$

    where $M_X = (1/n) X^T X$.

    Parameters
    ----------
    X : ndarray of shape (n_points, p)
        Design matrix.

    Returns
    -------
    float
        A-efficiency percentage.
    """
    M = information_matrix(X, normalized=True, alpha=0.0, X0=None)
    p = X.shape[1]
    return 100.0 * (p / np.trace(regularized_inv(M)))
