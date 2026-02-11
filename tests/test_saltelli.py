import unittest
import warnings

import numpy as np

from pydoe.doe_saltelli import saltelli_sampling
from pydoe.utils import scale_samples


class TestSaltelliSampling(unittest.TestCase):
    def test_saltelli_basic_2d(self):
        samples = saltelli_sampling(num_vars=2, N=4, seed=42)

        expected_shape = (4 * (2 * 2 + 2), 2)
        self.assertEqual(samples.shape, expected_shape)

        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_saltelli_basic_3d(self):
        samples = saltelli_sampling(num_vars=3, N=4, seed=123)

        expected_shape = (4 * (2 * 3 + 2), 3)
        self.assertEqual(samples.shape, expected_shape)

        # Test basic [0,1] bounds
        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_saltelli_with_scaling(self):
        samples = saltelli_sampling(num_vars=3, N=4, seed=123)
        bounds = [(0, 2), (-1, 1), (0.5, 1.5)]
        scaled_samples = scale_samples(samples, bounds)

        self.assertTrue(np.all(scaled_samples[:, 0] >= 0))
        self.assertTrue(np.all(scaled_samples[:, 0] <= 2))
        self.assertTrue(np.all(scaled_samples[:, 1] >= -1))
        self.assertTrue(np.all(scaled_samples[:, 1] <= 1))
        self.assertTrue(np.all(scaled_samples[:, 2] >= 0.5))
        self.assertTrue(np.all(scaled_samples[:, 2] <= 1.5))

    def test_saltelli_no_second_order(self):
        samples = saltelli_sampling(
            num_vars=3, N=4, calc_second_order=False, seed=42
        )

        expected_shape = (4 * (3 + 2), 3)
        self.assertEqual(samples.shape, expected_shape)

        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_saltelli_reproducibility(self):
        samples1 = saltelli_sampling(num_vars=3, N=4, seed=999)
        samples2 = saltelli_sampling(num_vars=3, N=4, seed=999)

        np.testing.assert_array_equal(samples1, samples2)

    def test_saltelli_scrambling(self):
        samples_scrambled = saltelli_sampling(
            num_vars=2, N=4, scramble=True, seed=42
        )

        samples_unscrambled = saltelli_sampling(
            num_vars=2, N=4, scramble=False, seed=42
        )

        self.assertEqual(samples_scrambled.shape, samples_unscrambled.shape)

        self.assertFalse(np.array_equal(samples_scrambled, samples_unscrambled))

    def test_saltelli_skip_values(self):
        samples1 = saltelli_sampling(num_vars=2, N=4, skip_values=8, seed=42)
        samples2 = saltelli_sampling(num_vars=2, N=4, skip_values=16, seed=42)

        self.assertEqual(samples1.shape, samples2.shape)

        self.assertFalse(np.array_equal(samples1, samples2))

    def test_saltelli_power_of_2_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            saltelli_sampling(num_vars=2, N=5, seed=42)

            self.assertTrue(len(w) >= 1)
            self.assertTrue(
                any("not a power of 2" in str(warning.message) for warning in w)
            )

    def test_saltelli_scale_samples_utility(self):
        samples = saltelli_sampling(num_vars=3, N=4, seed=42)
        bounds = [(-2, 2), (10, 20), (0.1, 0.9)]
        scaled_samples = scale_samples(samples, bounds)

        self.assertTrue(np.all(scaled_samples[:, 0] >= -2))
        self.assertTrue(np.all(scaled_samples[:, 0] <= 2))
        self.assertTrue(np.all(scaled_samples[:, 1] >= 10))
        self.assertTrue(np.all(scaled_samples[:, 1] <= 20))
        self.assertTrue(np.all(scaled_samples[:, 2] >= 0.1))
        self.assertTrue(np.all(scaled_samples[:, 2] <= 0.9))

    def test_saltelli_single_variable(self):
        samples = saltelli_sampling(num_vars=1, N=4, seed=42)

        expected_shape = (4 * (2 * 1 + 2), 1)
        self.assertEqual(samples.shape, expected_shape)

        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_saltelli_large_dimension(self):
        num_vars = 5
        samples = saltelli_sampling(num_vars=num_vars, N=4, seed=42)

        expected_shape = (4 * (2 * num_vars + 2), num_vars)
        self.assertEqual(samples.shape, expected_shape)

        # Test basic [0,1] bounds
        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_saltelli_matrix_structure(self):
        N = 2
        samples = saltelli_sampling(
            num_vars=2, N=N, calc_second_order=False, seed=42
        )

        expected_shape = (N * (2 + 2), 2)
        self.assertEqual(samples.shape, expected_shape)

        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_saltelli_deterministic_with_seed(self):
        samples1 = saltelli_sampling(num_vars=2, N=4, seed=123, scramble=False)
        samples2 = saltelli_sampling(num_vars=2, N=4, seed=123, scramble=False)

        np.testing.assert_array_equal(samples1, samples2)

    def test_saltelli_different_n_values(self):
        for N in [2, 4, 8, 16]:
            samples = saltelli_sampling(num_vars=2, N=N, seed=42)
            expected_shape = (N * (2 * 2 + 2), 2)
            self.assertEqual(samples.shape, expected_shape)

    def test_saltelli_sobol_properties(self):
        samples = saltelli_sampling(num_vars=2, N=8, scramble=False, seed=42)

        lower_half_x = np.sum(samples[:, 0] < 0.5)
        upper_half_x = np.sum(samples[:, 0] >= 0.5)
        lower_half_y = np.sum(samples[:, 1] < 0.5)
        upper_half_y = np.sum(samples[:, 1] >= 0.5)

        self.assertGreater(lower_half_x, 0)
        self.assertGreater(upper_half_x, 0)
        self.assertGreater(lower_half_y, 0)
        self.assertGreater(upper_half_y, 0)

    def test_saltelli_edge_case_scaling(self):
        samples = saltelli_sampling(num_vars=2, N=4, seed=42)
        bounds = [(0.5, 0.5001), (0.9999, 1.0)]
        scaled_samples = scale_samples(samples, bounds)

        self.assertTrue(np.all(scaled_samples[:, 0] >= 0.5))
        self.assertTrue(np.all(scaled_samples[:, 0] <= 0.5001))
        self.assertTrue(np.all(scaled_samples[:, 1] >= 0.9999))
        self.assertTrue(np.all(scaled_samples[:, 1] <= 1.0))

    def test_saltelli_negative_bounds_scaling(self):
        samples = saltelli_sampling(num_vars=2, N=4, seed=42)
        bounds = [(-10, -5), (-1, -0.5)]
        scaled_samples = scale_samples(samples, bounds)

        self.assertTrue(np.all(scaled_samples[:, 0] >= -10))
        self.assertTrue(np.all(scaled_samples[:, 0] <= -5))
        self.assertTrue(np.all(scaled_samples[:, 1] >= -1))
        self.assertTrue(np.all(scaled_samples[:, 1] <= -0.5))

    def test_saltelli_second_order_comparison(self):
        N = 4

        samples_first = saltelli_sampling(
            num_vars=3, N=N, calc_second_order=False, seed=42
        )

        samples_second = saltelli_sampling(
            num_vars=3, N=N, calc_second_order=True, seed=42
        )

        self.assertGreater(samples_second.shape[0], samples_first.shape[0])

        expected_first = (N * (3 + 2), 3)
        expected_second = (N * (2 * 3 + 2), 3)

        self.assertEqual(samples_first.shape, expected_first)
        self.assertEqual(samples_second.shape, expected_second)
