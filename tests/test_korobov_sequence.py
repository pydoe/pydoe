import unittest

import numpy as np

from pydoe import korobov_sequence


class TestKorobovSequence(unittest.TestCase):
    def test_korobov_sequence(self):
        n, d = 5, 3
        a = 3
        # Generator vector: [1, 3, (3 * 3) % 5 = 4]
        expected = np.array([
            [(0 * 1) % 5, (0 * 3) % 5, (0 * 4) % 5],
            [(1 * 1) % 5, (1 * 3) % 5, (1 * 4) % 5],
            [(2 * 1) % 5, (2 * 3) % 5, (2 * 4) % 5],
            [(3 * 1) % 5, (3 * 3) % 5, (3 * 4) % 5],
            [(4 * 1) % 5, (4 * 3) % 5, (4 * 4) % 5],
        ])
        actual = korobov_sequence(n, d, generator_param=a)

        np.testing.assert_array_equal(actual, expected)


def test_korobov_sequence_seed_is_reproducible():
    a = korobov_sequence(31, 4, seed=5)
    b = korobov_sequence(31, 4, seed=5)
    np.testing.assert_array_equal(a, b)
    different = [korobov_sequence(31, 4, seed=s) for s in range(6)]
    assert any(not np.array_equal(a, d) for d in different)
    np.testing.assert_array_equal(
        korobov_sequence(11, 3, 2, seed=0), korobov_sequence(11, 3, 2)
    )
