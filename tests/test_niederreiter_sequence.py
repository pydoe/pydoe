import itertools
import unittest

import numpy as np

from pydoe import niederreiter_sequence


class TestNiederreiterSequence(unittest.TestCase):
    def test_shape(self):
        for num_points, dimension in [(1, 1), (4, 2), (10, 5), (32, 20)]:
            seq = niederreiter_sequence(num_points, dimension)
            self.assertEqual(seq.shape, (num_points, dimension))

    def test_dtype(self):
        seq = niederreiter_sequence(4, 2)
        self.assertEqual(seq.dtype, np.float64)

    def test_values_within_unit_interval(self):
        seq = niederreiter_sequence(64, 10)
        self.assertTrue(bool(np.all(seq >= 0)))
        self.assertTrue(bool(np.all(seq < 1)))

    def test_first_point_is_origin(self):
        seq = niederreiter_sequence(1, 5)
        np.testing.assert_allclose(seq, np.zeros((1, 5)))

    def test_determinism(self):
        seq1 = niederreiter_sequence(20, 4)
        seq2 = niederreiter_sequence(20, 4)
        np.testing.assert_array_equal(seq1, seq2)

    def test_n_bits_changes_resolution(self):
        seq_default = niederreiter_sequence(64, 4)
        seq_small = niederreiter_sequence(64, 4, n_bits=4)
        self.assertEqual(seq_default.shape, seq_small.shape)
        self.assertFalse(np.allclose(seq_default, seq_small))
        # n_bits binary digits per coordinate
        np.testing.assert_array_equal(seq_small * 16, np.round(seq_small * 16))
        # and the points repeat after 2 ** n_bits of them
        np.testing.assert_array_equal(seq_small[:16], seq_small[16:32])

    def test_num_points_less_than_one_raises(self):
        with self.assertRaises(ValueError):
            niederreiter_sequence(0, 2)

    def test_dimension_less_than_one_raises(self):
        with self.assertRaises(ValueError):
            niederreiter_sequence(5, 0)

    def test_dimension_greater_than_twenty_raises(self):
        with self.assertRaises(ValueError):
            niederreiter_sequence(5, 21)

    def test_n_bits_less_than_two_raises(self):
        with self.assertRaises(ValueError):
            niederreiter_sequence(5, 2, n_bits=1)

    def test_max_dimension_is_supported(self):
        seq = niederreiter_sequence(8, 20)
        self.assertEqual(seq.shape, (8, 20))
        self.assertTrue(bool(np.all(seq >= 0)))
        self.assertTrue(bool(np.all(seq < 1)))

    def test_first_dimension_is_van_der_corput(self):
        seq = niederreiter_sequence(8, 1)
        expected = [0, 0.5, 0.25, 0.75, 0.125, 0.625, 0.375, 0.875]
        np.testing.assert_allclose(seq[:, 0], expected)

    def test_known_points(self):
        expected = np.array([
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.25],
            [0.25, 0.75, 0.75],
            [0.75, 0.25, 0.5],
            [0.125, 0.625, 0.5625],
            [0.625, 0.125, 0.8125],
            [0.375, 0.375, 0.3125],
            [0.875, 0.875, 0.0625],
        ])
        np.testing.assert_allclose(niederreiter_sequence(8, 3), expected)

    def test_every_dimension_takes_distinct_values(self):
        # The former generating matrices had rank at most the degree of
        # their polynomial, so 1024 points took only 4 to 16 distinct
        # values per dimension.
        m = 10
        seq = niederreiter_sequence(2**m, 20)
        for j in range(20):
            self.assertEqual(len(np.unique(seq[:, j])), 2**m)
        # For the two polynomials of degree 1, each coordinate is a
        # permutation of the multiples of 2**-m.
        grid = np.arange(2**m) / 2**m
        for j in range(2):
            np.testing.assert_allclose(np.sort(seq[:, j]), grid)

    def _assert_net(self, points, t, m):
        """Assert that ``points`` (2**m of them) form a (t, m, s)-net."""
        s = points.shape[1]
        for d in itertools.product(range(m - t + 1), repeat=s):
            if sum(d) != m - t:
                continue
            cells = np.zeros(len(points), dtype=np.int64)
            for i in range(s):
                side = 2 ** d[i]
                cells = cells * side + np.floor(points[:, i] * side).astype(
                    np.int64
                )
            counts = np.bincount(cells, minlength=2 ** (m - t))
            self.assertTrue(
                bool(np.all(counts == 2**t)),
                f"not a ({t}, {m}, {s})-net: intervals {d}",
            )

    def test_net_property(self):
        # t = sum(degree - 1) over the irreducible polynomials x, x + 1,
        # x^2 + x + 1, x^3 + x + 1, x^3 + x^2 + 1 of the dimensions.
        for s, t in [(1, 0), (2, 0), (3, 1), (4, 3), (5, 5)]:
            for m in range(t, 10):
                self._assert_net(niederreiter_sequence(2**m, s), t, m)

    def test_points_are_a_sequence(self):
        # The first points do not depend on how many are requested.
        np.testing.assert_array_equal(
            niederreiter_sequence(100, 6)[:37], niederreiter_sequence(37, 6)
        )

    def test_equidistribution_sanity_check(self):
        num_points = 256
        seq = niederreiter_sequence(num_points, 2, n_bits=8)

        bin_indices = np.minimum((seq * 4).astype(int), 3)
        counts = np.zeros((4, 4), dtype=int)
        for x_bin, y_bin in bin_indices:
            counts[x_bin, y_bin] += 1

        expected = num_points / 16
        self.assertTrue(bool(np.all(counts >= expected * 0.4)))
        self.assertTrue(bool(np.all(counts <= expected * 2.5)))
