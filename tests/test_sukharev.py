import unittest

import numpy as np

from pydoe.grid_designs import sukharev_grid


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


if __name__ == "__main__":
    unittest.main()
