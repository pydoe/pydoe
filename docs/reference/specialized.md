In this section, the following specialized designs are described:

- [Definitive Screening Design](#definitive-screening-design-definitive_screening_design)
- [Supersaturated Design](#supersaturated-design-supersaturated_design)

!!! note
    All available designs can be accessed after a simple import statement:
    ```pycon
    >>> from pydoe import definitive_screening_design, supersaturated_design
    ```

## Definitive Screening Design (`definitive_screening_design`) {#definitive-screening-design-definitive_screening_design}

A **definitive screening design** (Jones & Nachtsheim, 2011) is a
three-level design for *k* factors requiring only $2k + 1$ runs that
estimates all main effects independent of two-factor interactions and
of each other, estimates all quadratic effects, and keeps two-factor
interactions clear of main effects.

```pycon
>>> definitive_screening_design(k)  # (1)!
```

1. `k` — number of factors. `k - 1` must be an odd prime (e.g. `k` =
   4, 6, 8, 12, 14, 18, 20, 24, ...).

```pycon
>>> definitive_screening_design(4)
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  1.,  1.,  1.],
       [-1.,  0.,  1., -1.],
       [-1., -1.,  0.,  1.],
       [-1.,  1., -1.,  0.],
       [ 0., -1., -1., -1.],
       [ 1.,  0., -1.,  1.],
       [ 1.,  1.,  0., -1.],
       [ 1., -1.,  1.,  0.]])
```

!!! note
    The design is built from a Paley conference matrix $C$ of order $k$
    as $D = [0; C; -C]$, stacking the all-zero center run on top of $C$
    and its fold-over $-C$.

## Supersaturated Design (`supersaturated_design`) {#supersaturated-design-supersaturated_design}

A **supersaturated design** has more two-level factors than runs
($k > n$). It cannot estimate all main effects simultaneously, but is
useful for screening when only a small fraction of factors are
expected to be active. `supersaturated_design` performs a random
search to minimize $E(s^2)$, the average squared off-diagonal element
of $X^T X$.

```pycon
>>> supersaturated_design(n_factors, n_runs, iterations=1000, seed=None)  # (1)!
```

1. `n_factors` — number of two-level factors $k$ (must exceed
   `n_runs`). `n_runs` — number of runs $n$ (≥ 2). `iterations` —
   number of random candidates to evaluate. `seed` — for
   reproducibility.

```pycon
>>> supersaturated_design(6, 4, iterations=200, seed=0)
array([[-1.,  1.,  1., -1., -1.,  1.],
       [ 1.,  1., -1.,  1.,  1.,  1.],
       [ 1.,  1.,  1., -1.,  1., -1.],
       [ 1.,  1.,  1.,  1., -1., -1.]])
```

!!! note
    Smaller $E(s^2)$ values indicate lower average correlation between
    factor columns, allowing cleaner estimation of the active effects
    under effect sparsity.

## More Information

For further reading, see:

- Jones, B., & Nachtsheim, C. J. (2011). A class of three-level designs
  for definitive screening in the presence of second-order effects.
  *Journal of Quality Technology*, 43(1), 1-15.
- Xiao, L., Lin, D. K. J., & Bai, F. (2012). Constructing definitive
  screening designs using conference matrices. *Journal of Quality
  Technology*, 44(1), 2-8.
- Lin, D. K. J. (1993). A new class of supersaturated designs.
  *Technometrics*, 35(1), 28-31.
- [NIST Handbook Section 5.3.3.4 — Supersaturated Designs](https://www.itl.nist.gov/div898/handbook/pri/section3/pri334.htm)
