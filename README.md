pyDOE: An experimental design package for python
=====================================================

`pyDOE` is a fork of the [`pyDOE`](https://github.com/tisimst/pyDOE) package 
that is designed to help the scientist, engineer, statistician, etc., to 
construct appropriate experimental designs.

This fork came to life to solve bugs and issues that remained unsolved in the
original package.

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

What's new?
----------

### Generalized Subset Designs

In pyDOE the [Generalized Subset Design (GSD)](https://doi.org/10.1021/acs.analchem.7b00506)
is introduced. GSD is a generalization of traditional fractional factorial
designs to problems where factors can have more than two levels.

In many application problems, factors can have categorical or quantitative
factors on more than two levels. Previous reduced designs have not been
able to deal with such types of problems. Full multi-level factorial
designs can handle such problems but are however not economical regarding
the number of experiments.

The GSD provide balanced designs in multi-level experiments with the number
of experiments reduced by a user-specified reduction factor. Complementary
reduced designs are also provided analogous to fold-over in traditional
fractional factorial designs.

GSD is available in pyDOE as:

```
import pyDOE

levels = [2, 3, 4]  # Three factors with 2, 3 or 4 levels respectively.
reduction = 3       # Reduce the number of experiments to approximately a third.

pyDOE.gsd(levels, reduction)
```


Requirements
------------

- NumPy
- SciPy

Installation and download
-------------------------

Through pip:

```
pip install pyDOE
```


Credits
-------

`pyDOE` original code was originally converted from code by the following 
individuals for use with Scilab:
    
- Copyright (C) 2012 - 2013 - Michael Baudin
- Copyright (C) 2012 - Maria Christopoulou
- Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
- Copyright (C) 2009 - Yann Collette
- Copyright (C) 2009 - CEA - Jean-Marc Martinez

- Website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

`pyDOE` was converted to Python by the following individual:

- Copyright (c) 2014, Abraham D. Lee

The following individuals forked and work on `pyDOE`:

- Copyright (C) 2018 - Rickard Sjögren and Daniel Svensson


License
-------

This package is provided under two licenses:

1. The *BSD License* (3-clause)
2. Any other that the author approves (just ask!)

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
https://doi.org/10.1021/acs.analchem.7b00506.
