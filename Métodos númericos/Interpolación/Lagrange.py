from sympy import *

n = int(input("Ingrese el número de elementos: "))

i = 0
j = 0

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


i = list(range(n))  # rangos de I y J
j = list(range(n))

polinomio = []


for q in range(n):  # Número de iteraciones

    for k in range(n - 1):  # Condición de la productoria n-1

        x = symbols("x")

        if i[q] in j:  # Crea sub listas para i diferente de j

            lista = j[:]  # Copia lista desde index 0 hasta -1
            lista.remove(i[q])

            productoria = (x - eje_x[lista[k]]) / (
                eje_x[q] - eje_x[lista[k]]
            )  # productoria
            polinomio.append(productoria)

print("-" * 30)

resultados = []
Lagrange = []

for i in range(0, len(polinomio), n - 1):
    if i + 1 < len(polinomio):  # Asegurarse de que hay al menos dos elementos más
        multiplicacion = polinomio[i] * polinomio[i + 1]
        resultados.append(multiplicacion)


for i, j in zip(
    y, resultados
):  # multiplica los valores de Y por cada uno de los polinomios
    multi = i * j
    Lagrange.append(
        str(multi)
    )  # se necesita que sea str para la función join() ya que es objeto sympy

Final = "+".join(Lagrange)  # une los elementos de una lista con un + entre cada uno

print("-" * 30)
print(Final)


# j= (0,1,2)

# y=(3,2,1)

# i=0 , j=(1,2)

# y[j[]]
