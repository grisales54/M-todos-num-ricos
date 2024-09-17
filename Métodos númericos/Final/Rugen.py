import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


# Función de primer orden con la que se realizarán las iteracciones
# Usamos la misma función de los ejercicios anteriores y de esta manera podemos ver las mejoras de los métodos
def f1(x, y):
    return np.cos(x**2)


# Solución exacta de la ecuación de primer orden
def y_exacta(x):
    return (x + 1) ** 2 - 0.5 * np.exp(x)


# Método de Runge-Kutta de 4to orden, función para cada una de las pendientes
def RK4(f, x0, y0, xf, h):
    n = int((xf - x0) / h)
    x = np.linspace(x0, xf, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    # Se crean las listas para añadir cada resultado de la pendiente que se obtiene en cada iteración
    m1v, m2v, m3v, m4v, er = ["--"], ["--"], ["--"], ["--"], ["--"]
    # Se empíeza a iterar sobre cada una de las pendientes
    for i in range(n):
        m1 = f(x[i], y[i])
        m2 = f(x[i] + 0.5 * h, y[i] + 0.5 * m1 * h)
        m3 = f(x[i] + 0.5 * h, y[i] + 0.5 * m2 * h)
        m4 = f(x[i] + h, y[i] + m3 * h)
        y[i + 1] = y[i] + (1 / 6) * (m1 + 2 * m2 + 2 * m3 + m4) * h

        # Se calcula el error de cada iteración
        if y[i] != 0:
            error = abs((y[i + 1] - y[i]) * 100 / y[i])
        else:
            error = np.nan

        m1v.append(m1)
        m2v.append(m2)
        m3v.append(m3)
        m4v.append(m4)
        er.append(error)

    m1v.append("--")
    m2v.append("--")
    m3v.append("--")
    m4v.append("--")
    er.append("--")

    return x, y, m1v, m2v, m3v, m4v, er


# Condiciones iniciales del ejercicio
x0 = 0
y0 = 0
xf = 20
h = 0.1

# Se llama a la funcion para empezar a calcular cada una de las pendientes sobre el método utilizado
x, y, m1v, m2v, m3v, m4v, er = RK4(f1, x0, y0, xf, h)

# Crear una tabla de resultados
tabla = []
for i in range(len(x)):
    tabla.append(
        [
            f"{x[i]:.5f}",
            f"{y[i]:.5f}",
            m1v[i] if m1v[i] == "--" else f"{m1v[i]:.5f}",
            m2v[i] if m2v[i] == "--" else f"{m2v[i]:.5f}",
            m3v[i] if m3v[i] == "--" else f"{m3v[i]:.5f}",
            m4v[i] if m4v[i] == "--" else f"{m4v[i]:.5f}",
            er[i] if er[i] == "--" else f"{er[i]:.5f}",
        ]
    )
# Imprimir la tabla de resultados
print(" ")
print("Valores para cada iteración del método RK-4")
print(" ")
print("Tabla de datos")
print(" ")
print(tabulate(tabla, headers=["x", "y", "m1", "m2", "m3", "m4", "er(%)"]))
print(" ")

# Graficar los resultados
xp = np.linspace(x0, xf, 100)
plt.figure()
plt.plot(x, y, label="RK4")
# plt.plot(xp, y_exacta(xp), label="Exacta")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Método de Runge-Kutta de 4to orden vs Solución Exacta")
plt.show()
