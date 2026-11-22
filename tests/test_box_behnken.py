import itertools
import unittest

import numpy as np

from pydoe import bbdesign


class TestBoxBehnken(unittest.TestCase):
    def test_box_behnken1(self):
        expected = [
            [-1.0, -1.0, 0.0],
            [-1.0, 1.0, 0.0],
            [1.0, -1.0, 0.0],
            [1.0, 1.0, 0.0],
            [-1.0, 0.0, -1.0],
            [-1.0, 0.0, 1.0],
            [1.0, 0.0, -1.0],
            [1.0, 0.0, 1.0],
            [0.0, -1.0, -1.0],
            [0.0, -1.0, 1.0],
            [0.0, 1.0, -1.0],
            [0.0, 1.0, 1.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
        actual = bbdesign(3)
        np.testing.assert_allclose(actual, expected)

    def test_box_behnken_run_counts(self):
        # Box and Behnken (1960), Table 4, without centre runs; 3 to 5
        # factors pair every two factors, the rest use incomplete blocks.
        published = {
            3: 12,
            4: 24,
            5: 40,
            6: 48,
            7: 56,
            9: 120,
            10: 160,
            11: 176,
            12: 192,
            16: 384,
        }
        for n, runs in published.items():
            with self.subTest(n=n):
                self.assertEqual(bbdesign(n, center=0).shape, (runs, n))

    def test_box_behnken_all_pairs_without_published_design(self):
        # No design was published for 8 or 13 factors: every pair of
        # factors carries a 2^2 factorial.
        for n in (8, 13):
            with self.subTest(n=n):
                H = bbdesign(n, center=0)
                self.assertEqual(H.shape, (4 * n * (n - 1) // 2, n))
                self.assertTrue(np.all(np.count_nonzero(H, axis=1) == 2))

    def test_box_behnken_six_factors_matches_docs_table(self):
        # Table 3.28 of the docs: 54 runs, with the default 6 centre runs.
        self.assertEqual(bbdesign(6).shape, (54, 6))

    def test_box_behnken_fits_full_quadratic_model(self):
        for n in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16):
            with self.subTest(n=n):
                H = bbdesign(n, center=1)
                pairs = itertools.combinations(range(n), 2)
                X = np.column_stack([
                    np.ones(len(H)),
                    *H.T,
                    *(H[:, i] * H[:, j] for i, j in pairs),
                    *(H**2).T,
                ])
                self.assertEqual(np.linalg.matrix_rank(X), X.shape[1])

    def test_box_behnken_seven_factors_is_rotatable(self):
        # Box and Draper (2007), exercise 15.4: the 56-run design in seven
        # factors is rotatable: [iiii] = 3 [iijj] for every pair of factors.
        H = bbdesign(7, center=0)
        pure = (H**4).sum(axis=0)
        mixed = [
            (H[:, i] ** 2 * H[:, j] ** 2).sum()
            for i, j in itertools.combinations(range(7), 2)
        ]
        np.testing.assert_allclose(pure, 3 * mixed[0])
        np.testing.assert_allclose(mixed, mixed[0])

    def test_box_behnken_balanced_three_levels(self):
        for n in (6, 7, 9, 10, 11, 12, 16):
            with self.subTest(n=n):
                H = bbdesign(n, center=0)
                self.assertTrue(set(np.unique(H)) <= {-1.0, 0.0, 1.0})
                # each factor is at -1 and +1 equally often
                np.testing.assert_array_equal(H.sum(axis=0), 0)
                # first-order columns are orthogonal to each other
                np.testing.assert_allclose(
                    H.T @ H, np.diag(np.diag(H.T @ H)), atol=1e-12
                )

    def test_box_behnken_blocks_match_box_and_draper(self):
        # Box and Draper (2007), Table 15.9: the factors (numbered from 0)
        # that each block varies, each block carrying a 2^3 factorial.
        printed = {
            6: [
                (0, 1, 3),
                (0, 2, 5),
                (0, 3, 4),
                (1, 2, 4),
                (1, 4, 5),
                (2, 3, 5),
            ],
            7: [
                (0, 1, 3),
                (0, 2, 4),
                (0, 5, 6),
                (1, 2, 5),
                (1, 4, 6),
                (2, 3, 6),
                (3, 4, 5),
            ],
        }
        for n, blocks in printed.items():
            with self.subTest(n=n):
                H = bbdesign(n, center=0)
                supports = {tuple(np.flatnonzero(row)) for row in H}
                for block in supports:
                    rows = H[
                        np.all((H != 0) == np.isin(range(n), block), axis=1)
                    ]
                    self.assertEqual(
                        {tuple(r[list(block)]) for r in rows},
                        set(itertools.product((-1.0, 1.0), repeat=3)),
                    )
                # Seven factors are written cyclically: the printed design up
                # to a relabelling of the factors.
                relabelled = any(
                    {tuple(sorted(p[f] for f in b)) for b in supports}
                    == set(blocks)
                    for p in itertools.permutations(range(n))
                )
                self.assertTrue(relabelled)
                if n == 6:
                    self.assertEqual(supports, set(blocks))
