import numpy as np
import matplotlib.pyplot as plt

# Puntos de datos
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 1, 3, 2]


def spline_cubico(x, y):

    n = len(x)
    a = [0] * n  # Lista para almacenar los coeficientes
    b = [0] * n
    c = [0] * n
    d = [0] * n

    for i in range(n):

        if i == 0:
            a[i] = y[i]
            d[i] = 0  # Derivada segunda en el primer punto
        elif i == n - 1:
            a[i] = y[i]
            c[i] = 0  # Derivada primera en el último punto
        else:
            a[i] = y[i]

    for i in range(1, n):
        h = x[i] - x[i - 1]
        c[i - 1] = (y[i] - y[i - 1]) / h  # Diferencias finitas

    for i in range(1, n - 1):

        h1 = x[i] - x[i - 1]
        h2 = x[i + 1] - x[i]
        d[i] = 6 * ((c[i] - c[i - 1]) / (h1 + h2))

    d[0] = 0  # Condiciones de frontera
    d[n - 1] = 0

    for i in range(n - 2, -1, -1):
        h = x[i + 1] - x[i]
        b[i] = (d[i] - d[i + 1]) / (6 * h)
        c[i] = c[i] - (h * d[i + 1]) / 6
        d[i] = d[i] / 2

    return a, b, c, d


#
x_nuevo = np.linspace(x[0], x[-1], 100)
y_nuevo = np.zeros_like(x_nuevo)


# LLamamos la función
a, b, c, d = spline_cubico(x, y)

for i in range(len(x) - 1):
    idx = (x_nuevo >= x[i]) & (x_nuevo <= x[i + 1])  # límites True or False
    y_nuevo[idx] = (
        a[i]
        + b[i] * (x_nuevo[idx] - x[i])
        + c[i] * (x_nuevo[idx] - x[i]) ** 2
        + d[i] * (x_nuevo[idx] - x[i]) ** 3
    )

plt.figure(figsize=(8, 6))
plt.plot(x_nuevo, y_nuevo, "b", label="Spline cúbico")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spline cúbico")
plt.grid()
plt.show()
