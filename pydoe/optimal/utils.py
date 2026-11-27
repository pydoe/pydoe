from __future__ import annotations

from collections.abc import Callable
from typing import Literal

import numpy as np

from pydoe.optimal.criterion import (
    a_optimality,
    c_optimality,
    d_optimality,
    e_optimality,
    g_optimality,
    i_optimality,
    s_optimality,
    t_optimality,
    v_optimality,
)
from pydoe.optimal.model import build_design_matrix, build_uniform_moment_matrix


def _xtx_augmented(
    X: np.ndarray, alpha: float = 0.0, X0: np.ndarray = None
) -> np.ndarray:
    r"""
    Compute augmented information matrix:

    $$ X^T X_{\text{aug}} = X^T X + \alpha \left( \frac{X_0^T X_0}{N_0} \right) $$

    If $$\alpha = 0$$ or $$X_0$$ is None, returns plain $$X^T X$$.

    Parameters
    ----------
    X : ndarray of shape (n, p)
        Design matrix.
    alpha : float, optional
        Augmentation parameter (default is 0.0).
    X0 : ndarray, optional
        Candidate set for augmentation.

    Returns
    -------
    ndarray of shape (p, p)
        Augmented information matrix.
    """  # ruff: ignore[line-too-long]
    H = X.T @ X
    if alpha and X0 is not None and len(X0) > 0:
        N0 = X0.shape[0]
        H0 = (X0.T @ X0) / N0
        H = H + alpha * H0
    return H


def information_matrix(
    X: np.ndarray,
    *,
    normalized: bool = True,
    alpha: float = 0.0,
    X0: np.ndarray = None,
) -> np.ndarray:
    r"""
    Compute the information matrix for a design matrix,
    with optional augmentation.

    Parameters
    ----------
    X : ndarray of shape (n, p)
        Design matrix.
    normalized : bool, optional
        If True, returns $(1/n) \cdot (X^T X_{\text{aug}})$; else returns $X^T X_{\text{aug}}$.
    alpha : float, optional
        Augmentation parameter (default is 0.0).
    X0 : ndarray, optional
        Candidate set for augmentation.

    Returns
    -------
    ndarray of shape (p, p)
        Information matrix.
    """  # ruff: ignore[line-too-long]
    n = X.shape[0]
    H_aug = _xtx_augmented(X, alpha=alpha, X0=X0)
    return H_aug / n if normalized else H_aug


def criterion_value(  # ruff: ignore[too-many-return-statements, too-many-branches]
    X: np.ndarray,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"],
    X0: np.ndarray = None,
    alpha: float = 0.0,
    M_moment: np.ndarray = None,
    **kwargs: dict,
) -> float:
    """
    Compute the value of a specified optimality criterion for a design matrix.

    Parameters
    ----------
    X : ndarray
        Design matrix.
    criterion : str
        Criterion type: 'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'.
    X0 : ndarray, optional
        Full candidate set for augmentation.
    alpha : float, optional
        Augmentation parameter (default is 0.0).
    M_moment : ndarray, optional
        Moment matrix for I-optimality.
    **kwargs : dict, optional
        Additional arguments for specific criteria:
        - c_vector : for C-optimality, of length p (default: all ones)
        - test_points : for V-optimality, model-matrix rows of the points
          to predict at (default: ``X0``, or ``X`` when ``X0`` is None)
        - model_diff_subset : for T-optimality, the model differences at
          the rows of ``X`` (required)
        - candidates : for G-optimality

    Returns
    -------
    float
        Value of the specified criterion.

    Raises
    ------
    ValueError
        If an unknown criterion is specified, or if ``model_diff_subset``
        is missing for T-optimality.
    """
    M = information_matrix(X, normalized=True, alpha=alpha, X0=X0)
    p = X.shape[1]

    if criterion.upper() == "D":
        return d_optimality(M)
    elif criterion.upper() == "A":
        return a_optimality(M)
    elif criterion.upper() == "I":
        if M_moment is None and X0 is not None:
            M_moment = build_uniform_moment_matrix(X0)
        return i_optimality(M, M_moment)
    elif criterion.upper() == "C":
        c_vector = kwargs.get("c_vector")
        if c_vector is None:
            c_vector = np.ones(p)
        return c_optimality(M, np.asarray(c_vector, dtype=float))
    elif criterion.upper() == "E":
        return e_optimality(M)
    elif criterion.upper() == "G":
        candidates = kwargs.get("candidates", X0 if X0 is not None else X)
        return g_optimality(M, candidates)
    elif criterion.upper() == "V":
        # Averaging over the rows of X itself gives tr(M^-1 M) = p for
        # every design, so the default is the candidate set.
        test_points = kwargs.get("test_points")
        if test_points is None:
            test_points = X0 if X0 is not None else X
        return v_optimality(M, test_points)
    elif criterion.upper() == "S":
        # S compares the columns after scaling each to unit length, so an
        # augmentation term would make a column that the design does not
        # span look orthogonal. It needs no inverse: alpha is not applied.
        return s_optimality(information_matrix(X, normalized=True))
    elif criterion.upper() == "T":
        model_diff = kwargs.get("model_diff_subset")
        if model_diff is None:
            raise ValueError(
                "T-optimality needs the model differences at the design "
                "points (model_diff_subset)"
            )
        return t_optimality(X, model_diff)
    else:
        raise ValueError(f"Unknown criterion: {criterion}")


