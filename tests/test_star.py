import unittest

import numpy as np

from pydoe import star


class TestStar(unittest.TestCase):
    def test_star1(self):
        expected = (
            np.array([
                [-1.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, -1.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, -1.0],
                [0.0, 0.0, 1.0],
            ]),
            1,
        )
        actual = star(3)
        np.testing.assert_allclose(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])

    def test_star_default_cube_is_full_factorial(self):
        # Without n_cube, alpha counts the 2**n runs of the full factorial.
        self.assertAlmostEqual(star(5, alpha="rotatable")[1], 32**0.25)
        a = star(3, alpha="orthogonal", center=(4, 4))[1]
        self.assertAlmostEqual(a, (3 * (1 + 4 / 6) / (1 + 4 / 8)) ** 0.5)

    def test_star_rotatable_with_fractional_cube(self):
        # Box and Draper (2007), p. 491; Montgomery (2012), p. 511.
        for n, n_cube, expected in [
            (5, 16, 2.0),
            (6, 32, 2.3784),
            (7, 64, 2.8284),
        ]:
            with self.subTest(n=n):
                H, a = star(n, alpha="rotatable", n_cube=n_cube)
                self.assertAlmostEqual(a, expected, places=4)
                np.testing.assert_allclose(np.abs(H).max(), a)

    def test_star_orthogonal_with_fractional_cube(self):
        a = star(5, alpha="orthogonal", center=(4, 4), n_cube=16)[1]
        self.assertAlmostEqual(a, (5 * (1 + 4 / 10) / (1 + 4 / 16)) ** 0.5)

    def test_star_faced_ignores_n_cube(self):
        self.assertEqual(star(4, n_cube=8)[1], 1)

    def test_star_rejects_invalid_n_cube(self):
        for n_cube in (0, -8, 2.5):
            with self.subTest(n_cube=n_cube), self.assertRaises(ValueError):
                star(4, alpha="rotatable", n_cube=n_cube)
