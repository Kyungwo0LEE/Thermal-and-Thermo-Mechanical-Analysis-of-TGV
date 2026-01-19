## Mesh Convergence Verification

A mesh size sweep was conducted to verify the mesh independence of the thermal simulation results.
The maximum temperature of the model was selected as the quantity of interest, as peak values are generally the most sensitive to mesh resolution in thermal analyses.

The following figure illustrates the variation of the maximum temperature with respect to element size refinement, together with the extrapolated convergence limit.

### Mesh convergence of Tmax
![Mesh convergence (Tmax)](../figures/mesh_convergence/mesh_convergence.png)

**Figure 1.**  
Maximum temperature as a function of mesh size.
Discrete symbols represent FEM simulation results, while the solid curve denotes a nonlinear regression fit.
The dashed horizontal line indicates the extrapolated converged temperature \( T_\infty \), corresponding to the limit of vanishing element size.

As the mesh is refined, the maximum temperature monotonically approaches an asymptotic value.
To quantitatively assess mesh convergence, the simulation data were extrapolated using a nonlinear convergence model, allowing estimation of the mesh-independent solution.

Below a certain element size, further refinement produces negligible changes in the maximum temperature, indicating that numerical discretization errors are sufficiently reduced.

Based on this behavior, the mesh resolution used in the final simulations is considered adequate to ensure numerical accuracy while avoiding unnecessary computational cost.

## Mesh Optimization Based on Convergence Results

The mesh convergence results were further used to guide the final mesh optimization strategy in ANSYS.
Previous simulations indicated that the most significant temperature gradients occur near the Cu–glass interface, where local heat spreading and material property mismatch are dominant.

To accurately capture these localized effects, additional mesh refinement was applied to the interface region by adjusting both the refinement level and the transition setting.
While increasing the refinement level enhances local resolution, the transition setting controls how smoothly the mesh size changes from fine to coarse regions.

A slow transition was found to provide a more conservative and stable estimate of the maximum temperature by reducing numerical artifacts associated with abrupt mesh size changes.
Among the tested configurations, the mesh with refinement level 2 and slow transition resulted in the highest and most stable maximum temperature.

This mesh configuration was therefore selected for all subsequent thermal and thermo-mechanical analyses.
