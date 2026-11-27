"""
Every optimal-design algorithm against every optimality criterion.

The designs are checked against two kinds of oracle:

- the global optimum of small problems, found by enumerating every design,
  with the criteria recomputed here from their textbook formulas;
- optimal designs and criterion values published in the literature.
"""

import itertools

import numpy as np
import pytest

from pydoe import (
    build_design_matrix,
    detmax,
    fedorov,
    generate_candidate_set,
    modified_fedorov,
    optimal_design,
    s_optimality,
    sequential_dykstra,
    simple_exchange_wynn_mitchell,
    t_optimality,
)


METHODS = [
    "sequential",
    "simple_exchange",
    "fedorov",
    "modified_fedorov",
    "detmax",
]
EXCHANGE_METHODS = METHODS[1:]
FEDOROV_FAMILY = ["fedorov", "modified_fedorov", "detmax"]
CRITERIA = ["D", "A", "I", "C", "E", "G", "V", "S", "T"]
FUNCTIONS = {
    "sequential": sequential_dykstra,
    "simple_exchange": simple_exchange_wynn_mitchell,
    "fedorov": fedorov,
    "modified_fedorov": modified_fedorov,
    "detmax": detmax,
}
TOL = 1e-8


def _cubic(points):
    return points[:, 0] ** 3


def _dette_titoff(points):
    # Rival model of Dette and Titoff (2009), Example 2.3
    return 1 + points[:, 0] + points[:, 0] ** 3


def _cubic_2d(points):
    return points[:, 0] ** 3 + points[:, 0] * points[:, 1] ** 2


def _second_order_2d(points):
    return points[:, 0] * points[:, 1] + points[:, 0] ** 2


LINE = np.linspace(-1, 1, 5).reshape(-1, 1)
GRID = generate_candidate_set(n_factors=2, n_levels=3)

# name -> (candidates, n_points, degree, replicates, inputs per criterion)
SCENARIOS = {
    "line_quadratic_n3": (
        LINE,
        3,
        2,
        False,
        {
            "C": {"c_vector": [0, 0, 1]},
            "V": {"test_points": [[-0.5], [0.5]]},
            "T": {"model_diff": _cubic},
        },
    ),
    "line_quadratic_n6_replicates": (
        LINE,
        6,
        2,
        True,
        {
            "C": {"c_vector": [0, 0, 1]},
            "V": {"test_points": [[-0.5], [0.5]]},
            "T": {"model_diff": _cubic},
        },
    ),
    "line_linear_n6_replicates": (
        LINE,
        6,
        1,
        True,
        {
            "C": {"c_vector": [0, 1]},
            "V": {"test_points": [[-0.5], [0.5]]},
            "T": {"model_diff": _dette_titoff},
        },
    ),
    "grid_quadratic_n7": (
        GRID,
        7,
        2,
        False,
        {
            "C": {"c_vector": [0, 0, 0, 1, 0, 0]},
            "V": {"test_points": [[0, 0], [0.5, 0.5], [-0.5, 0.5]]},
            "T": {"model_diff": _cubic_2d},
        },
    ),
    "grid_linear_n4": (
        GRID,
        4,
        1,
        False,
        {
            "C": {"c_vector": [0, 1, 0]},
            "V": {"test_points": [[0, 0], [1, 1]]},
            "T": {"model_diff": _second_order_2d},
        },
    ),
}

# Cells in which the single-point exchanges of the Fedorov family stop at
# a local optimum below the global one. Every other cell reaches it.
LOCAL_OPTIMA = {
    ("line_quadratic_n3", "V"),
    ("line_quadratic_n6_replicates", "G"),
    ("line_linear_n6_replicates", "G"),
    ("grid_quadratic_n7", "E"),
    ("grid_quadratic_n7", "S"),
    ("grid_quadratic_n7", "T"),
    ("grid_linear_n4", "E"),
    ("grid_linear_n4", "G"),
    ("grid_linear_n4", "S"),
}


