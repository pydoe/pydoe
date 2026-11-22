import unittest

import numpy as np

from pydoe import ccdesign, fracfact


class TestComposite(unittest.TestCase):
    def test_composite1(self):
        expected = [
            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0],
            [1.0, -1.0, -1.0],
            [1.0, -1.0, 1.0],
            [1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [-1.82574186, 0.0, 0.0],
            [1.82574186, 0.0, 0.0],
            [0.0, -1.82574186, 0.0],
            [0.0, 1.82574186, 0.0],
            [0.0, 0.0, -1.82574186],
            [0.0, 0.0, 1.82574186],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
        actual = ccdesign(3)
        np.testing.assert_allclose(actual, expected)

    def test_composite_fractional_cube(self):
        gen = "a b c d abcd"  # 2^(5-1), resolution V: 16 runs
        H = ccdesign(5, center=(4, 4), alpha="r", generators=gen)
        self.assertEqual(H.shape, (16 + 4 + 10 + 4, 5))
        np.testing.assert_array_equal(H[:16], fracfact(gen))
        self.assertAlmostEqual(np.abs(H).max(), 2.0)

    def test_composite_rotatable_alpha_matches_textbooks(self):
        # Box and Draper (2007), p. 491; Montgomery (2012), p. 511.
        cases = [
            (5, "a b c d abcd", 2.0),
            (6, "a b c d e abcde", 2.3784),
            (7, "a b c d e f abcdef", 2.8284),
            (8, "a b c d e f abcd abef", 2.8284),
        ]
        for n, gen, expected in cases:
            with self.subTest(n=n):
                H = ccdesign(n, center=(0, 0), alpha="r", generators=gen)
                self.assertAlmostEqual(np.abs(H).max(), expected, places=4)

    def test_composite_fractional_cube_faced_and_inscribed(self):
        gen = "a b c d abcd"
        faced = ccdesign(5, center=(0, 0), face="ccf", generators=gen)
        self.assertEqual(np.abs(faced).max(), 1)
        inscribed = ccdesign(
            5, center=(0, 0), alpha="r", face="cci", generators=gen
        )
        np.testing.assert_allclose(np.abs(inscribed[:16]), 1 / 2.0)
        np.testing.assert_allclose(np.abs(inscribed[16:]).max(), 1)

    def test_composite_default_is_full_cube(self):
        np.testing.assert_array_equal(ccdesign(4, generators=None), ccdesign(4))

    def test_composite_rejects_generators_for_other_n(self):
        with self.assertRaises(ValueError):
            ccdesign(5, generators="a b c ab")

    def test_composite_rejects_non_string_generators(self):
        with self.assertRaises(TypeError):
            ccdesign(5, generators=["a", "b", "c", "d", "abcd"])
