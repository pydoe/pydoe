"""
`pyDOE` original code was originally converted from code by the following
individuals for use with Scilab:

- Copyright (C) 2012-2013, Michael Baudin
- Copyright (C) 2012, Maria Christopoulou
- Copyright (C) 2010-2011, INRIA, Michael Baudin
- Copyright (C) 2009, Yann Collette
- Copyright (C) 2009, CEA, Jean-Marc Martinez

`pyDOE` was converted to Python by the following individual:

- Copyright (c) 2014, Abraham D. Lee

The following individuals forked `pyDOE` and worked on `pyDOE2`:

- Copyright (C) 2018, Rickard Sjögren and Daniel Svensson

The following individuals forked `pyDOE2` and worked on `pyDOE3`:

- Copyright (C) 2023 - Rémi Lafage
"""

from importlib.metadata import PackageNotFoundError, version

from pyDOE.doe_box_behnken import bbdesign
from pyDOE.doe_composite import ccdesign
from pyDOE.doe_cranley_patterson_shift import cranley_patterson_shift
from pyDOE.doe_doehlert import doehlert_shell_design, doehlert_simplex_design
from pyDOE.doe_factorial import (
    alias_vector_indices,
    ff2n,
    fracfact,
    fracfact_aliasing,
    fracfact_by_res,
    fracfact_opt,
    fullfact,
)
from pyDOE.doe_fold import fold
from pyDOE.doe_gsd import gsd
from pyDOE.doe_halton import halton_sequence
from pyDOE.doe_korobov import korobov_sequence
from pyDOE.doe_lhs import lhs
from pyDOE.doe_plackett_burman import pbdesign
from pyDOE.doe_random_k_means import random_k_means
from pyDOE.doe_random_uniform import random_uniform
from pyDOE.doe_rank1 import rank1_lattice
from pyDOE.doe_saltelli import saltelli_sampling
from pyDOE.doe_sobol import sobol_sequence
from pyDOE.doe_sparse_grid import (
    doe_sparse_grid,
    sparse_grid_dimension,
)
from pyDOE.doe_taguchi import (
    TaguchiObjective,
    compute_snr,
    get_orthogonal_array,
    list_orthogonal_arrays,
    taguchi_design,
)
from pyDOE.doe_vanilla_morris import morris_sampling
from pyDOE.grid_designs import sukharev_grid
from pyDOE.utils import scale_samples
from pyDOE.var_regression_matrix import var_regression_matrix

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "bbdesign",
    "ccdesign",
    "fullfact",
    "ff2n",
    "fracfact",
    "fracfact_by_res",
    "fracfact_opt",
    "fracfact_aliasing",
    "alias_vector_indices",
    "lhs",
    "fold",
    "pbdesign",
    "var_regression_matrix",
    "gsd",
    "taguchi_design",
    "TaguchiObjective",
    "compute_snr",
    "list_orthogonal_arrays",
    "get_orthogonal_array",
    "doehlert_shell_design",
    "doehlert_simplex_design",
    "sukharev_grid",
    "cranley_patterson_shift",
    "halton_sequence",
    "sobol_sequence",
    "rank1_lattice",
    "korobov_sequence",
    "random_k_means",
    "random_uniform",
    "morris_sampling",
    "saltelli_sampling",
    "scale_samples",
    "doe_sparse_grid",
    "sparse_grid_dimension",
]
