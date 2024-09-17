import numpy as np
import matplotlib.pyplot as plt
import math as m


def f(x):
    y = -(np.sqrt(16 - (x + 1) ** 2)) + 2
    # y=np.exp(-x)-x
    return y


a = 1  # Valor inferior del intervalo
b = 3  # Valor superior del intervalo
tol = 0.001  # Tolerancia
imax = 20  # Maximas interaciones

# Inicializar variables

i = 0
error = 1  # El error se inicializa en 100 %
c = 0
c0 = 0

a0 = [a]
b0 = [b]
errores = []
raices = []


if f(a) * f(b) < 0:
    while error > tol:
        c = a - f(a) * ((b - a) / (f(b) - f(a)))
        if f(c) == 0:
            break
        elif f(a) * f(c) <= 0:
            b = c
        else:
            a = c

        i += 1
        error = abs((c - c0) / c)
        c0 = c

        a0.append(a)
        b0.append(b)
        errores.append(error)
        raices.append(c)

else:
    print("La raiz no esta definida en este intervalo")


print("*******************************")
print("Número de interaciones: ", i)
print("Raíz aproximada: ", c)
print("Error en porcentaje", error)

print("*******************************")


# x = np.linspace(1, 15, 1000)
# y = f(x)

# plt.plot(x, y, label="f(x)")
# plt.scatter(c, 0, color="blue", label="Raiz aproximada")

# plt.grid(True)
# plt.axhline(0, 0, color="black")
# plt.axvline(0, 0, color="black")
