import numpy as np
import pytest

from pydoe.doe_sparse_grid import doe_sparse_grid, sparse_grid_dimension


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
        expected_count = 13  # MATLAB verified

        grid_types = ["clenshaw_curtis", "chebyshev", "gauss_patterson"]

        for grid_type in grid_types:
            design = doe_sparse_grid(level, dims, grid_type=grid_type)
            assert len(design) == expected_count, (
                f"{grid_type} should produce {expected_count} points"
            )
            assert design.shape[1] == dims
            assert np.all(design >= 0.0) and np.all(design <= 1.0)

    def test_grid_types(self):
        level, dims = 2, 3
        expected_count = 25  # MATLAB verified

        # Test Clenshaw-Curtis grid type
        design_cc = doe_sparse_grid(level, dims, grid_type="clenshaw_curtis")
        assert len(design_cc) == expected_count

        # Test Chebyshev grid type
        design_cheb = doe_sparse_grid(level, dims, grid_type="chebyshev")
        assert len(design_cheb) == expected_count

        # Test Gauss-Patterson grid type
        design_gp = doe_sparse_grid(level, dims, grid_type="gauss_patterson")
        assert len(design_gp) == expected_count

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
