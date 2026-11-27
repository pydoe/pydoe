r"""
Optimal Experimental Design (OED)
=================================

This module implements optimality criteria for experimental design,
as used in the field of optimal experimental design (OED).

Optimal experimental designs are a class of experimental designs that
are optimal with respect to some statistical criterion, typically related
to the information matrix of the model. The goal is to estimate model parameters
with minimum variance and/or maximum information, often reducing the number of
experimental runs required for a given precision.

Key optimality criteria implemented here (see Wikipedia: https://en.wikipedia.org/wiki/Optimal_experimental_design):

- **D-optimality**: Maximizes $$|X'X|$$, giving the most information
in parameters.
- **A-optimality**: Minimizes $$\trace((X'X)^{-1})$$, reducing average parameter
variance.
- **E-optimality**: Maximizes smallest eigenvalue of $$X'X$$, improving
worst-case precision.
- **G-optimality**: Minimizes maximum prediction variance, improving
worst-case prediction.
- **I-optimality**: Minimizes average prediction variance over the design space.
- **V-optimality**: Minimizes average prediction variance at specified points.
- **C-optimality**: Minimizes variance of a chosen linear combination of
parameters.
- **S-optimality**: Maximizes orthogonality and determinant, ensuring balanced
design (Shin and Xiu, 2016).
- **T-optimality**: Maximizes the lack of fit of the model to the responses
of a rival model at the design points (Atkinson and Fedorov, 1975).

References
----------
Atkinson, A. C., & Fedorov, V. V. (1975). The design of experiments for
discriminating between two rival models. *Biometrika*, 62(1), 57-70.
https://doi.org/10.1093/biomet/62.1.57

Dette, H., & Titoff, S. (2009). Optimal discrimination designs. *The
Annals of Statistics*, 37(4), 2056-2082. https://doi.org/10.1214/08-AOS635

Shin, Y., & Xiu, D. (2016). Nonadaptive quasi-optimal points selection
for least squares linear regression. *SIAM Journal on Scientific
Computing*, 38(1), A385-A411. https://doi.org/10.1137/15M1015868

Welch, W. J. (1984). Computer-aided design of experiments for response
estimation. *Technometrics*, 26(3), 217-224.
https://doi.org/10.1080/00401706.1984.10487958
"""

import warnings

import numpy as np
from scipy.linalg import LinAlgWarning, inv


def regularized_inv(M: np.ndarray, reg_param: float = 1e-8) -> np.ndarray:
    """
    Compute the inverse of M, falling back to Tikhonov regularization when M
    is ill-conditioned or singular.

    ``scipy.linalg.inv`` raises ``LinAlgError`` only for exactly singular
    matrices but issues ``LinAlgWarning`` for ill-conditioned ones (rcond near
    zero).  By promoting that warning to an exception inside the context
    manager we catch both cases uniformly and apply the regularization
    ``M_reg = M + reg_param * I``, which shifts every eigenvalue up by
    *reg_param* and guarantees positive-definiteness.

    Both inversions use ``assume_a="pos"`` (Cholesky), so a numerically
    indefinite matrix (e.g. a positive-semidefinite information matrix with
    a tiny negative eigenvalue from roundoff) is regularized instead of
    yielding an inverse with a negative trace.

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Symmetric matrix to invert.
    reg_param : float, optional
        Tikhonov regularization strength (default 1e-8).

    Returns
    -------
    ndarray of shape (p, p)
        Inverse (or regularized inverse) of M.

    Raises
    ------
    numpy.linalg.LinAlgError
        If M is still not positive-definite after regularization.
    """
    with warnings.catch_warnings():
        warnings.simplefilter("error", LinAlgWarning)
        try:
            return inv(M, assume_a="pos")
        except (np.linalg.LinAlgError, LinAlgWarning):
            M_reg = M + reg_param * np.eye(M.shape[0])
            return inv(M_reg, assume_a="pos")


def d_optimality(M: np.ndarray) -> float:
    r"""
    Compute D-optimality criterion for a given information matrix.

    D-optimality maximizes the determinant of the information matrix.

    The D-optimality criterion is:

    $$\det(M)$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        Determinant of the information matrix.
    """
    return float(np.linalg.det(M))


def a_optimality(M: np.ndarray) -> float:
    r"""
    Compute A-optimality criterion for a given information matrix.

    A-optimality minimizes the trace of the inverse information matrix.
    Returns the negative value for maximization.

    The A-optimality criterion is:

    $$-\operatorname{tr}(M^{-1})$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        Negative trace of the inverse information matrix.
    """
    return -float(np.trace(regularized_inv(M)))


def i_optimality(M_X: np.ndarray, moment_matrix: np.ndarray) -> float:
    r"""
    Compute I-optimality criterion for a given information matrix
    and moment matrix.

    I-optimality minimizes the average prediction variance over
    the design space. Returns the negative value for maximization.

    The I-optimality criterion is:

    $$-\operatorname{tr}(M_{\text{moment}} M_X^{-1})$$

    Parameters
    ----------
    M_X : ndarray of shape (p, p)
        Information matrix.
    moment_matrix : ndarray of shape (p, p)
        Moment matrix for the design space.

    Returns
    -------
    float
        Negative trace of moment_matrix @ inv(M_X).
    """
    return -float(np.trace(moment_matrix @ regularized_inv(M_X)))


def c_optimality(M: np.ndarray, c: np.ndarray) -> float:
    r"""
    Compute C-optimality criterion for a given information matrix
    and contrast vector.

    C-optimality minimizes the variance of a linear combination of parameters.
    Returns the negative value for maximization.

    The C-optimality criterion is:

    $$-c^T M^{-1} c$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    c : ndarray of shape (p,)
        Contrast vector.

    Returns
    -------
    float
        Negative variance of the linear combination.
    """
    return -float(c.T @ regularized_inv(M) @ c)


