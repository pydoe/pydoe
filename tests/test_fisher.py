import numpy as np
import pytest

from pydoe import fisher_information, jacobian_optimal_design


def _line_jacobian():
    x = np.linspace(0, 1, 11)
    return np.stack([np.ones_like(x), x], axis=1)


def test_fim_2d_matches_jtj():
    J = _line_jacobian()
    assert np.allclose(fisher_information(J), J.T @ J)


def test_fim_covariance_forms():
    J = _line_jacobian()
    var = np.full(len(J), 4.0)
    expected = J.T @ J / 4.0
    assert np.allclose(fisher_information(J, covariance=4.0), expected)
    assert np.allclose(fisher_information(J, covariance=var), expected)
    assert np.allclose(fisher_information(J, covariance=np.diag(var)), expected)


def test_fim_3d_is_mean_over_points():
    J = _line_jacobian()
    J3 = np.stack([J, 3 * J], axis=2)
    expected = (J.T @ J + 9 * J.T @ J) / 2
    assert np.allclose(fisher_information(J3), expected)


def test_fim_rows_subset_with_full_covariance():
    J = _line_jacobian()
    cov = np.diag(np.arange(1.0, 12.0))
    rows = np.array([0, 5, 10])
    Js = J[rows]
    expected = Js.T @ np.linalg.inv(cov[np.ix_(rows, rows)]) @ Js
    assert np.allclose(fisher_information(J, rows, cov), expected)


def test_design_endpoints_for_line():
    idx, info = jacobian_optimal_design(_line_jacobian(), 4)
    assert sorted(idx.tolist()) == [0, 0, 10, 10]
    assert info["score"] > 0


def test_design_3d_and_covariance_shift_points():
    J = _line_jacobian()
    J3 = np.stack([J, 2 * J], axis=2)
    idx, _ = jacobian_optimal_design(J3, 4)
    assert sorted(idx.tolist()) == [0, 0, 10, 10]
    # very noisy endpoints push the design inward
    var = np.ones(len(J))
    var[[0, 10]] = 1e6
    idx, _ = jacobian_optimal_design(J, 4, covariance=var)
    assert not set(idx.tolist()) & {0, 10} or len(set(idx.tolist())) > 1


@pytest.mark.parametrize("criterion", ["A", "E", "S"])
def test_other_criteria_run(criterion):
    idx, info = jacobian_optimal_design(
        _line_jacobian(), 4, criterion=criterion
    )
    assert len(idx) == 4
    assert info["fim"].shape == (2, 2)


def test_errors():
    with pytest.raises(ValueError, match="criterion"):
        jacobian_optimal_design(_line_jacobian(), 3, criterion="X")
    with pytest.raises(ValueError, match="2D"):
        fisher_information(np.ones(3))
