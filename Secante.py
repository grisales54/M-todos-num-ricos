import numpy as np
import sympy as sp


def f(x):

    y = (
        1
        + (2 * x)
        - (3 * x**2) * np.exp(-x)
        + (2 * x**3) * (np.sin(x)) * np.exp(-x / 5)
    )

    return y


xi = float(input("Limite mayor: "))

xi_1 = 17
x0 = 0

tol = 0.001
error = 1

i = 0


while error > tol:

    i = i + 1

    xnuevo = xi - ((f(xi) * (xi_1 - xi)) / (f(xi_1) - f(xi)))

    error = abs(xnuevo - xi) / xnuevo

    xi_1 = xi
    xi = xnuevo


print("El error es: ", error)
print("La raíz está ubicada en: ", xi)
print("El número de iteraciones fue: ", i)
