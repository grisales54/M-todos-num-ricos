import numpy as np
import matplotlib.pyplot as plt


def regla_trapecio(x, y):
    n = len(x) - 1
    a = x[0]  # Punto inicial
    b = x[n]  # Punto final
    yn = y[n]
    suma = sum(y) - yn - y[0]  # Resto el punto final y el punto inicial
    area = round(
        (b - a) * (y[0] + 2 * suma + yn) / (2 * n), 4
    )  # Fórmula área total polinomio, redondeando 4 cifras decimales
    return area


print("*" * 50)
a = float(input("Ingrese el límite inferior: "))
b = float(input("Ingre el límite superior: "))
n = int(input("Ingrese el número de subintervalos: "))
print("*" * 50)


x = np.linspace(
    a, b, n + 1
)  # creamos un vector desde a hasta b divido n puntos de manera igual
y = (
    -0.27 * (x - 23.35) * (x - 22.08) * (x - 21.77)
    + 0.51 * (x - 22.08) * (x - 21.77)
    + 3.06
)

area = regla_trapecio(x, y)
print(f"El área bajo la curva usando la regla del trapecio es: {area}")

# Graficar la curva y el área
plt.figure(figsize=(10, 6))
plt.plot(x, y, "b", linewidth=2)
plt.fill_between(x, 0, y, color="lightblue", alpha=0.5)
plt.title("Área bajo la curva usando la regla del trapecio")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
