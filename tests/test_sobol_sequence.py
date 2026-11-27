import unittest

import numpy as np

from pydoe import sobol_sequence


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


def test_sobol_skip_with_power_of_two_rounding():
    # skip > 0 with the default use_pow_of_2=True raised a scipy error
    # unless skip + n happened to be a power of 2.
    full = sobol_sequence(16, 3)
    for skip in (1, 3, 5, 8):
        skipped = sobol_sequence(8, 3, skip=skip)
        np.testing.assert_allclose(skipped, full[skip : skip + 8])
    # n is still rounded up to a power of 2
    assert sobol_sequence(5, 2, skip=3).shape == (8, 2)
