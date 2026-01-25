import unittest

import numpy as np
import pytest

from pyDOE.doe_factorial import (
    ff2n,
    fracfact,
    fracfact_by_res,
    fracfact_opt,
    fullfact,
    validate_generator,
)


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
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0],
            [1.0, -1.0, -1.0],
            [1.0, -1.0, 1.0],
            [1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = ff2n(3)
        np.testing.assert_allclose(actual, expected)

    def test_factorial3(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, -1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = fracfact("a b ab")
        np.testing.assert_allclose(actual, expected)

    def test_factorial4(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, -1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = fracfact("A B AB")
        np.testing.assert_allclose(actual, expected)

    def test_factorial5(self):
        expected = [
            [-1.0, -1.0, -1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0, 1.0, 1.0],
            [-1.0, 1.0, 1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0, 1.0, -1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0, -1.0, -1.0],
            [1.0, 1.0, -1.0, 1.0, 1.0],
        ]
        actual = fracfact("a b -ab c +abc")
        np.testing.assert_allclose(actual, expected)

    def test_factorial6(self):
        expected = [
            [-1.0, -1.0, -1.0, 1.0, 1.0, 1.0],
            [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0, -1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0, -1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0, -1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0, 1.0, -1.0, -1.0],
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
            ffo_doe[2],
            np.array([0.0, 0.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        )


@pytest.mark.parametrize(
    "n_factors, generator, message",
    [
        (2, "a b c", "Generator does not match the number of factors."),
        (2, "a a", "Main factors are confounded with each other."),
        (2, "a c", "Use the letters `a b` for the main factors."),
        (5, "a b c ab ab", "Generators are not unique."),
        (5, "a b c ab ad", "Generators are not valid."),
        (2, "ab ac", "At least one unconfounded main factor is needed."),
    ],
)
def test_validate_generator_invalid(
    n_factors: int, generator: str, message: str
):
    with pytest.raises(ValueError, match=message):
        validate_generator(n_factors, generator)