def reference_score(design, candidates, degree, criterion, inputs):  # ruff: ignore[too-many-return-statements]
    """The criteria from their definitions, larger is better.

    A design that cannot estimate what the criterion needs scores -inf.
    """
    X = build_design_matrix(design, degree)
    n, p = X.shape
    M = X.T @ X / n
    full_rank = np.linalg.matrix_rank(X) == p

    if criterion == "T":
        d = np.asarray(inputs["model_diff"](design), dtype=float)
        residual = d - X @ (np.linalg.pinv(X) @ d)
        return float(residual @ residual)
    if criterion == "C":
        c = np.asarray(inputs["c_vector"], dtype=float)
        M_pinv = np.linalg.pinv(M)
        if not np.allclose(M @ M_pinv @ c, c, atol=1e-9):
            return -np.inf  # c'beta is not estimable
        return -float(c @ M_pinv @ c)
    if not full_rank:
        return -np.inf

    M_inv = np.linalg.inv(M)
    X0 = build_design_matrix(candidates, degree)
    if criterion == "D":
        return float(np.linalg.det(M))
    if criterion == "A":
        return -float(np.trace(M_inv))
    if criterion == "E":
        return float(np.linalg.eigvalsh(M).min())
    if criterion == "S":
        return float(np.sqrt(np.linalg.det(M)) / np.prod(np.sqrt(np.diag(M))))
    if criterion == "I":
        return -float(np.mean([x @ M_inv @ x for x in X0]))
    if criterion == "G":
        return -float(max(x @ M_inv @ x for x in X0))
    assert criterion == "V"
    points = np.atleast_2d(np.asarray(inputs["test_points"], dtype=float))
    Xt = build_design_matrix(points, degree)
    return -float(np.mean([x @ M_inv @ x for x in Xt]))


_OPTIMA = {}


def global_optimum(scenario, criterion):
    """Best reference score over every design of the scenario."""
    key = (scenario, criterion)
    if key not in _OPTIMA:
        candidates, n, degree, replicates, extra = SCENARIOS[scenario]
        choose = (
            itertools.combinations_with_replacement
            if replicates
            else itertools.combinations
        )
        _OPTIMA[key] = max(
            reference_score(
                candidates[list(rows)],
                candidates,
                degree,
                criterion,
                extra.get(criterion, {}),
            )
            for rows in choose(range(len(candidates)), n)
        )
    return _OPTIMA[key]


def run(scenario, criterion, method):
    candidates, n, degree, replicates, extra = SCENARIOS[scenario]
    return optimal_design(
        candidates,
        n,
        degree,
        criterion,
        method,
        replicates=replicates,
        **extra.get(criterion, {}),
    )


@pytest.mark.parametrize("criterion", CRITERIA)
@pytest.mark.parametrize("method", METHODS)
def test_method_with_criterion(criterion, method):
    """One algorithm with one criterion, on every scenario."""
    for scenario, (
        candidates,
        n,
        degree,
        replicates,
        extra,
    ) in SCENARIOS.items():
        inputs = extra.get(criterion, {})
        design, info = run(scenario, criterion, method)
        where = f"{scenario}, {criterion}, {method}"

        # a valid design: n candidates, distinct unless replicates are on
        assert design.shape == (n, candidates.shape[1]), where
        for row in design:
            assert np.any(np.all(np.isclose(candidates, row), axis=1)), where
        if not replicates:
            assert len(np.unique(design, axis=0)) == n, where
        assert info["criterion"] == criterion
        assert info["method"] == method
        assert info["n_runs"] == n

        # the reported score is the criterion as the literature defines it
        achieved = reference_score(
            design, candidates, degree, criterion, inputs
        )
        assert np.isfinite(achieved), where
        assert info["score"] == pytest.approx(achieved, rel=1e-6, abs=1e-7), (
            where
        )

        # C- and T-optimal designs may be singular by nature (they serve
        # one linear combination or one model comparison); the others
        # must be able to estimate the whole model
        if criterion not in {"C", "T"}:
            X = build_design_matrix(design, degree)
            assert np.linalg.matrix_rank(X) == X.shape[1], where
            assert info["D_eff"] > 0, where
            assert info["A_eff"] > 0, where

        # the function behind the method gives the same design
        direct = FUNCTIONS[method](
            candidates, n, degree, criterion, replicates=replicates, **inputs
        )
        np.testing.assert_array_equal(direct, design)

        # against the global optimum found by enumeration
        optimum = global_optimum(scenario, criterion)
        assert achieved <= optimum + TOL, where
        if method in FEDOROV_FAMILY:
            if (scenario, criterion) in LOCAL_OPTIMA:
                # single exchanges are known to stop short here; if a
                # method starts reaching the optimum, tighten LOCAL_OPTIMA
                assert achieved > -np.inf, where
            else:
                assert achieved == pytest.approx(optimum, rel=1e-6, abs=1e-7), (
                    where
                )

        # exchange algorithms start from the sequential design and only
        # accept improvements
        if method != "sequential":
            _, start = run(scenario, criterion, "sequential")
            assert info["score"] >= start["score"] - TOL, where


