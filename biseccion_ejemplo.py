import numpy as np  # trabajar con matrices
import math as m


# Función
def f(x):
    y = -(np.sqrt(16 - (x + 1) ** 2)) + 2

    return y


# límites
a = 0  # límite inferior
b = 2  # límite superior

tolerancia = 0.05
imax = 10

c = 0
c0 = 0
# Error

i = 0
error = 1  # El error se inicia en 100%

a0 = [a]
b0 = [b]
errores = [(a + b) / 2]

if f(a) * f(b) < 0:

    while (error > tolerancia) and (i <= imax):

        c = (a + b) / 2

        if f(c) == 0:
            print("La raíz es: ", c)

        elif f(a) * f(c) < 0:

            b = c

        else:
            a = c

        i = i + 1

        error = abs((c - c0) / c)
        c0 = c

        a0.append(a)
        b0.append(b)
        errores.append(error)
else:
    print("No existe raíz")


print("El número de interaciones fue: ", i)
print("El valor de la raíz es: ", c)
print("El error es de: ", error)


print(errores)
