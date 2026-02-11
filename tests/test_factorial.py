import unittest

import numpy as np
import pytest

from pydoe.doe_factorial import (
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

    def test_fracfact_by_res_resolution_III(self):
        """Test resolution III designs"""
        # 8 runs should support 4 factors at resolution III
        actual = fracfact_by_res(4, 3)
        assert actual.shape[0] == 8
        assert actual.shape[1] == 4

        # 16 runs should support 7 factors at resolution III
        actual = fracfact_by_res(7, 3)
        assert actual.shape[0] == 16
        assert actual.shape[1] == 7

    def test_fracfact_by_res_resolution_IV(self):
        """Test resolution IV designs"""
        # 16 runs should support 4 factors at resolution IV
        actual = fracfact_by_res(4, 4)
        assert actual.shape[0] == 16
        assert actual.shape[1] == 4

        # 32 runs should support 8 factors at resolution IV
        actual = fracfact_by_res(8, 4)
        assert actual.shape[0] == 32
        assert actual.shape[1] == 8

    def test_fracfact_by_res_invalid_n(self):
        with pytest.raises(ValueError, match="n must be at least 2"):
            fracfact_by_res(1, 3)

    def test_fracfact_by_res_invalid_resolution(self):
        with pytest.raises(ValueError, match="resolution must be >= 3"):
            fracfact_by_res(3, 2)

    def test_fracfact_by_res_table_lookup_path(self):
        # (6, 3) is explicitly in the DOE table -> k = 3
        design = fracfact_by_res(6, 3)
        assert design.shape == (8, 6)  # 2^3 runs, 6 factors
        assert set(np.unique(design)) == {-1.0, 1.0}

    def test_fracfact_by_res_fallback_calculation_path(self):
        # (16, 3) is not in the table -> fallback calculation
        design = fracfact_by_res(16, 3)
        # k = ceil(log2(17)) = 5 -> 32 runs
        assert design.shape == (32, 16)
        assert set(np.unique(design)) == {-1.0, 1.0}

    def test_fracfact_by_res_exceeds_base_factor_limit(self):
        with pytest.raises(ValueError, match="more than 26 base factors"):
            fracfact_by_res(2**27, 3)

    def test_fracfact_by_res_too_many_base_factors(self):
        # Force k > 26 via fallback logic
        with pytest.raises(ValueError, match="more than 26 base factors"):
            fracfact_by_res(2**27, 3)

    def test_fracfact_by_res_resolution_five(self):
        design = fracfact_by_res(6, 5)
        # From table: (6,5) -> k = 6 -> 64 runs
        assert design.shape == (64, 6)
        assert set(np.unique(design)) == {-1.0, 1.0}

    def test_fracfact_by_res_columns_match_n(self):
        for n, res in [(5, 3), (7, 4), (9, 5)]:
            design = fracfact_by_res(n, res)
            assert design.shape[1] == n


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
