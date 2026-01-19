import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import pandas as pd

h = np.array([
    1.0e-4, 9.5e-5, 9.0e-5, 8.5e-5, 8.0e-5, 7.5e-5,
    7.0e-5, 6.5e-5, 6.0e-5, 5.5e-5, 5.0e-5, 4.5e-5,
    4.0e-5, 3.5e-5, 3.0e-5, 2.5e-5, 2.0e-5, 1.5e-5
], dtype=float)

T = np.array([
    29.724, 29.725, 29.743, 29.740, 29.726, 29.740,
    29.757, 29.760, 29.700, 29.760, 29.757, 29.760,
    29.761, 29.762, 29.759, 29.762, 29.762, 29.763
], dtype=float)


def exp_convergence(h, T_inf, A, B):
    return T_inf + A * np.exp(-B / h)

p0 = [29.762, -0.05, 1e-5]

params, _ = curve_fit(
    exp_convergence, h, T,
    p0=p0, maxfev=10000
)

T_inf, A, B = params

h_grid = np.logspace(np.log10(h.min()), np.log10(h.max()), 400)
T_fit = exp_convergence(h_grid, T_inf, A, B)

plt.figure(figsize=(7.8, 5.0))

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIXGeneral"],
    "mathtext.fontset": "stix",
    "font.size": 12
})

plt.scatter(h, T, s=55, color="black", label="Data")


plt.plot(
    h_grid, T_fit,
    color="red", linewidth=2.5,
    label="Regression function"
)

plt.axhline(
    T_inf,
    color="red", linestyle="--", linewidth=1.5,
    label=rf"$T_\infty \approx {T_inf:.3f}\,^{{\circ}}C$"
)

output_path = "mesh_convergence"

plt.xscale("log")
plt.xlabel("element size (m)")
plt.ylabel("Maximum temperature of Model (°C)")
plt.title("Nonlinear regression")
plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.legend()
plt.tight_layout()
plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print(f"T_infinity (true value) = {T_inf:.3f} °C")


df_data = pd.DataFrame({
    "element_size_m": h,
    "Tmax_C": T
})

df_data.to_csv("mesh_convergence_data.csv", index=False)


df_params = pd.DataFrame({
    "parameter": ["T_infinity_C", "A", "B"],
    "value": [T_inf, A, B]
})

df_params.to_csv("mesh_convergence_params.csv", index=False)
