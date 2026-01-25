import unittest

import numpy as np

from pyDOE import cranley_patterson_shift


class TestCranleyPattersonShift(unittest.TestCase):
    def test_cranley_patterson_shift(self):
        points = np.array([[0.1, 0.2], [0.4, 0.8]])
        shifted = cranley_patterson_shift(points, seed=42)

        # Using fixed seed = 42, rng = np.random.default_rng(42)
        # Shift vector (approx): [0.77395605, 0.43887844]
        expected = (points + np.array([0.77395605, 0.43887844])) % 1

        np.testing.assert_allclose(shifted, expected, atol=1e-8)
