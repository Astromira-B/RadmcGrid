# RadmcGrid

Radiative transfer grid using RADMC-3D for protoplanetary disk simulations.

## Installation Requirements

To run this package, you need the following:

### Required Software
- **RADMC-3D**: Must be installed and accessible in your system PATH. [RADMC-3D Website](https://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/)
- **Python 3.7+**

### Python Packages
- `radmc3dPy`
- `numpy`
- `matplotlib`
- `astropy`
- `tqdm`
- `seaborn` *(optional, for nicer plots)*

Install the dependencies with:

```bash
pip install numpy matplotlib astropy tqdm seaborn
```

## Overview

RadmcGrid is a Python package that helps set up and run radiative transfer simulations of protoplanetary disks using RADMC-3D. It supports several types of disk structures and can be used to produce synthetic observations or run simple parameter studies.

The supported disk models are:

- **Continuous disk** : smooth and uninterrupted from the inner to outer edge.
- **Gapped disk** : inner and outer disks separated by a region with lower dust density.
- **Cavity disk** : cleared inner region, with dust only in the outer disk.

  The package allows you to set properties such as disk mass, radii, inclination, dust composition, and more. Simulations can be run in parallel using multiple cores.

  ### Basic usage

  Import the module and run the simulation by selecting the disk type and setting the parameters.

Run simulations for different models using:

  ``` py
grid.run(model=0, ...)  # Continuous disk
grid.run(model=1, ...)  # Gapped disk
grid.run(model=2, ...)  # Cavity disk

```

Each model requires parameters for disk structure, stellar properties, image setup, and dust templates. You can also pass optional_params for finer control (e.g., power-law profiles, photon counts, dust opacity settings).

### Exemple

``` py
grid.run(
    model=0,
    tstar_rstar_list=[['4000', '2.0*rs']],
    rdisk2=100,
    mdisk1=1e-3,
    Inc=[30],
    npix=200,
    sizeau=60,
    nlmin=3,
    nlmax=4,
    nlam=11,
    Cdelt3=0.1,
    dpc=145,
    composition_name="full_astrosil_amira",
    template_dir="./dust_templates",
    total_cores=8,
    cores_per_sim=2,
    optional_params={"plsig1": "-1.0", "plh": "0.1"}
)
```
