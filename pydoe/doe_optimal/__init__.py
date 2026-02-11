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

Examples
--------
>>> import numpy as np
>>> from pydoe.doe_optimal import optimal_design, generate_candidate_set
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
...     method="detmax",
... )
"""

from pydoe.doe_optimal.algorithms import (
    detmax,
    fedorov,
    modified_fedorov,
    sequential_dykstra,
    simple_exchange_wynn_mitchell,
)
from pydoe.doe_optimal.criterion import (
    a_optimality,
    c_optimality,
    d_optimality,
    e_optimality,
    g_optimality,
    i_optimality,
    s_optimality,
    t_optimality,
    v_optimality,
)
from pydoe.doe_optimal.efficiency import a_efficiency, d_efficiency
from pydoe.doe_optimal.model import (
    build_design_matrix,
    build_uniform_moment_matrix,
    generate_candidate_set,
)
from pydoe.doe_optimal.optimal import optimal_design
from pydoe.doe_optimal.utils import criterion_value, information_matrix


__author__ = "Saud Zahir"

__all__ = [
    "a_efficiency",
    "a_optimality",
    # Model building
    "build_design_matrix",
    "build_uniform_moment_matrix",
    "c_optimality",
    "criterion_value",
    # Efficiency measures
    "d_efficiency",
    # Optimality criteria
    "d_optimality",
    "detmax",
    "e_optimality",
    "fedorov",
    "g_optimality",
    "generate_candidate_set",
    "i_optimality",
    # Utilities
    "information_matrix",
    "modified_fedorov",
    # Main functions
    "optimal_design",
    "s_optimality",
    # Algorithms
    "sequential_dykstra",
    "simple_exchange_wynn_mitchell",
    "t_optimality",
    "v_optimality",
]