def test_local_optima_list_is_current():
    """Every listed cell still falls short for some Fedorov-type method."""
    for scenario, criterion in sorted(LOCAL_OPTIMA):
        candidates, _n, degree, _replicates, extra = SCENARIOS[scenario]
        optimum = global_optimum(scenario, criterion)
        achieved = [
            reference_score(
                run(scenario, criterion, method)[0],
                candidates,
                degree,
                criterion,
                extra.get(criterion, {}),
            )
            for method in FEDOROV_FAMILY
        ]
        assert min(achieved) < optimum - TOL, (scenario, criterion)


def _counts(design):
    """Number of runs at each distinct point of a one-factor design."""
    values, counts = np.unique(np.round(design[:, 0], 9), return_counts=True)
    return dict(zip(values.tolist(), counts.tolist(), strict=True))


class TestPublishedOptimalDesigns:
    """Designs and values known from the literature."""

    def test_d_optimal_quadratic_in_one_factor(self):
        for method in EXCHANGE_METHODS:
            # Equal weights on -1, 0, 1 (Hoel, 1958); det(M) = 4/27.
            design, info = optimal_design(
                LINE, 6, 2, "D", method, replicates=True
            )
            assert _counts(design) == {-1.0: 2, 0.0: 2, 1.0: 2}
            assert info["score"] == pytest.approx(4 / 27)
            # G-efficiency 100 %: the largest prediction variance equals p
            # (Kiefer and Wolfowitz equivalence theorem).
            X = build_design_matrix(design, 2)
            M_inv = np.linalg.inv(X.T @ X / 6)
            grid = build_design_matrix(
                np.linspace(-1, 1, 201).reshape(-1, 1), 2
            )
            assert max(x @ M_inv @ x for x in grid) == pytest.approx(3.0)

    def test_a_optimal_quadratic_in_one_factor(self):
        for method in EXCHANGE_METHODS:
            # Weights 1/4, 1/2, 1/4 on -1, 0, 1; trace(M^-1) = 8.
            design, info = optimal_design(
                LINE, 4, 2, "A", method, replicates=True
            )
            assert _counts(design) == {-1.0: 1, 0.0: 2, 1.0: 1}
            assert info["score"] == pytest.approx(-8.0)

    def test_e_optimal_quadratic_in_one_factor(self):
        for method in EXCHANGE_METHODS:
            # Weights 1/5, 3/5, 1/5 on the Chebyshev points -1, 0, 1
            # (Pukelsheim and Studden, 1993); smallest eigenvalue 1/5.
            design, info = optimal_design(
                LINE, 5, 2, "E", method, replicates=True
            )
            assert _counts(design) == {-1.0: 1, 0.0: 3, 1.0: 1}
            assert info["score"] == pytest.approx(0.2)

    def test_g_optimal_quadratic_in_one_factor(self):
        for method in EXCHANGE_METHODS:
            # With 3 runs the G-optimal design is the D-optimal one and the
            # largest prediction variance over the region is p = 3.
            design, info = optimal_design(LINE, 3, 2, "G", method)
            assert _counts(design) == {-1.0: 1, 0.0: 1, 1.0: 1}
            assert info["score"] == pytest.approx(-3.0)

    def test_c_optimal_slope_of_a_line(self):
        for method in EXCHANGE_METHODS:
            # The slope is estimated best with half of the runs at each end.
            design, info = optimal_design(
                LINE, 6, 1, "C", method, replicates=True, c_vector=[0, 1]
            )
            assert _counts(design) == {-1.0: 3, 1.0: 3}
            assert info["score"] == pytest.approx(-1.0)

    def test_s_optimal_line_has_orthogonal_columns(self):
        for method in EXCHANGE_METHODS:
            # S = 1 exactly when the model columns are orthogonal.
            design, info = optimal_design(
                LINE, 6, 1, "S", method, replicates=True
            )
            assert info["score"] == pytest.approx(1.0)
            assert design[:, 0].sum() == pytest.approx(0.0)

    def test_t_optimal_cubic_against_a_line(self):
        for method in EXCHANGE_METHODS:
            # Dette and Titoff (2009), Example 2.3: discriminating
            # 1 + x + x^3 from a straight line on [-1, 1]. The optimal designs
            # sit on -1, -1/2, 1/2, 1 and the criterion is 1/16 per run.
            design, info = optimal_design(
                LINE,
                6,
                1,
                "T",
                method,
                replicates=True,
                model_diff=_dette_titoff,
            )
            assert set(_counts(design)) <= {-1.0, -0.5, 0.5, 1.0}
            assert info["score"] == pytest.approx(6 / 16)

    def test_d_optimal_quadratic_on_the_3x3_grid(self):
        # Exact D-optimal designs of the full quadratic in two factors:
        # det(X'X) for 6 to 9 runs.
        published = {6: 256.0, 7: 960.0, 8: 2304.0, 9: 5184.0}
        for method in EXCHANGE_METHODS:
            for n_points, det_xtx in published.items():
                _design, info = optimal_design(GRID, n_points, 2, "D", method)
                assert info["det_XTX"] == pytest.approx(det_xtx), method

    def test_d_optimal_first_order_is_the_factorial(self):
        # The simple exchange stops one swap short here, at a local
        # optimum with a run at an edge midpoint; the Fedorov-type
        # exchanges reach the 2^2 factorial.
        for method in FEDOROV_FAMILY:
            design, info = optimal_design(GRID, 4, 1, "D", method)
            assert np.all(np.abs(design) == 1.0)
            assert len(np.unique(design, axis=0)) == 4
            assert info["score"] == pytest.approx(1.0)
            assert info["D_eff"] == pytest.approx(100.0)

    def test_i_and_v_agree_when_test_points_are_the_candidates(self):
        for method in EXCHANGE_METHODS:
            # V-optimality over the whole candidate set is I-optimality.
            _, info_i = optimal_design(GRID, 7, 2, "I", method)
            _, info_v = optimal_design(
                GRID, 7, 2, "V", method, test_points=GRID
            )
            _, info_default = optimal_design(GRID, 7, 2, "V", method)
            assert info_v["score"] == pytest.approx(info_i["score"])
            assert info_default["score"] == pytest.approx(info_i["score"])


