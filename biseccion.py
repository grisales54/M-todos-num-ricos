import math as m
import numpy as np

# Función de entrada
Fx = lambda x: -(np.sqrt(16 - (x + 1) ** 2)) + 2


# limites
a = float(input("Ingrese el primer límite: "))
b = float(input("Ingrese el segundo límite: "))

error = 1
criterio = 0.001
c = 0
c0 = 0
# vectores para almacenar los datos del problema
errores = []
iteraciones = 0

while criterio < error:
    iteraciones = iteraciones + 1
    # Punto medio
    c = (a + b) / 2

    # Bolzano

    fa = Fx(a)
    fb = Fx(b)
    fc = Fx(c)

    Bolzano = fa * fc

    if Bolzano < 0:

        error = abs((c - b)) / c
        b = c

    else:

        error = abs((c - a)) / c

        a = c

    errores.append(error)


print("****************************")
print("La raiz se encuentra en: ", c)
print("****************************")
print("El número de interaciones fue: ", iteraciones)
print("****************************")
