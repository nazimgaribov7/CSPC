import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize


# Equilibrium constant
K = 15.0


# Difference between equilibrium expression and K
def k_imbalance(x):
    return (2 * x)**2 / (1 - x)**2 - K


# Method 1: Newton root-finding
x_newton = newton(k_imbalance, 0.75)


# Method 2: SLSQP minimization
def objective(params):
    return k_imbalance(params[0])**2


result = minimize(
    objective,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.9999)]
)

x_slsqp = result.x[0]

print("Newton equilibrium x =", x_newton)
print("SLSQP equilibrium x =", x_slsqp)

# Equilibrium amounts
H2 = 1 - x_newton
I2 = 1 - x_newton
HI = 2 * x_newton

print("Equilibrium H2 =", H2, "mol")
print("Equilibrium I2 =", I2, "mol")
print("Equilibrium HI =", HI, "mol")

# Plot amounts against reaction extent
x = np.linspace(0, 0.99, 300)

plt.figure(figsize=(8, 5))
plt.plot(x, 1 - x, label="H2")
plt.plot(x, 1 - x, label="I2", linestyle="--")
plt.plot(x, 2 * x, label="HI")
plt.axvline(x_newton, linestyle=":", label="Equilibrium")

plt.xlabel("Reaction extent x (mol)")
plt.ylabel("Amount (mol)")
plt.title("Chemical equilibrium: H2 + I2 ⇌ 2 HI")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("equilibrium.png", dpi=150)
plt.show()
