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
