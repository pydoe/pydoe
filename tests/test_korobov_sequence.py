import unittest
import numpy as np
from pyDOE import korobov_sequence


class TestKorobovSequence(unittest.TestCase):
    def test_korobov_sequence(self):
        n, d = 5, 3
        a = 3
        # Generator vector: [1, 3, (3 * 3) % 5 = 4]
        expected = np.array(
            [
                [(0 * 1) % 5, (0 * 3) % 5, (0 * 4) % 5],
                [(1 * 1) % 5, (1 * 3) % 5, (1 * 4) % 5],
                [(2 * 1) % 5, (2 * 3) % 5, (2 * 4) % 5],
                [(3 * 1) % 5, (3 * 3) % 5, (3 * 4) % 5],
                [(4 * 1) % 5, (4 * 3) % 5, (4 * 4) % 5],
            ]
        )
        actual = korobov_sequence(n, d, generator_param=a)

        np.testing.assert_array_equal(actual, expected)
