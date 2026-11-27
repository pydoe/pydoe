r"""
Optimal Experimental Design (OED)
=================================

Algorithms for constructing optimal experimental designs.

This module implements several classical algorithms for generating
D-optimal and other optimal designs from a candidate set. Each algorithm
iteratively selects or exchanges points to optimize a chosen criterion
(e.g., D-, A-, I-optimality). The published algorithms are stated for
D-optimality; here every step is decided by the value of the chosen
criterion, so the same searches serve all criteria.

By default a candidate is used at most once in a design. The published
algorithms let a point be run several times, and exact optimal designs
often need that: pass ``replicates=True`` for this behavior.

References:
    - Atkinson, A. C., Donev, A. N., & Tobias, R. D. (2007).
    "Optimum Experimental Designs, with SAS." Oxford University Press.
    - Cook, R. D., & Nachtsheim, C. J. (1980). "A Comparison of Algorithms
    for Constructing Exact D-Optimal Designs." Technometrics, 22(3), 315-324.
    - Dykstra, O. (1971). "The Augmentation of Experimental Data to
    Maximize |X'X|." Technometrics, 13(3), 682-688.
    - Fedorov, V. V. (1972). "Theory of Optimal Experiments." Academic Press.
    - Mitchell, T. J. (1974). "An Algorithm for the Construction of 'D-Optimal'
    Experimental Designs." Technometrics, 16(2), 203-210.
    - Mitchell, T. J., & Miller, F. L. (1970). "Use of Design Repair to
    Construct Designs for Special Linear Models." Oak Ridge National
    Laboratory, Mathematics Division Annual Progress Report (ORNL-4661).
    - Montgomery D. C. (2017). "Design and Analysis of Experiments." Wiley.
    - Welch, W. J. (1982). "Branch-and-Bound Search for Experimental Designs
    Based on D Optimality and Other Criteria." Technometrics, 24(1), 41-48.
    - Wynn, H. P. (1972). "Results in the Theory and Construction of
    D-Optimum Experimental Designs." Journal of the Royal Statistical
    Society B, 34(2), 133-147.

Algorithms
----------
Sequential Dykstra Algorithm
    The sequential algorithm of Dykstra (1971) starts from an empty design
    and adds, one at a time, the candidate that improves the criterion the
    most. It is fast and deterministic, but as a greedy method it may stop
    well short of the optimum; the other algorithms start from its design.

Simple Exchange (Wynn-Mitchell) Algorithm
    The simple exchange of Mitchell and Miller (1970) and Wynn (1972)
    changes one point per iteration: a point is added to the design and
    another is deleted. This implementation deletes first, removing the
    point whose loss hurts the criterion the least, then adds the best
    candidate, and keeps the exchange only if the criterion improves.

Fedorov Algorithm
    The exchange algorithm of Fedorov (1972) evaluates every swap of a
    design point with a candidate and makes the single best one in each
    iteration, until no swap improves the criterion. It is more thorough
    and more expensive than the simple exchange. Like every exchange
    algorithm, it stops at a local optimum that need not be the global one.

Modified Fedorov Algorithm
    The modified Fedorov algorithm of Cook and Nachtsheim (1980) goes
    through the design points in turn and immediately replaces each one by
    its best swap, so one pass through the candidates can change every
    point of the design.

DETMAX Algorithm
    DETMAX (Mitchell, 1974) improves a design through excursions: the
    design grows or shrinks by several points before it returns to the
    requested size. This implementation is a reduced form of it: after
    the single swaps are exhausted it tries an excursion of one point,
    adding the best candidate and then deleting the least useful point.
    It does not make the longer excursions or keep the list of failed
    designs of the original.

Augmentation
    With ``alpha > 0`` the algorithms work on the augmented matrix
    $$X^T X + \alpha \, X_0^T X_0 / N_0$$, where $$X_0$$ holds the
    $$N_0$$ candidates. Mitchell (1974) introduced it to keep the matrix
    positive definite while the design has fewer points than the model has
    terms; a small value such as 0.001 is enough (Welch, 1982).
"""

from collections.abc import Callable
from typing import Literal

import numpy as np

from pydoe.optimal.utils import (
    _best_single_add,
    _best_single_drop,
    _make_scorer,
)


ModelDiff = np.ndarray | Callable[[np.ndarray], np.ndarray] | None