def _make_scorer(  # ruff: ignore[too-many-arguments]
    candidates: np.ndarray,
    degree: int,
    criterion: str,
    alpha: float = 0.0,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: np.ndarray | Callable[[np.ndarray], np.ndarray] | None = None,
) -> Callable[[np.ndarray], float]:
    """
    Build the function that scores a design (an array of points) with a
    criterion, with the inputs that the criterion needs.

    Parameters
    ----------
    candidates : ndarray of shape (N, k)
        Candidate points in the design space.
    degree : int
        Polynomial degree of the model.
    criterion : str
        Criterion type: 'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'.
    alpha : float, optional
        Augmentation parameter (default is 0.0).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of model
        parameters whose variance is minimized (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N,) or callable, optional
        T-optimality: difference between the responses of the two models,
        either at each candidate or as a function of an array of points.
        Required for the T criterion.

    Returns
    -------
    callable
        ``score(design) -> float``, larger is better. For the D, E and S
        criteria (D and E only when ``alpha`` is 0), a design whose model
        matrix has rank $$r < p$$ scores $$r - p$$ instead of 0.

    Raises
    ------
    ValueError
        If the criterion is unknown, an input has the wrong shape, or
        ``model_diff`` is missing for T-optimality.
    """
    candidates = np.asarray(candidates, dtype=float)
    criterion = criterion.upper()
    if criterion not in {"D", "A", "I", "C", "E", "G", "V", "S", "T"}:
        raise ValueError(f"Unknown criterion: {criterion}")

    X0 = build_design_matrix(candidates, degree)
    M_moment = build_uniform_moment_matrix(X0)
    p = X0.shape[1]
    kwargs = {}
    diff = None

    if criterion == "C" and c_vector is not None:
        c_vector = np.asarray(c_vector, dtype=float).reshape(-1)
        if c_vector.shape[0] != p:
            msg = f"c_vector must have {p} entries (one per model term)"
            raise ValueError(msg)
        kwargs["c_vector"] = c_vector
    elif criterion == "V" and test_points is not None:
        test_points = np.atleast_2d(np.asarray(test_points, dtype=float))
        if test_points.shape[1] != candidates.shape[1]:
            msg = (
                f"test_points must have {candidates.shape[1]} column(s), "
                "like the candidates"
            )
            raise ValueError(msg)
        kwargs["test_points"] = build_design_matrix(test_points, degree)
    elif criterion == "T":
        if model_diff is None:
            raise ValueError(
                "T-optimality needs model_diff: the difference between "
                "the responses of the two models, at each candidate or "
                "as a function of the points"
            )
        if callable(model_diff):
            diff = model_diff
        else:
            values = np.asarray(model_diff, dtype=float).reshape(-1)
            if values.shape[0] != candidates.shape[0]:
                msg = (
                    f"model_diff must have {candidates.shape[0]} entries "
                    "(one per candidate)"
                )
                raise ValueError(msg)
            lookup = {
                tuple(np.round(row, 12)): value
                for row, value in zip(candidates, values, strict=True)
            }

            def diff(points: np.ndarray) -> np.ndarray:
                return np.array([
                    lookup[tuple(np.round(row, 12))] for row in points
                ])

    # D, E and S are 0 for every design that cannot estimate the model
    # (S always, D and E when alpha is 0). Ranking those designs by their
    # rank deficiency lets a search that starts from few points progress.
    rank_graded = criterion == "S" or (criterion in {"D", "E"} and not alpha)

    def score(design: np.ndarray) -> float:
        X = build_design_matrix(design, degree)
        if rank_graded:
            rank = int(np.linalg.matrix_rank(X)) if X.shape[0] else 0
            if rank < p:
                return float(rank - p)
        if diff is not None:
            d = np.asarray(diff(design), dtype=float).reshape(-1)
            return criterion_value(
                X, criterion, X0, alpha, M_moment, model_diff_subset=d
            )
        return criterion_value(X, criterion, X0, alpha, M_moment, **kwargs)

    return score


def _best_single_add(
    current: np.ndarray, pool: np.ndarray, score: Callable[[np.ndarray], float]
) -> tuple[int, float]:
    """
    Among candidates in 'pool', find index that maximizes criterion
    if added to 'current'.

    Parameters
    ----------
    current : ndarray
        Current design points.
    pool : ndarray
        Pool of candidate points to consider adding.
    score : callable
        Scores a design, larger is better (see ``_make_scorer``).

    Returns
    -------
    best_idx : int
        Index in pool of the best candidate to add (or -1 if none improves).
    best_val : float
        Best criterion value achieved.
    """
    if len(pool) == 0:
        return -1, score(current)

    best_idx, best_val = -1, -np.inf
    for j in range(pool.shape[0]):
        val = score(np.vstack([current, pool[j]]))
        if val > best_val:
            best_val = val
            best_idx = j
    return best_idx, best_val


def _best_single_drop(
    current: np.ndarray, score: Callable[[np.ndarray], float]
) -> tuple[int, float]:
    """
    Among points in 'current', find index whose removal gives best criterion.

    Parameters
    ----------
    current : ndarray
        Current design points.
    score : callable
        Scores a design, larger is better (see ``_make_scorer``).

    Returns
    -------
    best_idx : int
        Index in current of the best point to drop (or -1 if none improves).
    best_val : float
        Best criterion value achieved after drop.
    """
    if current.shape[0] <= 1:
        return -1, score(current)

    best_idx, best_val = 0, -np.inf
    for i in range(current.shape[0]):
        val = score(np.delete(current, i, axis=0))
        if val > best_val:
            best_val = val
            best_idx = i
    return best_idx, best_val
