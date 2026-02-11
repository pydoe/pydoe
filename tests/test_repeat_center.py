import unittest

import numpy as np

from pydoe import repeat_center


class TestRepeatCenter(unittest.TestCase):
    def test_repeat_center1(self):
        expected = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        actual = repeat_center(3, 2)
        np.testing.assert_allclose(actual, expected)
