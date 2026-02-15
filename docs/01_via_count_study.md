# Phase 1 – Spatially Confined Via Redundancy Optimization
(Literature-Grounded Electro-Thermal Modeling)

---

## 1. Research Objective

This phase investigates thermo-mechanical stability of a glass interposer with varying numbers of copper Through-Glass Vias (TGVs) under 1 W RF excitation conditions.

The study aims to determine the optimal via redundancy within a spatially confined region that minimizes thermally induced stress.

Unlike conventional redundancy expansion approaches, all vias are restricted within a fixed circular footprint.

---

## 2. Key Geometric Constraint (Primary Differentiator)

All via configurations (1–5 vias) satisfy:

- Every via lies inside a circular region of 0.08 mm diameter
- The circle is centered at the origin (0, 0)
- Via diameter: 0.02 mm
- Substrate dimensions: 0.4 mm × 0.4 mm × 0.2 mm

Increasing via count does NOT increase occupied footprint.
Instead, it increases redundancy density within the same confined region.

This isolates density-driven thermal interaction effects rather than footprint expansion effects.

---

## 3. Literature-Based Heat Source Derivation (1 W Condition)

The heat source applied in this study is derived from:

L. Chen et al.,
“Electro-thermal Co-Design and Verification of TGV Transmission Structures for High-Power High-Frequency Applications,” TechRxiv, 2025.

The referenced work reports interface heat flux values under 1 W @ 18 GHz excitation.

Reported maximum interface heat flux:

| Via Count | Interface Heat Flux q″ (W/m²) |
|------------|--------------------------------|
| 1 (Single) | 3.51 × 10⁵ |
| 2 (Dual)   | 1.91 × 10⁵ |
| 3 (Triple) | 1.87 × 10⁵ |
| 4 (Quad)   | 1.87 × 10⁵ |
| 5 (Penta)  | 1.87 × 10⁵ |

These values were used to back-calculate the dissipated thermal power per via.

---

## 4. Conversion to Volumetric Heat Generation

Via geometry:

- Radius: 0.01 mm (1 × 10⁻⁵ m)
- Height: 0.2 mm (2 × 10⁻⁴ m)

Via volume:

V = π r² h  
V = 6.283 × 10⁻¹⁴ m³

Derived dissipated power per via:

| Via Count | Heat per Via (W) |
|------------|-------------------|
| 1 | 4.41 × 10⁻³ |
| 2 | 2.40 × 10⁻³ |
| 3 | 2.35 × 10⁻³ |
| 4 | 2.35 × 10⁻³ |
| 5 | 2.35 × 10⁻³ |

Volumetric heat generation applied in ANSYS:

q‴ = Q / V

| Via Count | q‴ (W/m³) |
|------------|------------|
| 1 | 7.02 × 10¹⁰ |
| 2 | 3.82 × 10¹⁰ |
| 3 | 3.74 × 10¹⁰ |
| 4 | 3.74 × 10¹⁰ |
| 5 | 3.74 × 10¹⁰ |

These volumetric heat sources were applied uniformly within each copper via.

---

## 5. Modeling Assumptions

This model assumes:

- The RF input power is 1 W (as reported in literature)
- The reported interface heat flux corresponds to total EM-to-thermal loss
- All dissipated power is converted into heat inside copper vias
- Heat generation is uniformly distributed within the via volume
- Radiation and secondary loss mechanisms are not explicitly modeled
- Higher-order electro-thermal coupling effects are neglected

This simplified approach enables controlled comparison of redundancy density effects under identical power conditions.

---

## 6. Boundary Conditions

- Volumetric heat generation applied to copper vias only
- Convection boundary condition applied to external surfaces
- Coupled thermal–structural analysis performed
- Identical conditions used for all via counts

---

## 7. Engineering Insight

Because all vias are confined within the same 0.08 mm diameter region, increasing via count increases redundancy density, not footprint size.

The literature-reported heat flux shows exponential saturation beyond N = 2.

This suggests:

- Thermal interaction between adjacent vias increases
- Localized heat concentration saturates
- Mechanical constraint within glass amplifies
- Excessive redundancy does not linearly reduce stress

The 2-via configuration represents the most balanced redundancy density under spatial confinement.

---

## 8. Significance

This study demonstrates that optimal via redundancy must be evaluated under spatial confinement and density effects, not merely increased via count.

The approach provides a controlled, literature-grounded electro-thermal model for evaluating TGV clustering behavior in advanced glass interposer systems.
