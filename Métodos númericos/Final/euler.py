import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Se define la función que vamos a utilizar


def dF(x, y):  # función original
    f = np.cos(x**2)
    return f


def fun(x):
    fun = np.cos(x**2)
    return fun


# se definen las condiciones iniciales y también el paso
x0 = 0
y0 = 0
xf = 20
n = 200

x = np.array([x0])
y = np.array([y0])


# Se hacen las iteraciones que se solicitaron
h = (xf - x0) / n
for i in range(1, n + 1):
    yn = y0 + dF(x0, y0) * h
    x0 = x0 + h
    y0 = yn
    x = np.append(x, x0)
    y = np.append(y, y0)

# Se crea una tabla con los resultados de las iteracciones que se han realizado

Datos = pd.DataFrame({"x": x, "y": y})
print(Datos)

# Se crean lasgráficas del método de Euler y la gráfica exacta de la solución de la ecuación
xp = np.linspace(0, 20, n)
plt.figure()
plt.plot(x, y)
plt.plot(xp, fun(xp))
plt.legend(["Euler", "Exacto"])
plt.grid()
plt.show()
