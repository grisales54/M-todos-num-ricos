import pandas as pd
from math import *
import numpy as np
import matplotlib.pyplot as plt


n = int(input("Ingrese el número de puntos: "))
# x = [1, 2, 3, 5, 6, 8, 9, 10]
# y = [1.5, 2, 4, 4.6, 4.7, 8.5, 8.8, 9]

x = []
y = []

i, j = 1, 1

print("-" * 30)  # Separador

while i <= n:  # Ingresan los valores de x a una lista
    v1 = float(input(f"Ingrese el valor {i} de x: "))
    i = i + 1
    x.append(v1)

print("-" * 30)

while j <= n:  # Ingresa los valores de y a una lista
    v2 = float(input(f"Ingrese el valor {j} de y: "))
    j = j + 1
    y.append(v2)

# Multiplicación de x*y
multi = []
x_cuadrado = []
y_cuadrado = []

for j, k in zip(x, y):
    x_cuadrado.append(j**2)
    y_cuadrado.append(k**2)
    mul = j * k
    multi.append(mul)

data1 = {
    "i": range(1, n + 1),
    "x": x,
    "y": y,
    "x*y": multi,
    "x^2": x_cuadrado,
    "y^2": y_cuadrado,
}

df = pd.DataFrame(data1)


# Objeto suma
sumas = df.sum()

# sumas de las diferentes columnas
suma_x = sumas["x"]
suma_y = sumas["y"]
suma_prod = sumas["x*y"]
suma_x_cua = sumas["x^2"]
suma_y_cua = sumas["y^2"]


# parametros

# Punto de corte

b = ((suma_y * suma_x_cua) - (suma_x * suma_prod)) / (
    (n * suma_x_cua) - (suma_x * suma_x)
)

m = ((n * suma_prod) - (suma_x * suma_y)) / ((n * suma_x_cua) - (suma_x * suma_x))

print(suma_x, suma_y, suma_prod, suma_x_cua, suma_y_cua)

df["Beta_cuadrado"] = df.apply(lambda row: (b + m * row["x"] - row["y"]) ** 2, axis=1)

print(df)


sumas = df.sum()
suma_beta = sumas["Beta_cuadrado"]

resultados = {
    "suma de x": [suma_x],
    "suma de y": [suma_y],
    "suma de x*y": [suma_prod],
    "suma de x^2": [suma_x_cua],
    "suma de y^2": [suma_y_cua],
    "suma de B^2": [suma_beta],
}

df1 = pd.DataFrame(resultados)

print("*" * 60)
print(df1)
print("*" * 60)

error_pendiente = sqrt(
    (n / ((n * suma_x_cua) - (suma_x * suma_x))) * (suma_beta / (n - 2))
)

error_corte = sqrt(
    (suma_x_cua / ((n * suma_x_cua) - (suma_x * suma_x))) * (suma_beta / (n - 2))
)

print("*" * 60)
print(f"El valor de la pendiente es {m}")
print(f"El valor del corte es {b}")
print("*" * 60)
print(f"El margen de error de la pendientes es {error_pendiente:.4f}")
print(f"El margen de error del corte es {error_corte:.4f}")
print("*" * 60)

eje_x = np.linspace(0, 14, 10)

fx = lambda x: m * x + b

eje_y = fx(eje_x)

# plotea la figuras en una sola
fig, ax = plt.subplots()
plt.plot(eje_x, eje_y)
ax.scatter(x=x, y=y)  # Puntos
plt.grid()
plt.show()
