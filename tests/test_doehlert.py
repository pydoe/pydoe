import unittest

import numpy as np

from pydoe import doehlert_shell_design, doehlert_simplex_design


class TestDoehlertDesign(unittest.TestCase):
    def test_shell_design_with_2_factors(self):
        actual = doehlert_shell_design(2, num_center_points=1)

        expected = np.array([
            [0.0, 0.0],  # center
            [np.sqrt(2) / 2, 0.0],  # shell 1, point 1
            [-np.sqrt(2) / 2, 0.0],  # shell 1, point 2
            [1.0, 0.0],  # shell 2, point 1
            [-0.5, np.sqrt(3) / 2],  # shell 2, point 2
            [-0.5, -np.sqrt(3) / 2],  # shell 2, point 3
        ])

        np.testing.assert_allclose(actual, expected, atol=1e-6)
        self.assertEqual(actual.shape[1], 2)

    def test_simplex_design_with_2_factors(self):
        actual = doehlert_simplex_design(2)

        expected = np.array([
            [0.0, 0.0],  # center
            [1.0, 0.0],
            [0.0, np.sqrt(3) / 2],
            [-1.0, 0.0],
            [0.0, -np.sqrt(3) / 2],
            [1.0, -np.sqrt(3) / 2],
            [-1.0, np.sqrt(3) / 2],
        ])

        np.testing.assert_allclose(actual, expected, atol=1e-6)

        self.assertEqual(actual.shape, (7, 2))
        self.assertEqual(actual.shape[1], 2)

        self.assertFalse(np.any(np.isnan(actual)))
        self.assertFalse(np.any(np.isinf(actual)))
