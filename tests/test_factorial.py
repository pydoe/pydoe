import unittest

import numpy as np

from pyDOE.doe_factorial import ff2n, fracfact, fracfact_by_res, fracfact_opt, fullfact


class TestFactorial(unittest.TestCase):
    def test_factorial1(self):
        expected = [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 2.0, 0.0],
            [1.0, 2.0, 0.0],
            [0.0, 3.0, 0.0],
            [1.0, 3.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
            [0.0, 2.0, 1.0],
            [1.0, 2.0, 1.0],
            [0.0, 3.0, 1.0],
            [1.0, 3.0, 1.0],
            [0.0, 0.0, 2.0],
            [1.0, 0.0, 2.0],
            [0.0, 1.0, 2.0],
            [1.0, 1.0, 2.0],
            [0.0, 2.0, 2.0],
            [1.0, 2.0, 2.0],
            [0.0, 3.0, 2.0],
            [1.0, 3.0, 2.0],
        ]
        actual = fullfact([2, 4, 3])
        np.testing.assert_allclose(actual, expected)

    def test_factorial2(self):
        expected = [
            [-1.0, -1.0, -1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = ff2n(3)
        np.testing.assert_allclose(actual, expected)

    def test_factorial3(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = fracfact("a b ab")
        np.testing.assert_allclose(actual, expected)

    def test_factorial4(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = fracfact("A B AB")
        np.testing.assert_allclose(actual, expected)

    def test_factorial5(self):
        expected = [
            [-1.0, -1.0, -1.0, -1.0, -1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0, -1.0, 1.0],
            [1.0, 1.0, -1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0, 1.0, 1.0],
            [1.0, -1.0, 1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0, 1.0, 1.0],
        ]
        actual = fracfact("a b -ab c +abc")
        np.testing.assert_allclose(actual, expected)

    def test_factorial6(self):
        expected = [
            [-1.0, -1.0, -1.0, 1.0, 1.0, 1.0],
            [1.0, -1.0, -1.0, -1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0, -1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0, 1.0, -1.0, -1.0],
            [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0, -1.0, -1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        ]
        actual = fracfact_by_res(6, 3)
        np.testing.assert_allclose(actual, expected)

    def test_issue_9(self):
        ffo_doe = fracfact_opt(4, 1)
        self.assertEqual(ffo_doe[0], "a b c abc")
        self.assertEqual(
            ffo_doe[1],
            [
                "a = bcd",
                "b = acd",
                "c = abd",
                "d = abc",
                "ab = cd",
                "ac = bd",
                "ad = bc",
                "abcd",
            ],
        )
        np.testing.assert_array_equal(
            ffo_doe[2], np.array([0.0, 0.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        )
