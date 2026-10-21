import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


                        
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)

time = data[:, 0]
concentration = data[:, 1]

                       
C0 = concentration[0]


                            
def model(t, k):
    return C0 * np.exp(-k * t)


                       
def total_error(params):
    k = params[0]
    predicted = model(time, k)
    return np.sum((concentration - predicted) ** 2)


                             
result = minimize(
    total_error,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 5)]
)

k_fit = result.x[0]

print("Fitted rate constant k =", k_fit)
print("Optimization successful:", result.success)

                                    
t_fit = np.linspace(time.min(), time.max(), 300)

plt.figure(figsize=(8, 5))
plt.scatter(time, concentration, label="Measured data")
plt.plot(t_fit, model(t_fit, k_fit), label=f"Fitted curve (k={k_fit:.3f})")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-order reaction kinetics")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("kinetics.png", dpi=150)
plt.show()