def _available(
    candidates: np.ndarray, design: np.ndarray, *, replicates: bool
) -> np.ndarray:
    """
    Candidates that may still join ``design``: all of them when replicates
    are allowed, otherwise those that are not already in the design.
    """
    if replicates:
        return candidates
    mask = np.ones(len(candidates), dtype=bool)
    for row in design:
        mask &= ~np.all(np.isclose(candidates, row, atol=1e-12), axis=1)
    return candidates[mask]


# ------------------- Algorithms -----------------


def sequential_dykstra(  # ruff: ignore[too-many-arguments]
    candidates: np.ndarray,
    n_points: int,
    degree: int,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"] = "D",
    alpha: float = 0.0,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: ModelDiff = None,
    replicates: bool = False,
) -> np.ndarray:
    """
    Construct an optimal design using the sequential (Dykstra) greedy algorithm.

    Parameters
    ----------
    candidates : ndarray of shape (N, k)
        Candidate points in the design space.
    n_points : int
        Number of points to select for the design.
    degree : int
        Polynomial degree of the model.
    criterion : {'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'}, optional
        Optimality criterion to maximize (default is 'D').
    alpha : float, optional
        Augmentation parameter for information matrix (default is 0.0).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of the model
        parameters whose variance is minimized (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N,) or callable, optional
        T-optimality: difference between the responses of the rival
        model and the fitted model, either at each candidate or as a
        function of an array of points. Required for the T criterion.
    replicates : bool, optional
        If True, a candidate may be run more than once, as in the
        published algorithms; exact optimal designs often need this (a
        quadratic in one factor with more than 3 runs, for instance).
        By default every run of the design is a different candidate.

    Returns
    -------
    design : ndarray of shape (n_points, k)
        Selected design points.

    Raises
    ------
    ValueError
        If n_points is less than 1, the criterion is unknown, or an input
        of the criterion is missing or has the wrong shape.
    """
    candidates = np.asarray(candidates, dtype=float)
    if n_points < 1:
        raise ValueError("n_points must be at least 1")
    if not replicates and n_points > candidates.shape[0]:
        msg = (
            f"n_points ({n_points}) exceeds the number of candidates "
            f"({candidates.shape[0]}); pass replicates=True to repeat runs"
        )
        raise ValueError(msg)
    score = _make_scorer(
        candidates,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
    )

    design = np.empty((0, candidates.shape[1]), dtype=float)
    remaining = candidates.copy()

    for _ in range(n_points):
        j_best, _ = _best_single_add(design, remaining, score)
        j_best = max(j_best, 0)
        design = np.vstack([design, remaining[j_best]])
        if not replicates:
            remaining = np.delete(remaining, j_best, axis=0)

    return design


def simple_exchange_wynn_mitchell(  # ruff: ignore[too-many-arguments, too-many-positional-arguments]
    candidates: np.ndarray,
    n_points: int,
    degree: int,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"] = "D",
    alpha: float = 0.0,
    max_iter: int = 200,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: ModelDiff = None,
    replicates: bool = False,
) -> np.ndarray:
    """
    Construct an optimal design using the simple exchange (Wynn-Mitchell)
    algorithm.

    Parameters
    ----------
    candidates : ndarray of shape (N, k)
        Candidate points in the design space.
    n_points : int
        Number of points to select for the design.
    degree : int
        Polynomial degree of the model.
    criterion : {'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'}, optional
        Optimality criterion to maximize (default is 'D').
    alpha : float, optional
        Augmentation parameter for information matrix (default is 0.0).
    max_iter : int, optional
        Maximum number of iterations (default is 200).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of the model
        parameters whose variance is minimized (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N,) or callable, optional
        T-optimality: difference between the responses of the rival
        model and the fitted model, either at each candidate or as a
        function of an array of points. Required for the T criterion.
    replicates : bool, optional
        If True, a candidate may be run more than once, as in the
        published algorithms; exact optimal designs often need this (a
        quadratic in one factor with more than 3 runs, for instance).
        By default every run of the design is a different candidate.

    Returns
    -------
    design : ndarray of shape (n_points, k)
        Selected design points.

    Raises
    ------
    ValueError
        If n_points is less than 1, the criterion is unknown, or an input
        of the criterion is missing or has the wrong shape.
    """
    candidates = np.asarray(candidates, dtype=float)
    score = _make_scorer(
        candidates,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
    )

    design = sequential_dykstra(
        candidates,
        n_points,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
        replicates=replicates,
    )

    best_score = score(design)

    for _ in range(max_iter):
        # Drop
        drop_idx, _ = _best_single_drop(design, score)
        # Remove from pool those already in design except the one
        # we plan to drop. Using exact match; for numeric safety,
        # use all rows then filter after equality check
        design_wo = np.delete(design, drop_idx, axis=0)

        # Add
        pool_avail = _available(candidates, design_wo, replicates=replicates)

        add_idx, cand_score = _best_single_add(design_wo, pool_avail, score)

        if add_idx >= 0 and cand_score > best_score + 1e-12:
            design = np.vstack([design_wo, pool_avail[add_idx]])
            best_score = cand_score
        else:
            break

    return design


