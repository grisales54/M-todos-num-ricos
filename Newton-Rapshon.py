import math
import sympy as sp
import numpy as np


def f(x0):
    x = sp.symbols("x")
    y = -(sp.sqrt(16 - (x + 1) ** 2)) + 2
    # y = 6.18 * sp.sin(x - 0.756) - 23.8 * sp.exp(-1.0604 * x)
    g = y.diff(x)

    y0 = y.evalf(subs={"x": x0})
    g0 = g.evalf(subs={"x": x0})

    return y0, g0


B0 = 1


error = 1
tolerancia_error = 0.05

raices = []

i = 0

while (error) >= tolerancia_error:
    i = i + 1

    B, B1 = f(B0)

    Bnuevo = B0 - (B / B1)

    raices.append(Bnuevo)

    error = abs((Bnuevo - B0) / Bnuevo)

    B0 = Bnuevo


print(f"El error es: ", error)
print("La raices de la función son: ", B0)
print("El número de iteraciones es: ", i)
