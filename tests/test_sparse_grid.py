import itertools

import numpy as np
import pytest

from pydoe import doe_sparse_grid, sparse_grid_dimension


class TestSparseGridExamples:
    def test_spdemo_2d_example(self):
        # From spdemo.m: 2D example with Clenshaw-Curtis grid
        level = 3
        dims = 2

        # MATLAB reference: spdim(3, 2) = 29
        expected_points = 29

        # Test point count calculation
        actual_count = sparse_grid_dimension(level, dims)
        assert actual_count == expected_points, (
            f"Expected {expected_points}, got {actual_count}"
        )

        # Test actual grid generation
        design = doe_sparse_grid(level, dims)
        assert len(design) == expected_points
        assert design.shape[1] == dims

        # Test function evaluation like in spdemo.m
        # (scale points to [0,2] x [-1,1])
        def test_function(x, y):
            return 1.0 / ((x * 2 - 0.3) ** 4 + (y * 3 - 0.7) ** 2 + 1)

        # Scale design from [0,1] to [0,2] x [-1,1] for function evaluation
        design_scaled = design.copy()
        design_scaled[:, 0] = design[:, 0] * 2  # Scale x from [0,1] to [0,2]
        design_scaled[:, 1] = (
            design[:, 1] * 2 - 1
        )  # Scale y from [0,1] to [-1,1]

        function_values = test_function(
            design_scaled[:, 0], design_scaled[:, 1]
        )
        assert np.all(np.isfinite(function_values))
        assert np.all(function_values > 0)

    def test_spcompare_3d_example(self):
        # From spcompare.m: 3D test with different levels
        dims = 3

        # MATLAB reference values from spcompare.m test levels
        test_cases = [
            (1, 7),  # spdim(1, 3) = 7
            (2, 25),  # spdim(2, 3) = 25
            (3, 69),  # spdim(3, 3) = 69
        ]

        for level, expected in test_cases:
            # Test dimension calculation
            actual_count = sparse_grid_dimension(level, dims)
            assert actual_count == expected, (
                f"Level {level}: expected {expected}, got {actual_count}"
            )

            # Test grid generation
            design = doe_sparse_grid(level, dims)
            assert len(design) == expected
            assert design.shape[1] == dims

            # All points should be in unit cube [0,1]^3
            assert np.all(design >= 0.0) and np.all(design <= 1.0)

    def test_testfunctions_genz_examples(self):
        # Test functions are defined on [0,1]^d as in testfunctions.m

        # Test different dimensions as used in spcompare.m
        test_cases = [
            (2, 2, 13),  # 2D, level 2
            (3, 2, 25),  # 3D, level 2
            (5, 2, 61),  # 5D, level 2
        ]

        for dims, level, expected_points in test_cases:
            design = doe_sparse_grid(level, dims)

            # Verify point count matches MATLAB
            assert len(design) == expected_points

            # Verify domain [0,1]^d as required by Genz functions
            assert np.all(design >= 0.0) and np.all(design <= 1.0)

            # Test Genz function evaluation examples
            # Function 2: Product Peak (from testfunctions.m)
            c = np.random.rand(dims) * 5 + 1  # Parameters c_i
            w = np.random.rand(dims)  # Parameters w_i

            def product_peak(points, _c=c, _w=w, _dims=dims):
                result = np.ones(len(points))
                for i in range(_dims):
                    result *= 1.0 / (
                        _c[i] ** (-2) + (points[:, i] - _w[i]) ** 2
                    )
                return result

            values = product_peak(design)
            assert np.all(np.isfinite(values))
            assert np.all(values > 0)

    def test_matlab_verified_point_counts(self):
        # These values were directly verified with MATLAB spdim(n,d)
        matlab_verified = [
            # (level, dims, matlab_spdim_result)
            (0, 1, 1),
            (0, 2, 1),
            (0, 3, 1),
            (0, 5, 1),
            (1, 1, 3),
            (1, 2, 5),
            (1, 3, 7),
            (1, 5, 11),
            (2, 1, 5),
            (2, 2, 13),
            (2, 3, 25),
            (2, 5, 61),
            (3, 1, 9),
            (3, 2, 29),
            (3, 3, 69),
            (4, 1, 17),
            (4, 2, 65),
            (4, 3, 177),
            (5, 1, 33),
            (5, 2, 145),
            (5, 3, 441),
        ]

        for level, dims, expected in matlab_verified:
            # Test dimension calculation
            actual = sparse_grid_dimension(level, dims)
            assert actual == expected, (
                f"spdim({level}, {dims}): expected {expected}, got {actual}"
            )

            # Test actual grid generation
            design = doe_sparse_grid(level, dims)
            assert len(design) == expected, (
                f"Grid generation ({level}, {dims}): expected {expected},"
                f" got {len(design)}"
            )

    def test_grid_type_variations(self):
        level, dims = 2, 2
        # Clenshaw-Curtis and Chebyshev: 1, 3, 5 points per axis;
        # Gauss-Patterson: 1, 3, 7 points per axis.
        expected_counts = {
            "clenshaw_curtis": 13,
            "chebyshev": 13,
            "gauss_patterson": 17,
        }

        for grid_type, expected_count in expected_counts.items():
            design = doe_sparse_grid(level, dims, grid_type=grid_type)
            assert len(design) == expected_count, (
                f"{grid_type} should produce {expected_count} points"
            )
            assert design.shape[1] == dims
            assert np.all(design >= 0.0) and np.all(design <= 1.0)
            assert sparse_grid_dimension(level, dims, grid_type) == (
                expected_count
            )

    def test_grid_types(self):
        level, dims = 2, 3

        design_cc = doe_sparse_grid(level, dims, grid_type="clenshaw_curtis")
        assert len(design_cc) == 25  # MATLAB verified

        design_cheb = doe_sparse_grid(level, dims, grid_type="chebyshev")
        assert len(design_cheb) == 25

        design_gp = doe_sparse_grid(level, dims, grid_type="gauss_patterson")
        assert len(design_gp) == 31

    def test_grid_types_give_different_points(self):
        # grid_type used to be ignored: all three gave the same design.
        cc = doe_sparse_grid(3, 2, grid_type="clenshaw_curtis")
        cheb = doe_sparse_grid(3, 2, grid_type="chebyshev")
        gp = doe_sparse_grid(3, 2, grid_type="gauss_patterson")
        assert cc.shape == cheb.shape
        assert not np.allclose(cc, cheb)
        assert gp.shape != cc.shape
        # only the Gauss-Patterson grid stays off the boundary
        assert np.any(cc == 0.0) and np.any(cc == 1.0)
        assert np.any(cheb == 0.0) and np.any(cheb == 1.0)
        assert np.all(gp > 0.0) and np.all(gp < 1.0)

    def test_unknown_grid_type(self):
        with pytest.raises(ValueError, match="grid_type must be one of"):
            doe_sparse_grid(2, 2, grid_type="bogus")
        with pytest.raises(ValueError, match="grid_type must be one of"):
            sparse_grid_dimension(2, 2, grid_type="bogus")

    def test_one_dimensional_points(self):
        np.testing.assert_allclose(
            np.sort(doe_sparse_grid(3, 1, "clenshaw_curtis")[:, 0]),
            np.linspace(0, 1, 9),
        )
        np.testing.assert_allclose(
            np.sort(doe_sparse_grid(3, 1, "chebyshev")[:, 0]),
            (1 - np.cos(np.pi * np.arange(9) / 8)) / 2,
        )
        # Gauss-Patterson: 3-point Gauss-Legendre rule, then Patterson's
        # 7-point extension (Patterson, 1968)
        np.testing.assert_allclose(
            np.sort(doe_sparse_grid(1, 1, "gauss_patterson")[:, 0]) * 2 - 1,
            [-np.sqrt(0.6), 0.0, np.sqrt(0.6)],
            atol=1e-14,
        )
        np.testing.assert_allclose(
            np.sort(doe_sparse_grid(2, 1, "gauss_patterson")[:, 0]) * 2 - 1,
            [
                -0.9604912687080203,
                -np.sqrt(0.6),
                -0.4342437493468026,
                0.0,
                0.4342437493468026,
                np.sqrt(0.6),
                0.9604912687080203,
            ],
            atol=1e-13,
        )

    def test_gauss_patterson_rules_are_exact(self):
        # The rule with 2n + 1 nodes integrates polynomials of degree
        # 3n + 1 exactly, which pins the nodes down.
        legendre = np.polynomial.legendre
        for level in range(1, 6):
            nodes = np.sort(doe_sparse_grid(level, 1, "gauss_patterson")[:, 0])
            x = nodes * 2 - 1
            m = len(x)
            assert m == 2 ** (level + 1) - 1
            degree = 3 * ((m - 1) // 2) + 1
            target = np.zeros(m)
            target[0] = 2.0
            weights = np.linalg.solve(legendre.legvander(x, m - 1).T, target)
            assert np.all(weights > 0)
            moments = legendre.legvander(x, degree).T @ weights
            moments[0] -= 2.0
            assert np.max(np.abs(moments)) < 1e-9

    def test_gauss_patterson_level_limit(self):
        with pytest.raises(ValueError, match="up to n_level 5"):
            doe_sparse_grid(6, 2, grid_type="gauss_patterson")

    def test_is_smolyak_union_of_tensor_grids(self):
        # H(n, d) is the union of the tensor grids X^l1 x ... x X^ld over
        # l1 + ... + ld <= n.
        for grid_type in ["clenshaw_curtis", "chebyshev", "gauss_patterson"]:
            for level, dims in [(2, 2), (3, 2), (4, 2), (3, 3), (2, 4)]:
                axes = [
                    doe_sparse_grid(lv, 1, grid_type)[:, 0]
                    for lv in range(level + 1)
                ]
                expected = set()
                for lv in itertools.product(range(level + 1), repeat=dims):
                    if sum(lv) <= level:
                        for point in itertools.product(*(axes[i] for i in lv)):
                            expected.add(tuple(np.round(point, 12)))
                design = doe_sparse_grid(level, dims, grid_type)
                actual = {tuple(np.round(p, 12)) for p in design}
                assert len(actual) == len(design), "duplicate points"
                assert actual == expected

    def test_levels_are_nested(self):
        for grid_type in ["clenshaw_curtis", "chebyshev", "gauss_patterson"]:
            for dims in (1, 2, 3):
                for level in range(1, 5):
                    lower = doe_sparse_grid(level - 1, dims, grid_type)
                    upper = doe_sparse_grid(level, dims, grid_type)
                    np.testing.assert_array_equal(upper[: len(lower)], lower)

    def test_design_is_symmetric(self):
        for grid_type in ["clenshaw_curtis", "chebyshev", "gauss_patterson"]:
            design = doe_sparse_grid(3, 3, grid_type)
            points = {tuple(np.round(p, 12)) for p in design}
            mirrored = {tuple(np.round(1 - p, 12)) for p in design}
            swapped = {tuple(np.round(p[::-1], 12)) for p in design}
            assert points == mirrored
            assert points == swapped

    def test_point_count_matches_generated_design(self):
        for grid_type in ["clenshaw_curtis", "chebyshev", "gauss_patterson"]:
            for level in range(6):
                for dims in range(1, 5):
                    assert sparse_grid_dimension(level, dims, grid_type) == len(
                        doe_sparse_grid(level, dims, grid_type)
                    )

    def test_point_count_beyond_level_seven(self):
        # The closed-form table stopped at level 7 and returned the
        # level-7 count for every higher level.
        assert sparse_grid_dimension(7, 1) == 129
        assert sparse_grid_dimension(8, 1) == 257
        assert sparse_grid_dimension(9, 1) == 513
        assert sparse_grid_dimension(8, 2) == 1537
        assert sparse_grid_dimension(8, 2) == len(doe_sparse_grid(8, 2))

    def test_high_dimensional_efficiency(self):
        # Test cases inspired by spcompare.m high-dimensional tests
        efficiency_tests = [
            (3, 2, 25, 27),  # 3D: sparse vs 3^3 full grid
            (5, 2, 61, 243),  # 5D: sparse vs 3^5 full grid
            (8, 1, 17, 6561),  # 8D: sparse vs 3^8 full grid
            (10, 1, 21, 59049),  # 10D: sparse vs 3^10 full grid
        ]

        for dims, level, expected_sparse, full_grid in efficiency_tests:
            sparse_count = sparse_grid_dimension(level, dims)
            assert sparse_count == expected_sparse

            # Verify efficiency for higher dimensions
            if dims >= 5:
                assert sparse_count < full_grid, (
                    f"Sparse grid should be more efficient for {dims}D"
                )
                efficiency = full_grid / sparse_count
                assert efficiency > 2, (
                    f"Should have at least 2x efficiency, got {efficiency:.1f}x"
                )

    def test_error_handling(self):
        # Test invalid inputs
        with pytest.raises(ValueError, match="n_level must be non-negative"):
            doe_sparse_grid(-1, 2)

        with pytest.raises(ValueError, match="n_factors must be positive"):
            doe_sparse_grid(2, 0)

    def test_reproducibility(self):
        level, dims = 3, 2

        design1 = doe_sparse_grid(level, dims)
        design2 = doe_sparse_grid(level, dims)

        np.testing.assert_array_equal(design1, design2)