def e_optimality(M: np.ndarray) -> float:
    r"""
    Compute E-optimality criterion for a given information matrix.

    E-optimality maximizes the smallest eigenvalue of the information matrix.

    The E-optimality criterion is:

    $$\min \operatorname{eig}(M)$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        Smallest eigenvalue of the information matrix.
    """
    return float(np.min(np.linalg.eigvalsh(M)))


def _pred_var_rows(rows: np.ndarray, M_inv: np.ndarray) -> np.ndarray:
    # rows: array of shape (m, p); M_inv: (p, p)
    # returns vector of x M_inv x^T for each row x
    return np.einsum("ij,jk,ik->i", rows, M_inv, rows)


def g_optimality(M: np.ndarray, candidates: np.ndarray) -> float:
    r"""
    Compute G-optimality criterion for a given information matrix
    and candidate set.

    G-optimality minimizes the maximum prediction variance over
    the candidate set. Returns the negative value for maximization.

    The G-optimality criterion is:

    $$-\max_{x \in \text{candidates}} x^T M^{-1} x$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    candidates : ndarray of shape (N, p)
        Candidate points for prediction variance evaluation.

    Returns
    -------
    float
        Negative maximum prediction variance.
    """
    M_inv = regularized_inv(M)
    variances = _pred_var_rows(np.asarray(candidates), M_inv)
    return -float(np.max(variances))


def i_pred_variance(M: np.ndarray, candidates: np.ndarray) -> float:
    """
    (Aux) Average prediction variance over candidates (for diagnostics).

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    candidates : ndarray of shape (N, p)
        Candidate points for prediction variance evaluation.

    Returns
    -------
    float
        Average prediction variance over candidates.
    """
    M_inv = regularized_inv(M)
    variances = _pred_var_rows(np.asarray(candidates), M_inv)
    return float(np.mean(variances))


def v_optimality(M: np.ndarray, test_points: np.ndarray) -> float:
    r"""
    Compute V-optimality criterion for a given information matrix
    and test points.

    V-optimality minimizes the average prediction variance over
    specified test points. Returns the negative value for maximization.

    The V-optimality criterion is:

    $$-\frac{1}{m} \sum_{i=1}^m x_i^T M^{-1} x_i$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    test_points : ndarray of shape (m, p)
        Test points for prediction variance evaluation.

    Returns
    -------
    float
        Negative average prediction variance.
    """
    M_inv = regularized_inv(M)
    variances = _pred_var_rows(np.asarray(test_points), M_inv)
    return -float(np.mean(variances))


def s_optimality(M: np.ndarray) -> float:
    r"""
    Compute S-optimality criterion for a given information matrix.

    S-optimality (Shin and Xiu, 2016) measures the mutual orthogonality of
    the columns of the design matrix $$X$$ together with the determinant
    of the information matrix.

    The S-optimality criterion is:

    $$\frac{\sqrt{\det(M)}}{\prod_j \sqrt{M_{jj}}}
    = \frac{\sqrt{\det(X^T X)}}{\prod_j \lVert X_j \rVert}$$

    which is Shin and Xiu's $$S(X)$$ raised to the power $$p$$. It does not
    depend on the scale of the columns, lies between 0 and 1 (Hadamard's
    inequality), and is 1 exactly when the columns of $$X$$ are orthogonal.

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        S-optimality value.

    References
    ----------
    Shin, Y., & Xiu, D. (2016). Nonadaptive quasi-optimal points selection
    for least squares linear regression. *SIAM Journal on Scientific
    Computing*, 38(1), A385-A411. https://doi.org/10.1137/15M1015868
    """
    col_rms = np.sqrt(np.clip(np.diag(M), 1e-15, None))
    det = max(float(np.linalg.det(M)), 0.0)
    return float(np.sqrt(det) / np.prod(col_rms))


def t_optimality(X: np.ndarray, model_diff_subset: np.ndarray) -> float:
    r"""
    Compute T-optimality criterion for model discrimination at design points.

    T-optimality maximizes discrimination between two models at the chosen
    design points (Atkinson and Fedorov, 1975): the lack of fit that
    remains when the model with design matrix $$X$$ is fitted to the
    responses of the rival model.

    The T-optimality criterion is:

    $$d^T (I - P_X) d = \min_{\beta} \lVert d - X \beta \rVert^2$$

    where $$P_X = X (X^T X)^{-1} X^T$$ and $$d$$ is the model difference
    vector: the responses of the rival model at the design points, or
    their difference from any response of the fitted model.

    Parameters
    ----------
    X : ndarray of shape (n_points, p)
        Design matrix.
    model_diff_subset : ndarray of shape (n_points,)
        Differences between models evaluated at the subset.

    Returns
    -------
    float
        Discrimination value: the residual sum of squares, which is 0
        when the design cannot tell the two models apart. A residual sum
        of squares within round-off of 0, below
        $$10^{-10} \lVert d \rVert^2$$, is returned as exactly 0, so that
        designs that fit the rival model exactly tie, whatever the
        floating-point library.
    """
    d = np.asarray(model_diff_subset, dtype=float).reshape(-1)
    beta = np.linalg.lstsq(X, d, rcond=None)[0]
    residual = d - X @ beta
    rss = float(residual @ residual)
    # Exact fits leave round-off of order 1e-30 that differs between BLAS
    # builds; a search comparing such values would follow that noise.
    if rss <= 1e-10 * float(d @ d):
        return 0.0
    return rss
