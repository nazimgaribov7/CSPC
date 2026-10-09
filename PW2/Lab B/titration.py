import numpy as np
import matplotlib.pyplot as plt


# Read titration data
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)

V = data[:, 0]
pH = data[:, 1]

# Calculate the slope of pH with respect to volume
slope = np.gradient(pH, V)

# Find the equivalence point
index = np.argmax(slope)
V_eq = V[index]

print("Equivalence point =", V_eq, "mL")
print("Maximum slope =", slope[index])


# Plot pH and its slope side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(V, pH, "o-")
axes[0].axvline(V_eq, linestyle="--", label=f"Equivalence: {V_eq:.2f} mL")
axes[0].set_xlabel("Volume of base (mL)")
axes[0].set_ylabel("pH")
axes[0].set_title("Titration curve")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(V, slope, "o-")
axes[1].axvline(V_eq, linestyle="--", label="Maximum slope")
axes[1].set_xlabel("Volume of base (mL)")
axes[1].set_ylabel("dpH/dV")
axes[1].set_title("Slope of titration curve")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig("titration.png", dpi=150)
plt.show()
