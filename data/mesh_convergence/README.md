# Mesh Convergence Data

This directory contains numerical data used for the mesh convergence study of the TGV thermal analysis.

## Files

- `mesh_convergence_data.csv`  
  Final mesh convergence dataset used for nonlinear regression analysis.
  This file includes:
  - element size (m)
  - maximum temperature obtained from ANSYS simulations

- `mesh_convergence_params.csv`  
  Parameters obtained from the nonlinear regression analysis, including:
  - extrapolated converged maximum temperature \( T_\infty \)
  - regression coefficients of the convergence model

## Notes

Preliminary datasets generated during early mesh studies have been moved to the `archive/` directory and are retained for reference and reproducibility.

The extrapolated converged temperature provides a mesh-independent reference value obtained by regression-based extrapolation to vanishing element size.
