# Mesh Convergence Analysis (Python)

This directory contains the finalized Python implementation for the mesh convergence analysis of the TGV thermal model.

The analysis evaluates the convergence behavior of the maximum temperature with respect to mesh size and applies nonlinear regression to estimate the
converged solution.


## Overview

The mesh convergence study is based on numerical results obtained from ANSYS thermal simulations. 
For each mesh size, the maximum temperature of the model is extracted and analyzed.

A nonlinear regression model is used to describe the convergence trend and to estimate the asymptotic maximum temperature as the mesh is refined.


## Methodology

- Mesh size is normalized to improve numerical stability during regression.
- A nonlinear exponential convergence model is applied:

  \[
  T_{\max}(h) = T_\infty - A \exp(-B h)
  \]

- Model parameters are estimated using the Levenberg–Marquardt algorithm implemented in `scipy.optimize.curve_fit`.
- A reference converged temperature, obtained from the finest mesh result, is visualized for comparison.


## Files

- `mesh_convergence.py`  
  Final Python script performing the mesh convergence analysis.
  The script:
  - fits the nonlinear regression model,
  - generates the convergence figure,
  - exports processed data and regression parameters to CSV files.

- `requirements.txt`  
  Python dependencies required to run the analysis.


## Output

Running the script generates the following outputs:

- **Figure**
  - `figures/mesh_convergence.png`  
    Mesh convergence plot showing simulation data, regression curve,
    and the reference converged temperature.

- **Data**
  - `data/mesh_convergence/mesh_convergence_data.csv`  
    Mesh size, simulated maximum temperature, and fitted temperature values.
  - `data/mesh_convergence/mesh_convergence_params.csv`  
    Estimated regression parameters and reference converged temperature.

