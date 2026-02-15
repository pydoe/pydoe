"""
`PyDOE` original code was originally converted from code by the following
individuals for use with Scilab:

- Copyright (C) 2012-2013, Michael Baudin
- Copyright (C) 2012, Maria Christopoulou
- Copyright (C) 2010-2011, INRIA, Michael Baudin
- Copyright (C) 2009, Yann Collette
- Copyright (C) 2009, CEA, Jean-Marc Martinez

`PyDOE` was converted to Python by the following individual:

- Copyright (c) 2014, Abraham D. Lee

The following individuals forked `PyDOE` and worked on `PyDOE2`:

- Copyright (C) 2018, Rickard Sjögren and Daniel Svensson

The following individuals forked `PyDOE2` and worked on `PyDOE3`:

- Copyright (C) 2023 - Rémi Lafage
"""

from importlib.metadata import PackageNotFoundError, version

from .clustering import random_k_means
from .factorial import (
    alias_vector_indices,
    ff2n,
    fold,
    fracfact,
    fracfact_aliasing,
    fracfact_by_res,
    fracfact_opt,
    fullfact,
    gsd,
    pbdesign,
)
from .optimal import (
    a_efficiency,
    a_optimality,
    build_design_matrix,
    build_uniform_moment_matrix,
    c_optimality,
    criterion_value,
    d_efficiency,
    d_optimality,
    detmax,
    e_optimality,
    fedorov,
    g_optimality,
    generate_candidate_set,
    i_optimality,
    information_matrix,
    modified_fedorov,
    optimal_design,
    s_optimality,
    sequential_dykstra,
    simple_exchange_wynn_mitchell,
    t_optimality,
    v_optimality,
)
from .response_surface import (
    bbdesign,
    ccdesign,
    doehlert_shell_design,
    doehlert_simplex_design,
    repeat_center,
    star,
    union,
)
from .sensitivity_analysis import morris_sampling, saltelli_sampling
from .space_filling.quasi_random import (
    cranley_patterson_shift,
    halton_sequence,
    korobov_sequence,
    rank1_lattice,
    sobol_sequence,
    sukharev_grid,
)
from .space_filling.stochastic import lhs, random_uniform
from .sparse_grid import doe_sparse_grid, sparse_grid_dimension
from .taguchi import (
    TaguchiObjective,
    compute_snr,
    get_orthogonal_array,
    list_orthogonal_arrays,
    taguchi_design,
)
from .utils import scale_samples, var_regression_matrix


try:  # noqa: RUF067
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "TaguchiObjective",
    "a_efficiency",
    "a_optimality",
    "alias_vector_indices",
    "bbdesign",
    "build_design_matrix",
    "build_uniform_moment_matrix",
    "c_optimality",
    "ccdesign",
    "compute_snr",
    "cranley_patterson_shift",
    "criterion_value",
    "d_efficiency",
    "d_optimality",
    "detmax",
    "doe_sparse_grid",
    "doehlert_shell_design",
    "doehlert_simplex_design",
    "e_optimality",
    "fedorov",
    "ff2n",
    "fold",
    "fracfact",
    "fracfact_aliasing",
    "fracfact_by_res",
    "fracfact_opt",
    "fullfact",
    "g_optimality",
    "generate_candidate_set",
    "get_orthogonal_array",
    "gsd",
    "halton_sequence",
    "i_optimality",
    "information_matrix",
    "korobov_sequence",
    "lhs",
    "list_orthogonal_arrays",
    "modified_fedorov",
    "morris_sampling",
    "optimal_design",
    "pbdesign",
    "random_k_means",
    "random_uniform",
    "rank1_lattice",
    "repeat_center",
    "s_optimality",
    "saltelli_sampling",
    "scale_samples",
    "sequential_dykstra",
    "simple_exchange_wynn_mitchell",
    "sobol_sequence",
    "sparse_grid_dimension",
    "star",
    "sukharev_grid",
    "t_optimality",
    "taguchi_design",
    "union",
    "v_optimality",
    "var_regression_matrix",
]
