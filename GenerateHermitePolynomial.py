import sympy as sp


def GenerateHermitePolynomial(data, n):

    if n != 2:
        raise ValueError("This implementation only supports exactly 2 distinct nodes.")

    x0, f0, fp0 = data[0]
    x1, f1, fp1 = data[2]

    x = sp.symbols('x')


    L0 = (x - x1) / (x0 - x1)
    L1 = (x - x0) / (x1 - x0)

    L0_prime = sp.diff(L0, x)
    L1_prime = sp.diff(L1, x)

    h00 = (1 - 2 * L0_prime.subs(x, x0) * (x - x0)) * (L0 ** 2)
    h10 = (x - x0) * (L0 ** 2)
    h11 = (1 - 2 * L1_prime.subs(x, x1) * (x - x1)) * (L1 ** 2)
    h01 = (x - x1) * (L1 ** 2)

    H = f0 * h00 + fp0 * h10 + f1 * h11 + fp1 * h01


    return sp.simplify(H)
