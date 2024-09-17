from sympy import symbols, diff, sympify
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

print("-" * 30)
n = int(input("Ingrese el valor de la n-esima derivada: "))
x0 = int(input("Ingrese el valor de x0: "))
y = input("Ingrese el polinomio: ")
print("-" * 30)


def derivador(y, n, x0):
    # Convierte la entrada de la función en una expresión sympy
    x = symbols("x")
    expr = sympify(y)

    i = 0
    Lista = []
    der = [expr]

    while i <= n:
        i += 1
        evaluar = der[-1].subs(x, x0)  # Evalúa la función dada con un valor de x dado
        Lista.append(evaluar)
        derivada = diff(der[-1], x)  # Deriva la función
        der.append(derivada)

    return Lista


derivadas = derivador(y, n, x0)


print("Funciones derivadas y evaludas")
print("-" * 30)
print(derivadas)
print("-" * 30)

n = len(derivadas)
x = symbols("x")
i = 0

taylor = []

while i < n:

    Taylor = str((derivadas[i] * (x - x0) ** (i)) / sp.factorial(i))
    i = i + 1
    taylor.append(Taylor)

for i in taylor:  # Remueve los ceros innecesarios
    if i == "0":
        taylor.remove("0")


print("-" * 30)
print("El polinomio de Taylor es:")
print("-" * 30)

funcion = "+".join(str(x) for x in taylor)

print(funcion)

x_1 = sympify(funcion)
x = symbols("x")

eje_x = np.arange(-5, 5, 0.01)

feje_x = [x_1.subs(x, value) for value in eje_x]

# feje_x = x_1.subs(x, eje_x)
# Imprime los elementos de una lista, con un '+ ' entre cada valor de lista

plt.plot(eje_x, feje_x)
plt.grid()
plt.show()
