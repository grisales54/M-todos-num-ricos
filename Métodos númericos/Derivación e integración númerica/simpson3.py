# Regla de simpson 1/3

# sirve para funciones que se parezca a una cubica
import numpy as np

a = int(input("Ingrese a: "))  # desde -2
b = int(input("Ingrese b: "))  # hasta 2

n = 5

x = np.linspace(a, b, n)

fx = lambda x: 1 - x**2 + 2 * x**3
dx = (b - a) / (n - 1)
y = fx(x)

I = (
    3 * dx * (y[0] + y[-1] + 3 * np.sum(y[1:-1:3]))
    + 3 * np.sum(y[2:-1:3])
    + 2 * np.sum(y[3:-1:3]) / 8
)

# 4*np.sum(y[1:-1:2]) desde el primer dato hasta el penultimo todos los impares
print(f"El área bajo la curva es {round(I,3)}")
