import unittest

import numpy as np

from pydoe import ff2n, scale_samples, var_regression_matrix
from pydoe.utils import build_regression_matrix


class TestBuildRegressionMatrix(unittest.TestCase):
    def test_interaction_model(self):
        H = np.array([[-1.0, -1.0], [1.0, -1.0], [-1.0, 1.0], [1.0, 1.0]])
        actual = build_regression_matrix(H, "1 x1 x2 x1*x2")
        expected = np.column_stack([
            np.ones(4),
            H[:, 0],
            H[:, 1],
            H[:, 0] * H[:, 1],
        ])
        np.testing.assert_allclose(actual, expected)

    def test_powers_and_coefficients(self):
        H = np.array([[2.0, 3.0], [0.5, -1.0]])
        actual = build_regression_matrix(H, "x1^2 x2**3 2*x1*x2 x1*x1")
        expected = np.column_stack([
            H[:, 0] ** 2,
            H[:, 1] ** 3,
            2 * H[:, 0] * H[:, 1],
            H[:, 0] ** 2,
        ])
        np.testing.assert_allclose(actual, expected)

    def test_single_run_as_1d_array(self):
        actual = build_regression_matrix(np.array([2.0, 3.0]), "1 x1 x2")
        np.testing.assert_allclose(actual, [[1.0, 2.0, 3.0]])

    def test_more_than_nine_variables(self):
        H = np.arange(1.0, 13.0).reshape(1, 12)
        actual = build_regression_matrix(H, "x1 x12 x1*x10")
        np.testing.assert_allclose(actual, [[1.0, 12.0, 10.0]])

    def test_build_mask(self):
        H = np.array([[2.0, 3.0]])
        actual = build_regression_matrix(
            H, "1 x1 x2", build=[True, False, True]
        )
        np.testing.assert_allclose(actual, [[1.0, 3.0]])

    def test_build_mask_wrong_length(self):
        with self.assertRaises(ValueError):
            build_regression_matrix(np.eye(2), "1 x1 x2", build=[True])

    def test_unknown_variable(self):
        with self.assertRaises(ValueError):
            build_regression_matrix(np.eye(2), "1 x3")

    def test_malformed_monomial(self):
        with self.assertRaises(ValueError):
            build_regression_matrix(np.eye(2), "1 x1+x2")


class TestVarRegressionMatrix(unittest.TestCase):
    def test_two_level_factorial(self):
        # For an orthogonal 2^2 design, H^T H = 4 I, so the variance at x
        # is sigma^2 * (1 + x1^2 + x2^2) / 4.
        model = "1 x1 x2"
        H = build_regression_matrix(ff2n(2), model)
        self.assertAlmostEqual(
            var_regression_matrix(H, [0.0, 0.0], model), 0.25
        )
        self.assertAlmostEqual(
            var_regression_matrix(H, [1.0, 1.0], model), 0.75
        )
        self.assertAlmostEqual(
            var_regression_matrix(H, np.array([0.5, -1.0]), model),
            (1 + 0.25 + 1) / 4,
        )

    def test_sigma_scales_variance(self):
        model = "1 x1 x2"
        H = build_regression_matrix(ff2n(2), model)
        self.assertAlmostEqual(
            var_regression_matrix(H, [1.0, 1.0], model, sigma=2), 3.0
        )

    def test_matches_explicit_formula(self):
        rng = np.random.default_rng(0)
        design = rng.uniform(-1, 1, size=(12, 3))
        model = "1 x1 x2 x3 x1*x2 x3^2"
        H = build_regression_matrix(design, model)
        x = np.array([0.3, -0.2, 0.9])
        f = np.array([1, x[0], x[1], x[2], x[0] * x[1], x[2] ** 2])
        expected = f @ np.linalg.inv(H.T @ H) @ f
        self.assertAlmostEqual(var_regression_matrix(H, x, model), expected)

    def test_rank_deficient_design(self):
        # Three runs cannot support a four-term model.
        model = "1 x1 x2 x1*x2"
        H = build_regression_matrix(ff2n(2)[:3], model)
        with self.assertRaises(ValueError):
            var_regression_matrix(H, [0.0, 0.0], model)

    def test_model_does_not_match_matrix(self):
        H = build_regression_matrix(ff2n(2), "1 x1 x2")
        with self.assertRaises(ValueError):
            var_regression_matrix(H, [0.0, 0.0], "1 x1")


def test_scale_samples_integer_input():
    # Integer samples kept an integer dtype, so scaled values were
    # truncated: 0.5 became 0 and 1.5 became 1.
    scaled = scale_samples(np.array([[0, 1], [1, 0]]), [(0.5, 1.5), (0, 10)])
    np.testing.assert_allclose(scaled, [[0.5, 10.0], [1.5, 0.0]])
    assert scaled.dtype == np.float64
