import unittest

import numpy as np

from pyDOE import rank1_lattice


class TestRank1Lattice(unittest.TestCase):
    def test_rank1_lattice(self):
        n, d = 5, 2
        generator_vector = [1, 2]
        lattice = rank1_lattice(n, d, generator_vector=generator_vector)

        expected = np.array([
            [(0 * 1) % 5, (0 * 2) % 5],
            [(1 * 1) % 5, (1 * 2) % 5],
            [(2 * 1) % 5, (2 * 2) % 5],
            [(3 * 1) % 5, (3 * 2) % 5],
            [(4 * 1) % 5, (4 * 2) % 5],
        ])

        np.testing.assert_array_equal(lattice, expected)
