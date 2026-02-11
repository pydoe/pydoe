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

from pydoe.doe_box_behnken import bbdesign
from pydoe.doe_composite import ccdesign
from pydoe.doe_cranley_patterson_shift import cranley_patterson_shift
from pydoe.doe_doehlert import doehlert_shell_design, doehlert_simplex_design
from pydoe.doe_factorial import (
    alias_vector_indices,
    ff2n,
    fracfact,
    fracfact_aliasing,
    fracfact_by_res,
    fracfact_opt,
    fullfact,
)
from pydoe.doe_fold import fold
from pydoe.doe_gsd import gsd
from pydoe.doe_halton import halton_sequence
from pydoe.doe_korobov import korobov_sequence
from pydoe.doe_lhs import lhs
from pydoe.doe_plackett_burman import pbdesign
from pydoe.doe_random_k_means import random_k_means
from pydoe.doe_random_uniform import random_uniform
from pydoe.doe_rank1 import rank1_lattice
from pydoe.doe_saltelli import saltelli_sampling
from pydoe.doe_sobol import sobol_sequence
from pydoe.doe_sparse_grid import doe_sparse_grid, sparse_grid_dimension
from pydoe.doe_taguchi import (
    TaguchiObjective,
    compute_snr,
    get_orthogonal_array,
    list_orthogonal_arrays,
    taguchi_design,
)
from pydoe.doe_vanilla_morris import morris_sampling
from pydoe.grid_designs import sukharev_grid
from pydoe.utils import scale_samples
from pydoe.var_regression_matrix import var_regression_matrix


try:  # noqa: RUF067
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "TaguchiObjective",
    "alias_vector_indices",
    "bbdesign",
    "ccdesign",
    "compute_snr",
    "cranley_patterson_shift",
    "doe_sparse_grid",
    "doehlert_shell_design",
    "doehlert_simplex_design",
    "ff2n",
    "fold",
    "fracfact",
    "fracfact_aliasing",
    "fracfact_by_res",
    "fracfact_opt",
    "fullfact",
    "get_orthogonal_array",
    "gsd",
    "halton_sequence",
    "korobov_sequence",
    "lhs",
    "list_orthogonal_arrays",
    "morris_sampling",
    "pbdesign",
    "random_k_means",
    "random_uniform",
    "rank1_lattice",
    "saltelli_sampling",
    "scale_samples",
    "sobol_sequence",
    "sparse_grid_dimension",
    "sukharev_grid",
    "taguchi_design",
    "var_regression_matrix",
]
