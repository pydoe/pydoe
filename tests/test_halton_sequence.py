import unittest

import numpy as np

from pyDOE import halton_sequence


class TestHaltonSequence(unittest.TestCase):
    def test_halton_sequence(self):
        seq = halton_sequence(num_points=5, dimension=2, skip=0)

        expected = np.array([
            [0.0, 0.0],
            [0.5, 1 / 3],
            [0.25, 2 / 3],
            [0.75, 1 / 9],
            [0.125, 4 / 9],
        ])

        np.testing.assert_allclose(seq, expected, atol=1e-8)
