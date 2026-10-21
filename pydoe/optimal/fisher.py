from __future__ import annotations

from typing import Literal

import numpy as np

from pydoe.optimal.criterion import (
    a_optimality,
    d_optimality,
    e_optimality,
    s_optimality,
)


_CRITERIA = {
    "D": d_optimality,
    "A": a_optimality,
    "E": e_optimality,
    "S": s_optimality,
}

_RIDGE = 1e-10


def _precision(
    covariance: np.ndarray | float | None, rows: np.ndarray
) -> np.ndarray:
    """
    Return the precision matrix ``Sigma^{-1}`` restricted to ``rows``.

    Parameters
    ----------
    covariance : None, float, ndarray of shape (N,) or (N, N)
        Noise covariance of the candidate observations. ``None`` means
        identity, a scalar is a common variance and a vector holds
        independent variances.
    rows : ndarray of int
        Indices of the selected candidate rows.

    Returns
    -------
    ndarray of shape (n, n)
        Inverse of the covariance sub-matrix of the selected rows.
    """
    n = len(rows)
    if covariance is None:
        return np.eye(n)
    cov = np.asarray(covariance, dtype=float)
    if cov.ndim == 0:
        return np.eye(n) / float(cov)
    if cov.ndim == 1:
        return np.diag(1.0 / cov[rows])
    return np.linalg.inv(cov[np.ix_(rows, rows)])


def fisher_information(
    jacobian: np.ndarray,
    rows: np.ndarray | None = None,
    covariance: np.ndarray | float | None = None,
) -> np.ndarray:
    r"""
    Fisher information matrix (FIM) from a Jacobian, averaged over
    parameter-space points.

    For a 2D Jacobian $J$ of shape ``(n, p)`` (rows are experiments, columns
    are parameters) the FIM is

    $$M = J^T \Sigma^{-1} J$$

    where $\Sigma$ is the ``(n, n)`` covariance of the observation noise
    (identity by default). For a 3D Jacobian of shape ``(n, p, K)`` the third
    axis indexes $K$ points of the parameter space; a FIM is computed for each
    point and the mean FIM is returned:

    $$\bar M = \frac{1}{K} \sum_{k=1}^K J_k^T \Sigma^{-1} J_k$$

    Parameters
    ----------
    jacobian : ndarray of shape (N, p) or (N, p, K)
        Jacobian of the N candidate experiments.
    rows : ndarray of int, optional
        Indices of the candidate rows forming the design (repeats allowed).
        Defaults to all rows.
    covariance : float, ndarray of shape (N,) or (N, N), optional
        Observation noise covariance over the candidates. The sub-matrix
        belonging to ``rows`` is used. Defaults to the identity.

    Returns
    -------
    ndarray of shape (p, p)
        The (mean) Fisher information matrix.

    Raises
    ------
    ValueError
        If the Jacobian is not 2D or 3D.

    Examples
    --------
    >>> import numpy as np
    >>> from pydoe import fisher_information
    >>> J = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    >>> fisher_information(J).tolist()
    [[2.0, 1.0], [1.0, 2.0]]
    >>> fisher_information(np.stack([J, 2 * J], axis=2))[0, 0]
    np.float64(5.0)
    """
    J = np.asarray(jacobian, dtype=float)
    if J.ndim == 2:
        J = J[:, :, None]
    elif J.ndim != 3:
        raise ValueError("jacobian must be 2D (N, p) or 3D (N, p, K).")
    rows = np.arange(J.shape[0]) if rows is None else np.asarray(rows, int)
    W = _precision(covariance, rows)
    j_sel = J[rows]
    return np.einsum("npk,nm,mqk->pq", j_sel, W, j_sel) / J.shape[2]


def jacobian_optimal_design(
    jacobian: np.ndarray,
    n_points: int,
    covariance: np.ndarray | float | None = None,
    criterion: Literal["D", "A", "E", "S"] = "D",
    max_iter: int = 100,
) -> tuple[np.ndarray, dict]:
    r"""
    Select rows of a Jacobian that optimize a criterion of the mean FIM.

    Rows are chosen greedily and then improved with point-exchange passes.
    Rows may be selected more than once (replicates). A 3D Jacobian
    ``(N, p, K)`` is treated as ``K`` parameter-space points: the FIM of the
    selected rows is computed for each point, averaged, and then the
    criterion is evaluated on the mean (robust / Bayesian-style OED, see
    https://doi.org/10.1214/22-BA1306). See
    [fisher_information][pydoe.fisher_information] for the FIM convention.

    Parameters
    ----------
    jacobian : ndarray of shape (N, p) or (N, p, K)
        Jacobian of the N candidate experiments.
    n_points : int
        Number of experiments to select.
    covariance : float, ndarray of shape (N,) or (N, N), optional
        Observation noise covariance over the candidates (default identity).
    criterion : {'D', 'A', 'E', 'S'}, optional
        Criterion maximized on the mean FIM (default 'D').
    max_iter : int, optional
        Maximum number of exchange passes (default 100).

    Returns
    -------
    indices : ndarray of shape (n_points,)
        Selected candidate row indices.
    info : dict
        Contains 'criterion', 'score' and the mean 'fim' of the design.

    Raises
    ------
    ValueError
        If the criterion is unknown or ``n_points`` is not positive.

    Examples
    --------
    >>> import numpy as np
    >>> from pydoe import jacobian_optimal_design
    >>> x = np.linspace(0, 1, 11)
    >>> J = np.stack([np.ones_like(x), x], axis=1)  # y = a + b x
    >>> idx, info = jacobian_optimal_design(J, 4)
    >>> sorted(idx.tolist())
    [0, 0, 10, 10]
    """
    crit = _CRITERIA.get(str(criterion).upper())
    if crit is None:
        raise ValueError(f"Unknown criterion: {criterion}")
    if n_points < 1:
        raise ValueError("n_points must be positive.")
    J = np.asarray(jacobian, dtype=float)
    if J.ndim == 2:
        J = J[:, :, None]
    elif J.ndim != 3:
        raise ValueError("jacobian must be 2D (N, p) or 3D (N, p, K).")
    N, p, _ = J.shape

    def score(rows: list[int]) -> float:
        M = fisher_information(J, np.array(rows), covariance)
        return crit(M + _RIDGE * np.eye(p))

    design: list[int] = []
    for _ in range(n_points):
        vals = [score([*design, j]) for j in range(N)]
        design.append(int(np.argmax(vals)))

    best = score(design)
    for _ in range(max_iter):
        improved = False
        for i in range(n_points):
            vals = [score([*design[:i], j, *design[i + 1 :]]) for j in range(N)]
            j = int(np.argmax(vals))
            if vals[j] > best + 1e-12 * abs(best) and j != design[i]:
                design[i], best, improved = j, vals[j], True
        if not improved:
            break

    indices = np.array(design)
    info = {
        "criterion": str(criterion).upper(),
        "score": float(best),
        "fim": fisher_information(J, indices, covariance),
    }
    return indices, info
