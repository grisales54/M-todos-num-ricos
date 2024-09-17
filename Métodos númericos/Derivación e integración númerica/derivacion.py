import numpy as np
import matplotlib.pyplot as plt


a = int(input("Ingrese a: "))  # desde -2
b = int(input("Ingrese b: "))  # hasta 2
n = int(input("Ingrese el cantidad de dados: "))  # cantidad de datos


x = np.linspace(a, b, n)
fx = lambda x: 3 * x**3 + 2 * x**2 + 5 * x + 1
y = fx(x)

dx = (b - a) / (n - 1)  # Esto es H


yp = np.zeros_like(x)

for i in range(n):  # primer dato cunado x=0
    if i == 0:
        yp[i] = (y[i + 1] - y[i]) / (dx)

    elif i == n - 1:  # ultimo dato
        yp[i] = (y[i] - y[i - 1]) / (dx)

    else:
        yp[i] = (y[i + 1] - y[i - 1]) / (2 * dx)


# Crear la figura y los subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))


ax1.plot(x, y)
ax1.set_title("Función original")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()

ax2.plot(x, yp)
ax2.set_title("Función derivada")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid()

# Ajustar el espaciado entre los subplots
plt.tight_layout()

# Mostrar la figura
plt.show()
