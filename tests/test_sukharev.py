import unittest

import numpy as np

from pydoe import sukharev_grid


class TestSukharevGrid(unittest.TestCase):
    def test_1d_case(self):
        actual = sukharev_grid(4, 1)
        expected = np.array([[0.125], [0.375], [0.625], [0.875]])
        np.testing.assert_allclose(actual, expected, atol=1e-12)
        self.assertEqual(actual.shape, (4, 1))

    def test_2d_case(self):
        actual = sukharev_grid(4, 2)
        expected = np.array([
            [0.25, 0.25],
            [0.25, 0.75],
            [0.75, 0.25],
            [0.75, 0.75],
        ])
        np.testing.assert_allclose(actual, expected, atol=1e-12)
        self.assertEqual(actual.shape, (4, 2))

    def test_3d_case(self):
        actual = sukharev_grid(8, 3)
        self.assertEqual(actual.shape, (8, 3))
        # All points should be strictly between 0 and 1
        self.assertTrue(np.all(actual > 0))
        self.assertTrue(np.all(actual < 1))

    def test_invalid_num_points(self):
        with self.assertRaises(ValueError):
            sukharev_grid(3, 2)  # 3 ** (1/2) is not integer

    def test_perfect_powers_with_inexact_float_root(self):
        # 125 ** (1 / 3) evaluates to 4.999..., which int() truncated to 4.
        for per_axis, dimension in [(5, 3), (10, 3), (6, 3), (7, 5), (3, 13)]:
            num_points = per_axis**dimension
            actual = sukharev_grid(num_points, dimension)
            self.assertEqual(actual.shape, (num_points, dimension))
            expected_axis = (np.arange(per_axis) + 0.5) / per_axis
            np.testing.assert_allclose(
                np.unique(actual[:, 0]), expected_axis, atol=1e-12
            )

    def test_near_perfect_powers_are_rejected(self):
        for num_points, dimension in [(124, 3), (126, 3), (999, 3)]:
            with self.assertRaises(ValueError):
                sukharev_grid(num_points, dimension)


if __name__ == "__main__":
    unittest.main()