def fedorov(  # ruff: ignore[too-many-arguments, too-many-positional-arguments]
    candidates: np.ndarray,
    n_points: int,
    degree: int,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"] = "D",
    alpha: float = 0.0,
    max_iter: int = 200,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: ModelDiff = None,
    replicates: bool = False,
) -> np.ndarray:
    """
    Construct an optimal design using the Fedorov exchange algorithm.

    Parameters
    ----------
    candidates : ndarray of shape (N, k)
        Candidate points in the design space.
    n_points : int
        Number of points to select for the design.
    degree : int
        Polynomial degree of the model.
    criterion : {'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'}, optional
        Optimality criterion to maximize (default is 'D').
    alpha : float, optional
        Augmentation parameter for information matrix (default is 0.0).
    max_iter : int, optional
        Maximum number of iterations (default is 200).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of the model
        parameters whose variance is minimized (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N,) or callable, optional
        T-optimality: difference between the responses of the rival
        model and the fitted model, either at each candidate or as a
        function of an array of points. Required for the T criterion.
    replicates : bool, optional
        If True, a candidate may be run more than once, as in the
        published algorithms; exact optimal designs often need this (a
        quadratic in one factor with more than 3 runs, for instance).
        By default every run of the design is a different candidate.

    Returns
    -------
    design : ndarray of shape (n_points, k)
        Selected design points.

    Raises
    ------
    ValueError
        If n_points is less than 1, the criterion is unknown, or an input
        of the criterion is missing or has the wrong shape.
    """
    candidates = np.asarray(candidates, dtype=float)
    score = _make_scorer(
        candidates,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
    )

    design = sequential_dykstra(
        candidates,
        n_points,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
        replicates=replicates,
    )

    best = score(design)

    for _ in range(max_iter):
        improved = False
        pool = _available(candidates, design, replicates=replicates)

        # evaluate all swaps (i in design, j in pool)
        best_i, best_j, best_val = -1, -1, best
        for i in range(design.shape[0]):
            for j in range(pool.shape[0]):
                trial = design.copy()
                trial[i] = pool[j]
                s = score(trial)
                if s > best_val + 1e-12:
                    best_i, best_j, best_val = i, j, s

        if best_i >= 0:
            design[best_i] = pool[best_j]
            best = best_val
            improved = True

        if not improved:
            break

    return design


def modified_fedorov(  # ruff: ignore[too-many-arguments, too-many-positional-arguments]
    candidates: np.ndarray,
    n_points: int,
    degree: int,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"] = "D",
    alpha: float = 0.0,
    max_iter: int = 100,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: ModelDiff = None,
    replicates: bool = False,
) -> np.ndarray:
    """
    Construct an optimal design using the modified Fedorov algorithm.

    Parameters
    ----------
    candidates : ndarray of shape (N, k)
        Candidate points in the design space.
    n_points : int
        Number of points to select for the design.
    degree : int
        Polynomial degree of the model.
    criterion : {'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'}, optional
        Optimality criterion to maximize (default is 'D').
    alpha : float, optional
        Augmentation parameter for information matrix (default is 0.0).
    max_iter : int, optional
        Maximum number of iterations (default is 100).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of the model
        parameters whose variance is minimized (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N,) or callable, optional
        T-optimality: difference between the responses of the rival
        model and the fitted model, either at each candidate or as a
        function of an array of points. Required for the T criterion.
    replicates : bool, optional
        If True, a candidate may be run more than once, as in the
        published algorithms; exact optimal designs often need this (a
        quadratic in one factor with more than 3 runs, for instance).
        By default every run of the design is a different candidate.

    Returns
    -------
    design : ndarray of shape (n_points, k)
        Selected design points.

    Raises
    ------
    ValueError
        If n_points is less than 1, the criterion is unknown, or an input
        of the criterion is missing or has the wrong shape.
    """
    candidates = np.asarray(candidates, dtype=float)
    score = _make_scorer(
        candidates,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
    )

    design = sequential_dykstra(
        candidates,
        n_points,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
        replicates=replicates,
    )

    for _ in range(max_iter):
        base = score(design)
        any_change = False

        # Try replace each point with best candidate for that position
        new_design = design.copy()
        for i in range(design.shape[0]):
            # candidates not used by the other rows of the design
            pool = _available(
                candidates,
                np.delete(new_design, i, axis=0),
                replicates=replicates,
            )
            best_val = base
            best_row = None
            for j in range(pool.shape[0]):
                trial = new_design.copy()
                trial[i] = pool[j]
                s = score(trial)
                if s > best_val + 1e-12:
                    best_val = s
                    best_row = pool[j]
            if best_row is not None:
                new_design[i] = best_row
                base = best_val
                any_change = True

        design = new_design
        if not any_change:
            break

    return design


