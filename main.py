# main.py

from DisplayData import DisplayData
from GenerateHermitePolynomial import GenerateHermitePolynomial
from Plot import PlotHermitePolynomial
from config import MAX_KNOTS
import sympy as sp


def input_data():
    num_knots = int(input("Input number of knots: "))
    if num_knots > MAX_KNOTS:
        print(f"Don't make more than {MAX_KNOTS} knots.")
        return None, None

    data = []
    for i in range(num_knots):
        x = float(input(f"Input Point {i + 1}: "))
        f_x = float(input(f"Input Value f(x) {i + 1}: "))
        f_prime_x = float(input(f"Input derivative f'(x) {i + 1}: "))
        data.append([x, f_x, f_prime_x])
    return data, num_knots


def main():
    print(
        "Give the points in order, e.g., x1, x2, x3... xn. When giving a knot with multiplicity, you have to input once more their derivative and value")
    data, num_knots = input_data()
    if data is None:
        return
    DisplayData(data, num_knots)

    distinct_nodes = sorted(set(d[0] for d in data))
    if len(distinct_nodes) != 2:
        print("This implementation supports exactly 2 distinct nodes.")
        return

    H = GenerateHermitePolynomial(data, 2)
    print("Your Hermite's Polynomial:")
    sp.pretty_print(H)


    x = sp.symbols('x')
    H_func = sp.lambdify(x, H, "numpy")
    PlotHermitePolynomial(data, num_knots, H_func)


if __name__ == "__main__":
    main()
