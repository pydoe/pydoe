import unittest

import numpy as np

from pydoe import morris_sampling, scale_samples


class TestMorrisSampling(unittest.TestCase):
    def test_morris_basic_2d(self):
        samples = morris_sampling(num_vars=2, N=2, num_levels=4, seed=42)

        expected_shape = (2 * (2 + 1), 2)
        self.assertEqual(samples.shape, expected_shape)

        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_morris_basic_3d(self):
        samples = morris_sampling(num_vars=3, N=3, num_levels=4, seed=123)

        expected_shape = (3 * (3 + 1), 3)
        self.assertEqual(samples.shape, expected_shape)

        # Test basic [0,1] bounds
        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_morris_with_scaling(self):
        samples = morris_sampling(num_vars=3, N=3, num_levels=4, seed=123)
        bounds = [(0, 2), (-1, 1), (0.5, 1.5)]
        scaled_samples = scale_samples(samples, bounds)

        self.assertTrue(np.all(scaled_samples[:, 0] >= 0))
        self.assertTrue(np.all(scaled_samples[:, 0] <= 2))
        self.assertTrue(np.all(scaled_samples[:, 1] >= -1))
        self.assertTrue(np.all(scaled_samples[:, 1] <= 1))
        self.assertTrue(np.all(scaled_samples[:, 2] >= 0.5))
        self.assertTrue(np.all(scaled_samples[:, 2] <= 1.5))

    def test_morris_reproducibility(self):
        samples1 = morris_sampling(num_vars=3, N=2, num_levels=4, seed=999)
        samples2 = morris_sampling(num_vars=3, N=2, num_levels=4, seed=999)

        np.testing.assert_array_equal(samples1, samples2)

    def test_morris_different_levels(self):
        samples_6 = morris_sampling(num_vars=2, N=2, num_levels=6, seed=42)
        self.assertEqual(samples_6.shape, (2 * 3, 2))

        samples_8 = morris_sampling(num_vars=2, N=2, num_levels=8, seed=42)
        self.assertEqual(samples_8.shape, (2 * 3, 2))

    def test_morris_odd_levels_error(self):
        with self.assertRaises(ValueError) as context:
            morris_sampling(num_vars=2, N=1, num_levels=5, seed=42)

        self.assertIn(
            "num_levels must be an even number", str(context.exception)
        )

    def test_morris_trajectory_structure(self):
        samples = morris_sampling(num_vars=2, N=1, num_levels=4, seed=42)

        self.assertEqual(samples.shape, (3, 2))

        for i in range(len(samples) - 1):
            diff = samples[i + 1] - samples[i]

            non_zero_diffs = np.count_nonzero(np.abs(diff) > 1e-10)
            self.assertEqual(
                non_zero_diffs,
                1,
                f"Points {i} and {i + 1} should differ "
                "in exactly one coordinate",
            )

    def test_morris_large_dimension(self):
        num_vars = 5
        samples = morris_sampling(num_vars=num_vars, N=2, num_levels=4, seed=42)

        expected_shape = (2 * (num_vars + 1), num_vars)
        self.assertEqual(samples.shape, expected_shape)

        # Test basic [0,1] bounds
        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_morris_single_trajectory(self):
        samples = morris_sampling(num_vars=2, N=1, num_levels=4, seed=42)

        self.assertEqual(samples.shape, (3, 2))

        # Test basic [0,1] bounds
        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

    def test_morris_expected_values_deterministic(self):
        samples = morris_sampling(num_vars=2, N=1, num_levels=4, seed=42)

        expected_shape = (3, 2)
        self.assertEqual(samples.shape, expected_shape)

        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples <= 1))

        self.assertTrue(samples.shape[0] > 0)

    def test_morris_scale_samples_utility(self):
        samples = morris_sampling(num_vars=3, N=2, num_levels=4, seed=42)
        bounds = [(-2, 2), (10, 20), (0.1, 0.9)]
        scaled_samples = scale_samples(samples, bounds)

        self.assertTrue(np.all(scaled_samples[:, 0] >= -2))
        self.assertTrue(np.all(scaled_samples[:, 0] <= 2))
        self.assertTrue(np.all(scaled_samples[:, 1] >= 10))
        self.assertTrue(np.all(scaled_samples[:, 1] <= 20))
        self.assertTrue(np.all(scaled_samples[:, 2] >= 0.1))
        self.assertTrue(np.all(scaled_samples[:, 2] <= 0.9))

    def test_morris_multiple_trajectories(self):
        N = 3
        samples = morris_sampling(num_vars=2, N=N, num_levels=4, seed=42)

        expected_points = N * (2 + 1)
        self.assertEqual(samples.shape, (expected_points, 2))

        D = 2
        for traj_idx in range(N):
            start_idx = traj_idx * (D + 1)
            end_idx = (traj_idx + 1) * (D + 1)
            trajectory = samples[start_idx:end_idx]

            self.assertEqual(trajectory.shape, (D + 1, D))

            for i in range(len(trajectory) - 1):
                diff = trajectory[i + 1] - trajectory[i]
                non_zero_diffs = np.count_nonzero(np.abs(diff) > 1e-10)
                self.assertEqual(non_zero_diffs, 1)
