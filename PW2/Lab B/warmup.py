import numpy as np
from scipy.optimize import newton, minimize


# Part 2A: Easy convex function
def f(x):
    return (x - 3)**2 + 1


def df(x):
    return 2 * (x - 3)


def ddf(x):
    return 2


def gradient_descent(func, derivative, x0, learning_rate=0.1, tolerance=1e-8):
    x = float(x0)

    for _ in range(10000):
        x_new = x - learning_rate * derivative(x)

        if abs(x_new - x) < tolerance:
            return x_new

        x = x_new

    return x


print("PART 2A: EASY CONVEX FUNCTION")
print("Gradient descent:", gradient_descent(f, df, 0))
print("Newton:", newton(df, 0, fprime=ddf))
result = minimize(lambda x: f(x[0]), [0.0], method="SLSQP")
print("SLSQP:", result.x[0])


# Part 2B: Harder landscape
def g(x):
    return x**4 - 3*x**2 + x + 5


def dg(x):
    return 4*x**3 - 6*x + 1


def ddg(x):
    return 12*x**2 - 6


print("\nPART 2B: HARDER LANDSCAPE")

for x0 in [0.0, 2.0]:
    print(f"\nStarting point: x0 = {x0}")

    gd_result = gradient_descent(g, dg, x0, learning_rate=0.01)
    print("Gradient descent:", gd_result, "g(x) =", g(gd_result))

    try:
        n_result = newton(dg, x0, fprime=ddg)
        curvature = ddg(n_result)

        if curvature > 0:
            point_type = "minimum"
        elif curvature < 0:
            point_type = "maximum"
        else:
            point_type = "inconclusive"

        print("Newton:", n_result)
        print("g(x) =", g(n_result))
        print("g''(x) =", curvature, "->", point_type)

    except (RuntimeError, ZeroDivisionError, OverflowError) as error:
        print("Newton failed:", error)

    s_result = minimize(
        lambda x: g(x[0]),
        [x0],
        method="SLSQP"
    )

    print("SLSQP:", s_result.x[0])
    print("g(x) =", g(s_result.x[0]))
