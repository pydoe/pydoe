import unittest

import numpy as np

from pyDOE.doe_taguchi import TaguchiObjective, compute_snr, taguchi_design


class TestTaguchiDesign(unittest.TestCase):
    def test_design_L_4_3_2(self):
        levels_per_factor = [[2, 4], [3, 5], [0, 1]]

        design = taguchi_design("L4(2^3)", levels_per_factor)
        design = design.astype(int)

        expected_design = np.array([[2, 3, 0], [2, 5, 1], [4, 3, 1], [4, 5, 0]])

        np.testing.assert_array_equal(design, expected_design)

        responses = np.array([
            [15, 16, 17],
            [20, 21, 22],
            [25, 26, 27],
            [30, 31, 32],
        ])

        expected_snrs = np.array([
            -10 * np.log10(np.mean(1.0 / y**2)) for y in responses
        ])

        actual_snrs = np.array([
            compute_snr(y, TaguchiObjective.LARGER_IS_BETTER) for y in responses
        ])

        np.testing.assert_allclose(actual_snrs, expected_snrs, rtol=1e-5)

        self.assertEqual(design.shape, (4, 3))

        for col, levels in enumerate(levels_per_factor):
            unique_vals = np.unique(design[:, col])
            self.assertTrue(set(unique_vals).issubset(set(levels)))


if __name__ == "__main__":
    unittest.main()
