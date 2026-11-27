import unittest

import numpy as np
import pytest

from pydoe import rank1_lattice


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


def test_rank1_lattice_seed_is_reproducible():
    a = rank1_lattice(31, 4, seed=5)
    b = rank1_lattice(31, 4, seed=5)
    np.testing.assert_array_equal(a, b)
    different = [rank1_lattice(31, 4, seed=s) for s in range(6)]
    assert any(not np.array_equal(a, d) for d in different)
    # a Generator is accepted too, and the given vector wins over the seed
    np.testing.assert_array_equal(
        rank1_lattice(31, 4, seed=np.random.default_rng(5)), a
    )
    np.testing.assert_array_equal(
        rank1_lattice(7, 2, [1, 3], seed=0), rank1_lattice(7, 2, [1, 3])
    )


def test_rank1_lattice_too_few_points_for_a_random_vector():
    with pytest.raises(ValueError, match="at least 3"):
        rank1_lattice(2, 2)
    assert rank1_lattice(2, 2, [1, 1]).shape == (2, 2)
