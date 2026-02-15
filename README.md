PyDOE: An Experimental Design Package for Python
================================================

[![Tests](https://github.com/pydoe/pydoe/actions/workflows/code_test.yml/badge.svg)](https://github.com/pydoe/pydoe/actions/workflows/code_test.yml)
[![Documentation](https://github.com/pydoe/pydoe/actions/workflows/docs_build.yml/badge.svg)](https://github.com/pydoe/pydoe/actions/workflows/docs_build.yml)
[![DOI](https://zenodo.org/badge/709347557.svg)](https://zenodo.org/doi/10.5281/zenodo.10958492)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![Stack Overflow](https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg)](
https://stackoverflow.com/questions/tagged/pydoe)
[![codecov](https://codecov.io/gh/pydoe/pydoe/branch/master/graph/badge.svg)](https://codecov.io/gh/pydoe/pydoe)
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](./LICENSE)

[![PyPI Downloads](https://img.shields.io/pypi/dm/pydoe.svg?label=PyPI%20downloads)](https://pypi.org/project/pydoe/)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pydoe.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/pydoe)
[![Python versions](https://img.shields.io/pypi/pyversions/pydoe.svg)](https://pypi.org/project/pydoe/)

PyDOE is a Python package for design of experiments (DOE), enabling scientists, engineers, and statisticians to efficiently construct experimental designs.

- **Website:** https://pydoe.github.io/pydoe/
- **Documentation:** https://pydoe.github.io/pydoe/reference/factorial/
- **Source code:** https://github.com/pydoe/pydoe
- **Contributing:** https://pydoe.github.io/pydoe/contributing/
- **Bug reports:** https://github.com/pydoe/pydoe/issues


Overview
--------

The package provides extensive support for design-of-experiments (DOE) methods and is capable of creating designs for any number of factors.

It provides:

- **Factorial Designs**
  - General Full-Factorial (``fullfact``)
  - 2-level Full-Factorial (``ff2n``)
  - 2-level Fractional Factorial (``fracfact``, ``fracfact_aliasing``, ``fracfact_by_res``, ``fracfact_opt``, ``alias_vector_indices``)
  - Plackett-Burman (``pbdesign``)
  - Generalized Subset Designs (``gsd``)
  - Fold-over Designs (``fold``)

- **Response-Surface Designs**
  - Box-Behnken (``bbdesign``)
  - Central-Composite (``ccdesign``)
  - Doehlert Design (``doehlert_shell_design``, ``doehlert_simplex_design``)
  - Star Designs (``star``)
  - Union Designs (``union``)
  - Repeated Center Points (``repeat_center``)

- **Space-Filling Designs**
  - Latin-Hypercube (``lhs``)
  - Random Uniform (``random_uniform``)

- **Low-Discrepancy Sequences**
  - Sukharev Grid (``sukharev_grid``)
  - Sobol’ Sequence (``sobol_sequence``)
  - Halton Sequence (``halton_sequence``)
  - Rank-1 Lattice Design (``rank1_lattice``)
  - Korobov Sequence (``korobov_sequence``)
  - Cranley-Patterson Randomization (``cranley_patterson_shift``)

- **Clustering Designs**
  - Random K-Means (``random_k_means``)

- **Sensitivity Analysis Designs**
  - Morris Method (``morris_sampling``)
  - Saltelli Sampling (``saltelli_sampling``)

- **Taguchi Designs**
  - Orthogonal arrays and robust design utilities (``taguchi_design``, ``compute_snr``, ``get_orthogonal_array``, ``list_orthogonal_arrays``, ``TaguchiObjective``)

- **Optimal Designs**
  - Advanced optimal design algorithms (``optimal_design``)
  - Optimality criteria (``a_optimality``, ``c_optimality``, ``d_optimality``, ``e_optimality``, ``g_optimality``, ``i_optimality``, ``s_optimality``, ``t_optimality``, ``v_optimality``)
  - Efficiency measures (``a_efficiency``, ``d_efficiency``)
  - Search algorithms (``sequential_dykstra``, ``simple_exchange_wynn_mitchell``, ``fedorov``, ``modified_fedorov``, ``detmax``)
  - Design utilities (``criterion_value``, ``information_matrix``, ``build_design_matrix``, ``build_uniform_moment_matrix``, ``generate_candidate_set``)

- **Sparse Grid Designs**
  - Sparse Grid Design (``doe_sparse_grid``)
  - Sparse Grid Dimension (``sparse_grid_dimension``)

Installation
------------

```bash
pip install pydoe
```

Credits
-------
For more info see: https://pydoe.github.io/pydoe/credits/

License
-------

This package is provided under the *BSD License* (3-clause)
