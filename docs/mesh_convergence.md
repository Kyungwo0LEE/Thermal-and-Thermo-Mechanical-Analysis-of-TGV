## Mesh Convergence Verification

A mesh size sweep was conducted to verify mesh independence of the thermal simulation results. 
The maximum temperature of the model was selected as the quantity of interest, as peak values are generally the most sensitive
to mesh resolution in thermal analyses.

The following figure illustrates the variation of the maximum temperature with respect to element size refinement.

### Mesh convergence of Tmax
![Mesh convergence (Tmax)](../figures/mesh_convergence/mesh_convergence.png)

**Figure 1.** 
Maximum temperature as a function of mesh size.
As the mesh is refined, the maximum temperature approaches an asymptotic value, indicating convergence toward a mesh-independent solution.

The change in maximum temperature becomes progressively smaller with mesh refinement. 
Below a certain element size, further refinement does not produce a meaningful change in the maximum temperature, 
suggesting that numerical discretization errors are sufficiently reduced.

Based on this behavior, the mesh resolution used in the final simulations is considered adequate to ensure numerical accuracy while avoiding
unnecessary computational cost.
