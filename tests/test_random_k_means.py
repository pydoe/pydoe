import unittest

import numpy as np

from pyDOE import random_k_means


class TestRandomKMeans(unittest.TestCase):
    def test_random_k_means_basic(self):
        """Test basic functionality with reproducible random state."""
        num_points = 5
        dimension = 2
        result = random_k_means(
            num_points=num_points, dimension=dimension, seed=42
        )

        # Check output shape
        self.assertEqual(result.shape, (num_points, dimension))

        # Check that all points are within [0, 1]
        self.assertTrue(np.all((0.0 <= result) & (result <= 1.0)))

        # Check reproducibility
        result2 = random_k_means(
            num_points=num_points, dimension=dimension, seed=42
        )
        np.testing.assert_allclose(result, result2)

    def test_random_k_means_reproducible_output(self):
        """Test specific expected output for known random state."""
        expected = np.array([
            [0.68138275, 0.30072643],
            [0.85733, 0.71384485],
            [0.23305099, 0.77871437],
            [0.68103389, 0.82427319],
            [0.26336031, 0.26282146],
        ])
        actual = random_k_means(
            num_points=5, dimension=2, num_steps=100, seed=42
        )
        np.testing.assert_allclose(actual, expected, rtol=1e-6)

    def test_random_k_means_with_initial_points(self):
        """Test with custom initial points."""
        initial_points = np.array([[0.1, 0.2], [0.3, 0.4], [0.7, 0.8]])

        result = random_k_means(
            num_points=3,
            dimension=2,
            initial_points=initial_points,
            num_steps=10,
            seed=42,
        )

        # Check output shape
        self.assertEqual(result.shape, (3, 2))

        # Check that all points are within [0, 1]
        self.assertTrue(np.all((0.0 <= result) & (result <= 1.0)))

    def test_random_k_means_different_dimensions(self):
        """Test with different dimensionalities."""
        for dim in [1, 3, 5]:
            result = random_k_means(num_points=4, dimension=dim, seed=42)
            self.assertEqual(result.shape, (4, dim))
            self.assertTrue(np.all((0.0 <= result) & (result <= 1.0)))

    def test_random_k_means_num_steps(self):
        """Test with different number of steps."""
        result1 = random_k_means(
            num_points=3, dimension=2, num_steps=10, seed=42
        )

        result2 = random_k_means(
            num_points=3, dimension=2, num_steps=1000, seed=42
        )

        # Both should be valid
        self.assertEqual(result1.shape, (3, 2))
        self.assertEqual(result2.shape, (3, 2))
        self.assertTrue(np.all((0.0 <= result1) & (result1 <= 1.0)))
        self.assertTrue(np.all((0.0 <= result2) & (result2 <= 1.0)))

    def test_random_k_means_callback(self):
        """Test callback functionality."""
        callback_calls = []

        def test_callback(centers):
            callback_calls.append(centers.copy())

        random_k_means(
            num_points=2,
            dimension=2,
            num_steps=5,
            callback=test_callback,
            seed=42,
        )

        # Should have been called 5 times (once per step)
        self.assertEqual(len(callback_calls), 5)

        # Each call should have the right shape
        for call in callback_calls:
            self.assertEqual(call.shape, (2, 2))

    def test_random_k_means_invalid_initial_points_shape(self):
        """Test error handling for wrong initial points shape."""
        with self.assertRaises(ValueError):
            random_k_means(
                num_points=3,
                dimension=2,
                initial_points=np.array([[0.1, 0.2]]),  # Wrong shape
            )

    def test_random_k_means_invalid_initial_points_range(self):
        """Test error handling for initial points outside [0,1]."""
        with self.assertRaises(ValueError):
            random_k_means(
                num_points=2,
                dimension=2,
                initial_points=np.array([
                    [0.1, 0.2],
                    [1.5, 0.8],
                ]),  # Outside range
            )

    def test_random_k_means_single_point(self):
        """Test with a single cluster center."""
        result = random_k_means(num_points=1, dimension=3, seed=42)

        self.assertEqual(result.shape, (1, 3))
        self.assertTrue(np.all((0.0 <= result) & (result <= 1.0)))

    def test_random_k_means_large_num_points(self):
        """Test with larger number of points."""
        result = random_k_means(
            num_points=50, dimension=2, num_steps=100, seed=42
        )

        self.assertEqual(result.shape, (50, 2))
        self.assertTrue(np.all((0.0 <= result) & (result <= 1.0)))

    def test_random_k_means_default_num_steps(self):
        """Test that default num_steps is correctly set."""
        # Default should be 100 * num_points
        num_points = 3
        callback_calls = []

        def test_callback(centers):
            callback_calls.append(centers.copy())

        random_k_means(
            num_points=num_points, dimension=2, callback=test_callback, seed=42
        )

        # Should have been called 300 times (100 * 3)
        self.assertEqual(len(callback_calls), 100 * num_points)

    def test_random_k_means_deprecated_random_state(self):
        num_points = 5
        dimension = 2

        with self.assertWarns(DeprecationWarning):
            result = random_k_means(
                num_points=num_points, dimension=dimension, random_state=42
            )

        self.assertEqual(result.shape, (num_points, dimension))
        self.assertTrue(np.all((0.0 <= result) & (result <= 1.0)))

        with self.assertWarns(DeprecationWarning):
            result_random_state = random_k_means(
                num_points=num_points, dimension=dimension, random_state=42
            )

        result_seed = random_k_means(
            num_points=num_points, dimension=dimension, seed=42
        )

        np.testing.assert_allclose(result_random_state, result_seed)
