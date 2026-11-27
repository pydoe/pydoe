import unittest

import numpy as np

from pydoe import doehlert_shell_design, doehlert_simplex_design


def _sorted_rows(points):
    rounded = np.round(points, 9) + 0.0
    return rounded[np.lexsort(rounded.T[::-1])]


class TestDoehlertDesign(unittest.TestCase):
    def test_shell_design_with_2_factors(self):
        actual = doehlert_shell_design(2, num_center_points=1)

        # Center, then the six vertices of a regular hexagon.
        h = np.sqrt(3) / 2
        expected = np.array([
            [0.0, 0.0],
            [1.0, 0.0],
            [0.5, h],
            [-1.0, 0.0],
            [-0.5, -h],
            [0.5, -h],
            [-0.5, h],
        ])

        np.testing.assert_allclose(actual, expected, atol=1e-12)

    def test_simplex_design_with_2_factors(self):
        actual = doehlert_simplex_design(2)

        h = np.sqrt(3) / 2
        expected = np.array([
            [0.0, 0.0],  # center
            [1.0, 0.0],
            [0.5, h],
            [-1.0, 0.0],
            [-0.5, -h],
            [0.5, -h],
            [-0.5, h],
        ])

        np.testing.assert_allclose(actual, expected, atol=1e-12)
        self.assertEqual(actual.shape, (7, 2))

    def test_three_factors_match_doehlert_1970(self):
        # The 13-run design of Doehlert (1970): a cuboctahedron.
        a, b, c = np.sqrt(3) / 2, 1 / (2 * np.sqrt(3)), np.sqrt(2 / 3)
        half = np.array([
            [1.0, 0.0, 0.0],
            [0.5, a, 0.0],
            [0.5, b, c],
            [0.5, -a, 0.0],
            [0.5, -b, -c],
            [0.0, 2 * b, -c],
        ])
        expected = np.vstack([np.zeros((1, 3)), half, -half])
        actual = doehlert_simplex_design(3)
        np.testing.assert_allclose(
            _sorted_rows(actual), _sorted_rows(expected), atol=1e-9
        )

    def test_run_counts(self):
        for k in range(1, 8):
            self.assertEqual(
                doehlert_simplex_design(k).shape, (k * k + k + 1, k)
            )
            for n_center in (0, 1, 3):
                self.assertEqual(
                    doehlert_shell_design(k, n_center).shape,
                    (k * k + k + n_center, k),
                )

    def test_uniform_shell_geometry(self):
        for k in range(1, 8):
            design = doehlert_simplex_design(k)
            np.testing.assert_allclose(design[0], 0.0, atol=1e-12)
            shell = design[1:]
            # every point on the unit sphere
            np.testing.assert_allclose(
                np.linalg.norm(shell, axis=1), 1.0, atol=1e-12
            )
            # no duplicates, and nearest neighbors at distance 1
            # (with one factor the shell is just -1 and +1)
            dist = np.linalg.norm(shell[:, None, :] - shell[None, :, :], axis=2)
            np.fill_diagonal(dist, np.inf)
            nearest = 2.0 if k == 1 else 1.0
            np.testing.assert_allclose(dist.min(axis=1), nearest, atol=1e-12)
            # symmetric about the center
            np.testing.assert_allclose(
                _sorted_rows(shell), _sorted_rows(-shell), atol=1e-9
            )
            # every factor is varied
            self.assertTrue(np.all(np.ptp(shell, axis=0) > 0))

    def test_levels_per_factor(self):
        # Doehlert designs have 5 levels for the first factor, 7 for the
        # ones in between and 3 for the last.
        design = doehlert_simplex_design(4)
        levels = [len(np.unique(np.round(col, 9))) for col in design.T]
        self.assertEqual(levels, [5, 7, 7, 3])

    def test_shell_is_simplex_design_with_center_replicates(self):
        for k in range(1, 6):
            simplex = doehlert_simplex_design(k)
            shell = doehlert_shell_design(k, num_center_points=3)
            np.testing.assert_allclose(shell[:3], 0.0, atol=1e-12)
            np.testing.assert_allclose(shell[3:], simplex[1:], atol=1e-12)

    def test_quadratic_model_is_estimable(self):
        for k in range(2, 7):
            x = doehlert_shell_design(k)
            cols = [np.ones(len(x))] + [x[:, i] for i in range(k)]
            cols += [x[:, i] * x[:, j] for i in range(k) for j in range(i, k)]
            X = np.column_stack(cols)
            self.assertEqual(np.linalg.matrix_rank(X), X.shape[1])

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            doehlert_shell_design(0)
        with self.assertRaises(ValueError):
            doehlert_simplex_design(0)
        with self.assertRaises(ValueError):
            doehlert_shell_design(2, num_center_points=-1)
