Inspired by Taguchi design methodology and the orthogonal arrays developed by Genichi Taguchi, this module provides utilities for generating Taguchi experimental designs and computing Signal-to-Noise Ratios (SNR), based on a library of orthogonal arrays.

Taguchi designs allow for systematic exploration of factor effects using a minimal number of experiments, offering a robust alternative to full factorial designs.

Sources of orthogonal arrays:

- [University of York Orthogonal Arrays](https://www.york.ac.uk/depts/maths/tables/orthogonal.htm)
- [A Library of Orthogonal Arrays by N. J. A. Sloane](https://neilsloane.com/oadir/)

## References

- Taguchi G., Chowdhury S., Wu Y. (2005). *Taguchi's Quality Engineering Handbook*. Wiley.
- Montgomery D. C. (2017). *Design and Analysis of Experiments*. Wiley.
- [What are Taguchi designs?](https://www.itl.nist.gov/div898/handbook/pri/section5/pri56.htm)

!!! hint
    All functions are available after importing:

    ```python
    >>> from pydoe import (list_orthogonal_arrays, get_orthogonal_array,
    ...     taguchi_design, compute_snr, TaguchiObjective)
    ```

## Available Orthogonal Arrays

You can list all available Taguchi orthogonal arrays:

```python
>>> list_orthogonal_arrays()
['L4(2^3)', 'L8(2^7)', 'L9(3^4)', 'L12(2^11)', 'L16(2^15)', ...]
```

Each array is described using notation like "$L_9(3^4)$", meaning an array with 9 runs and 4 factors each at 3 levels.

## Retrieving an Orthogonal Array

Get a numeric orthogonal array by name:

```python
>>> get_orthogonal_array('L4(2^3)')
array([[0, 0, 0],
       [0, 1, 1],
       [1, 0, 1],
       [1, 1, 0]])
```

The arrays use zero-indexed factor levels.

## Generating a Taguchi Design Matrix

Generate a concrete experimental matrix using factor levels:

```python
>>> levels = [
...     ["Low", "High"], # Factor 1
...     ["A"  , "B"   ], # Factor 2
...     [10   , 20    ], # Factor 3
... ]
>>> taguchi_design('L4(2^3)', levels)
array([['Low', 'A', 10],
       ['Low', 'B', 20],
       ['High', 'A', 20],
       ['High', 'B', 10]], dtype=object)
```

The design matrix replaces coded levels with actual settings for each factor.

## Signal-to-Noise Ratio (SNR)

Taguchi designs often focus on improving robustness, measured using the Signal-to-Noise Ratio (SNR).

Three objectives are supported:

- `LARGER_IS_BETTER`
- `SMALLER_IS_BETTER`
- `NOMINAL_IS_BEST`

Compute SNR for repeated measurements from one trial:

```python
>>> responses = np.array([90, 95, 93])
>>> compute_snr(responses, objective=TaguchiObjective.LARGER_IS_BETTER)
39.133...
```

SNR values are returned in decibels (dB).

!!! note
    `compute_snr` uses logarithmic transformations and assumes the responses are positive for `LARGER_IS_BETTER` and `SMALLER_IS_BETTER`.

## Enum for Objective

The optimization objective is specified using the enumeration `TaguchiObjective`:

```python
>>> TaguchiObjective.LARGER_IS_BETTER
<TaguchiObjective.LARGER_IS_BETTER: 'larger is better'>
```

## Summary

The Taguchi design utilities allow you to:

- Retrieve orthogonal arrays by name.
- Build concrete design matrices with specified factor levels.
- Evaluate robustness using Signal-to-Noise Ratios.

For more details, see:

- [NIST Engineering Statistics Handbook - Taguchi Designs](https://www.itl.nist.gov/div898/handbook/pri/section5/pri56.htm)
