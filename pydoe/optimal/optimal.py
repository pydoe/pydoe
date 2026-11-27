from __future__ import annotations

from collections.abc import Callable
from typing import Literal

import numpy as np

from pydoe.optimal.algorithms import (
    detmax,
    fedorov,
    modified_fedorov,
    sequential_dykstra,
    simple_exchange_wynn_mitchell,
)
from pydoe.optimal.efficiency import a_efficiency, d_efficiency
from pydoe.optimal.model import build_design_matrix
from pydoe.optimal.utils import _make_scorer


def optimal_design(  # ruff: ignore[too-many-arguments, too-many-positional-arguments]
    candidates: np.ndarray,
    n_points: int,
    degree: int,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"] = "D",
    method: Literal[
        "sequential", "simple_exchange", "fedorov", "modified_fedorov", "detmax"
    ] = "sequential",
    alpha: float = 0.0,
    max_iter: int = 200,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: np.ndarray | Callable[[np.ndarray], np.ndarray] | None = None,
    replicates: bool = False,
) -> tuple[np.ndarray, dict]:
    """
    Generate an optimal experimental design using a specified
    algorithm and criterion.

    Parameters
    ----------
    candidates : ndarray of shape (N0, k)
        Candidate set (region R).
    n_points : int
        Requested design size (n >= p is recommended).
    degree : int
        Polynomial degree of the model.
    criterion : {'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'}, optional
        Optimality criterion to maximize (default is 'D').
    method : {'sequential', 'simple_exchange', 'fedorov', 'modified_fedorov',
              'detmax'}, optional. Algorithm to use for design generation
              (default is 'sequential').
    alpha : float, optional
        Augmentation parameter for information matrix (default is 0.0):
        a small positive value, such as 0.001, keeps the matrix
        positive definite during the search (Mitchell, 1974).
    max_iter : int, optional
        Maximum number of iterations for iterative methods (default is 200).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of the model
        parameters whose variance is minimized, in the order of the
        columns of ``build_design_matrix`` (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N0,) or callable, optional
        T-optimality: difference between the responses of the rival
        model and the fitted model, either at each candidate or as a
        function of an array of points. Required for the T criterion.
    replicates : bool, optional
        If True, a candidate may be run more than once, as in the
        published algorithms; exact optimal designs often need this.
        By default every run of the design is a different candidate.

    Returns
    -------
    design : ndarray of shape (n_points, k)
        Selected design points.
    info : dict
        Dictionary with scores and efficiencies, including:
        - 'criterion': criterion used
        - 'method': algorithm used
        - 'alpha': augmentation parameter
        - 'score': criterion value
        - 'det_XTX': determinant of X^T X
        - 'D_eff': D-efficiency
        - 'A_eff': A-efficiency
        - 'p_columns': number of model parameters
        - 'n_runs': number of runs in the design

    Raises
    ------
    ValueError
        If an unknown method or criterion is specified, or an input of
        the criterion is missing or has the wrong shape.
    """
    algorithms = {
        "simple_exchange": simple_exchange_wynn_mitchell,
        "fedorov": fedorov,
        "modified_fedorov": modified_fedorov,
        "detmax": detmax,
    }
    inputs = {
        "c_vector": c_vector,
        "test_points": test_points,
        "model_diff": model_diff,
    }
    if method == "sequential":
        design = sequential_dykstra(
            candidates,
            n_points,
            degree,
            criterion,
            alpha,
            replicates=replicates,
            **inputs,
        )
    elif method in algorithms:
        design = algorithms[method](
            candidates,
            n_points,
            degree,
            criterion,
            alpha,
            max_iter,
            replicates=replicates,
            **inputs,
        )
    else:
        known = ["sequential", *algorithms]
        raise ValueError(f"Unknown method: {method!r}. Choose from {known}.")

    # Scores & efficiencies
    X = build_design_matrix(design, degree)
    score = _make_scorer(
        candidates, degree, criterion, alpha, graded=False, **inputs
    )(design)
    info = {
        "criterion": criterion,
        "method": method,
        "alpha": alpha,
        "score": float(score),
        "det_XTX": float(max(np.linalg.det(X.T @ X), 0.0)),
        "D_eff": float(d_efficiency(X)),
        "A_eff": float(a_efficiency(X)),
        "p_columns": int(X.shape[1]),
        "n_runs": int(X.shape[0]),
    }
    return design, info
