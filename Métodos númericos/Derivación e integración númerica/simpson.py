# Regla de simpson 1/3


# sirve para funciones que se parezca a una cuadratica
import numpy as np

a = int(input("Ingrese a: "))  # desde -2
b = int(input("Ingrese b: "))  # hasta 2

n = 5

x = np.linspace(a, b, n)

fx = lambda x: 2 * x**3 + 14 * x**2 + 1
dx = (b - a) / (n - 1)
y = fx(x)

I = dx * (fx(b) + fx(a) + 4 * np.sum(y[1:-1:2])) + 2 * np.sum(y[2, -1:2]) / 3


# 4*np.sum(y[1:-1:2]) desde el primer dato hasta el penultimo todos los impares
print(f"El área bajo la curva es {I}")
