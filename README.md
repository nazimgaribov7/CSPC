PW1 — Lab A: Reproducible Foundations

What I built:

Set up the CSPC repository and environment for the lab.
Implemented radioactive decay simulation, added tests, and compared Python and NumPy performance.

Speed comparison (loop vs NumPy):

version	time (s)
pure-Python loop	2.721565
NumPy (vectorised)	0.000281
Speed-up: 9669.83 × faster

Tests: all passing? (yes)

Conclusion:

The tests passed successfully.
The NumPy vectorised version was much faster than the pure-Python loop.
I learned how to write tests with pytest and compare the performance of different implementations.

## PW2 — Lab A

### Results

- Mean acceleration: -8.58 m/s²
- Acceleration standard deviation: 28.72 m/s²
- Largest position difference: 0.785 m

Differentiation amplifies measurement noise, so the acceleration obtained after two derivatives is much noisier than the original position data.
After integrating the noisy acceleration back to velocity and then position, the recovered position remained relatively close to the original position. The largest difference was about 0.785 m.

## PW2 — Lab B: Optimization and Chemical Applications

### Part 2: Optimization Methods

For the function f(x) = (x - 3)^2 + 1, gradient descent, Newton's method, and SLSQP found the minimum at x = 3, where f(x) = 1.

For the function g(x) = x^4 - 3x^2 + x + 5, the results depended on the starting point and optimization method.

Starting from x0 = 0, gradient descent and SLSQP found a minimum near x = -1.301, where g(x) ≈ 1.486. Newton's method found a local maximum near x = 0.170.

Starting from x0 = 2, gradient descent and Newton's method found a minimum near x = 1.131. SLSQP found a lower minimum near x = -1.301.

### Part 3: Chemical Kinetics

The experimental data were fitted to the first-order reaction model:

C(t) = C0 * exp(-k*t)

SLSQP minimized the sum of squared errors.

The fitted rate constant was k = 0.261761.

The graph is saved as `PW2/Lab B/kinetics.png`.

### Part 4: Chemical Equilibrium

For the reaction H2 + I2 ⇌ 2 HI, the equilibrium was calculated using Newton's method and SLSQP with K = 15.

Newton's method: x = 0.659458 mol.

SLSQP: x = 0.659458 mol.

Equilibrium amounts:
- H2 = 0.340542 mol
- I2 = 0.340542 mol
- HI = 1.318915 mol

The graph is saved as `PW2/Lab B/equilibrium.png`.

### Part 5: Acid-Base Titration

The numerical derivative of pH with respect to the added base volume was calculated using `numpy.gradient`.

The estimated equivalence point was 50.0 mL, with a maximum slope of 4.0 pH units/mL.

The titration curve and its derivative are saved as `PW2/Lab B/titration.png`.
