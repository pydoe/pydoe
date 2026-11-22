import itertools
import unittest
from unittest import mock

import numpy as np

from pydoe import block_ccdesign, block_full_factorial, small_composite_design


class TestBlockFullFactorial(unittest.TestCase):
    def test_shape(self):
        design, blocks = block_full_factorial(3, [(0, 1, 2)])
        self.assertEqual(design.shape, (8, 3))
        self.assertEqual(blocks.shape, (8,))

    def test_two_blocks_have_equal_size(self):
        _design, blocks = block_full_factorial(3, [(0, 1, 2)])
        self.assertEqual(np.sum(blocks == 0), 4)
        self.assertEqual(np.sum(blocks == 1), 4)

    def test_exact_values(self):
        _design, blocks = block_full_factorial(3, [(0, 1, 2)])
        expected_blocks = np.array([1, 0, 0, 1, 0, 1, 1, 0])
        np.testing.assert_array_equal(blocks, expected_blocks)

    def test_confounded_interaction_constant_within_block(self):
        design, blocks = block_full_factorial(3, [(0, 1, 2)])
        contrast = np.sign(design.prod(axis=1))
        for b in np.unique(blocks):
            self.assertEqual(len(np.unique(contrast[blocks == b])), 1)

    def test_four_blocks_from_two_generators(self):
        design, blocks = block_full_factorial(4, [(0, 1), (1, 2, 3)])
        self.assertEqual(design.shape, (16, 4))
        self.assertEqual(set(np.unique(blocks).tolist()), {0, 1, 2, 3})
        for b in range(4):
            self.assertEqual(np.sum(blocks == b), 4)

    def test_raises_k_less_than_2(self):
        with self.assertRaises(ValueError):
            block_full_factorial(1, [(0,)])

    def test_raises_empty_generators(self):
        with self.assertRaises(ValueError):
            block_full_factorial(3, [])

    def test_raises_empty_generator_tuple(self):
        with self.assertRaises(ValueError):
            block_full_factorial(3, [()])

    def test_raises_repeated_index(self):
        with self.assertRaises(ValueError):
            block_full_factorial(3, [(0, 0)])

    def test_raises_out_of_range_index(self):
        with self.assertRaises(ValueError):
            block_full_factorial(3, [(0, 3)])

    def test_raises_too_many_blocks(self):
        with self.assertRaises(ValueError):
            block_full_factorial(2, [(0,), (1,), (0, 1)])


class TestBlockCcdesign(unittest.TestCase):
    def test_shape(self):
        design, blocks = block_ccdesign(2, center=(2, 2))
        self.assertEqual(design.shape, (4 + 2 + 4 + 2, 2))
        self.assertEqual(blocks.shape, (12,))

    def test_block_labels(self):
        _design, blocks = block_ccdesign(2, center=(2, 2))
        self.assertEqual(np.sum(blocks == 0), 6)
        self.assertEqual(np.sum(blocks == 1), 6)

    def test_exact_values_n2(self):
        expected = np.array([
            [-1.0, -1.0],
            [-1.0, 1.0],
            [1.0, -1.0],
            [1.0, 1.0],
            [0.0, 0.0],
            [0.0, 0.0],
            [-np.sqrt(2), 0.0],
            [np.sqrt(2), 0.0],
            [0.0, -np.sqrt(2)],
            [0.0, np.sqrt(2)],
            [0.0, 0.0],
            [0.0, 0.0],
        ])
        design, _blocks = block_ccdesign(2, center=(2, 2))
        np.testing.assert_allclose(design, expected, atol=1e-8)

    def test_factorial_block_is_first(self):
        design, blocks = block_ccdesign(3, center=(4, 4))
        factorial_part = design[blocks == 0]
        self.assertEqual(factorial_part.shape, (8 + 4, 3))

    def test_raises_n_less_than_2(self):
        with self.assertRaises(ValueError):
            block_ccdesign(1)

    def test_raises_invalid_center(self):
        with self.assertRaises(ValueError):
            block_ccdesign(2, center=(1, 1, 1))


class TestSmallCompositeDesign(unittest.TestCase):
    def test_shape(self):
        design = small_composite_design(4, center=(2, 2))
        self.assertEqual(design.shape, (8 + 8 + 4, 4))

    def test_fewer_runs_than_full_ccd(self):
        # Full CCD on 2**4 has 16 + 8 + center runs, small composite uses
        # only 8 cube runs.
        design = small_composite_design(4, center=(2, 2))
        self.assertEqual(design.shape[0], 20)

    def test_cube_portion_is_plus_minus_one(self):
        design = small_composite_design(4, center=(2, 2))
        cube = design[:8]
        self.assertTrue(np.all(np.abs(cube) == 1))

    def test_star_points_present(self):
        design = small_composite_design(4, center=(2, 2))
        star_part = design[8 + 2 :]
        # 2*n star points should each have exactly one nonzero entry
        nonzero_counts = np.count_nonzero(star_part[:8], axis=1)
        np.testing.assert_array_equal(nonzero_counts, np.ones(8))

    def test_raises_n_less_than_3(self):
        with self.assertRaises(ValueError):
            small_composite_design(2)

    def test_raises_invalid_center(self):
        with self.assertRaises(ValueError):
            small_composite_design(4, center=(1,))

    def test_fits_full_quadratic_model(self):
        # Hartley (1959): the design must estimate the full second-order
        # model, with any center runs.
        for n in range(3, 13):
            for center in ((4, 4), (1, 0)):
                with self.subTest(n=n, center=center):
                    H = small_composite_design(n, center=center)
                    pairs = itertools.combinations(range(n), 2)
                    X = np.column_stack([
                        np.ones(len(H)),
                        *H.T,
                        *(H[:, i] * H[:, j] for i, j in pairs),
                        *(H**2).T,
                    ])
                    self.assertEqual(np.linalg.matrix_rank(X), X.shape[1])

    def test_no_two_factor_interactions_aliased_in_cube(self):
        for n in range(3, 13):
            with self.subTest(n=n):
                H = small_composite_design(n, center=(0, 0))
                cube = H[: len(H) - 2 * n]
                columns = [
                    cube[:, i] * cube[:, j]
                    for i, j in itertools.combinations(range(n), 2)
                ]
                for a, b in itertools.combinations(columns, 2):
                    self.assertLess(abs(a @ b), len(cube))

    def test_runs_match_box_and_draper(self):
        # Box and Draper (2007), p. 501: cube plus star runs.
        published = {3: 10, 4: 16, 5: 26, 6: 28, 7: 46, 9: 82}
        for n, runs in published.items():
            with self.subTest(n=n):
                H = small_composite_design(n, center=(0, 0))
                self.assertEqual(H.shape, (runs, n))

    def test_accepts_numpy_integer(self):
        # As on master, a numpy integer number of factors works.
        np.testing.assert_array_equal(
            small_composite_design(np.int64(5)), small_composite_design(5)
        )

    def test_falls_back_to_full_factorial_when_budget_runs_out(self):
        # With no search steps, no fraction is found: the cube is the full
        # 2^3 factorial (8 runs), not the 4-run fraction with C = AB.
        with mock.patch(
            "pydoe.response_surface.small_composite._SEARCH_BUDGET", 0
        ):
            design = small_composite_design(3, center=(0, 0))
        self.assertEqual(design.shape, (8 + 6, 3))
        self.assertEqual(
            small_composite_design(3, center=(0, 0)).shape, (10, 3)
        )
