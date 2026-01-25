import unittest

import numpy as np

from pyDOE import random_uniform


class TestRandomUniform(unittest.TestCase):
    def test_random_uniform_basic(self):
        """Test basic functionality of random_uniform."""
        num_points = 10
        dimension = 3

        # Set random seed for reproducibility
        result = random_uniform(num_points, dimension, seed=42)

        # Check output shape
        self.assertEqual(result.shape, (num_points, dimension))

        # Check that all values are in [0, 1)
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_reproducible(self):
        """Test reproducibility with same random seed."""
        expected = np.array([
            [0.77395605, 0.43887844, 0.85859792],
            [0.69736803, 0.09417735, 0.97562235],
            [0.7611397, 0.78606431, 0.12811363],
            [0.45038594, 0.37079802, 0.92676499],
            [0.64386512, 0.82276161, 0.4434142],
        ])

        actual = random_uniform(5, 3, seed=42)

        np.testing.assert_allclose(actual, expected, rtol=1e-6)

    def test_random_uniform_single_point(self):
        """Test with single point."""
        result = random_uniform(1, 2, seed=42)

        self.assertEqual(result.shape, (1, 2))
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_single_dimension(self):
        """Test with single dimension."""
        result = random_uniform(5, 1, seed=42)

        self.assertEqual(result.shape, (5, 1))
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_large_array(self):
        """Test with larger arrays."""
        result = random_uniform(100, 10, seed=42)

        self.assertEqual(result.shape, (100, 10))
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_zero_points(self):
        """Test with zero points."""
        result = random_uniform(0, 3, seed=42)

        self.assertEqual(result.shape, (0, 3))

    def test_random_uniform_zero_dimension(self):
        """Test with zero dimensions."""
        result = random_uniform(5, 0, seed=42)

        self.assertEqual(result.shape, (5, 0))

    def test_random_uniform_distribution_properties(self):
        """Test statistical properties of the uniform distribution."""
        result = random_uniform(10000, 1, seed=42)

        # For uniform distribution on [0, 1):
        # - Mean should be approximately 0.5
        # - Standard deviation should be approximately 1/sqrt(12) ≈ 0.289
        mean = np.mean(result)
        std = np.std(result)

        self.assertAlmostEqual(mean, 0.5, delta=0.02)  # Allow some tolerance
        self.assertAlmostEqual(std, 1 / np.sqrt(12), delta=0.02)

    def test_random_uniform_different_dimensions(self):
        """Test with various dimensions."""
        for dim in [1, 2, 5, 10, 20]:
            result = random_uniform(10, dim, seed=42)
            self.assertEqual(result.shape, (10, dim))
            self.assertTrue(np.all(result >= 0.0))
            self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_different_num_points(self):
        """Test with various numbers of points."""
        for num_points in [1, 10, 50, 100]:
            result = random_uniform(num_points, 3, seed=42)
            self.assertEqual(result.shape, (num_points, 3))
            self.assertTrue(np.all(result >= 0.0))
            self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_independence(self):
        """Test that different calls produce different results (not seeded)."""
        # Don't set seed for this test
        result1 = random_uniform(10, 3)
        result2 = random_uniform(10, 3)

        # Results should be different (very unlikely to be identical)
        self.assertFalse(np.allclose(result1, result2))

    def test_random_uniform_dtype(self):
        """Test that output has correct data type."""
        np.random.seed(42)
        result = random_uniform(5, 3)

        # Should be float type
        self.assertTrue(np.issubdtype(result.dtype, np.floating))

    def test_random_uniform_bounds_strict(self):
        """Test that values are strictly less than 1.0."""
        np.random.seed(42)
        result = random_uniform(1000, 5)

        # All values should be < 1.0 (not <= 1.0)
        self.assertTrue(np.all(result < 1.0))
        # All values should be >= 0.0
        self.assertTrue(np.all(result >= 0.0))
