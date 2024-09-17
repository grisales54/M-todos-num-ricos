import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x**3 + 2 * x + 3

n = int(
    input("Ingrese el número de intervalos: ")
)  # Número de intervalos en los cuales vamos a dividir la región

suma_areas = 0
vector = []  # áreas bajo la curva

a = float(input("Límite inferior: "))
b = float(input("Límite superior: "))

x_curva = np.linspace(
    a, b, 10
)  # Tocá definir desde aquí ya que a cambia en el ciclo for
y_curva = fx(x_curva)

espesor = (b - a) / n

for i in range(n):  # cuenta desde 0 hasta n-1

    h = fx(a)  # altura

    area = espesor * h  # base por altura
    vector.append(area)  # área bajo la curva

    suma_areas = suma_areas + abs(area)

    a = a + espesor

print(round(suma_areas, 3))


x = np.linspace(0, 10, 100)
y = fx(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, "b", linewidth=2)
plt.fill_between(x_curva, 0, y_curva, color="lightblue", alpha=0.5)
plt.title("Área bajo la curva usando la regla del rectagulo")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
