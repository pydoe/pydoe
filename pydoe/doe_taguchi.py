"""
Inspired by Taguchi design methodology and orthogonal arrays
developed by Genichi Taguchi, this code provides utilities for
generating Taguchi arrays, building experimental designs, and
computing Signal-to-Noise Ratios, based on orthogonal array libraries.

Sources of orthogonal arrays:

    - University of York, Department of Mathematics:
      https://www.york.ac.uk/depts/maths/tables/orthogonal.htm
    - A Library of Orthogonal Arrays by N. J. A. Sloane:
      https://neilsloane.com/oadir/

References:
    - Taguchi G., Chowdhury S., Wu Y. (2005). "Taguchi's Quality Engineering
    Handbook." Wiley.
    - Montgomery D. C. (2017). "Design and Analysis of Experiments." Wiley.
    - [What are Taguchi designs?](https://www.itl.nist.gov/div898/handbook/pri/section5/pri56.htm)
"""

from __future__ import annotations

from enum import Enum, unique
from typing import Literal

import numpy as np

from pydoe.orthogonal_arrays import ORTHOGONAL_ARRAYS


__all__ = [
    "TaguchiObjective",
    "compute_snr",
    "get_orthogonal_array",
    "list_orthogonal_arrays",
    "taguchi_design",
]

ORTHOGONAL_ARRAY_NAMES = Literal[
    "L4(2^3)",
    "L8(2^7)",
    "L9(3^4)",
    "L12(2^11)",
    "L16(2^15)",
    "L16(4^5)",
    "L18(6^1 3^6)",
    "L25(5^6)",
    "L27(2^1 3^12)",
    "L32(2^31)",
    "L32(2^1 4^9)",
    "L36(3^23)",
    "L50(2^1 5^11)",
    "L54(2^1 3^25)",
    "L64(2^31)",
    "L64(4^21)",
    "L81(3^40)",
]


def get_orthogonal_array(oa_name: ORTHOGONAL_ARRAY_NAMES) -> np.ndarray:
    """
    Return a Taguchi orthogonal array by its descriptive name.

    Parameters
    ----------
    oa_name : OAName
        Name of the array, e.g., 'L4(2^3)', 'L8(2^7)', 'L9(3^4)', etc.

    Returns
    -------
    np.ndarray
        The orthogonal array (zero-indexed factor levels).

    Raises
    ------
    ValueError
        If the array name is not found.
    """
    if oa_name not in ORTHOGONAL_ARRAYS:
        raise ValueError(
            f"Orthogonal array '{oa_name}' not found. "
            f"Available: {list(ORTHOGONAL_ARRAYS.keys())}"
        )
    return ORTHOGONAL_ARRAYS[oa_name]


def list_orthogonal_arrays() -> list[str]:
    """
    List descriptive names of available Taguchi orthogonal arrays.

    Returns
    -------
    list of str
        List of array names, e.g., ['L4(2^3)', 'L8(2^7)', 'L9(3^4)', ...].
    """
    return list(ORTHOGONAL_ARRAYS.keys())


def taguchi_design(
    oa_name: ORTHOGONAL_ARRAY_NAMES, levels_per_factor: list[list]
) -> np.ndarray:
    """
    Generate a Taguchi design matrix using an orthogonal array and
    factor levels.

    Parameters
    ----------
    oa_name : OAName
        Name of Taguchi orthogonal array, e.g., 'L4(2^3)', 'L9(3^4)', etc.
    levels_per_factor : list of lists
        Each inner list defines actual levels/settings for each factor.
        Length must match number of columns in the orthogonal array.

    Returns
    -------
    np.ndarray
        Design matrix with actual factor settings (not coded levels).

    Raises
    ------
    ValueError
        If number of levels does not match number of factors.
    """
    array = get_orthogonal_array(oa_name)
    n_factors = array.shape[1]

    if len(levels_per_factor) != n_factors:
        raise ValueError(
            f"Number of factors in array ({n_factors}) does not match "
            f"number of levels_per_factor provided ({len(levels_per_factor)})."
        )

    design_matrix = np.empty_like(array, dtype=object)

    for i, levels in enumerate(levels_per_factor):
        design_matrix[:, i] = [levels[level] for level in array[:, i]]

    return design_matrix


@unique
class TaguchiObjective(Enum):
    """
    Enumeration for Taguchi optimization objectives when calculating SNR.
    """

    LARGER_IS_BETTER = "larger is better"
    SMALLER_IS_BETTER = "smaller is better"
    NOMINAL_IS_BEST = "nominal is best"


def compute_snr(
    responses: np.ndarray,
    objective: TaguchiObjective = TaguchiObjective.LARGER_IS_BETTER,
) -> float:
    """
    Calculate the Signal-to-Noise Ratio (SNR) for Taguchi designs.

    Parameters
    ----------
    responses : array-like
        Repeated measurements for a single trial (1D array).
    objective : TaguchiObjective
        Optimization goal, one of: LARGER, SMALLER, NOMINAL.

    Returns
    -------
    float
        SNR value in decibels (dB).

    Raises
    ------
    ValueError
        If the objective is not recognized.
    """
    responses = np.asarray(responses)

    if objective == TaguchiObjective.LARGER_IS_BETTER:
        snr = -10 * np.log10(np.mean(1.0 / responses**2))
    elif objective == TaguchiObjective.SMALLER_IS_BETTER:
        snr = -10 * np.log10(np.mean(responses**2))
    elif objective == TaguchiObjective.NOMINAL_IS_BEST:
        mean_y = np.mean(responses)
        std_y = np.std(responses, ddof=1)
        snr = 10 * np.log10(mean_y**2 / std_y**2)
    else:
        raise ValueError("Invalid objective specified.")

    return snr
