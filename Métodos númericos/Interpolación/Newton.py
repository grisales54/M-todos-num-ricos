from sympy import *
import pprint  # IMPRIME BONITO
import numpy as np
import matplotlib.pyplot as plt


n = int(input("Ingrese el número de elementos: "))

i = 0
j = 0

# eje_x = [28.5, 29.86, 30.7, 31.84, 32.82]
# y = [6.23, 6.68, 6.67, 6.95, 7.53]

eje_x = []
y = []

print("-" * 30)  # Separador
while i < n:  # Ingresan los valores de x a una lista

    v1 = float(input(f"Ingrese el valor {i} de x: "))
    i = i + 1
    eje_x.append(v1)

print("-" * 30)

while j < n:  # Ingresa los valores de y a una lista

    v2 = float(input(f"Ingrese el valor {j} de y: "))
    j = j + 1
    y.append(v2)


coef = y.copy()

final = []

for i in range(1, n):
    polinomio = []
    final.append(polinomio)
    for j in range(n - i):

        coef[j] = (coef[j + 1] - coef[j]) / (
            eje_x[i + j] - eje_x[j]
        )  # diferencias dividas

        polinomio.append(coef[j])

    # print(["{:.2f}".format(num) for num in polinomio], end=",")  # formato dos decimales

    print()

for i in range(
    len(final)
):  # Ciclo corto para formatear con dos decimales cada elemento de las listas

    for j in range(len(final[i])):
        final[i][j] = round(
            final[i][j], 2
        )  # Muestra el resultado con dos decimales, siguen siendo un float


lista_traspuesta = []


for i in range(
    len(max(final, key=len))
):  # Este condinal encuentra la lista de mayor longitud
    fila = []
    for lista in final:
        if i < len(lista):
            fila.append(lista[i])
        else:
            pass
    lista_traspuesta.append(fila)


# Mostrar la lista traspuesta

for fila in lista_traspuesta:
    print(fila)


equis = symbols("x")

faprox = y[0]


for k in range(0, n - 1, 1):

    prod = 1

    for j in range(0, k + 1, 1):
        prod *= equis - eje_x[j]

    faprox += lista_traspuesta[0][k] * prod


print(faprox)

x_1 = sympify(faprox)
x = symbols("x")

eje_x = np.arange(0, 3, 0.01)

feje_x = [x_1.subs(x, value) for value in eje_x]

# feje_x = x_1.subs(x, eje_x)
# Imprime los elementos de una lista, con un '+ ' entre cada valor de lista

plt.plot(eje_x, feje_x)
plt.grid()
plt.show()