class TestCriterionInputs:
    def test_t_needs_a_model_difference(self):
        for method in METHODS:
            with pytest.raises(ValueError, match="model_diff"):
                optimal_design(GRID, 5, 1, "T", method)

    def test_model_diff_as_values_at_the_candidates(self):
        values = _second_order_2d(GRID)
        for method in METHODS:
            by_function, info_f = optimal_design(
                GRID, 5, 1, "T", method, model_diff=_second_order_2d
            )
            by_values, info_v = optimal_design(
                GRID, 5, 1, "T", method, model_diff=values
            )
            np.testing.assert_array_equal(by_function, by_values)
            assert info_f["score"] == pytest.approx(info_v["score"])

    def test_wrong_shapes_are_rejected(self):
        with pytest.raises(ValueError, match="c_vector"):
            optimal_design(GRID, 5, 1, "C", c_vector=[1, 0])
        with pytest.raises(ValueError, match="test_points"):
            optimal_design(GRID, 5, 1, "V", test_points=[[0.0, 0.0, 0.0]])
        with pytest.raises(ValueError, match="model_diff"):
            optimal_design(GRID, 5, 1, "T", model_diff=np.ones(3))

    def test_c_vector_changes_the_design(self):
        _, slope_1 = optimal_design(
            GRID, 4, 1, "C", "fedorov", c_vector=[0, 1, 0]
        )
        design_2, _ = optimal_design(
            GRID, 4, 1, "C", "fedorov", c_vector=[0, 0, 1]
        )
        # the variance of the second slope needs runs at x2 = -1 and +1
        assert slope_1["score"] == pytest.approx(-1.0)
        assert np.all(np.abs(design_2[:, 1]) == 1.0)

    def test_unknown_criterion_and_method(self):
        with pytest.raises(ValueError, match="Unknown criterion"):
            optimal_design(GRID, 5, 1, "Z")
        with pytest.raises(ValueError, match="Unknown method"):
            optimal_design(GRID, 5, 1, "D", "bogus")

    def test_more_runs_than_candidates_needs_replicates(self):
        with pytest.raises(ValueError, match="replicates=True"):
            optimal_design(LINE, 6, 1, "D")
        design, _ = optimal_design(LINE, 6, 1, "D", replicates=True)
        assert design.shape == (6, 1)

    def test_regularized_search(self):
        # alpha > 0 (Mitchell, 1974) must still give a usable design.
        candidates = generate_candidate_set(n_factors=2, n_levels=4)
        for criterion, method in itertools.product(CRITERIA, METHODS):
            inputs = {"model_diff": _cubic_2d} if criterion == "T" else {}
            design, info = optimal_design(
                candidates, 8, 2, criterion, method, alpha=0.001, **inputs
            )
            where = f"{criterion}, {method}"
            assert design.shape == (8, 2), where
            assert np.isfinite(info["score"]), where
            if criterion not in {"C", "T"}:
                assert info["D_eff"] > 0, where


