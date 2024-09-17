import numpy as np
from sympy import symbols, sin, cos, Matrix
import pandas as pd

# Definición de los símbolos
v2, t2, t3 = symbols("v2 t2 t3")

# Definición de las expresiones de las funciones p2, p3 y q2
p2 = v2 * (10 * sin(t2) + 4 * sin(t2 - t3))
p3 = 5 * sin(t2) + 4 * v2 * sin(t3 - t2)
q2 = 13 * v2 * 2 - v2 * (10 * cos(t2) + 4 * sin(t2 - t3))

# Cálculo de la matriz Jacobiana
J = Matrix([p2, p3, q2]).jacobian([v2, t2, t3])

# Inicialización de variables y listas
xp = np.array([[1], [0], [0]])  # Aproximación inicial
err = 0.001  # Tolerancia de error
f = np.zeros((3, 1))  # Vector de evaluaciones de las funciones
errores = []  # Lista para almacenar los errores en cada iteración
Fin = False

# Proceso de iteración
while not Fin:
    # Evaluación de las funciones y la matriz Jacobiana en el punto actual
    f[0][0] = p2.subs({v2: xp[0][0], t2: xp[1][0], t3: xp[2][0]})
    f[1][0] = p3.subs({v2: xp[0][0], t2: xp[1][0], t3: xp[2][0]})
    f[2][0] = q2.subs({v2: xp[0][0], t2: xp[1][0], t3: xp[2][0]})
    J_eval = np.array(J.subs({v2: xp[0][0], t2: xp[1][0], t3: xp[2][0]}), dtype=float)

    # Cálculo de la nueva aproximación
    J_pseudo_inv = np.linalg.pinv(J_eval)
    xpk = xp
    xp = np.add(xp, np.dot(-1 * J_pseudo_inv, f))  # productos de los vectores .dot

    # Cálculo del error y almacenamiento en la lista de errores
    error = np.linalg.norm(np.add(xp, -1 * xpk))
    errores.append(error)

    # Comprobación de la condición de terminación
    if error <= err:
        terminado = True

# Creación con los resultados
datos = pd.DataFrame(
    {
        "Error": errores,
        "V2": [xp[0][0]],
        "t2": [xp[1][0]],
        "t3": [xp[2][0]],
        "p2": [f[0][0]],
        "p3": [f[1][0]],
        "q2": [f[2][0]],
    }
)
print(datos)