def detmax(  # ruff: ignore[too-many-arguments, too-many-positional-arguments]
    candidates: np.ndarray,
    n_points: int,
    degree: int,
    criterion: Literal["D", "A", "I", "C", "E", "G", "V", "S", "T"] = "D",
    alpha: float = 0.0,
    max_iter: int = 100,
    *,
    c_vector: np.ndarray | None = None,
    test_points: np.ndarray | None = None,
    model_diff: ModelDiff = None,
    replicates: bool = False,
) -> np.ndarray:
    """
    Construct an optimal design using the DETMAX algorithm
    (exchange with excursions).

    Parameters
    ----------
    candidates : ndarray of shape (N, k)
        Candidate points in the design space.
    n_points : int
        Number of points to select for the design.
    degree : int
        Polynomial degree of the model.
    criterion : {'D', 'A', 'I', 'C', 'E', 'G', 'V', 'S', 'T'}, optional
        Optimality criterion to maximize (default is 'D').
    alpha : float, optional
        Augmentation parameter for information matrix (default is 0.0).
    max_iter : int, optional
        Maximum number of iterations (default is 100).
    c_vector : ndarray of shape (p,), optional
        C-optimality: coefficients of the linear combination of the model
        parameters whose variance is minimized (default: all ones).
    test_points : ndarray of shape (m, k), optional
        V-optimality: points at which the average prediction variance is
        minimized (default: the candidates).
    model_diff : ndarray of shape (N,) or callable, optional
        T-optimality: difference between the responses of the rival
        model and the fitted model, either at each candidate or as a
        function of an array of points. Required for the T criterion.
    replicates : bool, optional
        If True, a candidate may be run more than once, as in the
        published algorithms; exact optimal designs often need this (a
        quadratic in one factor with more than 3 runs, for instance).
        By default every run of the design is a different candidate.

    Returns
    -------
    design : ndarray of shape (n_points, k)
        Selected design points.

    Raises
    ------
    ValueError
        If n_points is less than 1, the criterion is unknown, or an input
        of the criterion is missing or has the wrong shape.
    """
    candidates = np.asarray(candidates, dtype=float)
    score = _make_scorer(
        candidates,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
    )

    design = simple_exchange_wynn_mitchell(
        candidates,
        n_points,
        degree,
        criterion,
        alpha,
        c_vector=c_vector,
        test_points=test_points,
        model_diff=model_diff,
        replicates=replicates,
    )

    best = score(design)

    for _ in range(max_iter):
        # Try a Fedorov-style single swap first
        improved = False
        pool = _available(candidates, design, replicates=replicates)

        best_i, best_j, best_val = -1, -1, best
        for i in range(design.shape[0]):
            for j in range(pool.shape[0]):
                trial = design.copy()
                trial[i] = pool[j]
                s = score(trial)
                if s > best_val + 1e-12:
                    best_i, best_j, best_val = i, j, s

        if best_i >= 0:
            design[best_i] = pool[best_j]
            best = best_val
            improved = True

        if improved:
            continue

        # Excursion: add best extra, then drop worst
        add_idx, _add_score = _best_single_add(design, pool, score)
        if add_idx < 0:
            break  # nothing to add

        expanded = np.vstack([design, pool[add_idx]])
        # Drop worst from expanded
        drop_idx, final_score = _best_single_drop(expanded, score)

        if final_score > best + 1e-12:
            design = np.delete(expanded, drop_idx, axis=0)
            best = final_score
            improved = True
        else:
            break

    return design