class TestCriterionDefinitions:
    def test_t_is_the_lack_of_fit_sum_of_squares(self):
        # Atkinson and Fedorov (1975): what a least-squares fit of the
        # model leaves of the rival model's responses.
        rng = np.random.default_rng(0)
        X = np.column_stack([np.ones(7), rng.normal(size=(7, 2))])
        d = rng.normal(size=7)
        beta = np.linalg.lstsq(X, d, rcond=None)[0]
        assert t_optimality(X, d) == pytest.approx(np.sum((d - X @ beta) ** 2))
        # nothing to discriminate when the rival lies in the model
        assert t_optimality(X, X @ [1.0, -2.0, 0.5]) == pytest.approx(0.0)

    def test_t_equivalence_theorem_example(self):
        # Dette and Titoff (2009), Example 2.3: weights (1/6, 1/3, 1/3,
        # 1/6) on (-1, -1/2, 1/2, 1) give 1/16 per run, and the best
        # fitting line is 1 + 1.75 x.
        x = np.array([-1, -0.5, -0.5, 0.5, 0.5, 1.0])
        X = np.column_stack([np.ones(6), x])
        d = 1 + x + x**3
        assert t_optimality(X, d) / 6 == pytest.approx(1 / 16)
        beta = np.linalg.lstsq(X, d, rcond=None)[0]
        np.testing.assert_allclose(beta, [1.0, 1.75])

    def test_s_follows_shin_and_xiu(self):
        rng = np.random.default_rng(1)
        X = rng.normal(size=(12, 4))
        M = X.T @ X / 12
        expected = np.sqrt(np.linalg.det(X.T @ X)) / np.prod(
            np.linalg.norm(X, axis=0)
        )
        assert s_optimality(M) == pytest.approx(expected)
        assert 0 < s_optimality(M) < 1
        # invariant to the scale of the columns
        scale = np.diag([1.0, 10.0, 0.1, 3.0])
        assert s_optimality(scale @ M @ scale) == pytest.approx(expected)
        # 1 for orthogonal columns, 0 for dependent ones
        Q = np.linalg.qr(X)[0]
        assert s_optimality(Q.T @ Q) == pytest.approx(1.0)
        X[:, 3] = X[:, 0] + X[:, 1]
        assert s_optimality(X.T @ X / 12) == pytest.approx(0.0, abs=1e-6)


def test_random_candidate_set_is_reproducible():
    a = generate_candidate_set(
        2, n_levels=4, grid_type="uniform_random", seed=9
    )
    b = generate_candidate_set(
        2, n_levels=4, grid_type="uniform_random", seed=9
    )
    c = generate_candidate_set(
        2, n_levels=4, grid_type="uniform_random", seed=10
    )
    np.testing.assert_array_equal(a, b)
    assert not np.array_equal(a, c)
    assert a.shape == (16, 2)
