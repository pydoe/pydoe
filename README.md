pyDOE: An experimental design package for python
=================================================

[![Tests](https://github.com/relf/pyDOE3/actions/workflows/tests.yml/badge.svg)](https://github.com/relf/pyDOE3/actions/workflows/tests.yml)
[![Documentation](https://readthedocs.org/projects/pydoe3/badge/?version=latest)](https://pydoe3.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/709347557.svg)](https://zenodo.org/doi/10.5281/zenodo.10958492)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This package is designed to help the scientist, engineer, statistician, etc., to
construct appropriate experimental designs.

Capabilities
------------

The package currently includes functions for creating designs for any
number of factors:

- **Factorial Designs**
  - General Full-Factorial (``fullfact``)
  - 2-level Full-Factorial (``ff2n``)
  - 2-level Fractional Factorial (``fracfact``)
  - Plackett-Burman (``pbdesign``)
  - Generalized Subset Designs (``gsd``)

- **Response-Surface Designs** 
  - Box-Behnken (``bbdesign``)
  - Central-Composite (``ccdesign``)
  - Doehlert Design (``doehlert_shell_design``, ``doehlert_simplex_design``)

- **Randomized Designs**
  - Latin-Hypercube (``lhs``)

- **Low-Discrepancy Sequences**
  - Sukharev Grid (``sukharev_grid``)
  - Sobol’ Sequence (``sobol_sequence``)
  - Halton Sequence (``halton_sequence``)
  - Rank-1 Lattice Design (``rank1_lattice``)
  - Korobov Sequence (``korobov_sequence``)
  - Cranley-Patterson Randomization (``cranley_patterson_shift``)

- **Taguchi Designs**
  - Orthogonal arrays and robust design utilities (``taguchi_design``, ``compute_snr``)
- **Optimal Designs**
  - Advanced optimal design algorithms (``optimal_design``)
  - Optimality criteria (``A``, ``C``, ``D``, ``E``, ``G``, ``I``, ``S``, ``T``, ``V``)
  - Search algorithms (``Sequential (Dykstra)``, ``Simple Exchange (Wynn-Mitchell)``, ``Fedorov``, ``Modified Fedorov``, ``DETMAX``)

See the original [pyDOE homepage](http://pythonhosted.org/pyDOE) for details
on usage and other notes.

Requirements
------------

- NumPy
- SciPy

Installation
------------

```bash
pip install pyDOE
```

Credits
-------

`pyDOE` original code was originally converted from code by the following
individuals for use with Scilab:

- Copyright (C) 2012-2013, Michael Baudin
- Copyright (C) 2012, Maria Christopoulou
- Copyright (C) 2010-2011, INRIA, Michael Baudin
- Copyright (C) 2009, Yann Collette
- Copyright (C) 2009, CEA, Jean-Marc Martinez

`pyDOE` was converted to Python by the following individual:

- Copyright (c) 2014 - Abraham D. Lee
- Copyright (C) 2018 - Rickard Sjögren and Daniel Svensson

License
-------

This package is provided under the *BSD License* (3-clause)

References
----------

- [Factorial designs](http://en.wikipedia.org/wiki/Factorial_experiment)
- [Plackett-Burman designs](http://en.wikipedia.org/wiki/Plackett-Burman_design)
- [Box-Behnken designs](http://en.wikipedia.org/wiki/Box-Behnken_design)
- [Central composite designs](http://en.wikipedia.org/wiki/Central_composite_design)
- [Doehlert Design](https://academic.oup.com/jrsssc/article/19/3/231/6882590)
- [Latin-Hypercube designs](http://en.wikipedia.org/wiki/Latin_hypercube_sampling)
- [Halton sequence](http://en.wikipedia.org/wiki/Halton_sequence)
- [Sobol sequence](http://en.wikipedia.org/wiki/Sobol_sequence)
- [Low-Discrepancy sequences](http://en.wikipedia.org/wiki/Low-discrepancy_sequence)
- [Taguchi designs](http://en.wikipedia.org/wiki/Taguchi_methods)
- [Generalized Subset Designs](https://doi.org/10.1021/acs.analchem.7b00506)
- [Optimal experimental design](https://en.wikipedia.org/wiki/Optimal_experimental_design)
