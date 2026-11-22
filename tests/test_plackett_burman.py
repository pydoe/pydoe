import itertools
import unittest

import numpy as np

from pydoe import pbdesign


class TestPlackettBurman(unittest.TestCase):
    def test_plackett_burman1(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = pbdesign(3)
        np.testing.assert_allclose(actual, expected)

    def test_plackett_burman2(self):
        expected = [
            [-1.0, -1.0, 1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0, -1.0, 1.0],
            [1.0, 1.0, 1.0, -1.0, -1.0],
            [-1.0, -1.0, 1.0, 1.0, -1.0],
            [1.0, -1.0, -1.0, 1.0, 1.0],
            [-1.0, 1.0, -1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0],
        ]
        actual = pbdesign(5)
        np.testing.assert_allclose(actual, expected)


def _signs(row):
    return np.array([1.0 if sign == "+" else -1.0 for sign in row.split()])


# Box and Draper (2007), p. 153: the generating rows of Plackett and
# Burman's (1946) designs. Montgomery (2012, Table 8.23) prints the same rows
# for 24 and 36 runs.
PRINTED_ROWS = {
    24: "+ + + + + - + - + + - - + + - - + - + - - - -",
    36: "- + - + + + - - - + + + + + - + + + - - + - - - - + - + - + + - - + -",
    44: "+ + - - + - + - - + + + - + + + + + - - - + - + + + - - - - - + - "
    "- - + + - + - + + -",
    48: "+ + + + + - + + + + - - + - + - + + + - - + - - + + - + + - - - + "
    "- + - + + - - - - + - - - -",
    60: "+ + - + + + - + - + - - + - - + + + - + + + + - - + + + + + - - - "
    "- - + + - - - - + - - - + + - + + - + - + - - - + -",
}


class TestPlackettBurmanSizes(unittest.TestCase):
    def test_every_multiple_of_four_up_to_112(self):
        for runs in range(4, 113, 4):
            with self.subTest(runs=runs):
                H = pbdesign(runs - 1)
                self.assertEqual(H.shape, (runs, runs - 1))
                self.assertTrue(np.all(np.abs(H) == 1))
                np.testing.assert_array_equal(H.T @ H, runs * np.eye(runs - 1))
                np.testing.assert_array_equal(H.sum(axis=0), 0)

    def test_printed_generating_rows(self):
        # The first column is the generating row, each next column the one
        # before moved down one run, then a run of minus signs.
        for runs, row in PRINTED_ROWS.items():
            with self.subTest(runs=runs):
                H = pbdesign(runs - 1)
                first = _signs(row)
                expected = np.column_stack([
                    np.roll(first, shift) for shift in range(runs - 1)
                ])
                np.testing.assert_array_equal(H[:-1], expected)
                np.testing.assert_array_equal(H[-1], -1)

    def test_28_runs_printed_blocks(self):
        # Box and Draper (2007), Table 5.8, and Montgomery (2012), Table 8.23:
        # blocks X Y Z / Z X Y / Y Z X, then a run of minus signs.
        H = pbdesign(27)
        first = "+ - + + + + - - - - + - - - + - - + + + - + - + + - +"
        tenth = "+ + - + - + + - + + - + + + + - - - - + - - - + - - +"
        np.testing.assert_array_equal(H[0], _signs(first))
        np.testing.assert_array_equal(H[9], _signs(tenth))
        np.testing.assert_array_equal(H[-1], -1)

    def test_24_runs_has_no_completely_aliased_interaction(self):
        # In the doubled 12-run design, 11 sets of three columns had a
        # constant product; in Plackett and Burman's design none does.
        H = pbdesign(23)
        largest = max(
            abs(np.prod(H[:, list(cols)], axis=1).sum())
            for cols in itertools.combinations(range(23), 3)
        )
        self.assertEqual(largest, 8)

    def test_error_names_the_run_count(self):
        with self.assertRaisesRegex(ValueError, "116 runs"):
            pbdesign(113)
