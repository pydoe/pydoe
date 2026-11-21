import itertools
import re
import unittest
from collections import Counter

import numpy as np

from pydoe import get_orthogonal_array, list_orthogonal_arrays, taguchi_design


def _levels(array):
    return Counter(len(np.unique(column)) for column in array.T)


class TestOrthogonalArrays(unittest.TestCase):
    def test_names_match_arrays(self):
        # "L36(2^11 3^12)": 36 runs, 11 two-level and 12 three-level columns.
        for name in list_orthogonal_arrays():
            with self.subTest(name=name):
                array = get_orthogonal_array(name)
                runs, levels = re.fullmatch(r"L(\d+)\((.*)\)", name).groups()
                stated = Counter()
                for level, count in re.findall(r"(\d+)\^(\d+)", levels):
                    stated[int(level)] += int(count)
                self.assertEqual(array.shape[0], int(runs))
                self.assertEqual(_levels(array), stated)

    def test_every_pair_of_columns_is_balanced(self):
        # Strength 2: each pair of columns shows each pair of levels equally
        # often.
        for name in list_orthogonal_arrays():
            with self.subTest(name=name):
                array = get_orthogonal_array(name)
                for i, j in itertools.combinations(range(array.shape[1]), 2):
                    counts = Counter(zip(array[:, i], array[:, j], strict=True))
                    n_pairs = len(np.unique(array[:, i])) * len(
                        np.unique(array[:, j])
                    )
                    self.assertEqual(len(counts), n_pairs)
                    self.assertEqual(len(set(counts.values())), 1)

    def test_l64_main_effects_clear_of_two_factor_interactions(self):
        signs = 2 * get_orthogonal_array("L64(2^31)") - 1
        for cols in itertools.combinations(range(31), 3):
            self.assertEqual(np.prod(signs[:, list(cols)], axis=1).sum(), 0)

    def test_l18_one_two_level_and_seven_three_level_columns(self):
        array = get_orthogonal_array("L18(2^1 3^7)")
        self.assertEqual(array.shape, (18, 8))
        self.assertEqual(
            [len(np.unique(column)) for column in array.T], [2] + [3] * 7
        )

    def test_old_names_warn_and_return_the_renamed_array(self):
        for old, new in [
            ("L27(2^1 3^12)", "L27(3^13)"),
            ("L36(3^23)", "L36(2^11 3^12)"),
        ]:
            with self.subTest(old=old):
                with self.assertWarns(DeprecationWarning):
                    array = get_orthogonal_array(old)
                np.testing.assert_array_equal(array, get_orthogonal_array(new))
                self.assertNotIn(old, list_orthogonal_arrays())

    def test_taguchi_design_with_old_name_warns(self):
        levels = [[1, 2, 3]] * 13
        with self.assertWarns(DeprecationWarning):
            old = taguchi_design("L27(2^1 3^12)", levels)
        np.testing.assert_array_equal(old, taguchi_design("L27(3^13)", levels))
