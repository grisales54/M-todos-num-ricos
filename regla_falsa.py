import numpy as np  # trabajar con matrices
import matplotlib.pyplot as plt  # Libreria para graficar
import math as m


# Función
def f(x):
    I = (
        1
        + (2 * x)
        - (3 * x**2) * np.exp(-x)
        + (2 * x**3) * (np.sin(x)) * np.exp(-x / 5)
    )

    return I


# límites
a = 4  # límite inferior
b = 20  # límite superior

tolerancia = 0.001
imax = 17

c = 0
c0 = 0
# Error

i = 0
error = 1  # El error se inicia en 100%

a0 = [a]
b0 = [b]

errores = [(a + b) / 2]

if f(a) * f(b) < 0:

    while i <= imax:

        c = (a - f(a)) * ((a - b) / (f(a) - f(b)))
        # c = b - ((f(b) - (a - b)) / (f(a) - f(b)))

        if f(c) == 0:
            print("La raíz es: ", c)
            break

        elif f(a) * f(c) < 0:

            b = c

        else:
            a = c

        i = i + 1

        # c0 = c

        # a0.append(a)
        # b0.append(b)
        # errores.append(error)
else:
    print("No existe raíz")


print("El número de interaciones fue: ", i)
print("El valor de la raíz es: ", c)
print("El error es de: ", error)

print(a0)
print(b0)
print(errores)

# x = np.linspace(1, 15, 1000)
# y = f(x)

# plt.plot(x, y, label="f(x)")
# plt.scatter(c, 0, color="blue", label="Raíz aproximada")

# plt.grid(True)
# plt.axhline(0, 0, color="black")
# plt.axvline(1, 0, color="black")

# plt.show()
