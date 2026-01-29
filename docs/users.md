# Who uses PyDOE?

PyDOE is a widely used Python library for *design of experiments (DOE)*. Its users range from individual researchers to global organizations, spanning academia, industry, and open-source projects. It supports applications in simulation-based optimization, engineering workflows, scientific research, and data-driven model development.

**Selected Testimonials**  
Below are some small selection of the many institutes and companies that use PyDOE.


[![NASA](./assets/images/nasa.png)](https://www.nasa.gov/)  
**GlennOPT** is a Python optimization tool developed by NASA for multi-objective optimization of engineering simulations (e.g., CFD problems). It uses evolutionary strategies (like Differential Evolution and NSGA methods) to explore design spaces, handle simulation failures, and restart long-running jobs robustly. It’s designed to track evaluations and integrate with external simulation workflows. It uses *PyDOE* to generate design-of-experiments samples for multi-objective simulation-based optimization.
> Source: <a href="https://github.com/nasa/GlennOPT" style="color: #484848;">github.com/nasa/GlennOPT</a>

<br>

[![IBM](./assets/images/IBM.png)](https://www.ibm.com/)  
IBM's **SimulAI** is a Python toolkit for *physics-informed machine learning*, combining models like Physics-Informed Neural Networks (PINNs), DeepONets, autoencoders, etc., for scientific computing and reduced-order modeling. It’s intended to unify state-of-the-art ML techniques for physical systems.
> Source: <a href="https://github.com/ibm/simulai" style="color: #484848;">github.com/ibm/simulai</a>

<br>

[![NANOGrav](./assets/images/NANOGrav.png)](https://nanograv.org/)  
**Holodeck** is an astrophysics software package developed by NANOGrav for *massive black-hole binary population synthesis* and for generating synthetic populations of supermassive black hole binaries for gravitational-wave background studies and related analyses.
> Source: <a href="https://github.com/nanograv/holodeck" style="color: #484848;">github.com/nanograv/holodeck</a>

<br>

[![TerraPower](./assets/images/TerraPower.png)](https://www.terrapower.com/)  
**ARMI** (**A**utomated **R**eactor **M**odeling **I**nfrastructure) is Terrapower’s Python framework for simulation and analysis of nuclear reactors’ core physics, including fuel performance and neutronics modeling. It builds complex reactor modeling pipelines.
> Source: <a href="https://github.com/terrapower/armi" style="color: #484848;">github.com/terrapower/armi</a>

<br>

[![OpenMDAO](./assets/images/OpenMDAO.png)](https://openmdao.org/)  
**OpenMDAO** is an open-source, multidisciplinary optimization framework in Python designed for systems engineering and analysis of complex coupled systems developed by *NASA Glenn Research Center*. It allows linking models, setting up design variables, and running optimizations with gradient and parallel support.
> Source: <a href="https://github.com/OpenMDAO/OpenMDAO" style="color: #484848;">github.com/OpenMDAO/OpenMDAO</a>

<br>

[![LANL](./assets/images/LANL.png)](https://www.lanl.gov/)  
Los Alamos National Laboratory' **Bohydra** is a workflow and data orchestration framework that supports design-of-experiments, optimization, UQ, and HPC workflows, particularly where multiple simulation codes must be coordinated. It’s focused on ensemble studies and model-based engineering.
> Source: <a href="https://github.com/lanl/bohydra" style="color: #484848;">github.com/lanl/bohydra</a>

<br>

[![LLNL](./assets/images/LLNL.png)](https://www.llnl.gov/)  
Lawrence Livermore National Laboratory uses DOE in **Zero-RK** and **Merlin-Spellbook** to generate design-of-experiments samples for simulation-based optimization workflows. **Zero-RK** is a numerical ODE integrator / solver framework optimized for HPC and accurate time integration of ODE systems. It provides high-performance integrators for stiff and non-stiff problems, often used in scientific computing. **Merlin-spellbook** is a small utility package (often used alongside Merlin workflows) providing common building blocks for configuring workflows and tasks.

> Sources:  
<a href="https://github.com/llnl/zero-rk" style="color: #484848;">github.com/llnl/zero-rk</a>  
<a href="https://github.com/llnl/merlin-spellbook" style="color: #484848;">github.com/llnl/merlin-spellbook</a>

<br>

[![SNL](./assets/images/SNL.png)](https://www.sandia.gov/)  
**pvOps** is a Python library for photovoltaic (PV) systems data analysis, particularly for field-collected operational data, text logs, time series, IV curves, etc. It includes processing and fusion of diverse PV datasets. Sandia National Laboratories uses DOE in *pvOps* create samples for black box optimization.
> Source: <a href="https://github.com/sandialabs/pvOps" style="color: #484848;">github.com/sandialabs/pvOps</a>

<br>

[![Gemseo](./assets/images/gemseo.png)](https://gemseo.org)  
**GEMSEO** (**G**eneric **E**ngine for **M**ulti-disciplinary **S**cenarios, **E**xploration and **O**ptimization) is a general engine for multidisciplinary scenarios, exploration, and optimization — a suite for optimization, UQ, MDO, and surrogate modeling tools. It’s modular and acts as an engine for exploring engineering systems under uncertainty.
> Source: <a href="https://github.com/gemseo/gemseo" style="color: #484848;">github.com/gemseo/gemseo</a>

<br>

[![MOG](./assets/images/MOG-only-light.png#only-light)](https://optgroup.it.jyu.fi/)
[![MOG](./assets/images/MOG--only-dark.png#only-dark)](https://optgroup.it.jyu.fi/)  
*The Multiobjective Optimization Group* uses DOE in **pyRVEA** to produce DOE samples for multi-objective optimization and surrogate model workflows. It implements the **R**eference **V**ector **G**uided **E**volutionary **A**lgorithm for global search in design spaces.
> Source: <a href="https://github.com/industrial-optimization-group/pyRVEA" style="color: #484848;">github.com/industrial-optimization-group/pyRVEA</a>

<br>

[![Paypal](./assets/images/Paypal.png)](https://www.paypal.com/)  
**Gators** is a package developed by *Paypal* to handle model building with big data and fast real-time pre-processing, even for a large number of QPS, using only Python. It uses DOE to generate structured design samples for model testing and performance tuning. It handles large-scale model building and real-time preprocessing on high-QPS data pipelines, providing a systematic way to explore input spaces efficiently before training or benchmarking.
> Source: <a href="https://github.com/paypal/gators" style="color: #484848;">github.com/paypal/gators</a>

<br>

[![SURG](./assets/images/SURG.png)](https://sites.google.com/site/jhusurg/)  
*SURGroup* uses DOE in **UQpy** (“**U**ncertainty **Q**uantification with **Py**thon”) to create design-of-experiments samples for uncertainty quantification and optimization workflows. *UQpy* is a general Python toolbox for uncertainty quantification in engineering and scientific contexts. It implements sampling, propagation, surrogate models, and sensitivity analysis.
> Source: <a href="https://github.com/SURGroup/UQpy" style="color: #484848;">github.com/SURGroup/UQpy</a>
