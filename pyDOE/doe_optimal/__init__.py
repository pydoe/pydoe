r"""
Optimal Experimental Design (OED)
=================================

This module implements various optimal design algorithms and optimality criteria
for design of experiments as described in theoretical literature.

Main Functions:
--------------
optimal_design : Generate optimal designs
generate_candidate_set : Generate candidate points for design space

Algorithms:
----------
- Sequential (Dykstra)
- Simple Exchange (Wynn-Mitchell)
- Fedorov
- Modified Fedorov
- DETMAX

Optimality Criteria:
-------------------
- D-optimality (determinant)
- A-optimality (average/trace)
- I-optimality (integrated prediction variance)
- C-optimality (linear combination of parameters)
- E-optimality (eigenvalue)
- G-optimality (maximum prediction variance)
- V-optimality (variance at specific points)
- S-optimality (mutual orthogonality)
- T-optimality (model discrimination)

After an optimal design is selected and experiments are performed,
we can model our system by estimating the regression parameters using:

$$\hat{\beta} = (X^{T}X)^{-1}X^{T}y$$

Example:
--------
>>> import numpy as np
>>> from pyDOE.doe_optimal import optimal_design, generate_candidate_set
>>>
>>> # Generate candidate set
>>> candidates = generate_candidate_set(n_factors=2, n_levels=5)
>>>
>>> # Create optimal design
>>> design, info = optimal_design(
...     candidates=candidates,
...     n_points=10,
...     degree=2,
...     criterion="D",
...     method="detmax"
... )
"""

from pyDOE.doe_optimal.optimal import optimal_design
from pyDOE.doe_optimal.model import (
    build_design_matrix,
    build_uniform_moment_matrix,
    generate_candidate_set,
)
from pyDOE.doe_optimal.algorithms import (
    sequential_dykstra,
    simple_exchange_wynn_mitchell,
    fedorov,
    modified_fedorov,
    detmax,
)
from pyDOE.doe_optimal.criterion import (
    d_optimality,
    a_optimality,
    i_optimality,
    c_optimality,
    e_optimality,
    g_optimality,
    v_optimality,
    s_optimality,
    t_optimality,
)
from pyDOE.doe_optimal.efficiency import d_efficiency, a_efficiency
from pyDOE.doe_optimal.utils import information_matrix, criterion_value

__author__ = "Saud Zahir"

__all__ = [
    # Main functions
    "optimal_design",
    "generate_candidate_set",
    # Model building
    "build_design_matrix",
    "build_uniform_moment_matrix",
    # Algorithms
    "sequential_dykstra",
    "simple_exchange_wynn_mitchell",
    "fedorov",
    "modified_fedorov",
    "detmax",
    # Optimality criteria
    "d_optimality",
    "a_optimality",
    "i_optimality",
    "c_optimality",
    "e_optimality",
    "g_optimality",
    "v_optimality",
    "s_optimality",
    "t_optimality",
    # Efficiency measures
    "d_efficiency",
    "a_efficiency",
    # Utilities
    "information_matrix",
    "criterion_value",
]
