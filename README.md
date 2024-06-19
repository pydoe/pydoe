pyDOE: An experimental design package for python
=================================================

[![Tests](https://github.com/relf/pyDOE3/actions/workflows/tests.yml/badge.svg)](https://github.com/relf/pyDOE3/actions/workflows/tests.yml)
[![Documentation](https://readthedocs.org/projects/pydoe3/badge/?version=latest)](https://pydoe3.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/709347557.svg)](https://zenodo.org/doi/10.5281/zenodo.10958492)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

`pyDOE` is a package that is designed to help the scientist, engineer,
statistician, etc., to construct appropriate experimental designs.

Capabilities
------------

The package currently includes functions for creating designs for any
number of factors:

- Factorial Designs
  - General Full-Factorial (``fullfact``)
  - 2-level Full-Factorial (``ff2n``)
  - 2-level Fractional Factorial (``fracfact``)
  - Plackett-Burman (``pbdesign``)
  - Generalized Subset Designs (``gsd``)
- Response-Surface Designs 
  - Box-Behnken (``bbdesign``)
  - Central-Composite (``ccdesign``)
- Randomized Designs
  - Latin-Hypercube (``lhs``)

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
- [Latin-Hypercube designs](http://en.wikipedia.org/wiki/Latin_hypercube_sampling)
- Surowiec, Izabella, Ludvig Vikström, Gustaf Hector, Erik Johansson,
Conny Vikström, and Johan Trygg. “Generalized Subset Designs in Analytical
Chemistry.” Analytical Chemistry 89, no. 12 (June 20, 2017): 6491–97.
<https://doi.org/10.1021/acs.analchem.7b00506>.
