import unittest

import numpy as np

from pyDOE import sobol_sequence


class TestSobolSequence(unittest.TestCase):
    def test_sobol_sequence(self):
        # Using unscrambled Sobol', first 4 points in 2D
        seq = sobol_sequence(
            n=4, d=2, scramble=False, seed=None, use_pow_of_2=True
        )

        expected = np.array([
            [0.0, 0.0],
            [0.5, 0.5],
            [0.75, 0.25],
            [0.25, 0.75],
        ])

        np.testing.assert_allclose(seq, expected, atol=1e-8)
