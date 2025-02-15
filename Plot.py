import matplotlib.pyplot as plt
import numpy as np


def PlotHermitePolynomial(data, num_knots, polynomial_func):

    x_vals_data = [point[0] for point in data]
    x_min = min(x_vals_data) - 1
    x_max = max(x_vals_data) + 1
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = polynomial_func(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label="Hermite Polynomial", color="blue")
    plt.scatter(x_vals_data, [point[1] for point in data], color="red", zorder=5, label="Data Points")

    plt.title("Hermite Interpolation Polynomial")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
