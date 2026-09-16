import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

start = time.perf_counter()
simulate_loop(N0, lam)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam)
numpy_time = time.perf_counter() - start

print(f"Pure Python: {loop_time:.6f} s")
print(f"NumPy: {numpy_time:.6f} s")
print(f"Speed-up: {loop_time / numpy_time:.2f}x faster")