import math as m
import numpy as np


def f(x):

    y = (1 * 10**6) - (1 * 10**5) * (x) - (250 * 10**3) * (x ** (1 / 2))

    return y


Xo = 6
tol = 0.001
error = 1
i = 0
x = 0

raices = [x]

while error > tol:
    i = i + 1
    x = f(Xo)
    raices.append(x)

    error = abs((x - Xo) / x)
    Xo = x


print("El valor de la raíz aproximada es: ", x)
print("El valor del error es: ", error)
print("El número de iteraciones fue: ", i)

# ejex = np.linspace(0, 15)
# y = f1(ejex)

# plt.plot(ejex, y, label="f(x)")
# plt.scatter(x, 0, color="blue", label="Raiz aproximada")
# plt.grid(True)
# plt.axhline(0, 0, color="black")
# plt.axvline(0, 0, color="black")
# plt.show()
