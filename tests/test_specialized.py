import unittest

import numpy as np

from pydoe import definitive_screening_design, supersaturated_design


class TestDefinitiveScreeningDesign(unittest.TestCase):
    def test_shape(self):
        for k in [4, 6, 8, 12]:
            design = definitive_screening_design(k)
            self.assertEqual(design.shape, (2 * k + 1, k))

    def test_levels_are_three(self):
        design = definitive_screening_design(4)
        self.assertEqual(set(np.unique(design).tolist()), {-1.0, 0.0, 1.0})

    def test_first_row_is_center(self):
        design = definitive_screening_design(6)
        np.testing.assert_array_equal(design[0], np.zeros(6))

    def test_main_effects_orthogonal(self):
        for k in [4, 6, 8]:
            design = definitive_screening_design(k)
            gram = design.T @ design
            expected = 2 * (k - 1) * np.eye(k)
            np.testing.assert_allclose(gram, expected)

    def test_foldover_structure(self):
        k = 4
        design = definitive_screening_design(k)
        np.testing.assert_allclose(design[1 : k + 1], -design[k + 1 :])

    def test_raises_k_minus_one_not_odd_prime(self):
        # k - 1 = 3 is odd prime -> ok; k - 1 = 4 is not prime
        with self.assertRaises(ValueError):
            definitive_screening_design(5)
        with self.assertRaises(ValueError):
            definitive_screening_design(7)

    def test_raises_k_too_small(self):
        with self.assertRaises(ValueError):
            definitive_screening_design(2)


class TestSupersaturatedDesign(unittest.TestCase):
    def test_shape(self):
        design = supersaturated_design(8, 4, iterations=50, seed=0)
        self.assertEqual(design.shape, (4, 8))

    def test_levels_are_pm_one(self):
        design = supersaturated_design(8, 4, iterations=50, seed=0)
        self.assertEqual(set(np.unique(design).tolist()), {-1.0, 1.0})

    def test_reproducible_with_seed(self):
        d1 = supersaturated_design(8, 4, iterations=50, seed=42)
        d2 = supersaturated_design(8, 4, iterations=50, seed=42)
        np.testing.assert_array_equal(d1, d2)

    def test_raises_n_runs_too_small(self):
        with self.assertRaises(ValueError):
            supersaturated_design(8, 1)

    def test_raises_not_supersaturated(self):
        with self.assertRaises(ValueError):
            supersaturated_design(4, 4)
        with self.assertRaises(ValueError):
            supersaturated_design(4, 6)
